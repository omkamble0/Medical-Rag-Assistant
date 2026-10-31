"""
Safety Guardrail Interface Specification for AegisMed.
Defines contracts for Tier-1 emergency interceptors, high-risk medication screeners,
contraindication checks, and age/dose validation engines.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel, Field


class SafetyRiskLevel(str, Enum):
    NONE = "none"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL_EMERGENCY = "critical_emergency"


class SafetyCheckResult(BaseModel):
    is_safe: bool = True
    risk_level: SafetyRiskLevel = SafetyRiskLevel.NONE
    is_emergency: bool = False
    headline: Optional[str] = None
    action_required: Optional[str] = None
    matched_flags: List[str] = Field(default_factory=list)
    contraindications_detected: List[Dict[str, str]] = Field(default_factory=list)
    escalation_required: bool = False
    disclaimer: Optional[str] = None


class SafetyGuardrailInterface(ABC):
    """Abstract interface for clinical safety guardrails."""

    @abstractmethod
    def evaluate(
        self,
        query: str,
        patient_context: Optional[Dict[str, Any]] = None
    ) -> SafetyCheckResult:
        """
        Evaluates input query and context against:
        - Emergency red flags (STEMI, stroke, anaphylaxis, severe dyspnea)
        - Teratogenic drugs and pregnancy warnings
        - High-risk narrow therapeutic index medications
        - Age and renal contraindication thresholds
        """
        pass

