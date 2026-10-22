"""
API Endpoints for 133,000+ CMS ICD-10-CM & WHO ICD-11 Clinical Taxonomy Search & Lookup.
"""

from fastapi import APIRouter, HTTPException, Query, status
from typing import Optional, List, Dict, Any
import time

from app.services.taxonomy_service import taxonomy_service, TaxonomyEntity, TaxonomySearchResponse

router = APIRouter(prefix="/api/v1/taxonomy", tags=["CMS & WHO Clinical Taxonomy"])


@router.get("/stats", summary="Get Taxonomy Database Statistics")
def get_taxonomy_statistics():
    """Returns total condition counts across CMS ICD-10 and WHO ICD-11."""
    return taxonomy_service.get_stats()


@router.get("/search", response_model=TaxonomySearchResponse, summary="Search 133,000+ CMS & WHO Medical Conditions")
def search_clinical_taxonomy(
    query: str = Query(..., min_length=1, description="Condition name, symptom, or diagnostic code (e.g. 'cholera', 'I10', 'asthma')"),
    source: Optional[str] = Query(None, description="Optional filter: 'CMS_ICD10' or 'WHO_ICD11'"),
    limit: int = Query(25, ge=1, le=100, description="Max results to return")
):
    """
    Sub-millisecond FTS5 search across 97,584 CMS ICD-10-CM diagnostic codes
    and 36,044 WHO ICD-11 entities.
    """
    t0 = time.time()
    results = taxonomy_service.search(query=query, source=source, limit=limit)
    latency = round((time.time() - t0) * 1000, 2)

    return TaxonomySearchResponse(
        total_matches=len(results),
        query=query,
        results=[TaxonomyEntity(**r) for r in results],
        latency_ms=latency
    )


@router.get("/code/{code}", summary="Lookup Condition by Diagnostic Code")
def get_condition_by_code(code: str):
    """Retrieves full classification details for an exact ICD-10 or ICD-11 code."""
    res = taxonomy_service.get_by_code(code)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Condition code '{code}' not found in CMS or WHO catalog."
        )
    return res
