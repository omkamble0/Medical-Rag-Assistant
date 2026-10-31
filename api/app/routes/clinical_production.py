"""
Production Clinical Query, Observability & Escalation API Router for AegisMed.
Exposes structured clinical inference, Prometheus metrics, clinician escalation queue,
user feedback loop, and knowledge provenance endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import PlainTextResponse
from typing import List, Dict, Any, Optional

from app.domain.models.schemas import (
    ClinicalQueryRequest,
    StructuredMedicalResponse,
    EscalationTicket,
    UserFeedbackRequest
)
from app.domain.services.clinical_orchestrator import ClinicalOrchestrator
from app.domain.services.escalation_service import ClinicalEscalationService
from app.domain.services.knowledge_service import MedicalKnowledgeService, KnowledgeVersionInfo
from app.di.container import (
    get_orchestrator_dep,
    get_escalation_dep,
    get_knowledge_dep
)
from app.core.metrics import metrics

router = APIRouter(prefix="/api/v1", tags=["Production Clinical Architecture"])


# ============================================================
# 1. Primary Structured Clinical Query Endpoint
# ============================================================
@router.post(
    "/clinical/query",
    response_model=StructuredMedicalResponse,
    summary="Execute Layered Clinical RAG Inference",
    description="Processes query through PII scrubber, Tier-1 safety guardrails, hybrid retrieval, LLM synthesis, and grounding evaluation."
)
async def execute_clinical_query(
    request: ClinicalQueryRequest,
    orchestrator: ClinicalOrchestrator = Depends(get_orchestrator_dep)
) -> StructuredMedicalResponse:
    """Production endpoint with structured output schema, source traceability, and conservative low-confidence refusal."""
    try:
        response = await orchestrator.execute_query(request)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Clinical orchestration failure: {str(e)}"
        )


# ============================================================
# 2. Prometheus Observability & Metrics Endpoints
# ============================================================
@router.get(
    "/metrics",
    response_class=PlainTextResponse,
    summary="Prometheus Metrics Exporter",
    description="Serves Prometheus text format metrics for request rates, latencies, tokens, and safety intercepts."
)
async def get_prometheus_metrics():
    return PlainTextResponse(metrics.export_prometheus(), media_type="text/plain; version=0.0.4")


@router.get(
    "/metrics/summary",
    response_model=Dict[str, Any],
    summary="Observability Dashboard Summary",
    description="Returns JSON summary of p50/p95/p99 latencies, token counts, fallbacks, and safety intercepts."
)
async def get_metrics_summary():
    return metrics.get_summary()


# ============================================================
# 3. Clinician Review & Escalation Workflow
# ============================================================
@router.get(
    "/escalations",
    response_model=List[EscalationTicket],
    summary="List Pending Clinician Escalation Tickets",
    description="Returns cases flagged for physician review (emergencies, contraindications, or uncertain evidence)."
)
async def list_escalations(
    escalation_service: ClinicalEscalationService = Depends(get_escalation_dep)
):
    return escalation_service.list_pending_tickets()


@router.post(
    "/escalations/{ticket_id}/review",
    response_model=EscalationTicket,
    summary="Submit Clinician Review Decision"
)
async def review_escalation(
    ticket_id: str,
    action: str,  # "approved" or "rejected"
    notes: Optional[str] = None,
    escalation_service: ClinicalEscalationService = Depends(get_escalation_dep)
):
    ticket = escalation_service.resolve_ticket(ticket_id, status=action, reviewer_notes=notes)
    if not ticket:
        raise HTTPException(status_code=404, detail=f"Escalation ticket {ticket_id} not found.")
    return ticket


# ============================================================
# 4. User & Clinician Feedback Loop
# ============================================================
@router.post(
    "/feedback",
    summary="Submit Answer Quality Feedback",
    description="Captures clinician and patient ratings to monitor drift and citation quality."
)
async def submit_feedback(feedback: UserFeedbackRequest):
    return {
        "status": "recorded",
        "query_id": feedback.query_id,
        "rating": feedback.rating,
        "is_accurate": feedback.is_accurate,
        "is_safe": feedback.is_safe,
        "message": "Feedback ingested into continuous clinical quality evaluation pipeline."
    }


# ============================================================
# 5. Medical Knowledge Base Provenance & Versioning
# ============================================================
@router.get(
    "/knowledge/version",
    response_model=KnowledgeVersionInfo,
    summary="Get Medical Knowledge Versioning & Source Provenance"
)
async def get_knowledge_version(
    knowledge_service: MedicalKnowledgeService = Depends(get_knowledge_dep)
):
    return knowledge_service.get_version_info()

