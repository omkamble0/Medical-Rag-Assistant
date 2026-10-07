"""
Inbound Clinical Query Disambiguation & Entity Parser.
Stage 1 of the AegisMed Healthcare Knowledge Navigator pipeline.

Performs structured clinical entity extraction, missing variable detection,
and anti-hallucination context gap flagging prior to evidence retrieval.
"""

import re
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class Demographics(BaseModel):
    age_group: Optional[str] = Field(None, description="pediatric, adult, geriatric, or unspecified")
    pregnancy_status: Optional[str] = Field(None, description="pregnant, postpartum, non-pregnant, or unspecified")
    comorbidities: List[str] = Field(default_factory=list, description="Explicitly mentioned comorbidities")


class ClinicalEntities(BaseModel):
    primary_condition: Optional[str] = Field(None, description="Target disease, disorder, or primary symptom")
    interventions: List[str] = Field(default_factory=list, description="Medications, procedures, or lifestyle therapies")
    patient_demographics: Demographics = Field(default_factory=Demographics, description="Extracted age, pregnancy, or cohort parameters")
    clinical_metrics: Dict[str, Any] = Field(default_factory=dict, description="Identified biomarkers, lab values, or vitals (e.g. eGFR, HbA1c, BP)")


class ParsedQueryAnalysis(BaseModel):
    raw_query: str
    entities: ClinicalEntities
    missing_variables: List[str] = Field(
        default_factory=list,
        description="Clinical variables required by guidelines but omitted in the query"
    )
    context_gaps: List[str] = Field(
        default_factory=list,
        description="Explicit anti-hallucination alerts regarding clinical dependencies"
    )
    requires_disambiguation: bool = Field(
        default=False,
        description="True if omitted variables or ambiguous acuity require clinical clarification"
    )
    recommended_clarifications: List[str] = Field(
        default_factory=list,
        description="Guided prompt options to disambiguate the clinical situation"
    )


# --- Clinical Knowledge Maps for Parsing & Gap Detection ---

CONDITION_PATTERNS = [
    (r"\b(covid[- ]?19|sars[- ]?cov[- ]?2|coronavirus|corona)\b", "COVID-19 (SARS-CoV-2 Infection)"),
    (r"\b(hypertension|high blood pressure|elevated bp|systolic hypertension)\b", "Essential Hypertension"),
    (r"\b(type 2 diabetes|diabetes mellitus|t2d|t2dm|high blood sugar|hyperglycemia)\b", "Type 2 Diabetes Mellitus"),
    (r"\b(asthma|bronchial asthma|reactive airway|wheezing)\b", "Bronchial Asthma"),
    (r"\b(copd|chronic obstructive pulmonary|emphysema|chronic bronchitis)\b", "Chronic Obstructive Pulmonary Disease (COPD)"),
    (r"\b(hyperlipidemia|hypercholesterolemia|high cholesterol|dyslipidemia|elevated ldl)\b", "Hyperlipidemia / Dyslipidemia"),
    (r"\b(heart failure|congestive heart failure|hfpef|hfref|cardiac insufficiency)\b", "Heart Failure"),
    (r"\b(anxiety|generalized anxiety|panic disorder|gad|panic attack)\b", "Generalized Anxiety Disorder"),
    (r"\b(major depression|depressive disorder|mdd|clinical depression)\b", "Major Depressive Disorder"),
    (r"\b(chronic kidney disease|ckd|renal failure|nephropathy)\b", "Chronic Kidney Disease (CKD)"),
    (r"\b(atrial fibrillation|afib|a-fib|arrhythmia)\b", "Atrial Fibrillation"),
    (r"\b(migraine|headache|tension headache)\b", "Migraine Disorder"),
]

INTERVENTION_PATTERNS = [
    (r"\b(paxlovid|nirmatrelvir|ritonavir|remdesivir|molnupiravir)\b", "Paxlovid (Nirmatrelvir / Ritonavir)"),
    (r"\b(amlodipine|norvasc|lisinopril|prinivil|losartan|cozaar|hydrochlorothiazide|hctz|metoprolol|atorvastatin|lipitor|rosuvastatin|crestor)\b", "Antihypertensive / Statin Pharmacotherapy"),
    (r"\b(semaglutide|ozempic|wegovy|rybelsus|tirzepatide|mounjaro|zepbound|metformin|glp[- ]?1|sglt2|empagliflozin|jardiance|dapagliflozin|farxiga)\b", "GLP-1 RA / SGLT2i Metabolic Therapy"),
    (r"\b(budesonide[- ]formoterol|symbicort|smart|albuterol|ventolin|fluticasone|advair|singulair|montelukast|trelegy)\b", "Inhaled Corticosteroid / Bronchodilator Therapy"),
    (r"\b(dash diet|sodium reduction|low sodium|aerobic exercise|weight loss|lifestyle modification)\b", "Non-Pharmacological Lifestyle Modification (DASH / Exercise)"),
    (r"\b(ssri|sertraline|zoloft|escitalopram|lexapro|cbt|cognitive behavioral therapy)\b", "SSRI Pharmacotherapy / Psychotherapy"),
]

DEMOGRAPHIC_PATTERNS = {
    "pediatric": [r"\b(child|children|pediatric|infant|toddler|teen|adolescent)\b"],
    "geriatric": [r"\b(elderly|geriatric|senior|older adult|age 65\+|age > 65|80-year-old|75-year-old)\b"],
    "adult": [r"\b(adult|young adult|middle-aged|30-year-old|45-year-old)\b"],
    "pregnant": [r"\b(pregnant|pregnancy|trimester|gestational|prenatal|expecting)\b"],
    "postpartum": [r"\b(postpartum|breastfeeding|lactating|nursing mother)\b"],
}

METRIC_PATTERNS = [
    (r"\begfr[:\s=]*([0-9]+(\.[0-9]+)?)\b", "eGFR", "mL/min/1.73m2"),
    (r"\bhba1c[:\s=]*([0-9]+(\.[0-9]+)?%?)\b", "HbA1c", "%"),
    (r"\blvef[:\s=]*([0-9]+(\.[0-9]+)?%?)\b", "LVEF", "%"),
    (r"\b(bp|blood pressure)[:\s=]*([0-9]{2,3}/[0-9]{2,3})\b", "blood_pressure", "mmHg"),
    (r"\b([0-9]{2,3}/[0-9]{2,3})\s*mmhg\b", "blood_pressure", "mmHg"),
    (r"\bldl[:\s=]*([0-9]+(\.[0-9]+)?)\b", "LDL-C", "mg/dL"),
    (r"\bcreatinine[:\s=]*([0-9]+(\.[0-9]+)?)\b", "Creatinine", "mg/dL"),
    (r"\bpotassium[:\s=]*([0-9]+(\.[0-9]+)?)\b", "Potassium", "mEq/L"),
    (r"\bday[s]?\s*([1-9]|10)\s*(of symptoms|post onset|since onset|of illness)\b", "symptom_duration", "days"),
    (r"\bwithin\s*([1-5])\s*days\b", "symptom_duration", "days"),
]


def extract_clinical_entities(query: str) -> ClinicalEntities:
    q_low = query.lower()
    
    # 1. Primary Condition
    primary_condition = None
    for pattern, name in CONDITION_PATTERNS:
        if re.search(pattern, q_low, re.IGNORECASE):
            primary_condition = name
            break

    # 2. Interventions
    interventions = []
    for pattern, name in INTERVENTION_PATTERNS:
        match = re.search(pattern, q_low, re.IGNORECASE)
        if match:
            interventions.append(match.group(0).title())
    
    # 3. Patient Demographics
    demographics = Demographics()
    for grp, patterns in DEMOGRAPHIC_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, q_low, re.IGNORECASE):
                if grp in ["pediatric", "geriatric", "adult"]:
                    demographics.age_group = grp
                elif grp in ["pregnant", "postpartum"]:
                    demographics.pregnancy_status = grp

    # Common Comorbidities
    comorbidity_keywords = [
        ("chronic kidney disease", "CKD"),
        ("renal impairment", "Renal Impairment"),
        ("hypertension", "Hypertension"),
        ("diabetes", "Diabetes Mellitus"),
        ("heart failure", "Heart Failure"),
        ("coronary artery disease", "CAD / ASCVD"),
        ("liver disease", "Hepatic Impairment"),
        ("asthma", "Asthma"),
    ]
    for kw, label in comorbidity_keywords:
        if kw in q_low and (primary_condition is None or kw not in primary_condition.lower()):
            if label not in demographics.comorbidities:
                demographics.comorbidities.append(label)

    # 4. Clinical Metrics
    clinical_metrics = {}
    for pattern, metric_name, unit in METRIC_PATTERNS:
        match = re.search(pattern, q_low, re.IGNORECASE)
        if match:
            val = match.group(1) if len(match.groups()) >= 1 else match.group(0)
            clinical_metrics[metric_name] = f"{val} {unit}".strip()

    return ClinicalEntities(
        primary_condition=primary_condition,
        interventions=interventions,
        patient_demographics=demographics,
        clinical_metrics=clinical_metrics,
    )


def detect_missing_variables_and_gaps(
    query: str, entities: ClinicalEntities
) -> tuple[List[str], List[str], List[str]]:
    """
    Evaluates guideline-mandated variable dependencies and produces anti-hallucination
    context gaps when critical clinical parameters are omitted.
    """
    q_low = query.lower()
    missing_vars: List[str] = []
    context_gaps: List[str] = []
    clarifications: List[str] = []

    # 1. Paxlovid / COVID-19 Antiviral Requirements
    if any(k in q_low for k in ["paxlovid", "nirmatrelvir", "antiviral", "covid"]):
        has_egfr = any(k in entities.clinical_metrics for k in ["eGFR", "Creatinine"]) or "egfr" in q_low or "kidney" in q_low
        has_duration = "symptom_duration" in entities.clinical_metrics or "day" in q_low or "onset" in q_low
        has_concomitant = any(k in q_low for k in ["medication", "taking", "statin", "interaction", "drug list"])

        if not has_egfr:
            missing_vars.append("Renal Function Metric (Baseline eGFR / Creatinine Clearance)")
            context_gaps.append(
                "Guideline application strictly depends on renal function: Paxlovid requires dose reduction at eGFR 30–59 mL/min (150mg/100mg BID) and is contraindicated if eGFR <30 mL/min."
            )
            clarifications.append("Specify patient eGFR (e.g., eGFR ≥60 mL/min vs. eGFR 30–59 mL/min)")

        if not has_duration:
            missing_vars.append("Symptom Duration / Initiation Window (<5 days vs >5 days)")
            context_gaps.append(
                "Antiviral efficacy degrades rapidly beyond symptom day 5 (EPIC-HR protocol requires initiation within ≤5 days of confirmed onset)."
            )
            clarifications.append("Confirm days since symptom onset (e.g., within 5 days)")

        if not has_concomitant and ("dose" in q_low or "prescribe" in q_low or "eligible" in q_low):
            missing_vars.append("Concomitant Medications (CYP3A4 substrates / inducers)")
            context_gaps.append(
                "Ritonavir component is a potent CYP3A4 inhibitor; comprehensive co-medication audit is required to prevent severe drug-drug interactions."
            )

    # 2. Asthma Management (Acuity & Controller vs Rescue)
    elif any(k in q_low for k in ["asthma", "inhaler", "wheez", "budesonide", "albuterol"]):
        has_acuity = any(k in q_low for k in ["acute", "attack", "emergency", "flare", "exacerbation", "maintenance", "daily", "chronic", "control"])
        has_step = any(k in q_low for k in ["mild", "moderate", "severe", "step", "fev1", "peak flow"])

        if not has_acuity:
            missing_vars.append("Clinical Acuity Status (Chronic Maintenance vs. Acute Severe Exacerbation)")
            context_gaps.append(
                "Guideline protocols diverge completely between chronic daily controller therapy (e.g. GINA SMART anti-inflammatory reliever) and acute severe exacerbation requiring emergency systemic corticosteroids and high-dose nebulization."
            )
            clarifications.append("Clarify if this is for routine daily maintenance or an acute sudden asthma attack")

        if not has_step:
            missing_vars.append("Asthma Severity Classification / Baseline Control Tier")
            context_gaps.append(
                "Inhaled medication dosing escalates based on GINA Steps 1–5 depending on nighttime awakenings and rescue inhaler frequency."
            )

    # 3. Hypertension & Blood Pressure
    elif any(k in q_low for k in ["hypertension", "blood pressure", "bp", "amlodipine", "lisinopril"]):
        has_bp_val = "blood_pressure" in entities.clinical_metrics or any(c.isdigit() for c in q_low if "/" in q_low)
        has_pregnancy = entities.patient_demographics.pregnancy_status is not None or "pregnant" in q_low or "pregnancy" in q_low

        if not has_bp_val:
            missing_vars.append("Baseline Blood Pressure Measurements (Systolic/Diastolic staging)")
            context_gaps.append(
                "Therapeutic thresholds depend on blood pressure staging (ACC/AHA Stage 1: 130–139/80–89 mmHg vs. Stage 2: ≥140/90 mmHg; dual-agent therapy is recommended if BP is ≥20/10 mmHg above target)."
            )
            clarifications.append("Provide current resting blood pressure reading (e.g., 145/92 mmHg)")

        if not has_pregnancy and ("woman" in q_low or "female" in q_low or "pregnant" in q_low):
            missing_vars.append("Pregnancy Status (Teratogenic medication check)")
            context_gaps.append(
                "ACE inhibitors (Lisinopril) and ARBs (Losartan) are strictly contraindicated in pregnancy due to fetal renal toxicity; Labetalol or Nifedipine are preferred."
            )

    # 4. Type 2 Diabetes & GLP-1 RA / SGLT2i
    elif any(k in q_low for k in ["diabetes", "semaglutide", "ozempic", "glp-1", "mounjaro", "sugar"]):
        has_hba1c = "HbA1c" in entities.clinical_metrics or "a1c" in q_low
        has_ascvd_ckd = any(k in q_low for k in ["kidney", "heart", "cvd", "ascvd", "stroke", "ckd", "hf"])

        if not has_hba1c:
            missing_vars.append("Baseline Glycemic Metric (HbA1c %)")
            context_gaps.append(
                "ADA Standards of Care calibrate escalation thresholds against baseline HbA1c (individualized target typically <7.0% vs. <8.0% in frail elderly)."
            )
            clarifications.append("Specify baseline HbA1c (e.g. HbA1c 8.2%)")

        if not has_ascvd_ckd:
            missing_vars.append("Cardiovascular & Renal Comorbidity Phenotype (ASCVD, HF, or CKD status)")
            context_gaps.append(
                "Independent of baseline HbA1c, presence of established ASCVD or CKD mandates GLP-1 RA or SGLT2i with proven organ protection per ADA/KDIGO consensus."
            )

    # 5. Cholesterol & Statin Therapy
    elif any(k in q_low for k in ["cholesterol", "statin", "atorvastatin", "ldl", "lipid"]):
        has_ldl = "LDL-C" in entities.clinical_metrics or "ldl" in q_low
        has_risk = any(k in q_low for k in ["ascvd", "risk", "infarct", "stroke", "diabetic", "primary prevention", "secondary prevention"])

        if not has_ldl:
            missing_vars.append("Baseline Lipid Profile (LDL-C mg/dL)")
            context_gaps.append(
                "Statin intensity (High vs. Moderate) is governed by baseline LDL-C and target percentage reduction (≥50% reduction for high-intensity)."
            )
            clarifications.append("Provide baseline LDL-C value (e.g. LDL 160 mg/dL)")

        if not has_risk:
            missing_vars.append("10-Year ASCVD Risk Category / Primary vs Secondary Prevention")
            context_gaps.append(
                "Guideline recommendations differ significantly between primary prevention (risk-calculator driven) and secondary prevention (mandatory high-intensity statin ± ezetimibe)."
            )

    # 6. Heart Failure
    elif any(k in q_low for k in ["heart failure", "hfref", "hfpef", "chf"]):
        has_lvef = "LVEF" in entities.clinical_metrics or "ejection fraction" in q_low or "lvef" in q_low
        if not has_lvef:
            missing_vars.append("Left Ventricular Ejection Fraction (LVEF % - HFrEF vs HFpEF)")
            context_gaps.append(
                "Guideline-Directed Medical Therapy (GDMT 4-pillar regimen) is specifically mandated for HFrEF (LVEF ≤40%), whereas HFpEF (LVEF ≥50%) emphasizes SGLT2i and diuretic symptom control."
            )
            clarifications.append("Specify LVEF percentage or subtype (e.g. HFrEF LVEF 35% vs HFpEF)")

    return missing_vars, context_gaps, clarifications


def parse_clinical_query(query: str) -> ParsedQueryAnalysis:
    """
    Main entry point for Stage 1 Inbound Analysis.
    Deconstructs the raw query, extracts entities, and detects missing clinical parameters.
    """
    entities = extract_clinical_entities(query)
    missing_vars, context_gaps, clarifications = detect_missing_variables_and_gaps(query, entities)

    requires_disambiguation = len(missing_vars) > 0 or len(context_gaps) > 0

    return ParsedQueryAnalysis(
        raw_query=query,
        entities=entities,
        missing_variables=missing_vars,
        context_gaps=context_gaps,
        requires_disambiguation=requires_disambiguation,
        recommended_clarifications=clarifications,
    )
