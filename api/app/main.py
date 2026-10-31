# pyrefly: ignore-errors[missing-import]
import sys
import logging
from pathlib import Path

# Ensure api directory is on sys.path regardless of how main.py is invoked
API_ROOT = Path(__file__).resolve().parent.parent
if str(API_ROOT) not in sys.path:
    sys.path.insert(0, str(API_ROOT))

from fastapi import FastAPI  # type: ignore # pyrefly: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore # pyrefly: ignore
from fastapi.responses import PlainTextResponse  # type: ignore # pyrefly: ignore

from app.config import settings  # type: ignore # pyrefly: ignore
from app.core.logging import setup_structured_logging
from app.core.security import SecurityHeadersMiddleware
from app.core.tracing import CorrelationIdMiddleware
from app.core.metrics import MetricsMiddleware, metrics

from app.api.v1.router import api_router  # type: ignore # pyrefly: ignore
from app.routes.validate import router as validate_router  # type: ignore # pyrefly: ignore
from app.routes.medical_query import router as medical_query_router  # type: ignore # pyrefly: ignore
from app.routes.research_recommendations import router as research_router  # type: ignore # pyrefly: ignore
from app.routes.agentic_pipeline import router as agentic_router  # type: ignore # pyrefly: ignore
from app.routes.medical_database import router as medical_database_router  # type: ignore # pyrefly: ignore
from app.routes.chat import router as chat_router  # type: ignore # pyrefly: ignore
from app.routes.encyclopedia import router as encyclopedia_router  # type: ignore # pyrefly: ignore
from app.routes.taxonomy import router as taxonomy_router  # type: ignore # pyrefly: ignore
from app.routes.audit import router as audit_router  # type: ignore # pyrefly: ignore
from app.routes.clinical_production import router as clinical_production_router  # type: ignore # pyrefly: ignore

logger = setup_structured_logging(log_level=settings.LOG_LEVEL)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Agentic Evidence-Based Clinical RAG Engine with Layered Architecture, Query Guard & Safety Interceptors",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 4. CORS middleware for Next.js frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS if settings.CORS_ORIGINS else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Prometheus scraper mount
@app.get("/metrics", response_class=PlainTextResponse, tags=["Observability"])
async def root_prometheus_metrics():
    return PlainTextResponse(metrics.export_prometheus(), media_type="text/plain; version=0.0.4")

# Include production layered architecture routes
app.include_router(clinical_production_router)

# Include legacy routes for 100% backwards compatibility
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(chat_router)
app.include_router(validate_router)
app.include_router(medical_query_router)
app.include_router(research_router)
app.include_router(agentic_router)
app.include_router(medical_database_router)
app.include_router(encyclopedia_router)
app.include_router(taxonomy_router)
app.include_router(audit_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to AegisMed Clinical Truth Engine API",
        "version": "2.0.0",
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health",
        "metrics": "/metrics",
        "structured_query": f"{settings.API_V1_STR}/clinical/query"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, app_dir=str(API_ROOT))
