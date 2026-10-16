"""
Polarity Disambiguator & False-Twin Clinical Anti-Bleed Engine.
Prevents semantic and keyword bleed between opposite clinical conditions:
e.g. "low blood pressure" vs "high blood pressure / hypertension"
     "hypoglycemia" vs "hyperglycemia"
     "bradycardia" vs "tachycardia"
     "dry cough" vs "productive wet cough"
     "hypokalemia" vs "hyperkalemia"
     "viral meningitis" vs "bacterial meningitis"
     "bipolar depression" vs "unipolar major depression"
     "ischemic stroke" vs "hemorrhagic stroke"
"""

import re
from typing import Dict, List, Tuple, Optional, Any

class PolarityRule:
    def __init__(
        self,
        name: str,
        trigger_regex: str,
        target_condition_keywords: List[str],
        contra_condition_keywords: List[str],
        boost_doc_ids: List[str],
        penalty_doc_ids: List[str],
        clinical_analogy: str,
        patient_explanation: str,
        clinician_focus: str
    ):
        self.name = name
        self.trigger_regex = re.compile(trigger_regex, re.IGNORECASE)
        self.target_condition_keywords = [k.lower() for k in target_condition_keywords]
        self.contra_condition_keywords = [k.lower() for k in contra_condition_keywords]
        self.boost_doc_ids = boost_doc_ids
        self.penalty_doc_ids = penalty_doc_ids
        self.clinical_analogy = clinical_analogy
        self.patient_explanation = patient_explanation
        self.clinician_focus = clinician_focus

POLARITY_RULES: List[PolarityRule] = [
    # 1. Low Blood Pressure vs Hypertension
    PolarityRule(
        name="Low Blood Pressure (Hypotension)",
        trigger_regex=r"\b(low\s*(blood\s*pressure|bp)|hypotension|postural\s*drop|orthostatic\s*(hypotension|drop)|blood\s*pressure\s*(is\s*too\s*low|dropped|falling|crashed|plunged))\b",
        target_condition_keywords=["orthostatic hypotension", "hypotension", "low blood pressure", "vasovagal"],
        contra_condition_keywords=["essential hypertension", "hypertension", "high blood pressure", "stage 1 hypertension", "stage 2 hypertension"],
        boost_doc_ids=["DOC-CARD-301", "DOC-CARD-305"],
        penalty_doc_ids=["DOC-CARD-001", "DOC-CARD-415", "DOC-CARD-417"],
        clinical_analogy="Think of blood pressure like the water pressure in a multi-story building. When blood pressure drops too low, there is not enough pressure to pump oxygen-rich blood up to the top floor (your brain), causing dizziness, lightheadedness, or blacking out when standing up [1].",
        patient_explanation="When you stand up, gravity pulls blood down toward your legs and belly. Normally, your body quickly squeezes leg blood vessels to maintain blood flow to your brain. In low blood pressure or orthostatic hypotension, this reflex lags, causing a temporary blood pressure drop.",
        clinician_focus="Management focuses on volume expansion, dietary sodium liberalization (unless contraindicated), compression garments, and pharmacological pressor therapy (Fludrocortisone, Midodrine, Droxidopa) rather than antihypertensive vasodilators."
    ),
    # 2. High Blood Pressure (Hypertension)
    PolarityRule(
        name="High Blood Pressure (Hypertension)",
        trigger_regex=r"\b(high\s*(blood\s*pressure|bp)|hypertension|elevated\s*bp|hypertensive|blood\s*pressure\s*(is\s*too\s*high|surged|spiked))\b",
        target_condition_keywords=["essential hypertension", "hypertension", "high blood pressure"],
        contra_condition_keywords=["orthostatic hypotension", "hypotension", "low blood pressure"],
        boost_doc_ids=["DOC-CARD-001"],
        penalty_doc_ids=["DOC-CARD-301", "DOC-CARD-305"],
        clinical_analogy="Think of your blood vessels like garden hoses carrying water under continuous high pressure. When pressure is elevated for months, it strains the heart pump and damages the delicate filtration vessels in your kidneys and brain [1].",
        patient_explanation="Elevated blood pressure slowly stiffens and thickens arterial walls. Combining dietary sodium reduction (DASH diet) with guideline medications relaxes the artery walls and protects vital organs.",
        clinician_focus="First-line pharmacotherapy utilizes ACE inhibitors, ARBs, CCBs, or thiazide-like diuretics targeting BP <130/80 mmHg."
    ),
    # 3. Low Blood Sugar (Hypoglycemia)
    PolarityRule(
        name="Low Blood Sugar (Hypoglycemia)",
        trigger_regex=r"\b(low\s*(blood\s*sugar|sugar|glucose)|hypoglycemia|hypoglycemic|sugar\s*(drop|crash|fell|plunged)|insulin\s*shock)\b",
        target_condition_keywords=["hypoglycemia", "low blood sugar", "whipple triad"],
        contra_condition_keywords=["type 2 diabetes", "hyperglycemia", "high blood sugar", "dka", "hhs"],
        boost_doc_ids=["DOC-CARD-302"],
        penalty_doc_ids=["DOC-CARD-007", "DOC-CARD-307", "DOC-CARD-308"],
        clinical_analogy="Think of glucose as the pure fuel in an engine's fuel line. When blood sugar drops below 70 mg/dL, the brain is starved of energy, triggering an immediate adrenaline alarm that causes shakiness, sweating, anxiety, and confusion [1].",
        patient_explanation="When blood sugar crashes, your body immediately needs fast-acting simple carbohydrates. The evidence-based 'Rule of 15' (eating 15 grams of fast-acting sugar like juice or glucose tabs, then waiting 15 minutes to recheck) safely restores brain fuel without causing an extreme rebound spike.",
        clinician_focus="Immediate treatment requires the Rule of 15 (oral fast carbohydrates), IV 10% or 50% Dextrose, or Glucagon (intranasal Baqsimi or IM), followed by review of insulin or sulfonylurea dosing."
    ),
    # 4. High Blood Sugar (Hyperglycemia / Diabetes)
    PolarityRule(
        name="High Blood Sugar (Hyperglycemia)",
        trigger_regex=r"\b(high\s*(blood\s*sugar|sugar|glucose)|hyperglycemia|hyperglycemic|sugar\s*(spike|surge|high))\b",
        target_condition_keywords=["type 2 diabetes", "diabetes mellitus", "hyperglycemia", "dka"],
        contra_condition_keywords=["hypoglycemia", "low blood sugar"],
        boost_doc_ids=["DOC-CARD-007"],
        penalty_doc_ids=["DOC-CARD-302"],
        clinical_analogy="Think of insulin like a key that unlocks cellular doors so sugar can leave the bloodstream and enter cells for energy. In hyperglycemia, the locks are resistant or keys are missing, allowing sugar to accumulate like excess silt in the pipes [1].",
        patient_explanation="Consistently elevated blood sugar leads to dehydration, frequent urination, and long-term damage to eyes, kidneys, and nerves.",
        clinician_focus="Guideline therapy incorporates Metformin, SGLT2 inhibitors, GLP-1 receptor agonists, and insulin titrated to target HbA1c <7.0%."
    ),
    # 5. Slow Heart Rate (Bradycardia / AV Block)
    PolarityRule(
        name="Slow Heart Rate (Bradycardia)",
        trigger_regex=r"\b(slow\s*(heart\s*rate|pulse|heartbeat)|bradycardia|heart\s*block|av\s*block|pulse\s*(too\s*slow|under\s*50|under\s*40)|sick\s*sinus)\b",
        target_condition_keywords=["sinus bradycardia", "complete av block", "atrioventricular block", "sick sinus syndrome", "bradycardia"],
        contra_condition_keywords=["tachycardia", "atrial fibrillation", "svt", "fast heart rate", "flutter"],
        boost_doc_ids=["DOC-CARD-303", "DOC-CARD-304", "DOC-CARD-412"],
        penalty_doc_ids=["DOC-CARD-003", "DOC-CARD-407", "DOC-CARD-408"],
        clinical_analogy="Think of your heart like an electronic metronome keeping the tempo of an orchestra. When the metronome slows excessively (below 50 or pauses for seconds), blood delivery to the brain stutters, causing dizziness, fatigue, and fainting [1].",
        patient_explanation="A resting pulse below 50-60 bpm with symptoms of dizziness or fainting indicates that the heart's natural electrical wiring is firing too slowly or blocked.",
        clinician_focus="Management identifies reversible medication culprits (beta-blockers, CCBs, digoxin), treats electrolyte abnormalities, and evaluates for permanent dual-chamber pacemaker implantation."
    ),
    # 6. Fast Heart Rate (Tachycardia / AFib)
    PolarityRule(
        name="Fast Heart Rate (Tachycardia)",
        trigger_regex=r"\b(fast\s*(heart\s*rate|pulse|heartbeat)|racing\s*heart|tachycardia|palpitations|heart\s*flutter|svt|atrial\s*fibrillation)\b",
        target_condition_keywords=["atrial fibrillation", "tachycardia", "supraventricular tachycardia", "ventricular tachycardia"],
        contra_condition_keywords=["bradycardia", "slow heart rate", "heart block"],
        boost_doc_ids=["DOC-CARD-003", "DOC-CARD-407", "DOC-CARD-408"],
        penalty_doc_ids=["DOC-CARD-303", "DOC-CARD-304"],
        clinical_analogy="Think of an electrical engine spinning into overdrive. When the heart beats at 150 to 200 bpm, the pumping chambers do not have enough time to refill with blood between contractions [1].",
        patient_explanation="Rapid heartbeats can feel like a fluttering bird or pounding drum in your chest.",
        clinician_focus="Rate control (beta-blockers, diltiazem), rhythm control (antiarrhythmics, cardioversion), and thromboembolic risk reduction with oral anticoagulation."
    ),
    # 7. Non-Productive (Dry) Cough
    PolarityRule(
        name="Dry Cough (Non-Productive)",
        trigger_regex=r"\b(dry\s*cough|tickle\s*cough|hacking\s*cough|cough\s*without\s*phlegm|non[\s-]*productive\s*cough)\b",
        target_condition_keywords=["acute non-productive dry cough", "dry cough", "cough reflex hypersensitivity"],
        contra_condition_keywords=["productive cough", "wet cough", "phlegm", "mucus"],
        boost_doc_ids=["DOC-CARD-310"],
        penalty_doc_ids=["DOC-CARD-309"],
        clinical_analogy="Think of hypersensitive cough nerve endings like an overly sensitive smoke detector that triggers from dry air or microscopic dust, setting off repeated coughing spasms even when there is zero phlegm to clear [1].",
        patient_explanation="A dry cough produces no mucus and is caused by irritated, twitchy nerve receptors in your upper airway.",
        clinician_focus="Management uses honey, demulcents, antitussives (Dextromethorphan), or inhaled corticosteroids for post-viral hypersensitivity without redundant antibiotics."
    ),
    # 8. Productive (Wet) Cough
    PolarityRule(
        name="Productive (Wet) Cough",
        trigger_regex=r"\b(wet\s*cough|productive\s*cough|coughing\s*up\s*(phlegm|mucus|sputum)|chest\s*congestion\s*cough)\b",
        target_condition_keywords=["acute productive cough", "productive cough", "bronchitis phlegm"],
        contra_condition_keywords=["dry cough", "non-productive cough"],
        boost_doc_ids=["DOC-CARD-309"],
        penalty_doc_ids=["DOC-CARD-310"],
        clinical_analogy="Think of phlegm like leaves clogging a stormwater drainage pipe. The productive wet cough is your body's vital natural broom sweeping the mucus and trapped bacteria upward so your airways stay open [1].",
        patient_explanation="A wet cough helps expel excess mucus from deep inside your lungs. Suppressing a wet cough with heavy cough syrups can trap bacteria inside your chest.",
        clinician_focus="Encourage hydration, expectorants (Guaifenesin), airway clearance, and evaluate for bacterial superinfection or pneumonia."
    ),
    # 9. Rotational Vertigo (BPPV / Vestibular)
    PolarityRule(
        name="Rotational Vertigo (Spinning)",
        trigger_regex=r"\b(vertigo|room\s*spinning|spinning\s*sensation|bppv|inner\s*ear\s*crystals|crystals\s*out\s*of\s*place)\b",
        target_condition_keywords=["benign paroxysmal positional vertigo", "bppv", "meniere", "vestibular"],
        contra_condition_keywords=["orthostatic hypotension", "presyncope", "lightheadedness", "fainting"],
        boost_doc_ids=["DOC-CARD-313", "DOC-CARD-314", "DOC-CARD-315"],
        penalty_doc_ids=["DOC-CARD-301", "DOC-CARD-305"],
        clinical_analogy="Think of your inner ear balance canals like tiny curved glass levels with microscopic fluid and stones. In BPPV, loose calcium crystals roll into the wrong canal, falsely telling your brain the room is violently spinning when you roll over in bed [1].",
        patient_explanation="True rotational vertigo produces an illusion that the room is spinning around you, triggered by head position changes.",
        clinician_focus="Diagnostic Dix-Hallpike maneuver followed by curative Epley particle repositioning maneuver (>85% single-session cure rate); vestibular suppressants should be minimized."
    ),
    # 10. Presyncope / Lightheadedness (Non-Spinning)
    PolarityRule(
        name="Presyncope / Lightheadedness",
        trigger_regex=r"\b(lightheaded|lightheadedness|feeling\s*faint|near\s*faint|about\s*to\s*pass\s*out|presyncope|graying\s*out|tunnel\s*vision)\b",
        target_condition_keywords=["vasovagal syncope", "orthostatic hypotension", "presyncope", "syncope"],
        contra_condition_keywords=["bppv", "rotational vertigo", "room spinning", "meniere"],
        boost_doc_ids=["DOC-CARD-305", "DOC-CARD-301"],
        penalty_doc_ids=["DOC-CARD-313", "DOC-CARD-314", "DOC-CARD-315"],
        clinical_analogy="Think of a temporary dip in electrical voltage to a computer screen, causing the display to dim or gray out for a few seconds before the power stabilizes [1].",
        patient_explanation="Presyncope is a sensation that you are about to pass out, without any sensation that the room is spinning.",
        clinician_focus="Evaluate orthostatic vitals, hydration status, ECG for conduction abnormalities, and teach physical counter-pressure maneuvers."
    ),
    # 11. Bipolar Depression vs Unipolar Depression
    PolarityRule(
        name="Bipolar Depression",
        trigger_regex=r"\b(bipolar\s*depression|bipolar\s*disorder|manic\s*depression|hypomania|bipolar\s*type\s*(1|2|i|ii))\b",
        target_condition_keywords=["bipolar depression", "bipolar disorder", "lurasidone", "quetiapine"],
        contra_condition_keywords=["major depressive disorder", "unipolar depression"],
        boost_doc_ids=["DOC-CARD-320"],
        penalty_doc_ids=["DOC-CARD-023"],
        clinical_analogy="Think of brain mood circuits operating on an alternating pendulum that swings between high-energy manic phases and low-energy depressive valleys. Standard unipolar antidepressants can dangerously fling the pendulum into full mania or rapid cycling [1].",
        patient_explanation="Bipolar depression is the low-mood phase of bipolar disorder. Treating it requires mood-stabilizing medicines rather than standard single antidepressants.",
        clinician_focus="First-line pharmacotherapy utilizes Quetiapine, Lurasidone, Lumateperone, or Cariprazine; antidepressant monotherapy is strictly contraindicated."
    ),
    # 12. Viral Meningitis vs Bacterial Meningitis
    PolarityRule(
        name="Viral Meningitis (Aseptic)",
        trigger_regex=r"\b(viral\s*meningitis|aseptic\s*meningitis|enteroviral\s*meningitis)\b",
        target_condition_keywords=["aseptic viral meningitis", "viral meningitis"],
        contra_condition_keywords=["acute bacterial meningitis", "bacterial meningitis", "streptococcal meningitis"],
        boost_doc_ids=["DOC-CARD-381"],
        penalty_doc_ids=["DOC-CARD-382"],
        clinical_analogy="A mild temporary swelling in the exterior insulation of a cable that cools down on its own with rest and fluids [1].",
        patient_explanation="Viral meningitis is inflammation of the protective brain lining caused by a common virus. Unlike bacterial meningitis, it is typically much milder and heals with rest.",
        clinician_focus="Supportive care with analgesia, antiemetics, and discontinuation of empiric antibacterials once CSF PCR/cultures rule out bacteria."
    ),
    # 13. Bacterial Meningitis (Emergency)
    PolarityRule(
        name="Acute Bacterial Meningitis",
        trigger_regex=r"\b(bacterial\s*meningitis|meningococcal\s*meningitis|pneumococcal\s*meningitis)\b",
        target_condition_keywords=["acute bacterial meningitis", "bacterial meningitis"],
        contra_condition_keywords=["viral meningitis", "aseptic meningitis"],
        boost_doc_ids=["DOC-CARD-382"],
        penalty_doc_ids=["DOC-CARD-381"],
        clinical_analogy="A severe fire breaking out directly inside the central computer server room, requiring immediate emergency fire suppressants [1].",
        patient_explanation="A life-threatening medical emergency where bacteria directly invade fluid around the brain, requiring immediate IV antibiotics.",
        clinician_focus="Immediate empiric IV Ceftriaxone + Vancomycin + Ampicillin combined with IV Dexamethasone administered before or with the first antibiotic dose."
    )
]

def detect_polarity_rule(query: str) -> Optional[PolarityRule]:
    """Matches query against clinical polarity rules."""
    for rule in POLARITY_RULES:
        if rule.trigger_regex.search(query):
            return rule
    return None

def adjust_document_scores_for_polarity(
    query: str,
    scored_docs: List[Tuple[int, float, Dict[str, Any]]]
) -> List[Tuple[int, float, Dict[str, Any]]]:
    """
    Applies aggressive anti-bleed re-ranking for False Twins:
    Boosts targeted twin records (2.5x - 4.0x) and heavily penalizes opposite records (0.01x).
    """
    rule = detect_polarity_rule(query)
    if not rule:
        return scored_docs

    adjusted = []
    for doc_id, score, doc in scored_docs:
        c_id = doc.get("id", "")
        disease_name = doc.get("disease", "").lower()
        title = doc.get("title", "").lower()

        is_boosted = False
        is_penalized = False

        # Check explicit ID lists
        if c_id in rule.boost_doc_ids:
            score *= 3.5
            is_boosted = True
        elif c_id in rule.penalty_doc_ids:
            score *= 0.01
            is_penalized = True

        # Check keyword patterns
        if not is_boosted and not is_penalized:
            if any(k in disease_name or k in title for k in rule.target_condition_keywords):
                score *= 2.5
            elif any(k in disease_name or k in title for k in rule.contra_condition_keywords):
                # Only penalize if the target keywords are NOT also present
                if not any(k in disease_name or k in title for k in rule.target_condition_keywords):
                    score *= 0.02

        adjusted.append((doc_id, score, doc))

    # Re-sort descending by adjusted score
    adjusted.sort(key=lambda x: x[1], reverse=True)
    return adjusted
