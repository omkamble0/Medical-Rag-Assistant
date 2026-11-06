import os
import sys
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # Core Application & Environment
    PROJECT_NAME: str = "AegisMed Clinical Truth Engine"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = Field(default="development", description="development | staging | production | test")
    DEBUG: bool = False
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]

    # Offline / Test Fast Switch (Prevents network socket timeouts during tests)
    OFFLINE_MODE: bool = Field(default=False, description="When true, uses local clinical engines without attempting network calls")
    IS_TESTING: bool = False

    @property
    def is_offline(self) -> bool:
        return (
            self.OFFLINE_MODE
            or self.IS_TESTING
            or os.getenv("OFFLINE_MODE") in ("1", "true")
            or bool(os.getenv("PYTEST_CURRENT_TEST"))
            or "pytest" in sys.modules
        )

    # LLM & Vector Store Settings
    OPENAI_API_KEY: str = Field(default="placeholder_key", repr=False)
    ANTHROPIC_API_KEY: str = Field(default="placeholder_key", repr=False)
    GEMINI_API_KEY: str = Field(default="", repr=False)
    GOOGLE_API_KEY: str = Field(default="", repr=False)
    GROQ_API_KEY: str = Field(default="", repr=False)
    GEMINI_MODEL: str = "gemini-flash-latest"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_TIMEOUT: float = 2.0

    # Qdrant Vector & Document Database (Local or Cloud)
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_URL: Optional[str] = None
    QDRANT_API_KEY: Optional[str] = Field(default=None, repr=False)
    QDRANT_COLLECTION: str = "clinical_evidence_v1"
    QDRANT_TIMEOUT: float = 3.0

    # Relational Database & Redis Cache
    DATABASE_URL: str = "sqlite:///./api/app/data/clinical_audit_trails.db"
    REDIS_URL: Optional[str] = None
    CACHE_TTL_SECONDS: int = 86400  # 24 hours

    # Grounding & Safety Thresholds
    EMERGENCY_TRIAGE_ENABLED: bool = True
    MIN_CONFIDENCE_THRESHOLD: float = 0.65
    HIGH_CONFIDENCE_THRESHOLD: float = 0.80
    LOW_CONFIDENCE_THRESHOLD: float = 0.50

    # Observability & Metrics
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    PROMETHEUS_METRICS_ENABLED: bool = True
    OPENTELEMETRY_ENABLED: bool = True

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env", "api/.env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    def is_production(self) -> bool:
        return self.ENVIRONMENT.lower() == "production"


settings = Settings()
