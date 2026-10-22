from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "AegisMed Clinical Truth Engine"
    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # LLM & Vector Store Settings
    OPENAI_API_KEY: str = "placeholder_key"
    ANTHROPIC_API_KEY: str = "placeholder_key"
    GEMINI_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_TIMEOUT: float = 20.0
    
    # Qdrant Vector & Document Database (Local or Cloud)
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_URL: Optional[str] = None       # e.g., "https://xxxxxx-xxxx-xxxx.us-east4-0.gcp.cloud.qdrant.io:6333"
    QDRANT_API_KEY: Optional[str] = None   # Qdrant Cloud Cluster API Key
    QDRANT_COLLECTION: str = "clinical_evidence_v1"
    
    # Grounding & Safety Thresholds
    EMERGENCY_TRIAGE_ENABLED: bool = True
    MIN_CONFIDENCE_THRESHOLD: float = 0.65

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env", "api/.env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()

