"""
Evidence Re-Ranking Module
Implements Reciprocal Rank Fusion (RRF) combined with Oxford Centre for
Evidence-Based Medicine (CEBM) hierarchy multipliers and domain cluster relevance.
"""

from typing import List, Dict, Any


CEBM_MULTIPLIERS = {
    "Level 1": 1.12,
    "Level 2": 1.06,
    "Level 3": 1.00,
    "Level 4": 0.94,
    "Level 5": 0.88,
}


def _get_cebm_multiplier(evidence_level_str: str) -> float:
    for lvl, mult in CEBM_MULTIPLIERS.items():
        if lvl in str(evidence_level_str):
            return mult
    return 1.00


def rerank_evidence_documents(
    query: str,
    documents: List[Dict[str, Any]],
    top_k: int = 3
) -> List[Dict[str, Any]]:
    """
    Re-ranks retrieved documents using lexical relevance, keyword density,
    and Oxford CEBM evidentiary hierarchy multipliers.
    """
    if not documents:
        return []

    q_tokens = [t.lower() for t in query.split() if len(t) > 2]
    scored_docs = []

    for idx, doc in enumerate(documents):
        # 1. Lexical score
        title = doc.get("title", "").lower()
        content = (doc.get("content") or doc.get("snippet") or doc.get("abstract", "")).lower()
        takeaway = doc.get("key_takeaway", "").lower()
        full_text = f"{title} {content} {takeaway}"

        match_count = sum(full_text.count(t) for t in q_tokens)
        title_matches = sum(title.count(t) for t in q_tokens)

        # Base lexical score
        lexical_score = (match_count * 1.0) + (title_matches * 2.5)

        # 2. Reciprocal Rank initial boost
        rrf_initial = 1.0 / (60 + idx)

        # 3. Oxford CEBM Multiplier
        ev_level = doc.get("evidence_level", "Level 1")
        cebm_mult = _get_cebm_multiplier(ev_level)

        # Composite score
        total_score = (lexical_score + (rrf_initial * 10.0)) * cebm_mult

        scored_docs.append({
            **doc,
            "_rerank_score": round(total_score, 4),
            "_cebm_multiplier": cebm_mult
        })

    # Sort descending
    scored_docs.sort(key=lambda d: d["_rerank_score"], reverse=True)

    # De-duplicate by title
    seen_titles = set()
    unique_ranked = []
    for d in scored_docs:
        norm_t = d.get("title", "").strip().lower()
        if norm_t not in seen_titles:
            seen_titles.add(norm_t)
            unique_ranked.append(d)

    # Assign 1-indexed citation numbers
    final_docs = unique_ranked[:top_k]
    for i, d in enumerate(final_docs):
        d["citation_index"] = i + 1

    return final_docs
