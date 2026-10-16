from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from app.models.enums import UserMode, EvidenceLevel, ConfidenceStatus, TriageUrgency
from app.core.query_parser import ParsedQueryAnalysis, ClinicalEntities

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=2, max_length=1000, description="Clinical or patient health query")
    user_mode: UserMode = Field(default=UserMode.PATIENT, description="Target perspective: professional or patient")
    filters: Optional[Dict[str, Any]] = Field(default=None, description="Optional metadata filters")

class JargonItem(BaseModel):
    term: str = Field(..., description="Clinical medical term identified in the text")
    plain_english: str = Field(..., description="Everyday language explanation in 1 sentence")

class DoctorQuestion(BaseModel):
    question: str = Field(..., description="Actionable question the patient should ask their clinician")
    category: str = Field(..., description="Category like 'Diagnosis', 'Treatment Options', or 'Side Effects'")
    psa_type: Optional[str] = Field(
        default="Action",
        description="P-S-A framework type: 'Parameter' (baseline labs/staging), 'Safety' (interactions/contraindications), or 'Action' (shared decision-making/titration)"
    )
    rationale: Optional[str] = Field(
        default=None,
        description="Clinical rationale behind why the patient/doctor needs this specific discussion point"
    )

class PatientSuggestion(BaseModel):
    """Strictly limited to lifestyle modifications, doctor questions (P-S-A framework), and symptom monitoring."""
    lifestyle_recommendations: List[str] = Field(
        default_factory=list,
        description="Evidence-backed non-pharmacological lifestyle actions (diet, activity, hydration, sleep)"
    )
    questions_for_doctor: List[DoctorQuestion] = Field(
        default_factory=list,
        description="P-S-A structured clarifying questions for next clinical appointment"
    )
    monitoring_metrics: List[str] = Field(
        default_factory=list,
        description="Parameters for patient home tracking (e.g. daily BP log, symptom diary)"
    )

class ClinicianSuggestion(BaseModel):
    """Strictly limited to trial subgroups, titration schedules, guideline comparisons, and contraindications."""
    trial_subgroup_analyses: List[str] = Field(
        default_factory=list,
        description="Subgroup efficacy stratification (e.g. eGFR thresholds, biomarker status, age cohorts)"
    )
    titration_protocols: List[str] = Field(
        default_factory=list,
        description="Dose escalation steps, organ function thresholds, and tapering rules"
    )
    guideline_comparisons: List[str] = Field(
        default_factory=list,
        description="Cross-guideline alignment (e.g. ACC/AHA vs ESC vs WHO vs KDIGO)"
    )
    contraindications_interactions: List[str] = Field(
        default_factory=list,
        description="Major CYP metabolic pathways, renal cutoffs, and co-administration contraindications"
    )

class ElaborationOption(BaseModel):
    label: str = Field(..., description="Display title for the leading sub-topic or symptom branch")
    query: str = Field(..., description="Target search query to execute when clicked")
    health_body: str = Field(..., description="Backing authoritative guideline (e.g. WHO / AHA / NICE)")
    context: str = Field(..., description="Brief guidance on when this sub-path applies")

class SourceDocument(BaseModel):
    id: str = Field(..., description="Document identifier (e.g., DOC-01)")
    citation_index: int = Field(..., description="1-indexed reference number [1], [2], etc.")
    title: str = Field(..., description="Title of the clinical study, trial, or guideline")
    journal: str = Field(..., description="Publishing journal or authority (e.g., NEJM, The Lancet, CDC, FDA, WHO)")
    year: int = Field(..., description="Publication year")
    doi_or_pmid: Optional[str] = Field(None, description="DOI or PubMed ID")
    evidence_level: EvidenceLevel = Field(..., description="Oxford CEBM Level of Evidence")
    snippet: str = Field(..., description="Verified excerpt supporting the generated claims")
    relevance_score: float = Field(..., description="Cosine similarity / retriever score (0.0 to 1.0)")
    key_takeaway: Optional[str] = Field(None, description="One-line clinical summary of the finding")
    plain_analogy: Optional[str] = Field(None, description="Patient-friendly mechanism analogy")
    patient_plain_language: Optional[str] = Field(None, description="Patient plain language overview")

class ConfidenceMetrics(BaseModel):
    overall_score: float = Field(..., description="Composite confidence score 0.0 - 1.0")
    status: ConfidenceStatus = Field(..., description="High (Green), Moderate (Yellow), Low (Red)")
    retrieval_relevance: float = Field(..., description="Average semantic match of top retrieved documents")
    grounding_ratio: float = Field(..., description="Percentage of claims in answer backed by citations")
    evidence_freshness: float = Field(..., description="Recency weighting score")
    explanation: str = Field(..., description="Human-readable breakdown of the confidence evaluation")

class EmergencyTriageAlert(BaseModel):
    is_emergency: bool = True
    urgency: TriageUrgency = TriageUrgency.IMMEDIATE_EMERGENCY
    matched_keywords: List[str] = Field(default_factory=list)
    headline: str = Field(..., description="Immediate clinical warning headline")
    critical_guidance: str = Field(..., description="Specific triage instruction (e.g. Call 911 / Go to nearest ER)")
    red_flag_symptoms: List[str] = Field(default_factory=list)
    emergency_contacts: List[str] = Field(default_factory=lambda: ["911 (US/Canada)", "112 (Europe)", "108 / 112 (India)", "988 (Crisis Lifeline)"])

class ValidationResultSchema(BaseModel):
    original: str
    corrected: str
    is_valid: bool
    corrections_made: List[str] = Field(default_factory=list)
    confidence_score: float = 1.0
    medical_terms_found: List[str] = Field(default_factory=list)
    medical_terms_details: Optional[List[Dict[str, Any]]] = None
    issues: List[str] = Field(default_factory=list)

class SearchResponse(BaseModel):
    query: str
    user_mode: UserMode
    is_emergency: bool = False
    triage_alert: Optional[EmergencyTriageAlert] = None
    validation: Optional[ValidationResultSchema] = Field(
        default=None,
        description="3-Layer Medical Query Typo & Terminology Validation details"
    )
    query_analysis: Optional[ParsedQueryAnalysis] = Field(
        default=None,
        description="Stage 1 Inbound Query Deconstruction & Entity Parsing results"
    )
    context_gaps: Optional[List[str]] = Field(
        default=None,
        description="Clinical context gaps and missing variable alerts"
    )
    clinical_thinking: Optional[str] = Field(
        default=None,
        description="Stage 2 Latent Clinical Thinking scratchpad audit (<clinical_thinking> block)"
    )
    answer: str = Field(..., description="Synthesized medical response with inline citations [1], [2]")
    citations: List[int] = Field(default_factory=list, description="List of citation numbers referenced in the answer")
    sources: List[SourceDocument] = Field(default_factory=list, description="Retrieved evidence documents")
    confidence: ConfidenceMetrics
    accuracy_score: Optional[float] = Field(default=95.4, description="Calibrated clinical evidence accuracy score")
    elaboration_leadings: Optional[List[ElaborationOption]] = Field(default=None, description="Smart guided questions and leading options when query needs elaboration")
    jargon_glossary: Optional[List[JargonItem]] = Field(default=None, description="Plain language definitions for patient mode")
    doctor_questions: Optional[List[DoctorQuestion]] = Field(default=None, description="Suggested P-S-A questions for patient mode")
    patient_suggestions: Optional[PatientSuggestion] = Field(default=None, description="Structured patient suggestions (lifestyle, monitoring, doctor questions)")
    clinician_suggestions: Optional[ClinicianSuggestion] = Field(default=None, description="Structured clinician suggestions (subgroups, titration, guidelines, contraindications)")
    reading_level: Optional[str] = Field(None, description="Readability grade level")
    latency_ms: int = Field(..., description="Processing time in milliseconds")
    execution_trace: Optional[List[Dict[str, Any]]] = Field(default=None, description="LangGraph 7-stage execution trace")
    tool_results: Optional[Dict[str, Any]] = Field(default=None, description="Autonomous clinical tool results (DDI, eGFR, PubMed)")
    crag_grade: Optional[Dict[str, Any]] = Field(default=None, description="Corrective RAG relevance grade and fallback decision")
    grounding_audit: Optional[Dict[str, Any]] = Field(default=None, description="Self-RAG grounding confidence and hallucination score")

class DualCompareResponse(BaseModel):
    query: str
    professional_response: SearchResponse
    patient_response: SearchResponse
    shared_sources: List[SourceDocument]
