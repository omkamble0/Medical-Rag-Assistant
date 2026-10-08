"""
AegisMed Admin Endpoints for Dynamic Clinical Knowledge Ingestion
Allows querying corpus statistics, importing new diseases from PubMed, and adding custom verified papers.
"""

from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.services.knowledge_manager import bulk_import_diseases, add_documents, load_imported_documents
from app.services.vector_store import get_corpus_stats, refresh_indexes
from app.models.enums import EvidenceLevel

router = APIRouter(prefix="/admin", tags=["Knowledge Administration"])


class BulkImportRequest(BaseModel):
    diseases: List[str] = Field(..., description="List of disease or medical condition names to import")
    max_papers_per_disease: int = Field(default=2, ge=1, le=5, description="Max verified papers to fetch per disease")


class AddPaperRequest(BaseModel):
    id: str = Field(..., description="Unique paper identifier, e.g. DOC-CUSTOM-01")
    domain: str = Field(..., description="Specialty domain, e.g. NEUROLOGY, ONCOLOGY")
    disease: Optional[str] = None
    title: str
    journal: str
    year: int
    doi_or_pmid: str
    evidence_level: EvidenceLevel = EvidenceLevel.LEVEL_1
    keywords: List[str]
    snippet: str
    key_takeaway: str


@router.get("/knowledge/stats")
async def get_knowledge_stats():
    """Returns total count and domain distribution of indexed clinical papers."""
    return get_corpus_stats()


@router.post("/knowledge/import")
async def import_diseases_endpoint(payload: BulkImportRequest):
    """
    Triggers automated ingestion of PubMed & Europe PMC verified papers for the requested diseases.
    """
    if not payload.diseases:
        raise HTTPException(status_code=400, detail="Please provide at least one disease name.")

    result = await bulk_import_diseases(
        diseases=payload.diseases,
        max_papers_per_disease=payload.max_papers_per_disease
    )
    return result


@router.post("/knowledge/add-paper")
async def add_custom_paper_endpoint(paper: AddPaperRequest):
    """Manually adds a verified clinical paper with DOI/PMID and Oxford CEBM grading."""
    doc_dict = paper.dict()
    added = add_documents([doc_dict])
    if added == 0:
        raise HTTPException(status_code=409, detail="Paper with this ID or DOI/PMID already exists.")
    return {"status": "success", "message": f"Successfully indexed {paper.title}"}


@router.post("/knowledge/reindex")
async def reindex_knowledge_endpoint():
    """Forces an immediate rebuild of the BM25 and Dense semantic retrieval indexes."""
    total = refresh_indexes()
    return {"status": "success", "total_indexed_documents": total}
