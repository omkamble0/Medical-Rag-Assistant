"""
AegisMed Medical Knowledge Database REST API Router
Exposes comprehensive endpoints for diseases, symptoms, clinical solutions,
peer-reviewed research papers, and the multi-symptom differential diagnosis checker.
"""

from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

from app.models.medical_db_schemas import (
    DiseaseRecord, SymptomCheckerRequest, SymptomCheckerResponse,
    DatabaseStatsResponse
)
from app.services.medical_db import medical_db

router = APIRouter(
    prefix="/api/v1/database",
    tags=["Internal Medical Knowledge Base"],
    include_in_schema=False  # Hidden from public OpenAPI documentation as private proprietary database
)


class HybridSearchRequest(BaseModel):
    query: str = Field(..., min_length=2, max_length=500, description="Semantic or clinical query")
    top_k: int = Field(default=5, ge=1, le=20, description="Maximum matches to return")


@router.get("/stats", response_model=DatabaseStatsResponse, summary="Get Medical Database Statistics")
async def get_database_stats():
    """
    Returns summary statistics for the medical knowledge database:
    - Total conditions, symptoms, solutions, and research papers
    - Distribution across 14 medical specialties
    - Oxford CEBM evidence level breakdown
    - Embedded Qdrant vector store collection status
    """
    try:
        return medical_db.get_stats()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch database statistics: {str(e)}"
        )


@router.get("/diseases", response_model=List[DiseaseRecord], summary="List and Search Disease Records")
async def list_diseases(
    query: Optional[str] = Query(None, description="Search term for condition name, ICD-10, symptom, or treatment"),
    specialty: Optional[str] = Query(None, description="Filter by specialty (e.g. Cardiovascular, Pulmonology, Neurology)"),
    organ_system: Optional[str] = Query(None, description="Filter by organ system (e.g. Circulatory, Respiratory)"),
    limit: int = Query(20, ge=1, le=100, description="Page size limit"),
    offset: int = Query(0, ge=0, description="Offset for pagination")
):
    """
    Retrieves disease monographs with filtering and full-text keyword ranking.
    """
    try:
        return medical_db.get_diseases(
            query=query,
            specialty=specialty,
            organ_system=organ_system,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to search diseases: {str(e)}"
        )


@router.get("/diseases/{disease_id}", response_model=DiseaseRecord, summary="Get Full Clinical Disease Monograph")
async def get_disease_by_id(disease_id: str):
    """
    Retrieves complete 360° clinical profile for a single disease:
    - ICD-10 code, overview, patient plain-language analogy
    - Granular symptoms with severity & frequencies
    - Pharmacological & non-pharmacological solutions with dosing and contraindications
    - Landmark peer-reviewed clinical trials (NEJM, Lancet, JAMA) with Oxford CEBM levels
    - Emergency red flags & doctor consultation checklist
    """
    record = medical_db.get_disease_by_id(disease_id)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Condition with ID '{disease_id}' was not found in the medical database."
        )
    return record


@router.get("/symptoms", summary="Browse All Indexed Medical Symptoms")
async def list_symptoms(
    query: Optional[str] = Query(None, description="Filter symptom by keyword"),
    limit: int = Query(50, ge=1, le=150, description="Max symptoms to return")
):
    """
    Returns unique indexed symptoms across all conditions, including frequency,
    severity, and count of associated medical conditions.
    """
    try:
        return medical_db.get_all_symptoms(query=query, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch symptoms: {str(e)}"
        )


@router.post("/symptom-checker", response_model=SymptomCheckerResponse, summary="Execute Symptom Differential Diagnosis Matcher")
async def check_symptoms(payload: SymptomCheckerRequest):
    """
    Primary Symptom-to-Disease Differential Diagnostic Engine:
    - Accepts patient-reported symptoms (e.g. ['chest pressure', 'shortness of breath'])
    - Automatically checks for Tier-1 Red Flag emergency indicators
    - Computes mathematical symptom overlap and hallmark correlation scores (0 - 100%)
    - Returns ranked candidate conditions with matched symptoms, missing symptoms,
      first-line GDMT pharmacological solutions, and supporting research papers.
    """
    try:
        return medical_db.check_symptoms(payload)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Symptom checker analysis failed: {str(e)}"
        )


@router.get("/solutions", summary="Browse Evidence-Backed Solutions & Protocols")
async def list_solutions(
    disease: Optional[str] = Query(None, description="Filter by disease name"),
    type: Optional[str] = Query(None, description="Filter by solution type (pharmacological, lifestyle, procedural)"),
    line_of_therapy: Optional[str] = Query(None, description="Filter by line (first_line, second_line, maintenance)"),
    limit: int = Query(30, ge=1, le=100, description="Max solutions to return")
):
    """
    Retrieves evidence-backed clinical treatments, drug dosages, contraindications,
    and lifestyle protocols across conditions.
    """
    try:
        return medical_db.get_solutions(
            disease_query=disease,
            solution_type=type,
            line_of_therapy=line_of_therapy,
            limit=limit
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch solutions: {str(e)}"
        )


@router.get("/papers", summary="Browse Peer-Reviewed Research Papers & Trials")
async def list_papers(
    disease: Optional[str] = Query(None, description="Filter by disease name or topic"),
    cebm_level: Optional[str] = Query(None, description="Filter by CEBM Level (Level 1, Level 2, etc.)"),
    min_year: Optional[int] = Query(None, description="Filter by minimum publication year"),
    limit: int = Query(30, ge=1, le=100, description="Max papers to return")
):
    """
    Retrieves landmark trials (NEJM, Lancet, JAMA, BMJ) with Oxford CEBM hierarchy grading,
    endpoints, and direct DOI/PMID citation links.
    """
    try:
        return medical_db.get_research_papers(
            disease_query=disease,
            cebm_level=cebm_level,
            min_year=min_year,
            limit=limit
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch research papers: {str(e)}"
        )


@router.post("/search-hybrid", summary="Execute Hybrid Dense Vector Search via Qdrant")
async def search_hybrid_endpoint(payload: HybridSearchRequest):
    """
    Executes dense vector similarity search through Qdrant vector database collection
    over disease profiles, symptoms, solutions, and research papers.
    """
    try:
        return medical_db.search_hybrid(query=payload.query, top_k=payload.top_k)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Hybrid vector search failed: {str(e)}"
        )
