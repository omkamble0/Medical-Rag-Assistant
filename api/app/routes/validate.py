# api/app/routes/validate.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import logging
from app.services.query_validator import validator

router = APIRouter(prefix="/api/v1", tags=["query-validation"])
logger = logging.getLogger(__name__)

class ValidationRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="Query string to validate")

class ValidationResponse(BaseModel):
    original: str
    corrected: str
    is_valid: bool
    corrections_made: List[str]
    confidence_score: float
    medical_terms_found: List[str]
    medical_terms_details: Optional[List[Dict[str, Any]]] = None
    issues: List[str]

@router.post("/validate-query", response_model=ValidationResponse)
async def validate_query(request: ValidationRequest):
    """
    Validate medical query, detect typos, and normalize medical terminology.
    """
    try:
        result = validator.validate_and_correct(request.query)
        return ValidationResponse(**result)
    except Exception as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to validate query: {str(e)}")

@router.get("/validate-query/health")
async def validation_health():
    return {
        "status": "healthy",
        "service": "medical-query-validator",
        "terms_registered": len(validator.terms_db)
    }
