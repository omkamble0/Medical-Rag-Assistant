"""
LLM Provider Interface Specification for AegisMed.
Defines contracts for clinical LLM generation, multi-turn chat, structured output schemas,
and fallback cascades across OpenAI, Groq, Gemini, Ollama, and Local Offline engines.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class LLMMessage(BaseModel):
    role: str = Field(..., description="'system' | 'user' | 'assistant'")
    content: str


class LLMResponse(BaseModel):
    content: Optional[str] = None
    provider: str
    model: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    latency_ms: float = 0.0
    status: str = "success"  # "success" | "fallback" | "error"
    error: Optional[str] = None


class LLMProviderInterface(ABC):
    """Abstract interface for LLM model providers."""

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> LLMResponse:
        """Single-turn prompt completion."""
        pass

    @abstractmethod
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> LLMResponse:
        """Multi-turn conversation chat completion."""
        pass

    @abstractmethod
    def get_provider_name(self) -> str:
        """Returns the canonical provider name."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Health-checks whether provider is accessible."""
        pass

