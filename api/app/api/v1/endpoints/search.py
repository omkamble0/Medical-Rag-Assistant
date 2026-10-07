from fastapi import APIRouter, HTTPException, status
from app.models.schemas import SearchRequest, SearchResponse, DualCompareResponse
from app.models.enums import UserMode
from app.services.rag_engine import execute_rag_pipeline

router = APIRouter()

@router.post("/search", response_model=SearchResponse, summary="Execute Dual-Mode Clinical Search")
async def search_endpoint(request: SearchRequest):
    """
    Primary RAG endpoint:
    - Checks for Emergency Red Flags (Tier-1 deterministic triage interceptor)
    - Retrieves Oxford CEBM evidence documents
    - Generates Clinician or Patient specialized synthesis
    - Computes Tri-Factor confidence & grounding metrics
    """
    try:
        response = execute_rag_pipeline(request.query, request.user_mode)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the clinical query: {str(e)}"
        )

@router.post("/compare", response_model=DualCompareResponse, summary="Compare Clinician and Patient Perspectives")
async def compare_perspectives_endpoint(request: SearchRequest):
    """
    Novel feature: Generates both Clinician and Patient explanations simultaneously
    over the exact same retrieved evidence set for synchronized provider-patient review.
    """
    try:
        pro_res = execute_rag_pipeline(request.query, UserMode.PROFESSIONAL)
        patient_res = execute_rag_pipeline(request.query, UserMode.PATIENT)
        
        return DualCompareResponse(
            query=request.query,
            professional_response=pro_res,
            patient_response=patient_res,
            shared_sources=pro_res.sources
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate comparative perspectives: {str(e)}"
        )
