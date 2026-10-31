"""
Structured JSON Logging Module for AegisMed Clinical Truth Engine.
Provides production-grade JSON log output with correlation IDs, latency tracking,
contextual clinical metadata, and safe exception formatting.
"""

import os
import sys
import json
import logging
from typing import Any, Dict, Optional
from datetime import datetime, timezone
import contextvars

# Context variables for distributed request tracing
trace_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("trace_id", default=None)
request_id_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("request_id", default=None)
user_mode_ctx: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar("user_mode", default=None)


class StructuredJsonFormatter(logging.Formatter):
    """
    Formats log records as single-line JSON objects for log aggregators
    (Datadog, CloudWatch, Google Cloud Logging, Loki).
    """

    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "file": f"{record.filename}:{record.lineno}",
            "function": record.funcName,
        }

        # Inject tracing context if present
        tid = trace_id_ctx.get()
        if tid:
            log_entry["trace_id"] = tid

        rid = request_id_ctx.get()
        if rid:
            log_entry["request_id"] = rid

        mode = user_mode_ctx.get()
        if mode:
            log_entry["audience_mode"] = mode

        # Inject extra attributes passed in record.__dict__
        if hasattr(record, "extra_fields") and isinstance(record.extra_fields, dict):
            log_entry.update(record.extra_fields)

        # Handle exceptions safely
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry, default=str)


def setup_structured_logging(log_level: str = "INFO", use_json: bool = True) -> logging.Logger:
    """Configures root logger with structured formatting."""
    root_logger = logging.getLogger()
    level = getattr(logging, log_level.upper(), logging.INFO)
    root_logger.setLevel(level)

    # Avoid duplicate handlers on reload
    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        if use_json:
            handler.setFormatter(StructuredJsonFormatter())
        else:
            handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
        root_logger.addHandler(handler)

    return logging.getLogger("aegismed")


logger = setup_structured_logging(
    log_level=os.getenv("LOG_LEVEL", "INFO"),
    use_json=os.getenv("LOG_FORMAT", "json").lower() == "json"
)

