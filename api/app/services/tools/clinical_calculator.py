"""
Clinical Risk & Physiological Formula Calculator Tool
Implements validated, peer-reviewed medical calculation algorithms:
- 2021 CKD-EPI Race-Free Creatinine eGFR (KDIGO 2024 guidance)
- World Health Organization (WHO) BMI & Metabolic Staging
- CHA2DS2-VASc Atrial Fibrillation Stroke Risk Stratification
- Wells Criteria for Pulmonary Embolism (PE) Clinical Probability
"""

import math
from typing import Dict, Any, Optional
from langchain_core.tools import tool


def calculate_egfr(creatinine: float, age: int, sex: str) -> Dict[str, Any]:
    """
    Computes estimated Glomerular Filtration Rate (eGFR) using the 2021 CKD-EPI race-free equation.
    Scr in mg/dL, age in years, sex in ['male', 'female'].
    """
    if creatinine <= 0:
        raise ValueError("Serum creatinine must be strictly positive (> 0 mg/dL).")
    if age < 0 or age > 130:
        raise ValueError("Age must be between 0 and 130 years.")

    is_female = sex.strip().lower() in ["f", "female", "woman", "girl"]
    kappa = 0.7 if is_female else 0.9
    alpha = -0.241 if is_female else -0.302
    gender_mult = 1.012 if is_female else 1.000

    scr_div_kappa = creatinine / kappa
    min_term = min(scr_div_kappa, 1.0) ** alpha
    max_term = max(scr_div_kappa, 1.0) ** (-1.200)
    age_term = 0.9938 ** age

    egfr_val = round(142.0 * min_term * max_term * age_term * gender_mult, 1)

    # KDIGO Staging
    if egfr_val >= 90:
        stage = "G1 (Normal or High Kidney Function)"
        clinical_interpretation = "Normal kidney filtration function."
    elif egfr_val >= 60:
        stage = "G2 (Mildly Decreased)"
        clinical_interpretation = "Mildly decreased filtration; generally normal in healthy elderly individuals."
    elif egfr_val >= 45:
        stage = "G3a (Mild to Moderately Decreased)"
        clinical_interpretation = "Early chronic kidney disease; medication dosage reconciliation advised."
    elif egfr_val >= 30:
        stage = "G3b (Moderately to Severely Decreased)"
        clinical_interpretation = "Moderate CKD; mandatory organ-clearance medication adjustments."
    elif egfr_val >= 15:
        stage = "G4 (Severely Decreased)"
        clinical_interpretation = "Severe kidney impairment; prepare for nephrology co-management and dialysis planning."
    else:
        stage = "G5 (Kidney Failure / End-Stage Renal Disease)"
        clinical_interpretation = "Kidney failure; urgent nephrology referral for renal replacement therapy."

    # Critical Drug Dosing Thresholds
    dosing_alerts = []
    if egfr_val < 30:
        dosing_alerts.append("PAXLOVID: Absolute Contraindication (eGFR < 30 mL/min).")
        dosing_alerts.append("METFORMIN: Contraindicated due to fatal lactic acidosis risk.")
        dosing_alerts.append("SGLT2i: Not recommended for glycemic initiation; monitor for fluid balance.")
    elif egfr_val < 60:
        dosing_alerts.append("PAXLOVID: Dose reduction mandatory (150mg Nirmatrelvir + 100mg Ritonavir BID).")
        dosing_alerts.append("METFORMIN: Maximum dose 1,000 mg daily; monitor renal panel every 3-6 months.")
        dosing_alerts.append("DOACs (Apixaban, Rivaroxaban): Review creatinine clearance for dose de-escalation.")
    else:
        dosing_alerts.append("Standard renal clearance parameters apply for guideline-directed oral pharmacotherapy.")

    return {
        "calculator": "2021 CKD-EPI Race-Free eGFR",
        "egfr": egfr_val,
        "unit": "mL/min/1.73 m²",
        "stage": stage,
        "interpretation": clinical_interpretation,
        "pharmacotherapy_alerts": dosing_alerts,
        "inputs": {"creatinine_mg_dl": creatinine, "age": age, "sex": "female" if is_female else "male"}
    }


def calculate_bmi(weight_kg: float, height_cm: float) -> Dict[str, Any]:
    """
    Computes Body Mass Index (BMI) and WHO metabolic category.
    weight in kg, height in cm.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0 kg.")
    height_m = height_cm / 100.0
    if height_m <= 0:
        raise ValueError("Height must be greater than 0 cm.")
    bmi_val = round(weight_kg / (height_m ** 2), 1)

    if bmi_val < 18.5:
        category = "Underweight"
        glp1_eligibility = "Not indicated for weight management pharmacotherapy."
    elif bmi_val < 25.0:
        category = "Normal Weight"
        glp1_eligibility = "Not indicated for weight loss agents."
    elif bmi_val < 30.0:
        category = "Overweight"
        glp1_eligibility = "Eligible for anti-obesity medications (e.g. Semaglutide/Tirzepatide) only if at least one weight-related comorbidity is present (Hypertension, T2D, Dyslipidemia, Sleep Apnea)."
    elif bmi_val < 35.0:
        category = "Class I Obesity"
        glp1_eligibility = "Full FDA/EMA guideline eligibility for GLP-1/GIP receptor agonist therapy alongside lifestyle modifications."
    elif bmi_val < 40.0:
        category = "Class II Obesity"
        glp1_eligibility = "Indicated for dual GLP-1/GIP incretin therapy and bariatric metabolic evaluation."
    else:
        category = "Class III Obesity (Severe / Morbid Obesity)"
        glp1_eligibility = "Strong consensus indication for comprehensive medical and surgical metabolic intervention."

    return {
        "calculator": "WHO Body Mass Index (BMI)",
        "bmi": bmi_val,
        "unit": "kg/m²",
        "category": category,
        "guideline_indications": glp1_eligibility,
        "inputs": {"weight_kg": weight_kg, "height_cm": height_cm}
    }


def calculate_cha2ds2_vasc(
    chf: bool = False,
    htn: bool = False,
    age: int = 50,
    diabetes: bool = False,
    stroke_history: bool = False,
    vascular_disease: bool = False,
    sex: str = "male"
) -> Dict[str, Any]:
    """
    Computes CHA2DS2-VASc score for non-valvular Atrial Fibrillation stroke risk.
    """
    score = 0
    breakdown = []

    if chf:
        score += 1
        breakdown.append("Congestive Heart Failure (+1)")
    if htn:
        score += 1
        breakdown.append("Hypertension (+1)")

    if age >= 75:
        score += 2
        breakdown.append("Age >= 75 years (+2)")
    elif age >= 65:
        score += 1
        breakdown.append("Age 65-74 years (+1)")

    if diabetes:
        score += 1
        breakdown.append("Diabetes Mellitus (+1)")
    if stroke_history:
        score += 2
        breakdown.append("Prior Stroke / TIA / Thromboembolism (+2)")
    if vascular_disease:
        score += 1
        breakdown.append("Vascular Disease (Prior MI, PAD, Aortic plaque) (+1)")

    is_female = sex.strip().lower() in ["f", "female", "woman"]
    if is_female:
        score += 1
        breakdown.append("Female Sex Category (+1)")

    # Anticoagulation threshold (AHA/ACC/ESC Guidelines)
    threshold = 2 if is_female else 1
    high_threshold = 3 if is_female else 2

    if score >= high_threshold:
        recommendation = "Oral Anticoagulation (DOAC e.g. Apixaban, Rivaroxaban) STRONGLY RECOMMENDED unless contraindicated (Class I, Level A)."
        risk_level = "High Annual Thromboembolic Risk"
    elif score >= threshold:
        recommendation = "Oral Anticoagulation SHOULD BE CONSIDERED based on individualized bleeding risk discussion (Class IIa)."
        risk_level = "Intermediate Annual Thromboembolic Risk"
    else:
        recommendation = "No antithrombotic therapy recommended; low risk of ischemic stroke (Class III)."
        risk_level = "Low Annual Thromboembolic Risk"

    return {
        "calculator": "CHA2DS2-VASc Stroke Risk Score",
        "score": score,
        "risk_level": risk_level,
        "recommendation": recommendation,
        "point_breakdown": breakdown
    }


def calculate_wells_pe(
    dvt_signs: bool = False,
    alternative_less_likely: bool = False,
    hr_over_100: bool = False,
    immobility: bool = False,
    prior_pe_dvt: bool = False,
    hemoptysis: bool = False,
    active_cancer: bool = False
) -> Dict[str, Any]:
    """
    Computes Wells Criteria for Pulmonary Embolism (PE) probability.
    """
    score = 0.0
    items = []
    if dvt_signs:
        score += 3.0
        items.append("Clinical signs/symptoms of DVT (+3.0)")
    if alternative_less_likely:
        score += 3.0
        items.append("Alternative diagnosis less likely than PE (+3.0)")
    if hr_over_100:
        score += 1.5
        items.append("Heart rate > 100 bpm (+1.5)")
    if immobility:
        score += 1.5
        items.append("Immobilization >= 3 days or surgery in past 4 weeks (+1.5)")
    if prior_pe_dvt:
        score += 1.5
        items.append("Previous objectively diagnosed PE or DVT (+1.5)")
    if hemoptysis:
        score += 1.0
        items.append("Hemoptysis (+1.0)")
    if active_cancer:
        score += 1.0
        items.append("Active malignancy treated in past 6 months (+1.0)")

    # 3-tier model
    if score > 6.0:
        prob = "High Probability (>6.0 points)"
        action = "Immediate CT Pulmonary Angiography (CTPA) indicated. Consider empiric therapeutic anticoagulation while awaiting imaging."
    elif score >= 2.0:
        prob = "Moderate Probability (2.0 - 6.0 points)"
        action = "High-sensitivity D-dimer assay recommended; proceed to CTPA if D-dimer elevated."
    else:
        prob = "Low Probability (<2.0 points)"
        action = "Apply PERC rule or perform high-sensitivity D-dimer. If negative, PE safely excluded without radiation."

    return {
        "calculator": "Wells Criteria for Pulmonary Embolism",
        "score": score,
        "probability_tier": prob,
        "clinical_action": action,
        "matched_criteria": items
    }


@tool
def clinical_calculator_tool(formula: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes clinical calculators for eGFR, BMI, CHA2DS2-VASc, or Wells PE score.
    Parameters:
      formula: 'egfr', 'bmi', 'cha2ds2_vasc', or 'wells_pe'
      parameters: dict containing relevant inputs (e.g. {'creatinine': 1.4, 'age': 65, 'sex': 'male'})
    """
    f = formula.strip().lower()
    if f in ["egfr", "gfr", "kidney"]:
        return calculate_egfr(
            creatinine=float(parameters.get("creatinine", 1.0)),
            age=int(parameters.get("age", 55)),
            sex=str(parameters.get("sex", "male"))
        )
    elif f in ["bmi", "weight", "obesity"]:
        return calculate_bmi(
            weight_kg=float(parameters.get("weight_kg", parameters.get("weight", 70))),
            height_cm=float(parameters.get("height_cm", parameters.get("height", 175)))
        )
    elif f in ["cha2ds2_vasc", "afib", "stroke_risk"]:
        return calculate_cha2ds2_vasc(
            chf=bool(parameters.get("chf", False)),
            htn=bool(parameters.get("htn", False)),
            age=int(parameters.get("age", 60)),
            diabetes=bool(parameters.get("diabetes", False)),
            stroke_history=bool(parameters.get("stroke_history", False)),
            vascular_disease=bool(parameters.get("vascular_disease", False)),
            sex=str(parameters.get("sex", "male"))
        )
    elif f in ["wells", "wells_pe", "pulmonary_embolism"]:
        return calculate_wells_pe(
            dvt_signs=bool(parameters.get("dvt_signs", False)),
            alternative_less_likely=bool(parameters.get("alternative_less_likely", False)),
            hr_over_100=bool(parameters.get("hr_over_100", False)),
            immobility=bool(parameters.get("immobility", False)),
            prior_pe_dvt=bool(parameters.get("prior_pe_dvt", False)),
            hemoptysis=bool(parameters.get("hemoptysis", False)),
            active_cancer=bool(parameters.get("active_cancer", False))
        )
    else:
        return {
            "error": f"Unknown clinical calculator '{formula}'. Supported formulas: 'egfr', 'bmi', 'cha2ds2_vasc', 'wells_pe'."
        }
