"""
Cache Backend Interface Specification for AegisMed.
Defines contracts for caching clinical queries, vector embeddings, and PubMed results.
"""

from abc import ABC, abstractmethod
from typing import Optional, Any


class CacheBackendInterface(ABC):
    """Abstract interface for caching engines (Redis / In-Memory)."""

    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        pass

    @abstractmethod
    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> bool:
        pass

    @abstractmethod
    def delete(self, key: str) -> bool:
        pass

    @abstractmethod
    def clear(self) -> bool:
        pass

