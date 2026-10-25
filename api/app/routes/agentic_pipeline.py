"""
Agentic Clinical Pipeline & Tools API Endpoints
Exposes the LangGraph multi-agent workflow, CRAG, Self-RAG, and standalone clinical tools.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

from app.services.agent_workflow import execute_agentic_rag_workflow
from app.services.tools.clinical_calculator import (
    calculate_egfr, calculate_bmi, calculate_cha2ds2_vasc, calculate_wells_pe, calculate_curb65
)
from app.services.tools.drug_interaction import check_drug_interactions, screen_single_drug_safety
from app.services.tools.pubmed_tool import search_pubmed_literature
from app.services.tools.guideline_tool import search_consensus_guidelines
from app.services.llm_gateway import llm_gateway
from app.core.prompts import normalize_audience

router = APIRouter(prefix="/api/v1/agentic", tags=["LangGraph Clinical Multi-Agent"])


class AgenticQueryRequest(BaseModel):
    query: str = Field(..., description="Clinical inquiry or patient symptoms description")
    audience: str = Field(default="patient", description="'patient' or 'doctor'")


class CalculatorRequest(BaseModel):
    formula: str = Field(..., description="'egfr', 'bmi', 'cha2ds2_vasc', 'wells_pe', or 'curb65'")
    parameters: Dict[str, Any] = Field(..., description="Key-value calculation inputs")


class DDIRequest(BaseModel):
    medications: List[str] = Field(..., description="List of drug names to check for interactions")


class PubMedRequest(BaseModel):
    query: str = Field(..., description="Medical topic or clinical study query")
    max_results: int = Field(default=3, description="Maximum literature items to retrieve")


@router.post("/query", summary="Execute LangGraph Multi-Agent Clinical RAG Workflow")
async def execute_agentic_query_endpoint(payload: AgenticQueryRequest):
    """
    Executes the 7-stage LangGraph multi-agent clinical workflow:
    1. Safety & Emergency Triage Interceptor
    2. Query Deconstruction & MeSH Mapping
    3. Autonomous Clinical Tool Execution (DDI, eGFR/BMI Calculator, PubMed)
    4. Vector Evidence Retrieval & CEBM Re-Ranking
    5. Corrective RAG (CRAG) Relevance Assessment
    6. Audience-Aware Synthesis (Patient Grade 6-8 vs Clinician Oxford CEBM)
    7. Self-RAG Reflective Hallucination & Citation Grounding Audit
    """
    try:
        norm_aud = normalize_audience(payload.audience)
        result = execute_agentic_rag_workflow(query=payload.query, audience=norm_aud)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agentic workflow execution error: {str(e)}"
        )


@router.post("/tools/calculate", summary="Execute Clinical Risk & Physiology Calculator")
async def calculate_endpoint(payload: CalculatorRequest):
    """
    Executes peer-reviewed clinical formula calculators:
    - egfr: 2021 CKD-EPI Race-Free equation (creatinine, age, sex)
    - bmi: WHO Body Mass Index & GLP-1 indications (weight_kg, height_cm)
    - cha2ds2_vasc: Atrial Fibrillation Stroke Risk (chf, htn, age, diabetes, stroke_history, vascular_disease, sex)
    - wells_pe: Wells Criteria for Pulmonary Embolism probability
    """
    formula = payload.formula.strip().lower()
    p = payload.parameters

    try:
        if formula in ["egfr", "gfr", "kidney"]:
            return calculate_egfr(
                creatinine=float(p.get("creatinine", 1.0)),
                age=int(p.get("age", 55)),
                sex=str(p.get("sex", "male"))
            )
        elif formula in ["bmi", "weight", "obesity"]:
            return calculate_bmi(
                weight_kg=float(p.get("weight_kg", p.get("weight", 70.0))),
                height_cm=float(p.get("height_cm", p.get("height", 175.0)))
            )
        elif formula in ["cha2ds2_vasc", "afib", "stroke_risk"]:
            return calculate_cha2ds2_vasc(
                chf=bool(p.get("chf", False)),
                htn=bool(p.get("htn", False)),
                age=int(p.get("age", 60)),
                diabetes=bool(p.get("diabetes", False)),
                stroke_history=bool(p.get("stroke_history", False)),
                vascular_disease=bool(p.get("vascular_disease", False)),
                sex=str(p.get("sex", "male"))
            )
        elif formula in ["wells_pe", "wells", "pe"]:
            return calculate_wells_pe(
                dvt_signs=bool(p.get("dvt_signs", False)),
                alternative_less_likely=bool(p.get("alternative_less_likely", False)),
                hr_over_100=bool(p.get("hr_over_100", False)),
                immobility=bool(p.get("immobility", False)),
                prior_pe_dvt=bool(p.get("prior_pe_dvt", False)),
                hemoptysis=bool(p.get("hemoptysis", False)),
                active_cancer=bool(p.get("active_cancer", False))
            )
        elif formula in ["curb65", "curb_65", "pneumonia"]:
            age_val = int(p.get("age", 0))
            return calculate_curb65(
                confusion=bool(p.get("confusion", False)),
                bun_over_19=bool(p.get("bun_over_19", p.get("urea", False))),
                rr_over_30=bool(p.get("rr_over_30", False)),
                sbp_under_90_or_dbp_under_60=bool(p.get("sbp_under_90_or_dbp_under_60", p.get("hypotension", False))),
                age_over_65=bool(p.get("age_over_65", age_val >= 65))
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unknown calculator '{formula}'. Supported: 'egfr', 'bmi', 'cha2ds2_vasc', 'wells_pe', 'curb65'"
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Calculation failed: {str(e)}"
        )


@router.post("/tools/check-ddi", summary="Execute Drug-Drug Interaction and Safety Screening")
async def check_ddi_endpoint(payload: DDIRequest):
    """
    Screens pharmaceutical combinations for CYP450 conflicts, Black Box warnings,
    and organ clearance contraindications.
    """
    try:
        return check_drug_interactions(payload.medications)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"DDI screening error: {str(e)}"
        )


@router.post("/tools/pubmed", summary="Query PubMed / NCBI Clinical Trials")
async def pubmed_search_endpoint(payload: PubMedRequest):
    """
    Searches PubMed literature with Oxford CEBM evidentiary grading.
    """
    try:
        return search_pubmed_literature(payload.query, max_results=payload.max_results)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"PubMed search error: {str(e)}"
        )


@router.get("/providers", summary="Get Active GenAI LLM Provider Status")
async def get_providers_endpoint():
    """
    Returns runtime LLM provider status (OpenAI, Groq, Gemini, Ollama, Local).
    """
    return llm_gateway.get_active_provider_info()
