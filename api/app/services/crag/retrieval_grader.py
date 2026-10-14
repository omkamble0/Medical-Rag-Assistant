"""
Corrective RAG (CRAG) Retrieval Grader
Evaluates whether retrieved clinical documents adequately satisfy the user's information need.
Flags low-relevance or missing context and triggers corrective fallback retrieval.
"""

from typing import List, Dict, Any
from pydantic import BaseModel, Field


class RetrievalGradeResult(BaseModel):
    is_sufficient: bool = Field(..., description="Whether evidence is sufficient to answer query")
    relevance_score: float = Field(..., description="Confidence score from 0.0 to 1.0")
    grade_decision: str = Field(..., description="'PASSED_CORRECTIVE_FILTER' or 'TRIGGER_FALLBACK_SEARCH'")
    graded_documents_count: int
    rationale: str
    missing_aspects: List[str]


def grade_retrieval_relevance(
    query: str,
    retrieved_docs: List[Dict[str, Any]],
    threshold: float = 0.60
) -> RetrievalGradeResult:
    """
    CRAG Relevance Grader:
    Analyzes lexical overlap, clinical entity coverage, and evidence depth.
    """
    if not retrieved_docs:
        return RetrievalGradeResult(
            is_sufficient=False,
            relevance_score=0.0,
            grade_decision="TRIGGER_FALLBACK_SEARCH",
            graded_documents_count=0,
            rationale="No documents were retrieved in primary search.",
            missing_aspects=["Primary condition guidelines", "Trial evidence"]
        )

    q_low = query.lower()
    q_tokens = set([t for t in q_low.split() if len(t) > 2])

    # Check match against all documents
    combined_doc_text = " ".join([
        f"{d.get('title', '')} {d.get('snippet', '')} {d.get('content', '')} {d.get('key_takeaway', '')}".lower()
        for d in retrieved_docs
    ])

    matched_tokens = [tok for tok in q_tokens if tok in combined_doc_text]
    overlap_ratio = len(matched_tokens) / max(len(q_tokens), 1)

    # Check clinical aspects coverage
    missing = []
    if any(k in q_low for k in ["dose", "dosing", "how much"]) and not any(k in combined_doc_text for k in ["mg", "daily", "bid", "titrat"]):
        missing.append("Specific dosing and titration schedule")
    if any(k in q_low for k in ["side effect", "adverse", "risk"]) and not any(k in combined_doc_text for k in ["adverse", "tolerab", "contraindicat", "warning"]):
        missing.append("Adverse events and safety profile")
    if any(k in q_low for k in ["trial", "evidence", "study"]) and not any(k in combined_doc_text for k in ["trial", "rct", "nejm", "lancet", "p<"]):
        missing.append("Specific trial endpoints and p-values")

    # Score calculation
    base_score = min(0.95, overlap_ratio * 0.7 + (0.25 if len(retrieved_docs) >= 2 else 0.15))
    if missing:
        base_score = max(0.35, base_score - (0.15 * len(missing)))

    final_score = round(base_score, 2)
    is_sufficient = final_score >= threshold

    decision = "PASSED_CORRECTIVE_FILTER" if is_sufficient else "TRIGGER_FALLBACK_SEARCH"
    rationale = (
        f"Retrieval graded at {final_score:.2f} relevance ({len(matched_tokens)}/{len(q_tokens)} key query entities matched). "
        f"{'Evidence base is comprehensive and grounded.' if is_sufficient else 'Context gaps detected; supplemental literature lookup recommended.'}"
    )

    return RetrievalGradeResult(
        is_sufficient=is_sufficient,
        relevance_score=final_score,
        grade_decision=decision,
        graded_documents_count=len(retrieved_docs),
        rationale=rationale,
        missing_aspects=missing
    )
