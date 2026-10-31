"""
Prometheus & Observability Metrics Module for AegisMed.
Collects and serves real-time performance indicators, LLM token metrics,
fallback rates, and safety interception counters.
"""

import time
import threading
from typing import Dict, Any, List
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse


class MetricsRegistry:
    """Thread-safe in-memory metrics registry for Prometheus exposition."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MetricsRegistry, cls).__new__(cls)
                cls._instance._init_metrics()
            return cls._instance

    def _init_metrics(self):
        self._request_counts: Dict[str, int] = {}
        self._latencies: Dict[str, List[float]] = {}
        self._safety_triggers: Dict[str, int] = {}
        self._fallback_counts: Dict[str, int] = {}
        self._token_counts: Dict[str, int] = {"prompt_tokens": 0, "completion_tokens": 0}
        self._retrieval_stats: Dict[str, int] = {"hits": 0, "misses": 0, "zero_confidence": 0}

    def record_request(self, endpoint: str, status_code: int, duration_sec: float):
        with self._lock:
            key = f'{endpoint}:{status_code}'
            self._request_counts[key] = self._request_counts.get(key, 0) + 1
            if endpoint not in self._latencies:
                self._latencies[endpoint] = []
            self._latencies[endpoint].append(duration_sec)
            # Keep sliding window of latest 500 samples
            if len(self._latencies[endpoint]) > 500:
                self._latencies[endpoint] = self._latencies[endpoint][-500:]

    def record_query(self, duration_ms: float = 0.0, success: bool = True, audience: str = "patient"):
        self.record_request(f"/api/v1/clinical/query?audience={audience}", 200 if success else 500, duration_ms / 1000.0)

    def record_safety_trigger(self, category: str = "", rule_name: str = ""):
        cat = category or rule_name or "general"
        with self._lock:
            self._safety_triggers[cat] = self._safety_triggers.get(cat, 0) + 1

    def record_fallback(self, provider: str, reason: str):
        with self._lock:
            key = f"{provider}:{reason}"
            self._fallback_counts[key] = self._fallback_counts.get(key, 0) + 1

    def record_tokens(self, prompt_tokens: int, completion_tokens: int):
        with self._lock:
            self._token_counts["prompt_tokens"] += prompt_tokens
            self._token_counts["completion_tokens"] += completion_tokens

    def record_retrieval(self, hit: bool = True, hits: int = 0, misses: int = 0, is_zero_confidence: bool = False):
        with self._lock:
            if is_zero_confidence:
                self._retrieval_stats["zero_confidence"] += 1
            if hits > 0:
                self._retrieval_stats["hits"] += hits
            elif hit:
                self._retrieval_stats["hits"] += 1
            if misses > 0:
                self._retrieval_stats["misses"] += misses
            elif not hit:
                self._retrieval_stats["misses"] += 1

    def get_summary(self) -> Dict[str, Any]:
        with self._lock:
            latency_summary: Dict[str, Dict[str, float]] = {}
            for ep, samples in self._latencies.items():
                if samples:
                    sorted_samples = sorted(samples)
                    n = len(sorted_samples)
                    latency_summary[ep] = {
                        "p50_ms": round(sorted_samples[int(n * 0.50)] * 1000, 2),
                        "p95_ms": round(sorted_samples[min(int(n * 0.95), n - 1)] * 1000, 2),
                        "p99_ms": round(sorted_samples[min(int(n * 0.99), n - 1)] * 1000, 2),
                        "count": n
                    }
            return {
                "total_queries": sum(self._request_counts.values()),
                "request_counts": dict(self._request_counts),
                "latencies": latency_summary,
                "safety_triggers": dict(self._safety_triggers),
                "fallback_counts": dict(self._fallback_counts),
                "token_usage": dict(self._token_counts),
                "retrieval_stats": dict(self._retrieval_stats)
            }

    def export_prometheus(self) -> str:
        """Renders metrics in standard Prometheus text format."""
        lines: List[str] = [
            "# HELP aegismed_requests_total Total requests processed",
            "# TYPE aegismed_requests_total counter",
            "# HELP aegismed_http_requests_total Total HTTP requests handled",
            "# TYPE aegismed_http_requests_total counter"
        ]
        with self._lock:
            for k, count in self._request_counts.items():
                ep, sc = k.rsplit(":", 1)
                lines.append(f'aegismed_requests_total{{endpoint="{ep}"}} {count}')
                lines.append(f'aegismed_http_requests_total{{endpoint="{ep}",status="{sc}"}} {count}')

            lines.append("# HELP aegismed_safety_triggers_total Safety and red flag intercepts")
            lines.append("# TYPE aegismed_safety_triggers_total counter")
            for cat, count in self._safety_triggers.items():
                lines.append(f'aegismed_safety_triggers_total{{category="{cat}"}} {count}')

            lines.append("# HELP aegismed_fallbacks_total Fallbacks to local synthesis or BM25")
            lines.append("# TYPE aegismed_fallbacks_total counter")
            for fb, count in self._fallback_counts.items():
                lines.append(f'aegismed_fallbacks_total{{reason="{fb}"}} {count}')

            lines.append("# HELP aegismed_tokens_total Token usage counts")
            lines.append("# TYPE aegismed_tokens_total counter")
            for t_type, count in self._token_counts.items():
                lines.append(f'aegismed_tokens_total{{type="{t_type}"}} {count}')

            lines.append("# HELP aegismed_retrieval_events_total Retrieval hit/miss events")
            lines.append("# TYPE aegismed_retrieval_events_total counter")
            for stat, count in self._retrieval_stats.items():
                lines.append(f'aegismed_retrieval_events_total{{status="{stat}"}} {count}')

            lines.append("# HELP aegismed_query_latency_ms Query execution latency in milliseconds")
            lines.append("# TYPE aegismed_query_latency_ms gauge")
            has_latency = False
            for ep, samples in self._latencies.items():
                if samples:
                    sorted_samples = sorted(samples)
                    p50 = round(sorted_samples[int(len(sorted_samples) * 0.50)] * 1000, 2)
                    lines.append(f'aegismed_query_latency_ms{{endpoint="{ep}",quantile="p50"}} {p50}')
                    has_latency = True
            if not has_latency:
                lines.append('aegismed_query_latency_ms{endpoint="default",quantile="p50"} 0.0')

        return "\n".join(lines) + "\n"


metrics = MetricsRegistry()


class MetricsMiddleware(BaseHTTPMiddleware):
    """Measures latency and logs request status for all incoming requests."""

    async def dispatch(self, request: Request, call_next) -> Response:
        # Skip metrics endpoint itself to avoid noise
        if request.url.path in ("/metrics", "/api/v1/metrics", "/docs", "/openapi.json"):
            return await call_next(request)

        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time

        metrics.record_request(
            endpoint=request.url.path,
            status_code=response.status_code,
            duration_sec=duration
        )
        return response

