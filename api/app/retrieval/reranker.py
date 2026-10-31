"""
Clinical Evidence Reranker for AegisMed.
Applies cross-evidence re-ranking using Oxford CEBM evidence hierarchy,
recency weighting, and strict clinical relevance thresholds.
"""

from typing import List, Tuple
from app.interfaces.retriever import RerankerInterface, RetrievedChunk, IgnoredEvidence

CEBM_LEVEL_MULTIPLIERS = {
    "Level 1": 1.18,
    "Level 2": 1.12,
    "Level 3": 1.00,
    "Level 4": 0.95,
    "Level 5": 0.90,
}


class ClinicalEvidenceReranker(RerankerInterface):
    """
    Reranks candidate evidence chunks and separates accepted chunks from
    ignored chunks with explicit, auditable exclusion reasons.
    """

    def __init__(self, min_relevance_threshold: float = 0.35, min_relevance_score: float = None):
        if min_relevance_score is not None:
            self.min_relevance_threshold = min_relevance_score
        else:
            self.min_relevance_threshold = min_relevance_threshold

    def rerank(
        self,
        query: str,
        chunks: List[RetrievedChunk],
        top_n: int = 4,
        top_k: int = None
    ) -> Tuple[List[RetrievedChunk], List[IgnoredEvidence]]:
        if top_k is not None:
            top_n = top_k
        if not chunks:
            return [], []

        q_lower = query.lower()
        scored_candidates: List[Tuple[float, RetrievedChunk]] = []
        ignored: List[IgnoredEvidence] = []

        seen_doc_ids = set()

        for chunk in chunks:
            base_score = chunk.relevance_score

            # 1. Evidence Grade Multiplier (Oxford CEBM)
            mult = CEBM_LEVEL_MULTIPLIERS.get(chunk.evidence_level, 1.0)
            calibrated_score = base_score * mult

            # 2. Query Entity Exact Match Boost
            t_low = chunk.title.lower()
            text_low = chunk.text.lower()
            q_terms = [t for t in q_lower.split() if len(t) > 2]
            match_count = sum(1 for term in q_terms if term in t_low or term in text_low)
            if match_count > 0:
                calibrated_score += min(0.25, match_count * 0.05)

            # 3. Recency Boost
            if chunk.year and chunk.year >= 2022:
                calibrated_score *= 1.05

            calibrated_score = round(min(1.0, calibrated_score), 3)
            chunk.relevance_score = calibrated_score

            # Filter sub-threshold evidence
            if calibrated_score < self.min_relevance_threshold:
                ignored.append(
                    IgnoredEvidence(
                        chunk_id=chunk.chunk_id,
                        title=chunk.title,
                        reason=f"Relevance score ({calibrated_score:.2f}) below clinical consensus threshold ({self.min_relevance_threshold}) (CEBM {chunk.evidence_level})",
                        score=calibrated_score
                    )
                )
                continue

            # Deduplication: prefer the highest-scored chunk per document/section
            dedup_key = f"{chunk.document_id}:{chunk.section_name}"
            if dedup_key in seen_doc_ids:
                ignored.append(
                    IgnoredEvidence(
                        chunk_id=chunk.chunk_id,
                        title=chunk.title,
                        reason="Redundant section chunk; higher-confidence chunk retained for this document",
                        score=calibrated_score
                    )
                )
                continue

            seen_doc_ids.add(dedup_key)
            scored_candidates.append((calibrated_score, chunk))

        # Sort by calibrated score descending
        scored_candidates.sort(key=lambda x: x[0], reverse=True)
        active_chunks = [c for _, c in scored_candidates[:top_n]]

        # Mark excess chunks as ignored
        for _, excess_chunk in scored_candidates[top_n:]:
            ignored.append(
                IgnoredEvidence(
                    chunk_id=excess_chunk.chunk_id,
                    title=excess_chunk.title,
                    reason=f"Ranked outside top {top_n} highest-evidence candidates",
                    score=excess_chunk.relevance_score
                )
            )

        return active_chunks, ignored

