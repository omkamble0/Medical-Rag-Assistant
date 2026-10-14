"""
Clinical Query Rewriting & Sub-Query Decomposition Module
Translates layperson symptom expressions into standardized MeSH / SNOMED CT terminology
and splits complex queries into targeted multi-angle sub-queries.
"""

import re
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

# Colloquial to MeSH / Medical terminology mapping
COLLOQUIAL_TO_MESH = {
    "high blood pressure": "Essential Hypertension",
    "high bp": "Essential Hypertension",
    "sugar": "Type 2 Diabetes Mellitus",
    "sugar problem": "Type 2 Diabetes Mellitus",
    "sugar disease": "Type 2 Diabetes Mellitus",
    "water pill": "Thiazide Diuretic",
    "blood thinner": "Anticoagulant / Antiplatelet",
    "bad cholesterol": "LDL Hyperlipidemia / Dyslipidemia",
    "fatty liver": "Metabolic Dysfunction-Associated Steatohepatitis (MASH/NAFLD)",
    "chest pain": "Acute Coronary Syndrome / Angina Pectoris",
    "short of breath": "Dyspnea / Pulmonary Impairment",
    "puffer": "Metered Dose Inhaler (ICS/LABA)",
    "headache": "Cephalea / Primary Headache Disorder",
    "migraine": "Migraine with/without Aura",
    "kidney failure": "Chronic Kidney Disease (CKD)",
    "heart attack": "Myocardial Infarction",
    "stroke": "Acute Cerebrovascular Event / CVA"
}

# Medication synonym mapping
KNOWN_MEDICATIONS = [
    "paxlovid", "nirmatrelvir", "ritonavir", "remdesivir", "veklury",
    "semaglutide", "ozempic", "wegovy", "tirzepatide", "mounjaro", "metformin",
    "lisinopril", "losartan", "amlodipine", "metoprolol", "carvedilol",
    "atorvastatin", "rosuvastatin", "simvastatin", "ezetimibe",
    "budesonide", "formoterol", "albuterol", "salbutamol", "fluticasone",
    "apixaban", "eliquis", "rivaroxaban", "xarelto", "warfarin",
    "ibuprofen", "naproxen", "aspirin", "acetaminophen", "paracetamol",
    "sertraline", "escitalopram", "fluoxetine", "duloxetine", "tramadol"
]


class ClinicalQueryDecomposition(BaseModel):
    raw_query: str
    canonical_condition: str
    mesh_terms: List[str]
    identified_drugs: List[str]
    clinical_metrics: Dict[str, Any]
    sub_queries: List[str] = Field(..., description="Targeted sub-queries for multi-vector retrieval")
    needs_drug_interaction_check: bool = False
    needs_clinical_calculator: bool = False
    recommended_calculator: Optional[str] = None


def rewrite_clinical_query(raw_query: str) -> ClinicalQueryDecomposition:
    """
    Deconstructs user query into MeSH terminology, extracts drugs and metrics,
    and generates 3 targeted sub-queries for multi-query retrieval.
    """
    q_clean = raw_query.strip()
    q_low = q_clean.lower()

    # 1. Map to Canonical Condition & MeSH
    canonical_condition = "General Clinical Inquiry"
    matched_mesh = []

    for phrase, mesh in COLLOQUIAL_TO_MESH.items():
        if phrase in q_low:
            canonical_condition = mesh
            matched_mesh.append(mesh)

    # Secondary checks
    if "hypertension" in q_low or "bp" in q_low:
        canonical_condition = "Essential Hypertension"
        matched_mesh.extend(["Blood Pressure Regulation", "ACC/AHA Guidelines"])
    elif "diabetes" in q_low or "glp-1" in q_low or "a1c" in q_low:
        canonical_condition = "Type 2 Diabetes Mellitus & Incretin Therapy"
        matched_mesh.extend(["Glycemic Target", "ADA Standards of Care", "Cardiovascular Outcomes"])
    elif "asthma" in q_low or "inhaler" in q_low:
        canonical_condition = "Asthma & Bronchospastic Disorders"
        matched_mesh.extend(["GINA Strategy", "ICS-Formoterol", "Bronchodilation"])
    elif "cholesterol" in q_low or "statin" in q_low:
        canonical_condition = "Atherosclerotic Cardiovascular Disease & Dyslipidemia"
        matched_mesh.extend(["LDL-C Targets", "Statin Safety", "ESC/AHA Guidelines"])
    elif "covid" in q_low or "coronavirus" in q_low or "paxlovid" in q_low:
        canonical_condition = "COVID-19 (SARS-CoV-2) Antiviral Therapy"
        matched_mesh.extend(["EPIC-HR", "CYP3A4 Inhibition", "Oral Antivirals"])
    elif "headache" in q_low or "migraine" in q_low:
        canonical_condition = "Primary Cephalea & Migraine Management"
        matched_mesh.extend(["ICHD-3 Criteria", "Abortive Therapy", "Red Flag Triage"])

    # Remove duplicates
    matched_mesh = list(dict.fromkeys(matched_mesh))

    # 2. Extract medications
    identified_drugs = []
    for med in KNOWN_MEDICATIONS:
        if re.search(r'\b' + re.escape(med) + r'\b', q_low):
            identified_drugs.append(med.title())

    needs_ddi = len(identified_drugs) >= 2 or any(d.lower() in ["paxlovid", "ritonavir", "warfarin"] for d in identified_drugs)

    # 3. Extract numerical metrics
    metrics: Dict[str, Any] = {}
    bp_match = re.search(r'\b(\d{2,3})\s*[/]\s*(\d{2,3})\b', q_clean)
    if bp_match:
        metrics["blood_pressure"] = f"{bp_match.group(1)}/{bp_match.group(2)} mmHg"
        metrics["systolic"] = int(bp_match.group(1))
        metrics["diastolic"] = int(bp_match.group(2))

    a1c_match = re.search(r'\b(?:a1c|hba1c)\s*(?:of|is|:)?\s*(\d+(?:\.\d+)?)\s*%?', q_low)
    if a1c_match:
        metrics["hba1c"] = float(a1c_match.group(1))

    egfr_match = re.search(r'\b(?:egfr|gfr)\s*(?:of|is|:)?\s*(\d+(?:\.\d+)?)\b', q_low)
    if egfr_match:
        metrics["egfr"] = float(egfr_match.group(1))

    creat_match = re.search(r'\b(?:creatinine|cr)\s*(?:of|is|:)?\s*(\d+(?:\.\d+)?)\b', q_low)
    if creat_match:
        metrics["creatinine"] = float(creat_match.group(1))

    bmi_match = re.search(r'\b(?:bmi)\s*(?:of|is|:)?\s*(\d+(?:\.\d+)?)\b', q_low)
    if bmi_match:
        metrics["bmi"] = float(bmi_match.group(1))

    # Detect if clinical calculator is recommended
    needs_calc = False
    recommended_calc = None
    if "creatinine" in metrics or "egfr" in q_low or "kidney function" in q_low:
        needs_calc = True
        recommended_calc = "egfr"
    elif "bmi" in metrics or "weight loss" in q_low or "obesity" in q_low:
        needs_calc = True
        recommended_calc = "bmi"
    elif "stroke risk" in q_low or "afib" in q_low or "atrial fibrillation" in q_low:
        needs_calc = True
        recommended_calc = "cha2ds2_vasc"
    elif "pulmonary embolism" in q_low or "pe" in q_low or "dvt" in q_low:
        needs_calc = True
        recommended_calc = "wells_pe"

    # 4. Generate targeted sub-queries for multi-query retrieval
    sub_queries = [
        f"{canonical_condition} guideline first line therapy and consensus recommendations",
        f"{canonical_condition} trial endpoints safety contraindications and organ cutoffs",
        f"{canonical_condition} patient education lifestyle interventions and red flags"
    ]

    return ClinicalQueryDecomposition(
        raw_query=raw_query,
        canonical_condition=canonical_condition,
        mesh_terms=matched_mesh,
        identified_drugs=identified_drugs,
        clinical_metrics=metrics,
        sub_queries=sub_queries,
        needs_drug_interaction_check=needs_ddi,
        needs_clinical_calculator=needs_calc,
        recommended_calculator=recommended_calc
    )
