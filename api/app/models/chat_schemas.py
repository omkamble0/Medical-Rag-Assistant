"""
Conversational Chat Schemas for AegisMed Clinical Truth Engine.
Supports stateful multi-turn clinical dialogue, audience register switching,
and evidence-grounded follow-ups.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from app.models.schemas import SourceDocument, ConfidenceMetrics, EmergencyTriageAlert


class ChatMessage(BaseModel):
    role: str = Field(..., description="'user', 'assistant', or 'system'")
    content: str = Field(..., description="Message text content")
    timestamp: Optional[str] = Field(default=None, description="ISO timestamp")
    audience: Optional[str] = Field(default="patient", description="'patient' or 'doctor'")
    citations: Optional[List[int]] = Field(default=None, description="Referenced citation indices")
    triage_alert: Optional[EmergencyTriageAlert] = Field(default=None, description="Acuity alert if triggered")


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2500, description="User's query or conversational follow-up")
    conversation_id: Optional[str] = Field(default=None, description="Unique conversation session UUID")
    audience: str = Field(default="patient", description="Target audience: 'patient' or 'doctor'")
    history: Optional[List[ChatMessage]] = Field(default_factory=list, description="Prior conversation message turns")
    active_condition: Optional[str] = Field(default=None, description="Explicit active medical condition or topic in context")


class ChatResponse(BaseModel):
    conversation_id: str = Field(..., description="Active conversation session UUID")
    audience: str = Field(..., description="Audience register of this turn: 'patient' or 'doctor'")
    message: str = Field(..., description="Synthesized multi-turn response")
    history: List[ChatMessage] = Field(default_factory=list, description="Updated session message turns")
    active_condition: Optional[str] = Field(default=None, description="Primary clinical condition resolved in context")
    triage_alert: Optional[EmergencyTriageAlert] = Field(default=None, description="Clinical acuity advisory if flagged")
    citations: List[int] = Field(default_factory=list, description="Referenced evidence citation indices")
    sources: List[SourceDocument] = Field(default_factory=list, description="Retrieved evidence sources")
    suggested_followups: List[str] = Field(default_factory=list, description="Context-aware suggested follow-up questions")
    confidence: Optional[ConfidenceMetrics] = Field(default=None, description="Grounding and confidence metrics")
    latency_ms: int = Field(..., description="Turn generation latency in milliseconds")
