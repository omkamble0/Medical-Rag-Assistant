"""
Hybrid Clinical Evidence Retriever for AegisMed.
Implements RetrieverInterface, uniting BM25 Sparse Lexical search and
Dense Vector Embeddings via Reciprocal Rank Fusion (RRF) with Oxford CEBM hierarchy.
"""

import time
from typing import List, Dict, Any, Optional
from app.interfaces.retriever import (
    RetrieverInterface,
    RetrievedChunk,
    IgnoredEvidence,
    RetrievalResult
)
from app.retrieval.bm25 import BM25Index
from app.retrieval.reranker import ClinicalEvidenceReranker
from app.retrieval.chunker import MedicalContentChunker
from app.services.medical_db import medical_db


class HybridClinicalRetriever(RetrieverInterface):
    """
    Hybrid Evidence Retriever:
    1. Sparse BM25 retrieval for precise drug names, gene symbols, and medical terms
    2. Dense vector similarity for semantic symptom concepts
    3. Reciprocal Rank Fusion (RRF) with CEBM grade weighting
    4. Reranker filtering with explicit ignored evidence tracking
    """

    def __init__(self, rrf_k: int = 60, min_score: float = 0.35):
        self.rrf_k = rrf_k
        self.min_score = min_score
        self.reranker = ClinicalEvidenceReranker(min_relevance_threshold=min_score)
        self.bm25 = BM25Index()
        self._all_chunks: List[RetrievedChunk] = []
        self._initialized = False

    def _ensure_chunks_indexed(self):
        if not self._initialized:
            # Build chunks from medical_db records
            all_records = medical_db.get_diseases(limit=600)
            chunks: List[RetrievedChunk] = []
            for r in all_records:
                chunks.extend(MedicalContentChunker.chunk_disease_record(r))
            self._all_chunks = chunks
            self.bm25.index_chunks(chunks)
            self._initialized = True

    def retrieve_sync(
        self,
        query: str,
        top_k: int = 4,
        filters: Optional[Dict[str, Any]] = None,
        min_score: float = 0.0
    ) -> RetrievalResult:
        start_time = time.time()
        self._ensure_chunks_indexed()

        threshold = max(min_score, self.min_score)

        # 1. BM25 Lexical Candidates
        bm25_matches = self.bm25.search(query, top_k=top_k * 3)
        bm25_ranks = {chunk.chunk_id: rank for rank, (chunk, _) in enumerate(bm25_matches, start=1)}
        bm25_chunk_map = {chunk.chunk_id: chunk for chunk, _ in bm25_matches}

        # 2. Vector / Medical DB Hybrid Candidates
        vec_candidates = medical_db.search_hybrid(query, top_k=top_k * 2)
        vec_ranks = {}
        for rank, candidate in enumerate(vec_candidates, start=1):
            disease = candidate.get("record")
            if disease:
                disease_chunks = MedicalContentChunker.chunk_disease_record(disease)
                for c in disease_chunks:
                    if c.chunk_id not in vec_ranks:
                        vec_ranks[c.chunk_id] = rank
                        bm25_chunk_map[c.chunk_id] = c

        # 3. Reciprocal Rank Fusion (RRF)
        fused_scores: Dict[str, float] = {}
        all_candidate_ids = set(bm25_ranks.keys()) | set(vec_ranks.keys())

        for c_id in all_candidate_ids:
            r_bm25 = bm25_ranks.get(c_id, 999)
            r_vec = vec_ranks.get(c_id, 999)

            score_bm25 = 1.0 / (self.rrf_k + r_bm25) if r_bm25 != 999 else 0.0
            score_vec = 1.0 / (self.rrf_k + r_vec) if r_vec != 999 else 0.0

            # Scale to 0.0 - 1.0 range
            rrf_score = min(1.0, (score_bm25 * 30.0) + (score_vec * 30.0))
            fused_scores[c_id] = rrf_score

        # Assemble retrieved chunks with RRF scores
        candidates_to_rerank: List[RetrievedChunk] = []
        for c_id, rrf_score in fused_scores.items():
            chunk = bm25_chunk_map.get(c_id)
            if chunk:
                # Apply metadata filters if provided
                if filters:
                    skip = False
                    for fk, fv in filters.items():
                        if fk in chunk.metadata and chunk.metadata[fk] != fv:
                            skip = True
                            break
                    if skip:
                        continue

                chunk.relevance_score = rrf_score
                candidates_to_rerank.append(chunk)

        # 4. Rerank and segregate ignored chunks
        active_chunks, ignored_chunks = self.reranker.rerank(
            query=query,
            chunks=candidates_to_rerank,
            top_n=top_k
        )

        mean_conf = (
            sum(c.relevance_score for c in active_chunks) / len(active_chunks)
            if active_chunks else 0.0
        )
        latency = (time.time() - start_time) * 1000

        return RetrievalResult(
            query=query,
            active_chunks=active_chunks,
            ignored_chunks=ignored_chunks,
            mean_confidence=round(mean_conf, 3),
            retrieval_method="hybrid_bm25_vector_rrf",
            latency_ms=round(latency, 2)
        )

    async def retrieve(
        self,
        query: str,
        top_k: int = 4,
        filters: Optional[Dict[str, Any]] = None,
        min_score: float = 0.0
    ) -> RetrievalResult:
        return self.retrieve_sync(query=query, top_k=top_k, filters=filters, min_score=min_score)

