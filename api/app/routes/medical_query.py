from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from app.services.query_guard import QueryGuard
from app.services.rag_agent import MedicalRAGAgent
from app.services.agent_workflow import execute_agentic_rag_workflow
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["Medical Agentic RAG"])

guard = QueryGuard()
rag = MedicalRAGAgent()

def normalize_audience(audience: str) -> str:
    """
    Normalize audience value to canonical forms: 'patient' or 'doctor'.
    Maps variations like 'clinician', 'professional', 'physician', 'md' → 'doctor'.
    Defaults to 'patient' if None or unrecognized.
    """
    if audience is None:
        return "patient"
    
    a = str(audience).strip().lower()
    
    # Map all doctor variants to single canonical value
    if a in {"doctor", "clinician", "professional", "physician", "md", "healthcare_provider"}:
        return "doctor"
    
    # Default to patient for safety
    return "patient"

class QueryRequest(BaseModel):
    query: str = Field(..., description="User medical query or symptoms description")
    audience: str = Field(default="patient", description="Target audience: 'patient' or 'doctor'")
    auto_correct: bool = Field(default=False, description="Automatically apply correction without user confirmation if true")

class ValidateQueryRequest(BaseModel):
    query: str

@router.post("/validate-query", summary="Interactive Typo & Medical Terminology Validation")
async def validate_query_endpoint(payload: ValidateQueryRequest):
    """
    Validates a query, detects medical typos (e.g. 'headavhe' -> 'headache'),
    and returns suggested corrections and confidence scores.
    """
    try:
        from app.services.query_validator import validator
        return validator.validate_and_correct(payload.query)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Validation failed: {str(e)}"
        )

@router.post("/medical-query", summary="Execute Agentic Medical RAG with Audience Routing")
async def medical_query_endpoint(payload: QueryRequest):
    """
    Agentic Medical Pipeline:
    1. Normalize audience to 'patient' or 'doctor'
    2. Query Validation Layer: Detects and flags typos
    3. Needs Correction check: Prompts user or applies auto-correction
    4. Retrieval Layer: Context fetched from clinical evidence store
    5. Generation Layer: Generates patient-tailored or doctor-tailored synthesis with sources
    
    STRICT AUDIENCE ENFORCEMENT:
    - patient: 6th-grade reading level, plain English, no jargon
    - doctor: graduate-level clinical terminology, statistics, dosing, trial endpoints
    """
    try:
        # CRITICAL: Normalize audience before any processing
        normalized_audience = normalize_audience(payload.audience)
        
        validation = guard.validate(payload.query)

        # If typo detected and user has not opted into auto_correct, prompt user
        if validation["needs_correction"] and not payload.auto_correct:
            return {
                "status": "needs_correction",
                "original": validation["original"],
                "corrected": validation["corrected"],
                "confidence": validation["confidence"],
                "corrections": validation["corrections"],
                "message": f"Did you mean '{validation['corrected']}'?"
            }

        effective_query = validation["corrected"] if validation["needs_correction"] else payload.query
        
        # Execute LangGraph Multi-Agent RAG Workflow with fallback
        try:
            workflow_res = execute_agentic_rag_workflow(effective_query, audience=normalized_audience)
            answer_text = workflow_res.get("answer", "")
            sources = workflow_res.get("sources", [])
            formatted_sources = [
                {
                    "index": s.get("citation_index", i + 1),
                    "title": s.get("title"),
                    "journal": s.get("journal"),
                    "year": s.get("year"),
                    "evidence_level": s.get("evidence_level", "Level 1"),
                    "snippet": s.get("content") or s.get("snippet", ""),
                    "key_takeaway": s.get("key_takeaway")
                }
                for i, s in enumerate(sources)
            ]
            trace = workflow_res.get("execution_trace", [])
            tool_results = workflow_res.get("tool_results", {})
            crag_grade = workflow_res.get("crag_grade")
            grounding_audit = workflow_res.get("grounding_audit")
            triage_alert = workflow_res.get("triage_alert")
            provider_name = workflow_res.get("provider_info", {}).get("active_provider", "LangGraph Clinical Multi-Agent")
        except Exception as workflow_err:
            logger.warning(f"Workflow execution fell back to basic generator: {workflow_err}")
            response = rag.generate(effective_query, audience=normalized_audience)
            answer_text = response["answer"]
            formatted_sources = response["sources"]
            trace = []
            tool_results = {}
            crag_grade = None
            grounding_audit = None
            triage_alert = None
            provider_name = response.get("provider", "Clinical RAG Agent")

        return {
            "status": "ok",
            "original_query": payload.query,
            "effective_query": effective_query,
            "was_corrected": validation["needs_correction"],
            "answer": answer_text,
            "sources": formatted_sources,
            "audience": normalized_audience,  # NORMALIZED: always 'patient' or 'doctor'
            "reading_level": "Grade 6.0 - Everyday English" if normalized_audience == "patient" else "Postgraduate Clinical Level",
            "provider": provider_name,
            "execution_trace": trace,
            "tool_results": tool_results,
            "crag_grade": crag_grade,
            "grounding_audit": grounding_audit,
            "triage_alert": triage_alert
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Medical RAG processing error: {str(e)}"
        )
