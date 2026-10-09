# api/app/services/query_validator.py
from typing import Dict, List, Any, Optional
from app.services.query_guard import QueryGuard, MEDICAL_TERMS

class MedicalQueryValidator:
    """
    Self-contained Medical Query Validator service.
    Detects typos, normalizes medical terms, and returns detailed validation results.
    """
    def __init__(self):
        self.guard = QueryGuard()
        self.terms_db = MEDICAL_TERMS

    def validate_and_correct(self, query: str) -> Dict[str, Any]:
        val = self.guard.validate(query)
        corrections_made = [
            f"{c['original_word']} -> {c['corrected_word']}" for c in val.get("corrections", [])
        ]
        
        # Extract matched medical terms
        words = self.guard.normalize(query).split()
        medical_terms_found = [w for w in words if w in self.terms_db]
        
        return {
            "original": val["original"],
            "corrected": val["corrected"],
            "is_valid": len(corrections_made) == 0,
            "corrections_made": corrections_made,
            "confidence_score": val.get("confidence", 1.0),
            "medical_terms_found": medical_terms_found,
            "medical_terms_details": [
                {"term": t, "category": "medical_concept"} for t in medical_terms_found
            ],
            "issues": ["Medical misspelling detected"] if val["needs_correction"] else []
        }

validator = MedicalQueryValidator()

__all__ = ["validator", "MedicalQueryValidator", "MEDICAL_TERMS"]
