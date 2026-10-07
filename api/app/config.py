try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseModel as BaseSettings

from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "AegisMed Clinical Truth Engine"
    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # LLM & Vector Store Settings
    OPENAI_API_KEY: str = "placeholder_key"
    ANTHROPIC_API_KEY: str = "placeholder_key"
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "clinical_evidence_v1"
    
    # Grounding & Safety Thresholds
    EMERGENCY_TRIAGE_ENABLED: bool = True
    MIN_CONFIDENCE_THRESHOLD: float = 0.65

settings = Settings()
