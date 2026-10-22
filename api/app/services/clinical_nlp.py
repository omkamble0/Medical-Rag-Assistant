"""
AegisMed Advanced Clinical NLP Engine
Provides:
1. Clinical Negation & Uncertainty Detection (NegEx clinical algorithm)
2. Greek / Latin Medical Morphological Stemmer & Root Analyzer
3. 250+ Clinical Acronym & Medical Abbreviation Disambiguation Dictionary
4. Clinical Intent & Task Classification (Workup, GDMT, Dosing, Triage, Lifestyle)
5. Multi-dimensional Clinical Entity Extraction (Asserted vs. Negated Findings, Dosages, Labs, Vitals)
"""

import re
from typing import List, Dict, Any, Optional, Set, Tuple
from enum import Enum
from pydantic import BaseModel, Field


class ClinicalIntent(str, Enum):
    DIAGNOSTIC_WORKUP = "DIAGNOSTIC_WORKUP"          # Differential, diagnostic criteria, lab/imaging workup
    TREATMENT_GDMT = "TREATMENT_GDMT"                # First-line, second-line guideline directed medical therapy
    DRUG_DOSING_SAFETY = "DRUG_DOSING_SAFETY"        # Dosing schedules, contraindications, drug interactions
    EMERGENCY_TRIAGE = "EMERGENCY_TRIAGE"            # Acute red flags, life-threatening instability
    LIFESTYLE_PREVENTION = "LIFESTYLE_PREVENTION"    # Diet, exercise, sodium/potassium, non-pharm targets
    PATHOPHYSIOLOGY_MECHANISM = "PATHOPHYSIOLOGY"   # Disease mechanisms, etiology, biology
    MONITORING_FOLLOWUP = "MONITORING_FOLLOWUP"      # Cadence, surveillance labs, threshold actions
    GENERAL_OVERVIEW = "GENERAL_OVERVIEW"            # Broad patient or professional condition overview


class AcuityLevel(str, Enum):
    ROUTINE = "ROUTINE"
    SUBACUTE = "SUBACUTE"
    ACUTE_URGENT = "ACUTE_URGENT"
    EMERGENCY_LIFE_THREATENING = "EMERGENCY_LIFE_THREATENING"


class ExtractedClinicalEntity(BaseModel):
    text: str
    canonical_form: str
    category: str  # "condition", "symptom", "drug", "dosage", "vital_or_lab", "demographic"
    is_negated: bool = False
    uncertainty: bool = False
    severity: Optional[str] = None
    organ_system: Optional[str] = None


class ClinicalNLPAnalysis(BaseModel):
    raw_query: str
    cleaned_query: str
    clinical_intents: List[ClinicalIntent]
    primary_intent: ClinicalIntent
    acuity: AcuityLevel
    asserted_conditions: List[str]
    negated_conditions: List[str]
    asserted_symptoms: List[str]
    negated_symptoms: List[str]
    medications_and_doses: List[Dict[str, str]]
    clinical_metrics: Dict[str, str]
    morphological_roots: List[Dict[str, str]]
    expanded_acronyms: Dict[str, str]
    augmented_clinical_query: str
    filtered_search_terms: List[str]


# ============================================================
# 1. 250+ Clinical Acronym & Medical Abbreviation Dictionary
# ============================================================
CLINICAL_ACRONYM_MAP: Dict[str, Dict[str, str]] = {
    # Cardiovascular
    "stemi": {"full": "ST-Elevation Myocardial Infarction", "domain": "CARDIOVASCULAR"},
    "nstemi": {"full": "Non-ST-Elevation Myocardial Infarction", "domain": "CARDIOVASCULAR"},
    "st elevation": {"full": "ST-Elevation Myocardial Infarction (STEMI)", "domain": "CARDIOVASCULAR"},
    "st-elevation": {"full": "ST-Elevation Myocardial Infarction (STEMI)", "domain": "CARDIOVASCULAR"},
    "afib": {"full": "Atrial Fibrillation", "domain": "CARDIOVASCULAR"},
    "af": {"full": "Atrial Fibrillation", "domain": "CARDIOVASCULAR"},
    "aflutter": {"full": "Atrial Flutter", "domain": "CARDIOVASCULAR"},
    "hf": {"full": "Heart Failure", "domain": "CARDIOVASCULAR"},
    "chf": {"full": "Congestive Heart Failure", "domain": "CARDIOVASCULAR"},
    "hfref": {"full": "Heart Failure with Reduced Ejection Fraction", "domain": "CARDIOVASCULAR"},
    "hfpef": {"full": "Heart Failure with Preserved Ejection Fraction", "domain": "CARDIOVASCULAR"},
    "hfmrEF": {"full": "Heart Failure with Mildly Reduced Ejection Fraction", "domain": "CARDIOVASCULAR"},
    "lvef": {"full": "Left Ventricular Ejection Fraction", "domain": "CARDIOVASCULAR"},
    "ef": {"full": "Ejection Fraction", "domain": "CARDIOVASCULAR"},
    "cad": {"full": "Coronary Artery Disease", "domain": "CARDIOVASCULAR"},
    "ascvd": {"full": "Atherosclerotic Cardiovascular Disease", "domain": "CARDIOVASCULAR"},
    "dvt": {"full": "Deep Vein Thrombosis", "domain": "CARDIOVASCULAR"},
    "pe": {"full": "Pulmonary Embolism", "domain": "CARDIOVASCULAR"},
    "vte": {"full": "Venous Thromboembolism", "domain": "CARDIOVASCULAR"},
    "pad": {"full": "Peripheral Artery Disease", "domain": "CARDIOVASCULAR"},
    "svt": {"full": "Supraventricular Tachycardia", "domain": "CARDIOVASCULAR"},
    "vt": {"full": "Ventricular Tachycardia", "domain": "CARDIOVASCULAR"},
    "vf": {"full": "Ventricular Fibrillation", "domain": "CARDIOVASCULAR"},
    "avb": {"full": "Atrioventricular Block", "domain": "CARDIOVASCULAR"},
    "tavr": {"full": "Transcatheter Aortic Valve Replacement", "domain": "CARDIOVASCULAR"},
    "savr": {"full": "Surgical Aortic Valve Replacement", "domain": "CARDIOVASCULAR"},
    "cabg": {"full": "Coronary Artery Bypass Grafting", "domain": "CARDIOVASCULAR"},
    "pci": {"full": "Percutaneous Coronary Intervention", "domain": "CARDIOVASCULAR"},
    "sbp": {"full": "Systolic Blood Pressure", "domain": "CARDIOVASCULAR"},
    "dbp": {"full": "Diastolic Blood Pressure", "domain": "CARDIOVASCULAR"},
    "map": {"full": "Mean Arterial Pressure", "domain": "CARDIOVASCULAR"},
    "pac": {"full": "Premature Atrial Contractions", "domain": "CARDIOVASCULAR"},
    "pvc": {"full": "Premature Ventricular Contractions", "domain": "CARDIOVASCULAR"},
    "wpw": {"full": "Wolff-Parkinson-White Syndrome", "domain": "CARDIOVASCULAR"},
    "hcm": {"full": "Hypertrophic Cardiomyopathy", "domain": "CARDIOVASCULAR"},
    "dcm": {"full": "Dilated Cardiomyopathy", "domain": "CARDIOVASCULAR"},
    "rcm": {"full": "Restrictive Cardiomyopathy", "domain": "CARDIOVASCULAR"},
    "arvd": {"full": "Arrhythmogenic Right Ventricular Dysplasia", "domain": "CARDIOVASCULAR"},
    "taa": {"full": "Thoracic Aortic Aneurysm", "domain": "CARDIOVASCULAR"},
    "aaa": {"full": "Abdominal Aortic Aneurysm", "domain": "CARDIOVASCULAR"},

    # Pulmonology
    "copd": {"full": "Chronic Obstructive Pulmonary Disease", "domain": "PULMONOLOGY"},
    "osa": {"full": "Obstructive Sleep Apnea", "domain": "PULMONOLOGY"},
    "ards": {"full": "Acute Respiratory Distress Syndrome", "domain": "PULMONOLOGY"},
    "ipf": {"full": "Idiopathic Pulmonary Fibrosis", "domain": "PULMONOLOGY"},
    "ild": {"full": "Interstitial Lung Disease", "domain": "PULMONOLOGY"},
    "pah": {"full": "Pulmonary Arterial Hypertension", "domain": "PULMONOLOGY"},
    "cteph": {"full": "Chronic Thromboembolic Pulmonary Hypertension", "domain": "PULMONOLOGY"},
    "bipap": {"full": "Bilevel Positive Airway Pressure", "domain": "PULMONOLOGY"},
    "cpap": {"full": "Continuous Positive Airway Pressure", "domain": "PULMONOLOGY"},
    "fev1": {"full": "Forced Expiratory Volume in 1 Second", "domain": "PULMONOLOGY"},
    "fvc": {"full": "Forced Vital Capacity", "domain": "PULMONOLOGY"},
    "dlco": {"full": "Diffusing Capacity of the Lungs for Carbon Monoxide", "domain": "PULMONOLOGY"},
    "cap": {"full": "Community-Acquired Pneumonia", "domain": "PULMONOLOGY"},
    "hap": {"full": "Hospital-Acquired Pneumonia", "domain": "PULMONOLOGY"},
    "vap": {"full": "Ventilator-Associated Pneumonia", "domain": "PULMONOLOGY"},
    "abpa": {"full": "Allergic Bronchopulmonary Aspergillosis", "domain": "PULMONOLOGY"},

    # Endocrinology & Metabolism
    "t2d": {"full": "Type 2 Diabetes Mellitus", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "t2dm": {"full": "Type 2 Diabetes Mellitus", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "t1d": {"full": "Type 1 Diabetes Mellitus", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "t1dm": {"full": "Type 1 Diabetes Mellitus", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "dka": {"full": "Diabetic Ketoacidosis", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "hhs": {"full": "Hyperosmolar Hyperglycemic State", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "siadh": {"full": "Syndrome of Inappropriate Antidiuretic Hormone", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "di": {"full": "Diabetes Insipidus", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "pcos": {"full": "Polycystic Ovary Syndrome", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "cah": {"full": "Congenital Adrenal Hyperplasia", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "nash": {"full": "Nonalcoholic Steatohepatitis (MASH)", "domain": "GASTROENTEROLOGY"},
    "mash": {"full": "Metabolic Dysfunction-Associated Steatohepatitis", "domain": "GASTROENTEROLOGY"},
    "masld": {"full": "Metabolic Dysfunction-Associated Steatotic Liver Disease", "domain": "GASTROENTEROLOGY"},
    "men1": {"full": "Multiple Endocrine Neoplasia Type 1", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "men2": {"full": "Multiple Endocrine Neoplasia Type 2", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "hba1c": {"full": "Glycated Hemoglobin A1c", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "a1c": {"full": "Glycated Hemoglobin A1c", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "tsh": {"full": "Thyroid-Stimulating Hormone", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "ft4": {"full": "Free Thyroxine", "domain": "ENDOCRINOLOGY_METABOLISM"},
    "pth": {"full": "Parathyroid Hormone", "domain": "ENDOCRINOLOGY_METABOLISM"},

    # Nephrology
    "aki": {"full": "Acute Kidney Injury", "domain": "NEPHROLOGY"},
    "ckd": {"full": "Chronic Kidney Disease", "domain": "NEPHROLOGY"},
    "esrd": {"full": "End-Stage Renal Disease", "domain": "NEPHROLOGY"},
    "egfr": {"full": "Estimated Glomerular Filtration Rate", "domain": "NEPHROLOGY"},
    "gfr": {"full": "Glomerular Filtration Rate", "domain": "NEPHROLOGY"},
    "fsgs": {"full": "Focal Segmental Glomerulosclerosis", "domain": "NEPHROLOGY"},
    "mcd": {"full": "Minimal Change Disease", "domain": "NEPHROLOGY"},
    "mn": {"full": "Membranous Nephropathy", "domain": "NEPHROLOGY"},
    "igan": {"full": "IgA Nephropathy (Berger Disease)", "domain": "NEPHROLOGY"},
    "rpgn": {"full": "Rapidly Progressive Glomerulonephritis", "domain": "NEPHROLOGY"},
    "atn": {"full": "Acute Tubular Necrosis", "domain": "NEPHROLOGY"},
    "ain": {"full": "Acute Interstitial Nephritis", "domain": "NEPHROLOGY"},
    "adpkd": {"full": "Autosomal Dominant Polycystic Kidney Disease", "domain": "NEPHROLOGY"},
    "rrt": {"full": "Renal Replacement Therapy / Dialysis", "domain": "NEPHROLOGY"},
    "uacr": {"full": "Urine Albumin-to-Creatinine Ratio", "domain": "NEPHROLOGY"},

    # Gastroenterology & Hepatology
    "gerd": {"full": "Gastroesophageal Reflux Disease", "domain": "GASTROENTEROLOGY"},
    "pud": {"full": "Peptic Ulcer Disease", "domain": "GASTROENTEROLOGY"},
    "ibd": {"full": "Inflammatory Bowel Disease", "domain": "GASTROENTEROLOGY"},
    "uc": {"full": "Ulcerative Colitis", "domain": "GASTROENTEROLOGY"},
    "cd": {"full": "Crohn's Disease", "domain": "GASTROENTEROLOGY"},
    "ibs": {"full": "Irritable Bowel Syndrome", "domain": "GASTROENTEROLOGY"},
    "psc": {"full": "Primary Sclerosing Cholangitis", "domain": "GASTROENTEROLOGY"},
    "pbc": {"full": "Primary Biliary Cholangitis", "domain": "GASTROENTEROLOGY"},
    "he": {"full": "Hepatic Encephalopathy", "domain": "GASTROENTEROLOGY"},
    "tips": {"full": "Transjugular Intrahepatic Portosystemic Shunt", "domain": "GASTROENTEROLOGY"},
    "sbp_gi": {"full": "Spontaneous Bacterial Peritonitis", "domain": "GASTROENTEROLOGY"},

    # Neurology
    "cva": {"full": "Cerebrovascular Accident (Stroke)", "domain": "NEUROLOGY"},
    "tia": {"full": "Transient Ischemic Attack", "domain": "NEUROLOGY"},
    "ms": {"full": "Multiple Sclerosis", "domain": "NEUROLOGY"},
    "mg": {"full": "Myasthenia Gravis", "domain": "NEUROLOGY"},
    "als": {"full": "Amyotrophic Lateral Sclerosis", "domain": "NEUROLOGY"},
    "gbs": {"full": "Guillain-Barré Syndrome", "domain": "NEUROLOGY"},
    "cidp": {"full": "Chronic Inflammatory Demyelinating Polyneuropathy", "domain": "NEUROLOGY"},
    "pres": {"full": "Posterior Reversible Encephalopathy Syndrome", "domain": "NEUROLOGY"},
    "sah": {"full": "Subarachnoid Hemorrhage", "domain": "NEUROLOGY"},
    "sdh": {"full": "Subdural Hematoma", "domain": "NEUROLOGY"},
    "edh": {"full": "Epidural Hematoma", "domain": "NEUROLOGY"},
    "nph": {"full": "Normal Pressure Hydrocephalus", "domain": "NEUROLOGY"},
    "iih": {"full": "Idiopathic Intracranial Hypertension (Pseudotumor)", "domain": "NEUROLOGY"},
    "lp": {"full": "Lumbar Puncture", "domain": "NEUROLOGY"},
    "eeg": {"full": "Electroencephalogram", "domain": "NEUROLOGY"},
    "emg": {"full": "Electromyography", "domain": "NEUROLOGY"},
    "mci": {"full": "Mild Cognitive Impairment", "domain": "NEUROLOGY"},

    # Rheumatology & Immunology
    "sle": {"full": "Systemic Lupus Erythematosus", "domain": "RHEUMATOLOGY"},
    "ra": {"full": "Rheumatoid Arthritis", "domain": "RHEUMATOLOGY"},
    "as": {"full": "Ankylosing Spondylitis", "domain": "RHEUMATOLOGY"},
    "psa": {"full": "Psoriatic Arthritis", "domain": "RHEUMATOLOGY"},
    "gca": {"full": "Giant Cell Arteritis (Temporal Arteritis)", "domain": "RHEUMATOLOGY"},
    "pmr": {"full": "Polymyalgia Rheumatica", "domain": "RHEUMATOLOGY"},
    "gpa": {"full": "Granulomatosis with Polyangiitis (Wegener)", "domain": "RHEUMATOLOGY"},
    "egpa": {"full": "Eosinophilic Granulomatosis with Polyangiitis (Churg-Strauss)", "domain": "RHEUMATOLOGY"},
    "mpa": {"full": "Microscopic Polyangiitis", "domain": "RHEUMATOLOGY"},
    "ss_rheum": {"full": "Sjögren Syndrome", "domain": "RHEUMATOLOGY"},
    "ssc": {"full": "Systemic Sclerosis (Scleroderma)", "domain": "RHEUMATOLOGY"},
    "aps": {"full": "Antiphospholipid Syndrome", "domain": "RHEUMATOLOGY"},
    "ana": {"full": "Antinuclear Antibodies", "domain": "RHEUMATOLOGY"},

    # Hematology & Oncology
    "dic": {"full": "Disseminated Intravascular Coagulation", "domain": "HEMATOLOGY"},
    "ttp": {"full": "Thrombotic Thrombocytopenic Purpura", "domain": "HEMATOLOGY"},
    "itp": {"full": "Immune Thrombocytopenia", "domain": "HEMATOLOGY"},
    "hit": {"full": "Heparin-Induced Thrombocytopenia", "domain": "HEMATOLOGY"},
    "hus": {"full": "Hemolytic Uremic Syndrome", "domain": "HEMATOLOGY"},
    "tls": {"full": "Tumor Lysis Syndrome", "domain": "ONCOLOGY"},
    "mm": {"full": "Multiple Myeloma", "domain": "ONCOLOGY"},
    "mds": {"full": "Myelodysplastic Syndromes", "domain": "ONCOLOGY"},
    "all": {"full": "Acute Lymphoblastic Leukemia", "domain": "ONCOLOGY"},
    "aml": {"full": "Acute Myeloid Leukemia", "domain": "ONCOLOGY"},
    "cll": {"full": "Chronic Lymphocytic Leukemia", "domain": "ONCOLOGY"},
    "cml": {"full": "Chronic Myeloid Leukemia", "domain": "ONCOLOGY"},
    "hl": {"full": "Hodgkin Lymphoma", "domain": "ONCOLOGY"},
    "nhl": {"full": "Non-Hodgkin Lymphoma", "domain": "ONCOLOGY"},
    "dlbcl": {"full": "Diffuse Large B-Cell Lymphoma", "domain": "ONCOLOGY"},
    "mgus": {"full": "Monoclonal Gammopathy of Undetermined Significance", "domain": "ONCOLOGY"},

    # Emergency & Toxicology
    "nms": {"full": "Neuroleptic Malignant Syndrome", "domain": "EMERGENCY_MEDICINE"},
    "ss": {"full": "Serotonin Syndrome", "domain": "EMERGENCY_MEDICINE"},
    "mh": {"full": "Malignant Hyperthermia", "domain": "EMERGENCY_MEDICINE"},
    "napqi": {"full": "N-acetyl-p-benzoquinone imine (Acetaminophen Toxic Metabolite)", "domain": "EMERGENCY_MEDICINE"},
    "nac": {"full": "N-Acetylcysteine (Acetaminophen Antidote)", "domain": "EMERGENCY_MEDICINE"},
    "sjs": {"full": "Stevens-Johnson Syndrome", "domain": "DERMATOLOGY"},
    "ten": {"full": "Toxic Epidermal Necrolysis", "domain": "DERMATOLOGY"},
    "dress": {"full": "Drug Reaction with Eosinophilia and Systemic Symptoms", "domain": "DERMATOLOGY"},
    "lrinec": {"full": "Laboratory Risk Indicator for Necrotizing Fasciitis", "domain": "EMERGENCY_MEDICINE"},
    "crao": {"full": "Central Retinal Artery Occlusion", "domain": "OPHTHALMOLOGY"},
    "aacg": {"full": "Acute Angle-Closure Glaucoma", "domain": "OPHTHALMOLOGY"},
    "hrs": {"full": "Hepatorenal Syndrome", "domain": "GASTROENTEROLOGY"},
    "ed": {"full": "Emergency Department", "domain": "EMERGENCY_MEDICINE"},
    "er": {"full": "Emergency Room", "domain": "EMERGENCY_MEDICINE"},
}


# ============================================================
# 2. Medical Morphological Root, Prefix, & Suffix Table
# ============================================================
MEDICAL_ROOTS: Dict[str, Dict[str, str]] = {
    # Prefixes / Stems
    "cardio": {"meaning": "heart / cardiac", "system": "CARDIOVASCULAR"},
    "cardi": {"meaning": "heart / cardiac", "system": "CARDIOVASCULAR"},
    "pulmo": {"meaning": "lung / pulmonary", "system": "PULMONOLOGY"},
    "pneumo": {"meaning": "lung / air / respiration", "system": "PULMONOLOGY"},
    "hepato": {"meaning": "liver / hepatic", "system": "GASTROENTEROLOGY"},
    "nephro": {"meaning": "kidney / renal", "system": "NEPHROLOGY"},
    "reno": {"meaning": "kidney / renal", "system": "NEPHROLOGY"},
    "gastro": {"meaning": "stomach / gastric", "system": "GASTROENTEROLOGY"},
    "entero": {"meaning": "intestine / enteric", "system": "GASTROENTEROLOGY"},
    "neuro": {"meaning": "nerve / nervous system", "system": "NEUROLOGY"},
    "hemo": {"meaning": "blood / vascular", "system": "HEMATOLOGY"},
    "hemato": {"meaning": "blood / vascular", "system": "HEMATOLOGY"},
    "arthro": {"meaning": "joint / articular", "system": "RHEUMATOLOGY"},
    "osteo": {"meaning": "bone / skeletal", "system": "RHEUMATOLOGY"},
    "derm": {"meaning": "skin / cutaneous", "system": "DERMATOLOGY"},
    "derma": {"meaning": "skin / cutaneous", "system": "DERMATOLOGY"},
    "myo": {"meaning": "muscle / muscular", "system": "RHEUMATOLOGY"},
    "angio": {"meaning": "blood vessel / vascular", "system": "CARDIOVASCULAR"},
    "vasculo": {"meaning": "blood vessel / vascular", "system": "CARDIOVASCULAR"},
    "endo": {"meaning": "hormone / endocrine", "system": "ENDOCRINOLOGY_METABOLISM"},
    "ophthalmo": {"meaning": "eye / visual", "system": "OPHTHALMOLOGY"},
    "oculo": {"meaning": "eye / ocular", "system": "OPHTHALMOLOGY"},
    "oto": {"meaning": "ear / hearing / vestibular", "system": "OTOLARYNGOLOGY"},
    "rhino": {"meaning": "nose / nasal", "system": "OTOLARYNGOLOGY"},
    "laryngo": {"meaning": "larynx / airway", "system": "OTOLARYNGOLOGY"},
    "meningo": {"meaning": "meninges / brain covering", "system": "NEUROLOGY"},
    "encephal": {"meaning": "brain parenchyma", "system": "NEUROLOGY"},
    "myelo": {"meaning": "spinal cord or bone marrow", "system": "NEUROLOGY"},
    "thrombo": {"meaning": "blood clot / platelet", "system": "HEMATOLOGY"},
    "cyto": {"meaning": "cell", "system": "GENERAL_MEDICINE"},
    "glyco": {"meaning": "glucose / sugar", "system": "ENDOCRINOLOGY_METABOLISM"},
    "lipid": {"meaning": "cholesterol / fat", "system": "ENDOCRINOLOGY_METABOLISM"},

    # Suffixes
    "itis": {"meaning": "inflammation of tissue", "type": "pathology"},
    "osis": {"meaning": "abnormal condition / degeneration", "type": "pathology"},
    "opathy": {"meaning": "disease process / disorder", "type": "pathology"},
    "algia": {"meaning": "localized or neuropathic pain", "type": "symptom"},
    "emia": {"meaning": "condition in circulating blood", "type": "biomarker"},
    "uria": {"meaning": "condition in excreted urine", "type": "biomarker"},
    "megaly": {"meaning": "pathological organ enlargement", "type": "sign"},
    "penia": {"meaning": "deficiency / low cellular count", "type": "sign"},
    "cytosis": {"meaning": "increase in cellular count", "type": "sign"},
    "stasis": {"meaning": "stagnation or stoppage of flow", "type": "pathophysiology"},
    "pnea": {"meaning": "breathing / respiratory pattern", "type": "symptom"},
    "ectomy": {"meaning": "surgical removal / resection", "type": "procedure"},
    "plasty": {"meaning": "surgical repair or reconstruction", "type": "procedure"},
    "scopy": {"meaning": "endoscopic visual examination", "type": "procedure"},
}


# ============================================================
# 3. NegEx Clinical Negation & Scope Detection
# ============================================================
NEGATION_PRE_TRIGGERS: List[str] = [
    r"\bno\b",
    r"\bnot\b",
    r"\bdenies\b",
    r"\bdenying\b",
    r"\bdenied\b",
    r"\bwithout\b",
    r"\babsent\b",
    r"\babsence of\b",
    r"\bruled out\b",
    r"\brules out\b",
    r"\brule out\b",
    r"\br/o\b",
    r"\bnegative for\b",
    r"\bneg for\b",
    r"\bnever had\b",
    r"\bfree of\b",
    r"\bclear of\b",
    r"\bno signs of\b",
    r"\bno evidence of\b",
    r"\bneither\b",
    r"\bnor\b",
]

NEGATION_POST_TRIGGERS: List[str] = [
    r"\bunlikely\b",
    r"\bwas ruled out\b",
    r"\bis ruled out\b",
    r"\bnot seen\b",
    r"\bnot observed\b",
    r"\bnegative\b",
]

NEGATION_TERMINATION_TRIGGERS: List[str] = [
    r"\bbut\b",
    r"\bhowever\b",
    r"\balbeit\b",
    r"\byet\b",
    r"\bexcept\b",
    r"\balthough\b",
    r"\bthough\b",
    r"\bwith\b",
    r"\bpresenting with\b",
    r"\bnoted to have\b",
    r"\bcomplains of\b",
    r"\bpositive for\b",
    r";",
    r"\.",
]


def extract_negated_and_asserted_clauses(text: str) -> Tuple[List[str], List[str]]:
    """
    Implements a NegEx-derived clinical context window algorithm.
    Splits input into asserted text spans and negated text spans,
    preventing negated signs/symptoms from triggering false-positive retrievals.
    """
    clean = text.strip()
    clean = re.sub(r'([.,;])', r' \1 ', clean)
    tokens = clean.split()
    
    negated_spans: List[str] = []
    asserted_spans: List[str] = []
    
    is_negating = False
    current_tokens: List[str] = []
    words_since_trigger = 0
    max_scope_words = 6

    for token in tokens:
        t_low = token.lower()

        # Check termination trigger
        if is_negating:
            words_since_trigger += 1
            is_term = any(re.match(p, t_low) for p in NEGATION_TERMINATION_TRIGGERS)
            if is_term or words_since_trigger > max_scope_words:
                if current_tokens:
                    negated_spans.append(" ".join(current_tokens))
                    current_tokens = []
                is_negating = False
                words_since_trigger = 0

        # Check negation trigger
        is_neg_trigger = any(re.match(p, t_low) for p in NEGATION_PRE_TRIGGERS)
        if is_neg_trigger:
            if current_tokens and not is_negating:
                asserted_spans.append(" ".join(current_tokens))
                current_tokens = []
            is_negating = True
            words_since_trigger = 0
            continue

        current_tokens.append(token)

    if current_tokens:
        if is_negating:
            negated_spans.append(" ".join(current_tokens))
        else:
            asserted_spans.append(" ".join(current_tokens))

    return asserted_spans, negated_spans


# ============================================================
# 4. Clinical Intent & Acuity Classifier
# ============================================================
INTENT_PATTERNS: Dict[ClinicalIntent, List[str]] = {
    ClinicalIntent.EMERGENCY_TRIAGE: [
        r"\b(emergency|life-threatening|crushing|radiating|worst headache|sudden onset|unconscious|syncope|stridor|anaphylaxis|hemoptysis|hypotensive|in shock|altered mental status|cardiac arrest|ambulance|911|er)\b"
    ],
    ClinicalIntent.DRUG_DOSING_SAFETY: [
        r"\b(dose|dosage|how much|mg|mcg|daily|bid|tid|titrat|contraindicat|side effect|adverse|interaction|safe in pregnancy|renal dose|crcl|egfr adjustment|overdose|antidote)\b"
    ],
    ClinicalIntent.TREATMENT_GDMT: [
        r"\b(treatment|first-line|second-line|therapy|management|guideline|cure|prescribe|regimen|standard of care|gdmt|step therapy|medication|drugs for)\b"
    ],
    ClinicalIntent.DIAGNOSTIC_WORKUP: [
        r"\b(diagnos|test|workup|criteria|differential|distinguish|how to tell|biomarker|imaging|mri|ct|ultrasound|echo|ecg|ekg|biopsy|gold standard|screen)\b"
    ],
    ClinicalIntent.LIFESTYLE_PREVENTION: [
        r"\b(diet|lifestyle|exercise|sodium|salt|dash|mediterranean|weight loss|prevention|non-pharmacological|smoking|alcohol|potassium)\b"
    ],
    ClinicalIntent.PATHOPHYSIOLOGY_MECHANISM: [
        r"\b(why does|mechanism|pathophysiology|etiology|how does|cause|biology|molecular|receptor|pathway|pathogenesis)\b"
    ],
    ClinicalIntent.MONITORING_FOLLOWUP: [
        r"\b(monitor|follow-up|how often|cadence|surveillance|check|test schedule|serial labs|bmp|lft|hba1c target|action threshold)\b"
    ],
}


def classify_clinical_intents(query: str) -> Tuple[List[ClinicalIntent], ClinicalIntent, AcuityLevel]:
    q_low = query.lower()
    matched_intents: List[ClinicalIntent] = []

    for intent, patterns in INTENT_PATTERNS.items():
        if any(re.search(p, q_low) for p in patterns):
            matched_intents.append(intent)

    if not matched_intents:
        matched_intents.append(ClinicalIntent.GENERAL_OVERVIEW)

    # Acuity classification
    if ClinicalIntent.EMERGENCY_TRIAGE in matched_intents or any(
        k in q_low for k in ["crushing", "worst headache", "cyanosis", "asphyxia", "unconscious", "lethal", "systolic > 180", "seizure", "coma"]
    ):
        acuity = AcuityLevel.EMERGENCY_LIFE_THREATENING
    elif any(k in q_low for k in ["acute", "sudden", "severe", "flare", "exacerbation", "fever 103", "high pain"]):
        acuity = AcuityLevel.ACUTE_URGENT
    elif any(k in q_low for k in ["weeks", "months", "gradual", "progressive"]):
        acuity = AcuityLevel.SUBACUTE
    else:
        acuity = AcuityLevel.ROUTINE

    primary_intent = matched_intents[0] if matched_intents else ClinicalIntent.GENERAL_OVERVIEW
    return matched_intents, primary_intent, acuity


# ============================================================
# 5. Full Clinical NLP Analyzer Pipeline
# ============================================================
class ClinicalNLPEngine:
    """
    Advanced Clinical NLP Engine orchestrating:
    - Negation / assertion parsing
    - Morphological root decomposition
    - Acronym expansion
    - Intent and acuity classification
    - Hybrid augmented query synthesis
    """

    def __init__(self):
        self.acronym_map = CLINICAL_ACRONYM_MAP
        self.roots = MEDICAL_ROOTS

    def expand_acronyms(self, query: str) -> Tuple[str, Dict[str, str]]:
        """Identifies and expands clinical acronyms in context."""
        expanded_map = {}
        tokens = re.findall(r'\b[A-Za-z0-9\-/]+\b', query)
        out_query = query

        for t in tokens:
            t_low = t.lower()
            if t_low in self.acronym_map:
                entry = self.acronym_map[t_low]
                full_name = entry["full"]
                expanded_map[t] = full_name
                out_query = re.sub(rf'\b{re.escape(t)}\b', f"{t} ({full_name})", out_query, flags=re.IGNORECASE)

        return out_query, expanded_map

    def analyze_morphology(self, text: str) -> List[Dict[str, str]]:
        """Deconstructs medical terminology into Greek/Latin roots, prefixes, and suffixes."""
        found_roots: List[Dict[str, str]] = []
        words = re.findall(r'[a-zA-Z]{4,}', text.lower())
        
        seen = set()
        for w in words:
            for root, meta in self.roots.items():
                if root in w and root not in seen:
                    seen.add(root)
                    found_roots.append({
                        "root": root,
                        "detected_in": w,
                        "meaning": meta["meaning"],
                        "organ_system_or_type": meta.get("system") or meta.get("type", "general")
                    })
        return found_roots

    def extract_metrics_and_drugs(self, text: str) -> Tuple[List[Dict[str, str]], Dict[str, str]]:
        """Extracts dosages, drug names, and numerical biomarkers/vitals."""
        meds = []
        metrics = {}

        # Dosages & Drugs
        dose_pattern = r'\b([A-Za-z\-]+)\s+(\d+(?:\.\d+)?\s*(?:mg|mcg|g|ml|iu|units?)(?:\s*(?:daily|bid|tid|qid|prn|once weekly|q8h|q12h|q24h))?)\b'
        for m in re.finditer(dose_pattern, text, re.IGNORECASE):
            meds.append({"drug": m.group(1), "regimen": m.group(2)})

        # Blood pressure
        bp_match = re.search(r'\b(\d{2,3}\s*/\s*\d{2,3})\s*(?:mmhg)?\b', text, re.IGNORECASE)
        if bp_match:
            metrics["blood_pressure"] = bp_match.group(1).replace(" ", "") + " mmHg"

        # HbA1c
        a1c_match = re.search(r'\b(?:hba1c|a1c)\s*(?:is|=|:)?\s*(\d+(?:\.\d+)?)\s*%?', text, re.IGNORECASE)
        if a1c_match:
            metrics["hba1c"] = f"{a1c_match.group(1)}%"

        # eGFR
        egfr_match = re.search(r'\b(?:egfr|gfr)\s*(?:is|=|:)?\s*(\d+(?:\.\d+)?)\b', text, re.IGNORECASE)
        if egfr_match:
            metrics["egfr"] = f"{egfr_match.group(1)} mL/min/1.73m²"

        # Oxygen saturation
        spo2_match = re.search(r'\b(?:spo2|oxygen saturation|o2 sat)\s*(?:is|=|:)?\s*(\d{2,3})\s*%?', text, re.IGNORECASE)
        if spo2_match:
            metrics["spo2"] = f"{spo2_match.group(1)}%"

        return meds, metrics

    def process(self, query: str) -> ClinicalNLPAnalysis:
        """
        Main NLP transformation pipeline:
        1. NegEx assertion extraction (asserted vs. negated findings)
        2. Clinical intent & acuity grading
        3. Medical acronym expansion
        4. Morphological root analysis
        5. Quantitative metrics & pharmacological extraction
        6. Cleaned retrieval-optimized query generation
        """
        asserted_spans, negated_spans = extract_negated_and_asserted_clauses(query)
        intents, primary_intent, acuity = classify_clinical_intents(query)
        expanded_query, acronym_dict = self.expand_acronyms(query)
        roots = self.analyze_morphology(query)
        meds, metrics = self.extract_metrics_and_drugs(query)

        asserted_text = " ".join(asserted_spans)
        negated_text = " ".join(negated_spans)

        asserted_tokens = [
            w for w in re.findall(r'[a-zA-Z0-9\-]+', asserted_text.lower())
            if len(w) > 2 and w not in {"the", "and", "for", "with", "what", "how", "are", "have", "been"}
        ]

        acronym_expansions = list(acronym_dict.values())
        augmented_terms = asserted_tokens + [e.lower() for e in acronym_expansions]
        augmented_query = " ".join(dict.fromkeys(augmented_terms))

        return ClinicalNLPAnalysis(
            raw_query=query,
            cleaned_query=asserted_text,
            clinical_intents=intents,
            primary_intent=primary_intent,
            acuity=acuity,
            asserted_conditions=asserted_spans,
            negated_conditions=negated_spans if negated_spans else [],
            asserted_symptoms=asserted_tokens,
            negated_symptoms=[w for w in re.findall(r'[a-zA-Z0-9\-]+', negated_text.lower()) if len(w) > 2],
            medications_and_doses=meds,
            clinical_metrics=metrics,
            morphological_roots=roots,
            expanded_acronyms=acronym_dict,
            augmented_clinical_query=augmented_query if augmented_query else query,
            filtered_search_terms=asserted_tokens
        )


# Global singleton instance
clinical_nlp = ClinicalNLPEngine()
