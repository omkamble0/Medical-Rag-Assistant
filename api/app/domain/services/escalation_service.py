"""
Human-in-the-Loop Clinical Review & Escalation Service for AegisMed.
Maintains a physician review queue for critical alerts, drug contraindications,
and low-confidence clinical queries.
"""

import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from app.domain.models.schemas import EscalationTicket, ClinicalRiskLevel


class ClinicalEscalationService:
    """Manages clinician escalation tickets and review workflows."""

    def __init__(self):
        self._tickets: Dict[str, EscalationTicket] = {}

    def create_ticket(
        self,
        query: str,
        reason: str,
        risk_level: ClinicalRiskLevel,
        audience: str
    ) -> EscalationTicket:
        t_id = f"ESC-{uuid.uuid4().hex[:8].upper()}"
        ticket = EscalationTicket(
            ticket_id=t_id,
            created_at=datetime.now(timezone.utc).isoformat(),
            query=query,
            reason=reason,
            risk_level=risk_level,
            audience=audience,
            status="pending_review"
        )
        self._tickets[t_id] = ticket
        return ticket

    def get_ticket(self, ticket_id: str) -> Optional[EscalationTicket]:
        return self._tickets.get(ticket_id)

    def list_pending_tickets(self) -> List[EscalationTicket]:
        return [t for t in self._tickets.values() if t.status == "pending_review"]

    def resolve_ticket(
        self,
        ticket_id: str,
        status: str,
        reviewer_notes: Optional[str] = None
    ) -> Optional[EscalationTicket]:
        ticket = self._tickets.get(ticket_id)
        if not ticket:
            return None
        ticket.status = status
        ticket.reviewer_notes = reviewer_notes
        return ticket

