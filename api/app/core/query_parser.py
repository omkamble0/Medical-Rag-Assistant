"""
Inbound Clinical Query Disambiguation & Entity Parser.
Stage 1 of the AegisMed Healthcare Knowledge Navigator pipeline.

Performs structured clinical entity extraction, missing variable detection,
and anti-hallucination context gap flagging prior to evidence retrieval.
"""

import re
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class ExpandedClinicalQuery(BaseModel):
    original_intent: str = Field(..., description="The user's query intent in plain text")
    clinical_synonyms: List[str] = Field(
        ..., 
        description="Standardized medical terminology, diagnoses, or drug classes related to the layperson query (e.g., 'Acute Viral Upper Respiratory Infection' for 'cold')"
    )
    is_common_ailment: bool = Field(..., description="True if this is a low-acuity primary care issue like a cold, minor sprain, or tension headache")
    augmented_query: Optional[str] = Field(
        default=None,
        description="Hybrid search query combining raw layperson terms with clinical guideline synonyms"
    )


class Demographics(BaseModel):
    age_group: Optional[str] = Field(default=None, description="pediatric, adult, geriatric, or unspecified")
    pregnancy_status: Optional[str] = Field(default=None, description="pregnant, postpartum, non-pregnant, or unspecified")
    comorbidities: List[str] = Field(default_factory=list, description="Explicitly mentioned comorbidities")


class ClinicalEntities(BaseModel):
    primary_condition: Optional[str] = Field(None, description="Target disease, disorder, or primary symptom")
    interventions: List[str] = Field(default_factory=list, description="Medications, procedures, or lifestyle therapies")
    patient_demographics: Demographics = Field(default_factory=Demographics, description="Extracted age, pregnancy, or cohort parameters")
    clinical_metrics: Dict[str, Any] = Field(default_factory=dict, description="Identified biomarkers, lab values, or vitals (e.g. eGFR, HbA1c, BP)")


class ParsedQueryAnalysis(BaseModel):
    raw_query: str
    entities: ClinicalEntities
    expanded_query: Optional[ExpandedClinicalQuery] = Field(
        default=None,
        description="Layperson-to-Clinical query expansion with standardized scientific nomenclature"
    )
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
    nlp_analysis: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Deep clinical NLP analysis (NegEx asserted/negated findings, intent, acuity, morphological roots, expanded acronyms)"
    )



# --- Comprehensive Layperson-to-Clinical Medical Lexicon & Ontology ---
LAYPERSON_CLINICAL_MAP: List[Dict[str, Any]] = [
    {
        "patterns": [r"\b(low\s*(blood\s*pressure|bp)|hypotension|postural\s*drop|orthostatic\s*(hypotension|drop)|blood\s*pressure\s*(is\s*too\s*low|dropped|falling|crashed|plunged))\b"],
        "clinical_synonyms": [
            "Orthostatic Hypotension (Postural Low Blood Pressure)",
            "Autonomic Failure Hypotension",
            "Fludrocortisone / Midodrine Pressor Therapy",
            "Volume Expansion & Sodium Liberalization",
            "Withhold Antihypertensive Vasodilators"
        ],
        "is_common_ailment": False,
        "primary_label": "Orthostatic Hypotension (Low Blood Pressure)"
    },
    {
        "patterns": [r"\b(high\s*(blood\s*pressure|bp)|hypertension|stage\s*[12]\s*hypertension|elevated\s*blood\s*pressure|elevated\s*bp)\b"],
        "clinical_synonyms": [
            "Essential Hypertension",
            "ACC/AHA Guideline Blood Pressure Management",
            "ACEi / ARB / CCB Guideline Therapy",
            "DASH Diet Sodium Restriction"
        ],
        "is_common_ailment": True,
        "primary_label": "Essential Hypertension (High Blood Pressure)"
    },
    {
        "patterns": [r"\b(low\s*(blood\s*sugar|sugar|glucose)|hypoglycemia|hypoglycemic|sugar\s*(drop|crash|fell|plunged)|insulin\s*shock)\b"],
        "clinical_synonyms": [
            "Acute Hypoglycemia (Whipple Triad)",
            "Rule of 15 Fast-Acting Carbohydrates",
            "Glucagon Emergency Protocol",
            "Dextrose 50% IV"
        ],
        "is_common_ailment": False,
        "primary_label": "Acute Hypoglycemia (Low Blood Sugar)"
    },
    {
        "patterns": [r"\b(slow\s*(heart\s*rate|pulse|heartbeat)|bradycardia|heart\s*block|av\s*block|sick\s*sinus)\b"],
        "clinical_synonyms": [
            "Sinus Bradycardia",
            "Complete Atrioventricular (AV) Block",
            "Sick Sinus Syndrome",
            "Dual-Chamber Pacemaker Evaluation"
        ],
        "is_common_ailment": False,
        "primary_label": "Sinus Bradycardia / Atrioventricular Block"
    },
    {
        "patterns": [r"\b(dry\s*cough|tickle\s*cough|hacking\s*cough|cough\s*without\s*phlegm|non[\s-]*productive\s*cough)\b"],
        "clinical_synonyms": [
            "Acute Non-Productive Dry Cough",
            "Cough Reflex Hypersensitivity",
            "Dextromethorphan Antitussive"
        ],
        "is_common_ailment": True,
        "primary_label": "Acute Non-Productive Dry Cough"
    },
    {
        "patterns": [r"\b(wet\s*cough|productive\s*cough|coughing\s*up\s*(phlegm|mucus|sputum)|chest\s*congestion\s*cough)\b"],
        "clinical_synonyms": [
            "Acute Productive Cough",
            "Bronchial Mucopurulent Secretions",
            "Guaifenesin Expectorant"
        ],
        "is_common_ailment": True,
        "primary_label": "Acute Productive Cough (Phlegm / Sputum)"
    },
    {
        "patterns": [r"\b(cold|common cold|head cold|runny nose|sneezing|stuffy nose|nasal drip)\b"],
        "clinical_synonyms": ["Acute Viral Upper Respiratory Infection", "Acute Rhinosinusitis", "Coryza", "Nasopharyngitis", "Viral Rhinitis"],
        "is_common_ailment": True,
        "primary_label": "Acute Viral Upper Respiratory Infection (Common Cold)"
    },
    {
        "patterns": [
            r"\b(throw up and the runs|throwing up and diarrhea|vomiting and diarrhea|stomach bug|stomach flu|food poisoning|tummy bug|vomiting and runs|puking and diarrhea)\b",
            r"\b(throw up|throwing up|puking|vomiting)\b.*\b(runs|diarrhea|loose stools|watery poop)\b",
            r"\b(runs|diarrhea|loose stools)\b.*\b(throw up|throwing up|puking|vomiting)\b"
        ],
        "clinical_synonyms": [
            "Acute Gastroenteritis",
            "Viral Enteritis (Norovirus / Rotavirus)",
            "Infectious Diarrheal Colitis",
            "Acute Dehydration & Fluid Loss",
            "Oral Rehydration Therapy (ORT)"
        ],
        "is_common_ailment": True,
        "primary_label": "Acute Infectious Gastroenteritis"
    },
    {
        "patterns": [r"\b(heart attack|chest clutching|crushing chest pain|coronary|clogged artery in heart|stent in heart)\b"],
        "clinical_synonyms": [
            "Acute Coronary Syndrome (ACS)",
            "Non-ST-Elevation Acute Coronary Syndrome (NSTEMI / Unstable Angina)",
            "ST-Elevation Myocardial Infarction (STEMI)",
            "High-Sensitivity Cardiac Troponin (hs-cTn)"
        ],
        "is_common_ailment": False,
        "primary_label": "Acute Coronary Syndrome (Myocardial Infarction)"
    },
    {
        "patterns": [r"\b(pink eye|red eye|crusty eye|goopy eye|eye discharge|eye infection)\b"],
        "clinical_synonyms": ["Acute Conjunctivitis", "Bacterial Conjunctivitis", "Viral Conjunctivitis", "Allergic Conjunctivitis"],
        "is_common_ailment": True,
        "primary_label": "Acute Conjunctivitis"
    },
    {
        "patterns": [r"\b(hives|welts|itchy bumps|nettle rash|wheals)\b"],
        "clinical_synonyms": ["Chronic Spontaneous Urticaria", "Acute Urticaria", "Second-Generation Antihistamines", "Omalizumab"],
        "is_common_ailment": True,
        "primary_label": "Chronic Spontaneous Urticaria"
    },
    {
        "patterns": [r"\b(strep throat|sore throat|scratchy throat|throat pain|swollen tonsils)\b"],
        "clinical_synonyms": ["Acute Pharyngitis", "Group A Streptococcal Pharyngitis", "Centor Score Criteria", "Tonsillitis"],
        "is_common_ailment": True,
        "primary_label": "Acute Streptococcal Pharyngitis"
    },
    {
        "patterns": [r"\b(water infection|bladder infection|burning pee|painful urination|peeing glass|urine infection|uti)\b"],
        "clinical_synonyms": ["Urinary Tract Infection (UTI)", "Acute Uncomplicated Cystitis", "Nitrofurantoin / TMP-SMX", "Pyelonephritis"],
        "is_common_ailment": True,
        "primary_label": "Urinary Tract Infection (Acute Cystitis)"
    },
    {
        "patterns": [r"\b(kidney stone|kidney stones|passing a stone|renal stone|back flank pain)\b"],
        "clinical_synonyms": ["Nephrolithiasis", "Urolithiasis", "Renal Colic", "Non-Contrast CT Abdomen/Pelvis", "Tamsulosin Medical Expulsive Therapy"],
        "is_common_ailment": False,
        "primary_label": "Nephrolithiasis (Kidney Stones)"
    },
    {
        "patterns": [r"\b(sugar disease|high blood sugar|sweet pee|diabetes|diabetic)\b"],
        "clinical_synonyms": ["Type 2 Diabetes Mellitus", "Hyperglycemia", "HbA1c Target <7.0%", "Metformin / GLP-1 Receptor Agonists", "SGLT2 Inhibitors"],
        "is_common_ailment": False,
        "primary_label": "Type 2 Diabetes Mellitus"
    },
    {
        "patterns": [r"\b(high blood pressure|high bp|hypertension|tight blood vessels)\b"],
        "clinical_synonyms": ["Essential Hypertension", "Stage 1 / Stage 2 Arterial Hypertension", "Amlodipine / Lisinopril / ARB", "DASH Diet & Sodium Restriction"],
        "is_common_ailment": False,
        "primary_label": "Essential Hypertension"
    },
    {
        "patterns": [r"\b(anxiety|anxious|panic|panic attack|panic disorder|gad|constant worry|nervousness)\b"],
        "clinical_synonyms": ["Generalized Anxiety Disorder (GAD)", "Panic Disorder", "SSRI / SNRI Pharmacotherapy", "Cognitive Behavioral Therapy (CBT)"],
        "is_common_ailment": False,
        "primary_label": "Generalized Anxiety Disorder / Panic Disorder"
    },
    {
        "patterns": [r"\b(heart failure|chf|congestive heart failure|swollen ankles.*breath|trouble breathing.*lying|breath.*lying down|breath.*lying flat|cannot lie flat|waking up gasping|orthopnea|peripheral edema|paroxysmal nocturnal dyspnea)\b"],
        "clinical_synonyms": ["Congestive Heart Failure (CHF)", "Heart Failure with Reduced Ejection Fraction (HFrEF)", "Orthopnea & Paroxysmal Nocturnal Dyspnea", "Peripheral Edema & Volume Overload", "Sacubitril/Valsartan (Entresto)", "Loop Diuretics"],
        "is_common_ailment": False,
        "primary_label": "Heart Failure (HFrEF)"
    },
    {
        "patterns": [r"\b(wheezing|asthma attack|short of breath|trouble breathing|winded|inhaler)\b"],
        "clinical_synonyms": ["Bronchial Asthma", "Acute Bronchospasm", "Inhaled Corticosteroid-Formoterol (SMART)", "Chronic Obstructive Pulmonary Disease (COPD)"],
        "is_common_ailment": False,
        "primary_label": "Bronchial Asthma / COPD"
    },
    {
        "patterns": [r"\b(stroke|brain bleed|face drooping|slurred speech|weak arm on one side|mini stroke|tia)\b"],
        "clinical_synonyms": ["Acute Ischemic Stroke", "Transient Ischemic Attack (TIA)", "Intravenous Thrombolysis (Alteplase / Tenecteplase)", "Endovascular Thrombectomy"],
        "is_common_ailment": False,
        "primary_label": "Acute Ischemic Stroke"
    },
    {
        "patterns": [r"\b(blood clot in leg|swollen red calf|clot in lungs|dvt|pulmonary embolus|blood clot)\b"],
        "clinical_synonyms": ["Deep Vein Thrombosis (DVT)", "Pulmonary Embolism (PE)", "Venous Thromboembolism (VTE)", "Direct Oral Anticoagulants (DOACs - Apixaban/Rivaroxaban)"],
        "is_common_ailment": False,
        "primary_label": "Venous Thromboembolism (DVT / PE)"
    },
    {
        "patterns": [r"\b(restless legs|jumpy legs at night|crawling sensation in legs|ants in legs)\b"],
        "clinical_synonyms": ["Restless Legs Syndrome (RLS)", "Willis-Ekbom Disease", "Serum Ferritin Deficiency (<75 ng/mL)", "Alpha-2-Delta Ligands (Pregabalin / Gabapentin)"],
        "is_common_ailment": True,
        "primary_label": "Restless Legs Syndrome (RLS)"
    },
    {
        "patterns": [r"\b(joint wear and tear|clicking knees|bone on bone|worn out hip|cartilage loss)\b"],
        "clinical_synonyms": ["Osteoarthritis (OA)", "Degenerative Joint Disease", "Topical NSAIDs / Exercise Therapy", "Total Knee / Hip Arthroplasty"],
        "is_common_ailment": True,
        "primary_label": "Osteoarthritis (OA)"
    },
    {
        "patterns": [r"\b(gout|red swollen big toe|uric acid flare|crystals in joint)\b"],
        "clinical_synonyms": ["Acute Gout Flare", "Gouty Arthritis", "Colchicine / NSAIDs / Corticosteroids", "Allopurinol Urate-Lowering Therapy (Target <6.0 mg/dL)"],
        "is_common_ailment": False,
        "primary_label": "Gout & Hyperuricemia"
    },
    {
        "patterns": [r"\b(acid reflux|heartburn|sour stomach|acid coming up throat|gerd|indigestion)\b"],
        "clinical_synonyms": ["Gastroesophageal Reflux Disease (GERD)", "Reflux Esophagitis", "Proton Pump Inhibitors (PPI - Omeprazole)", "H2 Receptor Antagonists"],
        "is_common_ailment": True,
        "primary_label": "Gastroesophageal Reflux Disease (GERD)"
    },
    {
        "patterns": [r"\b(low thyroid|sluggish thyroid|slow metabolism|cold sensitivity and weight gain)\b"],
        "clinical_synonyms": ["Primary Hypothyroidism", "Hashimoto Thyroiditis", "Serum TSH Elevation", "Levothyroxine Sodium Monotherapy"],
        "is_common_ailment": False,
        "primary_label": "Primary Hypothyroidism"
    },
    {
        "patterns": [r"\b(shingles|painful rash on one side|blisters in stripe|nerve pain after rash)\b"],
        "clinical_synonyms": ["Herpes Zoster", "Postherpetic Neuralgia (PHN)", "Oral Valacyclovir / Famciclovir", "Recombinant Zoster Vaccine (Shingrix)"],
        "is_common_ailment": False,
        "primary_label": "Herpes Zoster (Shingles)"
    },
    {
        "patterns": [r"\b(memory loss|forgetfulness|getting lost|senility|dementia|alzheimers)\b"],
        "clinical_synonyms": ["Early Alzheimer's Disease", "Mild Cognitive Impairment (MCI)", "Amyloid-Beta Monoclonal Antibodies (Lecanemab / Donanemab)", "Cholinesterase Inhibitors (Donepezil)"],
        "is_common_ailment": False,
        "primary_label": "Early Alzheimer's Disease & Cognitive Impairment"
    },
    {
        "patterns": [r"\b(eczema|atopic skin|itchy dry red patches|skin creases rash)\b"],
        "clinical_synonyms": ["Atopic Dermatitis (Eczema)", "Skin Barrier Dysfunction", "Topical Corticosteroids / Calcineurin Inhibitors", "Dupilumab Biologic Therapy"],
        "is_common_ailment": True,
        "primary_label": "Atopic Dermatitis (Eczema)"
    },
    {
        "patterns": [r"\b(psoriasis|silvery scaly patches|thick red skin plaques|elbow and knee plaques)\b"],
        "clinical_synonyms": ["Plaque Psoriasis", "Psoriatic Disease", "Topical Corticosteroid / Calcipotriene", "IL-17 / IL-23 / TNF Biologics"],
        "is_common_ailment": False,
        "primary_label": "Plaque Psoriasis"
    },
    {
        "patterns": [r"\b(appendix|belly button pain moving to right|right lower belly pain|burst appendix)\b"],
        "clinical_synonyms": ["Acute Appendicitis", "Laparoscopic Appendectomy", "Alvarado / AIR Score", "Abdominal CT / Ultrasound Evaluation"],
        "is_common_ailment": False,
        "primary_label": "Acute Appendicitis"
    },
    {
        "patterns": [r"\b(diverticulitis|left lower belly pain|pockets in colon|colon pouch inflammation)\b"],
        "clinical_synonyms": ["Acute Colonic Diverticulitis", "Uncomplicated vs Complicated Diverticulitis (Hinchey)", "Abdominal CT with IV Contrast", "Colonoscopy 6-8 Weeks Post-Resolution"],
        "is_common_ailment": False,
        "primary_label": "Acute Diverticulitis"
    },
    {
        "patterns": [r"\b(throat closing|severe allergic reaction|anaphylaxis|nut reaction|sting reaction)\b"],
        "clinical_synonyms": ["Systemic Anaphylaxis", "Intramuscular Epinephrine (Anterolateral Thigh)", "Biphasic Allergic Reaction", "Airway & Hemodynamic Compromise"],
        "is_common_ailment": False,
        "primary_label": "Anaphylaxis"
    },
    {
        "patterns": [r"\b(macular degeneration|wavy straight lines|blank spot in center vision|wet amd|dry amd)\b"],
        "clinical_synonyms": ["Age-Related Macular Degeneration (AMD)", "Neovascular / Wet AMD", "Intravitreal Anti-VEGF (Aflibercept / Ranibizumab)", "AREDS2 Antioxidant Formulation"],
        "is_common_ailment": False,
        "primary_label": "Age-Related Macular Degeneration (AMD)"
    },
    {
        "patterns": [r"\b(glaucoma|high eye pressure|tunnel vision|losing side vision)\b"],
        "clinical_synonyms": ["Primary Open-Angle Glaucoma (POAG)", "Intraocular Pressure (IOP) Reduction", "Topical Prostaglandin Analogs (Latanoprost)", "Selective Laser Trabeculoplasty (SLT)"],
        "is_common_ailment": False,
        "primary_label": "Primary Open-Angle Glaucoma (POAG)"
    },
    {
        "patterns": [r"\b(temple headache|jaw pain chewing|pain on side of scalp|blindness in one eye older adult)\b"],
        "clinical_synonyms": ["Giant Cell Arteritis (Temporal Arteritis)", "Erythrocyte Sedimentation Rate (ESR) / CRP Elevation", "High-Dose Systemic Glucocorticoids", "Tocilizumab IL-6 Receptor Antagonist"],
        "is_common_ailment": False,
        "primary_label": "Giant Cell Arteritis (Temporal Arteritis)"
    },
    {
        "patterns": [r"\b(bell's palsy|one side face paralyzed|face droop cannot close eye|droopy smile)\b"],
        "clinical_synonyms": ["Idiopathic Facial Paralysis (Bell's Palsy)", "Oral Corticosteroids (Prednisone within 72h)", "Corneal Lubrication & Eye Taping", "Facial Nerve (CN VII) Neuropathy"],
        "is_common_ailment": True,
        "primary_label": "Bell's Palsy (Idiopathic Facial Paralysis)"
    },
    {
        "patterns": [r"\b(carpal tunnel|numb hand at night|tingling thumb index|wrist splint|dropping things)\b"],
        "clinical_synonyms": ["Carpal Tunnel Syndrome (CTS)", "Median Nerve Compression", "Nocturnal Neutral-Angle Wrist Splinting", "Electromyography / Nerve Conduction Study (EMG/NCS)"],
        "is_common_ailment": True,
        "primary_label": "Carpal Tunnel Syndrome"
    },
    {
        "patterns": [r"\b(concussion|bumped head dizzy|head knock sports|post concussion)\b"],
        "clinical_synonyms": ["Mild Traumatic Brain Injury (mTBI / Concussion)", "Graduated Return-to-Learn / Return-to-Play", "SCAT5 / SCAT6 Protocol", "Avoidance of Prolonged Cocooning"],
        "is_common_ailment": True,
        "primary_label": "Mild Traumatic Brain Injury (Concussion)"
    },
    {
        "patterns": [r"\b(hay fever|seasonal allergy|pollen allergy|itchy eyes and sneezing in spring)\b"],
        "clinical_synonyms": ["Allergic Rhinitis", "Intranasal Corticosteroids (Fluticasone / Budesonide)", "Second-Generation Oral Antihistamines", "Allergen Immunotherapy"],
        "is_common_ailment": True,
        "primary_label": "Allergic Rhinitis"
    },
    {
        "patterns": [r"\b(pimples|zits|blackheads|cystic acne|skin breakouts|acne scars)\b"],
        "clinical_synonyms": ["Acne Vulgaris", "Topical Retinoids (Adapalene / Tretinoin)", "Benzoyl Peroxide", "Oral Isotretinoin for Nodulocystic Acne"],
        "is_common_ailment": True,
        "primary_label": "Acne Vulgaris"
    },
    {
        "patterns": [r"\b(stiff shoulders in morning|aching hips older adult|cannot lift arms morning stiffness)\b"],
        "clinical_synonyms": ["Polymyalgia Rheumatica (PMR)", "Low-Dose Systemic Glucocorticoids (Prednisone)", "ESR / CRP Inflammatory Markers", "Screening for Giant Cell Arteritis"],
        "is_common_ailment": False,
        "primary_label": "Polymyalgia Rheumatica (PMR)"
    },
    {
        "patterns": [r"\b(thyroid lump|neck knot|swollen gland in neck|thyroid nodule)\b"],
        "clinical_synonyms": ["Thyroid Nodule Evaluation", "Serum TSH & Diagnostic Neck Ultrasound", "Fine-Needle Aspiration (FNA) Biopsy", "Bethesda System for Thyroid Cytopathology"],
        "is_common_ailment": False,
        "primary_label": "Thyroid Nodule"
    },
    {
        "patterns": [r"\b(ectopic pregnancy|tubal pregnancy|positive pregnancy test sharp pelvic pain|cramping and bleeding positive test)\b"],
        "clinical_synonyms": ["Tubal Ectopic Pregnancy", "Transvaginal Ultrasound (TVUS) & Serial Beta-hCG", "Intramuscular Methotrexate Medical Management", "Emergency Laparoscopic Salpingectomy"],
        "is_common_ailment": False,
        "primary_label": "Tubal Ectopic Pregnancy"
    },
    {
        "patterns": [r"\b(bleeding after menopause|spotting years after period|postmenopausal bleeding)\b"],
        "clinical_synonyms": ["Postmenopausal Bleeding (PMB)", "Transvaginal Ultrasound (Endometrial Stripe ≤4 mm)", "Endometrial Biopsy", "Endometrial Hyperplasia / Carcinoma Screening"],
        "is_common_ailment": False,
        "primary_label": "Postmenopausal Bleeding & Endometrial Hyperplasia"
    },
    {
        "patterns": [r"\b(erectile dysfunction|impotence|trouble getting hard|cannot maintain erection)\b"],
        "clinical_synonyms": ["Erectile Dysfunction (ED)", "Phosphodiesterase-5 Inhibitors (PDE5i - Sildenafil / Tadalafil)", "Cardiovascular ASCVD Risk Screening", "Absolute Nitrate Contraindication"],
        "is_common_ailment": True,
        "primary_label": "Erectile Dysfunction (ED)"
    },
    {
        "patterns": [r"\b(high potassium|too much potassium in blood|elevated k\+|potassium spike)\b"],
        "clinical_synonyms": ["Hyperkalemia (Serum K+ ≥6.5 mEq/L or ECG changes)", "Intravenous Calcium Gluconate (Myocardial Stabilization)", "Intravenous Regular Insulin + Dextrose (Intracellular Shift)", "GI Potassium Binders / Emergent Hemodialysis"],
        "is_common_ailment": False,
        "primary_label": "Hyperkalemia"
    },
    {
        "patterns": [r"\b(panic attack|panic attacks|panic disorder|sudden terror|heart racing fear of dying|agoraphobia|fear of leaving home)\b"],
        "clinical_synonyms": [
            "Panic Disorder & Agoraphobia",
            "Cognitive Behavioral Therapy (CBT)",
            "Selective Serotonin Reuptake Inhibitors (SSRIs - Sertraline / Escitalopram)",
            "Cochrane Systematic Review: Bighelli I et al (2024)",
            "Interoceptive Exposure Protocol"
        ],
        "is_common_ailment": False,
        "primary_label": "Panic Disorder & Agoraphobia"
    },
    {
        "patterns": [r"\b(anxiety|chronic anxiety|generalized anxiety|constant worry|on edge|nervous breakdown|gad)\b"],
        "clinical_synonyms": [
            "Generalized Anxiety Disorder (GAD)",
            "GAD-7 Assessment Staging",
            "First-Line SSRI / SNRI Pharmacotherapy",
            "Evidence-Based Cognitive Behavioral Therapy (CBT)",
            "NICE Clinical Guideline 113"
        ],
        "is_common_ailment": True,
        "primary_label": "Generalized Anxiety Disorder (GAD)"
    },
    {
        "patterns": [r"\b(depression|major depression|severe sadness|loss of interest|anhedonia|feeling hopeless|mdd)\b"],
        "clinical_synonyms": [
            "Major Depressive Disorder (MDD)",
            "PHQ-9 Clinical Depression Screening",
            "Second-Generation Antidepressants (SSRIs / SNRIs)",
            "Interpersonal Psychotherapy (IPT) & CBT",
            "APA Clinical Practice Guideline for Depression"
        ],
        "is_common_ailment": True,
        "primary_label": "Major Depressive Disorder (MDD)"
    },
    {
        "patterns": [r"\b(evidence[- ]based treatments?|best treatments?|first[- ]line (therap(y|ies)|treatments?)|guideline[- ]directed)\b"],
        "clinical_synonyms": [
            "Oxford CEBM Level 1 Evidence",
            "Systematic Reviews & Meta-Analyses",
            "Clinical Practice Guidelines (WHO / NICE / APA / Cochrane)"
        ],
        "is_common_ailment": False,
        "primary_label": "Evidence-Based Clinical Guidelines"
    },
]


def expand_layperson_query(raw_query: str) -> ExpandedClinicalQuery:
    """
    Step 1: Layperson-to-Clinical Translator Engine.
    Maps conversational, everyday patient language ('cold', 'stomach bug', 'throw up and the runs')
    to standardized, CEBM Level 1 clinical nomenclatures and guideline entities.
    """
    clean_q = raw_query.strip()
    q_low = clean_q.lower()
    
    collected_synonyms: List[str] = []
    is_common = False
    
    for item in LAYPERSON_CLINICAL_MAP:
        matched = False
        for pat in item["patterns"]:
            if re.search(pat, q_low, re.IGNORECASE):
                matched = True
                break
        if matched:
            for syn in item["clinical_synonyms"]:
                if syn not in collected_synonyms:
                    collected_synonyms.append(syn)
            if item.get("is_common_ailment"):
                is_common = True
    
    # If no specialized colloquial match found, synthesize baseline clinical synonyms from tokens
    if not collected_synonyms:
        # Fallback to standard token extraction
        tokens = [w for w in re.findall(r"\b[a-zA-Z]{3,}\b", clean_q)]
        collected_synonyms = [f"Clinical evaluation of {t}" for t in tokens[:3]]
        is_common = False
    
    # Assemble augmented hybrid query
    synonym_suffix = " ".join(collected_synonyms[:4])
    augmented = f"{clean_q} {synonym_suffix}".strip()
    
    return ExpandedClinicalQuery(
        original_intent=clean_q,
        clinical_synonyms=collected_synonyms,
        is_common_ailment=is_common,
        augmented_query=augmented
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
    (r"\b(panic disorder|panic attack|panic attacks|agoraphobia)\b", "Panic Disorder & Agoraphobia"),
    (r"\b(anxiety|generalized anxiety|chronic anxiety|gad|nervousness)\b", "Generalized Anxiety Disorder (GAD)"),
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
    Deconstructs the raw query, maps layperson terminology to scientific clinical standards,
    extracts entities, runs NegEx negation / acronym expansion, and detects missing clinical parameters.
    """
    expanded_query = expand_layperson_query(query)
    entities = extract_clinical_entities(query)

    # Invoke Clinical NLP Engine for deep negation, intent, and morphology analysis
    nlp_dict = None
    try:
        from app.services.clinical_nlp import clinical_nlp
        nlp_res = clinical_nlp.process(query)
        nlp_dict = nlp_res.model_dump()
        
        # Merge extracted medications and metrics if not already present
        for med in nlp_res.medications_and_doses:
            med_str = f"{med['drug']} ({med['regimen']})"
            if med_str not in entities.interventions:
                entities.interventions.append(med_str)
        for met_k, met_v in nlp_res.clinical_metrics.items():
            if met_k not in entities.clinical_metrics:
                entities.clinical_metrics[met_k] = met_v
    except Exception as e:
        pass
    
    # If primary condition was not matched by strict patterns, derive from clinical synonyms
    if not entities.primary_condition and expanded_query.clinical_synonyms:
        entities.primary_condition = expanded_query.clinical_synonyms[0]

    missing_vars, context_gaps, clarifications = detect_missing_variables_and_gaps(query, entities)

    requires_disambiguation = len(missing_vars) > 0 or len(context_gaps) > 0

    return ParsedQueryAnalysis(
        raw_query=query,
        entities=entities,
        expanded_query=expanded_query,
        missing_variables=missing_vars,
        context_gaps=context_gaps,
        requires_disambiguation=requires_disambiguation,
        recommended_clarifications=clarifications,
        nlp_analysis=nlp_dict,
    )


