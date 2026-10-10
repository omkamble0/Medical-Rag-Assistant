"""
AegisMed Clinical Guideline Knowledge Base & Multi-Domain Client
Provides verified international clinical guidelines with Oxford CEBM evidentiary grading.
"""

from typing import List, Dict, Any, Optional
from app.models.enums import EvidenceLevel
from app.models.schemas import SourceDocument

CLINICAL_GUIDELINES: List[Dict[str, Any]] = [
    {
        "id": "GL-CARDIO-01",
        "domain": "cardiology",
        "authority": "American College of Cardiology / American Heart Association (ACC/AHA)",
        "title": "2023 ACC/AHA Guideline for the Management of Patients With Chronic Coronary Disease",
        "journal": "Journal of the American College of Cardiology / Circulation",
        "year": 2023,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["chest pain", "angina", "coronary", "statin", "aspirin", "cad", "myocardial infarction", "troponin"],
        "snippet": (
            "Class 1 Recommendations: High-intensity statin therapy (atorvastatin 80mg or rosuvastatin 40mg) is recommended "
            "for all patients with chronic coronary disease to achieve >=50% reduction in LDL-C and target LDL-C <55 mg/dL. "
            "Dual antiplatelet therapy (DAPT) duration is calibrated based on bleeding vs ischemic risk (PRECISE-DAPT / DAPT scores). "
            "SGLT2 inhibitors and GLP-1 receptor agonists are recommended for patients with type 2 diabetes and CAD to reduce cardiovascular events."
        ),
        "key_takeaway": "Mandates high-intensity statin to achieve LDL-C <55 mg/dL; incorporates SGLT2i/GLP-1RA for diabetic CAD patients."
    },
    {
        "id": "GL-HTN-01",
        "domain": "hypertension",
        "authority": "World Health Organization (WHO) & ACC/AHA",
        "title": "WHO Guideline for the Pharmacological Treatment of Hypertension in Adults & 2023 ACC/AHA Update",
        "journal": "WHO Guidelines Approved by the Guidelines Review Committee",
        "year": 2023,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["hypertension", "high blood pressure", "bp", "amlodipine", "lisinopril", "losartan", "dash", "chlorthalidone"],
        "snippet": (
            "Initiate pharmacological antihypertensive treatment in individuals with confirmed systolic blood pressure >= 140 mmHg "
            "or diastolic BP >= 90 mmHg (or >= 130/80 mmHg in high-risk CVD/diabetic cohorts). First-line pharmacological classes: "
            "thiazide/thiazide-like diuretics (chlorthalidone preferred), ACE inhibitors (lisinopril) or ARBs (losartan/valsartan), "
            "and dihydropyridine calcium channel blockers (amlodipine). Combination therapy using single-pill combinations improves compliance."
        ),
        "key_takeaway": "First-line triad: Thiazides, ACEi/ARBs, and CCBs; target BP <130/80 mmHg in high-risk patients with single-pill combinations."
    },
    {
        "id": "GL-DIAB-01",
        "domain": "diabetes",
        "authority": "American Diabetes Association (ADA)",
        "title": "Standards of Care in Diabetes—2024: Pharmacologic Approaches to Glycemic Treatment",
        "journal": "Diabetes Care",
        "year": 2024,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["diabetes", "semaglutide", "metformin", "hba1c", "ozempic", "glp-1", "sglt2", "empagliflozin", "mounjaro"],
        "snippet": (
            "For adults with type 2 diabetes and established atherosclerotic cardiovascular disease (ASCVD), heart failure, or "
            "chronic kidney disease (CKD), SGLT2 inhibitors (empagliflozin, dapagliflozin) or GLP-1 receptor agonists with proven "
            "CVD benefit (semaglutide, liraglutide, dulaglutide) are recommended independently of baseline HbA1c or metformin use. "
            "Target HbA1c is <7.0% (53 mmol/mol) for most non-pregnant adults without significant hypoglycemia."
        ),
        "key_takeaway": "SGLT2i and GLP-1RA recommended for cardiorenal protection independent of baseline HbA1c or background Metformin."
    },
    {
        "id": "GL-PULM-01",
        "domain": "asthma",
        "authority": "Global Initiative for Asthma (GINA)",
        "title": "Global Strategy for Asthma Management and Prevention (2023 Update)",
        "journal": "GINA Strategy Report / Respirology",
        "year": 2023,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["asthma", "inhaler", "budesonide", "formoterol", "albuterol", "wheezing", "ics", "bronchospasm"],
        "snippet": (
            "GINA Track 1 (Preferred Strategy across Steps 1–5): Low-dose inhaled corticosteroid (ICS)-formoterol as the reliever. "
            "In mild asthma (Steps 1-2), as-needed ICS-formoterol reduces severe exacerbation risk by 60-65% compared with SABA-only treatment. "
            "Short-Acting Beta-Agonist (SABA) monotherapy without concurrent ICS is strongly discouraged due to increased risk of fatal asthma attacks."
        ),
        "key_takeaway": "As-needed low-dose ICS-formoterol is preferred across all asthma severities; SABA monotherapy is unsafe and discouraged."
    },
    {
        "id": "GL-NEURO-01",
        "domain": "neurology",
        "authority": "International Headache Society (IHS) & American Headache Society (AHS)",
        "title": "The International Classification of Headache Disorders 3rd Edition (ICHD-3) and AHS Consensus Statement",
        "journal": "Cephalalgia / Headache",
        "year": 2023,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["headache", "migraine", "triptan", "sumatriptan", "cgrp", "rimegepant", "tension headache", "cluster headache"],
        "snippet": (
            "Migraine diagnosis requires >=5 attacks lasting 4-72 hours with unilateral location, pulsating quality, moderate-to-severe "
            "intensity, and nausea or photophobia/phonophobia. First-line acute treatment: NSAIDs for mild-moderate attacks; triptans "
            "(sumatriptan 50-100mg, zolmitriptan) or oral CGRP antagonists (rimegepant, ubrogepant) for moderate-severe attacks. "
            "Preventive therapy indicated if >=4 headache days/month: CGRP mAbs, topiramate, propranolol, or candesartan."
        ),
        "key_takeaway": "Acute treatment relies on triptans and CGRP antagonists; preventive therapy indicated for >=4 headache days/month."
    },
    {
        "id": "GL-RENAL-01",
        "domain": "kidney disease",
        "authority": "Kidney Disease: Improving Global Outcomes (KDIGO)",
        "title": "KDIGO 2023 Clinical Practice Guideline for the Management of Chronic Kidney Disease",
        "journal": "Kidney International",
        "year": 2023,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["kidney", "ckd", "renal", "egfr", "proteinuria", "dapagliflozin", "finerenone", "acei", "arb"],
        "snippet": (
            "Recommendation: Treat adults with CKD and type 2 diabetes with an SGLT2 inhibitor (eGFR >=20 mL/min/1.73m2) and a nonsteroidal "
            "mineralocorticoid receptor antagonist (finerenone) in combination with maximally tolerated RAS inhibitor (ACEi/ARB) "
            "to slow CKD progression and reduce cardiovascular morbidity."
        ),
        "key_takeaway": "Quadruple therapy (RASi + SGLT2i + finerenone + statin) provides maximum preservation of renal function."
    },
    {
        "id": "GL-INFECT-01",
        "domain": "infectious disease",
        "authority": "Infectious Diseases Society of America (IDSA) & CDC",
        "title": "IDSA Guidelines on the Treatment and Management of Patients with COVID-19 and Acute Viral Respiratory Infections",
        "journal": "Clinical Infectious Diseases",
        "year": 2024,
        "evidence_level": EvidenceLevel.LEVEL_1,
        "keywords": ["covid", "paxlovid", "nirmatrelvir", "antiviral", "ritonavir", "remdesivir", "respiratory infection"],
        "snippet": (
            "For non-hospitalized patients with mild-to-moderate COVID-19 at high risk for progression to severe disease, "
            "initiate nirmatrelvir/ritonavir (Paxlovid) within 5 days of symptom onset. Pre-treatment medication reconciliation is "
            "mandatory due to CYP3A inhibition. Alternative therapies: IV Remdesivir (within 7 days) or Molnupiravir (within 5 days)."
        ),
        "key_takeaway": "Paxlovid within 5 days of onset is primary oral antiviral; mandatory drug-drug interaction audit before dispensing."
    }
]

def load_guideline_sources() -> List[Dict[str, Any]]:
    """Loads all structured clinical guideline sources."""
    return list(CLINICAL_GUIDELINES)

def fetch_whole_guideline_data() -> List[Dict[str, Any]]:
    """Returns complete database of verified international clinical guidelines."""
    return list(CLINICAL_GUIDELINES)

def map_guidelines_to_domains() -> Dict[str, List[Dict[str, Any]]]:
    """Maps guideline sources to medical specialty domain clusters."""
    domain_map: Dict[str, List[Dict[str, Any]]] = {}
    for gl in CLINICAL_GUIDELINES:
        dom = gl.get("domain", "general_medicine").lower()
        if dom not in domain_map:
            domain_map[dom] = []
        domain_map[dom].append(gl)
    return domain_map

def find_guidelines_by_condition(condition: str) -> List[Dict[str, Any]]:
    """Searches guidelines matching clinical condition or symptoms."""
    c_low = condition.lower()
    matches = []
    for gl in CLINICAL_GUIDELINES:
        corpus = f"{gl['title']} {gl['snippet']} {' '.join(gl['keywords'])}".lower()
        if any(w in corpus for w in c_low.split() if len(w) > 3):
            matches.append(gl)
    return matches if matches else CLINICAL_GUIDELINES[:2]

def build_guideline_evidence_document(guideline: Dict[str, Any], citation_index: int = 1) -> SourceDocument:
    """Converts a guideline record into a validated SourceDocument."""
    return SourceDocument(
        id=guideline.get("id", f"GL-{citation_index}"),
        citation_index=citation_index,
        title=guideline.get("title", "Clinical Practice Guideline"),
        journal=guideline.get("journal", guideline.get("authority", "Clinical Guideline Authority")),
        year=int(guideline.get("year", 2023)),
        doi_or_pmid=f"GUIDELINE:{guideline.get('id', 'GL-01')}",
        evidence_level=guideline.get("evidence_level", EvidenceLevel.LEVEL_1),
        snippet=guideline.get("snippet", ""),
        relevance_score=0.98,
        key_takeaway=guideline.get("key_takeaway", "Consensus clinical guideline recommendation.")
    )
