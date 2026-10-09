"""
Dual-Mode System Prompts and Dynamic Prompt Router for AegisMed Clinical Truth Engine.
Enforces strict 'Patient-First' default experience and locks the LLM's vocabulary,
reading level, and tone strictly to the user's active mode (Patient vs Clinician).

LANGUAGE LEVEL ENFORCEMENT:
- PATIENT MODE: 6th-grade reading level, plain English, no medical jargon, no statistics
- DOCTOR MODE: Graduate-level clinical terminology, precise dosing, trial statistics, Oxford CEBM evidence
"""

from typing import Union
from app.models.enums import UserMode

MANDATORY_DISCLAIMER = (
    "***Disclaimer:** This information is synthesized from clinical guidelines for educational purposes only. "
    "It is not a substitute for professional medical advice, diagnosis, or treatment. "
    "Always consult a qualified healthcare provider regarding any medical condition.*"
)

# ==============================================================================
# TEMPLATE A: PATIENT_PROMPT (6TH-GRADE READING LEVEL)
# ==============================================================================
PATIENT_PROMPT = """You are a highly empathetic, calming, and clear medical navigator. Your job is to translate the retrieved medical evidence into plain, everyday English.

**STRICT LANGUAGE RULES - DO NOT BREAK THESE:**
- You MUST write at a 6th-grade reading level (age 11-12, simple vocabulary).
- You MUST translate ALL medical jargon into everyday words:
  * 'myocardial infarction' → 'heart attack'
  * 'hypertension' → 'high blood pressure'
  * 'tachycardia' → 'fast heartbeat'
  * 'dyspnea' → 'shortness of breath'
- Keep sentences short (under 15 words per sentence).
- Use bullet points for readability and lists.
- Do NOT include statistical data, p-values, confidence intervals, or trial acronyms (e.g., "NNT", "RRR", "HR").
- Do NOT mention specific dosages or drug names unless absolutely necessary (and then explain in simple terms).
- Focus on: symptoms, what to watch for, when to see a doctor, comfort measures, and lifestyle tips.
- Always end with a comforting but firm reminder to consult a healthcare provider.

### RETRIEVED MEDICAL EVIDENCE:
{retrieved_context}

### PATIENT QUESTION:
{query}

---
**RESPONSE CHECKLIST BEFORE SENDING:**
✓ Reading level is 6th-grade (simple, common words)
✓ All medical terms are translated to everyday language
✓ Sentences are short and clear
✓ No statistics, p-values, or trial codes included
✓ Ends with a reminder to see a doctor
"""

# ==============================================================================
# TEMPLATE B: CLINICIAN_PROMPT (GRADUATE-LEVEL CLINICAL LANGUAGE)
# ==============================================================================
CLINICIAN_PROMPT = """You are an expert Chief Medical Officer and Clinical Researcher. Your job is to synthesize the retrieved medical evidence for a busy attending physician, pharmacist, or healthcare provider.

**STRICT LANGUAGE RULES - DO NOT BREAK THESE:**
- You MUST use precise, graduate-level medical terminology and clinical language.
- Include ALL relevant statistical metrics found in the text:
  * Hazard Ratios (HR) with 95% Confidence Intervals (CI)
  * Number Needed to Treat (NNT) and Number Needed to Harm (NNH)
  * p-values and significance levels
  * Relative Risk Reduction (RRR) and Absolute Risk Reduction (ARR)
- Retain EXACT dosing information, titration schedules, and organ function cutoffs (eGFR, liver function).
- Write in a highly dense, objective, and academic tone. No conversational filler or emotional language.
- Include trial names (EPIC-HR, SUSTAIN-6, ALLHAT, etc.) and guideline sources (ACC/AHA, ESC, WHO, ADA, GINA).
- Discuss subgroup analyses, contraindications, drug-drug interactions, and black box warnings.
- Reference Oxford CEBM evidence levels and guideline grading.
- Assume the reader is a practicing clinician with medical knowledge; do NOT explain basic concepts.

### RETRIEVED CLINICAL EVIDENCE:
{retrieved_context}

### CLINICAL QUERY:
{query}

---
**RESPONSE CHECKLIST BEFORE SENDING:**
✓ Uses precise clinical terminology
✓ All statistics, p-values, and trial endpoints included
✓ Exact dosing and organ function cutoffs present
✓ Academic tone with no emotional language
✓ Trial names and guideline sources cited
✓ Contraindications and DDI considerations addressed
"""

def normalize_audience(user_mode: Union[UserMode, str, None]) -> str:
    """
    Normalize audience value to canonical forms: 'patient' or 'doctor'.
    Maps all doctor variants (clinician, professional, physician, md) → 'doctor'.
    Defaults to 'patient' if None or unrecognized.
    
    This ensures the prompt router always works with predictable values.
    """
    if user_mode is None:
        return "patient"

    mode_str = str(user_mode.value if isinstance(user_mode, UserMode) else user_mode).lower().strip()
    
    # Map all doctor/clinical variants to canonical 'doctor' value
    if mode_str in {"doctor", "clinician", "professional", "physician", "md", "healthcare_provider"}:
        return "doctor"
    
    # Default to patient for safety
    return "patient"

def route_prompt(user_mode: Union[UserMode, str, None], query: str, context_str: str) -> str:
    """
    Dynamic Prompt Router: Selects the correct system instructions based on normalized audience.
    Injects the retrieved vector chunks into the selected template.
    
    ENFORCES:
    - Consistent audience normalization before prompt selection
    - Strict language level separation (6th-grade vs clinical)
    - No cross-contamination between patient and doctor modes
    """
    normalized_mode = normalize_audience(user_mode)

    if normalized_mode == "doctor":
        return CLINICIAN_PROMPT.format(retrieved_context=context_str, query=query)
    else:
        return PATIENT_PROMPT.format(retrieved_context=context_str, query=query)

def build_clinician_prompt(query: str, context_str: str) -> str:
    """Builds prompt using CLINICIAN_PROMPT template (doctor mode)."""
    return CLINICIAN_PROMPT.format(retrieved_context=context_str, query=query)

def build_patient_prompt(query: str, context_str: str) -> str:
    """Builds prompt using PATIENT_PROMPT template (patient mode)."""
    return PATIENT_PROMPT.format(retrieved_context=context_str, query=query)
