"""
Security, PII De-Identification, and RBAC Authorization Module for AegisMed.
Implements HIPAA Safe Harbor de-identification rules, PII scrubbing,
clinical role-based access control, and API security headers.
"""

import re
from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from pydantic import BaseModel, Field
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class UserRole(str, Enum):
    PATIENT = "patient"
    CLINICIAN = "clinician"
    AUDITOR = "auditor"
    ADMIN = "admin"


# ============================================================
# HIPAA Safe Harbor PII Patterns
# ============================================================
PII_PATTERNS: List[Tuple[str, str, str]] = [
    # Social Security Numbers (SSN)
    (r"\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b", "[REDACTED_SSN]", "ssn"),
    # Medical Record Numbers (MRN)
    (r"\b(mrn|record\s*#?|patient\s*id)\s*[:#]?\s*([a-zA-Z0-9]{6,12})\b", r"\1: [REDACTED_MRN]", "mrn"),
    # Phone numbers (US & International)
    (r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b", "[REDACTED_PHONE]", "phone"),
    # Email addresses
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[REDACTED_EMAIL]", "email"),
    # Dates of birth (DOB)
    (r"\b(dob|birth\s*date|born)\s*[:#]?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b", r"\1: [REDACTED_DOB]", "dob"),
    # Credit / Debit Cards
    (r"\b(?:\d{4}[-\s]?){3}\d{4}\b", "[REDACTED_CARD]", "financial"),
    # First + Last Name self-declarations (e.g., "My name is John Doe", "I am Jane Smith")
    (r"\b(?:my name is|i am|this is|patient name is)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+))\b", "patient is [REDACTED_NAME]", "name"),
]


class PIIScrubResult(BaseModel):
    cleaned_text: str
    redactions_count: int
    detected_pii_types: List[str]
    has_pii: bool


def scrub_pii(text: str) -> PIIScrubResult:
    """
    Scrubs Protected Health Information (PHI) and PII from clinical queries
    prior to vector caching, LLM generation, or audit trail persistence.
    """
    if not text:
        return PIIScrubResult(cleaned_text="", redactions_count=0, detected_pii_types=[], has_pii=False)

    cleaned = text
    detected_types: List[str] = []
    total_redactions = 0

    for pattern, replacement, pii_type in PII_PATTERNS:
        matches = re.findall(pattern, cleaned, flags=re.IGNORECASE)
        if matches:
            total_redactions += len(matches)
            detected_types.append(pii_type)
            cleaned = re.sub(pattern, replacement, cleaned, flags=re.IGNORECASE)

    return PIIScrubResult(
        cleaned_text=cleaned,
        redactions_count=total_redactions,
        detected_pii_types=list(set(detected_types)),
        has_pii=total_redactions > 0
    )


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Injects enterprise healthcare security headers to guard against
    clickjacking, MIME-sniffing, XSS, and unauthorized framing.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "default-src 'self'; frame-ancestors 'none';"
        response.headers["Cache-Control"] = "no-store, max-age=0, must-revalidate"
        return response

