# api/app/routes/simplify.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import logging

router = APIRouter(prefix="/api/v1", tags=["medical-simplification"])
logger = logging.getLogger(__name__)

class SimplifyRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=5000, description="Medical text to simplify")
    audience: str = Field(..., pattern="^(patient|doctor)$", description="Target audience")
    source: str = Field(default="rag", description="Source of the text")

class SimplifyResponse(BaseModel):
    success: bool
    data: dict
    processing_time_ms: float
    model_version: str

@router.post("/simplify", response_model=SimplifyResponse)
async def simplify_medical_text(request: SimplifyRequest):
    """
    Simplify medical text for patient or doctor audience.
    
    Example:
    POST /api/v1/simplify
    {
      "text": "Acute myocardial infarction with ST-segment elevation",
      "audience": "patient",
      "source": "rag"
    }
    """
    try:
        from app.services.medical_simplifier import medical_simplifier
        
        result = await medical_simplifier.simplify_medical_text(
            text=request.text,
            audience=request.audience,
            source=request.source
        )
        
        return SimplifyResponse(
            success=True,
            data=result,
            processing_time_ms=result["processing_time_ms"],
            model_version="MedSiML-t5-base"
        )
    
    except Exception as e:
        logger.error(f"Simplification error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to simplify text: {str(e)}"
        )

@router.get("/simplify/health")
async def health_check():
    """Health check for simplification service"""
    return {
        "status": "ok",
        "service": "medical-simplifier",
        "model": "MedSiML-t5-base"
    }
