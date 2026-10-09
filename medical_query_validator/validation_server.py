# medical_query_validator/validation_server.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import logging
from query_validator import validator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Medical Query Validation Service",
    description="3-Layer Medical Query Typo Correction & Entity Grounding Layer",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/validate-query", response_model=ValidationResponse)
async def validate_query_endpoint(request: ValidationRequest):
    """
    Validate medical query, correct typos, and extract clinical concepts.
    
    Example:
    POST /validate-query
    {
      "query": "I have headavhe and diabtes"
    }
    """
    try:
        result = validator.validate_and_correct(request.query)
        return ValidationResponse(**result)
    except Exception as e:
        logger.error(f"Query validation error: {e}")
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "medical-query-validator",
        "terms_count": len(validator.terms_db)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("validation_server:app", host="0.0.0.0", port=8001, reload=True)
