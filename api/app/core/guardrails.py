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
    r"\b(severe bleeding|uncontrolled bleeding|massive hemorrhage|arterial bleed|coughing up blood|vomiting blood|gunshot|stab wound)\b",
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
        if re.search(euphemism_pat, query_lower):
            match = re.search(euphemism_pat, query_lower)
            matched_triggers.append(match.group(0))
            category = cat

    if not matched_triggers:
        return None

    triggers_str = " ".join(matched_triggers).lower()

    # Determine guidance details based on identified crisis type
    if category == "cardiac" or any(k in triggers_str for k in ["heart", "chest", "cardiac", "stemi", "elephant"]):
        headline = "CRITICAL CARDIAC WARNING: IMMEDIATE EMERGENCY MEDICAL EVALUATION REQUIRED"
        guidance = "Chest discomfort, pressure radiating to jaw/arm, or crushing sensation could indicate Acute Coronary Syndrome. Do not attempt self-treatment or wait for symptoms to pass."
        red_flags = [
            "Crushing central chest pressure or squeezing sensation",
            "Shortness of breath with cold sweats, nausea, or dizziness",
            "Pain or numbness radiating to left shoulder, arm, neck, or jaw",
            "Sudden unexplained lightheadedness or near-syncope"
        ]
    elif category == "neurological" or any(k in triggers_str for k in ["stroke", "slurred", "facial droop", "weakness", "thunderclap", "half my face"]):
        headline = "CRITICAL NEUROLOGICAL WARNING: POSSIBLE ACUTE STROKE DETECTED"
        guidance = "Remember the F.A.S.T. protocol (Face drooping, Arm weakness, Speech difficulty, Time to call 911). Thrombolysis window is strictly time-critical (<3-4.5 hours)."
        red_flags = [
            "Sudden numbness or weakness of face, arm, or leg, especially on one side",
            "Sudden confusion or difficulty speaking and understanding speech",
            "Sudden visual disturbance in one or both eyes",
            "Sudden severe 'thunderclap' headache with no known cause"
        ]
    elif category == "respiratory" or any(k in triggers_str for k in ["breathe", "suffocating", "airway", "anaphylaxis", "air hunger", "gasping"]):
        headline = "CRITICAL AIRWAY / RESPIRATORY EMERGENCY"
        guidance = "Acute respiratory distress or anaphylaxis is immediately life-threatening. If an Epinephrine auto-injector (EpiPen) is prescribed, administer immediately and call emergency services."
        red_flags = [
            "Inability to speak in full sentences without gasping for breath",
            "Stridor (high-pitched inspiratory wheezing) or swelling of lips, tongue, or uvula",
            "Cyanosis (blue/gray discoloration around lips or nailbeds)",
            "Rapidly worsening chest tightness with oxygen desaturation"
        ]
    elif category == "crisis" or any(k in triggers_str for k in ["suicide", "suicidal", "kill myself", "end my life", "check out permanently", "end it all"]):
        headline = "CRISIS SUPPORT: IMMEDIATE CONFIDENTIAL HELP AVAILABLE 24/7"
        guidance = "You are not alone. Please reach out immediately to trained, compassionate crisis counselors who can support you through this."
        red_flags = [
            "Suicide & Crisis Lifeline: Dial or Text 988 (US & Canada, toll-free 24/7)",
            "The Crisis Text Line: Text HOME to 741741",
            "International Resources & Emergency Hotlines: findahelpline.com",
            "Immediate local emergency services: Dial 911 / 112 / 108"
        ]
    else:
        headline = "POTENTIALLY LIFE-THREATENING SYMPTOM PATTERN DETECTED"
        guidance = "The symptoms you entered represent critical clinical red flags requiring direct emergency assessment rather than automated information synthesis."
        red_flags = [
            "Uncontrolled hemorrhage unresponsive to direct pressure",
            "Loss of consciousness, syncope, or altered mental status",
            "Sudden excruciating pain of acute onset"
        ]

    return EmergencyTriageAlert(
        is_emergency=True,
        urgency=TriageUrgency.IMMEDIATE_EMERGENCY,
        matched_keywords=list(set(matched_triggers)),
        headline=headline,
        critical_guidance=guidance,
        red_flag_symptoms=red_flags,
        emergency_contacts=[
            "📞 911 (United States & Canada)",
            "📞 112 (European Union & UK)",
            "📞 108 / 112 (India)",
            "📞 988 (Suicide & Mental Health Crisis Lifeline)"
        ]
    )
