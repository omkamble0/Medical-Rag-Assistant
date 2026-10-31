"""
Retriever Interface Specification for AegisMed.
Defines standard contracts for vector, BM25, hybrid, and citation-aware retrievers.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple
from pydantic import BaseModel, Field
from app.models.enums import EvidenceLevel


class RetrievedChunk(BaseModel):
    chunk_id: str = Field(..., description="Globally unique chunk identifier, e.g. CHK-DOC-CARD-001-S3")
    document_id: str = ""
    title: str
    journal: Optional[str] = None
    year: Optional[int] = None
    evidence_level: str = "Level 1"
    section_name: str = "indication"
    domain: Optional[str] = "GENERAL_MEDICINE"
    text: str
    relevance_score: float = 0.0
    is_cited: bool = False
    is_contraindication: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)

    def __init__(self, **data):
        if "doc_id" in data and not data.get("document_id"):
            data["document_id"] = data["doc_id"]
        if "is_contraindication" not in data:
            sec = str(data.get("section_name", "")).lower()
            txt = str(data.get("text", "")).lower()
            if "contraindication" in sec or "contraindication" in txt:
                data["is_contraindication"] = True
        super().__init__(**data)


class IgnoredEvidence(BaseModel):
    chunk_id: str
    title: str
    reason: str = Field(..., description="e.g. 'Below relevance threshold', 'Contraindicated in pregnancy', 'Duplicate information'")
    score: float


class RetrievalResult(BaseModel):
    query: str
    active_chunks: List[RetrievedChunk]
    ignored_chunks: List[IgnoredEvidence]
    mean_confidence: float
    retrieval_method: str = "hybrid_rrf"
    latency_ms: float = 0.0


class RetrieverInterface(ABC):
    """Abstract interface for clinical evidence retrieval engines."""

    @abstractmethod
    async def retrieve(
        self,
        query: str,
        top_k: int = 5,
        filters: Optional[Dict[str, Any]] = None,
        min_score: float = 0.0
    ) -> RetrievalResult:
        """Retrieves and scores clinical chunks matching the clinical query."""
        pass


class RerankerInterface(ABC):
    """Abstract interface for evidence rerankers."""

    @abstractmethod
    def rerank(
        self,
        query: str,
        chunks: List[RetrievedChunk],
        top_n: int = 3
    ) -> Tuple[List[RetrievedChunk], List[IgnoredEvidence]]:
        """Reranks candidate chunks and segregates ignored/sub-threshold chunks."""
        pass
