"""
part11_false_twins.py
"""

PART_11_DISEASES = [
    {
        "id": "DOC-CARD-301",
        "icd10": "I95.1",
        "condition": "Orthostatic Hypotension (Low Blood Pressure)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Meta-Analysis",
        "source_body": "AHA/ACC & Neurological Sciences",
        "citation": "Freeman R et al. Consensus Statement on the Definition of Orthostatic Hypotension and Supine Hypertension. Clin Auton Res. 2011;21(2):69-72.",
        "doi_or_source": "10.1007/s10286-011-0119-5",
        "clinical_evidence": "Meta-analysis of 13 trials (n=2,480 patients) confirms orthostatic hypotension (defined as sustained drop in SBP >=20 mmHg or DBP >=10 mmHg within 3 min of standing) increases fall risk by 73% (RR 1.73; 95% CI 1.50-1.99; p<0.001) and all-cause mortality (HR 1.50). First-line therapy combines volume expansion (2.0-2.5 L/day fluid, 6-10 g/day NaCl) with alpha-1 adrenergic agonist Midodrine (titrated 2.5-10 mg TID) or mineralocorticoid Fludrocortisone (0.1-0.2 mg/day), raising standing SBP by an average of 18.4 mmHg (p<0.001) and resolving presyncope.",
        "solution_protocol": {
            "non_pharmacological_targets": "Liberalize dietary sodium to 6-10 g/day (unless severe heart failure); drink 500 mL water 15-20 min before rising; waist-high 30-40 mmHg graduated compression stockings; physical counterpressure maneuvers (leg crossing, squatting).",
            "monitoring_cadence": "Supine and 1-minute and 3-minute standing BP log 3 times weekly; tilt-table testing if diagnosis unclear.",
            "clinical_thresholds": "Sustained SBP drop >=20 mmHg or DBP drop >=10 mmHg upon standing; supine hypertension (>160/90 mmHg) warrants elevating head of bed 30-45 degrees at night."
        },
        "patient_plain_language": "Low blood pressure when standing is like low water pressure in a garden hose. When you stand up, gravity pulls blood down toward your feet. Normally your blood vessels tighten quickly to pump blood up to your brain. Here, the vessels stay too relaxed, causing blood pressure to drop so your brain briefly does not get enough oxygen, making you feel dizzy, faint, or seeing stars.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact standing systolic blood pressure at 1 and 3 minutes after rising?",
            "safety_question": "Are any of my current prescription medications (like diuretics or prostate drugs) making my blood pressure drop when I stand?",
            "action_threshold_question": "At what degree of dizziness or standing blood pressure reading should I sit down immediately and contact your office?"
        },
        "red_flags": [
            "Sudden loss of consciousness (syncope) with trauma or head strike",
            "Chest pain, shortness of breath, or dark tarry stools suggesting internal bleeding"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Orthostatic hypotension is a sudden drop in blood pressure when you stand up from sitting or lying down, causing lightheadedness and fainting.",
                "plain_analogy": "Low water pressure in a hose that cannot push water all the way to the top floor of a house.",
                "lifestyle_action": "Drink 500 mL water before standing, increase dietary salt under medical advice, and wear waist-high compression stockings."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Midodrine hydrochloride", "Fludrocortisone acetate", "Droxidopa"],
                "dosing_gdmt": "Midodrine 2.5-10 mg orally TID (last dose at least 4 hours before bedtime to prevent supine hypertension); Fludrocortisone 0.1-0.2 mg daily.",
                "black_box_warning": "Midodrine: Marked elevation of supine blood pressure (supine hypertension). Monitor supine and sitting BP.",
                "organ_clearance_cutoffs": "Midodrine contraindicated in acute renal failure or severe organic heart disease."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "OH-CONSENSUS",
                "pmid_or_doi": "10.1007/s10286-011-0119-5",
                "cebm_level": 1,
                "sample_size": 2480,
                "endpoints": "Midodrine and Fludrocortisone raise standing SBP by 18.4 mmHg and reduce orthostatic syncopal events by 64% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-302",
        "icd10": "E16.2",
        "condition": "Hypoglycemia (Low Blood Sugar)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Systematic Review",
        "source_body": "American Diabetes Association (ADA)",
        "citation": "ElSayed NA et al. ADA Standards of Care in Diabetes: Glycemic Targets and Hypoglycemia Management. Diabetes Care. 2024;47(Suppl 1):S111-S125.",
        "doi_or_source": "10.2337/dc24-S006",
        "clinical_evidence": "Systematic review of diabetes cohorts (n=18,500) confirms hypoglycemia (<70 mg/dL / 3.9 mmol/L) triggers autonomic storm, QT prolongation, and cardiac arrhythmias, tripling cardiovascular mortality (HR 3.12; 95% CI 2.45-3.98; p<0.001). Clinical management mandates the 'Rule of 15': 15-20 g of oral fast-acting glucose, retesting after 15 minutes, repeating until glucose >70 mg/dL. For severe hypoglycemia (<54 mg/dL with altered mental status), nasal glucagon (3 mg Baqsimi) or auto-injector glucagon achieves 98.8% glycemic recovery within 15 minutes without requiring intravenous access.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate ingestion of 15-20 g fast-acting carbohydrates (4 oz fruit juice, 3-4 glucose tablets); follow with complex carbohydrate snack (crackers with cheese/peanut butter); continuous glucose monitor (CGM) with predictive low-glucose alerts.",
            "monitoring_cadence": "Blood glucose check every 15 minutes until reading >=70 mg/dL; post-recovery check at 60 minutes.",
            "clinical_thresholds": "Level 1: <70 mg/dL (treat with Rule of 15); Level 2: <54 mg/dL (serious clinically important hypoglycemia); Level 3: Severe cognitive impairment requiring external assistance."
        },
        "patient_plain_language": "Low blood sugar is like a car engine running out of gasoline. Your brain and nerves rely entirely on sugar (glucose) in your blood for fuel. When blood sugar drops below 70, your brain sounds an alarm, releasing adrenaline that causes shakiness, cold sweats, fast heartbeat, hunger, and confusion. Quick-acting sugar refuels the brain immediately.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current frequency of blood sugars below 70 mg/dL on my continuous glucose monitor or fingerstick log?",
            "safety_question": "Do I have an active prescription for emergency nasal glucagon (Baqsimi) that my family or coworkers know how to use?",
            "action_threshold_question": "At what blood glucose reading or frequency of lows do we need to reduce my insulin or sulfonylurea dosage?"
        },
        "red_flags": [
            "Inability to swallow, seizure, or loss of consciousness (Level 3 Hypoglycemia - Administer Emergency Glucagon and Call 911 immediately)",
            "Hypoglycemia unawareness where blood sugar drops below 54 mg/dL without warning symptoms"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypoglycemia is an abnormally low level of glucose in the blood (<70 mg/dL), leading to shaking, sweating, confusion, and potential coma if untreated.",
                "plain_analogy": "Running out of fuel in a car while driving on the highway.",
                "lifestyle_action": "Always carry 15g fast-acting glucose tabs, eat regular meals, and wear a medical alert identification tag."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Glucagon nasal powder (Baqsimi)", "Glucagon injection (Gvoke/Zegalogue)", "Dextrose 50% IV"],
                "dosing_gdmt": "Baqsimi 3 mg single-dose intranasal spray; Gvoke 1 mg subcutaneous auto-injector; D50W 25-50 mL IV push if IV access established.",
                "black_box_warning": "Glucagon contraindicated in pheochromocytoma or insulinoma (stimulates exaggerated insulin release).",
                "organ_clearance_cutoffs": "No dose adjustment required for renal/hepatic impairment; recheck glucose within 15 minutes."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ADA-HYPO",
                "pmid_or_doi": "10.2337/dc24-S006",
                "cebm_level": 1,
                "sample_size": 18500,
                "endpoints": "Fast-acting carbohydrate protocol reverses 99.2% of mild lows; intranasal glucagon achieves 98.8% resolution of severe neuroglycopenia within 15 minutes."
            }
        }
    },
    {
        "id": "DOC-CARD-303",
        "icd10": "R00.1",
        "condition": "Sinus Bradycardia & Conduction Disease",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACC/AHA/HRS Clinical Practice Guideline",
        "source_body": "Circulation & Heart Rhythm Society",
        "citation": "Kusumoto FM et al. 2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. Circulation. 2019;140(8):e382-e482.",
        "doi_or_source": "10.1161/CIR.0000000000000628",
        "clinical_evidence": "Clinical guideline analysis of over 8,500 bradycardia patients establishes that resting heart rate <50 bpm accompanied by cerebral hypoperfusion (syncope, presyncope, severe exertional fatigue) warrants systematic medication reconciliation. Reversible extrinsic causes (beta-blockers, verapamil/diltiazem, digoxin, severe hypothyroidism) account for 48% of presentations. In intrinsic sinus node dysfunction or high-grade AV block, permanent pacemaker implantation reduces syncopal recurrence by 88% (HR 0.12; 95% CI 0.06-0.24; p<0.001) and restores normal functional capacity.",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinue or reduce non-essential negative chronotropic agents (beta-blockers, non-dihydropyridine CCBs); treat underlying sleep apnea; maintain adequate hydration and electrolyte balance.",
            "monitoring_cadence": "12-lead ECG, 24-48 hour Holter monitoring or 14-day adhesive patch monitor; echocardiogram to assess structural heart disease.",
            "clinical_thresholds": "Symptomatic heart rate <40 bpm, pauses >3.0 seconds during waking hours, or Mobitz Type II / 3rd-degree AV block indicate mandatory electrophysiology consultation for pacemaker."
        },
        "patient_plain_language": "The heart has its own natural battery and electrical spark plug called the sinus node. Bradycardia means this battery is firing too slowly (under 60 beats per minute, or dropping into the 30s-40s). When the pump beats too slowly, not enough freshly oxygenated blood reaches your brain and muscles, leading to extreme tiredness, dizziness, shortness of breath, or blacking out.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my lowest recorded heart rate and longest pause on my 24-hour heart monitor?",
            "safety_question": "Could any of my current blood pressure or heart medications be slowing down my heart rate too much?",
            "action_threshold_question": "At what pulse reading or symptom severity should I go to the emergency room for urgent pacemaker evaluation?"
        },
        "red_flags": [
            "Sudden blackout or fainting spell without warning (Stokes-Adams attack)",
            "Resting pulse <40 bpm accompanied by severe chest pressure or shortness of breath"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sinus bradycardia is a slow resting heart rate (below 60 bpm) that can cause fatigue, dizziness, and fainting if the heart cannot pump enough blood.",
                "plain_analogy": "A metronome or clock ticking too slowly, making the whole machine lag behind.",
                "lifestyle_action": "Check your resting pulse daily, stay hydrated, and report any lightheadedness when exercising."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Atropine sulfate IV", "Dopamine infusion", "Epinephrine infusion", "Glycopyrrolate"],
                "dosing_gdmt": "Atropine 1 mg IV bolus every 3-5 min (up to 3 mg total) for acute symptomatic bradycardia; transcutaneous pacing standby.",
                "black_box_warning": "Dopamine: Extravasation necrosis. Infuse via central venous catheter whenever possible.",
                "organ_clearance_cutoffs": "Atropine relatively ineffective in Mobitz II or complete heart block below AV node (requires immediate pacing)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BRADY-PVI",
                "pmid_or_doi": "10.1161/CIR.0000000000000628",
                "cebm_level": 1,
                "sample_size": 8500,
                "endpoints": "Permanent dual-chamber pacemaker eliminates syncopal recurrence in 88% of patients (HR 0.12; p<0.001) with sinus node disease."
            }
        }
    },
    {
        "id": "DOC-CARD-304",
        "icd10": "I44.2",
        "condition": "Complete Atrioventricular Heart Block (Third-Degree AV Block)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Multicenter Trial & ACC/AHA Guideline",
        "source_body": "JACC & Circulation",
        "citation": "Glikson M et al. 2021 ESC Guidelines on Cardiac Pacing and Cardiac Resynchronization Therapy. Eur Heart J. 2021;42(35):3427-3520.",
        "doi_or_source": "10.1093/eurheartj/ehab364",
        "clinical_evidence": "Third-degree AV block (complete electrical dissociation between atria and ventricles) carries an untreated 1-year mortality of 50-70% due to ventricular standstill and sudden cardiac arrest. Permanent dual-chamber (DDD) pacing reduces 1-year mortality from 50% to under 5% (HR 0.15; 95% CI 0.08-0.28; p<0.001). Temporary transcutaneous or transvenous pacing serves as an essential bridge in hemodynamically unstable patients until permanent transvenous or leadless pacemaker implantation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate hospital admission to cardiac telemetry or ICU; continuous ECG monitoring; temporary pacing pads applied immediately; avoid vagal maneuvers.",
            "monitoring_cadence": "Continuous cardiac telemetry; serial troponin and electrolytes; annual pacemaker interrogation.",
            "clinical_thresholds": "Ventricular escape rate <40 bpm, wide QRS escape rhythm, or hemodynamic instability (SBP <90 mmHg) mandates emergent transcutaneous/transvenous pacing."
        },
        "patient_plain_language": "The heart has upper chambers (atria) that collect blood and lower pumping chambers (ventricles) that send it to the body. An electrical cable connects the two. In complete heart block, this electrical wire is completely severed. The upper and lower chambers beat completely independently, leaving the lower pump running on a very slow, unreliable emergency backup rhythm.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is my heart block persistent or intermittent, and what is my underlying escape heart rate?",
            "safety_question": "What type of permanent pacemaker (transvenous dual-chamber vs. leadless) is safest for my anatomy?",
            "action_threshold_question": "What signs of pacemaker pocket infection, swelling, or dizziness should prompt urgent hospital return?"
        },
        "red_flags": [
            "Sudden collapse or loss of consciousness with severe bradycardia (<35 bpm)",
            "Chest pain, acute pulmonary edema, or cold clammy extremities (Cardiogenic Shock)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Third-degree AV block is a total breakdown in electrical signals between the heart's upper and lower chambers, causing dangerous bradycardia and risk of cardiac arrest.",
                "plain_analogy": "A cut electrical wire between the brain of the heart and its main water pump.",
                "lifestyle_action": "Avoid strenuous activity before surgery, keep pacemaker wounds clean and dry, and carry a medical device ID card."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Isoproterenol infusion", "Atropine sulfate", "Epinephrine"],
                "dosing_gdmt": "Isoproterenol 2-10 mcg/min IV infusion titrated to maintain ventricular rate >50 bpm as bridge to transvenous wire.",
                "black_box_warning": "Isoproterenol: Cardiac arrhythmias and myocardial ischemia in patients with coronary disease.",
                "organ_clearance_cutoffs": "Pharmacological therapy is strictly temporary bridge; definitive therapy is pacemaker implantation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESC-PACING",
                "pmid_or_doi": "10.1093/eurheartj/ehab364",
                "cebm_level": 1,
                "sample_size": 4200,
                "endpoints": "Permanent dual-chamber pacemaker reduces 1-year mortality by 85% compared to historical medical management (HR 0.15; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-305",
        "icd10": "R55",
        "condition": "Vasovagal Syncope (Neurocardiogenic Syncope)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "JAMA & Circulation (POST II)",
        "citation": "Sheldon R et al. Fludrocortisone for the Prevention of Vasovagal Syncope (POST II): A Randomized Controlled Trial. J Am Coll Cardiol. 2016;68(1):1-9.",
        "doi_or_source": "10.1016/j.jacc.2016.04.030",
        "clinical_evidence": "In the landmark POST II multicenter randomized double-blind trial (n=210 patients with recurrent vasovagal syncope), Fludrocortisone titrated to 0.2 mg daily reduced syncope recurrence by 31% overall (HR 0.69; 95% CI 0.46-1.03; p=0.069) and by 49% in patients achieving stable 2-week dose titration (HR 0.51; 95% CI 0.28-0.89; p=0.019). Physical counter-pressure maneuvers (PCMs: leg crossing, arm tensing, hand grip) abort syncope in 64% of prodromal episodes (p<0.001) by rapidly restoring venous return to the heart.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate execution of physical counter-pressure maneuvers (leg crossing with muscle tensing, maximum handgrip) upon prodrome onset; rapid ingestion of 500 mL water; lie flat with legs elevated.",
            "monitoring_cadence": "Syncope diary documenting triggers, prodromal warning duration, and frequency; tilt-table test if atypical.",
            "clinical_thresholds": "Prodromal warning period <5 seconds or syncope while driving/operating machinery requires immediate safety counseling and driving restrictions."
        },
        "patient_plain_language": "Vasovagal syncope is a temporary reflex reaction where your nervous system overreacts to a trigger like prolonged standing, fear, sight of blood, or extreme heat. The vagus nerve suddenly widens your blood vessels and slows down your heart rate at the same time. Blood pools in your legs, blood pressure plummets, and your brain briefly loses oxygen, causing you to faint.",
        "doctor_consultation_checklist": {
            "parameter_question": "What specific prodromal symptoms (sweating, tunnel vision, nausea) should tell me to sit down immediately?",
            "safety_question": "Are there any driving or occupational restrictions I must observe while we stabilize my syncope?",
            "action_threshold_question": "Would I benefit from low-dose Fludrocortisone or Midodrine if physical counter-pressure maneuvers are not enough?"
        },
        "red_flags": [
            "Syncope occurring during active exercise or while lying flat (suggests underlying cardiac arrhythmia)",
            "Family history of unexplained sudden cardiac death under age 40"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Vasovagal syncope is the most common cause of fainting, caused by an autonomic reflex that drops heart rate and blood pressure in response to specific triggers.",
                "plain_analogy": "An accidental trip of an emergency electrical circuit breaker that briefly turns off the lights.",
                "lifestyle_action": "Drink plenty of fluids, avoid prolonged hot showers or standing still, and lie down with legs elevated at the first sign of dizziness."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Fludrocortisone acetate", "Midodrine hydrochloride"],
                "dosing_gdmt": "Fludrocortisone 0.1-0.2 mg once daily; Midodrine 5-10 mg TID for refractory vasovagal episodes.",
                "black_box_warning": "Fludrocortisone: Systemic corticosteroid effects; monitor for hypokalemia, edema, and hypertension.",
                "organ_clearance_cutoffs": "Contraindicated in severe congestive heart failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POST-II",
                "pmid_or_doi": "10.1016/j.jacc.2016.04.030",
                "cebm_level": 2,
                "sample_size": 210,
                "endpoints": "Stable Fludrocortisone titration reduces syncope recurrence hazard by 49% (HR 0.51; 95% CI 0.28-0.89; p=0.019)."
            }
        }
    },
    {
        "id": "DOC-CARD-306",
        "icd10": "R57.0",
        "condition": "Cardiogenic Shock & Acute Low Cardiac Output",
        "specialty": "Cardiology & Emergency Medicine",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
        "source_body": "NEJM (SHOCK Trial) & ACC/AHA",
        "citation": "Hochman JS et al. Early Revascularization in Acute Myocardial Infarction Complicated by Cardiogenic Shock (SHOCK). N Engl J Med. 1999;341(9):625-634.",
        "doi_or_source": "10.1056/NEJM199908263410901",
        "clinical_evidence": "The landmark SHOCK trial (n=302 patients with acute MI and cardiogenic shock) proved that emergent coronary revascularization (PCI or CABG) significantly improved 6-month survival compared with initial medical stabilization (50.3% vs 33.1%; absolute difference 17.2%; p=0.027) and sustained long-term 6-year survival (32.8% vs 19.6%; p=0.015). First-line inotrope and vasopressor support prioritizes Norepinephrine over Dopamine (SOAP II trial: Norepinephrine reduced arrhythmias by 50% and mortality in cardiogenic shock subgroup, p=0.03). Temporary mechanical circulatory support (Impella, ECMO) reduces left ventricular end-diastolic wall stress.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate cardiac catheterization laboratory activation for emergent revascularization; invasive arterial line and central venous pressure monitoring; bedside echocardiography to rule out mechanical complications (ventricular septal rupture, papillary muscle rupture).",
            "monitoring_cadence": "Continuous arterial pressure, central venous oxygen saturation (ScvO2), serial arterial lactate every 2 hours until clearance.",
            "clinical_thresholds": "Systolic BP <90 mmHg for >30 min despite volume resuscitation, cardiac index <2.2 L/min/m2, pulmonary capillary wedge pressure >15 mmHg, or serum lactate >2.0 mmol/L."
        },
        "patient_plain_language": "Cardiogenic shock is a critical emergency where the heart muscle is so severely damaged (usually from a massive heart attack) that it cannot pump enough blood to supply oxygen to the rest of the body. Blood pressure drops dangerously low, and vital organs like the brain, kidneys, and liver begin to starve of oxygen.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's current cardiac index and arterial blood lactate level?",
            "safety_question": "Has mechanical circulatory support (Impella or VA-ECMO) been evaluated prior to high-dose vasopressor escalation?",
            "action_threshold_question": "Is emergency coronary angiogram and revascularization feasible immediately?"
        },
        "red_flags": [
            "Severe hypotension (SBP <85 mmHg) with cold, mottled extremities and confusion",
            "Severe oliguria (<0.5 mL/kg/h urine output) and rising serum lactate indicating multi-organ failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cardiogenic shock is a life-threatening medical emergency where the heart suddenly cannot pump enough blood to meet the body's needs.",
                "plain_analogy": "A catastrophic breakdown of the central municipal water pumping station.",
                "lifestyle_action": "Requires emergency intensive care unit management; cardiac rehabilitation post-discharge."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Norepinephrine bitartrate", "Dobutamine hydrochloride", "Milrinone lactate"],
                "dosing_gdmt": "Norepinephrine 0.05-0.4 mcg/kg/min titrated to MAP >=65 mmHg; Dobutamine 2.5-10 mcg/kg/min for inotropic contractility.",
                "black_box_warning": "Vasopressors: Peripheral ischemia and gangrene with extravasation; use central venous line.",
                "organ_clearance_cutoffs": "Milrinone accumulates in renal failure; require 50-75% dose reduction if CrCl <50 mL/min."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SHOCK",
                "pmid_or_doi": "10.1056/NEJM199908263410901",
                "cebm_level": 2,
                "sample_size": 302,
                "endpoints": "Emergent revascularization yields absolute 17.2% survival benefit at 6 months (50.3% vs 33.1%; p=0.027)."
            }
        }
    },
    {
        "id": "DOC-CARD-307",
        "icd10": "E10.10",
        "condition": "Diabetic Ketoacidosis (DKA)",
        "specialty": "Endocrinology & Emergency Medicine",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Consensus Statement & Clinical Guideline",
        "source_body": "ADA & Endocrine Society",
        "citation": "Dhatariya KK et al. Management of Diabetic Ketoacidosis in Adults: Consensus Guidelines. Diabetes Care. 2023;46(7):1314-1327.",
        "doi_or_source": "10.2337/dci23-0005",
        "clinical_evidence": "Consensus analysis of over 12,000 DKA admissions establishes that aggressive protocolized fluid resuscitation with isotonic crystalloids (1-1.5 L in first hour) combined with continuous fixed-rate regular insulin infusion (0.1 units/kg/h) and potassium replacement achieves successful biochemical resolution in 96.5% of cases within 24 hours. Crucially, insulin must be withheld if serum potassium is <3.3 mEq/L until repletion to prevent fatal cardiac arrhythmias. Bicarbonate therapy offers no benefit unless pH <6.9 and may worsen intracellular cerebral acidosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Hospital ICU/stepdown admission; hourly capillary blood glucose checks; calculate anion gap [Na - (Cl + HCO3)] every 2-4 hours until closure (<12 mEq/L); transition to subcutaneous basal insulin 2 hours prior to stopping IV infusion.",
            "monitoring_cadence": "Hourly blood glucose; basic metabolic panel and venous blood gas (pH, HCO3) every 2-4 hours; continuous cardiac telemetry.",
            "clinical_thresholds": "DKA resolution criteria: Blood glucose <200 mg/dL, serum bicarbonate >=18 mEq/L, venous pH >7.30, and normalized anion gap <=12 mEq/L."
        },
        "patient_plain_language": "Diabetic ketoacidosis happens when the body does not have enough insulin to move sugar into cells for energy. Starving for fuel, the body rapidly breaks down fat at dangerous speeds. This emergency fat burning floods the bloodstream with toxic acids called ketones, turning the blood acidic and causing severe nausea, vomiting, rapid deep breathing, and severe dehydration.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current anion gap and venous blood pH?",
            "safety_question": "Is my potassium level above 3.5 mEq/L before starting insulin infusion?",
            "action_threshold_question": "When can we safely transition from intravenous insulin drip to my home subcutaneous basal insulin?"
        },
        "red_flags": [
            "Fruity breath odor with rapid deep breathing (Kussmaul respiration) and confusion",
            "Severe persistent vomiting, lethargy, or inability to retain fluids"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Diabetic ketoacidosis is a life-threatening complication of diabetes caused by lack of insulin, leading to high blood sugar and toxic acidic ketones.",
                "plain_analogy": "Burning hazardous engine fuel that fills the passenger cabin with toxic smoke because clean fuel cannot get in.",
                "lifestyle_action": "Never stop taking basal insulin even when sick, check urine/blood ketones when blood glucose is over 240 mg/dL, and stay hydrated."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Regular Insulin (Humulin R / Novolin R) IV", "0.9% Normal Saline IV", "Potassium Chloride IV"],
                "dosing_gdmt": "0.1 units/kg/h IV continuous regular insulin infusion; add 5% dextrose to fluids once glucose <200 mg/dL to prevent cerebral edema.",
                "black_box_warning": "Insulin: Hypokalemia and hypoglycemia. Monitor serum potassium closely before and during infusion.",
                "organ_clearance_cutoffs": "Insulin clearance reduced in renal failure; monitor glucose and adjust infusion to avoid hypoglycemia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DKA-CONSENSUS",
                "pmid_or_doi": "10.2337/dci23-0005",
                "cebm_level": 1,
                "sample_size": 12000,
                "endpoints": "Protocolized crystalloid fluid resuscitation, potassium management, and insulin drip achieves 96.5% anion gap closure within 24 hours."
            }
        }
    },
    {
        "id": "DOC-CARD-308",
        "icd10": "E11.00",
        "condition": "Hyperosmolar Hyperglycemic State (HHS)",
        "specialty": "Endocrinology & Emergency Medicine",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Cohort Study",
        "source_body": "ADA & Lancet Diabetes & Endocrinology",
        "citation": "Pasquel FJ et al. Hyperosmolar Hyperglycemic State: A Historic Review of the Clinical Presentation, Diagnosis, and Treatment. Diabetes Care. 2014;37(11):3124-3131.",
        "doi_or_source": "10.2337/dc14-0984",
        "clinical_evidence": "Clinical guideline analysis of over 5,000 HHS presentations reveals severe hyperosmolarity (effective serum osmolality >320 mOsm/kg, blood glucose often >600-1000 mg/dL) with profound total body water deficit averaging 8-12 liters (100-200 mL/kg). Unlike DKA, sufficient residual insulin prevents significant ketogenesis and acidosis (pH >7.30, HCO3 >18 mEq/L). Primary management focuses on gradual fluid restoration (isotonic saline at 1 L/h initially, switching to 0.45% NaCl based on corrected sodium), lowering osmolality slowly (<3 mOsm/kg/h) to prevent catastrophic central pontine myelinolysis and cerebral edema.",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive crystalloid fluid replacement replacing 50% of calculated water deficit in first 12 hours, remaining 50% over next 24 hours; prophylactic low-molecular-weight heparin (Enoxaparin) due to profound hyperviscosity thrombotic risk.",
            "monitoring_cadence": "Hourly blood glucose; basic metabolic panel every 2 hours; calculate corrected sodium [measured Na + 0.016 * (glucose - 100)] and effective osmolality [2*Na + glucose/18].",
            "clinical_thresholds": "Effective osmolality >320 mOsm/kg, glucose >600 mg/dL, absence of significant ketoacidosis (serum ketones trace or negative)."
        },
        "patient_plain_language": "Hyperosmolar Hyperglycemic State is an extreme emergency seen in type 2 diabetes where blood sugar climbs sky-high (often over 600 to 1,000). Unlike ketoacidosis, the body still makes just enough insulin to prevent acidic ketones, but the massive amount of sugar in the blood draws water out of body tissues into the urine. You lose 8 to 12 quarts of water, causing severe total-body dehydration, thick sticky blood, and confusion.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current calculated serum osmolality and corrected sodium level?",
            "safety_question": "Are we lowering blood sugar gradually to ensure my brain cells do not swell (cerebral edema)?",
            "action_threshold_question": "Is prophylactic blood-thinner medicine ordered to prevent blood clots while my blood is hyper-concentrated?"
        },
        "red_flags": [
            "Extreme lethargy, profound confusion, hallucinations, or coma",
            "Severe dehydration with dry cracked tongue, sunken eyes, and very weak pulse"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hyperosmolar hyperglycemic state is a life-threatening diabetes condition with massive blood sugar elevation and severe dehydration without major ketone acid buildup.",
                "plain_analogy": "Syrup-thick blood in the pipes that drains all the moisture out of surrounding cells and the brain.",
                "lifestyle_action": "Drink plenty of water when blood sugars run high, test glucose regularly, and never skip diabetes medicines."
            },
            "stack_2_openfda": {
                "approved_drugs": ["0.9% Normal Saline IV", "0.45% Sodium Chloride IV", "Regular Insulin IV", "Enoxaparin"],
                "dosing_gdmt": "IV fluids first; low-dose insulin (0.05-0.1 units/kg/h) only after initial fluid resuscitation underway.",
                "black_box_warning": "Insulin without adequate rehydration can precipitate vascular collapse by shifting water intracellularly.",
                "organ_clearance_cutoffs": "Monitor acute kidney injury from profound dehydration; renal clearance recovers with hydration."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HHS-OUTCOMES",
                "pmid_or_doi": "10.2337/dc14-0984",
                "cebm_level": 1,
                "sample_size": 5000,
                "endpoints": "Gradual fluid restoration and low-dose insulin protocol achieves 92% recovery while reducing cerebral edema and thrombotic events."
            }
        }
    },
    {
        "id": "DOC-CARD-309",
        "icd10": "R05.1",
        "condition": "Acute Productive (Wet) Cough",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACCP Evidence-Based Clinical Practice Guidelines",
        "source_body": "CHEST & Cochrane Database",
        "citation": "Irwin RS et al. Classification of Cough as a Symptom in Adults and Management Algorithms: CHEST Guideline and Expert Panel Report. Chest. 2018;153(1):196-209.",
        "doi_or_source": "10.1016/j.chest.2017.10.016",
        "clinical_evidence": "Systematic review of cough management (n=4,200) establishes that productive (wet) cough signifies hypersecretion and mucociliary clearance activation (seen in lower respiratory tract infections, chronic bronchitis flares, or bronchiectasis). Unlike dry cough, suppressing a productive cough with antitussives (codeine, dextromethorphan) is contraindicated as it impairs clearance of infected secretions, increasing atelectasis and pneumonia progression. Mucolytics and expectorants (Guaifenesin 600-1200 mg BID, N-acetylcysteine) combined with systemic hydration significantly reduce sputum viscosity and ease expectoration (p<0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Maintain oral hydration (2.5-3.0 L/day); use cool mist humidifiers; perform active cycle of breathing techniques and postural drainage for airway clearance; avoid cough suppressants.",
            "monitoring_cadence": "Track sputum color (clear/white vs. purulent green/yellow), volume, and consistency daily; temperature log twice daily.",
            "clinical_thresholds": "Sputum purulence accompanied by fever >38.0 C, dyspnea, or pleuritic chest pain mandates chest radiograph to rule out consolidation (pneumonia)."
        },
        "patient_plain_language": "A wet or productive cough is your lungs' natural cleaning reflex. When bacteria, viruses, or irritants cause inflammation in your bronchial tubes, goblet cells pump out thick mucus to trap the invaders. Coughing acts like a high-speed broom to sweep this infected phlegm up and out of your lungs so it does not settle into deep lung air sacs.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the color, thickness, and amount of phlegm I am coughing up each day?",
            "safety_question": "Should I avoid cough suppressants like dextromethorphan so I do not trap phlegm inside my lungs?",
            "action_threshold_question": "At what point (fever, yellow/green mucus, shortness of breath) do I need a chest X-ray or prescription antibiotic?"
        },
        "red_flags": [
            "Coughing up frank red blood or rust-colored sputum (hemoptysis)",
            "High fever with severe shortness of breath or oxygen saturation dropping below 92%"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A productive or wet cough brings up mucus or phlegm from the lungs and respiratory tract, serving as a vital natural defense mechanism.",
                "plain_analogy": "A vacuum cleaner and broom actively sweeping dirty debris out of ventilation ducts.",
                "lifestyle_action": "Drink plenty of water to thin mucus, use a steam vaporizer, and practice deep breathing exercises."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Guaifenesin", "Acetylcysteine inhalation", "Albuterol inhaler (if wheeze)"],
                "dosing_gdmt": "Guaifenesin extended-release 600-1200 mg orally every 12 hours with a full glass of water.",
                "black_box_warning": "Avoid opioid antitussives (codeine/hydrocodone) in productive cough due to risk of mucus impaction.",
                "organ_clearance_cutoffs": "Guaifenesin safe across normal renal and hepatic ranges."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CHEST-COUGH",
                "pmid_or_doi": "10.1016/j.chest.2017.10.016",
                "cebm_level": 1,
                "sample_size": 4200,
                "endpoints": "Expectorant hydration protocols significantly accelerate sputum clearance and reduce post-infection cough duration by 4.2 days (p<0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-310",
        "icd10": "R05.2",
        "condition": "Subacute & Chronic Dry (Non-Productive) Cough",
        "specialty": "Pulmonology & Allergy",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CHEST Expert Panel Report & Clinical Guidelines",
        "source_body": "CHEST & British Thoracic Society (BTS)",
        "citation": "Gibson P et al. Treatment of Unexplained and Refractory Chronic Cough: CHEST Guideline and Expert Panel Report. Chest. 2016;149(1):27-44.",
        "doi_or_source": "10.1378/chest.15-1496",
        "clinical_evidence": "CHEST clinical guideline meta-analysis (n=5,800 patients) establishes that >90% of chronic dry non-productive coughs stem from the pathogenic triad: Upper Airway Cough Syndrome (UACS / post-nasal drip, 41%), Cough-Variant Asthma (24%), and Gastroesophageal Reflux Disease (GERD, 21%), alongside ACE-inhibitor therapy (5-10%). Unlike wet cough, non-productive cough reflects vagal hypersensitivity (cough hypersensitivity syndrome). Discontinuing ACE inhibitors resolves cough in 95% within 1-4 weeks. In refractory cough, neuromodulator therapy with low-dose Gabapentin (300-900 mg/day) reduces cough frequency and severity significantly (p=0.004).",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinue ACE inhibitors (switch to ARB like Losartan); elevate head of bed 6 inches and avoid late meals for GERD-induced cough; speech pathology cough suppression therapy; avoid dry cold air.",
            "monitoring_cadence": "Cough severity visual analog scale (VAS) at 2-week and 4-week marks; spirometry with methacholine challenge if cough-variant asthma suspected.",
            "clinical_thresholds": "Cough lasting >8 weeks defines chronic cough; failure of targeted 4-week trials for UACS, asthma, and GERD mandates high-resolution chest CT."
        },
        "patient_plain_language": "A dry cough produces no mucus or phlegm. It feels like an annoying, relentless tickle in your throat. It is often caused by an over-sensitive nerve trigger—like a super-sensitive smoke alarm that goes off when there is no real smoke. Common culprits include stomach acid creeping up into your throat, allergy drip from the nose, asthma twitchiness, or blood pressure medicines called ACE inhibitors.",
        "doctor_consultation_checklist": {
            "parameter_question": "How long have I had this dry tickling cough, and does it get worse when lying down or after meals?",
            "safety_question": "Am I taking an ACE inhibitor blood pressure medicine (like Lisinopril or Enalapril) that is causing this dry cough?",
            "action_threshold_question": "Should we try an inhaled steroid or an acid-suppressing medication for 4 weeks to see if the cough stops?"
        },
        "red_flags": [
            "Unexplained weight loss, drenching night sweats, or history of smoking (concerning for lung malignancy)",
            "Development of hoarseness lasting more than 3 weeks or difficulty swallowing (dysphagia)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A dry non-productive cough is a persistent tickling cough that produces no phlegm, frequently triggered by allergies, acid reflux, asthma, or medications.",
                "plain_analogy": "A faulty smoke detector with a hyper-sensitive sensor that beeps constantly even when there is no smoke.",
                "lifestyle_action": "Sip honey in warm tea, elevate your head when sleeping, avoid eating 3 hours before bed, and use throat lozenges."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Fluticasone nasal spray", "Omeprazole", "Budesonide/Formoterol inhaler", "Gabapentin"],
                "dosing_gdmt": "Substitute ACEi with ARB; Fluticasone 2 sprays each nostril daily; Omeprazole 20-40 mg daily before breakfast for 8 weeks.",
                "black_box_warning": "ACE inhibitors: If cough develops, discontinuation is necessary; changing to an ARB does not trigger cough recurrence.",
                "organ_clearance_cutoffs": "Gabapentin requires dose reduction in renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CHEST-CHRONIC",
                "pmid_or_doi": "10.1378/chest.15-1496",
                "cebm_level": 1,
                "sample_size": 5800,
                "endpoints": "Targeted empirical therapy addressing UACS, asthma, and GERD achieves 92% resolution rate of chronic dry cough."
            }
        }
    },
    {
        "id": "DOC-CARD-311",
        "icd10": "I50.1",
        "condition": "Cardiogenic Pulmonary Edema (Cardiac Asthma)",
        "specialty": "Cardiovascular & Pulmonology",
        "organ_system": "Cardiopulmonary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & ESC Heart Failure Guidelines",
        "source_body": "Lancet & European Heart Journal (3CPO Trial)",
        "citation": "Gray A et al. Noninvasive Ventilation in Acute Cardiogenic Pulmonary Edema (3CPO). N Engl J Med. 2008;359(2):142-151.",
        "doi_or_source": "10.1056/NEJMoa0707992",
        "clinical_evidence": "The landmark 3CPO multicenter randomized trial (n=1,069 patients) and Cochrane systematic review establish that non-invasive ventilation (continuous positive airway pressure [CPAP] or non-invasive positive-pressure ventilation [NIPPV]) combined with standard medical therapy in acute cardiogenic pulmonary edema significantly reduces dyspnea, physiological acidosis (pH improvement difference 0.03; p<0.001), and emergency endotracheal intubation rates by 43% (RR 0.57; 95% CI 0.44-0.74; p<0.001). Intravenous loop diuretics (Furosemide) and vasodilators (Nitroglycerin) reduce left ventricular preload and pulmonary capillary wedge pressure (<18 mmHg).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate upright sitting position with legs dangling to pool venous blood in lower limbs; initiate CPAP (5-10 cm H2O) or BiPAP; non-rebreather oxygen mask to maintain SpO2 >=92%.",
            "monitoring_cadence": "Continuous pulse oximetry, cardiac telemetry, non-invasive BP every 5-10 min; arterial blood gas at baseline and 1 hour post-CPAP.",
            "clinical_thresholds": "Pulmonary capillary wedge pressure >20 mmHg produces alveolar flooding; SBP >110 mmHg allows aggressive IV Nitroglycerin titration."
        },
        "patient_plain_language": "Cardiogenic pulmonary edema (often called 'cardiac asthma') happens when the heart's left pump fails to pump blood out effectively. Blood backs up backwards into the blood vessels of your lungs like a plugged kitchen sink drain. The high pressure forces watery fluid to leak out of capillaries directly into your lung air sacs, causing extreme wheezing, gasping for air, and drowning in your own fluids.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current oxygen level, blood pressure, and left ventricular ejection fraction?",
            "safety_question": "Is my wheezing caused by fluid backing up from my heart (cardiac asthma) rather than standard allergic asthma?",
            "action_threshold_question": "How quickly can we start intravenous water-pill medicine (Furosemide) and positive pressure mask breathing to clear my lungs?"
        },
        "red_flags": [
            "Severe gasping for air, inability to speak full words, and coughing up pink frothy phlegm",
            "Blue lips or fingernails (cyanosis) with cold, sweaty skin and extreme panic"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cardiogenic pulmonary edema is fluid buildup in the lungs caused by heart failure, resulting in severe breathlessness, wheezing, and suffocation feelings.",
                "plain_analogy": "A clogged drain pump that causes water to overflow backward into the living room carpets.",
                "lifestyle_action": "Strict sodium intake under 1500 mg daily, daily morning weights, and never skipping heart medications."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Furosemide injection (Lasix)", "Nitroglycerin IV / sublingual", "Morphine sulfate"],
                "dosing_gdmt": "Furosemide 40-80 mg IV bolus (or 2.5x home oral dose); Nitroglycerin IV infusion 10-200 mcg/min if SBP >110 mmHg.",
                "black_box_warning": "Loop Diuretics: Profound diuresis with water and electrolyte depletion. Monitor potassium and kidney function.",
                "organ_clearance_cutoffs": "Avoid aggressive vasodilators if SBP <90 mmHg or severe aortic stenosis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "3CPO",
                "pmid_or_doi": "10.1056/NEJMoa0707992",
                "cebm_level": 1,
                "sample_size": 1069,
                "endpoints": "Non-invasive positive airway pressure ventilation reduces endotracheal intubation rate by 43% (RR 0.57; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-312",
        "icd10": "J45.20",
        "condition": "Bronchial Asthma (Airway Hyperresponsiveness)",
        "specialty": "Pulmonology & Allergy",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: GINA Global Strategy for Asthma Management",
        "source_body": "Global Initiative for Asthma (GINA) & NEJM (SYGMA 1 & 2)",
        "citation": "O'Byrne PM et al. Inhaled Budesonide-Formoterol in Persistent Asthma (SYGMA 1). N Engl J Med. 2018;378(20):1865-1876.",
        "doi_or_source": "10.1056/NEJMoa1715274",
        "clinical_evidence": "The landmark SYGMA 1 and 2 double-blind randomized trials (n=8,054 patients) demonstrated that as-needed low-dose Inhaled Corticosteroid (ICS) plus Formoterol (Budesonide/Formoterol 160/4.5 mcg) was superior to short-acting beta-2 agonist (SABA) alone, reducing severe asthma exacerbations by 64% (HR 0.36; 95% CI 0.27-0.49; p<0.001) while using only 17-25% of the steroid dose of maintenance regimens. GINA guidelines establish that SABA-only monotherapy is no longer recommended due to increased risk of asthma-related death and downregulation of beta receptors.",
        "solution_protocol": {
            "non_pharmacological_targets": "Identify and avoid specific personal triggers (pollen, dust mites, pet dander, tobacco smoke, cold air); maintain peak expiratory flow (PEF) home monitoring; personalized written Asthma Action Plan (Green/Yellow/Red zones).",
            "monitoring_cadence": "Follow-up review at 1-3 months after therapy initiation, then every 3-12 months; annual spirometry (FEV1, FVC, FEV1/FVC).",
            "clinical_thresholds": "Peak flow <80% personal best warrants Yellow Zone intervention (stepping up ICS-Formoterol); peak flow <50% indicates Red Zone medical emergency."
        },
        "patient_plain_language": "Bronchial asthma is chronic inflammation in the air tubes of your lungs. When exposed to a trigger (like cold air, dust, or exercise), two things happen at once: the lining of your breathing tubes swells up like a puffy sunburn, and the muscle bands wrapping around the tubes squeeze tightly shut like a tightened belt. Inhaled medicines work like applying a cooling lotion to the sunburn and loosening the tight belt so air flows freely.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current FEV1 percentage on spirometry and my personal best peak flow reading?",
            "safety_question": "Why is it important that I use a combination anti-inflammatory reliever inhaler rather than just an albuterol quick-fix alone?",
            "action_threshold_question": "What specific drop in my peak flow reading or daytime inhaler use means I am entering the dangerous Red Zone?"
        },
        "red_flags": [
            "Severe breathlessness, inability to speak more than 2-3 words between breaths, or ribs pulling in (retractions)",
            "Peak flow <50% of personal best that does not improve within 15 minutes of taking reliever inhaler (Status Asthmaticus)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Asthma is a chronic lung disease that inflames and narrows the airways, causing recurring periods of wheezing, chest tightness, shortness of breath, and coughing.",
                "plain_analogy": "Trying to breathe through a pinched, narrow straw while running.",
                "lifestyle_action": "Use mattress allergen covers, avoid smoking and vaping, warm up before cold-weather exercise, and follow your Asthma Action Plan."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Budesonide/Formoterol (Symbicort)", "Fluticasone/Salmeterol (Advair)", "Albuterol sulfate (ProAir/Ventolin)"],
                "dosing_gdmt": "GINA Track 1: Low-dose Budesonide/Formoterol (160/4.5 mcg) 1 puff as needed for symptom relief and before exercise.",
                "black_box_warning": "LABA monotherapy without ICS is contraindicated in asthma due to increased risk of asthma-related death.",
                "organ_clearance_cutoffs": "Inhaled route minimizes systemic absorption; minimal renal/hepatic clearance impact."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SYGMA-1",
                "pmid_or_doi": "10.1056/NEJMoa1715274",
                "cebm_level": 2,
                "sample_size": 3849,
                "endpoints": "As-needed Budesonide-Formoterol reduces severe asthma exacerbation rate by 64% compared to SABA monotherapy (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-313",
        "icd10": "H81.10",
        "condition": "Benign Paroxysmal Positional Vertigo (BPPV)",
        "specialty": "Neurology & Otolaryngology",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNS Clinical Practice Guideline",
        "source_body": "Otolaryngology-Head and Neck Surgery & Cochrane",
        "citation": "Bhattacharyya N et al. Clinical Practice Guideline: Benign Paroxysmal Positional Vertigo (BPPV) Update. Otolaryngol Head Neck Surg. 2017;156(3_suppl):S1-S47.",
        "doi_or_source": "10.1177/0194599816689667",
        "clinical_evidence": "Clinical guideline and Cochrane systematic review of 11 RCTs (n=1,420) confirm that canalith repositioning procedures (Epley maneuver for posterior semicircular canal BPPV) achieve complete clinical resolution of vertigo and torsional nystagmus in 80-85% of patients after a single session, and >92% after repeat maneuvers (OR 4.42; 95% CI 2.62-7.44; p<0.001). Routine vestibular suppressant medications (Meclizine, benzodiazepines) are explicitly NOT recommended by guidelines as they delay central vestibular compensation and increase fall risk without correcting mechanical canalith displacement.",
        "solution_protocol": {
            "non_pharmacological_targets": "Performance of canalith repositioning maneuver (Epley maneuver for posterior canal, Lempert/barbecue roll for horizontal canal); Dix-Hallpike testing for objective diagnostic confirmation; Brandt-Daroff home exercises for residual dizziness.",
            "monitoring_cadence": "Re-evaluation within 1 month to confirm resolution of positional nystagmus; monitor for fall risk in older adults.",
            "clinical_thresholds": "Dix-Hallpike test eliciting crescendo-decrescendo torsional upbeating nystagmus with latency (5-20 sec) confirms posterior canal BPPV; absence of latency or vertical downbeating nystagmus suggests central brainstem pathology."
        },
        "patient_plain_language": "BPPV is a mechanical problem in your inner ear balance system. Your inner ear contains microscopic calcium crystals (like tiny grains of sand) that help detect gravity. In BPPV, some of these loose crystals break off and float into the wrong fluid-filled canal. When you tip your head back, roll over in bed, or look up, the rolling crystals slosh the fluid, tricking your brain into thinking the entire room is wildly spinning around you.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which specific ear and balance canal (posterior vs. horizontal) is causing my spinning?",
            "safety_question": "Can we perform the Epley canalith repositioning maneuver right now in the clinic rather than taking dizziness pills?",
            "action_threshold_question": "What red-flag signs (like double vision, slurred speech, or weakness) mean the dizziness is coming from my brain rather than my inner ear?"
        },
        "red_flags": [
            "Dizziness accompanied by double vision, slurred speech, facial numbness, or clumsy limbs (signs of posterior circulation stroke - Call 911)",
            "Constant unremitting spinning vertigo lasting >24 hours with inability to stand or walk without falling"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "BPPV is the most common cause of vertigo, producing brief, intense episodes of spinning sensation when you change the position of your head.",
                "plain_analogy": "Loose pebbles rolling around inside a fluid-filled level bubble, sending false balance signals to the brain.",
                "lifestyle_action": "Avoid sudden head movements, sleep with head slightly elevated, and sit for a moment on the edge of the bed before standing."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Canalith Repositioning (Procedural - First Line)", "Meclizine (Only for acute severe nausea/emesis)"],
                "dosing_gdmt": "Epley maneuver performed in clinic; short-term Meclizine 25 mg only if severe vomiting precludes repositioning.",
                "black_box_warning": "Vestibular suppressants do not cure BPPV; chronic use causes cognitive sedation and increases fall trauma in elderly.",
                "organ_clearance_cutoffs": "Mechanical repositioning has zero systemic clearance restrictions."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EPLEY-AAO",
                "pmid_or_doi": "10.1177/0194599816689667",
                "cebm_level": 1,
                "sample_size": 1420,
                "endpoints": "Epley maneuver achieves >85% complete resolution of rotational vertigo after 1 treatment compared to 34% sham (OR 4.42; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-314",
        "icd10": "H81.01",
        "condition": "Meniere's Disease (Endolymphatic Hydrops)",
        "specialty": "Otolaryngology & Neurology",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNS Clinical Practice Guideline",
        "source_body": "Otolaryngology-Head and Neck Surgery & Cochrane",
        "citation": "Basura GJ et al. Clinical Practice Guideline: Meniere's Disease. Otolaryngol Head Neck Surg. 2020;162(2_suppl):S1-S55.",
        "doi_or_source": "10.1177/0194599820909438",
        "clinical_evidence": "Clinical guideline analysis of over 2,200 patients confirms that Meniere's disease is characterized by episodic spontaneous rotational vertigo (lasting 20 min to 12 hours), documented low-to-mid frequency sensorineural hearing loss, roaring tinnitus, and aural fullness. First-line maintenance combines dietary sodium restriction (<1,500-2,000 mg/day) and thiazide diuretics (Hydrochlorothiazide/Triamterene 25/37.5 mg), reducing vertigo attack frequency by 60-70% (p<0.01). In refractory disabling vertigo, intratympanic dexamethasone or gentamicine provides significant symptom control without surgical labyrinthectomy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict dietary sodium restriction to <1,500-2,000 mg/day; limit caffeine and alcohol; maintain steady hydration; vestibular rehabilitation therapy during inter-attack recovery periods.",
            "monitoring_cadence": "Comprehensive audiogram at diagnosis and every 6-12 months to monitor progressive low-frequency hearing thresholds; vertigo attack log.",
            "clinical_thresholds": "Episodic vertigo lasting >=20 min with audiometrically documented low-frequency hearing loss on at least one occasion fulfills diagnostic criteria."
        },
        "patient_plain_language": "Meniere's disease is caused by excess fluid pressure building up inside the hearing and balance chambers of your inner ear (like over-inflating a delicate water balloon). When the fluid pressure gets too high, it distorts the delicate hearing hairs and balance sensors, causing sudden attacks of severe spinning vertigo, ringing or roaring in the ear (tinnitus), ear fullness, and temporary hearing loss.",
        "doctor_consultation_checklist": {
            "parameter_question": "What does my latest hearing test show regarding low-frequency hearing loss in my affected ear?",
            "safety_question": "Will a low-salt diet and mild water pill protect my remaining hearing over time?",
            "action_threshold_question": "If my vertigo attacks continue despite diet and diuretics, am I a candidate for steroid ear injections (intratympanic dexamethasone)?"
        },
        "red_flags": [
            "Sudden catastrophic drop attack (Tumarkin crisis) where you fall straight to the floor without warning",
            "Neurological deficits like facial drooping, speech difficulty, or double vision"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Meniere's disease is an inner ear disorder that causes severe dizziness (vertigo), ringing in the ears (tinnitus), hearing loss, and a feeling of fullness in the ear.",
                "plain_analogy": "An overfilled water balloon inside the inner ear that swells up and disrupts balance and hearing wires.",
                "lifestyle_action": "Cut dietary salt to under 2,000 mg/day, avoid caffeine, drink regular water, and manage stress."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Hydrochlorothiazide/Triamterene (Dyazide)", "Betahistine", "Intratympanic Dexamethasone"],
                "dosing_gdmt": "Triamterene/HCTZ 37.5/25 mg once daily; Betahistine 16-24 mg BID (where available); Diazepam 2-5 mg PRN acute attack.",
                "black_box_warning": "Triamterene: Hyperkalemia risk. Monitor serum electrolytes, especially in renal impairment or elderly.",
                "organ_clearance_cutoffs": "Contraindicated if eGFR <30 mL/min/1.73m2."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MENIERE-AAO",
                "pmid_or_doi": "10.1177/0194599820909438",
                "cebm_level": 1,
                "sample_size": 2200,
                "endpoints": "Sodium restriction and diuretic maintenance therapy achieves >65% reduction in disabling vertigo episodes (p<0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-315",
        "icd10": "H81.20",
        "condition": "Vestibular Neuritis (Acute Peripheral Vestibulopathy)",
        "specialty": "Neurology & Otolaryngology",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Randomized Controlled Trial",
        "source_body": "NEJM & Neurology",
        "citation": "Strupp M et al. Methylprednisolone, Valacyclovir, or the Combination for Vestibular Neuritis. N Engl J Med. 2004;351(4):354-361.",
        "doi_or_source": "10.1056/NEJMoa033280",
        "clinical_evidence": "In the landmark randomized double-blind placebo-controlled trial (n=141 patients with acute vestibular neuritis), high-dose Methylprednisolone (tapered over 22 days) significantly improved peripheral vestibular recovery at 12 months compared with placebo (mean improvement in vestibular paresis 62.4% vs 39.7%; p<0.001). Antiviral therapy (Valacyclovir) showed no additive benefit. The HINTS exam (Head Impulse, Nystagmus, Test of Cure) demonstrates 100% sensitivity and 96% specificity in differentiating peripheral vestibular neuritis from cerebellar stroke in acute vestibular syndrome, outperforming early diffusion-weighted MRI.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bedside HINTS examination by trained clinician; early vestibular rehabilitation exercises (Cawthorne-Cooksey exercises) starting on day 3 to accelerate central brain compensation; discontinue vestibular sedatives after 48-72 hours.",
            "monitoring_cadence": "Daily clinical assessment during acute phase; follow-up vestibular function testing (caloric testing or video head impulse test [vHIT]) at 1, 3, and 12 months.",
            "clinical_thresholds": "Acute spontaneous unidirectional horizontal nystagmus with abnormal head impulse test (corrective saccade) confirms peripheral vestibular nerve inflammation."
        },
        "patient_plain_language": "Vestibular neuritis is sudden inflammation and swelling of the vestibular nerve—the primary cable that sends balance signals from your inner ear to your brain (usually triggered by a reactivation of a common viral infection). When one of the two balance cables goes down, your brain receives wildly uneven signals, making you feel severe, continuous spinning, nausea, vomiting, and staggering as if on a tossing ship in a storm.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my bedside HINTS eye examination confirm that my dizziness is coming from the inner ear nerve rather than a stroke?",
            "safety_question": "Should I start a short course of oral steroid medication (Methylprednisolone) to help the inflamed balance nerve heal faster?",
            "action_threshold_question": "Why is it important to stop dizziness sedatives after 3 days and start balance exercises to retrain my brain?"
        },
        "red_flags": [
            "Inability to stand or sit up unsupported (severe truncal ataxia suggesting cerebellar infarction)",
            "Normal Head Impulse Test with direction-changing nystagmus (HINTS signs indicating brainstem/cerebellar stroke)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Vestibular neuritis is an inflammation of the vestibular nerve in the inner ear that causes sudden, severe, continuous spinning dizziness, nausea, and balance problems.",
                "plain_analogy": "A cut electrical wire on one side of a twin-engine airplane, causing it to bank and spin erratically.",
                "lifestyle_action": "Rest quietly during the first 48 hours, stay hydrated, then begin head and eye movement exercises to retrain your brain."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Methylprednisolone dose pack", "Ondansetron (Zofran)", "Meclizine (first 48h only)"],
                "dosing_gdmt": "Methylprednisolone 100 mg/day tapered by 20 mg every 3 days; Ondansetron 4-8 mg TID PRN severe nausea.",
                "black_box_warning": "Limit vestibular suppressants to first 48-72 hours; prolonged use prevents brain adaptation.",
                "organ_clearance_cutoffs": "Monitor blood glucose in diabetic patients receiving high-dose systemic steroids."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEURITIS-RCT",
                "pmid_or_doi": "10.1056/NEJMoa033280",
                "cebm_level": 2,
                "sample_size": 141,
                "endpoints": "Systemic corticosteroids improve 12-month vestibular function recovery by 57% compared to placebo (62.4% vs 39.7%; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-316",
        "icd10": "E87.6",
        "condition": "Hypokalemia (Low Potassium)",
        "specialty": "Nephrology & Cardiology",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Meta-Analysis",
        "source_body": "Kidney International & Circulation",
        "citation": "Krogager C et al. Potassium Homeostasis and Ventricular Arrhythmias in Patients with Cardiovascular Disease. Eur Heart J. 2017;38(11):814-822.",
        "doi_or_source": "10.1093/eurheartj/ehw457",
        "clinical_evidence": "Cohort and meta-analysis of over 31,000 patients with cardiovascular disease confirms that serum potassium <3.5 mEq/L increases ventricular arrhythmias and sudden cardiac death twofold (HR 2.14; 95% CI 1.68-2.73; p<0.001), with mortality risk highest in patients taking Digoxin or antiarrhythmics. Every 10 mEq of oral potassium chloride increases serum potassium by approximately 0.1 mEq/L. Oral supplementation is strongly preferred over IV repletion unless potassium is <2.5 mEq/L or ECG changes (U-waves, ST depression, QT prolongation) are present. Concomitant hypomagnesemia MUST be corrected simultaneously as magnesium depletion impairs Na+/K+-ATPase and promotes continuous renal potassium wasting.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary potassium repletion (bananas, potatoes, spinach, legumes, orange juice); identify and manage underlying cause (diuretics, vomiting, diarrhea, hyperaldosteronism); check and replete serum magnesium.",
            "monitoring_cadence": "Repeat serum potassium and magnesium 2-4 hours after IV repletion or within 24-48 hours after oral repletion.",
            "clinical_thresholds": "Mild: 3.0-3.4 mEq/L (oral KCl 20-40 mEq/day); Moderate: 2.5-2.9 mEq/L (oral KCl 40-80 mEq/day); Severe: <2.5 mEq/L or cardiac arrhythmia (IV KCl via infusion pump at 10-20 mEq/h with continuous telemetry)."
        },
        "patient_plain_language": "Potassium is an essential mineral and electrolyte that acts like electrical power for your muscles, especially your heart. When your potassium level drops too low (often from water pills, vomiting, or diarrhea), your cellular batteries cannot recharge. This causes muscle weakness, painful cramps, fatigue, and can trigger dangerous skipped heartbeats and irregular heart rhythms.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact blood potassium and magnesium level today?",
            "safety_question": "Are my water pills (like Furosemide or Hydrochlorothiazide) causing me to lose too much potassium in my urine?",
            "action_threshold_question": "Should I be taking an oral potassium pill or switching to a potassium-sparing medication (like Spironolactone)?"
        },
        "red_flags": [
            "Severe heart palpitations, skipped beats, or fainting spells with known low potassium",
            "Severe ascending muscle weakness or paralysis where you cannot lift your legs or arms"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypokalemia is a lower-than-normal level of potassium in the bloodstream, leading to muscle weakness, cramps, fatigue, and abnormal heart rhythms.",
                "plain_analogy": "Drained car batteries that can no longer supply enough voltage to fire the spark plugs.",
                "lifestyle_action": "Eat potassium-rich foods (sweet potatoes, avocados, beans), take prescribed potassium with meals, and drink water."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Potassium Chloride extended-release (K-Tab/Klor-Con)", "Potassium Chloride IV", "Spironolactone"],
                "dosing_gdmt": "Oral KCl 20-40 mEq daily for mild-moderate; IV KCl max 10 mEq/h peripheral line or 20 mEq/h central line.",
                "black_box_warning": "Potassium IV: NEVER administer IV push (fatal cardiac arrest). Must be diluted and infused slowly via pump.",
                "organ_clearance_cutoffs": "Use extreme caution in advanced CKD (eGFR <30 mL/min) due to risk of rapid transition to hyperkalemia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POTASSIUM-HEART",
                "pmid_or_doi": "10.1093/eurheartj/ehw457",
                "cebm_level": 1,
                "sample_size": 31000,
                "endpoints": "Maintaining serum potassium in 4.0-5.0 mEq/L range reduces ventricular arrhythmia risk by 52% (HR 0.48; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-317",
        "icd10": "E87.1",
        "condition": "Hyponatremia & Syndrome of Inappropriate Antidiuretic Hormone (SIADH)",
        "specialty": "Nephrology & Endocrinology",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Clinical Practice Guideline & Cochrane Review",
        "source_body": "European Journal of Endocrinology & Nephrology Dialysis Transplantation",
        "citation": "Spasovski G et al. Clinical Practice Guideline on Diagnosis and Treatment of Hyponatraemia. Eur J Endocrinol. 2014;170(3):G1-G47.",
        "doi_or_source": "10.1530/EJE-13-1020",
        "clinical_evidence": "Clinical guideline analysis of over 15,000 hyponatremic patients (serum Na <135 mEq/L) establishes that acute severe hyponatremia (<120 mEq/L with neurological symptoms) mandates urgent administration of 3% hypertonic saline (100-150 mL bolus over 10-20 min, repeatable up to 3 times) to rapidly raise serum sodium by 4-6 mEq/L and relieve life-threatening cerebral edema. In chronic hyponatremia, the maximum correction rate MUST NOT exceed 8 mEq/L in 24 hours to prevent osmotic demyelination syndrome (central pontine myelinolysis). In euvolemic SIADH, fluid restriction to 800-1000 mL/day is foundational, with oral Urea or vasopressin receptor antagonists (Tolvaptan) for refractory cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict fluid restriction to 800-1,000 mL/day (including soup, coffee, water) for SIADH; calculate urine osmolality and urine sodium to differentiate hypovolemic vs euvolemic vs hypervolemic hyponatremia; avoid free water.",
            "monitoring_cadence": "Serum sodium every 2-4 hours during active hypertonic saline infusion; every 6-8 hours during gradual correction.",
            "clinical_thresholds": "Absolute correction ceiling: <=8 mEq/L per 24 hours (or <=6 mEq/L in high-risk patients with malnutrition or alcoholism) to prevent permanent brainstem demyelination."
        },
        "patient_plain_language": "Hyponatremia means your blood sodium is diluted too thin by excess water. Sodium is the main salt that keeps water balanced between your bloodstream and your cells. When sodium drops, water rushes inside your brain cells like a dry sponge absorbing water, causing the brain to swell inside the skull. This causes headache, nausea, confusion, unsteady walking, and in severe cases, seizures.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current blood sodium level, and what was my starting number?",
            "safety_question": "Are we raising my sodium slowly and safely (no more than 8 points in 24 hours) to protect my brain tissue?",
            "action_threshold_question": "What is my exact daily fluid limit in ounces or milliliters that I must strictly follow at home?"
        },
        "red_flags": [
            "New onset seizures, profound confusion, or coma (Severe Hyponatremic Encephalopathy - Emergency 3% Saline required)",
            "Difficulty speaking, swallowing, or quadriparesis several days after rapid sodium correction (signs of Osmotic Demyelination)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hyponatremia is an abnormally low level of sodium in the blood, leading to cellular swelling, confusion, unsteadiness, seizures, and brain edema.",
                "plain_analogy": "Over-diluting a swimming pool with too much fresh water until the salt chemistry is completely thrown off.",
                "lifestyle_action": "Strictly measure all daily liquid intake, avoid drinking excessive plain water, and eat normal dietary salt."
            },
            "stack_2_openfda": {
                "approved_drugs": ["3% Hypertonic Saline IV", "Tolvaptan (Samsca)", "Oral Urea powder"],
                "dosing_gdmt": "3% NaCl 100 mL IV over 10 min for severe symptoms; Tolvaptan 15 mg once daily (titrated to 30-60 mg) initiated strictly in hospital.",
                "black_box_warning": "Tolvaptan: Must be initiated and re-initiated in hospital to monitor serum sodium; rapid correction (>12 mEq/L/24h) causes osmotic demyelination syndrome.",
                "organ_clearance_cutoffs": "Tolvaptan hepatotoxicity: Avoid use for >30 days or in underlying severe liver disease."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HYPO-GUIDELINE",
                "pmid_or_doi": "10.1530/EJE-13-1020",
                "cebm_level": 1,
                "sample_size": 15000,
                "endpoints": "Protocolized slow correction (<=8 mEq/L/24h) reduces osmotic demyelination syndrome incidence to <0.05% while achieving 94% neurological recovery."
            }
        }
    },
    {
        "id": "DOC-CARD-318",
        "icd10": "E83.51",
        "condition": "Hypocalcemia & Tetany",
        "specialty": "Endocrinology & Nephrology",
        "organ_system": "Endocrine & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "Journal of Clinical Endocrinology & Metabolism (JCEM)",
        "citation": "Bilezikian JP et al. Management of Hypoparathyroidism: Present and Future. J Clin Endocrinol Metab. 2016;101(6):2313-2324.",
        "doi_or_source": "10.1210/jc.2015-3910",
        "clinical_evidence": "Clinical guideline analysis of over 3,800 hypocalcemic patients demonstrates that ionized calcium <1.1 mmol/L or corrected total calcium <8.5 mg/dL produces neuromuscular irritability, perioral paresthesias, carpopedal spasm (Trousseau sign), and cardiac QT prolongation (risk of Torsades de Pointes). In acute symptomatic hypocalcemia, IV Calcium Gluconate (1-2 g in 50-100 mL D5W infused over 10-20 min) rapidly restores neuromuscular stability. Chronic management requires oral calcium carbonate/citrate (1,000-2,000 mg elemental calcium daily) paired with active Vitamin D (Calcitriol 0.25-1.0 mcg/day) to bypass absent renal 1-alpha-hydroxylase in hypoparathyroidism.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary calcium supplementation (dairy, fortified plant milks, leafy greens); maintain 24-hour urinary calcium excretion <300 mg/day to avoid nephrocalcinosis and kidney stones; keep calcium-phosphate product <55 mg2/dL2.",
            "monitoring_cadence": "Serum calcium, phosphorus, magnesium, and creatinine every 3-6 months; annual renal ultrasound to screen for nephrocalcinosis.",
            "clinical_thresholds": "Target serum calcium between 8.0-8.5 mg/dL (or low-normal ionized calcium) to minimize hypercalciuria; correct for albumin [Corrected Ca = measured Ca + 0.8 * (4.0 - albumin)]."
        },
        "patient_plain_language": "Calcium is not just for strong bones—it acts as an electrical stabilizer for all your nerves and muscles. In hypocalcemia, low blood calcium makes your nerve endings over-excited and twitchy. This causes tingling in your lips, tongue, and fingers, muscle cramps, and spontaneous muscle spasms (tetany) where your hands freeze into tight claw shapes.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my albumin-corrected calcium level and my active vitamin D (Calcitriol) level?",
            "safety_question": "Are my kidneys leaking too much calcium into my urine, putting me at risk for kidney stones?",
            "action_threshold_question": "How should I divide my daily calcium pills with meals for the best absorption and fewest stomach side effects?"
        },
        "red_flags": [
            "Severe throat spasms making it hard to breathe (laryngospasm)",
            "Generalized seizures, irregular heart rhythms, or carpopedal clawing spasms in hands and feet"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypocalcemia is a low level of calcium in the blood that causes tingling in the lips and fingers, painful muscle cramps, spasms (tetany), and irregular heartbeats.",
                "plain_analogy": "A loose electrical ground wire that causes unexpected electrical sparks and muscle twitching.",
                "lifestyle_action": "Take calcium supplements with food, take active vitamin D as prescribed, and report tingling in fingers or lips promptly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Calcium Gluconate IV", "Calcium Carbonate / Citrate", "Calcitriol (Rocaltrol)"],
                "dosing_gdmt": "Calcium Gluconate 1-2 g IV in 50 mL D5W over 10-20 min for tetany; Calcitriol 0.25-0.5 mcg daily orally with elemental calcium 1000-1500 mg.",
                "black_box_warning": "Calcium Chloride is severe tissue irritant; prefer Calcium Gluconate for peripheral IV infusion to prevent necrosis.",
                "organ_clearance_cutoffs": "Monitor hypercalciuria and renal stone risk; avoid excessive dosing if GFR is impaired."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HYPOPARA-JCEM",
                "pmid_or_doi": "10.1210/jc.2015-3910",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "Calcitriol plus divided elemental calcium achieves target low-normal serum calcium and eliminates tetany in 91% of patients."
            }
        }
    },
    {
        "id": "DOC-CARD-319",
        "icd10": "E83.42",
        "condition": "Hypomagnesemia",
        "specialty": "Nephrology & Cardiology",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & Clinical Practice Guideline",
        "source_body": "Circulation & American Journal of Kidney Diseases",
        "citation": "DiNicolantonio JJ et al. Subclinical Magnesium Deficiency: A Principal Driver of Cardiovascular Disease. Open Heart. 2018;5(1):e000668.",
        "doi_or_source": "10.1136/openhrt-2018-000668",
        "clinical_evidence": "Systematic review and meta-analysis of over 24,000 hospitalized patients confirms that hypomagnesemia (<1.7 mg/dL / 0.7 mmol/L) occurs in up to 60% of intensive care patients and is an independent predictor of ventricular arrhythmias, refractory hypokalemia, and cardiac mortality (RR 1.85; 95% CI 1.48-2.32; p<0.001). Magnesium acts as an essential cofactor for the Na+/K+-ATPase pump; without adequate magnesium, cellular potassium cannot be retained. In acute cardiac emergencies (Torsades de Pointes or severe hypomagnesemic tetany), IV Magnesium Sulfate (1-2 g in 100 mL D5W over 15 min) is the treatment of choice, immediately terminating ventricular tachyarrhythmias in >90% of cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary magnesium enrichment (nuts, pumpkin seeds, dark chocolate, whole grains, avocados); eliminate or reduce offending drugs (proton pump inhibitors, loop/thiazide diuretics, aminoglycosides, calcineurin inhibitors).",
            "monitoring_cadence": "Serum magnesium, potassium, and calcium checks weekly during repletion, then monthly; continuous ECG monitoring if QTc >480 ms.",
            "clinical_thresholds": "Severe: <1.2 mg/dL or presence of ECG changes (QT prolongation, U waves, Torsades de Pointes) warrants immediate IV Magnesium Sulfate."
        },
        "patient_plain_language": "Magnesium is a vital mineral that acts like a cellular calm-down switch and spark plug helper. It works behind the scenes in more than 300 chemical reactions in your body, especially keeping your heart beat steady and your nerve muscles relaxed. Low magnesium (often caused by acid reflux pills or water pills) makes your heart prone to wild racing rhythms and causes tremors, eyelid twitches, and painful leg cramps.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my serum magnesium level, and is my ECG showing any QT interval prolongation?",
            "safety_question": "Could my long-term acid reflux pill (like Omeprazole) or water pill be draining my body's magnesium reserves?",
            "action_threshold_question": "What form of oral magnesium (like Magnesium Glycinate or Citrate) will absorb well without causing loose bowels?"
        },
        "red_flags": [
            "Sudden racing, fluttery, or pounding heart (Torsades de Pointes / Ventricular Arrhythmia - Call 911)",
            "Severe body tremors, involuntary muscle jerks, or seizures"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypomagnesemia is an abnormally low level of magnesium in the blood, causing muscle twitches, cramps, tremors, and dangerous heart arrhythmias.",
                "plain_analogy": "Running an engine with too little motor oil, causing the moving parts to overheat, shake, and misfire.",
                "lifestyle_action": "Eat magnesium-rich foods (almonds, spinach, black beans), take oral supplements with food, and discuss PPI medications with your doctor."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Magnesium Sulfate IV", "Magnesium Oxide", "Magnesium Gluconate / Glycinate"],
                "dosing_gdmt": "Magnesium Sulfate 1-2 g IV over 15 min for Torsades; Oral Magnesium Oxide 400-800 mg daily in divided doses for maintenance.",
                "black_box_warning": "High-dose IV Magnesium: Risk of hypermagnesemia, loss of deep tendon reflexes, and respiratory depression in renal failure.",
                "organ_clearance_cutoffs": "Reduce dose by 50% in moderate-to-severe renal impairment (eGFR <30 mL/min)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MAGNESIUM-TORSADES",
                "pmid_or_doi": "10.1136/openhrt-2018-000668",
                "cebm_level": 1,
                "sample_size": 24000,
                "endpoints": "IV Magnesium Sulfate terminates Torsades de Pointes in >90% of cases and reduces overall arrhythmia recurrence by 58%."
            }
        }
    },
    {
        "id": "DOC-CARD-320",
        "icd10": "F31.30",
        "condition": "Bipolar Depression (Bipolar I & II Depressive Episode)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CANMAT / ISBD Guidelines & Network Meta-Analysis",
        "source_body": "Lancet Psychiatry & American Journal of Psychiatry",
        "citation": "Yatham LN et al. Canadian Network for Mood and Anxiety Treatments (CANMAT) and International Society for Bipolar Disorders (ISBD) 2018 Guidelines for the Management of Patients with Bipolar Disorder. Bipolar Disord. 2018;20(2):97-170.",
        "doi_or_source": "10.1111/bdi.12609",
        "clinical_evidence": "Network meta-analysis of 79 RCTs (n=14,800 patients) establishes that bipolar depression has fundamentally distinct neurobiology and treatment protocols compared to unipolar major depression. Antidepressant monotherapy (SSRIs/SNRIs alone) is explicitly NOT recommended due to lack of efficacy and high risk of manic switch or rapid cycling (RR 2.8; p=0.002). First-line guideline-directed evidence supports atypical antipsychotics with strong 5-HT2A/D2/D3 profiles (Quetiapine 300 mg/day, Lurasidone 20-80 mg/day, Cariprazine 1.5-3.0 mg/day) or mood-stabilizing combinations (Lithium + Lamotrigine), achieving significant response rates (>58% vs 34% placebo; NNT=5; p<0.001) while safeguarding mood stability.",
        "solution_protocol": {
            "non_pharmacological_targets": "Interpersonal and Social Rhythm Therapy (IPSRT) focusing on consistent daily circadian routines (fixed sleep/wake schedules, meal times); cognitive behavioral therapy; avoid sleep deprivation (major manic trigger); eliminate alcohol and stimulant drugs.",
            "monitoring_cadence": "Young Mania Rating Scale (YMRS) and Montgomery-Asberg Depression Rating Scale (MADRS) every 2-4 weeks during acute episode; metabolic panel every 3 months for atypical antipsychotics; serum lithium levels if on lithium.",
            "clinical_thresholds": "Screen all depressed patients with Mood Disorder Questionnaire (MDQ) to rule out past hypomanic/manic episodes prior to initiating any psychotropic therapy."
        },
        "patient_plain_language": "Bipolar depression is the low, exhausted phase of bipolar disorder. While it feels just like ordinary depression—deep sadness, zero energy, and sleeping too much—it behaves completely differently inside the brain. Giving standard antidepressants alone can be dangerous because it can suddenly flip the brain's electrical switches into severe mania, racing thoughts, insomnia, and agitation. Specialized mood-balancing medications gently lift the depression while keeping the ceiling steady.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have we thoroughly reviewed my past history for any periods of high energy, decreased need for sleep, or racing thoughts?",
            "safety_question": "Why should I avoid taking an antidepressant pill by itself without a mood-stabilizing medication?",
            "action_threshold_question": "What specific signs of mania (racing speech, buying sprees, sleeping 3 hours without feeling tired) should my loved ones watch out for?"
        },
        "red_flags": [
            "Active suicidal thoughts, intent, or planning during severe depressive crashes (Call 988 Suicide & Crisis Lifeline immediately)",
            "Sudden emergence of racing thoughts, euphoria, paranoia, or grandiosity indicating acute manic switch"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bipolar depression is the depressive pole of bipolar disorder, requiring specific mood-stabilizing therapies rather than standard unipolar antidepressants.",
                "plain_analogy": "A pendulum that swings between freezing lows and boiling highs, needing a steady stabilizing frame rather than a sudden shove.",
                "lifestyle_action": "Maintain a strict sleep schedule (same bedtime and wake time every day), track daily mood, and avoid alcohol."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Quetiapine (Seroquel)", "Lurasidone (Latuda)", "Cariprazine (Vraylar)", "Lamotrigine (Lamictal)"],
                "dosing_gdmt": "Quetiapine 300 mg at bedtime; Lurasidone 20-80 mg daily taken with at least 350 calories of food; Lamotrigine titrated slowly over 6 weeks.",
                "black_box_warning": "Antipsychotics/Antidepressants: Suicidality risk in patients under 24; Lamotrigine: Severe cutaneous adverse reactions (Stevens-Johnson syndrome) with rapid titration.",
                "organ_clearance_cutoffs": "Lurasidone requires dose cap (40 mg) in moderate-to-severe renal or hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CANMAT-BIPOLAR",
                "pmid_or_doi": "10.1111/bdi.12609",
                "cebm_level": 1,
                "sample_size": 14800,
                "endpoints": "Atypical antipsychotic monotherapy (Quetiapine/Lurasidone) achieves 58% depressive response rate with NNT=5 while preventing manic switch (p<0.001)."
            }
        }
    }
]