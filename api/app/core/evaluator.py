import re
from typing import List, Tuple
from app.models.schemas import ConfidenceMetrics, SourceDocument
from app.models.enums import ConfidenceStatus

def evaluate_grounding_and_confidence(
    answer: str,
    sources: List[SourceDocument],
    current_year: int = 2026
) -> Tuple[ConfidenceMetrics, List[int]]:
    """
    Computes a composite confidence score based on:
    1. Semantic retrieval relevance (0.40 weight)
    2. Citation density & claim grounding (0.40 weight)
    3. Evidence freshness / recency (0.20 weight)
    """
    if not sources:
        return ConfidenceMetrics(
            overall_score=0.20,
            status=ConfidenceStatus.LOW,
            retrieval_relevance=0.0,
            grounding_ratio=0.0,
            evidence_freshness=0.5,
            explanation="No verified clinical sources were retrieved for this query."
        ), []

    # 1. Retrieval Relevance (average top scores)
    avg_relevance = sum(s.relevance_score for s in sources) / len(sources)

    # 2. Extract cited indices [1], [2], [1, 2]
    citation_matches = re.findall(r"\[(\d+(?:,\s*\d+)*)\]", answer)
    cited_indices = set()
    for match in citation_matches:
        for idx_str in match.split(","):
            try:
                cited_indices.add(int(idx_str.strip()))
            except ValueError:
                pass
                
    cited_list = sorted(list(cited_indices))
    
    # Grounding ratio: proportion of retrieved sources that were actually referenced in the answer
    # and presence of at least 2 citations for robust grounding
    valid_source_indices = {s.citation_index for s in sources}
    valid_citations_used = [idx for idx in cited_list if idx in valid_source_indices]
    
    if len(sources) > 0:
        source_utilization = min(1.0, len(valid_citations_used) / len(sources))
    else:
        source_utilization = 0.0

    sentence_count = max(1, len([s for s in re.split(r"[.!?]+", answer) if len(s.strip()) > 10]))
    citation_density = min(1.0, len(citation_matches) / max(2, sentence_count * 0.5))
    grounding_ratio = round(0.5 * source_utilization + 0.5 * citation_density, 2)

    # 3. Evidence Freshness (Publications within 5 years get 1.0, decayed smoothly)
    avg_year = sum(s.year for s in sources) / len(sources)
    year_diff = max(0, current_year - avg_year)
    freshness = max(0.4, round(1.0 - (year_diff * 0.04), 2))

    # Composite weighted score (0.0 to 1.0)
    composite = (0.40 * avg_relevance) + (0.40 * grounding_ratio) + (0.20 * freshness)
    overall_score = round(min(0.99, max(0.10, composite)), 2)

    # Determine status tier
    if overall_score >= 0.82:
        status = ConfidenceStatus.HIGH
        explanation = f"High evidentiary consensus. Grounded across {len(valid_citations_used)} peer-reviewed clinical sources with strong semantic alignment."
    elif overall_score >= 0.65:
        status = ConfidenceStatus.MODERATE
        explanation = "Moderate evidentiary certainty. Findings are substantiated by clinical literature, but further domain-specific validation is recommended."
    else:
        status = ConfidenceStatus.LOW
        explanation = "Low confidence. Sparse or indirect source alignment detected. Exercise heightened clinical caution."

    metrics = ConfidenceMetrics(
        overall_score=overall_score,
        status=status,
        retrieval_relevance=round(avg_relevance, 2),
        grounding_ratio=grounding_ratio,
        evidence_freshness=freshness,
        explanation=explanation
    )

    return metrics, cited_list
