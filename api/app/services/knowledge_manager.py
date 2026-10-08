"""
AegisMed Dynamic Knowledge Base Manager
Handles persistent storage, deduplication, live indexing, and bulk disease importing.
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from app.models.enums import EvidenceLevel
from app.services.pubmed_client import PubMedImporter

# Storage path for persisted imported documents
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
KNOWLEDGE_FILE = DATA_DIR / "imported_knowledge.json"

_pubmed_importer = PubMedImporter()


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_imported_documents() -> List[Dict[str, Any]]:
    """Loads all dynamically imported verified clinical documents from disk."""
    ensure_data_dir()
    if not KNOWLEDGE_FILE.exists():
        return []
    try:
        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ensure enum compatibility
            for item in data:
                if isinstance(item.get("evidence_level"), str):
                    try:
                        item["evidence_level"] = EvidenceLevel(item["evidence_level"])
                    except ValueError:
                        item["evidence_level"] = EvidenceLevel.LEVEL_1
            return data
    except Exception:
        return []


def save_imported_documents(docs: List[Dict[str, Any]]) -> bool:
    """Saves dynamically imported clinical documents to disk."""
    ensure_data_dir()
    try:
        # Convert enums to string for serialization
        serializable = []
        for d in docs:
            item = dict(d)
            if isinstance(item.get("evidence_level"), EvidenceLevel):
                item["evidence_level"] = item["evidence_level"].value
            serializable.append(item)

        with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
            json.dump(serializable, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving imported knowledge: {e}")
        return False


def add_documents(new_docs: List[Dict[str, Any]]) -> int:
    """
    Appends new verified papers without duplicate DOIs or PMIDs.
    Returns the count of newly added documents.
    """
    existing = load_imported_documents()
    existing_ids = {d.get("id") for d in existing}
    existing_dois = {d.get("doi_or_pmid") for d in existing if d.get("doi_or_pmid")}

    added_count = 0
    for doc in new_docs:
        doc_id = doc.get("id")
        doc_doi = doc.get("doi_or_pmid")

        if doc_id in existing_ids or (doc_doi and doc_doi in existing_dois):
            continue

        existing.append(doc)
        existing_ids.add(doc_id)
        if doc_doi:
            existing_dois.add(doc_doi)
        added_count += 1

    if added_count > 0:
        save_imported_documents(existing)
        # Trigger index rebuild
        from app.services.vector_store import refresh_indexes
        refresh_indexes()

    return added_count


async def bulk_import_diseases(
    diseases: List[str],
    max_papers_per_disease: int = 2
) -> Dict[str, Any]:
    """
    Bulk imports verified peer-reviewed research papers for a list of diseases.
    """
    imported_docs: List[Dict[str, Any]] = []
    summary_by_disease: Dict[str, int] = {}

    for disease in diseases:
        clean_name = disease.strip()
        if not clean_name:
            continue
        try:
            papers = await _pubmed_importer.search_and_fetch_disease_papers(
                disease_name=clean_name,
                max_results=max_papers_per_disease
            )
            imported_docs.extend(papers)
            summary_by_disease[clean_name] = len(papers)
        except Exception as e:
            summary_by_disease[clean_name] = 0

    added_count = add_documents(imported_docs)

    return {
        "status": "success",
        "requested_diseases_count": len(diseases),
        "total_papers_fetched": len(imported_docs),
        "new_papers_saved": added_count,
        "disease_breakdown": summary_by_disease
    }
