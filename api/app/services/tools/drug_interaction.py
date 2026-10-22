"""
Clinical Drug-Drug Interaction (DDI) and Safety Screening Tool
Detects dangerous pharmaceutical interactions, CYP450 metabolism conflicts,
Black Box warnings, and organ clearance cutoffs.
"""

from typing import List, Dict, Any, Tuple
from langchain_core.tools import tool

# High-risk drug interaction matrix
DDI_RULES: List[Dict[str, Any]] = [
    {
        "drugs": [["nitroglycerin", "nitro", "isosorbide", "nitrate"], ["sildenafil", "viagra", "tadalafil", "cialis", "vardenafil", "pde5 inhibitor"]],
        "severity": "CONTRAINDICATED",
        "mechanism": "Co-administration causes synergistic potentiation of cyclic GMP-mediated vasodilation.",
        "clinical_risk": "Severe, refractory systemic hypotension, cardiovascular collapse, and fatal myocardial infarction.",
        "management": "Strictly contraindicated. Do not administer nitrates within 24 hours of sildenafil/vardenafil or within 48 hours of tadalafil."
    },
    {
        "drugs": [["methotrexate", "mtx"], ["ibuprofen", "naproxen", "meloxicam", "aspirin", "nsaid"]],
        "severity": "CONTRAINDICATED",
        "mechanism": "NSAIDs decrease renal blood flow and inhibit renal tubular secretion of methotrexate.",
        "clinical_risk": "Severe, life-threatening methotrexate toxicity including fatal myelosuppression, pancytopenia, and acute renal failure.",
        "management": "Avoid concomitant NSAIDs with high-dose methotrexate; exercise extreme vigilance and monitor CBC/renal panels with low-dose regimens."
    },
    {
        "drugs": [["spironolactone", "eplerenone", "aldactone"], ["lisinopril", "losartan", "ramipril", "valsartan", "ace inhibitor", "arb", "potassium", "klor-con"]],
        "severity": "MAJOR",
        "mechanism": "Synergistic inhibition of aldosterone-mediated renal potassium excretion.",
        "clinical_risk": "Severe hyperkalemia (K+ > 6.0 mEq/L) predisposing to fatal cardiac dysrhythmias and asystole.",
        "management": "Check baseline serum potassium and creatinine before initiation; re-check at 1, 4, and 12 weeks. Maintain dietary potassium awareness."
    },
    {
        "drugs": [["paxlovid", "nirmatrelvir", "ritonavir"], ["simvastatin", "lovastatin", "atorvastatin", "statin"]],
        "severity": "CONTRAINDICATED",
        "mechanism": "Ritonavir is an ultra-potent CYP3A4 inhibitor, leading to massive accumulation of statin plasma levels.",
        "clinical_risk": "Severe rhabdomyolysis, acute renal failure, and myopathy.",
        "management": "Withhold simvastatin/lovastatin during 5-day Paxlovid treatment course and for 3-5 days after completion. Consider temporary hold of atorvastatin or rosuvastatin."
    },
    {
        "drugs": [["paxlovid", "nirmatrelvir", "ritonavir"], ["amiodarone", "flecainide", "propafenone", "antiarrhythmic"]],
        "severity": "CONTRAINDICATED",
        "mechanism": "CYP3A4 inhibition markedly increases antiarrhythmic concentrations.",
        "clinical_risk": "Life-threatening cardiac arrhythmias, QT prolongation, and cardiac arrest.",
        "management": "Paxlovid is strictly contraindicated with amiodarone and flecainide. Select alternative COVID-19 therapy (IV Remdesivir or convalescent plasma)."
    },
    {
        "drugs": [["paxlovid", "nirmatrelvir", "ritonavir"], ["rivaroxaban", "apixaban", "dabigatran", "doac", "blood thinner"]],
        "severity": "MAJOR",
        "mechanism": "Ritonavir inhibits CYP3A4 and P-glycoprotein, impairing direct oral anticoagulant elimination.",
        "clinical_risk": "Significantly elevated systemic exposure and severe, potentially fatal hemorrhage.",
        "management": "Dose reduction or temporary hold of DOAC with bridging therapy where clinically indicated. Consult hematology or use IV remdesivir."
    },
    {
        "drugs": [["lisinopril", "enalapril", "ramipril", "ace inhibitor", "acei"], ["losartan", "valsartan", "candesartan", "arb"]],
        "severity": "CONTRAINDICATED",
        "mechanism": "Dual Renin-Angiotensin-Aldosterone System (RAAS) blockade without additive clinical benefit.",
        "clinical_risk": "Severe hyperkalemia, acute kidney injury (AKI), and refractory systemic hypotension.",
        "management": "Contraindicated. Discontinue one agent immediately and monotherapy or combine with calcium channel blocker/thiazide diuretic instead."
    },
    {
        "drugs": [["lisinopril", "enalapril", "losartan", "valsartan", "ace inhibitor", "arb"], ["ibuprofen", "naproxen", "meloxicam", "diclofenac", "nsaid"]],
        "severity": "MAJOR",
        "mechanism": "NSAIDs inhibit renal prostaglandins causing afferent arteriolar constriction; ACEi/ARBs cause efferent arteriolar vasodilation ('Triple Whammy' with diuretics).",
        "clinical_risk": "Marked acute drop in glomerular filtration rate (AKI) and blunting of antihypertensive effect.",
        "management": "Avoid routine NSAID therapy in patients taking ACEi/ARBs. Recommend acetaminophen for analgesia or perform baseline serum creatinine/potassium checks."
    },
    {
        "drugs": [["semaglutide", "ozempic", "wegovy", "tirzepatide", "mounjaro", "glp-1"], ["insulin", "glargine", "lispro", "glipizide", "glimepiride", "sulfonylurea"]],
        "severity": "MAJOR",
        "mechanism": "Additive potentiation of glucose disposal; delayed gastric emptying may cause unpredictable carbohydrate absorption.",
        "clinical_risk": "Severe symptomatic hypoglycemia and altered oral absorption kinetics.",
        "management": "Pre-emptively reduce baseline basal insulin by 20% and/or taper sulfonylurea dose upon initiating GLP-1 RA. Instruct patient on glucose monitoring."
    },
    {
        "drugs": [["sertraline", "fluoxetine", "escitalopram", "paroxetine", "citalopram", "ssri", "snri", "duloxetine", "venlafaxine"], ["tramadol", "linezolid", "sumatriptan", "triptan", "maoi"]],
        "severity": "MAJOR",
        "mechanism": "Additive serotonergic neurotransmission and inhibition of serotonin reuptake.",
        "clinical_risk": "Serotonin Syndrome (autonomic instability, hyperreflexia, hyperthermia, delirium).",
        "management": "Avoid concomitant administration of tramadol with serotonergic antidepressants. Monitor closely for tremors, clonus, diaphoresis, and fever."
    },
    {
        "drugs": [["sertraline", "fluoxetine", "escitalopram", "ssri"], ["ibuprofen", "naproxen", "aspirin", "nsaid"]],
        "severity": "MODERATE",
        "mechanism": "SSRIs deplete platelet serotonin stores needed for aggregation; NSAIDs inhibit platelet thromboxane A2 and damage gastric mucosa.",
        "clinical_risk": "Up to a 4-fold increase in upper gastrointestinal ulceration and bleeding.",
        "management": "Co-prescribe a proton pump inhibitor (PPI like omeprazole) if co-therapy is clinically indispensable."
    },
    {
        "drugs": [["metoprolol", "carvedilol", "atenolol", "bisoprolol", "beta blocker"], ["verapamil", "diltiazem", "non-dhp ccb"]],
        "severity": "MAJOR",
        "mechanism": "Additive negative inotropic, chronotropic, and dromotropic cardiac depression.",
        "clinical_risk": "Severe symptomatic bradycardia, complete heart block (3rd degree AV block), and cardiogenic shock.",
        "management": "Generally contraindicated outside of strictly monitored electrophysiology settings. Prefer dihydropyridine CCB (e.g. Amlodipine) if dual therapy is needed."
    },
    {
        "drugs": [["warfarin", "coumadin"], ["ciprofloxacin", "fluconazole", "metronidazole", "bactrim", "amiodarone"]],
        "severity": "CONTRAINDICATED",
        "mechanism": "Inhibition of CYP2C9 and clearance of the more potent S-warfarin enantiomer.",
        "clinical_risk": "Dramatic prolongation of International Normalized Ratio (INR) and life-threatening bleeding.",
        "management": "Select alternative antibiotic/antifungal or reduce warfarin dose by 30-50% with serial INR monitoring within 48-72 hours."
    },
    {
        "drugs": [["metformin"], ["iodinated contrast", "ct contrast"]],
        "severity": "MAJOR",
        "mechanism": "Contrast-induced nephropathy can impair metformin clearance leading to massive intracellular drug accumulation.",
        "clinical_risk": "Metformin-associated lactic acidosis (MALA), with mortality rates exceeding 30-50%.",
        "management": "Withhold metformin prior to or at time of iodinated contrast procedure if eGFR <60 or patient is acutely ill; re-evaluate eGFR 48 hours later before resumption."
    }
]

# Black box warnings and single-agent safety profiles
SINGLE_DRUG_PROFILES: Dict[str, Dict[str, Any]] = {
    "semaglutide": {
        "black_box_warning": "Thyroid C-Cell Tumors: Absolute contraindication in patients with personal or family history of Medullary Thyroid Carcinoma (MTC) or MEN 2.",
        "key_precautions": "Risk of acute pancreatitis, gallbladder disease, and diabetic retinopathy progression with rapid glycemic improvement.",
        "organ_thresholds": "No dose adjustment required for renal impairment, but caution advised due to nausea-induced volume contraction and dehydration."
    },
    "paxlovid": {
        "black_box_warning": "Severe Drug Interactions: Highly potent CYP3A4 inhibition can cause fatal drug toxicities or loss of virologic response.",
        "key_precautions": "Must be initiated within 5 days of symptom onset. Rebound symptoms reported in a minority of patients.",
        "organ_thresholds": "eGFR 30–59 mL/min: Dose reduction mandatory (150mg/100mg BID). eGFR <30 mL/min or severe Child-Pugh C hepatic impairment: Absolutely contraindicated."
    },
    "lisinopril": {
        "black_box_warning": "Fetal Toxicity: Discontinue immediately if pregnancy is detected (causes oligohydramnios, fetal renal agenesis, and fetal death in 2nd/3rd trimesters).",
        "key_precautions": "Angioedema (higher incidence in Black patients), dry persistent cough, hyperkalemia.",
        "organ_thresholds": "Evaluate serum creatinine and potassium at 2–4 weeks post-initiation. Titrate carefully if eGFR <30 mL/min."
    },
    "metformin": {
        "black_box_warning": "Lactic Acidosis: Severe metabolic acidosis associated with metformin accumulation, particularly in hypoxemic or renal impaired states.",
        "key_precautions": "Gastrointestinal distress, vitamin B12 deficiency on long-term therapy.",
        "organ_thresholds": "Contraindicated if eGFR <30 mL/min. Maximum dose 1,000 mg/day if eGFR 30–44 mL/min."
    },
    "atorvastatin": {
        "black_box_warning": "None, but FDA warning for statin-induced myopathy, rhabdomyolysis, and immune-mediated necrotizing myopathy.",
        "key_precautions": "Baseline liver function test (LFT) recommended. Discontinue if persistent transaminase elevations >3x ULN or unexplained severe muscle pain occurs.",
        "organ_thresholds": "Contraindicated in active decompensated liver disease."
    }
}


def check_drug_interactions(drugs: List[str]) -> Dict[str, Any]:
    """
    Screens a list of medications for potential adverse interactions and safety contraindications.
    """
    clean_drugs = [d.strip().lower() for d in drugs if d.strip()]
    if len(clean_drugs) == 0:
        return {"interactions_found": 0, "alerts": [], "status": "No medications provided."}

    matched_interactions = []
    
    # Check all pairs against DDI rules
    for rule in DDI_RULES:
        group_a, group_b = rule["drugs"]
        has_a = any(any(alias in drug for alias in group_a) for drug in clean_drugs)
        has_b = any(any(alias in drug for alias in group_b) for drug in clean_drugs)

        if has_a and has_b:
            matched_interactions.append({
                "severity": rule["severity"],
                "mechanism": rule["mechanism"],
                "clinical_risk": rule["clinical_risk"],
                "management": rule["management"]
            })

    # Screen individual drug safety profiles
    drug_warnings = []
    for drug in clean_drugs:
        for profile_name, profile_data in SINGLE_DRUG_PROFILES.items():
            if profile_name in drug:
                drug_warnings.append({
                    "drug": profile_name.title(),
                    "black_box_warning": profile_data["black_box_warning"],
                    "key_precautions": profile_data["key_precautions"],
                    "organ_thresholds": profile_data["organ_thresholds"]
                })

    return {
        "screened_medications": clean_drugs,
        "interactions_found": len(matched_interactions),
        "ddi_alerts": matched_interactions,
        "black_box_and_safety_profiles": drug_warnings,
        "status": "DDI Screening Completed"
    }


def screen_single_drug_safety(drug_name: str) -> Dict[str, Any]:
    """
    Retrieves safety profile and Black Box warnings for a single drug.
    """
    d_clean = drug_name.strip().lower()
    for name, data in SINGLE_DRUG_PROFILES.items():
        if name in d_clean:
            return {
                "drug": name.title(),
                "has_profile": True,
                **data
            }
    return {
        "drug": drug_name,
        "has_profile": False,
        "black_box_warning": "No specific Black Box profile indexed; review standard package insert and FDA label.",
        "key_precautions": "Standard clinical medication reconciliation and organ function monitoring advised.",
        "organ_thresholds": "Follow standard renal/hepatic dosing recommendations."
    }


@tool
def drug_interaction_tool(medications: List[str]) -> Dict[str, Any]:
    """
    Checks Drug-Drug Interactions (DDI), Black Box warnings, and organ clearance cutoffs for a list of drugs.
    Parameters:
      medications: list of drug names (e.g. ['Paxlovid', 'Atorvastatin', 'Lisinopril'])
    """
    return check_drug_interactions(medications)
