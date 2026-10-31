"""
Domain Data Models and Structured Output Schemas for AegisMed.
Defines typed clinical contracts, structured responses, evidence traceability,
and escalation review payloads.
"""

from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel, Field


class ClinicalRiskLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL_EMERGENCY = "critical_emergency"
    CRITICAL = "critical_emergency"


class ConfidenceBand(str, Enum):
    LOW = "low"          # < 0.50: Triggers refusal / clarifying question
    MEDIUM = "medium"    # 0.50 - 0.75: Cautionary response with caveats
    HIGH = "high"        # >= 0.75: Full guideline-directed cited answer


class EvidenceItem(BaseModel):
    chunk_id: str = Field(..., description="Unique chunk reference ID")
    title: str = Field(..., description="Document or clinical trial title")
    journal_or_source: Optional[str] = None
    year: Optional[int] = None
    evidence_level: str = "Level 1"
    snippet: str = Field(..., description="Key clinical text supporting the claim")
    confidence: float = Field(..., ge=0.0, le=1.0)
    doi_or_url: Optional[str] = None


class IgnoredEvidenceItem(BaseModel):
    chunk_id: str
    title: str
    reason: str
    relevance_score: float


class StructuredMedicalResponse(BaseModel):
    query: str
    audience: str = Field(..., description="'patient' or 'clinician'")
    diagnosis_summary: str = Field(..., description="Clinical synthesis or plain English explanation")
    risk_level: ClinicalRiskLevel = ClinicalRiskLevel.LOW
    confidence_band: ConfidenceBand = ConfidenceBand.HIGH
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    is_refusal_or_clarification: bool = False
    is_emergency: bool = False
    escalation_required: bool = False
    evidence_list: List[EvidenceItem] = Field(default_factory=list)
    ignored_evidence: List[IgnoredEvidenceItem] = Field(default_factory=list)
    disclaimers: List[str] = Field(default_factory=list)
    follow_up_questions: List[str] = Field(default_factory=list)
    red_flag_warnings: List[str] = Field(default_factory=list)
    contraindications_detected: List[str] = Field(default_factory=list)
    reading_grade_level: Optional[str] = "Grade 6.0"
    rag_evaluation: Optional[Any] = None
    groundedness_score: float = 1.0
    latency_ms: float = 0.0
    escalation_ticket_id: Optional[str] = None

    @property
    def evidence(self) -> List[EvidenceItem]:
        return self.evidence_list


class ClinicalQueryRequest(BaseModel):
    query: str = Field(..., min_length=2, max_length=2000, description="Patient symptom narrative or clinical query")
    audience: str = Field(default="patient", description="'patient' | 'doctor' | 'clinician'")
    patient_age: Optional[int] = Field(default=None, ge=0, le=125)
    is_pregnant: Optional[bool] = False
    current_medications: List[str] = Field(default_factory=list)
    egfr: Optional[float] = Field(default=None, ge=0.0, description="Estimated GFR in mL/min/1.73m2")


class EscalationTicket(BaseModel):
    ticket_id: str
    created_at: str
    query: str
    reason: str
    risk_level: ClinicalRiskLevel
    audience: str
    status: str = "pending_review"  # "pending_review" | "approved" | "rejected"
    reviewer_notes: Optional[str] = None


class UserFeedbackRequest(BaseModel):
    query_id: str
    query_text: str
    rating: int = Field(..., ge=1, le=5, description="1 to 5 stars")
    is_accurate: bool
    is_safe: bool
    audience: str
    clinician_comments: Optional[str] = None

