# api/app/services/query_validator.py
import sys
from pathlib import Path

# Add root directory to sys.path to easily import medical_query_validator
root_dir = Path(__file__).resolve().parent.parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from medical_query_validator.query_validator import validator, MedicalQueryValidator, MEDICAL_TERMS_DB, MEDICAL_ACRONYMS

__all__ = ["validator", "MedicalQueryValidator", "MEDICAL_TERMS_DB", "MEDICAL_ACRONYMS"]
