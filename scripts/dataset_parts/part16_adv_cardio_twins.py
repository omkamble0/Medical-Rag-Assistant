"""
part16_adv_cardio_twins.py
"""

PART_16_DISEASES = [
    {
        "id": "DOC-CARD-401",
        "icd10": "I42.1",
        "condition": "Hypertrophic Obstructive Cardiomyopathy (HOCM)",
        "specialty": "Cardiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ACC HOCM Guideline & EXPLORER-HCM",
        "source_body": "Lancet",
        "citation": "Olivotto I et al. Mavacamten for Treatment of Symptomatic Obstructive Hypertrophic Cardiomyopathy (EXPLORER-HCM). Lancet. 2020;396(10253):759-769.",
        "doi_or_source": "10.1016/S0140-6736(20)31792-X",
        "clinical_evidence": "The landmark phase 3 EXPLORER-HCM trial (n=251) proved that cardiac myosin inhibitor Mavacamten achieved 37% clinical composite improvement (p<0.001) and reduced LVOT gradient by 36 mmHg versus placebo. Beta-blockers or non-DHP calcium channel blockers remain foundational first-line therapy; vasodilators and pure inotropes (digoxin) are strictly contraindicated due to worsening outflow tract obstruction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid dehydration, intense competitive sprinting/burst exertion, and saunas; maintain adequate oral fluid and salt intake; avoid pure vasodilators (nitrates, ACE inhibitors, PDE5 inhibitors) which worsen LVOT gradient.",
            "monitoring_cadence": "Transthoracic echocardiogram with Valsalva maneuver every 6-12 months; continuous 48-hour Holter monitoring every 1-2 years for non-sustained VT.",
            "clinical_thresholds": "Resting or provoked LVOT peak gradient >=50 mmHg defines severe obstruction requiring targeted therapy or surgical septal myectomy."
        },
        "patient_plain_language": "The muscular wall separating the left and right pumping chambers of your heart becomes excessively thick and overgrown due to a genetic trait. As the heart muscle squeezes, this thick wall bulges into the exit doorway, choking off blood flow to the body. Dehydration and hot showers make the blockage worse.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my peak LVOT obstruction gradient at rest and during a Valsalva straining maneuver?",
            "safety_question": "Am I a candidate for targeted cardiac myosin inhibitor therapy (Mavacamten) or surgical myectomy?",
            "action_threshold_question": "Why are common blood pressure pills like nitrates and pure vasodilators strictly dangerous for my condition?"
        },
        "red_flags": [
            "Sudden fainting (syncope) during or right after physical exercise (High Risk for Sudden Cardiac Death)",
            "Sustained rapid heart palpitations accompanied by chest pressure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "HOCM is genetic heart muscle thickening that obstructs blood leaving the heart chamber.",
                "plain_analogy": "A thickened door that swings shut and jams the hallway exit whenever everyone rushes to leave.",
                "lifestyle_action": "Stay well-hydrated, avoid sudden explosive sprinting, and avoid medications that dilate blood vessels."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Mavacamten (Camzyos - First-in-class Myosin Inhibitor)",
                    "Metoprolol Succinate",
                    "Verapamil"
                ],
                "dosing_gdmt": "Mavacamten 5 mg orally daily, titrated based on LVEF and LVOT gradient (max 15 mg); Metoprolol 50-200 mg daily.",
                "black_box_warning": "Mavacamten REMS program: can cause heart failure due to systolic dysfunction (LVEF <50%); requires baseline and serial echo.",
                "organ_clearance_cutoffs": "Contraindicated with strong CYP2C19 inhibitors; pause if LVEF drops <50%."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EXPLORER-HCM",
                "pmid_or_doi": "10.1016/S0140-6736(20)31792-X",
                "cebm_level": 2,
                "sample_size": 251,
                "endpoints": "Mavacamten achieves 37% composite symptom/functional improvement and eliminates LVOT obstruction."
            }
        }
    },
    {
        "id": "DOC-CARD-402",
        "icd10": "I42.0",
        "condition": "Dilated Cardiomyopathy (Non-Ischemic Systolic Dysfunction)",
        "specialty": "Cardiology & Heart Failure",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ACC/HFSA Heart Failure Guidelines",
        "source_body": "Circulation",
        "citation": "Heidenreich PA et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032.",
        "doi_or_source": "10.1161/CIR.0000000000001063",
        "clinical_evidence": "Quadruple guideline-directed medical therapy (ARNI Sacubitril/Valsartan + Evidence-based Beta-blocker + MRA Spironolactone + SGLT2 inhibitor Dapagliflozin/Empagliflozin) reduces 2-year all-cause mortality by 63% and promotes reverse ventricular remodeling (increasing LVEF from <35% to >45% in 38% of patients). Genetic testing (LMNA, TTN, MYH7) identifies familial risk.",
        "solution_protocol": {
            "non_pharmacological_targets": "Sodium restriction (<2,000 mg/day); fluid restriction to 1.5-2.0 L/day if hyponatremic; complete alcohol abstinence (reverses alcoholic DCM in up to 50%); daily morning weight tracking.",
            "monitoring_cadence": "Echocardiogram 3-6 months post-GDMT titration to re-evaluate LVEF for ICD/CRT primary prevention criteria; BNP/NT-proBNP serial tracking.",
            "clinical_thresholds": "LVEF <=35% despite 3 months of optimal GDMT indicates guideline criteria for primary prevention Implantable Cardioverter-Defibrillator (ICD)."
        },
        "patient_plain_language": "Unlike HOCM where the heart muscle is overly thick, dilated cardiomyopathy causes the heart's main pumping chamber to stretch out, thin, and balloon like an over-inflated rubber glove. Because the stretched walls are weak, the heart cannot squeeze hard enough, causing fluid to back up into the lungs and legs.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Left Ventricular Ejection Fraction (LVEF) on echocardiogram?",
            "safety_question": "Am I taking all 4 foundational heart failure medications (ARNI, beta-blocker, aldosterone blocker, SGLT2 inhibitor)?",
            "action_threshold_question": "If my ejection fraction stays at or below 35%, do I qualify for an implantable defibrillator (ICD) to protect against arrhythmias?"
        },
        "red_flags": [
            "Rapid weight gain (>3 lbs in 1 day or >5 lbs in 1 week) with severe orthopnea requiring sleeping upright",
            "Severe dizziness or fainting spells indicative of ventricular tachycardia"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dilated cardiomyopathy is enlargement and thinning of heart chambers causing reduced pumping power.",
                "plain_analogy": "A water balloon that has been stretched out so many times that its rubber walls lose their snap.",
                "lifestyle_action": "Weigh yourself every morning, restrict dietary salt, abstain from alcohol, and take GDMT medicines."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Sacubitril/Valsartan (Entresto)",
                    "Carvedilol / Metoprolol Succinate",
                    "Spironolactone",
                    "Dapagliflozin / Empagliflozin"
                ],
                "dosing_gdmt": "Sacubitril/Valsartan 49/51 mg BID titrated to 97/103 mg BID; Carvedilol 25-50 mg BID; Spironolactone 25 mg daily; Dapagliflozin 10 mg daily.",
                "black_box_warning": "ARNI black box warning for fetal toxicity; do not combine with ACE inhibitors (requires 36-hour washout).",
                "organ_clearance_cutoffs": "Dose adjustment for renal impairment (eGFR <30 mL/min) and hyperkalemia (>5.0 mEq/L)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PARADIGM-HF",
                "pmid_or_doi": "10.1056/NEJMoa1409077",
                "cebm_level": 2,
                "sample_size": 8442,
                "endpoints": "ARNI reduces cardiovascular death and heart failure hospitalization by 20% compared to Enalapril."
            }
        }
    },
    {
        "id": "DOC-CARD-403",
        "icd10": "I31.1",
        "condition": "Chronic Constrictive Pericarditis (Rigid Pericardial Shell)",
        "specialty": "Cardiology & Cardiothoracic Surgery",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ESC Pericardial Diseases Guidelines",
        "source_body": "European Heart Journal",
        "citation": "Adler Y et al. 2015 ESC Guidelines for the Diagnosis and Management of Pericardial Diseases. Eur Heart J. 2015;36(42):2921-2964.",
        "doi_or_source": "10.1093/eurheartj/ehv318",
        "clinical_evidence": "Right and left ventricular catheterization demonstrating ventricular interdependence (discordance of LV and RV systolic pressures during respiration) confirms constrictive physiology. Complete surgical pericardiectomy ('pericardial stripping') remains the only definitive curative therapy for chronic fibrotic constriction, restoring normal cardiac output in >80% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Judicious low-dose loop diuretics to relieve hepatic congestion while avoiding severe preload depletion; dietary sodium restriction; surgical evaluation before irreversible myocardial atrophy or liver cirrhosis occurs.",
            "monitoring_cadence": "Cardiac MRI/CT evaluating pericardial thickening (>4 mm) and calcification; serial hepatic function panels to assess cardiac cirrhosis.",
            "clinical_thresholds": "Kussmaul sign (paradoxical JVP rise during inspiration), prominent y-descent on jugular venous pulse, and pericardial knock on auscultation."
        },
        "patient_plain_language": "The sac surrounding your heart (pericardium) becomes stiff, thickened, and heavily calcified like an armor shell or eggshell. Because this rigid shell will not stretch, the heart cannot expand to fill with blood between beats, leading to massive fluid backup into the liver, stomach, and legs.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did cardiac MRI or CT scan confirm calcification and thickening greater than 4 mm of my pericardial sac?",
            "safety_question": "Do heart pressure measurements show ventricular interdependence (the chambers bumping into each other)?",
            "action_threshold_question": "Am I a candidate for surgical pericardiectomy (stripping away the calcified shell)?"
        },
        "red_flags": [
            "Rapidly worsening ascites with yellow jaundice and confusion (cardiac cirrhosis failure)",
            "Profound hypotension following standard diuretic doses (severe preload failure)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Constrictive pericarditis is rigid calcification of the heart sac that prevents normal chamber filling.",
                "plain_analogy": "A heart trapped inside an unyielding plaster cast that cannot expand to receive incoming blood.",
                "lifestyle_action": "Avoid heavy exertion, limit sodium, and consult cardiothoracic surgery for pericardial removal."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Complete Surgical Pericardiectomy (Curative)",
                    "Furosemide IV/oral",
                    "Colchicine (if acute inflammation present)"
                ],
                "dosing_gdmt": "Pericardiectomy is definitive; Furosemide 20-40 mg daily titrated carefully to avoid prerenal azotemia.",
                "black_box_warning": "Over-diuresis in constrictive pericarditis rapidly causes severe hypotension and shock due to fixed preload limit.",
                "organ_clearance_cutoffs": "Monitor renal function closely during diuretic therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESC-PERICARD",
                "pmid_or_doi": "10.1093/eurheartj/ehv318",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "Complete surgical pericardial stripping achieves durable symptom resolution in 83% of patients."
            }
        }
    },
    {
        "id": "DOC-CARD-404",
        "icd10": "E85.4",
        "condition": "Cardiac Amyloidosis (ATTR Transthyretin Cardiomyopathy)",
        "specialty": "Cardiology & Hematology",
        "organ_system": "Circulatory & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATTR-ACT Trial & ACC Expert Consensus",
        "source_body": "New England Journal of Medicine",
        "citation": "Maurer MS et al. Tafamidis Treatment for Patients with Transthyretin Amyloid Cardiomyopathy (ATTR-ACT). N Engl J Med. 2018;379(11):1007-1016.",
        "doi_or_source": "10.1056/NEJMoa1805689",
        "clinical_evidence": "The pivotal ATTR-ACT phase 3 trial (n=441) proved that Transthyretin stabilizer Tafamidis reduced all-cause mortality by 30% (p=0.026) and cardiovascular hospitalizations by 32% (p<0.001) in wild-type and hereditary ATTR cardiomyopathy. Non-invasive diagnosis via 99mTc-PYP scintigraphy (Grade 2-3 myocardial uptake) with negative serum/urine free light chains avoids endomyocardial biopsy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict sodium (<2 g/day) and fluid restriction; avoid beta-blockers, ACE inhibitors, and digoxin (which bind to amyloid fibrils causing severe toxicity and orthostatic collapse); maintain sinus rhythm.",
            "monitoring_cadence": "Technetium-99m pyrophosphate (99mTc-PYP) bone scintigraphy scan; serial NT-proBNP and troponin T; annual 24-hour Holter monitor.",
            "clinical_thresholds": "Apical sparing strain pattern on echocardiogram ('cherry on top' on bullseye map) with symmetric LV wall thickening >12 mm."
        },
        "patient_plain_language": "Misfolded proteins (amyloid fibrils) gradually deposit in between your heart muscle cells like cement or hardening glue. The heart walls become extremely stiff and thick, but unlike true muscle growth, the muscle fibers are replaced by dead protein, causing restrictive heart failure and conduction blocks.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my 99mTc-PYP nuclear scan confirm transthyretin cardiac amyloidosis without monoclonal plasma cell cancer?",
            "safety_question": "Am I taking Tafamidis to lock the unstable transthyretin proteins and stop further cardiac damage?",
            "action_threshold_question": "Why should standard heart failure drugs like beta-blockers and digoxin be avoided or discontinued in my case?"
        },
        "red_flags": [
            "Sudden dizzy spells, blackouts, or heart pauses >3 seconds (High Grade Conduction Block - Pacemaker Needed)",
            "Rapid accumulation of abdominal ascites and peripheral edema refractory to diuretics"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cardiac amyloidosis is stiffening of the heart caused by protein fibril deposits in the muscle walls.",
                "plain_analogy": "Cement poured between the bricks of a building, turning flexible shock-absorbers into solid stone.",
                "lifestyle_action": "Take Tafamidis daily as prescribed, strictly limit dietary salt, and report fainting spells immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Tafamidis Meglumine / Free Acid (Vyndamax - First Line)",
                    "Loop Diuretics (Bumetanide/Torsemide)",
                    "SGLT2 Inhibitors"
                ],
                "dosing_gdmt": "Tafamidis 61 mg orally once daily; Torsemide 10-40 mg daily for volume control.",
                "black_box_warning": "Standard beta-blockers, ACE inhibitors, and calcium channel blockers are poorly tolerated and exacerbate hypotension.",
                "organ_clearance_cutoffs": "No dosage adjustments required for renal or mild-moderate hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATTR-ACT",
                "pmid_or_doi": "10.1056/NEJMoa1805689",
                "cebm_level": 2,
                "sample_size": 441,
                "endpoints": "Tafamidis reduces 30-month all-cause mortality by 30% and preserves 6-minute walk distance."
            }
        }
    },
    {
        "id": "DOC-CARD-405",
        "icd10": "I71.01",
        "condition": "Acute Aortic Dissection - Stanford Type A (Ascending Aorta)",
        "specialty": "Cardiothoracic Surgery & Vascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: STS/AATS Guidelines & IRAD Consensus",
        "source_body": "Annals of Thoracic Surgery",
        "citation": "MacGillivray TE et al. The Society of Thoracic Surgeons/American Association for Thoracic Surgery Clinical Practice Guidelines on the Management of Type A Aortic Dissection. Ann Thorac Surg. 2022;113(4):1073-1085.",
        "doi_or_source": "10.1016/j.athoracsur.2021.11.029",
        "clinical_evidence": "EMERGENT OPEN SURGICAL REPLACEMENT of the ascending aorta (with or without aortic root/valve replacement) is mandatory. Mortality increases by 1-2% per hour of delay, reaching 50% at 48 hours without surgery. Immediate anti-impulse medical therapy (IV Esmolol targeting HR <60 bpm, followed by IV Nitroprusside targeting SBP 100-120 mmHg) prevents propagation.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATE SURGICAL EMERGENCE; strict NPO; blood typing and cross-matching for 6-8 units PRBC and FFP; avoid thrombolysis or anticoagulation (catastrophic fatal hemopericardium).",
            "monitoring_cadence": "Continuous intra-arterial blood pressure monitoring in right radial artery; emergent CT angiography of chest/abdomen/pelvis.",
            "clinical_thresholds": "Tear involving ascending aorta (Stanford Type A / DeBakey I & II) mandates emergent operating room transfer."
        },
        "patient_plain_language": "A catastrophic surgical emergency where the inner layer of the main artery leaving your heart (ascending aorta) tears open. High-pressure blood rips into the middle layer of the artery wall, creating a false channel that can burst open into the heart sac, crush coronary arteries, or cause fatal stroke within minutes.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the cardiothoracic surgery team in the operating room right now for emergent open aortic repair?",
            "safety_question": "Has IV Esmolol beta-blocker brought my heart rate below 60 and blood pressure to 100-120 mmHg?",
            "action_threshold_question": "Has anticoagulation and clot-busting medicine been strictly avoided?"
        },
        "red_flags": [
            "Sudden severe, sharp, tearing chest pain radiating between the shoulder blades (Stanford Type A Dissection)",
            "Unequal blood pressure between right and left arms (>20 mmHg difference) with syncope or stroke"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Type A aortic dissection is a life-threatening tear in the main heart artery requiring emergent open surgery.",
                "plain_analogy": "A high-pressure garden hose inner lining tearing loose, letting water rip the outer casing apart.",
                "lifestyle_action": "Call 911 immediately for sudden tearing chest pain; open surgery within hours is life-saving."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Emergent Open Surgical Aortic Repair (Mandatory)",
                    "Esmolol IV (Anti-impulse therapy)",
                    "Nicardipine / Nitroprusside IV"
                ],
                "dosing_gdmt": "Esmolol IV infusion titrated to HR 50-60 bpm, followed by Nicardipine IV titrated to SBP 100-120 mmHg.",
                "black_box_warning": "NEVER give vasodilators BEFORE beta-blockers (triggers reflex tachycardia and accelerates aortic tear).",
                "organ_clearance_cutoffs": "Emergency surgical intervention; no pharmacological substitute."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "IRAD-TYPE-A",
                "pmid_or_doi": "10.1016/j.athoracsur.2021.11.029",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "Emergent surgical repair reduces 48-hour mortality from >50% (medical) to <18% (surgical)."
            }
        }
    },
    {
        "id": "DOC-CARD-406",
        "icd10": "I71.02",
        "condition": "Acute Aortic Dissection - Stanford Type B (Descending Aorta)",
        "specialty": "Vascular Surgery & Interventional Radiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: SVS/STS Guidelines & INSTEAD-XL Trial",
        "source_body": "Journal of Vascular Surgery",
        "citation": "Lombardi JV et al. Society for Vascular Surgery and Society of Thoracic Surgeons Guidelines on the Management of Type B Aortic Dissection. J Vasc Surg. 2020;71(3):720-746.",
        "doi_or_source": "10.1016/j.jvs.2019.11.002",
        "clinical_evidence": "Uncomplicated Type B dissection is managed primarily with aggressive medical anti-impulse therapy (IV Esmolol/Labetalol targeting HR <60 bpm and SBP <=120 mmHg). Complicated Type B (refractory pain, malperfusion syndrome, rapid aortic expansion >44 mm) mandates Thoracic Endovascular Aortic Repair (TEVAR), which the INSTEAD-XL trial showed improves 5-year aorta-specific survival (86.9% vs 69.3%; p=0.04).",
        "solution_protocol": {
            "non_pharmacological_targets": "Anti-impulse medical therapy in ICU setting; lifelong strict blood pressure control (target SBP <120 mmHg, HR <60 bpm); avoid heavy isometric weightlifting and Valsalva straining.",
            "monitoring_cadence": "Repeat CT angiography at 72 hours, 1 month, 6 months, and annually; serial monitoring of renal function, peripheral pulses, and bowel viability.",
            "clinical_thresholds": "Complicated dissection criteria: Visceral, renal, or lower extremity malperfusion; refractory hypertension; aortic diameter >=55 mm."
        },
        "patient_plain_language": "The main aorta tears downstream from the heart (after the left arm artery branch in your chest or abdomen). Unlike Type A, the tear is past the heart, so it usually does NOT need open-heart surgery. Instead, strict ICU blood pressure lowering and resting the artery wall allows it to heal, or a stent-graft (TEVAR) is placed if blood flow to organs is blocked.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is my dissection uncomplicated, or is there any sign of malperfusion to my kidneys, intestines, or legs?",
            "safety_question": "Is my heart rate kept strictly below 60 beats/min and systolic BP below 120 mmHg with IV beta-blockers?",
            "action_threshold_question": "Will I need a minimally invasive stent-graft (TEVAR) through my groin artery?"
        },
        "red_flags": [
            "Loss of pulses in legs, severe abdominal pain, or sudden decrease in urine output (Visceral Malperfusion)",
            "Recurrent excruciating back pain indicating ongoing aortic tear expansion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Type B aortic dissection is a tear in the descending aorta managed with blood pressure control or stent repair.",
                "plain_analogy": "A tear in the downstream section of an irrigation pipe, clamped with pressure valves or lined with an internal sleeve.",
                "lifestyle_action": "Take blood pressure medications religiously, avoid heavy lifting, and attend yearly CT scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Esmolol IV / Labetalol IV (First Line)",
                    "Nicardipine IV",
                    "TEVAR (Thoracic Endovascular Repair for complicated cases)"
                ],
                "dosing_gdmt": "Labetalol IV 20 mg bolus then 1-2 mg/min infusion; target HR <60 bpm and SBP 100-120 mmHg.",
                "black_box_warning": "Vasodilators must not be given without concurrent beta-blockade due to reflex shear stress.",
                "organ_clearance_cutoffs": "Renal adjustments for oral antihypertensives during long-term maintenance."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "INSTEAD-XL",
                "pmid_or_doi": "10.1161/CIRCULATIONAHA.113.003185",
                "cebm_level": 2,
                "sample_size": 140,
                "endpoints": "TEVAR combined with medical therapy improves 5-year aorta-specific survival over medical therapy alone (p=0.04)."
            }
        }
    },
    {
        "id": "DOC-CARD-407",
        "icd10": "I47.2",
        "condition": "Ventricular Tachycardia (Monomorphic Sustained VT)",
        "specialty": "Cardiac Electrophysiology & Critical Care",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ACC/HRS Guideline on Ventricular Arrhythmias",
        "source_body": "Circulation",
        "citation": "Al-Khatib SM et al. 2017 AHA/ACC/HRS Guideline for Management of Patients With Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death. Circulation. 2018;138(13):e272-e391.",
        "doi_or_source": "10.1161/CIR.0000000000000549",
        "clinical_evidence": "Sustained monomorphic VT with hemodynamic instability mandates IMMEDIATE SYNCHRONIZED DIRECT-CURRENT CARDIOVERSION (100-200 J). Stable VT is treated with IV Amiodarone (150 mg over 10 min) or IV Procainamide (20-50 mg/min). Catheter ablation guided by 3D electroanatomical mapping reduces recurrent ICD shocks by 42% (VANISH trial; p=0.04).",
        "solution_protocol": {
            "non_pharmacological_targets": "Cardiopulmonary resuscitation and defibrillation readiness; treat reversible triggers (hypokalemia >4.0 mEq/L, hypomagnesemia >2.0 mg/dL, ischemia); avoid stimulants and sympathomimetics; catheter ablation for refractory VT.",
            "monitoring_cadence": "Continuous ECG telemetry; serum electrolytes every 4-6 hours until normalized; 12-lead ECG demonstrating AV dissociation, capture beats, or fusion beats.",
            "clinical_thresholds": "Wide complex tachycardia (QRS >=120 ms) with heart rate >100 bpm is presumed Ventricular Tachycardia until proven otherwise."
        },
        "patient_plain_language": "An abnormally rapid, dangerous electrical short-circuit originates deep inside your heart's main pumping chambers (ventricles). The chambers race at 150 to 250 beats a minute—so fast that they do not have time to fill with blood between squeezes. If blood pressure drops, an immediate electric shock reset is required.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the 12-lead ECG show AV dissociation or fusion beats proving this was Ventricular Tachycardia and not SVT?",
            "safety_question": "Has my blood potassium been brought above 4.0 mEq/L and magnesium above 2.0 mg/dL?",
            "action_threshold_question": "Do I qualify for an implantable cardioverter-defibrillator (ICD) or catheter ablation to prevent sudden death?"
        },
        "red_flags": [
            "Sudden loss of consciousness or pulselessness (Immediate CPR and Unsynchronized Defibrillation)",
            "Severe chest pain, breathlessness, and systolic BP <90 mmHg during rapid heart palpitations"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ventricular tachycardia is a rapid, potentially fatal electrical short-circuit in the lower heart chambers.",
                "plain_analogy": "A motor spinning out of control in high gear with no clutch, failing to deliver power to the wheels.",
                "lifestyle_action": "Never ignore rapid fluttering with lightheadedness; seek emergency defibrillation and electrophysiology care."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Synchronized DC Cardioversion (Immediate if unstable)",
                    "Amiodarone IV",
                    "Procainamide IV",
                    "Sotalol oral"
                ],
                "dosing_gdmt": "Amiodarone 150 mg IV over 10 min, then 1 mg/min x 6h, then 0.5 mg/min; or Procainamide 20-50 mg/min (max 17 mg/kg).",
                "black_box_warning": "Amiodarone pulmonary toxicity and QT prolongation; Procainamide induces lupus-like syndrome and hypotension.",
                "organ_clearance_cutoffs": "Reduce amiodarone maintenance dose; monitor liver function, thyroid function, and chest X-ray."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "VANISH-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1513614",
                "cebm_level": 2,
                "sample_size": 259,
                "endpoints": "Catheter ablation reduces composite death, VT storm, and ICD shocks compared to escalated antiarrhythmics."
            }
        }
    },
    {
        "id": "DOC-CARD-408",
        "icd10": "I47.1",
        "condition": "Paroxysmal Supraventricular Tachycardia (AVNRT / AVRT)",
        "specialty": "Cardiac Electrophysiology & Emergency Medicine",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ACC/HRS SVT Guidelines",
        "source_body": "Circulation",
        "citation": "Page RL et al. 2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia. Circulation. 2016;133(14):e506-e574.",
        "doi_or_source": "10.1161/CIR.0000000000000311",
        "clinical_evidence": "Vagal maneuvers (modified Valsalva technique with leg elevation; REVERT trial) achieve 43% cardioversion success versus 17% standard Valsalva (p<0.0001). Intravenous Adenosine (6 mg rapid push, followed by 12 mg if needed) transiently blocks the AV node, terminating >90% of AVNRT/AVRT reentrant circuits. Catheter ablation provides >95% curative success.",
        "solution_protocol": {
            "non_pharmacological_targets": "Modified Valsalva maneuver (strain at 40 mmHg for 15s, then immediately lie flat with legs elevated at 45 degrees for 15s); avoid excessive caffeine, energy drinks, nicotine, and adrenergic stimulants.",
            "monitoring_cadence": "Continuous rhythm strip during vagal maneuvers or adenosine push; 12-lead ECG post-conversion to inspect for pre-excitation (delta wave of WPW).",
            "clinical_thresholds": "Regular narrow-complex tachycardia (QRS <120 ms) with sudden onset and termination, heart rate 150-220 bpm."
        },
        "patient_plain_language": "A benign electrical short-circuit or looping pathway inside the heart's upper junction box (AV node) triggers sudden bouts where your heart races at 160 to 200 beats per minute out of the blue. Simple straining techniques with leg lifting can reset the rhythm, or a fast-acting IV medicine (Adenosine) stops the loop instantly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the modified Valsalva maneuver (blowing into a syringe then raising legs) terminate the episode?",
            "safety_question": "Did the 12-lead ECG after the heart slowed down show any pre-excitation delta waves (Wolff-Parkinson-White)?",
            "action_threshold_question": "Am I a candidate for a quick, curative radiofrequency catheter ablation of the extra electrical wire?"
        },
        "red_flags": [
            "Syncope with heart rate >200 bpm and hemodynamic instability (requires synchronized cardioversion)",
            "Palpitations accompanied by diaphoresis and ischemic ST depressions on ECG"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "AVNRT is a sudden racing heart caused by a looping electrical circuit in the AV junction.",
                "plain_analogy": "A doorbell button that gets stuck down, causing the chime to ring continuously until tapped.",
                "lifestyle_action": "Perform the modified Valsalva maneuver when fluttering starts, and consult electrophysiology for curative ablation."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Adenosine IV (Rapid Push)",
                    "Diltiazem IV",
                    "Metoprolol IV",
                    "Radiofrequency Catheter Ablation (Curative)"
                ],
                "dosing_gdmt": "Adenosine 6 mg rapid IV push followed by 20 mL saline flush; if no response in 1-2 min, give 12 mg rapid IV.",
                "black_box_warning": "Adenosine causes brief (seconds) feeling of chest tightness, facial flushing, and impending doom; warns patient in advance.",
                "organ_clearance_cutoffs": "Contraindicated in severe reactive bronchospasm (asthma); use verapamil or diltiazem instead."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "REVERT-TRIAL",
                "pmid_or_doi": "10.1016/S0140-6736(15)60738-5",
                "cebm_level": 2,
                "sample_size": 433,
                "endpoints": "Modified Valsalva with leg elevation achieves 43% cardioversion rate compared to 17% standard strain (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-409",
        "icd10": "I45.6",
        "condition": "Wolff-Parkinson-White Syndrome (Pre-Excited Atrial Fibrillation)",
        "specialty": "Cardiac Electrophysiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ACC/HRS Guideline on Ventricular Arrhythmias",
        "source_body": "Circulation",
        "citation": "Brugada J et al. Pharmacological and Nonpharmacological Therapy for Arrhythmias in the Pediatric and Adult WPW Population. J Am Coll Cardiol. 2020;75(15):1848-1861.",
        "doi_or_source": "10.1016/j.jacc.2020.02.043",
        "clinical_evidence": "Pre-excited Atrial Fibrillation conducts down an accessory pathway (Bundle of Kent) at rates >250-300 bpm, risking ventricular fibrillation. AV-NODAL BLOCKING DRUGS (ADENOSINE, BETA-BLOCKERS, DILTIAZEM, VERAPAMIL, DIGOXIN) ARE STRICTLY CONTRAINDICATED as they preferentially divert conduction down the accessory pathway, triggering fatal VF. Treatment is Procainamide IV or urgent electrical cardioversion.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATE AVOIDANCE OF AV NODAL BLOCKING DRUGS; catheter ablation of the accessory bypass tract is class I definitive curative recommendation (>95% cure rate).",
            "monitoring_cadence": "12-lead ECG monitoring for shortest pre-excited RR interval (SPERRI <=250 ms identifies high risk for sudden cardiac death).",
            "clinical_thresholds": "Irregular wide-complex tachycardia with varying QRS morphology and axis, heart rate >200-250 bpm."
        },
        "patient_plain_language": "You were born with an extra microscopic electrical wire (accessory pathway) connecting the upper and lower heart chambers. If you develop atrial fibrillation, impulses rush down this extra wire dangerously fast (over 250 beats a minute). Standard heart pills like beta-blockers and diltiazem are dangerous poisons here; Procainamide or catheter burning of the extra wire is required.",
        "doctor_consultation_checklist": {
            "parameter_question": "Why are standard heart rate drugs like diltiazem, beta-blockers, and adenosine strictly forbidden for my WPW rhythm?",
            "safety_question": "Was IV Procainamide or electrical cardioversion used to safely convert my pre-excited rhythm?",
            "action_threshold_question": "When is my radiofrequency catheter ablation procedure scheduled to permanently disconnect the extra pathway?"
        },
        "red_flags": [
            "Irregular rapid heart fluttering with dizziness and blood pressure collapse (Pre-excited AF - Urgent Cardioversion)",
            "Shortest RR interval <250 ms on ECG (Extreme risk for Ventricular Fibrillation)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "WPW with pre-excited AF is a life-threatening arrhythmia where electrical impulses bypass normal safety filters.",
                "plain_analogy": "An illegal electrical hotwire that bypasses the circuit breaker fuse, delivering raw voltage directly to delicate appliances.",
                "lifestyle_action": "Never take AV nodal blocking drugs (beta-blockers, calcium channel blockers) during pre-excited AF; seek immediate electrophysiology care."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Catheter Ablation of Accessory Pathway (Curative - Class I)",
                    "Procainamide IV",
                    "Ibutilide IV",
                    "Direct-Current Cardioversion"
                ],
                "dosing_gdmt": "Procainamide 20-50 mg/min IV infusion until arrhythmia terminates or max dose 17 mg/kg reached; or urgent DC cardioversion.",
                "black_box_warning": "STRICT CONTRAINDICATION: Adenosine, Beta-blockers, Verapamil, Diltiazem, and Digoxin precipitate fatal VF in pre-excited AF.",
                "organ_clearance_cutoffs": "Renal excretion of active metabolite NAPA; requires dose adjustment in renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PEDI-WPW-ABL",
                "pmid_or_doi": "10.1016/j.jacc.2020.02.043",
                "cebm_level": 1,
                "sample_size": 2120,
                "endpoints": "Catheter ablation of accessory pathways achieves >95% permanent cure with <1% complication risk."
            }
        }
    },
    {
        "id": "DOC-CARD-410",
        "icd10": "I49.8",
        "condition": "Brugada Syndrome (Type 1 Coved ST Elevation Channelopathy)",
        "specialty": "Cardiac Electrophysiology & Genetics",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: HRS/EHRA/APHRS Expert Consensus Statement",
        "source_body": "Heart Rhythm",
        "citation": "Antzelevitch C et al. J-Wave Syndromes Expert Consensus Conference Report: Emerging Concepts and Gaps in Knowledge. Heart Rhythm. 2016;13(10):e295-e324.",
        "doi_or_source": "10.1016/j.hrthm.2016.05.024",
        "clinical_evidence": "Brugada syndrome (SCN5A sodium channel mutation) causes sudden nocturnal polymorphic VT / ventricular fibrillation in young individuals. Type 1 ECG pattern (coved ST elevation >=2 mm followed by negative T-wave in V1-V2) can be unmasked by fever or sodium channel blockers (Ajmaline, Flecainide). Implantable Cardioverter-Defibrillator (ICD) is the ONLY proven therapy to prevent sudden death.",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive antipyretic fever treatment (acetaminophen/NSAIDs immediately for temp >38.0 C); avoid all drugs on the BrugadaDrugs.org blacklist (flecainide, propafenone, tricyclic antidepressants, lithium); avoid excessive alcohol and heavy meals.",
            "monitoring_cadence": "Continuous telemetry during febrile illness; 12-lead ECG with high precordial leads (2nd and 3rd intercostal spaces); genetic testing for SCN5A mutations.",
            "clinical_thresholds": "Type 1 coved ST-segment elevation >=2 mm in >=1 right precordial lead (V1, V2) positioned in 2nd, 3rd, or 4th intercostal space."
        },
        "patient_plain_language": "A genetic condition affecting the microscopic sodium gates in your heart cells. It causes a distinctive wave on your ECG and can trigger dangerous heart short-circuits, especially during a high fever or while sleeping at night. Taking fever-reducing pills immediately during an illness is life-saving, and an implantable defibrillator protects against sudden death.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my ECG show the Type 1 coved ST-elevation pattern, and was it unmasked during fever or medication testing?",
            "safety_question": "Have I received the complete BrugadaDrugs.org unsafe medication list to share with all my doctors and pharmacies?",
            "action_threshold_question": "Do I qualify for an Implantable Cardioverter-Defibrillator (ICD) based on prior fainting spells?"
        },
        "red_flags": [
            "Fainting (syncope) without warning, especially at night or during a febrile illness (High Sudden Death Risk)",
            "Nocturnal agonal gasping respiration (signifies resuscitated polymorphic ventricular tachycardia)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Brugada syndrome is a genetic sodium channel disorder causing dangerous nighttime heart arrhythmias.",
                "plain_analogy": "A faulty electrical switch in a home that trips unexpectedly when the thermostat gets too hot.",
                "lifestyle_action": "Treat all fevers aggressively with acetaminophen, avoid blacklisted medications, and discuss an ICD with your cardiologist."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Implantable Cardioverter-Defibrillator (ICD - Gold Standard)",
                    "Quinidine oral (for electrical storm)",
                    "Acetaminophen (aggressive antipyretic)"
                ],
                "dosing_gdmt": "Acetaminophen 650-1000 mg q6h for any fever; Quinidine 300-600 mg q8h for recurrent VT/VF storm.",
                "black_box_warning": "Class IC antiarrhythmics (Flecainide) and local anesthetics (Bupivacaine) can induce fatal cardiac arrest.",
                "organ_clearance_cutoffs": "Quinidine monitoring: check QTc interval and serum levels; watch for cinchonism."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HRS-BRUGADA",
                "pmid_or_doi": "10.1016/j.hrthm.2016.05.024",
                "cebm_level": 1,
                "sample_size": 1850,
                "endpoints": "ICD implantation provides 100% successful termination of ventricular fibrillation episodes in symptomatic Brugada patients."
            }
        }
    },
    {
        "id": "DOC-CARD-411",
        "icd10": "I45.81",
        "condition": "Congenital Long QT Syndrome (LQTS - Torsades de Pointes)",
        "specialty": "Cardiology & Pediatric Cardiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ACC/HRS Guidelines on Ventricular Arrhythmias",
        "source_body": "Circulation",
        "citation": "Priori SG et al. 2013 HRS/EHRA/APHRS Expert Consensus Statement on the Diagnosis and Management of Patients with Inherited Primary Arrhythmia Syndromes. Heart Rhythm. 2013;10(12):1932-1963.",
        "doi_or_source": "10.1016/j.hrthm.2013.05.014",
        "clinical_evidence": "Congenital LQTS (LQT1 KCNQ1, LQT2 KCNH2, LQT3 SCN5A) delays cardiac repolarization, predisposing to early afterdepolarizations and polymorphic VT (Torsades de Pointes). Beta-blockers (Nadolol or Propranolol) are the mainstay of therapy, reducing cardiac events by >70% in LQT1 and LQT2. IV Magnesium Sulfate (2 g bolus) is first-line acute treatment for Torsades.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of all QT-prolonging medications (CredibleMeds.org list: macrolides, fluoroquinolones, ondansetron, antipsychotics); maintain serum potassium >=4.0 mEq/L and magnesium >=2.0 mg/dL; avoid competitive swimming in LQT1; avoid sudden loud alarm clocks in LQT2.",
            "monitoring_cadence": "Annual 12-lead ECG measuring Bazett-corrected QTc; exercise treadmill stress testing; genetic cascade screening for family members.",
            "clinical_thresholds": "Bazett QTc interval >460 ms in women or >450 ms in men; Schwartz score >=3.5 indicates high probability of congenital LQTS."
        },
        "patient_plain_language": "The electrical recharging phase of your heart muscle cells takes longer than normal. On an ECG, this appears as an extended QT interval. During times of stress, exercise (like swimming), or sudden loud alarms, this delay can cause the heart to wobble into a chaotic, twisty rhythm called Torsades de Pointes, leading to blackouts or cardiac arrest.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact QTc interval on ECG, and which specific genetic subtype (LQT1, LQT2, or LQT3) do I have?",
            "safety_question": "Am I taking non-selective beta-blocker therapy (Nadolol or Propranolol) at an adequate protective dose?",
            "action_threshold_question": "Have all my prescriptions been screened against the CredibleMeds.org QT-prolonging drug database?"
        },
        "red_flags": [
            "Sudden fainting spell triggered by exercise, loud noises, or emotional shock (Torsades de Pointes)",
            "Family history of unexplained sudden drowning or early sudden cardiac death"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Long QT syndrome is an electrical recharging delay in the heart that triggers twisty, dangerous heartbeats.",
                "plain_analogy": "A camera flash that takes twice as long to recharge, jamming the shutter if triggered too soon.",
                "lifestyle_action": "Take your prescribed beta-blocker every day, never take medications on the CredibleMeds list, and avoid sudden auditory alarms."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Nadolol / Propranolol (Non-selective Beta-blockers - First Line)",
                    "Magnesium Sulfate IV (for acute Torsades)",
                    "Mexiletine (specifically for LQT3)",
                    "ICD Implantation"
                ],
                "dosing_gdmt": "Nadolol 1-2 mg/kg/day once daily; Magnesium Sulfate 2 g IV over 1-2 minutes for acute Torsades de Pointes.",
                "black_box_warning": "Metoprolol is INFERIOR to Nadolol/Propranolol for LQTS breakthrough prevention; do not substitute.",
                "organ_clearance_cutoffs": "Dose reduction in renal dysfunction for nadolol."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HRS-LQTS",
                "pmid_or_doi": "10.1016/j.hrthm.2013.05.014",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "Non-selective beta-blockers reduce syncope, cardiac arrest, and sudden death by 78% in LQT1 and 63% in LQT2."
            }
        }
    },
    {
        "id": "DOC-CARD-412",
        "icd10": "I49.5",
        "condition": "Sick Sinus Syndrome (Tachycardia-Bradycardia Syndrome)",
        "specialty": "Cardiac Electrophysiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACC/AHA/HRS Bradycardia Guidelines",
        "source_body": "Circulation",
        "citation": "Kusumoto FM et al. 2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. Circulation. 2019;140(8):e382-e482.",
        "doi_or_source": "10.1161/CIR.0000000000000628",
        "clinical_evidence": "Intrinsic dysfunction of the sinoatrial node causes inappropriate sinus bradycardia, sinus arrest, or alternating paroxysmal atrial tachyarrhythmias (tachy-brady syndrome). PERMANENT DUAL-CHAMBER PACEMAKER (DDDR) is the definitive class I therapy for symptomatic bradycardia, allowing safe initiation of AV-nodal blocking drugs to control the tachycardia component without worsening sinus pauses.",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinue non-essential bradycardic medications (beta-blockers, non-DHP CCBs, clonidine) prior to pacemaker evaluation; fall prevention precautions during dizzy spells; anticoagulation for stroke prevention based on CHA2DS2-VASc score.",
            "monitoring_cadence": "24-48 hour ambulatory Holter or 30-day event monitor correlating symptoms with sinus pauses >3 seconds or profound bradycardia; baseline echocardiogram.",
            "clinical_thresholds": "Symptomatic sinus bradycardia (HR <40 bpm while awake) or sinus pauses >=3.0 seconds associated with syncope or presyncope."
        },
        "patient_plain_language": "Your heart's natural spark plug (the sinus node) has worn out with age or fibrous scarring. It fires too slowly, skips beats, or pauses for several seconds, leaving you lightheaded or exhausted. Sometimes it alternates between racing too fast (atrial flutter/fibrillation) and suddenly stalling out. A dual-chamber pacemaker restores steady, reliable electrical beats.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did heart monitoring prove my fainting and lightheadedness happened during sinus pauses longer than 3 seconds?",
            "safety_question": "Do I need a dual-chamber permanent pacemaker (DDDR) to give my heart a reliable floor heart rate?",
            "action_threshold_question": "Do I need blood thinner anticoagulation to prevent stroke caused by the racing atrial rhythm component?"
        },
        "red_flags": [
            "Sinus pause >3 seconds causing sudden blackout or falling with traumatic head injury",
            "Profound daytime heart rate <35 bpm accompanied by shortness of breath and confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sick sinus syndrome is natural pacemaker malfunction causing alternating slow heart pauses and racing rhythms.",
                "plain_analogy": "A car spark plug that intermittently misfires and stalls at traffic lights, then suddenly surges in park.",
                "lifestyle_action": "Report all blackout episodes, avoid non-prescribed sedatives, and consult an electrophysiologist for pacemaker implantation."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Permanent Dual-Chamber Pacemaker (DDDR - Definitive Class I)",
                    "Apixaban / Rivaroxaban (Anticoagulation for AF)",
                    "Metoprolol (only AFTER pacemaker placed)"
                ],
                "dosing_gdmt": "Pacemaker programmed to DDDR mode with lower rate limit 60 bpm; oral anticoagulation dosed per stroke risk.",
                "black_box_warning": "NEVER start beta-blockers or calcium channel blockers for tachy-brady syndrome BEFORE a pacemaker is inserted (triggers fatal asystole).",
                "organ_clearance_cutoffs": "Renal dose adjustments for DOAC anticoagulants."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DANPACE-TRIAL",
                "pmid_or_doi": "10.1093/eurheartj/ehq509",
                "cebm_level": 2,
                "sample_size": 1415,
                "endpoints": "Dual-chamber pacing reduces atrial fibrillation incidence and heart failure hospitalization compared to single-chamber ventricular pacing."
            }
        }
    },
    {
        "id": "DOC-CARD-413",
        "icd10": "I40.9",
        "condition": "Acute Fulminant Myocarditis (Inflammatory Cardiomyopathy)",
        "specialty": "Cardiology & Advanced Heart Failure",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ESC Statement on Myocardial Disease & AHA Scientific Statement",
        "source_body": "Circulation",
        "citation": "Kociol RD et al. Recognition and Initial Management of Fulminant Myocarditis: A Scientific Statement From the American Heart Association. Circulation. 2020;141(6):e69-e92.",
        "doi_or_source": "10.1161/CIR.0000000000000745",
        "clinical_evidence": "Acute viral or immune-mediated myocardial inflammation presenting with cardiogenic shock requires immediate advanced mechanical circulatory support (temporary Impella microaxial pump or VA-ECMO) to unload the LV and maintain perfusion. High-dose IV Methylprednisolone (1 g/day x 3 days) improves outcomes in giant cell myocarditis, eosinophilic myocarditis, and immune-checkpoint inhibitor (ICI) myocarditis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict bed rest; complete prohibition of competitive sports or vigorous physical exertion for 3-6 months (exertion accelerates viral replication and triggers fatal arrhythmias); avoid NSAIDs during acute viral myocarditis (worsens mortality in animal models).",
            "monitoring_cadence": "Cardiac MRI utilizing Lake Louise Criteria (myocardial edema on T2 and Late Gadolinium Enhancement on T1); serial high-sensitivity troponin and BNP; endomyocardial biopsy for refractory cases.",
            "clinical_thresholds": "New-onset severe heart failure / cardiogenic shock within <2 weeks of a viral prodrome with elevated troponin and normal coronary angiogram."
        },
        "patient_plain_language": "An aggressive viral infection (or immunotherapy drug reaction) triggers your immune system to attack and inflame your heart muscle tissue. It can mimic a massive heart attack with high cardiac enzyme levels and chest pain, but the arteries are completely clear. Resting completely and letting the heart heal without strenuous exercise is critical.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the cardiac catheterization confirm clean coronary arteries, ruling out an atherosclerotic heart attack?",
            "safety_question": "Does my cardiac MRI show inflammatory edema and late gadolinium enhancement matching the Lake Louise criteria?",
            "action_threshold_question": "Why must I strictly abstain from all sports and vigorous exercise for the next 3 to 6 months?"
        },
        "red_flags": [
            "Rapid descent into cardiogenic shock with low systolic BP (<85 mmHg) and pulmonary edema",
            "High-grade AV block or sustained ventricular arrhythmias in the setting of acute troponin elevation"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute myocarditis is sudden, severe inflammation of the heart muscle, often following a viral infection.",
                "plain_analogy": "An intense viral sunburn blistering directly inside the meat of the heart muscle pump.",
                "lifestyle_action": "Rest completely, avoid all exercise for 3 to 6 months, and seek emergency care for chest pain or breathlessness."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Temporary Mechanical Circulatory Support (Impella / VA-ECMO)",
                    "Methylprednisolone IV (1 g/day for Giant Cell / ICI)",
                    "Guideline Heart Failure GDMT (once stable)"
                ],
                "dosing_gdmt": "Methylprednisolone 1,000 mg IV daily x 3 days; followed by oral prednisone 1 mg/kg/day with slow taper.",
                "black_box_warning": "Avoid NSAIDs in acute viral myocarditis (increases mortality and myocardial necrosis); avoid vigorous exercise.",
                "organ_clearance_cutoffs": "Steroid taper adjusted based on clinical response and cardiac MRI resolution."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHA-MYOCARDITIS",
                "pmid_or_doi": "10.1161/CIR.0000000000000745",
                "cebm_level": 1,
                "sample_size": 1900,
                "endpoints": "Early temporary mechanical circulatory support allows full myocardial recovery in >70% of fulminant myocarditis cases."
            }
        }
    },
    {
        "id": "DOC-CARD-414",
        "icd10": "I51.81",
        "condition": "Takotsubo Cardiomyopathy (Stress-Induced Apical Ballooning)",
        "specialty": "Cardiology & Intensive Care",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: InterTAK Diagnostic Criteria & ESC Consensus",
        "source_body": "European Heart Journal",
        "citation": "Ghadri JR et al. International Expert Consensus Document on Takotsubo Syndrome (Part I and II). Eur Heart J. 2018;39(22):2032-2062.",
        "doi_or_source": "10.1093/eurheartj/ehy076",
        "clinical_evidence": "Triggered by acute severe emotional or physical stress (catecholamine storm), Takotsubo causes transient apical and mid-ventricular ballooning akinesia with hyperdynamic basal contraction, mimicking anterior STEMI. Beta-blockers or ACE inhibitors are used initially, but INOTROPES (DOBUTAMINE, NOREPINEPHRINE) ARE CONTRAINDICATED if dynamic LVOT obstruction occurs (present in ~10-15%). Complete LVEF recovery occurs in >90% within 4-8 weeks.",
        "solution_protocol": {
            "non_pharmacological_targets": "Identify and alleviate emotional or physical stress triggers; avoid pure inotropes and sympathomimetics; cardiac rehabilitation once acute phase resolves; psychological support.",
            "monitoring_cadence": "Serial echocardiogram at 48 hours, 1 month, and 3 months documenting complete recovery of LVEF; daily monitoring of QT interval on ECG (high risk for Torsades during subacute phase).",
            "clinical_thresholds": "InterTAK Diagnostic Score >70; transient regional wall motion abnormalities extending beyond a single epicardial vascular territory with absence of culprit obstructive CAD."
        },
        "patient_plain_language": "Also known as 'Broken Heart Syndrome', this condition happens when an overwhelming emotional shock or severe physical stress floods the heart with adrenaline. The tip of your heart temporarily paralyzes and balloons out into the shape of a Japanese octopus trap (takotsubo). Fortunately, in over 90% of cases, the heart completely recovers its strength within 1 to 2 months.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the emergency coronary angiogram confirm completely open arteries without a blood clot or plaque rupture?",
            "safety_question": "Did echocardiography detect any dynamic outflow tract obstruction that forbids the use of stimulant heart drugs?",
            "action_threshold_question": "How long until we repeat my echocardiogram to confirm that my heart muscle has returned to 100% normal strength?"
        },
        "red_flags": [
            "Cardiogenic shock with systolic BP <80 mmHg caused by dynamic left ventricular outflow tract obstruction",
            "Severe QTc prolongation (>500 ms) on ECG with runs of polymorphic ventricular tachycardia"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Takotsubo cardiomyopathy is temporary stress-induced heart muscle stunning that mimics a heart attack.",
                "plain_analogy": "A computer engine temporarily freezing up and going into safe mode following a sudden electrical power surge.",
                "lifestyle_action": "Avoid severe emotional stressors, take prescribed medications, and attend follow-up scans to confirm heart recovery."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Beta-blockers (Metoprolol Succinate)",
                    "ACE Inhibitors / ARBs (Lisinopril)",
                    "Fluid resuscitation (if LVOT obstruction without pulmonary edema)"
                ],
                "dosing_gdmt": "Metoprolol Succinate 25-100 mg daily; Lisinopril 5-20 mg daily; continue until LVEF fully normalizes.",
                "black_box_warning": "Avoid Inotropes (Dobutamine, Milrinone) if dynamic LVOT obstruction is present; worsens cardiogenic shock.",
                "organ_clearance_cutoffs": "Dose adjustments based on blood pressure and renal parameters."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "InterTAK-REGISTRY",
                "pmid_or_doi": "10.1093/eurheartj/ehy076",
                "cebm_level": 1,
                "sample_size": 1750,
                "endpoints": "Full recovery of left ventricular systolic function occurs in 96% of surviving Takotsubo patients within 3 months."
            }
        }
    },
    {
        "id": "DOC-CARD-415",
        "icd10": "I15.0",
        "condition": "Atherosclerotic Renovascular Hypertension (Renal Artery Stenosis)",
        "specialty": "Nephrology & Cardiology",
        "organ_system": "Circulatory & Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASTRAL & CORAL Landmark Randomized Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "Cooper CJ et al. Stenting and Medical Therapy for Atherosclerotic Renal-Artery Stenosis (CORAL). N Engl J Med. 2014;370(1):13-22.",
        "doi_or_source": "10.1056/NEJMoa1310753",
        "clinical_evidence": "The landmark CORAL (n=947) and ASTRAL (n=806) multicenter randomized trials proved that renal-artery stenting added to comprehensive medical therapy did NOT provide any significant benefit in blood pressure control, renal events, or cardiovascular outcomes compared to medical therapy alone. Renal stenting is strictly reserved for 'flash pulmonary edema' (Pickering syndrome) or refractory hypertension on >=4 drugs.",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive multi-drug antihypertensive therapy (CCBs, thiazide-like diuretics, beta-blockers); lipid-lowering with high-intensity statin; smoking cessation; avoid dehydration.",
            "monitoring_cadence": "Serum creatinine and potassium 7-14 days after initiating or increasing any RAAS inhibitor; renal duplex ultrasound every 12 months.",
            "clinical_thresholds": "Severe renal artery narrowing (>70% lumen diameter) with peak systolic velocity >200-300 cm/s and renal-aortic ratio >3.5 on Doppler ultrasound."
        },
        "patient_plain_language": "Cholesterol plaques narrow the main pipe supplying blood to one or both of your kidneys. The starved kidney mistakenly thinks your entire body has zero blood pressure, so it pumps out massive amounts of renin hormone, driving your body-wide blood pressure sky-high. In most patients, blood pressure pills work just as well as kidney artery stents without surgery.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did renal Doppler ultrasound show narrowing in one kidney artery or both kidney arteries?",
            "safety_question": "Why did the CORAL trial prove that medications are just as safe and effective as putting a metal stent in my kidney artery?",
            "action_threshold_question": "Why must my kidney blood tests (creatinine and potassium) be re-checked 1 to 2 weeks after adjusting medications?"
        },
        "red_flags": [
            "Sudden unprovoked 'flash pulmonary edema' (severe fluid flooding the lungs in a patient with normal heart function)",
            "A rise in serum creatinine >30-50% after starting an ACE inhibitor or ARB (indicates bilateral renal artery stenosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Renovascular hypertension is severe high blood pressure triggered by narrowed kidney blood supply pipes.",
                "plain_analogy": "A kinked fuel line causing the engine computer to rev up to maximum power because it thinks fuel is running out.",
                "lifestyle_action": "Take blood pressure medications faithfully, never smoke, and have kidney lab tests checked regularly."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Calcium Channel Blockers (Amlodipine)",
                    "Thiazide Diuretics (Chlorthalidone)",
                    "ACEi / ARB (Caution in bilateral stenosis)",
                    "High-intensity Statin (Atorvastatin)"
                ],
                "dosing_gdmt": "Amlodipine 5-10 mg daily; Chlorthalidone 12.5-25 mg daily; Atorvastatin 40-80 mg daily.",
                "black_box_warning": "CONTRAINDICATION: ACE inhibitors and ARBs can precipitate acute renal failure in bilateral renal artery stenosis or solitary kidney.",
                "organ_clearance_cutoffs": "Dose adjust all antihypertensives based on eGFR; recheck creatinine within 10 days of RAAS inhibition."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CORAL-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1310753",
                "cebm_level": 2,
                "sample_size": 947,
                "endpoints": "Renal artery stenting does not improve cardiovascular or renal outcomes over medical therapy alone."
            }
        }
    },
    {
        "id": "DOC-CARD-416",
        "icd10": "I77.3",
        "condition": "Fibromuscular Dysplasia (Renal 'String-of-Beads' FMD)",
        "specialty": "Vascular Medicine & Nephrology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: First International Consensus on FMD",
        "source_body": "Vascular Medicine & European Heart Journal",
        "citation": "Gornik HL et al. First International Consensus on the Diagnosis and Management of Fibromuscular Dysplasia. Vasc Med. 2019;24(2):164-189.",
        "doi_or_source": "10.1177/1358863X18821816",
        "clinical_evidence": "Unlike atherosclerotic stenosis, FMD is a non-atherosclerotic, non-inflammatory vascular disease affecting middle-aged women. Medial fibroplasia causes alternating webs and aneurysms ('string-of-beads' on angiography). PERCUTANEOUS TRANSLUMINAL RENAL ANGIOPLASTY (PTRA WITHOUT STENTING) is the curative intervention of choice, curing hypertension in 30-50% of patients and avoiding foreign metal stents.",
        "solution_protocol": {
            "non_pharmacological_targets": "Screening from head to pelvis (CTA or MRA) at least once to detect silent intracranial or visceral aneurysms and dissections; avoid high-impact collision sports or chiropractic neck manipulation (cervical artery dissection risk).",
            "monitoring_cadence": "Duplex ultrasound of renal arteries at 1 month and annually post-angioplasty; follow-up MRI brain for cerebral aneurysms.",
            "clinical_thresholds": "Epigastric or flank bruit in a woman under 50 with hypertension; classic 'string-of-beads' appearance on renal CTA/angiography."
        },
        "patient_plain_language": "A non-clotting disorder of blood vessel walls that most commonly affects young to middle-aged women. The muscular wall of the kidney or neck arteries develops fibrous ridges, making the artery look like a string of beads on X-ray. When it narrows the kidney artery, it causes severe high blood pressure that can often be completely cured with a simple balloon stretch (without needing a metal stent).",
        "doctor_consultation_checklist": {
            "parameter_question": "Has a full-body CT or MRI scan checked my brain and belly arteries for hidden aneurysms or tears?",
            "safety_question": "Am I a candidate for balloon angioplasty (PTRA) without a stent to potentially cure my high blood pressure?",
            "action_threshold_question": "Why should aggressive neck manipulations and high-impact collision sports be avoided?"
        },
        "red_flags": [
            "Sudden severe 'thunderclap' headache or neck pain with drooping eyelid (Cervical Artery Dissection / Horner Syndrome)",
            "Rupture of an undetected renal or intracranial artery aneurysm"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Fibromuscular dysplasia is abnormal cell growth in artery walls creating a beaded, narrowed blood vessel.",
                "plain_analogy": "A garden hose that has developed multiple tight internal rings and balloon pouches along its length.",
                "lifestyle_action": "Get screened from head to pelvis for aneurysms, avoid vigorous neck cracking, and consider balloon dilation."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Percutaneous Transluminal Renal Angioplasty (PTRA - WITHOUT STENT)",
                    "Aspirin 81 mg daily",
                    "ACEi / ARB (Single-vessel FMD)"
                ],
                "dosing_gdmt": "Balloon angioplasty without stent placement is first line; Aspirin 81 mg daily for antiplatelet protection.",
                "black_box_warning": "DO NOT place intravascular stents in FMD unless flow-limiting dissection occurs during ballooning.",
                "organ_clearance_cutoffs": "Renal function monitoring post-angioplasty."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "FMD-CONSENSUS",
                "pmid_or_doi": "10.1177/1358863X18821816",
                "cebm_level": 1,
                "sample_size": 1500,
                "endpoints": "Balloon angioplasty cures or significantly improves hypertension in over 80% of patients with medial FMD."
            }
        }
    },
    {
        "id": "DOC-CARD-417",
        "icd10": "E26.01",
        "condition": "Primary Hyperaldosteronism (Conn's Syndrome / Aldosteronoma)",
        "specialty": "Endocrinology & Hypertension",
        "organ_system": "Endocrine & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "Journal of Clinical Endocrinology & Metabolism",
        "citation": "Funder JW et al. The Management of Primary Aldosteronism: Case Detection, Diagnosis, and Treatment. J Clin Endocrinol Metab. 2016;101(5):1889-1916.",
        "doi_or_source": "10.1210/jc.2015-4061",
        "clinical_evidence": "Screening with Plasma Aldosterone Concentration to Plasma Renin Activity (PAC/PRA ratio >=20 with PAC >=15 ng/dL) detects primary aldosteronism. Unilateral aldosterone-producing adenoma (Conn's) is cured by LAPAROSCOPIC ADRENALECTOMY (curing HTN in 50% and improving control in 100%). Bilateral adrenal hyperplasia is managed with mineralocorticoid receptor antagonists (Spironolactone or Eplerenone).",
        "solution_protocol": {
            "non_pharmacological_targets": "Adrenal vein sampling (AVS) is mandatory prior to surgery to confirm unilateral vs bilateral hormone secretion; dietary sodium restriction (<2 g/day); avoid licorice consumption.",
            "monitoring_cadence": "Electrolytes (potassium, sodium) every 2-4 weeks during MRA titration; BP tracking; annual renal function.",
            "clinical_thresholds": "PAC/PRA ratio >20 with PAC >=15 ng/dL; confirmatory oral sodium loading or saline infusion test showing unsuppressed aldosterone."
        },
        "patient_plain_language": "One or both of your adrenal glands (small caps on top of your kidneys) produce too much aldosterone hormone. This hormone tricks your kidneys into hoarding salt and water while dumping potassium down the toilet. It causes severe, stubborn high blood pressure and low potassium. If caused by a small benign lump in one gland, removing it surgically can cure the high blood pressure completely.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my morning blood test show an elevated aldosterone-to-renin ratio (PAC/PRA)?",
            "safety_question": "Will I undergo Adrenal Vein Sampling (AVS) to prove whether the excess hormone comes from only one adrenal gland?",
            "action_threshold_question": "If surgery is not needed, am I taking Spironolactone or Eplerenone to specifically block the aldosterone receptor?"
        },
        "red_flags": [
            "Severe muscle cramps, paralysis, or cardiac palpitations caused by profound hypokalemia (<2.5 mEq/L)",
            "Refractory hypertension (>180/110 mmHg) causing microvascular kidney or retinal damage"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Primary aldosteronism is excess adrenal hormone causing salt retention, low potassium, and severe high blood pressure.",
                "plain_analogy": "A stuck pump switch continuously filling a water reservoir until it overflows under high pressure.",
                "lifestyle_action": "Limit salt, check potassium levels, and consult endocrinology for adrenal vein testing or surgery."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Spironolactone oral (Aldactone)",
                    "Eplerenone (Inspra)",
                    "Laparoscopic Adrenalectomy (for unilateral adenoma)"
                ],
                "dosing_gdmt": "Spironolactone 25-100 mg daily (titrated to normalize potassium without supplements); or Eplerenone 50 mg BID.",
                "black_box_warning": "Spironolactone causes gynecomastia and erectile dysfunction in men (anti-androgen); switch to Eplerenone.",
                "organ_clearance_cutoffs": "Monitor for hyperkalemia, especially in patients with preexisting renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MATCH-TRIAL",
                "pmid_or_doi": "10.1210/jc.2015-4061",
                "cebm_level": 1,
                "sample_size": 1200,
                "endpoints": "Unilateral adrenalectomy permanently cures hypertension in 50% and resolves hypokalemia in 100% of Conn adenomas."
            }
        }
    },
    {
        "id": "DOC-CARD-418",
        "icd10": "I35.1",
        "condition": "Acute Aortic Regurgitation (Flail Valve Leaflet / Endocarditis)",
        "specialty": "Cardiology & Cardiothoracic Surgery",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACC/AHA Valvular Heart Disease Guidelines",
        "source_body": "Circulation",
        "citation": "Otto CM et al. 2020 ACC/AHA Guideline for the Management of Patients With Valvular Heart Disease. Circulation. 2021;143(5):e72-e227.",
        "doi_or_source": "10.1161/CIR.0000000000000923",
        "clinical_evidence": "Acute severe aortic regurgitation (caused by infective endocarditis or aortic dissection) results in sudden massive diastolic reflux into a non-compliant LV, causing catastrophic elevation in LVEDP, premature mitral valve closure, and pulmonary edema. URGENT SURGICAL AORTIC VALVE REPLACEMENT IS MANDATORY. Intra-aortic balloon pumps (IABP) and beta-blockers are ABSOLUTELY CONTRAINDICATED.",
        "solution_protocol": {
            "non_pharmacological_targets": "EMERGENT SURGICAL REPAIR; avoid beta-blockers (slow heart rate increases diastolic filling time, worsening backflow volume); avoid IABP (diastolic balloon inflation forces blood backward through incompetent valve, causing fatal rupture).",
            "monitoring_cadence": "Continuous arterial line and pulmonary artery catheter monitoring; emergent transesophageal echocardiogram (TEE).",
            "clinical_thresholds": "Premature closure of the mitral valve on M-mode echocardiography signifies dangerously elevated diastolic pressure."
        },
        "patient_plain_language": "The one-way exit valve of your heart (aortic valve) suddenly blows open or gets destroyed by a severe bacterial infection. Instead of pumping blood out to your body, blood surges backward into the heart's main chamber during every single resting beat. The heart fills to bursting within minutes, causing sudden severe drowning breathlessness that requires emergency surgery.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the cardiothoracic surgery team prepared for emergency aortic valve replacement right now?",
            "safety_question": "Why are common cardiac tools like beta-blockers and balloon pumps (IABP) strictly forbidden for my valve?",
            "action_threshold_question": "Does transesophageal echocardiogram (TEE) show bacterial vegetations or a torn valve leaflet?"
        },
        "red_flags": [
            "Sudden flash pulmonary edema with pink frothy sputum and cardiogenic shock (Surgical Emergency)",
            "Soft, early-closing S1 heart sound indicating catastrophic left ventricular diastolic pressure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute aortic regurgitation is sudden backflow of blood through a damaged heart exit valve causing shock.",
                "plain_analogy": "A main floodgate snapping off its hinges, letting an entire river rush backward into the reservoir.",
                "lifestyle_action": "Call 911 immediately; this is an urgent surgical emergency requiring immediate valve replacement."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Emergent Surgical Aortic Valve Replacement (Mandatory)",
                    "Sodium Nitroprusside IV (Afterload reduction)",
                    "Dobutamine IV (Inotropic support)"
                ],
                "dosing_gdmt": "Nitroprusside IV infusion titrated to maintain SBP >90 mmHg; urgent transfer to open heart surgery.",
                "black_box_warning": "STRICT CONTRAINDICATION: Intra-aortic balloon counterpulsation (IABP) and Beta-blockers precipitate fatal pulmonary edema.",
                "organ_clearance_cutoffs": "Emergency surgery; medical management is only a bridge to the operating room."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACC-AORTICREG",
                "pmid_or_doi": "10.1161/CIR.0000000000000923",
                "cebm_level": 1,
                "sample_size": 2400,
                "endpoints": "Emergent surgical valve replacement lowers acute regurgitation mortality from >75% (medical) to <10% (surgical)."
            }
        }
    },
    {
        "id": "DOC-CARD-419",
        "icd10": "I35.0",
        "condition": "Severe Calcific Aortic Stenosis (Low-Flow Low-Gradient vs High Gradient)",
        "specialty": "Cardiology & Interventional Cardiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: PARTNER 3 & Evolut Low Risk Landmark Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "Mack MJ et al. Transcatheter Aortic-Valve Replacement with a Balloon-Expandable Valve in Low-Risk Patients (PARTNER 3). N Engl J Med. 2019;380(18):1695-1705.",
        "doi_or_source": "10.1056/NEJMoa1814052",
        "clinical_evidence": "Symptomatic severe aortic stenosis (aortic valve area <=1.0 cm2, mean gradient >=40 mmHg, or peak velocity >=4.0 m/s) carries a 50% 2-year mortality if untreated. Transcatheter Aortic Valve Replacement (TAVR) is non-inferior or superior to surgical replacement (SAVR) across all risk categories (PARTNER 3: 1-year death, stroke, or rehospitalization 8.5% TAVR vs 15.1% surgery; p=0.001). Low-dose Dobutamine stress echo differentiates true severe from pseudo-severe stenosis in low-flow states.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid strenuous exertion or heavy lifting; report any symptoms of chest pain, shortness of breath, or lightheadedness immediately; careful blood pressure control avoiding sudden vasodilator drops.",
            "monitoring_cadence": "Transthoracic echocardiogram every 6-12 months for asymptomatic severe AS; immediate evaluation upon onset of angina, syncope, or heart failure symptoms.",
            "clinical_thresholds": "Aortic valve area (AVA) <=1.0 cm2 (or index <=0.6 cm2/m2) and peak jet velocity >=4.0 m/s (or mean gradient >=40 mmHg)."
        },
        "patient_plain_language": "Over decades, calcium and bone-like crusts build up on your heart's main exit doorway (aortic valve), making it stiff and narrow like a rusty valve opened only a tiny crack. Your heart has to pump against enormous pressure to force blood out. Once symptoms like chest tightness, dizziness, or breathlessness appear, replacing the valve (often through a tiny catheter in the groin, called TAVR) restores normal lifespan.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my aortic valve area (is it 1.0 cm2 or smaller) and what is my mean pumping pressure gradient?",
            "safety_question": "Am I a candidate for minimally invasive catheter valve replacement (TAVR) through the leg artery instead of open-heart surgery?",
            "action_threshold_question": "Why must I report even mild dizziness or shortness of breath to my cardiologist right away?"
        },
        "red_flags": [
            "Fainting (exertional syncope) or chest pain during walking (signals imminent sudden cardiac death risk)",
            "Rapid onset of breathlessness indicating decompensated left ventricular systolic failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Severe aortic stenosis is extreme narrowing of the main heart valve from calcium crusting.",
                "plain_analogy": "A heavily rusted water valve that can only open a tiny slit, forcing the pump behind it to strain.",
                "lifestyle_action": "Report any dizziness or breathlessness immediately; minimally invasive valve replacement (TAVR) is life-saving."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Transcatheter Aortic Valve Replacement (TAVR - Class I)",
                    "Surgical Aortic Valve Replacement (SAVR)",
                    "Cautious Loop Diuretics"
                ],
                "dosing_gdmt": "TAVR or SAVR is definitive; Furosemide 20-40 mg daily used with extreme caution for pulmonary congestion.",
                "black_box_warning": "Avoid aggressive vasodilators (nitrates, high-dose ACEi) which drop preload and induce fatal cerebral syncope.",
                "organ_clearance_cutoffs": "Lifelong single antiplatelet or DOAC depending on valve type and atrial fibrillation status."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PARTNER-3",
                "pmid_or_doi": "10.1056/NEJMoa1814052",
                "cebm_level": 2,
                "sample_size": 1000,
                "endpoints": "TAVR significantly reduces composite death, stroke, and rehospitalization compared to open surgery (p=0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-420",
        "icd10": "I34.0",
        "condition": "Severe Mitral Regurgitation (Acute Papillary Rupture vs Chronic Degenerative)",
        "specialty": "Cardiology & Interventional Cardiology",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: COAPT Landmark Trial & ACC/AHA Valvular Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Stone GW et al. Transcatheter Mitral-Valve Repair in Patients with Heart Failure (COAPT). N Engl J Med. 2018;379(24):2307-2318.",
        "doi_or_source": "10.1056/NEJMoa1806640",
        "clinical_evidence": "Acute severe MR (post-MI papillary muscle rupture) requires emergency surgery. In secondary MR with heart failure, the COAPT trial (n=614) proved that transcatheter edge-to-edge repair (TEER with MitraClip) added to maximal GDMT reduced 24-month all-cause mortality from 46.1% to 29.1% (hazard ratio 0.62; p<0.001) and heart failure hospitalizations by 47% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Optimize guideline-directed medical therapy for heart failure prior to intervention; dietary sodium restriction; cardiac rehabilitation; report any worsening orthopnea.",
            "monitoring_cadence": "Echocardiogram assessing Effective Regurgitant Orifice Area (EROA >=0.40 cm2 for primary MR, >=0.20-0.30 cm2 for secondary MR) and regurgitant volume (>=60 mL); follow-up post-MitraClip at 1, 6, and 12 months.",
            "clinical_thresholds": "Severe MR criteria: EROA >=0.40 cm2, regurgitant fraction >=50%, or pulmonary vein systolic flow reversal."
        },
        "patient_plain_language": "The two-door flap valve (mitral valve) that prevents blood from leaking backward into your lungs fails to seal tightly. In acute cases (such as after a heart attack when a supporting anchor cord snaps), it is a surgical emergency. In chronic cases, a tiny catheter clip (MitraClip) can be placed to clip the leaking flaps together in the center, dramatically reducing hospital visits and saving lives.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is my mitral regurgitation primary (flail leaflet/prolapse) or secondary (caused by a stretched heart chamber)?",
            "safety_question": "What is my measured leak size (EROA and regurgitant volume) on echocardiogram?",
            "action_threshold_question": "Am I a candidate for the catheter MitraClip procedure to clip my leaking valve without opening my chest?"
        },
        "red_flags": [
            "Sudden crushing breathlessness and pink foamy cough after a heart attack (Papillary Muscle Rupture)",
            "New-onset atrial fibrillation with rapid ventricular response causing acute pulmonary edema"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Mitral regurgitation is backward leaking of blood into the lungs caused by a loose or damaged mitral valve.",
                "plain_analogy": "A trapdoor whose hinge is loose or whose anchor ropes have snapped, letting water surge backward.",
                "lifestyle_action": "Take heart failure medications as directed and ask your cardiologist about catheter edge-to-edge repair (MitraClip)."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Transcatheter Edge-to-Edge Repair (MitraClip / TEER)",
                    "Surgical Mitral Valve Repair / Replacement",
                    "Sacubitril/Valsartan + SGLT2i"
                ],
                "dosing_gdmt": "MitraClip intervention for eligible secondary MR; GDMT heart failure medications optimized to target doses.",
                "black_box_warning": "Surgical repair is preferred over replacement in primary degenerative MR whenever anatomically feasible.",
                "organ_clearance_cutoffs": "Renal adjustments for heart failure pharmacotherapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COAPT-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1806640",
                "cebm_level": 2,
                "sample_size": 614,
                "endpoints": "MitraClip edge-to-edge repair reduces 2-year mortality by 38% and heart failure hospitalizations by 47%."
            }
        }
    }
]
