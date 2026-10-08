from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.config import settings
from app.api.v1.router import api_router
from app.routes.simplify import router as simplify_router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Initializing Medical Simplifier...")
    try:
        from app.services.medical_simplifier import medical_simplifier
        await medical_simplifier.initialize_model()
        logger.info("Medical Simplifier ready!")
    except Exception as e:
        logger.warning(f"Medical Simplifier pre-loading skipped (will load on first request): {e}")
    yield
    # Shutdown
    logger.info("Shutting down Medical Simplifier...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Dual-Mode Evidence-Based Clinical RAG Engine with Oxford CEBM Grounding & Tier-1 Safety Guardrails",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware for Next.js frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include v1 routes
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(simplify_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to AegisMed Clinical Truth Engine API",
        "docs": "/docs",
        "health": f"{settings.API_V1_STR}/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
