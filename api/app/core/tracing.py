"""
Distributed Request Tracing & OpenTelemetry Hooks for AegisMed.
Propagates X-Request-ID and X-Trace-ID across HTTP headers, logs, and internal tasks.
"""

import uuid
import time
from typing import Optional, Dict, Any
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.core.logging import trace_id_ctx, request_id_ctx, user_mode_ctx


class TraceSpan:
    """Lightweight in-process OpenTelemetry-compatible tracing span."""

    def __init__(self, name: str, trace_id: Optional[str] = None, attributes: Optional[Dict[str, Any]] = None):
        self.name = name
        self.trace_id = trace_id or trace_id_ctx.get() or f"trace-{uuid.uuid4().hex[:16]}"
        self.span_id = uuid.uuid4().hex[:8]
        self.attributes = attributes or {}
        self.start_time = time.time()
        self.end_time: Optional[float] = None
        self.duration_ms: float = 0.0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.duration_ms = round((self.end_time - self.start_time) * 1000, 2)
        if exc_type:
            self.attributes["error"] = True
            self.attributes["error_message"] = str(exc_val)
        return False

    def set_attribute(self, key: str, value: Any):
        self.attributes[key] = value


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    """
    Ensures every request has a unique Request-ID and Trace-ID.
    Binds them to async context vars for structured logging.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        req_id = request.headers.get("X-Request-ID") or f"req-{uuid.uuid4().hex[:12]}"
        trace_id = request.headers.get("X-Trace-ID") or f"trace-{uuid.uuid4().hex[:16]}"

        request_id_ctx.set(req_id)
        trace_id_ctx.set(trace_id)

        # Audience mode context if passed as query or header
        aud = request.headers.get("X-Audience-Mode") or request.query_params.get("mode") or request.query_params.get("audience")
        if aud:
            user_mode_ctx.set(aud)

        response = await call_next(request)
        response.headers["X-Request-ID"] = req_id
        response.headers["X-Trace-ID"] = trace_id
        return response

