from enum import Enum

class UserMode(str, Enum):
    PROFESSIONAL = "professional"
    PATIENT = "patient"

class EvidenceLevel(str, Enum):
    LEVEL_1 = "Level 1 (Meta-Analysis / Systematic Review)"
    LEVEL_2 = "Level 2 (Randomized Controlled Trial)"
    LEVEL_3 = "Level 3 (Cohort / Case-Control Study)"
    LEVEL_4 = "Level 4 (Case Series / Observational)"
    LEVEL_5 = "Level 5 (Expert Opinion / Clinical Guideline)"

class ConfidenceStatus(str, Enum):
    HIGH = "high"       # Green (>= 85%)
    MODERATE = "moderate" # Yellow (65% - 84%)
    LOW = "low"         # Red (< 65%)

class TriageUrgency(str, Enum):
    IMMEDIATE_EMERGENCY = "immediate_emergency"
    URGENT_EVALUATION = "urgent_evaluation"
    ROUTINE = "routine"
