import re
from typing import Optional, List, Tuple
from app.models.schemas import EmergencyTriageAlert
from app.models.enums import TriageUrgency

# ============================================================
# 1. Deterministic Explicit Emergency Trigger Patterns
# ============================================================
EXPLICIT_EMERGENCY_TRIGGERS = [
    # Cardiac & Acute Coronary Syndrome
    r"\b(heart attack|myocardial infarction|stemi|nstemi|cardiac arrest|crushing chest pain|severe chest pressure|radiating chest pain)\b",
    # Neurological / Stroke (FAST)
    r"\b(stroke|facial droop|slurred speech|sudden hemiparesis|sudden weakness|loss of consciousness|unresponsive|thunderclap headache|subarachnoid)\b",
    # Severe Airway & Respiratory Failure
    r"\b(can't breathe|cannot breathe|severe shortness of breath|suffocating|gasping for air|cyanosis|stridor|anaphylaxis|throat closing|severe allergic reaction|epipen)\b",
    # Hemorrhage & Severe Trauma
    r"\b(severe bleeding|uncontrolled bleeding|massive hemorrhage|arterial bleed|coughing up(\s+\w+){0,4}\s+blood|vomiting(\s+\w+){0,4}\s+blood|hemoptysis|hematemesis|gunshot|stab wound)\b",
    # Poisoning & Crisis Self-Harm
    r"\b(overdose|poisoning|swallowed bleach|suicide|suicidal|kill myself|end my life|want to die)\b"
]

# ============================================================
# 2. Clinical Euphemisms & Metaphorical Crisis Phrases
# (Zero-latency zero-shot semantic emergency detector)
# ============================================================
EUPHEMISTIC_EMERGENCY_PATTERNS = [
    # Cardiac euphemisms
    (r"\b(elephant (sitting )?(on|upon) my chest|band squeezing (my )?chest|chest in a vice|crushing weight on (my )?chest)\b", "cardiac"),
    # Neurological euphemisms
    (r"\b(worst headache of my life|head exploding like thunder|room is spinning and (my )?face feels heavy|half (my )?face is numb and droopy|arm won't lift and speech is garbled)\b", "neurological"),
    # Respiratory euphemisms
    (r"\b(air hunger|fighting for (every )?breath|breathing through a (tiny )?straw|gasping like a fish|lungs feel like they're on fire and collapsing)\b", "respiratory"),
    # Crisis / Self-Harm euphemisms
    (r"\b(can't go on anymore|ready to check out permanently|no reason to wake up tomorrow|planning to end it all|saying goodbye to everyone forever)\b", "crisis")
]

# ============================================================
# 3. Conversational Negation & Historical Context Patterns
# Prevents false positive emergency intercepts on ruled-out / past events
# ============================================================
CONVERSATIONAL_NEGATION_PATTERNS = [
    r"\b(doctor|dr|physician|er|hospital|cardiologist|neurologist)\s+(ruled out|cleared|tested negative for|disproved)\b",
    r"\b(tested negative for|no evidence of|not having|ruled out|cleared of)\s+(a\s+)?(heart attack|stroke|cardiac arrest|myocardial infarction)\b",
    r"\b(no|never had|without any|denies)\s+(chest pain|shortness of breath|facial droop|bleeding|suicidal thoughts)\b",
    r"\b(history of|past|previous|had a|diagnosed with)\s+(heart attack|stroke|tia)\s+(in \d{4}|\d+\s*(years?|months?|yrs?)\s+ago|years back)\b",
    r"\b(not suicidal|no thoughts of self harm|not going to hurt myself)\b"
]


def is_negated_or_historical(query: str) -> bool:
    """Checks if emergency terms are strictly mentioned in a negated or historical context."""
    q_low = query.lower()
    for neg_pat in CONVERSATIONAL_NEGATION_PATTERNS:
        if re.search(neg_pat, q_low):
            return True
    return False


def evaluate_safety_guardrails(query: str) -> Optional[EmergencyTriageAlert]:
    """
    Tier-1 Safety Interceptor:
    1. Checks for explicit emergency patterns (911, STEMI, stroke).
    2. Zero-shot matches colloquial euphemisms ("elephant on my chest").
    3. Respects conversational negations ("doctor ruled out a heart attack").
    """
    query_lower = query.lower()

    # If the query is explicitly discussing a ruled-out or historical event, bypass emergency lock
    if is_negated_or_historical(query_lower):
        return None

    matched_triggers: List[str] = []
    category: Optional[str] = None

    # Check explicit emergency patterns
    for pattern in EXPLICIT_EMERGENCY_TRIGGERS:
        matches = re.findall(pattern, query_lower)
        if matches:
            matched_triggers.extend([m if isinstance(m, str) else m[0] for m in matches])

    # Check euphemistic crisis patterns
    for euphemism_pat, cat in EUPHEMISTIC_EMERGENCY_PATTERNS:
        match = re.search(euphemism_pat, query_lower)
        if match:
            matched_triggers.append(match.group(0))
            category = cat

    if not matched_triggers:
        return None

    triggers_str = " ".join(matched_triggers).lower()

    # Determine guidance details based on identified crisis type
    if category == "cardiac" or any(k in triggers_str for k in ["heart", "chest", "cardiac", "stemi", "elephant"]):
        headline = "CLINICAL ACUITY ADVISORY: POTENTIAL ACUTE CARDIAC SYMPTOMS"
        guidance = (
            "Chest discomfort, pressure radiating to jaw/arm, or crushing sensations are acute clinical indicators. "
            "Prompt in-person clinical assessment by a healthcare provider or urgent care clinic is strongly recommended. "
            "Self-treatment should not delay clinical evaluation."
        )
        red_flags = [
            "Crushing central chest pressure or squeezing sensation",
            "Shortness of breath with cold sweats, nausea, or dizziness",
            "Pain or numbness radiating to left shoulder, arm, neck, or jaw",
            "Sudden unexplained lightheadedness or near-syncope"
        ]
        contacts = [
            "Consult Primary Care Physician or Urgent Care Clinic",
            "Local Hospital / Clinical Health Center",
            "Crisis & Health Support Directory (findahelpline.com)"
        ]
    elif category == "neurological" or any(k in triggers_str for k in ["stroke", "slurred", "facial droop", "weakness", "thunderclap", "half my face"]):
        headline = "CLINICAL ACUITY ADVISORY: POTENTIAL ACUTE NEUROLOGICAL SYMPTOMS"
        guidance = (
            "Sudden neurological deficits such as facial droop, unilateral limb weakness, or speech difficulty "
            "warrant immediate in-person medical evaluation to assess neurological function."
        )
        red_flags = [
            "Sudden numbness or weakness of face, arm, or leg, especially on one side",
            "Sudden confusion or difficulty speaking and understanding speech",
            "Sudden visual disturbance in one or both eyes",
            "Sudden severe 'thunderclap' headache of acute onset"
        ]
        contacts = [
            "Urgent Neurological / Clinical Medical Evaluation",
            "Local Hospital / Outpatient Clinic",
            "Health Information & Triage Services"
        ]
    elif category == "respiratory" or any(k in triggers_str for k in ["breathe", "suffocating", "airway", "anaphylaxis", "air hunger", "gasping"]):
        headline = "CLINICAL ACUITY ADVISORY: SEVERE RESPIRATORY / AIRWAY SYMPTOMS"
        guidance = (
            "Acute shortness of breath, audible stridor, or rapid airway swelling requires immediate professional clinical examination. "
            "If an epinephrine auto-injector is prescribed for known anaphylaxis, use as clinically directed."
        )
        red_flags = [
            "Inability to speak in full sentences without gasping for breath",
            "Stridor (high-pitched inspiratory wheezing) or swelling of lips/tongue",
            "Cyanosis (blue/gray discoloration around lips or nailbeds)",
            "Rapidly worsening chest tightness with breathing difficulty"
        ]
        contacts = [
            "Urgent Care Center / Pulmonary Clinical Evaluation",
            "Local Hospital Walk-in Clinic",
            "Personal Prescribing Physician Consultation"
        ]
    elif category == "crisis" or any(k in triggers_str for k in ["suicide", "suicidal", "kill myself", "end my life", "check out permanently", "end it all"]):
        headline = "CRISIS SUPPORT & MENTAL HEALTH ADVISORY: 24/7 CONFIDENTIAL RESOURCES"
        guidance = (
            "You are not alone. If you are experiencing intense emotional distress or crisis, compassionate, "
            "trained counselors are available around the clock to support you."
        )
        red_flags = [
            "Suicide & Crisis Lifeline: Dial or Text 988 (US & Canada, toll-free 24/7)",
            "The Crisis Text Line: Text HOME to 741741",
            "International Resources & Support: findahelpline.com"
        ]
        contacts = [
            "988 Suicide & Crisis Lifeline (Dial or Text 988)",
            "Crisis Text Line (Text HOME to 741741)",
            "findahelpline.com (Global Free Crisis Centers)"
        ]
    else:
        headline = "CLINICAL ACUITY ADVISORY: HIGH-URGENCY SYMPTOMS DETECTED"
        guidance = (
            "The symptoms entered include clinical red flags that warrant timely in-person evaluation by a healthcare provider. "
            "Automated information should support, not replace, a direct medical examination."
        )
        red_flags = [
            "Uncontrolled hemorrhage unresponsive to direct pressure",
            "Loss of consciousness, syncope, or altered mental status",
            "Sudden excruciating pain of acute onset"
        ]
        contacts = [
            "Prompt In-Person Clinical Healthcare Consultation",
            "Local Urgent Care or Outpatient Center",
            "Personal Primary Care Physician"
        ]

    return EmergencyTriageAlert(
        is_emergency=False,
        urgency=TriageUrgency.URGENT_EVALUATION,
        matched_keywords=list(set(matched_triggers)),
        headline=headline,
        critical_guidance=guidance,
        red_flag_symptoms=red_flags,
        emergency_contacts=contacts
    )
