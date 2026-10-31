"""
Clinical Orchestrator Domain Service for AegisMed.
Integrates safety guardrails, hybrid retrieval, LLM gateway, grounding evaluation,
and structured output formatting with dependency-injected interfaces.
"""

import time
import uuid
from typing import Dict, Any, List, Optional

from app.interfaces.retriever import RetrieverInterface, RetrievalResult
from app.interfaces.llm_provider import LLMProviderInterface
from app.interfaces.guardrail import SafetyGuardrailInterface, SafetyRiskLevel
from app.domain.models.schemas import (
    ClinicalQueryRequest,
    StructuredMedicalResponse,
    EvidenceItem,
    IgnoredEvidenceItem,
    ClinicalRiskLevel,
    ConfidenceBand
)
from app.domain.services.triage_service import ClinicalTriageService
from app.domain.services.escalation_service import ClinicalEscalationService
from app.core.security import scrub_pii
from app.core.disclaimers import get_disclaimer, EMERGENCY_DISCLAIMER
from app.core.readability import enforce_audience_contract
from app.retrieval.evaluator import ClinicalRagEvaluator
from app.core.prompts import PATIENT_PROMPT, CLINICIAN_PROMPT


class ClinicalOrchestrator:
    """
    Production Domain Orchestrator for Evidence-Based Clinical Assistant:
    - Coordinates safety guardrails, hybrid retrieval, LLM synthesis, and grounding audit.
    - Decoupled from HTTP routes and frameworks via clear interfaces.
    """

    def __init__(
        self,
        retriever: RetrieverInterface,
        llm_provider: LLMProviderInterface,
        safety_service: SafetyGuardrailInterface,
        triage_service: Optional[ClinicalTriageService] = None,
        escalation_service: Optional[ClinicalEscalationService] = None,
        evaluator: Optional[ClinicalRagEvaluator] = None
    ):
        self.retriever = retriever
        self.llm = llm_provider
        self.safety = safety_service
        self.triage = triage_service or ClinicalTriageService()
        self.escalation = escalation_service or ClinicalEscalationService()
        self.evaluator = evaluator or ClinicalRagEvaluator()

    def process_query_sync(self, request: ClinicalQueryRequest) -> StructuredMedicalResponse:
        start_time = time.time()

        # 1. PII Scrubbing
        pii_result = scrub_pii(request.query)
        clean_query = pii_result.cleaned_text
        audience = "doctor" if request.audience.lower() in ("doctor", "clinician") else "patient"

        # 2. Tier-1 Safety & Contraindication Guardrails
        patient_ctx = {
            "patient_age": request.patient_age,
            "is_pregnant": request.is_pregnant,
            "current_medications": request.current_medications,
            "egfr": request.egfr
        }
        safety_check = self.safety.evaluate(clean_query, patient_context=patient_ctx)

        # Handle Critical Emergency Immediately
        if safety_check.is_emergency:
            ticket = self.escalation.create_ticket(
                query=clean_query,
                reason="Acute Emergency Red Flag Triggered",
                risk_level=ClinicalRiskLevel.CRITICAL_EMERGENCY,
                audience=audience
            )
            latency = (time.time() - start_time) * 1000
            return StructuredMedicalResponse(
                query=clean_query,
                audience=audience,
                diagnosis_summary=(
                    f"### 🚨 {safety_check.headline}\n\n"
                    f"**CRITICAL ACTION REQUIRED:** {safety_check.action_required}\n\n"
                    f"**Identified Red Flag Symptoms:** {', '.join(safety_check.matched_flags)}\n\n"
                    f"Please immediately call 911 or proceed to the nearest Emergency Department. "
                    f"Do not drive yourself if you are feeling lightheaded, short of breath, or experiencing acute chest pressure."
                ),
                risk_level=ClinicalRiskLevel.CRITICAL,
                confidence_band=ConfidenceBand.HIGH,
                confidence_score=1.0,
                is_refusal_or_clarification=False,
                is_emergency=True,
                escalation_required=True,
                evidence_list=[],
                ignored_evidence=[],
                disclaimers=[EMERGENCY_DISCLAIMER],
                follow_up_questions=["Are you alone right now?", "Are you able to call emergency dispatch immediately?"],
                red_flag_warnings=safety_check.matched_flags,
                groundedness_score=1.0,
                latency_ms=round(latency, 2),
                escalation_ticket_id=ticket.ticket_id
            )

        # Handle Contraindication Alert
        if not safety_check.is_safe and safety_check.contraindications_detected:
            ticket = self.escalation.create_ticket(
                query=clean_query,
                reason="High-Risk Clinical Contraindication",
                risk_level=ClinicalRiskLevel.HIGH,
                audience=audience
            )
            contra_bullets = "\n".join([
                f"- **{c.get('category')}:** {c.get('description')}"
                for c in safety_check.contraindications_detected
            ])
            latency = (time.time() - start_time) * 1000
            return StructuredMedicalResponse(
                query=clean_query,
                audience=audience,
                diagnosis_summary=(
                    f"### ⚠️ {safety_check.headline}\n\n"
                    f"**SAFETY ALERT:** A significant clinical contraindication was detected:\n\n"
                    f"{contra_bullets}\n\n"
                    f"**Action:** Withhold therapy or obtain direct physician clearance before proceeding."
                ),
                risk_level=ClinicalRiskLevel.HIGH,
                confidence_band=ConfidenceBand.HIGH,
                confidence_score=0.95,
                is_refusal_or_clarification=False,
                is_emergency=False,
                escalation_required=True,
                evidence_list=[],
                ignored_evidence=[],
                disclaimers=[get_disclaimer(audience)],
                follow_up_questions=["Has your prescribing physician verified this medication during your current clinical status?"],
                contraindications_detected=[c.get("description", "") for c in safety_check.contraindications_detected],
                groundedness_score=1.0,
                latency_ms=round(latency, 2),
                escalation_ticket_id=ticket.ticket_id
            )

        # 3. Hybrid Evidence Retrieval
        if hasattr(self.retriever, "retrieve_sync"):
            retrieval_res = self.retriever.retrieve_sync(query=clean_query, top_k=4, min_score=0.30)
        else:
            import asyncio
            retrieval_res = asyncio.run(self.retriever.retrieve(query=clean_query, top_k=4, min_score=0.30))

        confidence_band = self.triage.determine_confidence_band(retrieval_res.mean_confidence)

        # 4. Conservative Refusal / Low-Confidence Path
        if confidence_band == ConfidenceBand.LOW or not retrieval_res.active_chunks:
            ticket = self.escalation.create_ticket(
                query=clean_query,
                reason="Inconclusive clinical evidence retrieved (confidence < 0.50)",
                risk_level=ClinicalRiskLevel.LOW,
                audience=audience
            )
            refusal_text, clarif_questions = self.triage.build_low_confidence_refusal(
                query=clean_query,
                audience=audience,
                confidence_score=retrieval_res.mean_confidence,
                suggested_followups=[]
            )
            latency = (time.time() - start_time) * 1000
            return StructuredMedicalResponse(
                query=clean_query,
                audience=audience,
                diagnosis_summary=refusal_text,
                risk_level=ClinicalRiskLevel.LOW,
                confidence_band=ConfidenceBand.LOW,
                confidence_score=retrieval_res.mean_confidence,
                is_refusal_or_clarification=True,
                is_emergency=False,
                escalation_required=False,
                evidence_list=[],
                ignored_evidence=[
                    IgnoredEvidenceItem(
                        chunk_id=i.chunk_id,
                        title=i.title,
                        reason=i.reason,
                        relevance_score=i.score
                    ) for i in retrieval_res.ignored_chunks
                ],
                disclaimers=[get_disclaimer("low_confidence")],
                follow_up_questions=clarif_questions,
                groundedness_score=0.0,
                latency_ms=round(latency, 2),
                escalation_ticket_id=ticket.ticket_id
            )

        # 5. Format Evidence Context for LLM Synthesis
        evidence_text_blocks = []
        evidence_items: List[EvidenceItem] = []
        for idx, chunk in enumerate(retrieval_res.active_chunks, start=1):
            evidence_text_blocks.append(
                f"[Evidence {idx} - ID: {chunk.chunk_id}] {chunk.title} ({chunk.journal}, {chunk.year or 'Recent'} - {chunk.evidence_level}):\n{chunk.text}"
            )
            evidence_items.append(
                EvidenceItem(
                    chunk_id=chunk.chunk_id,
                    title=chunk.title,
                    journal_or_source=chunk.journal,
                    year=chunk.year,
                    evidence_level=chunk.evidence_level,
                    snippet=chunk.text[:200] + "...",
                    confidence=chunk.relevance_score,
                    doi_or_url=chunk.metadata.get("doi_or_pmid")
                )
            )

        context_str = "\n\n".join(evidence_text_blocks)
        sys_prompt = CLINICIAN_PROMPT if audience == "doctor" else PATIENT_PROMPT
        user_prompt = f"CLINICAL EVIDENCE:\n{context_str}\n\nUSER INQUIRY:\n{clean_query}"

        # 6. LLM Generation
        llm_resp = self.llm.generate(
            prompt=user_prompt,
            system_prompt=sys_prompt,
            temperature=0.2
        )
        raw_text = llm_resp.content or ""

        # Enforce Audience Contract
        refined_text, audit_info = enforce_audience_contract(
            raw_text,
            audience
        )

        # 7. Grounding and Hallucination Evaluation
        eval_score = self.evaluator.evaluate(
            query=clean_query,
            response_text=refined_text,
            retrieved_chunks=retrieval_res.active_chunks
        )

        # 8. Follow-up Questions Generation
        follow_ups = [
            f"Would you like more details on the clinical trials cited?",
            f"Are there any specific lifestyle or dietary habits you'd like to discuss?",
            f"Should we check interactions with any current medications you take?"
        ]

        ignored_items = [
            IgnoredEvidenceItem(
                chunk_id=i.chunk_id,
                title=i.title,
                reason=i.reason,
                relevance_score=i.score
            ) for i in retrieval_res.ignored_chunks
        ]

        latency = (time.time() - start_time) * 1000

        return StructuredMedicalResponse(
            query=clean_query,
            audience=audience,
            diagnosis_summary=refined_text,
            risk_level=ClinicalRiskLevel.LOW if safety_check.risk_level == SafetyRiskLevel.LOW else ClinicalRiskLevel.MODERATE,
            confidence_band=confidence_band,
            confidence_score=retrieval_res.mean_confidence,
            is_refusal_or_clarification=False,
            is_emergency=False,
            escalation_required=False,
            evidence_list=evidence_items,
            ignored_evidence=ignored_items,
            disclaimers=[get_disclaimer(audience)],
            follow_up_questions=follow_ups,
            reading_grade_level="Grade 6.0" if audience == "patient" else "Postgraduate Clinical",
            rag_evaluation=eval_score,
            groundedness_score=eval_score.groundedness_score,
            latency_ms=round(latency, 2)
        )

    async def execute_query(self, request: ClinicalQueryRequest) -> StructuredMedicalResponse:
        return self.process_query_sync(request)
        start_time = time.time()

        # 1. PII Scrubbing
        pii_result = scrub_pii(request.query)
        clean_query = pii_result.cleaned_text
        audience = "doctor" if request.audience.lower() in ("doctor", "clinician") else "patient"

        # 2. Tier-1 Safety & Contraindication Guardrails
        patient_ctx = {
            "patient_age": request.patient_age,
            "is_pregnant": request.is_pregnant,
            "current_medications": request.current_medications,
            "egfr": request.egfr
        }
        safety_check = self.safety.evaluate(clean_query, patient_context=patient_ctx)

        # Handle Critical Emergency Immediately (0% generative hallucination risk)
        if safety_check.is_emergency:
            ticket = self.escalation.create_ticket(
                query=clean_query,
                reason="Acute Emergency Red Flag Triggered",
                risk_level=ClinicalRiskLevel.CRITICAL_EMERGENCY,
                audience=audience
            )
            latency = (time.time() - start_time) * 1000
            return StructuredMedicalResponse(
                query=clean_query,
                audience=audience,
                diagnosis_summary=(
                    f"### 🚨 {safety_check.headline}\n\n"
                    f"**CRITICAL ACTION REQUIRED:** {safety_check.action_required}\n\n"
                    f"**Identified Red Flag Symptoms:** {', '.join(safety_check.matched_flags)}\n\n"
                    f"Please immediately call 911 or proceed to the nearest Emergency Department. "
                    f"Do not drive yourself if you are feeling lightheaded, short of breath, or experiencing acute chest pressure."
                ),
                risk_level=ClinicalRiskLevel.CRITICAL_EMERGENCY,
                confidence_band=ConfidenceBand.HIGH,
                confidence_score=1.0,
                is_refusal_or_clarification=False,
                evidence_list=[],
                ignored_evidence=[],
                disclaimers=[EMERGENCY_DISCLAIMER],
                follow_up_questions=["Are you alone right now?", "Are you able to call emergency dispatch immediately?"],
                red_flag_warnings=safety_check.matched_flags,
                groundedness_score=1.0,
                latency_ms=round(latency, 2),
                escalation_ticket_id=ticket.ticket_id
            )

        # Handle Contraindication Alert
        if not safety_check.is_safe and safety_check.contraindications_detected:
            ticket = self.escalation.create_ticket(
                query=clean_query,
                reason="High-Risk Clinical Contraindication",
                risk_level=ClinicalRiskLevel.HIGH,
                audience=audience
            )
            contra_bullets = "\n".join([
                f"- **{c.get('category')}:** {c.get('description')}"
                for c in safety_check.contraindications_detected
            ])
            latency = (time.time() - start_time) * 1000
            return StructuredMedicalResponse(
                query=clean_query,
                audience=audience,
                diagnosis_summary=(
                    f"### ⚠️ {safety_check.headline}\n\n"
                    f"**SAFETY ALERT:** A significant clinical contraindication was detected:\n\n"
                    f"{contra_bullets}\n\n"
                    f"**Action:** Withhold therapy or obtain direct physician clearance before proceeding."
                ),
                risk_level=ClinicalRiskLevel.HIGH,
                confidence_band=ConfidenceBand.HIGH,
                confidence_score=0.95,
                is_refusal_or_clarification=False,
                evidence_list=[],
                ignored_evidence=[],
                disclaimers=[get_disclaimer(audience)],
                follow_up_questions=["Has your prescribing physician verified this medication during your current clinical status?"],
                contraindications_detected=[c.get("description", "") for c in safety_check.contraindications_detected],
                groundedness_score=1.0,
                latency_ms=round(latency, 2),
                escalation_ticket_id=ticket.ticket_id
            )

        # 3. Hybrid Evidence Retrieval (BM25 + Vector + CEBM Weighting)
        retrieval_res: RetrievalResult = await self.retriever.retrieve(
            query=clean_query,
            top_k=4,
            min_score=0.30
        )

        confidence_band = self.triage.determine_confidence_band(retrieval_res.mean_confidence)

        # 4. Conservative Refusal / Low-Confidence Path
        if confidence_band == ConfidenceBand.LOW or not retrieval_res.active_chunks:
            ticket = self.escalation.create_ticket(
                query=clean_query,
                reason="Inconclusive clinical evidence retrieved (confidence < 0.50)",
                risk_level=ClinicalRiskLevel.LOW,
                audience=audience
            )
            refusal_text, clarif_questions = self.triage.build_low_confidence_refusal(
                query=clean_query,
                audience=audience,
                confidence_score=retrieval_res.mean_confidence,
                suggested_followups=[]
            )
            latency = (time.time() - start_time) * 1000
            return StructuredMedicalResponse(
                query=clean_query,
                audience=audience,
                diagnosis_summary=refusal_text,
                risk_level=ClinicalRiskLevel.LOW,
                confidence_band=ConfidenceBand.LOW,
                confidence_score=retrieval_res.mean_confidence,
                is_refusal_or_clarification=True,
                evidence_list=[],
                ignored_evidence=[
                    IgnoredEvidenceItem(
                        chunk_id=i.chunk_id,
                        title=i.title,
                        reason=i.reason,
                        relevance_score=i.score
                    ) for i in retrieval_res.ignored_chunks
                ],
                disclaimers=[get_disclaimer("low_confidence")],
                follow_up_questions=clarif_questions,
                groundedness_score=0.0,
                latency_ms=round(latency, 2),
                escalation_ticket_id=ticket.ticket_id
            )

        # 5. Format Evidence Context for LLM Synthesis
        evidence_text_blocks = []
        evidence_items: List[EvidenceItem] = []
        for idx, chunk in enumerate(retrieval_res.active_chunks, start=1):
            evidence_text_blocks.append(
                f"[Evidence {idx} - ID: {chunk.chunk_id}] {chunk.title} ({chunk.journal}, {chunk.year or 'Recent'} - {chunk.evidence_level}):\n{chunk.text}"
            )
            evidence_items.append(
                EvidenceItem(
                    chunk_id=chunk.chunk_id,
                    title=chunk.title,
                    journal_or_source=chunk.journal,
                    year=chunk.year,
                    evidence_level=chunk.evidence_level,
                    snippet=chunk.text[:200] + "...",
                    confidence=chunk.relevance_score,
                    doi_or_url=chunk.metadata.get("doi_or_pmid")
                )
            )

        context_str = "\n\n".join(evidence_text_blocks)
        sys_prompt = CLINICIAN_PROMPT if audience == "doctor" else PATIENT_PROMPT
        user_prompt = f"CLINICAL EVIDENCE:\n{context_str}\n\nUSER INQUIRY:\n{clean_query}"

        # 6. LLM Generation
        llm_resp = self.llm.generate(
            prompt=user_prompt,
            system_prompt=sys_prompt,
            temperature=0.2
        )
        raw_text = llm_resp.content or ""

        # Enforce Audience Contract (Plain English analogy for patient; GDMT for clinician)
        refined_text = enforce_audience_contract(
            answer=raw_text,
            audience=audience,
            query=clean_query,
            sources=[]
        )

        # 7. Grounding and Hallucination Evaluation
        eval_score = self.evaluator.evaluate(
            query=clean_query,
            response_text=refined_text,
            retrieved_chunks=retrieval_res.active_chunks
        )

        # 8. Follow-up Questions Generation
        follow_ups = [
            f"Would you like more details on the clinical trials cited?",
            f"Are there any specific lifestyle or dietary habits you'd like to discuss?",
            f"Should we check interactions with any current medications you take?"
        ]

        ignored_items = [
            IgnoredEvidenceItem(
                chunk_id=i.chunk_id,
                title=i.title,
                reason=i.reason,
                relevance_score=i.score
            ) for i in retrieval_res.ignored_chunks
        ]

        latency = (time.time() - start_time) * 1000

        return StructuredMedicalResponse(
            query=clean_query,
            audience=audience,
            diagnosis_summary=refined_text,
            risk_level=ClinicalRiskLevel.LOW if safety_check.risk_level == SafetyRiskLevel.LOW else ClinicalRiskLevel.MODERATE,
            confidence_band=confidence_band,
            confidence_score=retrieval_res.mean_confidence,
            is_refusal_or_clarification=False,
            evidence_list=evidence_items,
            ignored_evidence=ignored_items,
            disclaimers=[get_disclaimer(audience)],
            follow_up_questions=follow_ups,
            groundedness_score=eval_score.groundedness_score,
            latency_ms=round(latency, 2)
        )

