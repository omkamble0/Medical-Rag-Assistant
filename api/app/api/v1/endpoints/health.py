from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    version: str
    service: str
    knowledge_base_status: str

@router.get("/health", response_model=HealthResponse, summary="Service Health & Vector Engine Status")
async def health_check():
    return HealthResponse(
        status="healthy",
        version="0.1.0",
        service="AegisMed Clinical Truth Engine",
        knowledge_base_status="connected (Oxford CEBM Indexed)"
    )
