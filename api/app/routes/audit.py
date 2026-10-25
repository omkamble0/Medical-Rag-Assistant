"""
Clinical Audit & SaMD Traceability API Router for AegisMed.
Exposes endpoints for auditing AI decision support transactions,
inspecting historical reasoning traces, and reviewing clinical quality metrics.
"""

from fastapi import APIRouter, Query, HTTPException, status
from typing import List, Dict, Any, Optional
from app.core.audit_logger import clinical_audit_logger

router = APIRouter(prefix="/api/v1/audit", tags=["Clinical Audit & SaMD Traceability"])


@router.get("/logs", summary="Retrieve Clinical AI Audit Trail Logs")
async def get_audit_logs_endpoint(
    limit: int = Query(default=50, ge=1, le=200, description="Maximum audit records to return"),
    audience: Optional[str] = Query(default=None, description="Filter by audience: 'patient' or 'doctor'"),
    session_id: Optional[str] = Query(default=None, description="Filter by session ID"),
    emergency_only: bool = Query(default=False, description="Filter to acute emergency triage events only")
):
    """
    Returns immutable audit trail entries containing:
    - Audit UUID & ISO 8601 UTC timestamp
    - Inbound and effective query
    - Triage alert status
    - Retrieved Oxford CEBM source IDs & evidence levels
    - DDI contraindications detected
    - Flesch-Kincaid reading level & Self-RAG grounding score
    """
    try:
        logs = clinical_audit_logger.query_audit_trail(
            limit=limit,
            session_id=session_id,
            audience=audience,
            emergency_only=emergency_only
        )
        return {
            "status": "ok",
            "total_records": len(logs),
            "logs": logs
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to query audit trail: {str(e)}"
        )


@router.get("/metrics", summary="Retrieve Clinical Quality & Safety Audit Metrics")
async def get_audit_metrics_endpoint():
    """
    Returns aggregate clinical governance and safety metrics:
    - Total clinical transactions processed
    - Emergency triage interceptions count
    - Patient vs Doctor inquiry distribution
    - Average patient reading level (target <= Grade 6.5)
    - Average Self-RAG grounding score (target >= 0.90)
    - FDA SaMD / HIPAA compliance posture
    """
    try:
        return clinical_audit_logger.get_audit_summary_metrics()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to compute audit metrics: {str(e)}"
        )
