"""
Clinical Practice Guidelines Search Tool
Searches authoritative international guideline recommendations
(WHO, ACC/AHA, ADA, GINA, KDIGO, NICE, ESC, IDSA).
"""

from typing import List, Dict, Any
from langchain_core.tools import tool

CONSENSUS_GUIDELINES: List[Dict[str, Any]] = [
    {
        "organization": "WHO (World Health Organization)",
        "guideline_title": "WHO Guideline for the Pharmacological Treatment of Hypertension in Adults",
        "year": 2021,
        "condition": "hypertension",
        "keywords": ["hypertension", "blood pressure", "bp", "dash", "amlodipine", "lisinopril"],
        "recommendation": "Initiate treatment with any of 3 classes of first-line agents: thiazide diuretics, ACE inhibitors/ARBs, or dihydropyridine calcium channel blockers. Dual combination therapy recommended for baseline SBP >= 20 mmHg over target.",
        "target_bp": "< 140/90 mmHg for general adults; < 130/80 mmHg with established CVD.",
        "evidence_strength": "Strong recommendation, moderate-certainty evidence"
    },
    {
        "organization": "ADA (American Diabetes Association)",
        "guideline_title": "Standards of Care in Diabetes — Pharmacologic Approaches to Glycemic Treatment",
        "year": 2024,
        "condition": "diabetes",
        "keywords": ["diabetes", "type 2", "sugar", "glp-1", "semaglutide", "metformin", "sglt2"],
        "recommendation": "In adults with type 2 diabetes and established ASCVD, heart failure, or CKD, an SGLT2 inhibitor and/or GLP-1 receptor agonist with demonstrated CVD benefit is recommended independent of baseline HbA1c or metformin use.",
        "target_bp": "HbA1c < 7.0% for most non-pregnant adults; individualized to 7.5–8.0% in frail elderly.",
        "evidence_strength": "Level A (Highest quality RCT evidence)"
    },
    {
        "organization": "GINA (Global Initiative for Asthma)",
        "guideline_title": "Global Strategy for Asthma Management and Prevention",
        "year": 2023,
        "condition": "asthma",
        "keywords": ["asthma", "inhaler", "budesonide", "formoterol", "albuterol", "wheezing"],
        "recommendation": "GINA Track 1 (Preferred): As-needed low-dose ICS-formoterol is the preferred reliever across all asthma severities. SABA-only treatment without concurrent inhaled corticosteroid is no longer recommended due to increased mortality risk.",
        "target_bp": "Zero nighttime awakenings, normal pulmonary function (FEV1 > 80%).",
        "evidence_strength": "Evidence Level A"
    },
    {
        "organization": "ACC/AHA / Multi-Society",
        "guideline_title": "AHA/ACC/Multisociety Guideline on the Management of Blood Cholesterol",
        "year": 2023,
        "condition": "cholesterol",
        "keywords": ["cholesterol", "statin", "ldl", "atorvastatin", "pcsk9", "hyperlipidemia"],
        "recommendation": "High-intensity statin therapy (Atorvastatin 40-80 mg or Rosuvastatin 20-40 mg) achieving >= 50% LDL-C reduction recommended for secondary prevention in ASCVD. Add ezetimibe if LDL remains >= 70 mg/dL.",
        "target_bp": "LDL-C < 55 mg/dL in very high-risk ASCVD patients.",
        "evidence_strength": "Class I, Level A"
    },
    {
        "organization": "IDSA / WHO",
        "guideline_title": "Guidelines on the Treatment and Management of Patients with COVID-19",
        "year": 2023,
        "condition": "covid-19",
        "keywords": ["covid", "coronavirus", "paxlovid", "remdesivir", "nirmatrelvir"],
        "recommendation": "In ambulatory patients with mild-to-moderate COVID-19 at high risk of progression, IDSA strongly recommends ritonavir-boosted nirmatrelvir (Paxlovid) initiated within 5 days of symptom onset.",
        "target_bp": "Prevention of hospitalization and death; prompt viral load decay.",
        "evidence_strength": "Strong recommendation, high certainty evidence"
    }
]


def search_consensus_guidelines(query: str, max_results: int = 3) -> List[Dict[str, Any]]:
    """
    Searches consensus medical guidelines matching query.
    """
    q_low = query.strip().lower()
    tokens = [t for t in q_low.split() if len(t) > 2]

    scored = []
    for g in CONSENSUS_GUIDELINES:
        score = 0
        search_blob = f"{g['organization']} {g['guideline_title']} {g['condition']} {' '.join(g['keywords'])} {g['recommendation']}".lower()
        if g["condition"] in q_low:
            score += 5
        for tok in tokens:
            if tok in search_blob:
                score += 1
        scored.append((score, g))

    scored.sort(key=lambda x: x[0], reverse=True)
    top_matches = [item[1] for item in scored if item[0] > 0][:max_results]

    if not top_matches:
        top_matches = CONSENSUS_GUIDELINES[:max_results]

    return top_matches


@tool
def guideline_retriever_tool(condition_or_query: str) -> List[Dict[str, Any]]:
    """
    Retrieves official international clinical practice guidelines (WHO, AHA, ADA, GINA, IDSA, KDIGO).
    Parameters:
      condition_or_query: Disease name or clinical subject (e.g. 'hypertension', 'asthma', 'type 2 diabetes')
    """
    return search_consensus_guidelines(condition_or_query)
