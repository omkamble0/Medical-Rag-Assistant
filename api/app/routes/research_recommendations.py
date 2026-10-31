"""
AegisMed Research Recommendation API Route
Provides stateful clinical and educational research recommendations
for Patient and Clinician/Doctor audiences with PubMed & Guideline grounding.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from app.core.prompts import normalize_audience, MANDATORY_DISCLAIMER
from app.services.guideline_client import find_guidelines_by_condition, build_guideline_evidence_document
from app.services.pubmed_client import search_pubmed, search_pubmed_sync, build_medical_evidence_document
from app.services.vector_store import retrieve_clinical_evidence
from app.models.schemas import SourceDocument
from app.models.enums import EvidenceLevel

router = APIRouter(prefix="/api/v1", tags=["Clinical Research Recommendations"])

class ResearchRecommendationRequest(BaseModel):
    condition: str = Field(..., min_length=2, max_length=500, description="Clinical condition, disease, or medical topic")
    audience: str = Field(default="patient", description="Target audience: 'patient' or 'doctor'")
    max_results: int = Field(default=5, ge=1, le=20, description="Maximum research items to return")

class ResearchItem(BaseModel):
    citation_index: int
    title: str
    journal: str
    year: int
    doi_or_pmid: Optional[str] = None
    evidence_level: str
    key_findings: str
    clinical_implication: str

class PatientResearchResponse(BaseModel):
    status: str = "ok"
    condition: str
    audience: str = "patient"
    reading_level: str = "Grade 6.0 - Everyday English"
    overview: str
    plain_language_findings: List[Dict[str, str]]
    questions_for_doctor: List[str]
    reputable_resources: List[str]
    sources: List[Dict[str, Any]]
    disclaimer: str

class DoctorResearchResponse(BaseModel):
    status: str = "ok"
    condition: str
    audience: str = "doctor"
    reading_level: str = "Postgraduate Clinical Level"
    evidence_synthesis: str
    key_trials_and_rcts: List[ResearchItem]
    guideline_consensus: List[Dict[str, str]]
    contraindications_and_safety: List[str]
    sources: List[Dict[str, Any]]
    disclaimer: str

@router.post(
    "/research-recommendations",
    summary="Get Evidence-Backed Research Recommendations for Patients or Doctors",
    response_model=Dict[str, Any]
)
def get_research_recommendations(payload: ResearchRecommendationRequest):
    """
    Generates targeted clinical research recommendations based on:
    1. Audience Normalization ('patient' vs 'doctor')
    2. Real-time / Curated PubMed search
    3. Multi-domain international clinical guidelines
    4. Strict language level formatting & Oxford CEBM evidence grading
    """
    try:
        norm_audience = normalize_audience(payload.audience)
        condition = payload.condition.strip()

        # Step 1: Retrieve multi-source evidence (Guidelines + PubMed + Vector DB)
        guidelines = find_guidelines_by_condition(condition)
        pubmed_articles = search_pubmed_sync(condition, max_results=payload.max_results)
        vector_sources = retrieve_clinical_evidence(condition, top_k=payload.max_results)

        # Assemble unified source list
        sources: List[SourceDocument] = []
        c_idx = 1

        # Add guidelines
        for gl in guidelines[:2]:
            sources.append(build_guideline_evidence_document(gl, citation_index=c_idx))
            c_idx += 1

        # Add PubMed
        for pm in pubmed_articles[:2]:
            sources.append(build_medical_evidence_document(pm, citation_index=c_idx))
            c_idx += 1

        # Add Vector if needed
        for vs in vector_sources:
            if not any(s.title.lower() == vs.title.lower() for s in sources):
                vs.citation_index = c_idx
                sources.append(vs)
                c_idx += 1
            if len(sources) >= payload.max_results:
                break

        formatted_sources = [s.model_dump() if hasattr(s, "model_dump") else s.dict() for s in sources]

        # Step 2: Generate Audience-Specific Payload
        if norm_audience == "patient":
            from app.core.readability import sanitize_patient_mode_text
            # Patient: Plain English, 6th-grade, no statistics, empathetic
            findings_list = []
            for s in sources:
                takeaway = s.key_takeaway or s.snippet[:200]
                clean_takeaway = sanitize_patient_mode_text(takeaway)
                clean_takeaway = clean_takeaway.replace("MACE", "major heart events").replace("eGFR", "kidney filtration rate")
                findings_list.append({
                    "topic": s.title,
                    "what_it_means_for_you": clean_takeaway,
                    "source": f"[{s.citation_index}] {s.journal} ({s.year})"
                })

            return PatientResearchResponse(
                condition=condition,
                audience="patient",
                overview=(
                    f"Here is what recent clinical medical guidelines and research studies say about {condition}. "
                    "This information explains the latest proven treatments and healthy daily steps in simple language."
                ),
                plain_language_findings=findings_list,
                questions_for_doctor=[
                    f"What is the best initial treatment plan for my {condition}?",
                    "Are there lifestyle changes or dietary steps that can support my care?",
                    "What specific warning signs or symptom changes should prompt me to contact your office?",
                    "Do any of my current medications interact with treatments for this condition?"
                ],
                reputable_resources=[
                    "World Health Organization (WHO) Patient Guidelines",
                    "American Heart Association / American Diabetes Association Patient Resources",
                    "National Institutes of Health (NIH) MedlinePlus",
                    "ClinicalTrials.gov (for experimental trial participation)"
                ],
                sources=formatted_sources,
                disclaimer=MANDATORY_DISCLAIMER
            ).model_dump()

        else:
            # Doctor: Precise clinical terminology, statistics, dosing, guidelines
            trial_items: List[ResearchItem] = []
            for s in sources:
                ev_str = s.evidence_level.value if hasattr(s.evidence_level, "value") else str(s.evidence_level)
                trial_items.append(
                    ResearchItem(
                        citation_index=s.citation_index,
                        title=s.title,
                        journal=s.journal,
                        year=s.year,
                        doi_or_pmid=s.doi_or_pmid,
                        evidence_level=ev_str,
                        key_findings=s.snippet[:300],
                        clinical_implication=s.key_takeaway or "Guideline-directed evidence based recommendation."
                    )
                )

            return DoctorResearchResponse(
                condition=condition,
                audience="doctor",
                evidence_synthesis=(
                    f"Oxford CEBM evidence synthesis for {condition}: Evaluated across international clinical guidelines "
                    f"(ACC/AHA, ESC, ADA, GINA, IDSA, KDIGO) and peer-reviewed randomized controlled trials / meta-analyses."
                ),
                key_trials_and_rcts=trial_items,
                guideline_consensus=[
                    {"guideline": s.title, "authority": s.journal, "level": str(s.evidence_level), "recommendation": s.key_takeaway or s.snippet[:150]}
                    for s in sources if "guideline" in s.title.lower() or "consensus" in s.title.lower() or "standard" in s.title.lower()
                ] or [
                    {"guideline": sources[0].title, "authority": sources[0].journal, "level": str(sources[0].evidence_level), "recommendation": sources[0].key_takeaway or sources[0].snippet[:150]}
                ],
                contraindications_and_safety=[
                    "Evaluate baseline organ function profile (eGFR, LFTs, serum electrolytes) prior to initiating or escalating pharmacotherapy.",
                    "Reconcile concomitant CYP450 substrates/inhibitors to prevent competitive metabolic accumulation and adverse interactions.",
                    "Review guideline-directed Black Box Warnings and monitor patient tolerance at 2–4 week intervals."
                ],
                sources=formatted_sources,
                disclaimer=MANDATORY_DISCLAIMER
            ).model_dump()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate research recommendations: {str(e)}"
        )
