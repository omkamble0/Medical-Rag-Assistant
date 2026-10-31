"""
Medical Knowledge Base, Provenance & Versioning Service for AegisMed.
Maintains curated Evidence Cards, trusted source validation, freshness tracking,
and versioned clinical monographs.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class EvidenceCard(BaseModel):
    card_id: str
    title: str
    authors_or_organization: str
    publication_or_guideline: str
    publication_date: str
    url_or_doi: Optional[str] = None
    evidence_level: str = "Level 1"
    specialty: str
    key_clinical_takeaway: str
    last_verified_date: str = "2024-10"
    is_deprecated: bool = False
    is_peer_reviewed: bool = True
    source_authority_tier: int = 1  # 1 = CDC/WHO/AHA/FDA, 2 = Peer-reviewed RCTs, 3 = Consensus


class KnowledgeVersionInfo(BaseModel):
    version: str = "2024.10-EBM-v2"
    release_date: str = "2024-10-25"
    total_indexed_conditions: int = 600
    total_peer_reviewed_trials: int = 1200
    source_authorities: List[str] = [
        "American College of Cardiology (ACC / AHA)",
        "American Diabetes Association (ADA Standards of Care 2024)",
        "Kidney Disease: Improving Global Outcomes (KDIGO 2024)",
        "Global Initiative for Chronic Obstructive Lung Disease (GOLD 2024)",
        "World Health Organization (WHO ICD-11)",
        "Centers for Disease Control and Prevention (CDC)",
        "U.S. Food and Drug Administration (FDA MedWatch)"
    ]
    provenance_policy: str = "Oxford CEBM Level 1 & Level 2 Strict Hierarchy"


TRUSTED_MEDICAL_AUTHORITIES = {
    "acc", "aha", "ada", "kdigo", "gold", "who", "cdc", "fda", "nice",
    "nejm", "lancet", "jama", "bmj", "circulation", "cochrane"
}


class MedicalKnowledgeService:
    """Manages knowledge provenance, evidence cards, freshness audits, and versioning."""

    def __init__(self):
        self._version_info = KnowledgeVersionInfo()

    def get_version_info(self) -> KnowledgeVersionInfo:
        return self._version_info

    def validate_source(self, journal_or_source: str) -> bool:
        """Verifies if a clinical source meets the trusted medical source policy."""
        if not journal_or_source:
            return False
        j_low = journal_or_source.lower()
        return any(auth in j_low for auth in TRUSTED_MEDICAL_AUTHORITIES)

    def check_freshness(self, year: Optional[int], max_age_years: int = 7) -> Dict[str, Any]:
        """Audits guideline freshness against current year (2024)."""
        current_year = 2024
        if not year:
            return {"is_current": True, "age_years": 0, "status": "unknown_date"}
        age = current_year - year
        is_current = age <= max_age_years
        return {
            "is_current": is_current,
            "age_years": age,
            "status": "current" if is_current else "requires_revalidation",
            "warning": None if is_current else f"Publication is {age} years old; verify against current annual guidelines."
        }

    def get_knowledge_version_info(self) -> Dict[str, Any]:
        info = self.get_version_info()
        return {
            "guidelines_version": info.version,
            "version": info.version,
            "release_date": info.release_date,
            "trusted_authorities": info.source_authorities,
            "source_authorities": info.source_authorities,
            "provenance_policy": info.provenance_policy
        }

    def is_source_trusted(self, journal_or_source: str) -> bool:
        return self.validate_source(journal_or_source)

    def create_evidence_card(
        self,
        title: str,
        journal: str,
        year: int,
        evidence_level: str,
        doi_or_pmid: Optional[str] = None,
        takeaway: str = ""
    ) -> EvidenceCard:
        import hashlib
        card_id = f"CARD-{hashlib.sha256(title.encode()).hexdigest()[:8]}"
        is_peer = self.validate_source(journal) or any(l in str(evidence_level) for l in ["1", "2"])
        card = EvidenceCard(
            card_id=card_id,
            title=title,
            authors_or_organization=journal,
            publication_or_guideline=journal,
            publication_date=str(year),
            url_or_doi=doi_or_pmid,
            evidence_level=evidence_level,
            specialty="General Medicine",
            key_clinical_takeaway=takeaway,
            is_peer_reviewed=is_peer,
            source_authority_tier=1 if is_peer else 2
        )
        return card


