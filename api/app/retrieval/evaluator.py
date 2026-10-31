"""
Retrieval & Generation Quality Evaluator for AegisMed.
Measures Groundedness, Relevance, Citation Precision, and Hallucination Risk
to provide measurable, benchmark-driven validation.
"""

import re
from typing import List, Dict, Any, Tuple
from pydantic import BaseModel, Field
from app.interfaces.retriever import RetrievedChunk


class ClinicalEvaluationScore(BaseModel):
    groundedness_score: float = Field(..., ge=0.0, le=1.0, description="Percentage of claims substantiated by retrieved chunks")
    relevance_score: float = Field(..., ge=0.0, le=1.0, description="Alignment of response with query intent")
    citation_precision: float = Field(..., ge=0.0, le=1.0, description="Fraction of cited chunks actively supporting content")
    hallucination_risk: float = Field(..., ge=0.0, le=1.0, description="Estimated probability of unsupported assertions (0.0 = zero risk)")
    composite_score: float = 0.0
    passed_quality_gate: bool = True
    critique_notes: List[str] = Field(default_factory=list)


class ClinicalRagEvaluator:
    """
    Automated RAG evaluation pipeline for medical responses:
    - Verifies factual grounding against chunk corpora
    - Checks whether cited study names or numbers appear in the text
    - Identifies unsupported pharmacological statements
    """

    @staticmethod
    def extract_factual_claims(text: str) -> List[str]:
        """Extracts complete assertive sentences from response text."""
        sentences = re.split(r"(?<=[.!?])\s+", text)
        return [
            s.strip() for s in sentences
            if len(s.strip()) > 20 and not s.strip().startswith("#") and not s.strip().startswith(">")
        ]

    def evaluate(
        self,
        query: str,
        response_text: str = "",
        retrieved_chunks: List[RetrievedChunk] = None,
        response: str = None,
        citations: List[Any] = None
    ) -> ClinicalEvaluationScore:
        if response and not response_text:
            response_text = response
        if retrieved_chunks is None:
            retrieved_chunks = []
        if not response_text:
            return ClinicalEvaluationScore(
                groundedness_score=0.0,
                relevance_score=0.0,
                citation_precision=0.0,
                hallucination_risk=1.0,
                passed_quality_gate=False,
                critique_notes=["Empty response provided"]
            )

        if not retrieved_chunks:
            # If no evidence chunks exist, groundedness is 0
            return ClinicalEvaluationScore(
                groundedness_score=0.10,
                relevance_score=0.40,
                citation_precision=0.0,
                hallucination_risk=0.85,
                passed_quality_gate=False,
                critique_notes=["No evidence chunks available to substantiate response"]
            )

        # 1. Answer Relevance Calculation
        q_tokens = set(re.findall(r"\w+", query.lower()))
        r_tokens = set(re.findall(r"\w+", response_text.lower()))
        overlap = len(q_tokens & r_tokens)
        relevance = min(1.0, round(overlap / max(1, len(q_tokens)), 2))

        # 2. Groundedness Evaluation
        combined_evidence = " ".join([c.text.lower() for c in retrieved_chunks])
        claims = self.extract_factual_claims(response_text)

        substantiated_claims = 0
        notes: List[str] = []

        for claim in claims:
            claim_keywords = [w for w in re.findall(r"\w+", claim.lower()) if len(w) > 3]
            if not claim_keywords:
                continue
            matching_words = sum(1 for kw in claim_keywords if kw in combined_evidence)
            coverage = matching_words / len(claim_keywords)
            if coverage >= 0.40:
                substantiated_claims += 1
            else:
                notes.append(f"Low evidence match for statement: '{claim[:80]}...'")

        groundedness = round(substantiated_claims / max(1, len(claims)), 2)

        # 3. Citation Precision
        # Check if citations or chunk titles/IDs are mentioned in the text
        cited_count = 0
        for chunk in retrieved_chunks:
            title_words = [w for w in chunk.title.lower().split() if len(w) > 4]
            chunk_mentioned = chunk.chunk_id.lower() in response_text.lower() or any(
                tw in response_text.lower() for tw in title_words
            )
            if chunk_mentioned:
                cited_count += 1

        citation_precision = round(cited_count / max(1, len(retrieved_chunks)), 2)

        # 4. Hallucination Risk (Inverse of groundedness weighted with relevance)
        hallucination_risk = round(max(0.0, 1.0 - (groundedness * 0.70 + relevance * 0.30)), 2)

        passed = groundedness >= 0.60 and hallucination_risk <= 0.40
        composite = round(groundedness * 0.50 + relevance * 0.30 + citation_precision * 0.20, 2)

        return ClinicalEvaluationScore(
            groundedness_score=groundedness,
            relevance_score=relevance,
            citation_precision=citation_precision,
            hallucination_risk=hallucination_risk,
            composite_score=composite,
            passed_quality_gate=passed,
            critique_notes=notes[:4]
        )

