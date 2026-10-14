import sys
import logging
from pathlib import Path

# Ensure api directory is on sys.path regardless of how main.py is invoked
API_ROOT = Path(__file__).resolve().parent.parent
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))

# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1.router import api_router
from app.routes.medical_query import router as medical_query_router
from app.routes.research_recommendations import router as research_router
from app.routes.validate import router as validate_router
from app.routes.agentic_pipeline import router as agentic_router
from app.routes.medical_database import router as medical_database_router
from app.routes.chat import router as chat_router

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Agentic Evidence-Based Clinical RAG Engine with Query Guard & Audience-Aware Routing",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware for Next.js frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(chat_router)
app.include_router(medical_query_router)
app.include_router(research_router)
app.include_router(validate_router)
app.include_router(agentic_router)
app.include_router(medical_database_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to AegisMed Clinical Truth Engine API",
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, app_dir=str(API_ROOT))
