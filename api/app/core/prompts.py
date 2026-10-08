"""
Dual-Mode System Prompts and Dynamic Prompt Router for AegisMed Clinical Truth Engine.
Enforces a 'Patient-First' default experience and locks the LLM's vocabulary,
reading level, and tone strictly to the user's active mode (Patient vs Clinician).
"""

from typing import Union
from app.models.enums import UserMode

MANDATORY_DISCLAIMER = (
    "***Disclaimer:** This information is synthesized from clinical guidelines for educational purposes only. "
    "It is not a substitute for professional medical advice, diagnosis, or treatment. "
    "Always consult a qualified healthcare provider regarding any medical condition.*"
)

# ==============================================================================
# TEMPLATE A: PATIENT_PROMPT
# ==============================================================================
PATIENT_PROMPT = """You are a highly empathetic, calming, and clear medical navigator. Your job is to translate the retrieved medical evidence into plain, everyday English. 
- You MUST write at a 6th-grade reading level.
- You MUST translate all medical jargon (e.g., 'myocardial infarction' becomes 'heart attack').
- Keep sentences short and use bullet points for readability.
- Do not include statistical data, p-values, or complex trial acronyms.
- Always end with a comforting but firm reminder to consult a doctor.

### RETRIEVED MEDICAL EVIDENCE:
{retrieved_context}

### PATIENT QUESTION:
{query}
"""

# ==============================================================================
# TEMPLATE B: CLINICIAN_PROMPT
# ==============================================================================
CLINICIAN_PROMPT = """You are an expert Chief Medical Officer and Clinical Researcher. Your job is to synthesize the retrieved medical evidence for a busy attending physician.
- You MUST use precise, graduate-level medical terminology.
- Include all relevant statistical metrics found in the text (e.g., Hazard Ratios, NNT, 95% CIs, p-values).
- Retain exact dosing, titration thresholds, and eGFR cutoffs.
- Write in a highly dense, objective, and academic tone. Do not use conversational filler.

### RETRIEVED CLINICAL EVIDENCE:
{retrieved_context}

### CLINICAL QUERY:
{query}
"""


def route_prompt(user_mode: Union[UserMode, str], query: str, context_str: str) -> str:
    """
    Dynamic Prompt Router: Selects the correct system instructions and generation contract
    based on the user_mode passed from the frontend ('patient' vs 'professional'/'clinician').
    Injects the retrieved vector chunks into the selected template.
    """
    mode_str = str(user_mode.value if isinstance(user_mode, UserMode) else user_mode).lower()
    
    if mode_str in ["clinician", "professional", "doctor"]:
        return CLINICIAN_PROMPT.format(retrieved_context=context_str, query=query)
    else:
        return PATIENT_PROMPT.format(retrieved_context=context_str, query=query)


def build_clinician_prompt(query: str, context_str: str) -> str:
    """Builds prompt using CLINICIAN_PROMPT template."""
    return CLINICIAN_PROMPT.format(retrieved_context=context_str, query=query)


def build_patient_prompt(query: str, context_str: str) -> str:
    """Builds prompt using PATIENT_PROMPT template."""
    return PATIENT_PROMPT.format(retrieved_context=context_str, query=query)

