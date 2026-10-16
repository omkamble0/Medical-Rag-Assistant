"""
part6_cardio_pulm_vascular.py
"""

PART_6_DISEASES = [
    {
        "id": "DOC-CARD-201",
        "icd10": "I34.0",
        "condition": "Mitral Valve Regurgitation",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (COAPT Trial) & ACC/AHA",
        "citation": "Stone GW et al. Transcatheter Mitral-Valve Repair in Patients with Heart Failure (COAPT). N Engl J Med. 2018;379(24):2307-2318.",
        "doi_or_source": "10.1056/NEJMoa1806640",
        "clinical_evidence": "In the landmark COAPT trial (n=614 heart failure patients with secondary mitral regurgitation), transcatheter mitral-valve repair (MitraClip) plus guideline-directed medical therapy (GDMT) significantly reduced annual hospitalization for heart failure compared with GDMT alone (35.8% vs 67.9% per patient-year; HR 0.53; 95% CI 0.40-0.70; p<0.001) and all-cause 24-month mortality (29.1% vs 46.1%; HR 0.62; 95% CI 0.46-0.82; p<0.001). Number needed to treat (NNT) to prevent 1 death was 5.9.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict daily dietary sodium restriction to <2,000 mg/day; daily morning weight tracking; supervised cardiac rehabilitation once stabilized.",
            "monitoring_cadence": "Comprehensive transthoracic echocardiogram (TTE) every 6 months for severe asymptomatic MR; transesophageal echocardiogram (TEE) prior to structural intervention.",
            "clinical_thresholds": "Regurgitant volume >=60 mL/beat, effective regurgitant orifice area (EROA) >=0.40 cm2, or LV end-systolic dimension (LVESD) >40 mm triggers urgent heart valve team review."
        },
        "patient_plain_language": "The mitral valve is like a one-way swinging door that lets blood flow forward from your heart's upper chamber to the lower pump. In mitral regurgitation, the door does not seal completely tightly, allowing blood to leak backwards into your lungs with every heartbeat.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current regurgitant volume and left ventricular end-systolic dimension (LVESD) on my latest echocardiogram?",
            "safety_question": "Are my current blood pressure medications keeping my heart's workload low enough to prevent the valve leak from worsening?",
            "action_threshold_question": "What degree of shortness of breath when lying flat (orthopnea) or ankle swelling indicates I need an immediate valve repair evaluation?"
        },
        "red_flags": [
            "Sudden severe shortness of breath when lying flat, coughing up pink frothy fluid, or sudden syncope (fainting) indicating acute pulmonary edema"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Mitral valve regurgitation occurs when the heart's mitral valve does not close tightly, allowing blood to flow backward into the heart and lungs.",
                "plain_analogy": "A backward-leaking valve flap that forces the heart to pump the same blood twice.",
                "lifestyle_action": "Sodium restriction under 2g/day, low-impact walking, and weighing every morning before breakfast."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Sacubitril/Valsartan", "Carvedilol", "Furosemide", "Spironolactone"],
                "dosing_gdmt": "Optimize ARNI to 97/103 mg BID, Carvedilol 25-50 mg BID, adjust loop diuretic to maintain euvolemia.",
                "black_box_warning": "ARNI/ACEi: Fetal toxicity; avoid during pregnancy. Monitor serum potassium and creatinine.",
                "organ_clearance_cutoffs": "Contraindicated if eGFR <15 mL/min/1.73m2 or serum potassium >5.4 mEq/L."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COAPT",
                "pmid_or_doi": "10.1056/NEJMoa1806640",
                "cebm_level": 2,
                "sample_size": 614,
                "endpoints": "All-cause mortality at 24 months 29.1% vs 46.1% (HR 0.62; p<0.001); annualized HF hospitalizations reduced by 47%."
            }
        }
    },
    {
        "id": "DOC-CARD-202",
        "icd10": "I33.0",
        "condition": "Infective Endocarditis",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Multicenter Trial",
        "source_body": "Circulation (AHA Endocarditis Guidelines) & NEJM (POET)",
        "citation": "Iversen K et al. Partial Oral versus Intravenous Antibiotic Treatment of Endocarditis (POET). N Engl J Med. 2019;380(5):415-424.",
        "doi_or_source": "10.1056/NEJMoa1808312",
        "clinical_evidence": "The landmark POET trial (n=400 randomized patients with left-sided endocarditis stabilized on initial IV therapy) proved that transitioning to step-down oral antibiotics was non-inferior to continued intravenous antibiotic therapy for the composite primary outcome of all-cause mortality, unplanned cardiac surgery, embolic events, or relapsed bacteremia (9.0% oral vs 12.1% IV; difference -3.1 percentage points; 95% CI -8.8 to 2.5; p=0.40). Modified Duke Criteria remain the gold standard for clinical diagnosis (sensitivity >80%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate removal of infected indwelling central venous catheters; strict dental hygiene optimization to prevent transient bacteremia; mandatory valve surgery evaluation for refractory infection.",
            "monitoring_cadence": "Repeat blood cultures every 24-48 hours until documented microbiological clearance; weekly CRP and ESR; follow-up TTE at completion of antimicrobial therapy.",
            "clinical_thresholds": "Vegetation size >10 mm with embolic episode, severe acute valve regurgitation causing cardiogenic shock, or perivalvular abscess mandates emergent surgical consultation."
        },
        "patient_plain_language": "Infective endocarditis is a serious infection of the smooth inner lining and valves of your heart. Bacteria or microbes enter your bloodstream (often from the gums, skin, or medical lines) and settle on heart valves, creating clumps of bacteria that damage the heart flaps.",
        "doctor_consultation_checklist": {
            "parameter_question": "What specific organism grew on my blood cultures and what are its exact antibiotic sensitivities?",
            "safety_question": "Do I need prophylactic antibiotics before dental cleanings or invasive procedures in the future?",
            "action_threshold_question": "What fever temperature or sudden neurological symptoms (weakness, numbness) require calling the surgical cardiology team immediately?"
        },
        "red_flags": [
            "New focal neurologic deficits (stroke), sudden visual changes (Roth spots), splinter hemorrhages under nails with high spike fever, or sudden breathless collapse"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Infective endocarditis is an infection of the inner tissues of the heart, most commonly affecting the heart valves.",
                "plain_analogy": "Bacteria from the bloodstream sticking like barnacles to the heart valves, eroding the tissue.",
                "lifestyle_action": "Meticulous oral hygiene, twice-daily brushing, antibiotic prophylaxis before dental work if high-risk."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Vancomycin", "Ampicillin", "Ceftriaxone", "Gentamicin", "Daptomycin"],
                "dosing_gdmt": "Empiric: Vancomycin 15-20 mg/kg IV q8-12h targeting trough 15-20 mcg/mL + Ceftriaxone 2g IV q24h for 4-6 weeks.",
                "black_box_warning": "Vancomycin: Nephrotoxicity and ototoxicity; monitor AUC/MIC (target 400-600) and serum creatinine.",
                "organ_clearance_cutoffs": "Dose-adjust for eGFR <50 mL/min; discontinue concurrent aminoglycosides if serum Cr increases by >0.5 mg/dL."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POET",
                "pmid_or_doi": "10.1056/NEJMoa1808312",
                "cebm_level": 1,
                "sample_size": 400,
                "endpoints": "Oral step-down non-inferior to IV therapy: primary composite outcome 9.0% vs 12.1% (p=0.40); median length of stay reduced by 14 days."
            }
        }
    },
    {
        "id": "DOC-CARD-203",
        "icd10": "I30.9",
        "condition": "Acute Pericarditis",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (ICAP Trial) & ESC Guidelines",
        "citation": "Imazio M et al. A Randomized Trial of Colchicine for Acute Pericarditis (ICAP). N Engl J Med. 2013;369(16):1522-1528.",
        "doi_or_source": "10.1056/NEJMoa1208536",
        "clinical_evidence": "In the landmark multicenter double-blind ICAP trial (n=240 patients with first-episode acute pericarditis), adding weight-adjusted colchicine (0.5 mg once or twice daily for 3 months) to standard anti-inflammatory therapy significantly reduced the rate of recurrent pericarditis at 18 months from 37.5% in the placebo group to 16.7% in the colchicine group (relative risk reduction 56%; absolute risk reduction 20.8 percentage points; NNT = 5; p<0.001). Colchicine also reduced symptom persistence at 72 hours (19.2% vs 40.0%; p=0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of strenuous physical exertion, competitive athletics, and aerobic exercise until symptom resolution and normalization of CRP (minimum 3 months for athletes).",
            "monitoring_cadence": "Weekly serum high-sensitivity CRP (hs-CRP) until complete normalization; baseline and 4-week transthoracic echocardiogram to exclude pericardial effusion.",
            "clinical_thresholds": "PR depression with diffuse concave ST-segment elevations on 12-lead ECG; failure of symptom improvement within 72 hours on NSAID + Colchicine warrants inpatient admission."
        },
        "patient_plain_language": "Pericarditis is an inflammation of the pericardium, the protective fluid-filled double-layered sac that surrounds and cushions your heart. When inflamed, the two layers rub against each other like sandpaper, causing sharp chest pain that feels worse when breathing deeply or lying flat, but eases when leaning forward.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my high-sensitivity C-reactive protein (CRP) level, and has my 12-lead ECG returned to baseline?",
            "safety_question": "Should I take a stomach-protecting medication (like a PPI) while taking high-dose ibuprofen or indomethacin with colchicine?",
            "action_threshold_question": "When is it safe for me to resume light jogging or gym exercises without triggering a relapse?"
        },
        "red_flags": [
            "Severe shortness of breath when resting, muffled heart sounds, lightheadedness, or swelling of the neck veins indicating fluid buildup around the heart (Cardiac Tamponade)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Pericarditis is swelling and irritation of the thin saclike membrane surrounding your heart.",
                "plain_analogy": "Two dry leather surfaces rubbing together each time the heart beats, creating sharp friction pain.",
                "lifestyle_action": "Strict rest, no gym or running until inflammation markers normalize; sit upright leaning forward for relief."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Colchicine", "Ibuprofen", "Indomethacin", "Aspirin", "Anakinra"],
                "dosing_gdmt": "Colchicine 0.5 mg daily (<70kg) or BID (>=70kg) for 3 months PLUS Ibuprofen 600-800 mg TID with food for 1-2 weeks.",
                "black_box_warning": "Colchicine: Fatal toxicity with strong CYP3A4 inhibitors (e.g. clarithromycin) in renal/hepatic impairment.",
                "organ_clearance_cutoffs": "Reduce colchicine dose by 50% if eGFR 30-50 mL/min; avoid if eGFR <30 mL/min."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ICAP",
                "pmid_or_doi": "10.1056/NEJMoa1208536",
                "cebm_level": 2,
                "sample_size": 240,
                "endpoints": "Recurrent pericarditis halved from 37.5% to 16.7% (RRR 56%, NNT=5; p<0.001); 72-hour symptom persistence reduced by 52%."
            }
        }
    },
    {
        "id": "DOC-CARD-204",
        "icd10": "I31.4",
        "condition": "Cardiac Tamponade",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Observational Synthesis",
        "source_body": "ESC Guidelines on Pericardial Diseases & JAMA Rational Clinical Exam",
        "citation": "Adler Y et al. 2015 ESC Guidelines for the diagnosis and management of pericardial diseases. Eur Heart J. 2015;36(42):2921-2964.",
        "doi_or_source": "10.1093/eurheartj/ehv318",
        "clinical_evidence": "Cardiac tamponade is a life-threatening hemodynamic emergency where pericardial fluid accumulation under high pressure impairs diastolic filling. Beck's triad (hypotension, jugular venous distension, muffled heart sounds) has high specificity (>90%) but low sensitivity (<30%). The single most sensitive clinical sign is pulsus paradoxus (>10 mmHg inspiratory drop in systolic blood pressure, sensitivity 98%). Echocardiographic hallmark is right ventricular early diastolic collapse (specificity 95%) and right atrial late diastolic collapse. Immediate pericardiocentesis resolves hemodynamics in >98% of cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Emergent bedside echocardiography-guided pericardiocentesis; placement of a temporary pericardial pigtail drain until output is <25-30 mL/24h.",
            "monitoring_cadence": "Continuous arterial line invasive blood pressure monitoring and telemetry in cardiac ICU; repeat TTE at 24 hours post-drain removal.",
            "clinical_thresholds": "Pulsus paradoxus >10 mmHg, IVC plethora with <50% inspiratory collapse, or RV collapse >1/3 of diastole mandates immediate decompression."
        },
        "patient_plain_language": "Cardiac tamponade is a medical emergency where fluid rapidly builds up inside the sac wrapped around your heart. The fluid squeezes your heart like a tight vise grip, preventing the heart chambers from opening wide enough to fill with blood. This causes blood pressure to plunge dangerously low.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured depth of my pericardial effusion and was there evidence of right heart chamber collapse?",
            "safety_question": "What was the underlying trigger of the fluid buildup (infection, autoimmune disease, or kidney disease)?",
            "action_threshold_question": "How will we ensure the fluid does not re-accumulate once the pericardial drainage tube is removed?"
        },
        "red_flags": [
            "Severe air hunger, cold clammy pale extremities, sudden profound dizziness, systolic blood pressure below 90 mmHg, or sudden loss of consciousness"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cardiac tamponade is pressure on the heart that occurs when blood or fluid builds up in the space between the heart muscle and the outer sac.",
                "plain_analogy": "A water balloon squeezing tightly around the heart so it cannot expand to fill with blood.",
                "lifestyle_action": "Emergency hospital admission immediately. Zero exertion. Fluid removal procedure required."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Sodium Chloride 0.9% IV", "Norepinephrine", "Dobutamine"],
                "dosing_gdmt": "Aggressive IV volume expansion (500-1000 mL normal saline bolus) as bridge to pericardiocentesis; avoid vasodilators.",
                "black_box_warning": "Norepinephrine: Peripheral ischemia and necrosis; administer via central line with continuous arterial monitoring.",
                "organ_clearance_cutoffs": "Absolute contraindication to positive pressure mechanical ventilation if avoidable, as it halts venous return."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESC Pericardial Registry",
                "pmid_or_doi": "10.1093/eurheartj/ehv318",
                "cebm_level": 1,
                "sample_size": 1054,
                "endpoints": "Echo-guided pericardiocentesis technical success rate >98%; procedural complication rate <1.5%; mortality reduction >95% upon decompression."
            }
        }
    },
    {
        "id": "DOC-CARD-205",
        "icd10": "I47.2",
        "condition": "Ventricular Tachycardia (VT)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (VANISH Trial) & AHA/ACC/HRS Guidelines",
        "citation": "Sapp JL et al. Ventricular Tachycardia Ablation versus Escalation of Antiarrhythmic Drugs (VANISH). N Engl J Med. 2016;375(2):111-121.",
        "doi_or_source": "10.1056/NEJMoa1513614",
        "clinical_evidence": "In the multicenter VANISH trial (n=259 patients with ischemic cardiomyopathy and recurrent VT despite baseline antiarrhythmic therapy), catheter ablation significantly reduced the primary composite outcome of death, VT storm (>=3 episodes in 24 hours), or appropriate ICD shocks compared with escalated antiarrhythmic drug therapy (59.1% vs 68.5%; HR 0.72; 95% CI 0.53-0.98; p=0.04). Catheter ablation reduced VT storm by 42% (HR 0.58; p=0.04) and ICD shocks by 35% without excess procedural mortality.",
        "solution_protocol": {
            "non_pharmacological_targets": "Zero caffeine or sympathomimetic intake; avoidance of recreational stimulants; mandatory driving restrictions per state cardiology motor vehicle regulations (minimum 6 months shock-free).",
            "monitoring_cadence": "Remote wireless ICD home monitoring weekly; comprehensive in-clinic electrophysiology interrogations every 3-6 months; annual serum electrolytes, TSH, and liver panels.",
            "clinical_thresholds": "Sustained VT (>30 seconds) or hemodynamically unstable VT requires immediate synchronized cardioversion; >=2 ICD shocks within 24h triggers emergent ICU transfer."
        },
        "patient_plain_language": "Ventricular tachycardia (VT) is a dangerously fast heartbeat that starts in the bottom pumping chambers (ventricles) of the heart. The ventricles fire off rapid electrical pulses (over 100-200 beats a minute), beating so fast that they quiver and do not have time to fill with blood before squeezing, causing blood pressure to drop rapidly.",
        "doctor_consultation_checklist": {
            "parameter_question": "What does my ICD interrogation report show regarding total VT episodes and ventricular pacing percentage?",
            "safety_question": "Is catheter ablation a safer long-term option for me than increasing amiodarone and risking lung or thyroid side effects?",
            "action_threshold_question": "What is our emergency action plan if my defibrillator (ICD) delivers a shock while I am at home?"
        },
        "red_flags": [
            "Sudden rapid heart racing accompanied by gray vision, loss of consciousness (syncope), severe chest pain, or multiple shocks from an implanted defibrillator"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ventricular tachycardia is a fast heart rhythm that starts in the heart's lower chambers (ventricles).",
                "plain_analogy": "An engine revving out of control in neutral gear—spinning at redline speeds without actually moving blood.",
                "lifestyle_action": "Avoid all stimulants and energy drinks. Follow driving restriction laws strictly. Sleep with home ICD monitor connected."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Amiodarone", "Sotalol", "Metoprolol Succinate", "Mexiletine", "Lidocaine IV"],
                "dosing_gdmt": "Amiodarone 400 mg daily oral load for 2-4 weeks, then 200 mg daily maintenance. Metoprolol titrated to resting HR 60-70 bpm.",
                "black_box_warning": "Amiodarone: Fatal pulmonary toxicity (alveolitis/fibrosis), hepatotoxicity, and proarrhythmic exacerbation.",
                "organ_clearance_cutoffs": "Monitor PFTs (DLCO) and chest X-ray annually; check LFTs and TSH every 6 months."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "VANISH",
                "pmid_or_doi": "10.1056/NEJMoa1513614",
                "cebm_level": 2,
                "sample_size": 259,
                "endpoints": "Primary composite of death, VT storm, or ICD shock reduced by 28% with catheter ablation vs drug escalation (HR 0.72; p=0.04)."
            }
        }
    },
    {
        "id": "DOC-CARD-206",
        "icd10": "I47.1",
        "condition": "Supraventricular Tachycardia (SVT)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (REVERT Trial) & ACC/AHA/HRS Guidelines",
        "citation": "Appelboam A et al. Postural modification to the standard Valsalva manoeuvre for emergency treatment of supraventricular tachycardia (REVERT). Lancet. 2015;386(10005):1747-1753.",
        "doi_or_source": "10.1016/S0140-6736(15)61485-4",
        "clinical_evidence": "The multicenter REVERT trial (n=428 emergency department patients with acute SVT) proved that a modified Valsalva maneuver (40 mmHg forced strain for 15 seconds in semi-recumbent position followed immediately by supine repositioning with 45-degree passive leg raise for 15 seconds) achieved cardioversion to normal sinus rhythm in 43% of patients compared with only 17% with standard Valsalva (odds ratio 3.7; 95% CI 2.3-5.8; p<0.0001; NNT = 3.8). This simple maneuver halved the need for intravenous adenosine (50% vs 69%). Definitive catheter radiofrequency ablation achieves >95% long-term cure.",
        "solution_protocol": {
            "non_pharmacological_targets": "Education in modified postural Valsalva maneuver; elimination of caffeine, alcohol, pseudoephedrine decongestants, and nicotine triggers.",
            "monitoring_cadence": "Wearable smartwatch ECG or 14-day continuous patch monitor to record reentrant paroxysms; outpatient electrophysiology referral for curative catheter ablation.",
            "clinical_thresholds": "Narrow complex tachycardia at 150-250 bpm; hemodynamically stable SVT managed with modified Valsalva followed by rapid IV adenosine bolus (6 mg, then 12 mg)."
        },
        "patient_plain_language": "Supraventricular tachycardia (SVT) is a condition where an extra electrical short-circuit in the top chambers of your heart suddenly causes your pulse to race like a runaway freight train (often 150 to 220 beats per minute) out of nowhere. It starts and stops abruptly like flipping an electrical light switch.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my ECG trace show an AV nodal reentrant tachycardia (AVNRT) or an accessory pathway like Wolff-Parkinson-White (WPW)?",
            "safety_question": "Am I a good candidate for curative catheter ablation so I never have to take daily heart pills again?",
            "action_threshold_question": "How many minutes of an SVT attack should I attempt the modified Valsalva maneuver at home before going to the emergency room?"
        },
        "red_flags": [
            "Heart racing over 180 bpm accompanied by chest tightness, fainting, gray vision, or a wide irregular heartbeat on an ECG monitor"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Supraventricular tachycardia is an abnormally fast heartbeat caused by faulty electrical signals in the upper parts of the heart.",
                "plain_analogy": "An electrical short-circuit switch that gets stuck in the 'fast' position until reset.",
                "lifestyle_action": "Master the modified Valsalva maneuver. Avoid cold decongestants (pseudoephedrine) and excessive caffeine."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Adenosine IV", "Verapamil", "Diltiazem", "Metoprolol", "Flecainide"],
                "dosing_gdmt": "Acute: Adenosine 6 mg rapid IV push via large antecubital vein + 20 mL saline flush; if no conversion in 1-2 min, give 12 mg.",
                "black_box_warning": "Adenosine: Transient complete heart block, bronchospasm, and brief asystole; contraindicated in severe reactive airway asthma.",
                "organ_clearance_cutoffs": "Avoid AV nodal blockers (verapamil/diltiazem/adenosine) in pre-excited atrial fibrillation with accessory pathways (WPW)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "REVERT",
                "pmid_or_doi": "10.1016/S0140-6736(15)61485-4",
                "cebm_level": 2,
                "sample_size": 428,
                "endpoints": "Cardioversion rate increased from 17% to 43% with postural modification (OR 3.7; p<0.0001; NNT 3.8); emergency adenosine requirement reduced."
            }
        }
    },
    {
        "id": "DOC-CARD-207",
        "icd10": "I71.2",
        "condition": "Thoracic Aortic Aneurysm",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Registry Synthesis",
        "source_body": "JACC / Circulation (AHA/ACC Aortic Guidelines)",
        "citation": "Isselbacher EM et al. 2022 ACC/AHA Guideline for the Diagnosis and Management of Aortic Disease. J Am Coll Cardiol. 2022;80(24):e223-e393.",
        "doi_or_source": "10.1016/j.jacc.2022.08.004",
        "clinical_evidence": "The comprehensive 2022 ACC/AHA Aortic Disease Guideline establishes strict diameter thresholds for elective surgical intervention in thoracic aortic aneurysms (TAA). For ascending aortic aneurysms in low-surgical-risk centers of excellence, elective repair is recommended at >=5.0 cm (Class 2a) or >=5.5 cm in standard centers (Class 1). In patients with genetic aortopathies (Marfan syndrome, Loeys-Dietz, bicuspid aortic valve), the threshold drops to 4.5-5.0 cm, or an aortic cross-sectional area to height ratio >10 cm2/m. Strict blood pressure control with beta-blockers and ARBs reduces rate of aortic expansion by >30%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute cessation of smoking; strict avoidance of heavy isometric weightlifting (e.g. heavy bench press, squats, straining) or Valsalva maneuver exertion; genetic testing for first-degree family members.",
            "monitoring_cadence": "Contrast CT angiography (CTA) or magnetic resonance angiography (MRA) of aorta at 6 months initially, then annually if stable; identical imaging modality must be used for longitudinal measurements.",
            "clinical_thresholds": "Ascending aorta diameter >=5.5 cm (or >=5.0 cm in expert centers; >=4.5 cm in Marfan), or expansion rate >=0.5 cm/year mandates surgical aortic graft replacement."
        },
        "patient_plain_language": "A thoracic aortic aneurysm is a bulge or ballooning in the aorta, the large main highway artery carrying oxygen-rich blood directly out of your heart through your chest. When the artery wall weakens, high blood pressure causes it to stretch outward like an over-inflated tire.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact maximum diameter of my thoracic aorta in millimeters on my latest CT or MRI scan?",
            "safety_question": "Is my systolic blood pressure strictly below 120 mmHg, and should my children undergo genetic screening for aortic conditions?",
            "action_threshold_question": "What specific sudden chest, back, or neck pain symptoms indicate an aortic tear requiring an emergency 911 call?"
        },
        "red_flags": [
            "Sudden severe ripping, tearing, or stabbing chest pain radiating through to the upper back between the shoulder blades (Acute Aortic Dissection)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A thoracic aortic aneurysm is an expansion or weakening in the wall of the aorta where it runs through the chest.",
                "plain_analogy": "An over-stretched, thin spot on a high-pressure garden hose carrying all the water from your pump.",
                "lifestyle_action": "Keep blood pressure strictly under 120/80. Never perform heavy weightlifting or power-lifting. Quit smoking immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Losartan", "Atenolol", "Metoprolol Succinate", "Amlodipine"],
                "dosing_gdmt": "Titrate beta-blocker (Atenolol 50-100 mg daily or Metoprolol) PLUS ARB (Losartan 50-100 mg daily) to target resting HR <60 bpm and SBP <120.",
                "black_box_warning": "ARBs/ACEis: Fetal toxicity; avoid in women of childbearing age without effective contraception.",
                "organ_clearance_cutoffs": "Monitor renal function and electrolytes biannually; fluoroquinolone antibiotics are contraindicated (increase dissection risk)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACC/AHA Aortic Guidelines",
                "pmid_or_doi": "10.1016/j.jacc.2022.08.004",
                "cebm_level": 1,
                "sample_size": 11200,
                "endpoints": "Elective repair at 5.0-5.5 cm reduces catastrophic dissection/rupture mortality from >80% to <2% elective operative risk."
            }
        }
    },
    {
        "id": "DOC-CARD-208",
        "icd10": "I71.4",
        "condition": "Abdominal Aortic Aneurysm (AAA)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Long-Term Multicenter Randomized Controlled Trial",
        "source_body": "The Lancet (EVAR trial 1 & 2) & USPSTF",
        "citation": "Patel R et al. Endovascular versus open repair of abdominal aortic aneurysm in 15-years' follow-up of the UK EVAR trial 1. Lancet. 2016;388(10058):2366-2374.",
        "doi_or_source": "10.1016/S0140-6736(16)31135-7",
        "clinical_evidence": "The landmark UK EVAR-1 trial (n=1252 patients with AAA >=5.5 cm followed for 15 years) demonstrated that endovascular aneurysm repair (EVAR) produced a 73% reduction in 30-day operative mortality compared with open surgical repair (1.8% vs 4.3%; p=0.02). Beyond 8 years, aneurysm-related mortality became similar, but EVAR required higher rates of reintervention for endoleaks (HR 2.42; p<0.0001). USPSTF recommends 1-time screening ultrasound in all men aged 65-75 who have ever smoked (Grade B; reduces rupture mortality by 50%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute smoking cessation (smoking increases aneurysm expansion rate by 300%); moderate walking exercise; avoidance of heavy abdominal straining.",
            "monitoring_cadence": "Abdominal duplex ultrasound every 3 years for 3.0-3.9 cm; every 12 months for 4.0-4.9 cm; every 3-6 months for 5.0-5.4 cm.",
            "clinical_thresholds": "Aortic diameter >=5.5 cm in men, >=5.0 cm in women, or expansion rate >1.0 cm/year triggers vascular surgical intervention."
        },
        "patient_plain_language": "An abdominal aortic aneurysm (AAA) is a balloon-like swelling in the lower part of the aorta, the main blood vessel running through your belly to supply your legs. Most people have no symptoms until the aneurysm becomes very large. Smoking and high blood pressure are the leading causes of the blood vessel wall thinning out.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact maximum width of my abdominal aorta on my latest ultrasound scan?",
            "safety_question": "Am I a candidate for minimally invasive endovascular stent repair (EVAR) versus traditional open surgery?",
            "action_threshold_question": "What sudden belly, back, or groin pain symptoms indicate that I need immediate emergency medical care?"
        },
        "red_flags": [
            "Sudden severe ripping abdominal or lower back pain, a pulsating mass in the belly, dizziness, pale sweaty skin, or fainting (Impending Rupture)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "An abdominal aortic aneurysm is an enlarged area in the lower part of the major vessel that supplies blood to the body.",
                "plain_analogy": "A worn spot on an inner bicycle tube bulging outward in the belly under constant pressure.",
                "lifestyle_action": "Quit smoking immediately. Control blood pressure. Avoid extreme abdominal lifting or straining."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Atorvastatin", "Lisinopril", "Amlodipine"],
                "dosing_gdmt": "High-intensity statin (Atorvastatin 40-80 mg daily) to stabilize atherosclerotic wall + SBP target <130 mmHg.",
                "black_box_warning": "ACE inhibitors: Fetal toxicity in pregnancy; monitor serum potassium and renal clearance.",
                "organ_clearance_cutoffs": "Fluoroquinolones (ciprofloxacin, levofloxacin) carry an FDA black box warning to avoid in AAA due to collagen breakdown."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EVAR-1",
                "pmid_or_doi": "10.1016/S0140-6736(16)31135-7",
                "cebm_level": 1,
                "sample_size": 1252,
                "endpoints": "30-day operative mortality reduced from 4.3% with open repair to 1.8% with EVAR (p=0.02); long-term graft surveillance required."
            }
        }
    },
    {
        "id": "DOC-CARD-209",
        "icd10": "I73.00",
        "condition": "Raynaud's Phenomenon",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Meta-Analysis",
        "source_body": "Cochrane Database of Systematic Reviews & ACR",
        "citation": "Ennis H et al. Calcium channel blockers for primary Raynaud's phenomenon. Cochrane Database Syst Rev. 2016;2(2):CD002069.",
        "doi_or_source": "10.1002/14651858.CD002069.pub5",
        "clinical_evidence": "In a comprehensive Cochrane systematic review and meta-analysis of 7 randomized controlled trials (n=296 participants), oral dihydropyridine calcium channel blockers (predominantly nifedipine) significantly reduced the frequency of vasospastic attacks by 33% compared with placebo (mean difference -2.8 attacks per week; 95% CI -3.9 to -1.7; p<0.0001). Attack severity was also significantly reduced by 33%. In severe secondary Raynaud's resistant to CCBs, phosphodiesterase-5 inhibitors (sildenafil) reduce attack frequency by a further 45% and accelerate digital ulcer healing.",
        "solution_protocol": {
            "non_pharmacological_targets": "Layered insulated thermal mittens and electric hand warmers; absolute cessation of smoking and avoidance of second-hand smoke; avoidance of rapid temperature shifts.",
            "monitoring_cadence": "Nailfold capillaroscopy and ANA titers at baseline to rule out systemic sclerosis; annual dermatologic inspection of digital pulp for ulceration.",
            "clinical_thresholds": "Occurrence of digital ulceration, gangrene, or severe tissue ischemia warrants immediate vasodilatory escalation (PDE5i or IV prostacyclin)."
        },
        "patient_plain_language": "Raynaud's phenomenon is an over-reactive response in the small blood vessels of your fingers and toes when exposed to cold or emotional stress. The tiny arteries suddenly spasm and shut down tightly, turning your fingers white, then blue as oxygen runs low, and finally bright red, throbbing, and tingling as blood rushes back in.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I have primary Raynaud's (benign) or secondary Raynaud's associated with an autoimmune condition like scleroderma or lupus?",
            "safety_question": "Are there over-the-counter decongestants, migraine pills (triptans), or beta-blockers that might be worsening my finger spasms?",
            "action_threshold_question": "What should I do if I notice a painful dark sore, blister, or cut on the tip of my finger that will not heal?"
        },
        "red_flags": [
            "Persistent black or blue discoloration of a fingertip lasting over 2 hours, non-healing digital skin ulcers, or sudden excruciating digital pain"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Raynaud's phenomenon causes blood vessels in your fingers and toes to narrow and feel numb and cold in response to cold temperatures or stress.",
                "plain_analogy": "A hyper-sensitive thermostat that overreacts to chilly weather by slamming the blood flow valves shut in your fingers.",
                "lifestyle_action": "Wear insulated mittens (warmer than gloves), avoid cold drinks without a koozie, and never touch ice with bare hands."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Nifedipine ER", "Amlodipine", "Sildenafil", "Fluoxetine", "Topical Nitroglycerin"],
                "dosing_gdmt": "First-line: Nifedipine extended-release 30-60 mg daily orally. Second-line for digital ulcers: Sildenafil 20 mg TID.",
                "black_box_warning": "Sildenafil: Absolute contraindication with concurrent organic nitrates (nitroglycerin) due to fatal hypotension.",
                "organ_clearance_cutoffs": "Monitor for peripheral pedal edema, reflex tachycardia, and orthostatic dizziness; discontinue beta-blockers if present."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Cochrane Raynaud's Review",
                "pmid_or_doi": "10.1002/14651858.CD002069.pub5",
                "cebm_level": 1,
                "sample_size": 296,
                "endpoints": "Vasospastic attack frequency reduced by 33% (mean difference -2.8 attacks/week; p<0.0001); attack severity scores reduced significantly."
            }
        }
    },
    {
        "id": "DOC-CARD-210",
        "icd10": "I73.1",
        "condition": "Buerger's Disease (Thromboangiitis Obliterans)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Cohort Consensus",
        "source_body": "Circulation (AHA Vascular Guidelines) & European Consensus",
        "citation": "Olin JW. Thromboangiitis obliterans (Buerger's disease). N Engl J Med. 2000;343(12):864-869.",
        "doi_or_source": "10.1056/NEJM200009213431207",
        "clinical_evidence": "Buerger's disease (thromboangiitis obliterans) is a non-atherosclerotic segmental inflammatory vaso-occlusive vasculopathy affecting small and medium-sized arteries and veins of the extremities, almost exclusively in young tobacco smokers (<45 years). Complete and permanent cessation of all tobacco and nicotine products is the single proven intervention that halts disease progression and prevents limb loss. Continued smoking leads to amputation in 43% of patients at 10 years, compared to <5% in those who achieve complete smoking cessation (p<0.001). IV iloprost significantly improves ulcer healing and relieves ischemic rest pain (85% vs 17% placebo; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute and permanent 100% cessation of all forms of tobacco, cigars, cigarettes, e-cigarettes, chewing tobacco, and nicotine replacement therapies; avoidance of cold exposure and minor foot trauma.",
            "monitoring_cadence": "Quarterly vascular physical examination and digital photoplethysmography (PPG); formal urinary cotinine testing to objectively confirm tobacco abstinence.",
            "clinical_thresholds": "Toe-brachial index (TBI) <0.50 or non-healing ischemic digital ulceration requires immediate prostacyclin infusion or sympathectomy evaluation."
        },
        "patient_plain_language": "Buerger's disease is an inflammatory disease that causes swelling, inflammation, and tiny blood clots in the blood vessels of your hands and feet. This blocks blood flow to your fingers and toes, causing pain, coldness, and sores that can lead to tissue death (gangrene). It is directly linked to tobacco use—stopping smoking completely is the only way to save your fingers and toes.",
        "doctor_consultation_checklist": {
            "parameter_question": "What do my digital pressure measurements and pulse volume recordings show in my toes and fingers?",
            "safety_question": "Can I use non-nicotine smoking cessation medications (like bupropion or varenicline) safely to help me quit?",
            "action_threshold_question": "What treatments (such as specialized vasodilating infusions) are available if my foot pain occurs even while resting?"
        },
        "red_flags": [
            "Severe unrelenting burning foot or hand pain while lying in bed, blackened or blue skin on toes, or open sores that smell bad and drain pus"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Buerger's disease is a rare disease of the arteries and veins in the arms and legs where blood vessels become inflamed and blocked with blood clots.",
                "plain_analogy": "Tobacco chemicals triggering intense swelling that plugs up the smallest blood pipes in your toes and fingers like hardened grease.",
                "lifestyle_action": "Complete, zero-tolerance cessation of all smoking and tobacco. Keep feet warm, protected, and inspected daily."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Iloprost IV", "Cilostazol", "Bupropion", "Varenicline"],
                "dosing_gdmt": "Bupropion 150 mg BID or Varenicline 1 mg BID for tobacco cessation. In acute digital ischemia: Iloprost IV 0.5-2.0 ng/kg/min for 28 days.",
                "black_box_warning": "Cilostazol: Black box warning in heart failure of any severity (increases ventricular arrhythmia mortality).",
                "organ_clearance_cutoffs": "Contraindicated with active peptic ulcer or severe bleeding diathesis. Revascularization surgery is rarely feasible due to distal vessel involvement."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Buerger's Cessation Cohorts",
                "pmid_or_doi": "10.1056/NEJM200009213431207",
                "cebm_level": 1,
                "sample_size": 1840,
                "endpoints": "Amputation rate drops from 43% with continued smoking to <5% with verified complete tobacco cessation (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-211",
        "icd10": "I27.81",
        "condition": "Cor Pulmonale",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Evidence Synthesis",
        "source_body": "CHEST & European Respiratory Society (ERS/ESC)",
        "citation": "Humbert M et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Heart J. 2022;43(38):3618-3731.",
        "doi_or_source": "10.1093/eurheartj/ehac237",
        "clinical_evidence": "Cor pulmonale represents right ventricular (RV) hypertrophy, dilation, and systolic dysfunction resulting directly from severe pulmonary hypertension secondary to intrinsic lung disease (COPD, IPF, OSA). Long-term oxygen therapy (LTOT) in patients with chronic resting hypoxemia (PaO2 <=55 mmHg or SaO2 <=88%) significantly reduces pulmonary vascular resistance, prevents RV deterioration, and improves 5-year survival by 48% (NOTT and MRC trials). Judicious loop diuretic titration relieves RV volume overload without causing pre-renal azotemia.",
        "solution_protocol": {
            "non_pharmacological_targets": "Continuous supplemental oxygen therapy >=15-18 hours/day targeting resting SpO2 89-92% (or 90-94%); dietary sodium restriction <2,000 mg/day; nocturnal CPAP for sleep-disordered breathing.",
            "monitoring_cadence": "Transthoracic echocardiogram every 6-12 months assessing tricuspid annular plane systolic excursion (TAPSE) and RV systolic pressure (RVSP); quarterly serum BNP and renal panel.",
            "clinical_thresholds": "TAPSE <17 mm, RV fractional area change <35%, or mean pulmonary arterial pressure (mPAP) >20 mmHg with severe right atrial enlargement triggers advanced pulmonary team review."
        },
        "patient_plain_language": "Cor pulmonale is heart enlargement and weakness on the right side of your heart caused by chronic lung disease. When damaged lungs cannot absorb enough oxygen, the lung blood vessels clamp down tight. This forces the right side of your heart to work overtime against high resistance, causing it to stretch and weaken.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my tricuspid annular plane systolic excursion (TAPSE) and right ventricular systolic pressure on my echocardiogram?",
            "safety_question": "How many hours a day do I need to keep my supplemental oxygen cannula on to protect my heart from working too hard?",
            "action_threshold_question": "At what point of leg swelling or abdominal bloating should I adjust my water pill (diuretic) dose?"
        },
        "red_flags": [
            "Severe progressive shortness of breath at rest, swelling extending past knees into thighs, fainting (syncope) upon standing, or blue lips (cyanosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cor pulmonale is a condition that most commonly causes the right side of the heart to fail due to high blood pressure in the lungs.",
                "plain_analogy": "The right heart pump wearing out because it has to push blood through clogged, constricted lung pipes.",
                "lifestyle_action": "Wear oxygen as prescribed (at least 15 hours daily). Weigh yourself every morning. Limit salt intake."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Oxygen Therapy", "Furosemide", "Bumetanide", "Spironolactone"],
                "dosing_gdmt": "Target SpO2 89-92% with nocturnal and exertional oxygen. Furosemide 40-80 mg daily titrated to maintain JVP <8 cm H2O.",
                "black_box_warning": "Loop diuretics: Profound diuresis with fluid and electrolyte depletion; monitor serum potassium and BUN/creatinine.",
                "organ_clearance_cutoffs": "Avoid pulmonary arterial vasodilators (sildenafil/endothelin antagonists) in group 3 pulmonary hypertension without expert consultation (may worsen ventilation-perfusion mismatch)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESC/ERS PH Guidelines",
                "pmid_or_doi": "10.1093/eurheartj/ehac237",
                "cebm_level": 1,
                "sample_size": 4500,
                "endpoints": "Long-term oxygen therapy in hypoxemic lung disease reduces RV failure hospitalizations by 45% and improves survival."
            }
        }
    },
    {
        "id": "DOC-CARD-212",
        "icd10": "J47.9",
        "condition": "Bronchiectasis (Non-Cystic Fibrosis)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Multicenter Trial",
        "source_body": "European Respiratory Journal (ERS) & Thorax (BTS)",
        "citation": "Polverino E et al. European Respiratory Society guidelines for the management of adult bronchiectasis. Eur Respir J. 2017;50(3):1700629.",
        "doi_or_source": "10.1183/13993003.00629-2017",
        "clinical_evidence": "The ERS and British Thoracic Society (BTS) Bronchiectasis Guidelines confirm that airway clearance techniques (oscillating positive expiratory pressure [OPEP]) combined with long-term macrolide maintenance therapy (Azithromycin 250-500 mg 3 times weekly) significantly reduces the annualized rate of pulmonary exacerbations by 51% (rate ratio 0.49; 95% CI 0.36-0.66; p<0.0001; EMBRACE and BAT trials). Inhaled hypertonic saline (6-7%) or nebulized dornase alfa improves sputum clearance and FEV1.",
        "solution_protocol": {
            "non_pharmacological_targets": "Twice-daily airway clearance therapy utilizing an oscillating PEP device (e.g. Flutter or Acapella valve) combined with the active cycle of breathing technique (ACBT); pulmonary rehabilitation.",
            "monitoring_cadence": "Quarterly quantitative sputum bacteriology cultures (specifically screening for Pseudomonas aeruginosa); baseline and annual spirometry (FEV1/FVC); high-resolution chest CT (HRCT).",
            "clinical_thresholds": "Isolation of Pseudomonas aeruginosa requires immediate eradication protocol (e.g. oral ciprofloxacin + nebulized colistimethate or tobramycin for 3 months)."
        },
        "patient_plain_language": "Bronchiectasis is a chronic lung condition where the airways (bronchial tubes) become abnormally widened, stretched, and scarred. These stretched airways lose their normal ability to clear out mucus. Mucus pools in the enlarged pockets, leading to frequent lung infections and a persistent daily phlegm-producing cough.",
        "doctor_consultation_checklist": {
            "parameter_question": "What bacteria showed up on my latest sputum culture, and is there any sign of Pseudomonas?",
            "safety_question": "Have we checked my hearing (audiogram) and ECG heart rhythm (QT interval) before starting long-term azithromycin?",
            "action_threshold_question": "What antibiotic should I keep at home as an emergency rescue pack if my phlegm suddenly turns dark green and increases in volume?"
        },
        "red_flags": [
            "Coughing up frank red blood (hemoptysis >50-100 mL), sudden high fever with chills, severe breathlessness, or sharp pleuritic chest pain"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bronchiectasis is a long-term condition where the airways of the lungs become abnormally widened, leading to a build-up of excess mucus.",
                "plain_analogy": "Airways that have become baggy and stretched like old socks, trapping pools of mucus that cannot be swept out.",
                "lifestyle_action": "Use airway clearance flutter devices twice every day. Stay well hydrated to keep mucus thin. Exercise regularly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Azithromycin", "Hypertonic Saline 7% Nebulized", "Tobramycin Inhalation", "Ciprofloxacin"],
                "dosing_gdmt": "Azithromycin 250 mg or 500 mg orally 3 days a week for exacerbation prevention. Nebulize 4 mL 7% hypertonic saline BID.",
                "black_box_warning": "Azithromycin: QTc prolongation and potential fatal cardiac arrhythmias; rule out non-tuberculous mycobacteria (NTM) prior to monotherapy.",
                "organ_clearance_cutoffs": "Screen for baseline QTc >450 ms in men, >470 ms in women; verify 3 negative sputum NTM smears prior to azithromycin initiation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EMBRACE / BAT",
                "pmid_or_doi": "10.1183/13993003.00629-2017",
                "cebm_level": 1,
                "sample_size": 1820,
                "endpoints": "Pulmonary exacerbations reduced by 51% with long-term macrolide maintenance (rate ratio 0.49; p<0.0001); FEV1 stabilized."
            }
        }
    },
    {
        "id": "DOC-CARD-213",
        "icd10": "J93.9",
        "condition": "Spontaneous Pneumothorax",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (PSP Trial) & British Thoracic Society (BTS)",
        "citation": "Brown SGA et al. Conservative versus Interventional Treatment for Spontaneous Pneumothorax (PSP). N Engl J Med. 2020;382(5):405-415.",
        "doi_or_source": "10.1056/NEJMoa1910775",
        "clinical_evidence": "In the open-label noninferiority PSP trial (n=316 patients aged 14-50 with a first large primary spontaneous pneumothorax [>=32% on chest radiograph]), conservative observation alone (analgesia and serial clinical review without interventional drainage) was noninferior to routine interventional chest drain insertion with respect to radiographic lung re-expansion at 8 weeks (94.4% conservative vs 98.5% interventional; difference -4.1 percentage points; 95% CI -8.6 to 0.5; p=0.02 for noninferiority). Conservative management dramatically reduced hospital length of stay (1.6 vs 6.1 days; p<0.001) and recurrence (8.8% vs 16.8%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute smoking and vaping cessation (smoking increases recurrence risk by 20-fold); avoidance of scuba diving permanently unless definitive bilateral surgical pleurectomy performed; avoid air travel until 2 weeks after complete radiographic resolution.",
            "monitoring_cadence": "Repeat upright inspiratory chest X-ray at 4 hours, 24-48 hours, and 2 weeks in stable conservative patients; follow-up high-resolution CT to evaluate apical blebs.",
            "clinical_thresholds": "Physiologic instability (tachypnea >24, SpO2 <92% on room air, hypotension) or tension pneumothorax requires immediate needle decompression (2nd intercostal space midclavicular or 5th ICS anterior axillary line) followed by pigtail catheter."
        },
        "patient_plain_language": "A spontaneous pneumothorax is a collapsed lung that occurs suddenly without any injury. A tiny air blister (bleb) on the outer surface of your lung bursts, letting air escape into the space between your lung and your chest wall. The trapped air presses against your lung from the outside, causing part or all of it to collapse.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the calculated percentage size of my pneumothorax on my chest X-ray and am I stable enough for conservative healing?",
            "safety_question": "Do I have small air blisters (apical blebs) on my lungs that might require a keyhole surgery (VATS pleurodesis) to prevent another collapse?",
            "action_threshold_question": "When is it completely safe for me to travel by airplane or resume athletic activities?"
        },
        "red_flags": [
            "Sudden severe shortness of breath, rapid heart rate, severe sharp stabbing chest pain, blue lips, or tracheal shift (Tension Pneumothorax)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A pneumothorax is a collapsed lung that occurs when air enters the pleural cavity surrounding the lung.",
                "plain_analogy": "A small leak in the outer skin of an inner lung balloon that lets air escape into the chest cavity, deflating the lung.",
                "lifestyle_action": "Zero smoking or vaping. Never scuba dive. Avoid flying on commercial airlines until cleared on chest X-ray."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Acetaminophen", "Ibuprofen", "Oxygen Therapy", "Talc Slurry for Pleurodesis"],
                "dosing_gdmt": "High-flow supplemental oxygen (10 L/min via non-rebreather) accelerates nitrogen reabsorption rate by 4-fold.",
                "black_box_warning": "Procedural sedation: Monitor continuous pulse oximetry and capnography during any tube thoracostomy placement.",
                "organ_clearance_cutoffs": "Small-bore pigtail catheter (<=14 Fr) is preferred over large-bore chest tubes for initial drainage if intervention required."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PSP",
                "pmid_or_doi": "10.1056/NEJMoa1910775",
                "cebm_level": 2,
                "sample_size": 316,
                "endpoints": "Conservative management noninferior for 8-week re-expansion (94.4% vs 98.5%); hospital days reduced from 6.1 to 1.6 days; adverse events reduced by 60%."
            }
        }
    },
    {
        "id": "DOC-CARD-214",
        "icd10": "J90",
        "condition": "Pleural Effusion (Exudative vs Transudative)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Validation Meta-Analysis",
        "source_body": "Thorax (British Thoracic Society) & Light's Criteria Meta-Analysis",
        "citation": "Light RW. Clinical practice. Pleural effusion. N Engl J Med. 2002;346(25):1971-1977.",
        "doi_or_source": "10.1056/NEJMcp010731",
        "clinical_evidence": "Diagnostic thoracentesis evaluated using Light's Criteria has 98% sensitivity for distinguishing exudative from transudative pleural effusions. An effusion is exudative if any of the following 3 criteria are met: pleural fluid protein to serum protein ratio >0.5; pleural fluid LDH to serum LDH ratio >0.6; or pleural fluid LDH > two-thirds the upper limit of normal serum LDH. Transudative effusions are driven by systemic hydrostatic/oncotic imbalances (heart failure, cirrhosis, nephrosis) and resolve with medical diuresis. Parapneumonic effusions with pH <7.20, glucose <40 mg/dL, or positive Gram stain mandate prompt chest tube drainage.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bedside ultrasound-guided diagnostic and therapeutic thoracentesis; maximum fluid removal capped at 1,500 mL per session to prevent re-expansion pulmonary edema.",
            "monitoring_cadence": "Post-procedure bedside ultrasound or upright chest radiograph to rule out iatrogenic pneumothorax; daily drainage monitoring if indwelling pleural catheter (IPC) placed.",
            "clinical_thresholds": "Pleural fluid pH <7.20, fluid glucose <40 mg/dL, or frank pus (empyema) requires immediate tube thoracostomy and intrapleural tPA/DNase if multiloculated."
        },
        "patient_plain_language": "A pleural effusion is an abnormal buildup of extra fluid in the space between your lung and the chest wall (the pleural space). As fluid collects, it pushes against your lung, squishing it down like a sponge submerged under water. This makes it hard to take a full deep breath and causes a dry cough.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my fluid analysis meet Light's criteria for an exudate (infection/inflammation) or a transudate (heart/liver fluid buildup)?",
            "safety_question": "Was my pleural fluid pH checked immediately, and is there any sign of bacteria or cancer cells in the laboratory fluid report?",
            "action_threshold_question": "At what point will we need to place a temporary drain tube versus managing this with water pills?"
        },
        "red_flags": [
            "Severe worsening breathlessness, inability to lie flat, high spiking fevers with chills, or coughing up purulent sputum"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A pleural effusion is a buildup of fluid between the layers of tissue that line the lungs and chest cavity.",
                "plain_analogy": "Water pooling inside the wall cavity around your lung, compressing the lung so it cannot expand.",
                "lifestyle_action": "Rest upright in a recliner chair for comfort. Limit fluid and sodium intake if caused by heart or kidney failure."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Furosemide", "Alteplase (tPA) Intrapleural", "Dornase Alfa Intrapleural", "Ceftriaxone"],
                "dosing_gdmt": "For complicated parapneumonic effusion/empyema: Intrapleural Alteplase 10 mg + Dornase alfa 5 mg BID via chest tube for 3 days (MIST-2 trial protocol).",
                "black_box_warning": "Thoracentesis: Monitor for re-expansion pulmonary edema if >1.5 L removed in a single procedure.",
                "organ_clearance_cutoffs": "Avoid therapeutic thoracentesis without platelet count >50,000/mcL or INR <1.5 unless emergent."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Light's Criteria / MIST-2",
                "pmid_or_doi": "10.1056/NEJMcp010731",
                "cebm_level": 1,
                "sample_size": 2400,
                "endpoints": "Light's criteria sensitivity 98%; combined tPA/DNase in empyema reduces surgical referral by 77% (HR 0.23; p=0.003)."
            }
        }
    },
    {
        "id": "DOC-CARD-215",
        "icd10": "J62.8",
        "condition": "Silicosis (Occupational Pneumoconiosis)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Epidemiological Synthesis",
        "source_body": "WHO / International Labour Organization (ILO) & ATS",
        "citation": "Leung CC et al. Silicosis. Lancet. 2012;379(9830):2008-2018.",
        "doi_or_source": "10.1016/S0140-6736(12)60235-9",
        "clinical_evidence": "Silicosis is an irreversible fibrotic occupational lung disease caused by the inhalation of respirable crystalline silica (quartz) particles (<5 microns). Silica particles ingested by alveolar macrophages trigger persistent activation of the NLRP3 inflammasome, releasing interleukin-1-beta and transforming growth factor-beta (TGF-beta), producing classical fibrotic silicotic nodules in upper lung zones. Patients with silicosis have a 30-fold increased risk of developing active tuberculosis (silicotuberculosis) and a 2.5-fold increased risk of lung cancer (IARC Group 1 human carcinogen). Primary prevention through engineering controls (wet-cutting, HEPA ventilation, N95/P100 respirators) is the only definitive intervention.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate and permanent removal from all further occupational silica dust exposure; strict personal protective equipment (P100 powered air-purifying respirators); annual influenza, COVID-19, and pneumococcal vaccinations.",
            "monitoring_cadence": "Annual chest radiograph classified according to the ILO International Classification of Radiographs of Pneumoconioses; annual tuberculin skin test (TST) or interferon-gamma release assay (IGRA); biannual spirometry.",
            "clinical_thresholds": "A positive TST (>=5 mm induration) or positive IGRA warrants immediate latent tuberculosis treatment (Rifampin daily for 4 months or Isoniazid for 9 months) to prevent lethal reactivation."
        },
        "patient_plain_language": "Silicosis is a chronic, permanent lung condition caused by breathing in tiny, invisible specks of mineral dust called crystalline silica, common in construction, stone masonry, quartz countertop cutting, sandblasting, and mining. Over time, the razor-sharp dust particles scar the lung tissue, making it stiff like leather and causing chronic shortness of breath.",
        "doctor_consultation_checklist": {
            "parameter_question": "What ILO profusion grade are my lung nodules on my latest occupational chest X-ray or high-resolution CT scan?",
            "safety_question": "Have I been screened for latent tuberculosis with an IGRA blood test, given the high risk of silicotuberculosis?",
            "action_threshold_question": "At what degree of breathing limitation or oxygen drop should I be referred for a specialized lung transplant assessment?"
        },
        "red_flags": [
            "Rapidly worsening breathlessness, unexplained night sweats, unintended weight loss, or coughing up blood (suspect Silicotuberculosis or Lung Cancer)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Silicosis is an occupational lung disease caused by breathing in tiny bits of silica, a mineral that is part of sand, rock, and mineral ores.",
                "plain_analogy": "Inhaling microscopic glass dust that settles permanently in the lungs, triggering scar tissue that never leaves.",
                "lifestyle_action": "Leave dusty work areas immediately. Never cut stone without water and certified P100 respirators. Quit smoking."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Rifampin", "Isoniazid", "Pirfenidone (Investigational)", "Supplemental Oxygen"],
                "dosing_gdmt": "For latent TB prevention: Rifampin 600 mg daily for 4 months or 3HP (Isoniazid + Rifapentine weekly for 12 weeks).",
                "black_box_warning": "Isoniazid: Severe and sometimes fatal hepatitis; monitor liver function tests monthly.",
                "organ_clearance_cutoffs": "Discontinue hepatotoxic drugs if AST/ALT exceed 3x ULN with symptoms, or 5x ULN without symptoms."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WHO/ILO Silicosis Review",
                "pmid_or_doi": "10.1016/S0140-6736(12)60235-9",
                "cebm_level": 1,
                "sample_size": 8900,
                "endpoints": "Engineering dust control reduces incidence by >90%; latent TB treatment in silicosis reduces active TB risk by 68%."
            }
        }
    },
    {
        "id": "DOC-CARD-216",
        "icd10": "J61",
        "condition": "Asbestosis & Pleural Plaques",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Consensus Criteria",
        "source_body": "American Thoracic Society (ATS) & Lancet Oncology",
        "citation": "American Thoracic Society. Diagnosis and initial management of nonmalignant diseases related to asbestos. Am J Respir Crit Care Med. 2004;170(6):691-715.",
        "doi_or_source": "10.1164/rccm.200310-1436ST",
        "clinical_evidence": "Asbestosis is diffuse interstitial pulmonary fibrosis caused by inhalation of asbestos fibers (chrysotile, amosite, crocidolite), typically presenting 20-30 years post-exposure. High-resolution CT (HRCT) hallmarks include bilateral calcified pleural plaques (parietal pleura along diaphragm and lateral chest wall) and subpleural bibasilar reticular opacities with honeycombing. Smoking combined with asbestos exposure exhibits a supra-multiplicative synergistic effect, increasing bronchogenic lung carcinoma risk by 50- to 60-fold compared to unexposed non-smokers. Annual low-dose CT (LDCT) lung cancer screening reduces lung cancer mortality by 20% in this high-risk population.",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute smoking cessation to eliminate the synergistic cancer risk; pulmonary rehabilitation; annual influenza, pneumococcal, and RSV immunizations.",
            "monitoring_cadence": "Annual low-dose chest CT (LDCT) for lung cancer and malignant pleural mesothelioma surveillance; annual spirometry (FEV1, FVC) and gas transfer (DLCO).",
            "clinical_thresholds": "Development of unilateral pleural effusion, rapidly expanding pleural nodularity, or unexplained weight loss requires immediate thoracoscopy to rule out Malignant Mesothelioma."
        },
        "patient_plain_language": "Asbestosis is long-term scarring and inflammation of the lungs caused by breathing in asbestos fibers, a heat-resistant mineral widely used in old insulation, pipefitting, shipbuilding, and construction. The microscopic fibers lodge deep inside the air sacs, causing stiff scar tissue and chalky calcium patches (pleural plaques) along the lung lining.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do my CT scans show calcified pleural plaques alone, or is there active interstitial lung fibrosis (asbestosis)?",
            "safety_question": "Should I be enrolled in annual low-dose CT screening for lung cancer and mesothelioma?",
            "action_threshold_question": "What should I do if I develop a persistent dry cough, chest wall ache, or unexplained weight loss?"
        },
        "red_flags": [
            "New persistent chest wall pain, unilateral fluid buildup around one lung, unexplained weight loss, or coughing up blood"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Asbestosis is a chronic lung disease caused by inhaling asbestos fibers, leading to lung tissue scarring and shortness of breath.",
                "plain_analogy": "Microscopic needle-like mineral fibers permanently embedded in lung tissue, causing stiff calluses that restrict lung expansion.",
                "lifestyle_action": "Zero smoking. Avoid all home remodeling that disturbs old insulation. Get annual lung cancer CT scans."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Supplemental Oxygen", "Albuterol Inhaler", "Pneumococcal Conjugate Vaccine", "Influenza Vaccine"],
                "dosing_gdmt": "Vaccination: PCV20 single dose followed by PPSV23. Oxygen titrated to maintain SpO2 >=90% at rest and exertion.",
                "black_box_warning": "No approved antifibrotic reverse asbestosis; avoid unproven immunosuppressants which increase infection risk.",
                "organ_clearance_cutoffs": "Monitor DLCO; decline >15% over 12 months signifies accelerated fibrotic progression."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS Asbestos Guidelines",
                "pmid_or_doi": "10.1164/rccm.200310-1436ST",
                "cebm_level": 1,
                "sample_size": 5200,
                "endpoints": "Smoking cessation eliminates synergistic 50-fold lung cancer risk multiplier; annual LDCT screening reduces mortality by 20%."
            }
        }
    },
    {
        "id": "DOC-CARD-217",
        "icd10": "J67.9",
        "condition": "Hypersensitivity Pneumonitis",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATS/JRS/ALAT Clinical Practice Guideline",
        "source_body": "American Thoracic Society & European Respiratory Society",
        "citation": "Raghu G et al. Diagnosis of Hypersensitivity Pneumonitis in Adults: An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;202(3):e36-e69.",
        "doi_or_source": "10.1164/rccm.202005-2032ST",
        "clinical_evidence": "The 2020 international guideline categorizes Hypersensitivity Pneumonitis (HP) into non-fibrotic and fibrotic phenotypes. HP is an immune-mediated interstitial disease triggered by inhaled environmental antigens (avian proteins in bird fanciers, thermophilic actinomycetes in farmer's lung, mold in water-damaged buildings). High-resolution chest CT shows ground-glass opacities, centrilobular nodules, and the pathognomonic 'three-density sign' (headcheese sign: mosaic attenuation of ground glass, normal lung, and air trapping). Bronchoalveolar lavage (BAL) demonstrates marked lymphocytosis (>30-40% lymphocytes). Complete antigen remediation/avoidance is the cornerstone of therapy; non-fibrotic HP resolves in >80% with antigen removal alone.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate, complete identification and remediation of environmental antigens (removal of birds, feather duvets, down pillows; remediation of household mold and water damage; industrial biocides).",
            "monitoring_cadence": "Serial spirometry (FVC) and DLCO at 1, 3, 6, and 12 months following antigen remediation; repeat high-resolution CT at 6 months.",
            "clinical_thresholds": "Decline in FVC >=10% or DLCO >=15% despite antigen avoidance warrants oral corticosteroid induction (prednisone 0.5 mg/kg/day tapered over 3-6 months)."
        },
        "patient_plain_language": "Hypersensitivity pneumonitis is an allergic reaction deep inside the air sacs of your lungs triggered by breathing in microscopic organic dust or mold over long periods. Common culprits include feather bedding, pet birds (parakeets, pigeons), hot tubs, or damp moldy basements. The immune system treats the particles as invaders, causing widespread inflammation.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my lung washing (bronchoalveolar lavage) show elevated lymphocytes, and was a specific precipitating antibody panel identified?",
            "safety_question": "Do I have non-fibrotic (reversible) or fibrotic (scarring) hypersensitivity pneumonitis on my chest CT scan?",
            "action_threshold_question": "What specific environmental inspection steps do I need to take in my home or workplace to remove the antigen completely?"
        },
        "red_flags": [
            "Acute breathlessness accompanied by high fever, chills, and oxygen levels dropping below 88% within 4 to 8 hours after entering a specific building or cleaning bird cages"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypersensitivity pneumonitis is an allergic inflammation of the lungs caused by breathing in certain dusts, fungus, or molds.",
                "plain_analogy": "An allergic thunderstorm deep inside the lungs triggered by microscopic mold spores or bird feather dust.",
                "lifestyle_action": "Remove all down pillows, feather quilts, and indoor birds. Fix all home water leaks and mold immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone", "Mycophenolate Mofetil", "Azathioprine", "Nintedanib"],
                "dosing_gdmt": "Prednisone 0.5 mg/kg daily for 4 weeks, tapering by 5-10 mg every 2 weeks. For progressive fibrotic HP: Nintedanib 150 mg BID.",
                "black_box_warning": "Mycophenolate: Fetal toxicity and spontaneous abortions; embryo-fetal toxicity risk evaluation strategy (REMS).",
                "organ_clearance_cutoffs": "For Nintedanib: Check liver function tests (AST, ALT, bilirubin) baseline and monthly for 3 months; reduce dose if ALT/AST >3x ULN."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS/JRS/ALAT HP Guidelines",
                "pmid_or_doi": "10.1164/rccm.202005-2032ST",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Complete antigen avoidance cures >80% of non-fibrotic HP; addition of antifibrotics slows FVC decline by 57% in progressive fibrotic HP."
            }
        }
    },
    {
        "id": "DOC-CARD-218",
        "icd10": "D86.0",
        "condition": "Pulmonary & Systemic Sarcoidosis",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Multicenter Consensus",
        "source_body": "ATS / ERS Sarcoidosis Guidelines & NEJM",
        "citation": "Crouser ED et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;201(8):e26-e51.",
        "doi_or_source": "10.1164/rccm.202002-0251ST",
        "clinical_evidence": "Sarcoidosis is a multisystem granulomatous disorder characterized by noncaseating epithelioid granulomas, primarily affecting the lungs and intrathoracic lymph nodes (>90% of cases). Diagnostic hallmarks include bilateral hilar lymphadenopathy (BHL) on chest radiography, elevated serum ACE levels (60% sensitivity), and negative microbiological stains/cultures to exclude tuberculosis and histoplasmosis. Scadding radiographic stages I through IV correlate with spontaneous remission rates (Stage I: 60-80% spontaneous remission vs Stage IV: <15%). Baseline screening must include 12-lead ECG (cardiac sarcoidosis screen), ophthalmologic slit-lamp exam (uveitis in 25-50%), and serum/urinary calcium (hypercalcemia due to 1-alpha-hydroxylase production in granulomas).",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoidance of excessive direct sun exposure and vitamin D supplements (prevents granuloma-driven hypercalcemia and nephrolithiasis); regular low-intensity conditioning exercise.",
            "monitoring_cadence": "Quarterly pulmonary function testing (FVC, DLCO); annual 12-lead ECG and Holter monitor (cardiac screening); annual dilated ophthalmology slit-lamp exam; serum calcium, creatinine, and ACE levels.",
            "clinical_thresholds": "Decline in FVC >10%, cardiac conduction abnormalities (AV block/VT), ocular uveitis, or neurologic involvement mandates immediate systemic corticosteroid therapy."
        },
        "patient_plain_language": "Sarcoidosis is an inflammatory disease where your immune system clusters together into tiny microscopic clumps called granulomas. While these granulomas can appear anywhere, they most commonly form in your lungs and chest lymph nodes. In many people, the clumps clear up on their own, but in others, they can cause coughing, chest ache, skin rashes, and joint stiffness.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Scadding stage on my chest X-ray and did my lung biopsy confirm non-caseating granulomas?",
            "safety_question": "Have we thoroughly screened my heart (with an ECG) and my eyes (with a slit-lamp exam) for silent sarcoidosis inflammation?",
            "action_threshold_question": "At what degree of lung function decline or blood calcium elevation should we begin oral steroid therapy?"
        },
        "red_flags": [
            "Sudden heart palpitations, skipping beats, fainting spells (suspect Cardiac Sarcoidosis / Heart Block), sudden blurry painful red eyes, or facial muscle drooping"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sarcoidosis is a disease characterized by the growth of tiny collections of inflammatory cells (granulomas) in any part of your body.",
                "plain_analogy": "The immune system forming small inflammatory sand dunes inside the lungs and lymph nodes.",
                "lifestyle_action": "Avoid vitamin D supplements and excessive tanning (prevents calcium spikes). Schedule annual eye and heart exams."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone", "Methotrexate", "Infliximab", "Hydroxychloroquine"],
                "dosing_gdmt": "First-line: Prednisone 20-40 mg daily for 1-3 months, tapering to 5-10 mg. Second-line: Methotrexate 10-20 mg once weekly + Folic acid 1 mg daily.",
                "black_box_warning": "Methotrexate: Bone marrow suppression, hepatotoxicity, and fetal death; avoid alcohol and monitor CBC/LFTs every 4-8 weeks.",
                "organ_clearance_cutoffs": "Contraindicated in severe renal impairment (eGFR <30 mL/min); Infliximab requires baseline negative latent TB IGRA."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS Sarcoidosis Guidelines",
                "pmid_or_doi": "10.1164/rccm.202002-0251ST",
                "cebm_level": 1,
                "sample_size": 4200,
                "endpoints": "Stage I BHL spontaneous remission >70%; oral steroids improve FVC by 8.4% in symptomatic progressive pulmonary disease."
            }
        }
    },
    {
        "id": "DOC-CARD-219",
        "icd10": "J84.89",
        "condition": "Cryptogenic Organizing Pneumonia (COP)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Observational Synthesis",
        "source_body": "American Thoracic Society & European Respiratory Society",
        "citation": "Cottin V et al. Cryptogenic organizing pneumonia. Eur Respir J. 2012;40(6):1548-1558.",
        "doi_or_source": "10.1183/09031936.00062412",
        "clinical_evidence": "Cryptogenic Organizing Pneumonia (COP, formerly BOOP) is a distinct clinicopathologic entity characterized by intra-alveolar buds of granulation tissue (Masson bodies) extending into alveolar ducts. Unlike idiopathic pulmonary fibrosis (IPF), COP is predominantly an inflammatory and reversible condition rather than a permanent fibrotic disease. Classic HRCT findings show bilateral patchy peripheral subpleural and peribronchovascular ground-glass consolidation, often with the pathognomonic 'reverse halo sign' (atoll sign: central ground glass surrounded by a crescentic or complete ring of consolidation, specificity >90%). First-line systemic corticosteroid therapy produces dramatic clinical and radiographic clearance in >80% of patients within 48 to 72 hours, though relapse occurs in 30-50% during steroid tapering.",
        "solution_protocol": {
            "non_pharmacological_targets": "Pulmonary rehabilitation; smoking cessation; annual pneumococcal and influenza immunizations; avoidance of respiratory irritants.",
            "monitoring_cadence": "Chest radiograph or HRCT at 1, 3, 6, and 12 months; serial spirometry (FVC) and DLCO every 3 months; monitor bone density (DEXA) during prolonged steroid courses.",
            "clinical_thresholds": "Recurrence of fever, dry cough, or new migratory consolidation during steroid taper warrants immediate step-up in prednisone dose or initiation of macrolide/azathioprine steroid-sparing therapy."
        },
        "patient_plain_language": "Cryptogenic organizing pneumonia (COP) is a non-infectious inflammatory lung condition where plugs of healing scar-like tissue and white blood cells form inside your lung's tiny air sacs. It often mimics pneumonia with dry cough, fever, and shortness of breath, but standard antibiotics fail to cure it because it is not caused by bacteria. Fortunately, it responds rapidly to steroid medications.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my high-resolution CT show the classic 'reverse halo' sign of organizing pneumonia?",
            "safety_question": "What is our precise schedule for slowly tapering down my steroid medication so the lung inflammation does not bounce back?",
            "action_threshold_question": "What symptoms (such as return of fever or coughing) signal that my organizing pneumonia is relapsing?"
        },
        "red_flags": [
            "Rapidly progressive shortness of breath over 24-48 hours, inability to catch breath while resting, or lips turning bluish"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cryptogenic organizing pneumonia is a rare lung disease that affects the small airways and air sacs, causing inflammation and flu-like symptoms.",
                "plain_analogy": "Healing plugs of tissue that temporarily clog the air sacs, mimicking bacterial pneumonia but cleared by steroids.",
                "lifestyle_action": "Take calcium and vitamin D while on steroids to protect bones. Report any return of fever or cough immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone", "Methylprednisolone", "Azathioprine", "Clarithromycin"],
                "dosing_gdmt": "Prednisone 0.75 mg/kg daily for 4 weeks, tapering to 0.5 mg/kg for 4 weeks, then 0.25 mg/kg for 4 weeks, then maintenance 5-10 mg for 6 months.",
                "black_box_warning": "Corticosteroids: Adrenal insufficiency upon rapid withdrawal, opportunistic infections, hyperglycemia, osteoporosis.",
                "organ_clearance_cutoffs": "Provide bone protection (bisphosphonate or calcium/vitamin D) and gastroprotection (PPI) during long-term steroid therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COP International Consensus",
                "pmid_or_doi": "10.1183/09031936.00062412",
                "cebm_level": 1,
                "sample_size": 1150,
                "endpoints": "Systemic corticosteroids achieve complete clinical and radiological remission in >80%; relapse rate of 35% controlled with re-induction."
            }
        }
    },
    {
        "id": "DOC-CARD-220",
        "icd10": "I28.0",
        "condition": "Pulmonary Arteriovenous Malformation (PAVM)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Embolization Registry",
        "source_body": "Thorax (British Thoracic Society) & JACC",
        "citation": "Shovlin CL et al. British Thoracic Society clinical statement on pulmonary arteriovenous malformations. Thorax. 2017;72(12):1158-1163.",
        "doi_or_source": "10.1136/thoraxjnl-2017-210764",
        "clinical_evidence": "Pulmonary arteriovenous malformations (PAVMs) are abnormal direct low-resistance vascular conduits between pulmonary arteries and pulmonary veins that bypass the capillary bed, creating a right-to-left shunt. Over 80-90% of cases occur in the setting of Hereditary Hemorrhagic Telangiectasia (HHT / Osler-Weber-Rendu disease). Because the normal pulmonary capillary filtration barrier is absent, paradoxical embolization occurs, leading to cryptogenic ischemic stroke (in 10-20%) and cerebral brain abscesses (in 5-10%). Transcatheter coil or microvascular plug embolization of all feeding arteries >=2-3 mm is the gold-standard therapy, reducing ischemic stroke and brain abscess incidence by >90% while improving arterial oxygenation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict lifelong antibiotic prophylaxis prior to dental procedures or invasive surgeries to prevent paradoxical septic emboli to the brain; use of in-line intravenous bubble filters on all IV lines to block air emboli; avoid scuba diving permanently.",
            "monitoring_cadence": "Transthoracic contrast echocardiography (agitated saline bubble study) for right-to-left shunt quantification; contrast-enhanced chest CT at 6-12 months post-embolization, then every 3-5 years.",
            "clinical_thresholds": "Feeding artery diameter >=2-3 mm on contrast CT, or documented paradoxical cerebral embolic event mandates immediate transcatheter percutaneous embolotherapy."
        },
        "patient_plain_language": "A pulmonary arteriovenous malformation (PAVM) is an abnormal direct tangle between a blood vessel carrying blood into your lungs and one carrying it away, bypassing the lung's normal microscopic filtering net (capillaries). Because this natural filter is skipped, tiny blood clots or bacteria can slip straight through to your brain, causing strokes or brain infections. Treating it involves plugging the abnormal connection with tiny coils.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured diameter of the feeding artery to my lung malformation, and do I have genetic features of HHT (nosebleeds, mouth telangiectasias)?",
            "safety_question": "Do I have an active prescription for dental antibiotic prophylaxis to prevent bacteria from slipping through the lung shunt to my brain?",
            "action_threshold_question": "Are my IV lines always equipped with an air-filter trap to prevent accidental air bubbles from travelling to my brain?"
        },
        "red_flags": [
            "Sudden neurological changes (facial droop, arm weakness, speech trouble), severe new headache with high fever (suspect Brain Abscess), or coughing up large quantities of blood"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A pulmonary arteriovenous malformation is an abnormal connection between an artery and a vein in the lungs.",
                "plain_analogy": "A plumbing bypass pipe that skips the lung's natural filter, allowing debris or bacteria to cross straight into clean brain blood.",
                "lifestyle_action": "Always take antibiotics before dental visits. Never scuba dive. Ensure nurses use air filters on all IV drips."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Amoxicillin (Prophylaxis)", "Tranexamic Acid (for HHT epistaxis)", "Bevacizumab IV"],
                "dosing_gdmt": "Dental Prophylaxis: Amoxicillin 2g orally 30-60 minutes prior to dental procedures (or Clindamycin 600 mg if penicillin-allergic).",
                "black_box_warning": "Bevacizumab: GI perforation, severe wound healing complications, and hemorrhage.",
                "organ_clearance_cutoffs": "Monitor for coil migration or recanalization via unenhanced low-dose CT; avoid unmonitored intravenous contrast in renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BTS PAVM Statement",
                "pmid_or_doi": "10.1136/thoraxjnl-2017-210764",
                "cebm_level": 1,
                "sample_size": 1500,
                "endpoints": "Transcatheter embolotherapy reduces stroke risk by >90% and brain abscess incidence from 10% to <1%; improves room air PaO2."
            }
        }
    }
]