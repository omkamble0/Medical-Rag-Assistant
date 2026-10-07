from fastapi import APIRouter
from app.api.v1.endpoints import search, health

api_router = APIRouter()
api_router.include_router(search.router, tags=["RAG Search & Evidence"])
api_router.include_router(health.router, tags=["System Health"])
