"""
AegisMed Clinical Disease Metadata Dictionary
Provides clinical ICD-10 codes, granular symptoms, first-line & second-line pharmacological solutions,
and clinical trial details for the 100 landmark conditions.
"""

from typing import Dict, Any, List

DISEASE_METADATA: Dict[str, Dict[str, Any]] = {
    "DOC-CARD-001": {
        "icd10": "I10",
        "severity": "Moderate",
        "symptoms": [
            {"name": "Occipital morning headache", "frequency": "occasional", "severity": "mild", "description": "Dull ache at the base of the skull upon waking, often resolving after several hours."},
            {"name": "Dizziness / Lightheadedness", "frequency": "occasional", "severity": "mild", "description": "Transient unsteadiness, particularly upon standing or rapid posture changes."},
            {"name": "Facial flushing", "frequency": "occasional", "severity": "mild", "description": "Warmth and erythema of cheeks and neck during acute blood pressure surges."},
            {"name": "Blurred vision", "frequency": "rare", "severity": "moderate", "description": "Intermittent visual haziness during hypertensive spikes due to retinal vascular tone changes."},
            {"name": "Epistaxis (Nosebleeds)", "frequency": "rare", "severity": "moderate", "description": "Spontaneous bleeding from fragile nasal mucosal vessels under high vascular pressure."},
            {"name": "Asymptomatic elevation", "frequency": "hallmark", "severity": "mild", "description": "Often completely silent ('silent killer') with no overt warning signs until target-organ damage occurs."}
        ],
        "solutions": [
            {
                "id": "SOL-CARD-001-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Thiazide Diuretics (Chlorthalidone / Hydrochlorothiazide)",
                "description": "Inhibits sodium and chloride reabsorption in the distal convoluted tubule, reducing extracellular fluid volume and peripheral vascular resistance.",
                "dosage_or_protocol": "Chlorthalidone 12.5–25 mg orally once daily in the morning; or HCTZ 25–50 mg once daily.",
                "contraindications": ["Anuria", "Hypokalemia", "Hyponatremia", "Severe renal impairment (eGFR <30 mL/min for HCTZ)"],
                "side_effects": ["Hypokalemia", "Hyperuricemia / gout precipitation", "Hyponatremia", "Hyperglycemia"],
                "monitoring": "Basic metabolic panel (BMP) checking serum potassium, sodium, and creatinine at 2–4 weeks."
            },
            {
                "id": "SOL-CARD-001-P2",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "ACE Inhibitors (Lisinopril / Enalapril) or ARBs (Losartan / Valsartan)",
                "description": "Blocks renin-angiotensin-aldosterone system (RAAS), preventing angiotensin II-mediated vasoconstriction and aldosterone release. Preferred in diabetes or CKD with proteinuria.",
                "dosage_or_protocol": "Lisinopril 10–40 mg once daily; or Losartan 50–100 mg once daily.",
                "contraindications": ["History of ACEi-induced angioedema", "Pregnancy (Black Box Warning)", "Bilateral renal artery stenosis"],
                "side_effects": ["Dry cough (ACEi ~10%)", "Hyperkalemia", "Hypotension", "Acute decline in GFR"],
                "monitoring": "Serum creatinine and potassium 2–4 weeks post-initiation; hold if potassium >5.5 mEq/L."
            },
            {
                "id": "SOL-CARD-001-P3",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Dihydropyridine Calcium Channel Blockers (Amlodipine)",
                "description": "Inhibits L-type calcium channels on vascular smooth muscle cells, causing potent peripheral arterial vasodilation and afterload reduction.",
                "dosage_or_protocol": "Amlodipine 2.5–10 mg orally once daily.",
                "contraindications": ["Severe aortic stenosis", "Cardiogenic shock"],
                "side_effects": ["Peripheral dependent ankle edema", "Headache", "Reflex flushing", "Gingival hyperplasia"],
                "monitoring": "Assess lower extremity edema at routine follow-up."
            },
            {
                "id": "SOL-CARD-001-L1",
                "type": "lifestyle",
                "line_of_therapy": "first_line",
                "name": "DASH Nutritional Pattern & Dietary Sodium Reduction",
                "description": "Diet rich in fruits, vegetables, whole grains, and low-fat dairy with reduced saturated fat and cholesterol. Restrict sodium to <1,500 mg/day (or at least 1,000 mg/day reduction).",
                "dosage_or_protocol": "Daily dietary adherence yields ~11 mmHg SBP reduction in hypertensive adults; 90–150 min/week moderate aerobic exercise.",
                "contraindications": [],
                "side_effects": [],
                "monitoring": "Standardized home blood pressure monitoring (HBPM) 2 morning and 2 evening readings for 7 days."
            }
        ]
    },
    "DOC-CARD-002": {
        "icd10": "I50.2",
        "severity": "Severe",
        "symptoms": [
            {"name": "Dyspnea on exertion", "frequency": "hallmark", "severity": "severe", "description": "Breathlessness during physical effort due to pulmonary venous congestion and inadequate cardiac output reserve."},
            {"name": "Orthopnea", "frequency": "hallmark", "severity": "severe", "description": "Inability to lie flat without progressive breathlessness; requires 2 or more pillows for sleep."},
            {"name": "Paroxysmal nocturnal dyspnea (PND)", "frequency": "common", "severity": "severe", "description": "Waking from sleep gasping for air 1–2 hours after recumbency as peripheral edema fluid re-enters circulatory volume."},
            {"name": "Bilateral lower extremity edema", "frequency": "common", "severity": "moderate", "description": "Dependent pitting edema around ankles and pretibial areas from systemic venous hypertension."},
            {"name": "Fatigue and weakness", "frequency": "common", "severity": "moderate", "description": "Profound generalized physical exhaustion due to low forward systemic perfusion."},
            {"name": "Nocturnal dry cough", "frequency": "occasional", "severity": "mild", "description": "Persistent dry wheezing cough when recumbent due to pulmonary capillary engorgement."}
        ],
        "solutions": [
            {
                "id": "SOL-CARD-002-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "ARNI (Sacubitril/Valsartan - Entresto)",
                "description": "Neprilysin inhibitor combined with angiotensin receptor blocker. Enhances natriuretic peptide system while inhibiting RAAS. Foundational Pillar 1 of GDMT.",
                "dosage_or_protocol": "Initial 49/51 mg PO BID (or 24/26 mg BID if low baseline BP/eGFR), titrating every 2–4 weeks to target 97/103 mg PO BID.",
                "contraindications": ["Concurrent ACE inhibitor within 36 hours (angioedema risk)", "History of hereditary/idiopathic angioedema", "Pregnancy"],
                "side_effects": ["Hypotension", "Hyperkalemia", "Renal impairment", "Angioedema"],
                "monitoring": "Blood pressure, serum potassium, and renal function (eGFR) at 1–2 weeks following initiation."
            },
            {
                "id": "SOL-CARD-002-P2",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Evidence-Based Beta-Blockers (Carvedilol / Metoprolol Succinate / Bisoprolol)",
                "description": "Blunts chronic toxic sympathetic overactivation, reverses LV remodeling, reduces heart rate, and lowers sudden cardiac death. Foundational Pillar 2.",
                "dosage_or_protocol": "Carvedilol starting 3.125 mg BID, doubling every 2 weeks to target 25–50 mg BID; or Metoprolol Succinate ER 25–200 mg daily.",
                "contraindications": ["Acute decompensated heart failure with overt fluid overload", "Second- or third-degree AV block", "Severe active bronchospasm"],
                "side_effects": ["Bradycardia", "Transient fluid retention during titration", "Fatigue", "Hypotension"],
                "monitoring": "Heart rate (target resting 60–70 bpm) and daily morning weights."
            },
            {
                "id": "SOL-CARD-002-P3",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Mineralocorticoid Receptor Antagonists (Spironolactone / Eplerenone)",
                "description": "Blocks aldosterone binding at renal and cardiovascular receptors, reducing myocardial fibrosis and potassium wasting. Foundational Pillar 3.",
                "dosage_or_protocol": "Spironolactone 12.5–25 mg daily, titrating to 50 mg daily as tolerated.",
                "contraindications": ["eGFR <30 mL/min/1.73m²", "Serum potassium >5.0 mEq/L"],
                "side_effects": ["Hyperkalemia", "Gynecomastia / breast tenderness (spironolactone)", "Mild renal dysfunction"],
                "monitoring": "Check potassium and creatinine at 1, 4, and 12 weeks, then semi-annually."
            },
            {
                "id": "SOL-CARD-002-P4",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "SGLT2 Inhibitors (Dapagliflozin / Empagliflozin)",
                "description": "Promotes osmotic diuresis, improves myocardial energetics, and lowers cardiac preload and afterload independent of diabetes status. Foundational Pillar 4.",
                "dosage_or_protocol": "Dapagliflozin 10 mg once daily; or Empagliflozin 10 mg once daily.",
                "contraindications": ["Type 1 diabetes without specialist protocol (euglycemic DKA risk)", "Dialysis or eGFR <20 mL/min"],
                "side_effects": ["Genitourinary mycotic infections", "Mild volume depletion", "Rare euglycemic DKA"],
                "monitoring": "Volume status and glycemic parameters if co-administered with sulfonylureas/insulin."
            }
        ]
    },
    "DOC-CARD-003": {
        "icd10": "I48.91",
        "severity": "Severe",
        "symptoms": [
            {"name": "Palpitations / Fluttering heartbeat", "frequency": "hallmark", "severity": "moderate", "description": "Irregular, rapid sensation of skipping beats or fluttering in the chest."},
            {"name": "Exertional dyspnea", "frequency": "common", "severity": "moderate", "description": "Shortness of breath with minimal activity due to loss of atrial kick and rapid ventricular response."},
            {"name": "Lightheadedness / Dizziness", "frequency": "common", "severity": "mild", "description": "Cerebral hypoperfusion during rapid ventricular rates or sudden pauses."},
            {"name": "Exercise intolerance", "frequency": "common", "severity": "moderate", "description": "Substantial decrease in physical stamina and early onset exhaustion."},
            {"name": "Chest tightness", "frequency": "occasional", "severity": "moderate", "description": "Discomfort resulting from increased myocardial oxygen demand during tachyarrhythmia."}
        ],
        "solutions": [
            {
                "id": "SOL-CARD-003-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Direct Oral Anticoagulants - DOACs (Apixaban / Rivaroxaban / Dabigatran)",
                "description": "Directly inhibits factor Xa or thrombin, preventing left atrial appendage thrombus formation and ischemic stroke.",
                "dosage_or_protocol": "Apixaban 5 mg orally BID (reduce to 2.5 mg BID if any 2 of: age ≥80, body weight ≤60 kg, serum creatinine ≥1.5 mg/dL).",
                "contraindications": ["Active clinically significant pathological bleeding", "Severe renal impairment (CrCl <15 mL/min)", "Mechanical heart valves"],
                "side_effects": ["Bleeding (GI, epistaxis, hematuria)", "Bruising"],
                "monitoring": "Annual renal function (CrCl via Cockcroft-Gault) and CBC."
            },
            {
                "id": "SOL-CARD-003-P2",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Rate Control Therapy (Metoprolol Succinate / Diltiazem)",
                "description": "AV nodal blocking agents to control ventricular rate at rest (<80–110 bpm) and during exertion.",
                "dosage_or_protocol": "Metoprolol succinate 25–100 mg daily; or Diltiazem CD 120–360 mg daily (avoid diltiazem in HFrEF).",
                "contraindications": ["Decompensated heart failure", "Second/third-degree AV block without pacemaker", "Pre-excitation (WPW syndrome)"],
                "side_effects": ["Bradycardia", "Hypotension", "Fatigue"],
                "monitoring": "Resting and exertional heart rate on ECG or telemetry."
            }
        ]
    },
    "DOC-CARD-007": {
        "icd10": "E11.9",
        "severity": "Chronic",
        "symptoms": [
            {"name": "Polyuria (Frequent urination)", "frequency": "hallmark", "severity": "moderate", "description": "Excessive urination due to osmotic diuresis when blood glucose exceeds renal threshold (~180 mg/dL)."},
            {"name": "Polydipsia (Excessive thirst)", "frequency": "hallmark", "severity": "moderate", "description": "Persistent severe thirst triggered by hypothalamic dehydration signaling."},
            {"name": "Polyphagia (Extreme hunger)", "frequency": "common", "severity": "mild", "description": "Intense hunger despite eating, as glucose is blocked from entering cells due to insulin resistance."},
            {"name": "Unexplained weight loss", "frequency": "occasional", "severity": "moderate", "description": "Loss of body mass as catabolism breaks down glycogen, fat, and muscle stores."},
            {"name": "Blurred vision", "frequency": "common", "severity": "mild", "description": "Osmotic swelling of ocular lens during periods of acute hyperglycemia."},
            {"name": "Peripheral numbness / Tingling (Paresthesias)", "frequency": "common", "severity": "moderate", "description": "Distal symmetric stocking-glove sensory loss from chronic diabetic microvascular neuropathy."}
        ],
        "solutions": [
            {
                "id": "SOL-CARD-007-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Metformin Extended-Release (Biguanide)",
                "description": "Activates AMP-activated protein kinase (AMPK), reducing hepatic gluconeogenesis and improving peripheral insulin sensitivity.",
                "dosage_or_protocol": "500 mg orally once daily with evening meal, titrating by 500 mg weekly to target 2,000 mg daily in divided doses.",
                "contraindications": ["eGFR <30 mL/min/1.73m² (Black Box Warning: Lactic Acidosis)", "Severe hepatic impairment", "Acute metabolic acidosis"],
                "side_effects": ["GI distress (diarrhea, nausea, bloating ~25%)", "Vitamin B12 deficiency with long-term use"],
                "monitoring": "Annual eGFR and serum vitamin B12 levels."
            },
            {
                "id": "SOL-CARD-007-P2",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "GLP-1 Receptor Agonists (Semaglutide / Dulaglutide)",
                "description": "Enhances glucose-dependent insulin secretion, suppresses glucagon, slows gastric emptying, and reduces MACE and progression of CKD.",
                "dosage_or_protocol": "Semaglutide SubQ 0.25 mg weekly x 4 weeks, escalate to 0.5 mg weekly; may increase to 1.0–2.0 mg weekly based on glycemic goals.",
                "contraindications": ["Personal/family history of Medullary Thyroid Carcinoma (MTC)", "Multiple Endocrine Neoplasia syndrome type 2 (MEN 2)"],
                "side_effects": ["Nausea", "Vomiting", "Diarrhea", "Decreased appetite", "Rare acute pancreatitis"],
                "monitoring": "HbA1c quarterly until stable, then semi-annually."
            },
            {
                "id": "SOL-CARD-007-P3",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "SGLT2 Inhibitors (Empagliflozin / Dapagliflozin)",
                "description": "Inhibits sodium-glucose cotransporter 2 in proximal renal tubules, inducing urinary glucose excretion and providing substantial cardiovascular/renal protection.",
                "dosage_or_protocol": "Empagliflozin 10–25 mg orally once daily in the morning.",
                "contraindications": ["End-stage renal disease on dialysis", "Prior euglycemic DKA"],
                "side_effects": ["Mycotic genital infections", "Urinary tract infections", "Orthostatic hypotension"],
                "monitoring": "Renal function and skin integrity of feet."
            }
        ]
    },
    "DOC-PULM-012": {
        "icd10": "J45.9",
        "severity": "Moderate",
        "symptoms": [
            {"name": "Expiratory wheezing", "frequency": "hallmark", "severity": "moderate", "description": "High-pitched musical whistling sounds during expiration caused by turbulent airflow through narrowed airways."},
            {"name": "Chest tightness", "frequency": "common", "severity": "moderate", "description": "Sensation of constriction or pressure around the rib cage due to bronchospasm."},
            {"name": "Dyspnea / Shortness of breath", "frequency": "common", "severity": "moderate", "description": "Episodic breathlessness worsening with exercise, cold air, or viral respiratory infections."},
            {"name": "Nocturnal / Early morning cough", "frequency": "common", "severity": "mild", "description": "Recurrent dry or productive cough, often awakening patient between 3 AM and 5 AM."},
            {"name": "Prolonged expiratory phase", "frequency": "occasional", "severity": "moderate", "description": "Extended time required to fully exhale due to lower airway obstruction."}
        ],
        "solutions": [
            {
                "id": "SOL-PULM-012-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Inhaled Corticosteroid + Formoterol (ICS-Formoterol SMART Regimen)",
                "description": "GINA Track 1 Preferred Strategy: Low-dose ICS (Budesonide) combined with fast-acting LABA (Formoterol) used both as maintenance and as-needed reliever.",
                "dosage_or_protocol": "Budesonide/Formoterol 160/4.5 mcg: 1–2 inhalations daily plus 1 inhalation as needed for relief (max 8–12 puffs/day).",
                "contraindications": ["Primary treatment of status asthmaticus without emergency protocol", "Known hypersensitivity"],
                "side_effects": ["Oral candidiasis (thrush)", "Dysphonia (hoarseness)", "Transient tremor/palpitations"],
                "monitoring": "Rinse mouth thoroughly with water and spit after inhalation. Measure peak expiratory flow (PEF)."
            },
            {
                "id": "SOL-PULM-012-P2",
                "type": "pharmacological",
                "line_of_therapy": "second_line",
                "name": "Leukotriene Receptor Antagonists (Montelukast)",
                "description": "Inhibits cysteinyl leukotriene CysLT1 receptor, blocking airway edema, smooth muscle contraction, and cellular inflammation. Useful in allergic rhinitis comorbidity.",
                "dosage_or_protocol": "10 mg orally once daily in the evening.",
                "contraindications": ["Hypersensitivity"],
                "side_effects": ["Neuropsychiatric events (mood changes, vivid dreams, suicidal ideation - FDA Black Box Warning)", "Headache"],
                "monitoring": "Screen for neuropsychiatric symptoms at every clinic visit."
            }
        ]
    },
    "DOC-PULM-013": {
        "icd10": "J44.9",
        "severity": "Severe",
        "symptoms": [
            {"name": "Chronic progressive dyspnea", "frequency": "hallmark", "severity": "severe", "description": "Persistent exertional shortness of breath that worsens gradually over years and persists between exacerbations."},
            {"name": "Chronic productive morning cough", "frequency": "hallmark", "severity": "moderate", "description": "Daily cough producing mucoid or purulent sputum, classically described as 'smoker's cough'."},
            {"name": "Wheezing and chest tightness", "frequency": "common", "severity": "moderate", "description": "Generalized airway narrowing and mucus hypersecretion."},
            {"name": "Barrel chest (Increased AP diameter)", "frequency": "occasional", "severity": "moderate", "description": "Hyperinflation of lungs causing rib cage remodeling and flattened diaphragms."},
            {"name": "Pursed-lip breathing", "frequency": "occasional", "severity": "mild", "description": "Compensatory breathing technique to maintain positive end-expiratory airway pressure."}
        ],
        "solutions": [
            {
                "id": "SOL-PULM-013-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "LAMA / LABA Dual Bronchodilators (Tiotropium + Olodaterol or Umeclidinium + Vilanterol)",
                "description": "GOLD Guidelines Group E/B first-line therapy: Long-acting muscarinic antagonist plus long-acting beta2-agonist provides superior FEV1 improvement and reduces exacerbations vs monotherapy.",
                "dosage_or_protocol": "Tiotropium 5 mcg + Olodaterol 5 mcg (Respimat) 2 puffs once daily; or Umeclidinium 62.5 mcg + Vilanterol 25 mcg (Ellipta) 1 puff once daily.",
                "contraindications": ["Narrow-angle glaucoma (caution)", "Severe urinary retention"],
                "side_effects": ["Dry mouth", "Urinary hesitancy", "Tachycardia", "Nasopharyngitis"],
                "monitoring": "Post-bronchodilator spirometry (FEV1/FVC <0.70 confirms airflow limitation); annual CAT/mMRC symptom score."
            },
            {
                "id": "SOL-PULM-013-L1",
                "type": "lifestyle",
                "line_of_therapy": "first_line",
                "name": "Smoking Cessation Protocol & Pulmonary Rehabilitation",
                "description": "The single most effective intervention to slow the decline of FEV1. Supervised 6–12 week pulmonary rehabilitation program improving exercise capacity and quality of life.",
                "dosage_or_protocol": "Combination nicotine replacement therapy (NRT) or Varenicline; structured aerobic and strength exercise 3 days/week.",
                "contraindications": [],
                "side_effects": [],
                "monitoring": "Exhaled carbon monoxide or smoking abstinence tracking."
            }
        ]
    },
    "DOC-NEUR-025": {
        "icd10": "G43.9",
        "severity": "Moderate",
        "symptoms": [
            {"name": "Unilateral pulsating / Throbbing headache", "frequency": "hallmark", "severity": "severe", "description": "Moderate to severe throbbing pain typically localized to one side of the head, lasting 4–72 hours."},
            {"name": "Photophobia (Light sensitivity)", "frequency": "hallmark", "severity": "moderate", "description": "Heightened discomfort and worsening pain provoked by bright or fluorescent lights."},
            {"name": "Phonophobia (Sound sensitivity)", "frequency": "hallmark", "severity": "moderate", "description": "Intolerance of normal conversational or environmental sounds."},
            {"name": "Nausea and Vomiting", "frequency": "common", "severity": "moderate", "description": "Autonomic dysfunction accompanying pain, often preventing oral medication absorption."},
            {"name": "Visual Aura (Scintillating scotoma)", "frequency": "occasional", "severity": "moderate", "description": "Reversible neurological visual disturbances (flickering zigzag lights, blind spots) developing over 5–20 minutes preceding headache."}
        ],
        "solutions": [
            {
                "id": "SOL-NEUR-025-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Triptans (Sumatriptan / Rizatriptan) + NSAID (Naproxen)",
                "description": "5-HT1B/1D receptor agonist causing cranial vasoconstriction and inhibition of calcitonin gene-related peptide (CGRP) release. Co-administered with naproxen for synergy.",
                "dosage_or_protocol": "Sumatriptan 50–100 mg orally at onset of headache (repeat once after 2 hours if needed, max 200 mg/24h) + Naproxen sodium 500 mg.",
                "contraindications": ["Ischemic heart disease (CAD, prior MI)", "History of stroke / TIA", "Uncontrolled hypertension", "Hemiplegic migraine"],
                "side_effects": ["Chest tightness / heaviness (triptan sensations)", "Flushing", "Drowsiness", "Paresthesias"],
                "monitoring": "Limit acute triptan use to ≤9 days per month to prevent Medication Overuse Headache (MOH)."
            },
            {
                "id": "SOL-NEUR-025-P2",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "CGRP Antagonists (Gepants - Rimegepant / Ubrogepant) or Monoclonal Antibodies",
                "description": "Small-molecule CGRP receptor antagonists for acute attack termination without vasoconstrictive contraindications. Safe in vascular disease.",
                "dosage_or_protocol": "Rimegepant 75 mg orally dissolving tablet (ODT) at headache onset.",
                "contraindications": ["Concomitant strong CYP3A4 inhibitors"],
                "side_effects": ["Nausea", "Somnolence", "Dry mouth"],
                "monitoring": "Monthly migraine headache day (MHD) diary."
            }
        ]
    },
    "DOC-PSYC-023": {
        "icd10": "F32.9",
        "severity": "Severe",
        "symptoms": [
            {"name": "Depressed mood", "frequency": "hallmark", "severity": "severe", "description": "Persistent sadness, emptiness, or hopelessness present most of the day, nearly every day for ≥2 weeks."},
            {"name": "Anhedonia", "frequency": "hallmark", "severity": "severe", "description": "Marked loss of interest or pleasure in all or almost all activities previously enjoyed."},
            {"name": "Sleep disturbance (Insomnia or Hypersomnia)", "frequency": "common", "severity": "moderate", "description": "Classically middle-of-the-night or terminal early morning awakening with inability to return to sleep."},
            {"name": "Psychomotor agitation or retardation", "frequency": "common", "severity": "moderate", "description": "Observable slowing of speech and movement or severe pacing and restlessness."},
            {"name": "Fatigue / Loss of energy", "frequency": "common", "severity": "moderate", "description": "Sustained depletion of vitality even without physical exertion."},
            {"name": "Feelings of worthlessness or excessive guilt", "frequency": "common", "severity": "severe", "description": "Unwarranted self-reproach or delusional feelings of failure."}
        ],
        "solutions": [
            {
                "id": "SOL-PSYC-023-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Selective Serotonin Reuptake Inhibitors - SSRIs (Escitalopram / Sertraline)",
                "description": "Selectively blocks serotonin transporter (SERT), increasing synaptic serotonin availability and stimulating downstream neurogenesis (BDNF).",
                "dosage_or_protocol": "Escitalopram starting 10 mg PO daily, titrating to 20 mg daily after 2–4 weeks; or Sertraline 50–200 mg daily.",
                "contraindications": ["Concurrent MAOIs (within 14 days, risk of fatal Serotonin Syndrome)", "Hypersensitivity"],
                "side_effects": ["Nausea and GI upset (transient ~1–2 weeks)", "Sexual dysfunction (decreased libido, anorgasmia ~30–40%)", "Insomnia/somnolence", "Black Box Warning: Increased suicidal thoughts in age <25 during early therapy"],
                "monitoring": "PHQ-9 score assessment at baseline, 2 weeks, 4 weeks, and 8 weeks; close monitoring of suicidal ideation."
            },
            {
                "id": "SOL-PSYC-023-P2",
                "type": "non_pharmacological",
                "line_of_therapy": "first_line",
                "name": "Cognitive Behavioral Therapy (CBT)",
                "description": "Structured psychotherapy focusing on identifying and modifying negative cognitive distortions and behavioral activation.",
                "dosage_or_protocol": "12–16 weekly 50-minute individual sessions with certified clinical psychologist or psychiatrist.",
                "contraindications": [],
                "side_effects": [],
                "monitoring": "Symptom remission tracking via validated depression inventories (PHQ-9, MADRS)."
            }
        ]
    },
    "DOC-INF-041": {
        "icd10": "U07.1",
        "severity": "Moderate",
        "symptoms": [
            {"name": "Fever and Chills", "frequency": "hallmark", "severity": "moderate", "description": "Core body temperature elevation accompanied by rigors and diaphoresis."},
            {"name": "Dry persistent cough", "frequency": "hallmark", "severity": "moderate", "description": "Nonproductive paroxysmal hacking cough due to bronchial mucosal irritation."},
            {"name": "Anosmia & Ageusia", "frequency": "common", "severity": "mild", "description": "Sudden total loss or alteration of smell and taste sensations."},
            {"name": "Profound fatigue & Myalgias", "frequency": "common", "severity": "moderate", "description": "Generalized muscle aches, soreness, and overwhelming physical fatigue."},
            {"name": "Sore throat & Nasal congestion", "frequency": "common", "severity": "mild", "description": "Upper respiratory catarrhal symptoms."},
            {"name": "Dyspnea / Shortness of breath", "frequency": "occasional", "severity": "severe", "description": "Difficulty catching breath; sign of lower respiratory tract infection or viral pneumonitis."}
        ],
        "solutions": [
            {
                "id": "SOL-INF-041-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Nirmatrelvir / Ritonavir (Paxlovid)",
                "description": "SARS-CoV-2 main protease (Mpro / 3CLpro) inhibitor co-packaged with ritonavir as a CYP3A4 pharmacokinetic booster to maintain therapeutic nirmatrelvir blood levels.",
                "dosage_or_protocol": "Nirmatrelvir 300 mg (two 150 mg tablets) plus Ritonavir 100 mg (one 100 mg tablet) orally twice daily for 5 consecutive days, initiated within 5 days of symptom onset.",
                "contraindications": ["Severe renal impairment (eGFR <30 mL/min)", "Severe hepatic impairment (Child-Pugh Class C)", "Co-administration with drugs highly dependent on CYP3A4 clearance (e.g., Amiodarone, Simvastatin, Lovastatin, Carbamazepine, Rifampin)"],
                "side_effects": ["Dysgeusia (metallic/bitter taste ~6%)", "Diarrhea", "Hypertension", "Rebound COVID-19 symptoms in 2–5%"],
                "monitoring": "Comprehensive drug interaction screening before prescribing; renal function assessment (reduce nirmatrelvir to 150 mg BID if eGFR 30–59 mL/min)."
            },
            {
                "id": "SOL-INF-041-P2",
                "type": "pharmacological",
                "line_of_therapy": "second_line",
                "name": "Intravenous Remdesivir (Veklury - 3-Day Outpatient Protocol)",
                "description": "Nucleotide prodrug that inhibits viral RNA-dependent RNA polymerase (RdRp). Preferred alternative when Paxlovid is contraindicated due to severe CYP3A4 drug interactions.",
                "dosage_or_protocol": "200 mg IV on Day 1, followed by 100 mg IV on Days 2 and 3, initiated within 7 days of symptom onset.",
                "contraindications": ["Known hypersensitivity"],
                "side_effects": ["Transient transaminase elevation (ALT/AST)", "Nausea", "Headache"],
                "monitoring": "Baseline hepatic and renal panels."
            }
        ]
    },
    "DOC-GAST-019": {
        "icd10": "K21.9",
        "severity": "Mild",
        "symptoms": [
            {"name": "Pyrosis (Heartburn)", "frequency": "hallmark", "severity": "moderate", "description": "Retrosternal burning sensation radiating upwards toward the neck and throat, exacerbated by bending over or lying recumbent."},
            {"name": "Acid regurgitation", "frequency": "hallmark", "severity": "moderate", "description": "Effortless reflux of sour or bitter gastric contents into the pharynx or mouth."},
            {"name": "Dysphagia", "frequency": "occasional", "severity": "moderate", "description": "Difficulty swallowing, requiring endoscopic evaluation to rule out peptic stricture or malignancy."},
            {"name": "Chronic dry cough & Hoarseness", "frequency": "occasional", "severity": "mild", "description": "Extraesophageal reflux manifesting as laryngeal irritation and nocturnal coughing spells."},
            {"name": "Globus sensation", "frequency": "occasional", "severity": "mild", "description": "Persistent feeling of a lump in the throat without physical obstruction."}
        ],
        "solutions": [
            {
                "id": "SOL-GAST-019-P1",
                "type": "pharmacological",
                "line_of_therapy": "first_line",
                "name": "Proton Pump Inhibitors - PPIs (Omeprazole / Pantoprazole)",
                "description": "Irreversibly inhibits H+/K+ ATPase enzyme system in gastric parietal cells, providing potent and prolonged acid suppression to heal reflux esophagitis.",
                "dosage_or_protocol": "Omeprazole 20–40 mg orally once daily taken 30–60 minutes before the first meal of the day for 4–8 weeks.",
                "contraindications": ["Hypersensitivity to substituted benzimidazoles"],
                "side_effects": ["Headache", "Abdominal discomfort", "Long-term risk of hypomagnesemia, vitamin B12 deficiency, bone fracture risk, and C. difficile infection"],
                "monitoring": "Re-evaluate need for continued therapy at 8 weeks; step down to H2RA or as-needed therapy if symptoms resolved."
            },
            {
                "id": "SOL-GAST-019-L1",
                "type": "lifestyle",
                "line_of_therapy": "first_line",
                "name": "Anti-Reflux Postural & Dietary Modifications",
                "description": "Elevate head of bed by 6 inches (using bed risers or wedge pillow); avoid eating within 3 hours of reclining; weight reduction; avoid trigger foods (caffeine, chocolate, peppermint, high-fat foods).",
                "dosage_or_protocol": "Continuous daily behavioral maintenance.",
                "contraindications": [],
                "side_effects": [],
                "monitoring": "Symptom diary review."
            }
        ]
    }
}
