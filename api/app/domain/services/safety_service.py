"""
Clinical Safety & Guardrail Domain Service for AegisMed.
Implements SafetyGuardrailInterface with multi-layered safety screening:
- Acute Emergency Red Flags
- Pregnancy & Teratogen Black Box Warnings
- High-Risk / Narrow Therapeutic Index Medications
- Age-Specific Contraindications (Pediatric Reye's Syndrome, Geriatric Beers Criteria)
- Renal Impairment eGFR Cutoffs
- Conversational Negation & History Awareness
"""

import re
from typing import Dict, Any, List, Optional
from app.interfaces.guardrail import SafetyGuardrailInterface, SafetyCheckResult, SafetyRiskLevel
from app.core.guardrails import (
    EXPLICIT_EMERGENCY_TRIGGERS,
    EUPHEMISTIC_EMERGENCY_PATTERNS,
    CONVERSATIONAL_NEGATION_PATTERNS,
    PREGNANCY_TERATOGEN_PATTERNS,
    is_negated_or_historical
)
from app.core.disclaimers import EMERGENCY_DISCLAIMER


# High-Risk / Narrow Therapeutic Index (NTI) Medications
HIGH_RISK_MEDICATIONS = [
    (r"\b(warfarin|coumadin)\b", "Warfarin", "Anticoagulant requiring INR monitoring (target 2.0-3.0). High bleeding hazard."),
    (r"\b(lithium|eskalith|lithobid)\b", "Lithium", "Narrow therapeutic index mood stabilizer (target 0.6-1.2 mEq/L). Toxicity causes tremor, ataxia, renal failure."),
    (r"\b(digoxin|lanoxin)\b", "Digoxin", "Cardiac glycoside (target 0.5-0.9 ng/mL). Toxicity risk elevated by hypokalemia; causes arrhythmias and visual xanthopsia."),
    (r"\b(theophylline|theo-24)\b", "Theophylline", "Methylxanthine bronchodilator. Toxicity triggers seizures, arrhythmias, and nausea."),
    (r"\b(methotrexate|trexall)\b", "Methotrexate", "Antimetabolite requiring routine CBC, LFT, and renal monitoring. Boxed warnings for bone marrow suppression and hepatotoxicity."),
    (r"\b(fentanyl|oxycodone|morphine|hydromorphone|dilaudid|methadone)\b", "Opioid Analgesic", "High risk of fatal respiratory depression and physical dependence. Strictly contraindicates concurrent benzodiazepine use.")
]

# Pediatric & Geriatric Age-Specific Clinical Rules
AGE_RULES = [
    {
        "pattern": r"\b(aspirin|acetylsalicylic)\b",
        "min_age": 19,
        "warning": "Aspirin is strictly contraindicated in children and adolescents under 19 with viral illnesses due to fatal Reye's Syndrome (hepatic failure and encephalopathy)."
    },
    {
        "pattern": r"\b(ciprofloxacin|levofloxacin|fluoroquinolone)\b",
        "min_age": 18,
        "warning": "Fluoroquinolones carry FDA boxed warnings for tendon rupture, cartilage toxicity, and QT prolongation; avoid in pediatric patients unless no alternatives exist."
    },
    {
        "pattern": r"\b(diazepam|lorazepam|alprazolam|clonazepam|zolpidem|ambien)\b",
        "max_age": 65,
        "warning": "Beers Criteria Warning: Benzodiazepines and sedative-hypnotics produce cognitive impairment, ataxia, delirium, and severe fall/fracture hazards in adults aged 65 and older."
    }
]

# Renal Cutoffs (eGFR in mL/min/1.73m2)
RENAL_RULES = [
    {
        "pattern": r"\b(metformin|glucophage)\b",
        "min_egfr": 30.0,
        "warning": "Metformin is contraindicated when eGFR is below 30 mL/min/1.73m2 due to high risk of life-threatening lactic acidosis."
    },
    {
        "pattern": r"\b(empagliflozin|dapagliflozin|canagliflozin|sglt2)\b",
        "min_egfr": 20.0,
        "warning": "SGLT2 inhibitors are not recommended for initiation when eGFR is below 20 mL/min/1.73m2 due to reduced glycemic efficacy."
    },
    {
        "pattern": r"\b(ibuprofen|naproxen|ketorolac|meloxicam|nsaid)\b",
        "min_egfr": 30.0,
        "warning": "NSAIDs cause renal vasoconstriction and acute kidney injury; strictly contraindicated in stage 4/5 chronic kidney disease (eGFR < 30)."
    }
]


class ClinicalSafetyService(SafetyGuardrailInterface):
    """Production-grade safety evaluation service."""

    def evaluate(
        self,
        query: str,
        patient_context: Optional[Dict[str, Any]] = None
    ) -> SafetyCheckResult:
        ctx = patient_context or {}
        q_low = query.lower()

        # 1. Historical / Ruled-Out bypass check
        if is_negated_or_historical(q_low):
            return SafetyCheckResult(
                is_safe=True,
                risk_level=SafetyRiskLevel.LOW,
                is_emergency=False,
                headline="Historical / Ruled-Out Clinical Discussion",
                matched_flags=["negated_or_historical"]
            )

        # 2. Check Acute Emergency Red Flags
        matched_triggers: List[str] = []
        for pat in EXPLICIT_EMERGENCY_TRIGGERS:
            m = re.search(pat, q_low)
            if m:
                matched_triggers.append(m.group(0))

        for pat, cat in EUPHEMISTIC_EMERGENCY_PATTERNS:
            m = re.search(pat, q_low)
            if m:
                matched_triggers.append(f"{cat}: {m.group(0)}")

        if matched_triggers:
            return SafetyCheckResult(
                is_safe=False,
                risk_level=SafetyRiskLevel.CRITICAL_EMERGENCY,
                is_emergency=True,
                headline="CRITICAL EMERGENCY RED FLAG INTERCEPT",
                action_required="IMMEDIATE IN-PERSON EMERGENCY EVALUATION REQUIRED (Call 911 / EMS)",
                matched_flags=matched_triggers,
                escalation_required=True,
                disclaimer=EMERGENCY_DISCLAIMER
            )

        contraindications: List[Dict[str, str]] = []

        # 3. Pregnancy Teratogen Check
        is_pregnant = ctx.get("is_pregnant", False) or bool(
            re.search(r"\b(pregnant|pregnancy|expecting|trimester|trying to conceive)\b", q_low)
        )
        if is_pregnant:
            for drug_pat, drug_name, contra_desc in PREGNANCY_TERATOGEN_PATTERNS:
                if re.search(drug_pat, q_low):
                    contraindications.append({
                        "category": "Pregnancy Teratogenicity",
                        "drug": drug_name,
                        "description": contra_desc
                    })

        # 4. Age-Specific Rules
        age = ctx.get("patient_age")
        if age is not None:
            for rule in AGE_RULES:
                if re.search(rule["pattern"], q_low):
                    if "min_age" in rule and age < rule["min_age"]:
                        contraindications.append({
                            "category": "Pediatric Safety Warning",
                            "drug": rule["pattern"],
                            "description": rule["warning"]
                        })
                    if "max_age" in rule and age >= rule["max_age"]:
                        contraindications.append({
                            "category": "Geriatric Beers Criteria",
                            "drug": rule["pattern"],
                            "description": rule["warning"]
                        })

        # 5. Renal Impairment eGFR Check
        egfr = ctx.get("egfr")
        if egfr is not None:
            for r_rule in RENAL_RULES:
                if re.search(r_rule["pattern"], q_low) and egfr < r_rule["min_egfr"]:
                    contraindications.append({
                        "category": "Renal Contraindication",
                        "drug": r_rule["pattern"],
                        "description": r_rule["warning"]
                    })

        # 6. High-Risk / NTI Drug Screen
        matched_high_risk: List[str] = []
        for drug_pat, name, clinical_note in HIGH_RISK_MEDICATIONS:
            if re.search(drug_pat, q_low):
                matched_high_risk.append(f"{name}: {clinical_note}")

        if contraindications:
            return SafetyCheckResult(
                is_safe=False,
                risk_level=SafetyRiskLevel.HIGH,
                is_emergency=False,
                headline="CLINICAL CONTRAINDICATION ALERT",
                action_required="Withhold medication; require physician review of contraindication",
                contraindications_detected=contraindications,
                matched_flags=[c["category"] for c in contraindications],
                escalation_required=True
            )

        if matched_high_risk:
            return SafetyCheckResult(
                is_safe=True,
                risk_level=SafetyRiskLevel.MODERATE,
                is_emergency=False,
                headline="High-Risk Medication Surveillance",
                action_required="Ensure strict laboratory monitoring and therapeutic range validation",
                matched_flags=matched_high_risk
            )

        return SafetyCheckResult(
            is_safe=True,
            risk_level=SafetyRiskLevel.LOW,
            is_emergency=False
        )

    def check_emergency_red_flags(self, query: str):
        res = self.evaluate(query)
        from app.domain.models.schemas import ClinicalRiskLevel
        class EmergencyCheckResult:
            def __init__(self, is_emergency, risk_level, escalation_reason):
                self.is_emergency = is_emergency
                self.risk_level = risk_level
                self.escalation_reason = escalation_reason
        return EmergencyCheckResult(
            is_emergency=res.is_emergency,
            risk_level=ClinicalRiskLevel.CRITICAL if res.is_emergency else ClinicalRiskLevel.LOW,
            escalation_reason=res.action_required or "Emergency"
        )

    def check_pregnancy_contraindications(self, query: str, is_pregnant: bool = True):
        res = self.evaluate(query, patient_context={"is_pregnant": is_pregnant})
        from app.domain.models.schemas import ClinicalRiskLevel
        warnings = [c.get("description", "") for c in res.contraindications_detected]
        class PregnancyCheckResult:
            def __init__(self, is_safe, warnings, risk_level):
                self.is_safe = is_safe
                self.warnings = warnings
                self.risk_level = risk_level
        return PregnancyCheckResult(
            is_safe=res.is_safe,
            warnings=warnings or ["Safe"],
            risk_level=ClinicalRiskLevel.HIGH if not res.is_safe else ClinicalRiskLevel.LOW
        )

    def check_pediatric_safety(self, query: str, patient_age_years: int):
        res = self.evaluate(query, patient_context={"patient_age": patient_age_years})
        warnings = [c.get("description", "") for c in res.contraindications_detected]
        class PediatricCheckResult:
            def __init__(self, is_safe, warnings):
                self.is_safe = is_safe
                self.warnings = warnings
        return PediatricCheckResult(is_safe=res.is_safe, warnings=warnings or ["Safe"])

    def check_geriatric_safety(self, query: str, patient_age_years: int):
        q_low = query.lower()
        contra = []
        if patient_age_years >= 65 and any(d in q_low for d in ["diphenhydramine", "benadryl", "diazepam", "lorazepam", "zolpidem", "ambien"]):
            contra.append("Beers criteria: Diphenhydramine and anticholinergics increase cognitive impairment, urinary retention, and fall hazards in older adults.")
        class GeriatricCheckResult:
            def __init__(self, is_safe, warnings):
                self.is_safe = is_safe
                self.warnings = warnings
        return GeriatricCheckResult(is_safe=len(contra) == 0, warnings=contra or ["Safe"])

    def check_renal_safety(self, query: str, egfr_ml_min: float):
        res = self.evaluate(query, patient_context={"egfr": egfr_ml_min})
        warnings = [c.get("description", "") for c in res.contraindications_detected]
        class RenalCheckResult:
            def __init__(self, is_safe, warnings):
                self.is_safe = is_safe
                self.warnings = warnings
        return RenalCheckResult(is_safe=res.is_safe, warnings=warnings or ["Safe"])

    def check_high_risk_medications(self, query: str):
        q_low = query.lower()
        matched = []
        for drug_pat, name, note in HIGH_RISK_MEDICATIONS:
            if re.search(drug_pat, q_low):
                matched.append(name.lower())
        class NTIResult:
            def __init__(self, identified_nti_drugs):
                self.identified_nti_drugs = identified_nti_drugs
        return NTIResult(identified_nti_drugs=matched)


