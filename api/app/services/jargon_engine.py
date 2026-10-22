"""
AegisMed Dynamic Clinical Jargon & Medical Terminology Engine.
Provides contextual, plain-language translation of complex medical jargon,
laboratory tests, biomarkers, pharmacological drug classes, and diagnostic scores
detected within clinical queries, doctor explanations, and patient syntheses.
"""

import re
from typing import List, Dict, Tuple, Optional, Set, Any
from app.models.schemas import JargonItem


# ============================================================
# Comprehensive Clinical Glossary Knowledge Bank
# ============================================================
CLINICAL_GLOSSARY_REGISTRY: List[Dict[str, Any]] = [
    # ── 1. Laboratory Biomarkers & Diagnostic Metrics ─────────
    {
        "term": "HbA1c",
        "patterns": [r"\b(hba1c|a1c|glycated hemoglobin|hemoglobin a1c)\b"],
        "plain_english": "A key blood test that measures your average blood sugar level over the past 2 to 3 months, used to track diabetes control."
    },
    {
        "term": "eGFR (Kidney Filtration Rate)",
        "patterns": [r"\b(egfr|gfr|estimated glomerular filtration rate|glomerular filtration)\b"],
        "plain_english": "A vital laboratory metric showing how effectively your kidneys are filtering toxins and fluid from your blood (normal is above 90)."
    },
    {
        "term": "Troponin",
        "patterns": [r"\b(troponin|hs-ctnt|hs-ctni|cardiac troponin)\b"],
        "plain_english": "A sensitive heart muscle protein that spills into the bloodstream when heart cells are injured or deprived of oxygen during a heart attack."
    },
    {
        "term": "BNP / NT-proBNP",
        "patterns": [r"\b(bnp|nt-probnp|b-type natriuretic peptide|natriuretic peptide)\b"],
        "plain_english": "A cardiac hormone released into the blood when heart chambers become stretched or fluid-overloaded, helping doctors detect heart failure."
    },
    {
        "term": "D-Dimer",
        "patterns": [r"\b(d-dimer|ddimer|fibrin degradation fragment)\b"],
        "plain_english": "A blood protein fragment produced when the body breaks down a blood clot; used to help rule out deep vein thrombosis (DVT) or pulmonary embolism."
    },
    {
        "term": "Serum Creatinine",
        "patterns": [r"\b(creatinine|serum creatinine|crcl)\b"],
        "plain_english": "A natural muscle waste product that builds up in the bloodstream when kidney filtration slows down."
    },
    {
        "term": "CRP (C-Reactive Protein)",
        "patterns": [r"\b(crp|c-reactive protein|hs-crp)\b"],
        "plain_english": "A protein made by the liver that surges in response to acute inflammation, infection, or vascular irritation."
    },
    {
        "term": "Serum Ferritin",
        "patterns": [r"\b(ferritin|serum ferritin|iron stores)\b"],
        "plain_english": "A blood protein that stores iron inside cells; low levels indicate iron deficiency, while very high levels signal iron overload or systemic inflammation."
    },
    {
        "term": "Microalbuminuria",
        "patterns": [r"\b(microalbuminuria|albuminuria|urine albumin-to-creatinine ratio|uacr|proteinuria)\b"],
        "plain_english": "Tiny amounts of protein leaking into the urine, which serves as the earliest warning sign of kidney vessel damage from diabetes or high blood pressure."
    },
    {
        "term": "Blood Lactate",
        "patterns": [r"\b(lactate|lactic acid|hyperlactatemia)\b"],
        "plain_english": "A chemical produced by tissues when they are severely starved of oxygen, used in emergency settings to detect sepsis or shock."
    },
    {
        "term": "Anion Gap",
        "patterns": [r"\b(anion gap|high anion gap metabolic acidosis|hagma)\b"],
        "plain_english": "A calculation comparing positive and negative blood electrolytes to identify dangerous acid build-up (such as in diabetic ketoacidosis or toxic ingestions)."
    },
    {
        "term": "Oxygen Saturation (SpO2)",
        "patterns": [r"\b(spo2|oxygen saturation|o2 sat|pulse oximetry)\b"],
        "plain_english": "The percentage of oxygen-carrying hemoglobin in your red blood cells (normal resting levels are typically 95% to 100%)."
    },

    # ── 2. Pharmacological Drug Classes & Regimens ─────────────
    {
        "term": "SGLT2 Inhibitors",
        "patterns": [r"\b(sglt2|sglt-2|sglt2i|dapagliflozin|empagliflozin|canagliflozin|farxiga|jardiance)\b"],
        "plain_english": "A breakthrough drug class that protects the heart and kidneys by releasing excess glucose and sodium out through the urine."
    },
    {
        "term": "GLP-1 Receptor Agonists",
        "patterns": [r"\b(glp-1|glp-1ra|semaglutide|liraglutide|dulaglutide|tirzepatide|ozempic|wegovy|mounjaro)\b"],
        "plain_english": "Medications that mimic natural gut hormones to lower blood sugar, slow stomach emptying, reduce appetite, and protect against cardiovascular events."
    },
    {
        "term": "ACE Inhibitors & ARBs",
        "patterns": [r"\b(ace inhibitor|acei|arb|angiotensin receptor blocker|lisinopril|enalapril|losartan|valsartan)\b"],
        "plain_english": "Foundational blood pressure medicines that relax and widen blood vessels while shielding delicate kidney filtration units from long-term damage."
    },
    {
        "term": "Beta-Blockers",
        "patterns": [r"\b(beta-blocker|beta blocker|metoprolol|carvedilol|bisoprolol|atenolol)\b"],
        "plain_english": "Heart medications that ease cardiovascular strain by slowing your resting heart rate and dampening the effects of adrenaline."
    },
    {
        "term": "DOACs (Direct Oral Anticoagulants)",
        "patterns": [r"\b(doac|doacs|noac|apixaban|eliquis|rivaroxaban|xarelto|dabigatran|oral anticoagulant)\b"],
        "plain_english": "Modern blood-thinning pills that prevent dangerous clots in conditions like AFib or DVT without requiring frequent routine blood monitoring."
    },
    {
        "term": "Statins",
        "patterns": [r"\b(statin|statins|atorvastatin|rosuvastatin|simvastatin|lipitor|crestor|hmg-coa)\b"],
        "plain_english": "Pill medications that significantly lower artery-clogging LDL cholesterol and strengthen protective caps over arterial plaque."
    },
    {
        "term": "CGRP Antagonists",
        "patterns": [r"\b(cgrp|erenumab|aimovig|fremanezumab|ajovy|rimegepant|nurtec|ubrogepant|anti-cgrp)\b"],
        "plain_english": "Targeted therapies that block calcitonin gene-related peptide (a pain transmitter in the brain) to prevent severe migraine attacks."
    },
    {
        "term": "Proton Pump Inhibitors (PPIs)",
        "patterns": [r"\b(ppi|ppis|proton pump inhibitor|omeprazole|esomeprazole|pantoprazole|prilosec)\b"],
        "plain_english": "Medications that significantly turn down acid production in the stomach lining to allow inflamed stomach or esophagus tissue to heal."
    },
    {
        "term": "CFTR Modulators",
        "patterns": [r"\b(cftr|cftr modulator|trikafta|elexacaftor|tezacaftor|ivacaftor)\b"],
        "plain_english": "Targeted precision genetic drugs that fix defective chloride channels in cells, dramatically clearing mucus in cystic fibrosis."
    },
    {
        "term": "N-Acetylcysteine (NAC)",
        "patterns": [r"\b(n-acetylcysteine|nac|acetadote|parvolex)\b"],
        "plain_english": "The life-saving intravenous or oral antidote for acetaminophen (Tylenol) poisoning that rapidly replenishes the liver's antioxidant defense."
    },

    # ── 3. Diagnostic Criteria, Scores & Consensus Rules ───────
    {
        "term": "Rumack-Matthew Nomogram",
        "patterns": [r"\b(rumack-matthew|rumack matthew|rumack|acetaminophen nomogram)\b"],
        "plain_english": "A clinical decision graph plotting blood acetaminophen levels against hours since ingestion to determine if emergency liver antidote therapy is required."
    },
    {
        "term": "Beck's Triad",
        "patterns": [r"\b(beck's triad|becks triad|beck triad)\b"],
        "plain_english": "A trio of emergency signs (low blood pressure, muffled heart sounds, and distended neck veins) signaling life-threatening fluid compression around the heart."
    },
    {
        "term": "Rule of 15 (Hypoglycemia)",
        "patterns": [r"\b(rule of 15|rule-of-15|15-15 rule|15g of fast-acting)\b"],
        "plain_english": "The standard safety protocol for low blood sugar: consume 15 grams of fast-acting sugar (like juice), wait 15 minutes, and re-check your blood glucose."
    },
    {
        "term": "NYHA Functional Class",
        "patterns": [r"\b(nyha|nyha class|new york heart association)\b"],
        "plain_english": "A standard 4-tier medical scale describing how much heart failure symptoms limit a patient's everyday physical activities."
    },
    {
        "term": "KDIGO Staging",
        "patterns": [r"\b(kdigo|kdigo staging|kdigo guidelines)\b"],
        "plain_english": "International clinical kidney disease guidelines that grade chronic kidney damage based on filtration rate (eGFR) and urine protein leakage."
    },
    {
        "term": "Centor Score",
        "patterns": [r"\b(centor|centor score|modified centor)\b"],
        "plain_english": "A clinical scoring checklist used by doctors to determine whether a sore throat is caused by strep bacteria requiring antibiotics or a common viral cold."
    },
    {
        "term": "Burch-Wartofsky Score",
        "patterns": [r"\b(burch-wartofsky|burch wartofsky|bwp point)\b"],
        "plain_english": "An emergency scoring system assessing heart rate, fever, and mental status to diagnose thyroid storm (a severe hyperthyroid crisis)."
    },

    # ── 4. Pathophysiological Mechanisms & Clinical Concepts ───
    {
        "term": "Ejection Fraction (EF)",
        "patterns": [r"\b(ejection fraction|ef|lvef|reduced ejection fraction|hfref|preserved ejection fraction|hfpef)\b"],
        "plain_english": "The percentage of blood inside your heart's main pumping chamber that is pushed out with each heartbeat (normal is 50% to 70%)."
    },
    {
        "term": "Orthostatic Hypotension",
        "patterns": [r"\b(orthostatic hypotension|postural hypotension|orthostatic drop)\b"],
        "plain_english": "A temporary drop in blood pressure when moving from sitting or lying to standing, which causes dizziness or blacking out."
    },
    {
        "term": "Ischemia",
        "patterns": [r"\b(ischemia|ischemic|myocardial ischemia|cerebral ischemia)\b"],
        "plain_english": "A dangerous restriction in blood supply to body tissues, starving cells of the vital oxygen and glucose needed to survive."
    },
    {
        "term": "Bronchospasm",
        "patterns": [r"\b(bronchospasm|bronchoconstriction|airway constriction)\b"],
        "plain_english": "A sudden involuntary tightening of the muscle bands surrounding your airways, causing wheezing, chest tightness, and coughing."
    },
    {
        "term": "Diaphoresis",
        "patterns": [r"\b(diaphoresis|profuse sweating|cold sweat|diaphoretic)\b"],
        "plain_english": "Excessive, profuse sweating triggered by the nervous system in response to acute physical distress, pain, or cardiac events."
    },
    {
        "term": "Dyspnea",
        "patterns": [r"\b(dyspnea|shortness of breath|breathlessness|air hunger)\b"],
        "plain_english": "The medical term for difficulty breathing or feeling uncomfortable air hunger even with minimal physical exertion."
    },
    {
        "term": "Paresthesia",
        "patterns": [r"\b(paresthesia|paresthesias|pins and needles|tingling sensation)\b"],
        "plain_english": "An abnormal burning, prickling, or 'pins-and-needles' skin sensation usually caused by temporary or chronic nerve compression."
    },
    {
        "term": "Hepatomegaly",
        "patterns": [r"\b(hepatomegaly|enlarged liver)\b"],
        "plain_english": "The clinical condition of having a liver enlarged beyond its normal anatomical size due to inflammation, congestion, or fat accumulation."
    },
    {
        "term": "Diabetic Ketoacidosis (DKA)",
        "patterns": [r"\b(diabetic ketoacidosis|dka|ketosis|ketoacidosis)\b"],
        "plain_english": "A dangerous metabolic emergency where a lack of insulin forces the body to burn fat for fuel, generating toxic acidic waste called ketones."
    },
    {
        "term": "Tension Pneumothorax",
        "patterns": [r"\b(tension pneumothorax|collapsed lung)\b"],
        "plain_english": "A life-threatening condition where air leaks into the chest cavity and cannot escape, putting high pressure on the heart and lungs."
    },

    # ── 5. Evidence-Based Medicine & Core Principles ───────────
    {
        "term": "First-Line GDMT",
        "patterns": [r"\b(first-line|first line|gdmt|guideline-directed|guideline directed)\b"],
        "plain_english": "Guideline-Directed Medical Therapy: the gold-standard treatments that international doctor panels have proven to be the most effective first choice."
    },
    {
        "term": "Oxford CEBM Level 1 Evidence",
        "patterns": [r"\b(cebm level 1|level 1 evidence|oxford cebm|meta-analysis|randomized controlled trial|rct)\b"],
        "plain_english": "The highest tier of scientific evidence, derived from large, rigorously controlled human trials and systematic statistical reviews."
    },
    {
        "term": "Dose Titration",
        "patterns": [r"\b(titration|dose titration|titrate|titrated)\b"],
        "plain_english": "The careful clinical process of starting a medication at a low dose and adjusting it gradually to achieve maximum benefit with minimal side effects."
    },
    {
        "term": "Contraindication",
        "patterns": [r"\b(contraindication|contraindications|contraindicated)\b"],
        "plain_english": "A specific health condition, lab result, or drug combination that makes a particular medicine unsafe to take."
    }
]


# ============================================================
# Dynamic Extraction Engine
# ============================================================
def extract_contextual_jargon(
    text: str,
    max_items: int = 5,
    query_context: Optional[str] = None
) -> List[JargonItem]:
    """
    Scans the synthesized response and query for complex clinical terms,
    returning a personalized, deduplicated list of JargonItems.
    """
    if not text:
        return _fallback_jargon_items()

    search_corpus = f"{query_context or ''} {text}".lower()
    scored_matches: List[Tuple[int, Dict[str, Any]]] = []

    for entry in CLINICAL_GLOSSARY_REGISTRY:
        matched = False
        match_count = 0
        for pat in entry["patterns"]:
            matches = re.findall(pat, search_corpus, flags=re.IGNORECASE)
            if matches:
                matched = True
                match_count += len(matches)

        if matched:
            # Score bonus if term was in user's query
            query_bonus = 5 if (query_context and any(re.search(p, query_context, re.IGNORECASE) for p in entry["patterns"])) else 0
            priority_score = match_count + query_bonus
            scored_matches.append((priority_score, entry))

    # Sort descending by contextual relevance
    scored_matches.sort(key=lambda x: x[0], reverse=True)

    results: List[JargonItem] = []
    seen_terms: Set[str] = set()

    for _, entry in scored_matches:
        term_name = entry["term"]
        if term_name not in seen_terms:
            seen_terms.add(term_name)
            results.append(
                JargonItem(
                    term=term_name,
                    plain_english=entry["plain_english"]
                )
            )
        if len(results) >= max_items:
            break

    # If fewer than 2 detected, supplement with essential foundational terms
    if len(results) < 2:
        for fb in _fallback_jargon_items():
            if fb.term not in seen_terms:
                results.append(fb)
                seen_terms.add(fb.term)
            if len(results) >= max_items:
                break

    return results


def _fallback_jargon_items() -> List[JargonItem]:
    """Standard baseline definitions when no specialized biomarkers/drugs are matched."""
    return [
        JargonItem(
            term="First-Line Treatment",
            plain_english="The very first therapy that doctor guidelines recommend because it has the best track record of safety and success."
        ),
        JargonItem(
            term="Clinical Guideline",
            plain_english="Evidence-backed medical recommendations developed by specialist physician organizations to ensure safe care."
        ),
        JargonItem(
            term="Evidence Level",
            plain_english="A medical rating system (Oxford CEBM) that grades how strongly supported a treatment is by large clinical studies."
        ),
        JargonItem(
            term="Side Effects",
            plain_english="Unintended body reactions to a medicine, which are usually mild, temporary, and manageable."
        )
    ]
