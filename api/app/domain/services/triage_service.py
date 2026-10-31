"""
Clinical Triage & Confidence Threshold Router for AegisMed.
Implements the conservative 'no-answer / low-confidence' path, ensuring the system
refuses to guess or synthesize advice when retrieved clinical evidence is weak or contradictory.
"""

from typing import List, Tuple
from app.domain.models.schemas import ConfidenceBand, StructuredMedicalResponse, ClinicalRiskLevel
from app.core.disclaimers import LOW_CONFIDENCE_DISCLAIMER


class ClinicalTriageService:
    """
    Evaluates evidence strength and determines routing path:
    - Low confidence (< 0.50): Refusal / Clarifying Question Path
    - Medium confidence (0.50 - 0.75): Cautionary Guidance with Caveats
    - High confidence (>= 0.75): Full Evidenced Clinical Synthesis
    """

    def __init__(self, low_cutoff: float = 0.50, high_cutoff: float = 0.75):
        self.low_cutoff = low_cutoff
        self.high_cutoff = high_cutoff

    def determine_confidence_band(self, score: float) -> ConfidenceBand:
        if score < self.low_cutoff:
            return ConfidenceBand.LOW
        elif score < self.high_cutoff:
            return ConfidenceBand.MEDIUM
        return ConfidenceBand.HIGH

    def evaluate_confidence(
        self,
        retrieval_score: float,
        evidence_count: int,
        has_red_flags: bool = False,
        is_ambiguous: bool = False
    ):
        band = self.determine_confidence_band(retrieval_score)
        should_refuse = (retrieval_score < self.low_cutoff) or (evidence_count == 0) or is_ambiguous
        
        clarifying_questions = []
        if should_refuse:
            clarifying_questions = [
                "Could you specify the exact duration and severity of the symptoms?",
                "Are there any relevant medical conditions, recent surgeries, or current medications?",
                "Has a physician previously diagnosed or treated this condition?"
            ]
        
        class TriageEvalResult:
            def __init__(self, should_refuse_advice, confidence_band, clarifying_questions, triage_action):
                self.should_refuse_advice = should_refuse_advice
                self.confidence_band = confidence_band
                self.clarifying_questions = clarifying_questions
                self.triage_action = triage_action

        return TriageEvalResult(
            should_refuse_advice=should_refuse,
            confidence_band=band,
            clarifying_questions=clarifying_questions,
            triage_action="Clarify details before finalizing recommendations" if should_refuse else "Proceed to synthesis"
        )

    def build_low_confidence_refusal(
        self,
        query: str,
        audience: str,
        confidence_score: float,
        suggested_followups: List[str]
    ) -> Tuple[str, List[str]]:
        """
        Conservative refusal path: Generates safe, non-hallucinatory guidance
        asking clarifying questions rather than offering speculative medical advice.
        """
        if audience == "patient":
            refusal_text = (
                "### Evidence-Based Clinical Notice: Clarification Needed\n\n"
                "We reviewed our medical guidelines for your inquiry, but there is insufficient high-certainty evidence "
                "to provide safe, personalized health recommendations for this specific scenario.\n\n"
                "**Why we are asking for more information:** Medical recommendations vary greatly depending on "
                "duration of symptoms, severity, and existing health conditions. To protect your safety, "
                "we avoid guessing when medical evidence is inconclusive.\n\n"
                "### Recommended Next Steps:\n"
                "1. Please consider the clarifying questions below to help us locate more accurate clinical information.\n"
                "2. If your symptoms are distressing, persistent, or worsening, please consult your primary doctor or an urgent care clinician."
            )
        else:
            refusal_text = (
                "### Inconclusive Evidence Advisory (Confidence < 0.50)\n\n"
                "The retrieved clinical literature does not meet our minimum Oxford CEBM evidence consensus threshold "
                "to deliver definitive clinical decision support for this query.\n\n"
                "**Clinical Recommendation:** Correlate with institutional hospital protocols, direct diagnostic workup, "
                "or consult a subspecialty physician. Consider refining query with explicit ICD-10 nosology or drug dosage details."
            )

        questions = suggested_followups if suggested_followups else [
            "How long have you noticed these symptoms, and how often do they occur?",
            "Are you currently taking any prescription medications or over-the-counter supplements?",
            "Do you have a personal medical history of chronic conditions (such as diabetes, heart disease, or kidney disease)?"
        ]

        return refusal_text, questions

