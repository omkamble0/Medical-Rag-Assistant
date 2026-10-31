"""
Medical-Aware Content Chunker for AegisMed Clinical Truth Engine.
Chunks clinical text and disease records by section, evidence level,
clinical guideline, trial data, and contraindications with deterministic chunk IDs.
"""

import re
import hashlib
from typing import List, Dict, Any, Optional
from app.interfaces.retriever import RetrievedChunk
from app.models.medical_db_schemas import DiseaseRecord


class MedicalContentChunker:
    """
    Splits clinical records into semantic, citation-aware chunks:
    - By section: indications, pathophysiology, GDMT, clinical trials, contraindications, red flags
    - By evidence level: Level 1 (Meta-Analyses), Level 2 (RCTs), Level 5 (Consensus Guidelines)
    - With deterministic UUIDs / chunk IDs for audit traceability.
    """

    def __init__(self, chunk_size: int = 200, chunk_overlap: int = 20):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(
        self,
        text: str,
        doc_id: str,
        title: str,
        evidence_level: str = "Level 1",
        domain: str = "GENERAL_MEDICINE"
    ) -> List[RetrievedChunk]:
        """Chunks clinical text by section headers or sentence blocks."""
        section_pattern = r"(CONTRAINDICATIONS|ADVERSE REACTIONS|DOSAGE AND ADMINISTRATION|INDICATIONS|WARNINGS):"
        splits = re.split(section_pattern, text)
        
        chunks: List[RetrievedChunk] = []
        if len(splits) > 1:
            i = 0
            if splits[0].strip():
                chunks.append(RetrievedChunk(
                    chunk_id=f"CHK-{doc_id}-0",
                    document_id=doc_id,
                    title=f"{title} - Overview",
                    evidence_level=evidence_level,
                    section_name="overview",
                    domain=domain,
                    text=splits[0].strip(),
                    relevance_score=0.9
                ))
                i = 1
            while i < len(splits) - 1:
                sec_name = splits[i].strip()
                sec_body = splits[i+1].strip()
                c_id = f"CHK-{doc_id}-{sec_name.lower().replace(' ', '_')}"
                is_contra = "contraindication" in sec_name.lower() or "contraindication" in sec_body.lower()
                chunks.append(RetrievedChunk(
                    chunk_id=c_id,
                    document_id=doc_id,
                    title=f"{title} - {sec_name}",
                    evidence_level=evidence_level,
                    section_name=sec_name.lower(),
                    domain=domain,
                    text=f"{sec_name}: {sec_body}",
                    relevance_score=0.95,
                    is_contraindication=is_contra,
                    metadata={"section": sec_name}
                ))
                i += 2
        else:
            return self.chunk_raw_text(text, doc_id, title, evidence_level)

        return chunks

    @staticmethod
    def chunk_disease_record(record: DiseaseRecord) -> List[RetrievedChunk]:
        """Decomposes a structured DiseaseRecord into discrete citation-tagged chunks."""
        chunks: List[RetrievedChunk] = []

        # 1. Overview & Pathophysiology Chunk
        if record.overview:
            c_id = f"CHK-{record.id}-OVERVIEW"
            chunks.append(
                RetrievedChunk(
                    chunk_id=c_id,
                    document_id=record.id,
                    title=f"{record.name} - Clinical Overview & Pathophysiology",
                    journal="AegisMed Clinical Compendium",
                    year=2024,
                    evidence_level="Level 1",
                    section_name="overview",
                    text=f"{record.name} ({record.icd10_code}): {record.overview}",
                    relevance_score=1.0,
                    metadata={
                        "organ_system": record.organ_system,
                        "specialty": record.specialty,
                        "icd10": record.icd10_code
                    }
                )
            )

        # 2. Patient Plain English & Analogy Chunk
        if record.patient_plain_language:
            c_id = f"CHK-{record.id}-PATIENT-EXPLANATION"
            chunks.append(
                RetrievedChunk(
                    chunk_id=c_id,
                    document_id=record.id,
                    title=f"{record.name} - Plain-Language Explanation & Analogy",
                    journal="Patient Education Review",
                    year=2024,
                    evidence_level="Level 5",
                    section_name="patient_explanation",
                    text=record.patient_plain_language,
                    relevance_score=1.0,
                    metadata={"audience": "patient", "specialty": record.specialty}
                )
            )

        # 3. Treatment Solutions Chunks (by line of therapy)
        for idx, sol in enumerate(record.solutions, start=1):
            c_id = f"CHK-{record.id}-SOL-{sol.id or idx}"
            sol_text = (
                f"Treatment Protocol ({sol.line_of_therapy.replace('_', ' ').title()} - {sol.type.title()}): {sol.name}. "
                f"Description: {sol.description}. Dosage/Protocol: {sol.dosage_or_protocol}. "
                f"Contraindications: {', '.join(sol.contraindications) if sol.contraindications else 'None noted'}. "
                f"Monitoring: {sol.monitoring or 'Routine surveillance'}."
            )
            chunks.append(
                RetrievedChunk(
                    chunk_id=c_id,
                    document_id=record.id,
                    title=f"{record.name} Therapy - {sol.name}",
                    journal="Clinical Pharmacotherapy Guidelines",
                    year=2024,
                    evidence_level="Level 1" if sol.line_of_therapy == "first_line" else "Level 2",
                    section_name="pharmacotherapy" if sol.type == "pharmacological" else "lifestyle",
                    text=sol_text,
                    relevance_score=0.95,
                    metadata={
                        "contraindications": sol.contraindications,
                        "side_effects": sol.side_effects,
                        "line_of_therapy": sol.line_of_therapy
                    }
                )
            )

        # 4. Landmark Research Papers Chunks (RCTs / Systematic Reviews)
        for p_idx, paper in enumerate(record.research_papers, start=1):
            c_id = f"CHK-{record.id}-TRIAL-{paper.id or p_idx}"
            trial_text = (
                f"Clinical Trial ({paper.cebm_level}): {paper.title} published in {paper.journal} ({paper.year}). "
                f"Study Design: {paper.study_design}. Sample size: {paper.sample_size or 'Standard Cohort'}. "
                f"Key Findings: {paper.key_findings}. Clinical Takeaway: {paper.clinical_takeaway}."
            )
            chunks.append(
                RetrievedChunk(
                    chunk_id=c_id,
                    document_id=record.id,
                    title=paper.title,
                    journal=paper.journal,
                    year=paper.year,
                    evidence_level=paper.cebm_level,
                    section_name="clinical_trial",
                    text=trial_text,
                    relevance_score=0.98,
                    metadata={
                        "doi_or_pmid": paper.doi_or_pmid,
                        "study_design": paper.study_design,
                        "cebm_level": paper.cebm_level
                    }
                )
            )

        # 5. Red Flags & Critical Warnings Chunk
        if record.red_flags:
            c_id = f"CHK-{record.id}-RED-FLAGS"
            rf_text = f"Emergency Red Flags for {record.name}: " + "; ".join(record.red_flags)
            chunks.append(
                RetrievedChunk(
                    chunk_id=c_id,
                    document_id=record.id,
                    title=f"{record.name} - Emergency Red Flags & Triage Criteria",
                    journal="Emergency Medicine Triage Consensus",
                    year=2024,
                    evidence_level="Level 1",
                    section_name="contraindication_and_emergency",
                    text=rf_text,
                    relevance_score=1.0,
                    metadata={"is_emergency_criteria": True}
                )
            )

        return chunks

    @staticmethod
    def chunk_raw_text(
        text: str,
        document_id: str,
        title: str,
        evidence_level: str = "Level 2"
    ) -> List[RetrievedChunk]:
        """Chunks unstructured medical guideline text by headings or semantic paragraphs."""
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n|(?=###\s+)", text) if len(p.strip()) > 40]
        chunks: List[RetrievedChunk] = []

        for idx, para in enumerate(paragraphs, start=1):
            h = hashlib.sha256(para.encode("utf-8")).hexdigest()[:8]
            c_id = f"CHK-{document_id}-P{idx}-{h}"
            chunks.append(
                RetrievedChunk(
                    chunk_id=c_id,
                    document_id=document_id,
                    title=f"{title} (Section {idx})",
                    evidence_level=evidence_level,
                    section_name="guideline_section",
                    text=para,
                    relevance_score=0.90,
                    metadata={"paragraph_index": idx}
                )
            )
        return chunks

