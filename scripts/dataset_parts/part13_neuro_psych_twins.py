"""
part13_neuro_psych_twins.py
"""

PART_13_DISEASES = [
    {
        "id": "DOC-CARD-341",
        "icd10": "I63.9",
        "condition": "Acute Ischemic Stroke (LVO / Thrombolytic Candidate)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA Stroke Guidelines",
        "source_body": "Stroke & NEJM",
        "citation": "Powers WJ et al. 2018 Guidelines for the Early Management of Patients with Acute Ischemic Stroke. Stroke. 2018;49(3):e46-e110.",
        "doi_or_source": "10.1161/STR.0000000000000158",
        "clinical_evidence": "Intravenous Alteplase (0.9 mg/kg within 4.5 hours) plus endovascular thrombectomy (within 24 hours for large vessel occlusions in DAWN/DEFUSE-3) reduces 90-day disability from 55% to 28% (NNT=2.8; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Emergency stroke team activation; maintain head flat or elevated 30 degrees; maintain oxygen saturation >=94%; permissive hypertension up to 185/110 mmHg prior to tPA.",
            "monitoring_cadence": "NIH Stroke Scale (NIHSS) hourly; neuro checks every 15 min during infusion.",
            "clinical_thresholds": "Blood pressure >185/110 mmHg must be lowered with Labetalol/Nicardipine prior to thrombolysis."
        },
        "patient_plain_language": "A blood clot clogs an artery supplying blood to your brain, causing sudden facial drooping, arm weakness, and slurred speech. Every minute delayed, 1.9 million brain cells starve and die.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact 'last known well' time for my loved one?",
            "safety_question": "Is the patient eligible for emergency clot-busting medicine (tPA) or mechanical thrombectomy?",
            "action_threshold_question": "What is the current NIH Stroke Scale score?"
        },
        "red_flags": [
            "Sudden one-sided weakness, facial droop, or loss of speech (BE-FAST - Emergency Code Stroke)",
            "Sudden loss of balance, vision loss, or confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute ischemic stroke is a blocked brain artery causing sudden paralysis or speech loss.",
                "plain_analogy": "A clogged water pipe in a garden that causes the flowers downstream to wither rapidly.",
                "lifestyle_action": "Memorize BE-FAST (Balance, Eyes, Face, Arms, Speech, Time) and call 911 immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Alteplase IV (tPA)",
                    "Tenecteplase IV",
                    "Aspirin 325 mg (after 24h post-tPA)"
                ],
                "dosing_gdmt": "Alteplase 0.9 mg/kg (max 90 mg; 10% bolus over 1 min, remainder over 60 min).",
                "black_box_warning": "Alteplase: Risk of fatal intracranial hemorrhage. Monitor BP strictly.",
                "organ_clearance_cutoffs": "Permissive hypertension allows cerebral perfusion."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHA-STROKE",
                "pmid_or_doi": "10.1161/STR.0000000000000158",
                "cebm_level": 1,
                "sample_size": 14500,
                "endpoints": "Thrombolysis plus mechanical thrombectomy yields functional independence in 49% vs 13% standard care."
            }
        }
    },
    {
        "id": "DOC-CARD-342",
        "icd10": "I61.9",
        "condition": "Acute Spontaneous Intracerebral Hemorrhage (ICH)",
        "specialty": "Neurology & Neurosurgery",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA ICH Guidelines",
        "source_body": "Stroke & Lancet",
        "citation": "Greenberg SM et al. 2022 Guideline for the Management of Patients with Spontaneous Intracerebral Hemorrhage. Stroke. 2022;53(7):e282-e361.",
        "doi_or_source": "10.1161/STR.0000000000000407",
        "clinical_evidence": "Immediate intensive SBP lowering (target 130-140 mmHg within 1 hour in INTERACT-2) and urgent reversal of anticoagulation (4-factor PCC for warfarin, Andexanet alfa for DOACs) reduces hematoma expansion by 48% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "THROMBOLYTICS STRICTLY CONTRAINDICATED; elevate head of bed 30 degrees; ICU admission; reverse coagulopathy within 60 minutes; neurosurgical consultation for cerebellar hematomas >3 cm.",
            "monitoring_cadence": "Continuous invasive arterial line BP monitoring; follow-up head CT at 24 hours.",
            "clinical_thresholds": "Target systolic BP 130-140 mmHg; avoid dropping SBP <120 mmHg to prevent renal injury."
        },
        "patient_plain_language": "A blood vessel inside your brain bursts open under high pressure, bleeding directly into brain tissue. It creates a growing pool of blood that compresses delicate brain centers, causing sudden excruciating headache and paralysis.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has a non-contrast head CT ruled out ischemic stroke and confirmed bleeding?",
            "safety_question": "Have we immediately reversed any blood-thinner pills with specific antidote medicine?",
            "action_threshold_question": "Is my blood pressure being rapidly lowered to 130-140 mmHg to stop the bleeding?"
        },
        "red_flags": [
            "Rapid neurological deterioration with blown pupil (herniation)",
            "Coma or severe obtundation requiring emergency intubation"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Intracerebral hemorrhage is a bleeding emergency inside brain tissue caused by a ruptured blood vessel.",
                "plain_analogy": "A burst water pipe that floods and destroys the drywall inside a room.",
                "lifestyle_action": "Strictly control high blood pressure, take blood pressure pills daily, and avoid heavy alcohol."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Nicardipine IV infusion",
                    "4-Factor Prothrombin Complex Concentrate (Kcentra)",
                    "Andexanet alfa"
                ],
                "dosing_gdmt": "Nicardipine 5 mg/h IV titrated up to 15 mg/h; Kcentra 25-50 units/kg for warfarin reversal.",
                "black_box_warning": "Thrombolytics and antiplatelets are strictly contraindicated.",
                "organ_clearance_cutoffs": "Renal and hepatic clearance considerations during ICU care."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "INTERACT-2",
                "pmid_or_doi": "10.1161/STR.0000000000000407",
                "cebm_level": 1,
                "sample_size": 2839,
                "endpoints": "Rapid intensive BP lowering reduces hematoma expansion and improves functional recovery."
            }
        }
    },
    {
        "id": "DOC-CARD-343",
        "icd10": "I60.9",
        "condition": "Aneurysmal Subarachnoid Hemorrhage (aSAH)",
        "specialty": "Neurosurgery & Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA Guidelines",
        "source_body": "Stroke & NEJM",
        "citation": "Hoh BL et al. 2023 Guideline for the Management of Patients with Aneurysmal Subarachnoid Hemorrhage. Stroke. 2023;54(7):e314-e370.",
        "doi_or_source": "10.1161/STR.0000000000000436",
        "clinical_evidence": "Early aneurysm securing (endovascular coiling or surgical clipping within 24 hours) eliminates re-rupture risk (mortality >70%). Nimodipine (60 mg q4h for 21 days) reduces delayed cerebral ischemia and secondary cerebral infarction by 34% (RR 0.66; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Bedrest in quiet darkened room; maintain SBP <140-160 mmHg before coiling; enteral Nimodipine for 21 days; transcranial Doppler (TCD) daily to monitor for vasospasm on days 4-14.",
            "monitoring_cadence": "Continuous arterial BP, neuro checks every 1-2 hours; daily transcranial Doppler.",
            "clinical_thresholds": "Hunt and Hess Grade / Fisher Grade classification on initial CT."
        },
        "patient_plain_language": "A blister-like balloon (aneurysm) on a brain artery bursts, spraying blood into the fluid spaces around your brain. Patients describe it as the 'worst headache of my life' (a thunderclap headache reaching maximum agony in seconds).",
        "doctor_consultation_checklist": {
            "parameter_question": "Has an emergency CT angiogram located the bleeding brain aneurysm?",
            "safety_question": "Are we coiling or clipping the aneurysm within the first 24 hours to prevent re-bleeding?",
            "action_threshold_question": "Is Nimodipine scheduled around the clock to prevent brain artery clamping (vasospasm)?"
        },
        "red_flags": [
            "Sudden peak agony headache ('thunderclap') with stiff neck and vomiting",
            "Sudden coma or seizure at headache onset"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Subarachnoid hemorrhage is bleeding into the fluid surrounding the brain from a ruptured aneurysm.",
                "plain_analogy": "A pressurized water balloon popping on the roof of the brain, causing sudden intense shockwaves.",
                "lifestyle_action": "Never ignore a sudden severe thunderclap headache; seek emergency room care immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Nimodipine oral/enteral",
                    "Nicardipine IV",
                    "Levetiracetam (Keppra) for seizure prophylaxis"
                ],
                "dosing_gdmt": "Nimodipine 60 mg orally every 4 hours for 21 days; Nicardipine to maintain SBP <140 mmHg prior to securing.",
                "black_box_warning": "Nimodipine is strictly for ORAL or ENTERAL use; accidental IV injection is FATAL.",
                "organ_clearance_cutoffs": "Adjust dosing if severe hypotension occurs."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BRITISH-SAH",
                "pmid_or_doi": "10.1161/STR.0000000000000436",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Enteral Nimodipine reduces delayed cerebral ischemic infarction by 34% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-344",
        "icd10": "G47.31",
        "condition": "Central Sleep Apnea (Cheyne-Stokes Breathing)",
        "specialty": "Pulmonology & Neurology",
        "organ_system": "Respiratory & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASM Clinical Practice Guideline",
        "source_body": "Journal of Clinical Sleep Medicine",
        "citation": "Aurora RN et al. Practice Parameters for the Treatment of Central Sleep Apnea. J Clin Sleep Med. 2012;8(6):697-705.",
        "doi_or_source": "10.5664/jcsm.2366",
        "clinical_evidence": "Unlike obstructive sleep apnea, central sleep apnea stems from loss of brainstem respiratory drive or high loop gain. In heart failure patients, Adaptive Servo-Ventilation (ASV) is contraindicated if LVEF <=45% (SERVE-HF trial showed 28% increased all-cause mortality; HR 1.28; p=0.01). Continuous Positive Airway Pressure (CPAP) or nighttime supplemental oxygen remains first-line.",
        "solution_protocol": {
            "non_pharmacological_targets": "Optimize underlying heart failure GDMT (reduces central sleep apnea events by 50%); nocturnal supplemental oxygen (2-3 L/min via nasal cannula); avoid ASV in HFrEF.",
            "monitoring_cadence": "Polysomnography tracking central apnea-hypopnea index (cAHI) and Cheyne-Stokes respiration cycle.",
            "clinical_thresholds": "cAHI >=5 events/hour with central events comprising >50% of total apneas."
        },
        "patient_plain_language": "Unlike typical sleep apnea where your throat physically closes off, central sleep apnea happens when your brain simply forgets to tell your breathing muscles to breathe while you sleep. Breathing waxes and wanes in smooth rolling waves.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my central apnea index compared to obstructive apneas on my sleep study?",
            "safety_question": "Is my heart pumping function (ejection fraction) above 45% before considering specialized pressure machines?",
            "action_threshold_question": "Will supplemental oxygen at night help smooth out my breathing rhythm?"
        },
        "red_flags": [
            "Sudden severe nighttime breathlessness waking you from sleep (paroxysmal nocturnal dyspnea)",
            "Daytime micro-sleep episodes while driving or working"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Central sleep apnea is a disorder where the brain fails to send signals to muscles to breathe during sleep.",
                "plain_analogy": "A thermostat whose sensor is miscalibrated, making the furnace cycle on and off in slow rolling waves.",
                "lifestyle_action": "Treat underlying heart failure, avoid alcohol, and use prescribed nocturnal oxygen or CPAP."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Continuous Positive Airway Pressure (CPAP)",
                    "Nocturnal Oxygen therapy",
                    "Acetazolamide (Diamox)"
                ],
                "dosing_gdmt": "CPAP titrated to resolve apneas; Acetazolamide 125-250 mg at bedtime to stimulate respiratory drive.",
                "black_box_warning": "Adaptive Servo-Ventilation (ASV) is black-box contraindicated in heart failure with LVEF <=45%.",
                "organ_clearance_cutoffs": "Caution with acetazolamide in severe renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SERVE-HF",
                "pmid_or_doi": "10.5664/jcsm.2366",
                "cebm_level": 1,
                "sample_size": 1325,
                "endpoints": "Optimizing heart failure GDMT and CPAP reduces central apnea events without excess mortality."
            }
        }
    },
    {
        "id": "DOC-CARD-345",
        "icd10": "H40.20X0",
        "condition": "Acute Angle-Closure Glaucoma",
        "specialty": "Ophthalmology & Emergency Medicine",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO Preferred Practice Pattern",
        "source_body": "Ophthalmology",
        "citation": "Prum BE et al. Primary Angle Closure Preferred Practice Pattern Guidelines. Ophthalmology. 2016;123(1):P1-P40.",
        "doi_or_source": "10.1016/j.ophtha.2015.10.049",
        "clinical_evidence": "Laser Peripheral Iridotomy (LPI) provides definitive anatomic bypass, lowering intraocular pressure (IOP) from >50 mmHg to <20 mmHg in 95% of eyes, preventing permanent optic nerve ischemic blindness.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate ophthalmic emergency consultation; position patient supine (do NOT patch eye); emergency medical therapy: Timolol 0.5%, Apraclonidine 1%, Pilocarpine 1-2%, and IV Acetazolamide (500 mg).",
            "monitoring_cadence": "Intraocular pressure check every 30-60 minutes until <20 mmHg; gonioscopy of both eyes.",
            "clinical_thresholds": "IOP >40-60 mmHg with steamy cornea, fixed mid-dilated pupil, and severe eye pain."
        },
        "patient_plain_language": "A sudden plumbing blockage in your eye. The colored iris bulges forward, clamping shut the microscopic drain pipes. Fluid builds up rapidly to extreme pressure, causing severe eye pain, headache, seeing rainbow halos around lights, and risking blindness within hours.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current eye pressure number on the tonometer?",
            "safety_question": "Have we given eye drops and acetazolamide to lower the pressure immediately?",
            "action_threshold_question": "When can the ophthalmologist perform laser peripheral iridotomy to create a safety drain hole?"
        },
        "red_flags": [
            "Severe eye pain with cloudy steamy vision and fixed mid-dilated pupil (Immediate Ophthalmic Emergency)",
            "Nausea and vomiting accompanying severe unilateral headache and red eye"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute angle-closure glaucoma is a sudden, dangerous spike in eye pressure caused by blocked drainage canals.",
                "plain_analogy": "A clogged kitchen sink drain where water overflows and builds massive destructive pressure inside the pipes.",
                "lifestyle_action": "Seek emergency ophthalmic care immediately; never take antihistamines or decongestants if at risk of narrow angles."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetazolamide IV / oral",
                    "Timolol 0.5% ophthalmic",
                    "Apraclonidine 1%",
                    "Pilocarpine 2%"
                ],
                "dosing_gdmt": "Acetazolamide 500 mg IV stat; Timolol 1 drop + Apraclonidine 1 drop + Pilocarpine 1 drop every 15 min x 2.",
                "black_box_warning": "Avoid anticholinergics and pupil-dilating drops (precipitates pupillary block).",
                "organ_clearance_cutoffs": "Acetazolamide contraindicated in sulfa allergy or severe renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO-GLAUCOMA",
                "pmid_or_doi": "10.1016/j.ophtha.2015.10.049",
                "cebm_level": 1,
                "sample_size": 2200,
                "endpoints": "Medical pressure lowering followed by laser iridotomy saves functional vision in 95% of presenting eyes."
            }
        }
    },
    {
        "id": "DOC-CARD-346",
        "icd10": "G45.9",
        "condition": "Transient Ischemic Attack (High ABCD2 Score)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA Guidelines & POINT Trial",
        "source_body": "Stroke & NEJM",
        "citation": "Johnston SC et al. Clopidogrel and Aspirin in Acute Ischemic Stroke and High-Risk TIA (POINT). N Engl J Med. 2018;379(3):215-225.",
        "doi_or_source": "10.1056/NEJMoa1800410",
        "clinical_evidence": "The landmark POINT and CHANCE trials (n=10,000 patients with high-risk TIA ABCD2 >=4 or minor stroke) proved that Dual Antiplatelet Therapy (DAPT with Clopidogrel 300 mg load then 75 mg/day + Aspirin) for the first 21 days reduced subsequent ischemic stroke by 28% (HR 0.72; 95% CI 0.56-0.92; p=0.008).",
        "solution_protocol": {
            "non_pharmacological_targets": "Urgent hospital admission or rapid-access TIA clinic; calculate ABCD2 score (Age, BP, Clinical features, Duration, Diabetes); urgent MRI brain with diffusion-weighted imaging (DWI) and carotid vessel imaging within 24 hours.",
            "monitoring_cadence": "Neuro checks; continuous telemetry to detect paroxysmal atrial fibrillation; lipid panel.",
            "clinical_thresholds": "ABCD2 score >=4 or speech/motor deficit lasting >10 minutes carries high 48-hour stroke risk."
        },
        "patient_plain_language": "A transient ischemic attack (often called a 'mini-stroke') is a temporary blockage of a brain artery that clears on its own within minutes. It is a critical warning siren: without immediate preventative medicine, up to 10-20% of patients suffer a devastating permanent stroke within days.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my ABCD2 stroke risk score?",
            "safety_question": "Should I start dual blood-thinner pills (Aspirin + Plavix) for the next 21 days to prevent a major stroke?",
            "action_threshold_question": "Have we imaged my carotid neck arteries and checked for hidden atrial fibrillation?"
        },
        "red_flags": [
            "Return of weakness, numbness, or speech slurring (Active Stroke - Call 911 immediately)",
            "Carotid artery narrowing >70% requiring urgent surgical endarterectomy"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A TIA is a temporary stroke warning where symptoms resolve quickly but indicate high risk of permanent stroke.",
                "plain_analogy": "A temporary engine sputter from a fuel line blockage that clears, warning that the fuel pump is about to fail.",
                "lifestyle_action": "Take prescribed blood thinners every day, maintain low cholesterol, and quit smoking immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Aspirin",
                    "Clopidogrel (Plavix)",
                    "Atorvastatin 80 mg"
                ],
                "dosing_gdmt": "DAPT: Clopidogrel 300 mg load, then 75 mg daily + Aspirin 81 mg daily for 21 days, then monotherapy.",
                "black_box_warning": "Limit DAPT strictly to 21-30 days to avoid long-term major bleeding risks.",
                "organ_clearance_cutoffs": "High-intensity statin (Atorvastatin 80 mg) regardless of baseline cholesterol."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POINT-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1800410",
                "cebm_level": 2,
                "sample_size": 4881,
                "endpoints": "21 days of DAPT reduces subsequent stroke by 28% compared to aspirin monotherapy."
            }
        }
    },
    {
        "id": "DOC-CARD-347",
        "icd10": "M11.20",
        "condition": "Pseudogout / Calcium Pyrophosphate Deposition (CPPD)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR Recommendations on CPPD",
        "source_body": "Annals of the Rheumatic Diseases",
        "citation": "Zhang W et al. European League Against Rheumatism Recommendations for Calcium Pyrophosphate Deposition. Ann Rheum Dis. 2011;70(4):563-570.",
        "doi_or_source": "10.1136/ard.2010.139360",
        "clinical_evidence": "CPPD acute arthritis is caused by rhomboid-shaped, positively birefringent calcium pyrophosphate crystals (differentiating it from needle-shaped urate crystals in gout). Allopurinol is completely ineffective. Intra-articular corticosteroid injection or short-course Colchicine (0.6 mg BID) achieves >85% pain relief within 48 hours.",
        "solution_protocol": {
            "non_pharmacological_targets": "Joint aspiration and intra-articular corticosteroid injection (Triamcinolone 20-40 mg for knee); ice application and joint rest; screen for secondary metabolic causes (hemochromatosis, hyperparathyroidism, hypomagnesemia).",
            "monitoring_cadence": "Assess joint pain and range of motion at 48 hours; check serum iron, calcium, magnesium, and ferritin.",
            "clinical_thresholds": "Synovial fluid analysis showing rhomboid crystals with positive birefringence confirms CPPD."
        },
        "patient_plain_language": "Pseudogout feels almost identical to regular gout—a swollen, red, hot, excruciatingly painful joint (most commonly the knee or wrist). However, instead of uric acid crystals, it is caused by calcium crystals that irritate the joint lining like tiny grains of sharp sand.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the joint fluid test confirm calcium pyrophosphate rhomboid crystals rather than uric acid?",
            "safety_question": "Can we perform an injection of numbing medicine and steroid directly into the swollen knee for quick relief?",
            "action_threshold_question": "Have we checked my blood for high iron (hemochromatosis) or high parathyroid hormone?"
        },
        "red_flags": [
            "High fever with swollen hot joint (mandatory aspiration to rule out septic bacterial arthritis)",
            "Rapid joint destruction with inability to bear weight"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Pseudogout is a painful arthritis caused by calcium pyrophosphate crystal buildup in joints.",
                "plain_analogy": "Sharp grains of calcium sand grating inside the hinges of a door.",
                "lifestyle_action": "Rest the swollen joint, apply ice packs wrapped in towels, and take prescribed anti-inflammatory medicine."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Triamcinolone acetonide intra-articular",
                    "Colchicine (Colcrys)",
                    "Naproxen"
                ],
                "dosing_gdmt": "Intra-articular Triamcinolone 20-40 mg; Colchicine 0.6 mg BID for acute flares.",
                "black_box_warning": "Allopurinol has zero effect on calcium crystals and should not be used for CPPD.",
                "organ_clearance_cutoffs": "Colchicine dose reduction in severe kidney disease."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EULAR-CPPD",
                "pmid_or_doi": "10.1136/ard.2010.139360",
                "cebm_level": 1,
                "sample_size": 1950,
                "endpoints": "Intra-articular steroid injection and colchicine achieve rapid pain relief in >85% of acute CPPD flares."
            }
        }
    },
    {
        "id": "DOC-CARD-348",
        "icd10": "G25.0",
        "condition": "Essential Tremor (Action & Kinetic Tremor)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN Clinical Guideline",
        "source_body": "Neurology",
        "citation": "Zesiewicz TA et al. Evidence-Based Guideline Update: Treatment of Essential Tremor. Neurology. 2011;77(19):1752-1760.",
        "doi_or_source": "10.1212/WNL.0b013e318236f0fd",
        "clinical_evidence": "Propranolol (60-240 mg/day) and Primidone (50-250 mg/day) are Level A first-line therapies, reducing tremor amplitude by 50-70% on objective accelerometry (p<0.001). Unlike Parkinson's disease (resting pill-rolling tremor), essential tremor is an action/kinetic tremor occurring during voluntary movement (drinking, writing). MRI-guided focused ultrasound (MRgFUS) thalamotomy provides >75% tremor reduction in refractory cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Physical and occupational therapy; weighted utensils and heavy pens to dampen tremor amplitude; eliminate caffeine and stimulants; manage performance anxiety.",
            "monitoring_cadence": "Tremor rating scale (FTM TRS) at 3-month follow-up; heart rate and BP for beta-blockers.",
            "clinical_thresholds": "Bilateral action tremor of hands/forearms without resting tremor, rigidity, or bradykinesia confirms diagnosis."
        },
        "patient_plain_language": "Essential tremor is the most common movement disorder. It causes your hands to shake when you try to use them—like holding a cup of coffee, spooning soup, or signing your name. Unlike Parkinson's, your hands are steady when resting in your lap, but start shaking the moment you reach for something.",
        "doctor_consultation_checklist": {
            "parameter_question": "How does my tremor differ from Parkinson's disease?",
            "safety_question": "Would a low-dose beta-blocker (like Propranolol) calm my hand shaking before social meals or writing?",
            "action_threshold_question": "Am I a candidate for weighted utensils or focused ultrasound treatment?"
        },
        "red_flags": [
            "Sudden rapid worsening of tremor with difficulty walking or loss of balance",
            "Development of stiffness, slow movement, or pill-rolling resting tremor (suggesting Parkinson's)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Essential tremor is a nerve disorder that causes involuntary shaking of the hands during action and movement.",
                "plain_analogy": "A microphone picking up gentle acoustic feedback whenever you start to speak.",
                "lifestyle_action": "Use heavier weighted mugs and pens, cut back on coffee and energy drinks, and pace your movements."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Propranolol (Inderal)",
                    "Primidone (Mysoline)",
                    "Topiramate (Topamax)"
                ],
                "dosing_gdmt": "Propranolol long-acting 60-160 mg daily; Primidone started low at 25 mg bedtime and titrated.",
                "black_box_warning": "Propranolol contraindicated in severe asthma, high-grade heart block, or bradycardia.",
                "organ_clearance_cutoffs": "Primidone may cause acute ataxia or sedation upon initiation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAN-TREMOR",
                "pmid_or_doi": "10.1212/WNL.0b013e318236f0fd",
                "cebm_level": 1,
                "sample_size": 2400,
                "endpoints": "Propranolol and Primidone reduce kinetic tremor amplitude by over 55% in randomized controlled trials."
            }
        }
    },
    {
        "id": "DOC-CARD-349",
        "icd10": "F01.50",
        "condition": "Vascular Dementia (Subcortical Ischemic Stepwise Decline)",
        "specialty": "Neurology & Psychiatry",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA Scientific Statement",
        "source_body": "Stroke & Lancet Neurology",
        "citation": "Gorelick PB et al. Vascular Contributions to Cognitive Impairment and Dementia: A Statement for Healthcare Professionals from the AHA/ASA. Stroke. 2011;42(9):2672-2713.",
        "doi_or_source": "10.1161/STR.0b013e3182299496",
        "clinical_evidence": "Aggressive vascular risk factor control (SBP target <130 mmHg, high-intensity statin, antiplatelet therapy) reduces secondary stroke recurrence by 40% and halts stepwise cognitive decline. Donepezil (5-10 mg/day) produces modest cognitive improvement on ADAS-Cog (+1.5 points; p<0.01) in mixed vascular/Alzheimer cohorts.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict blood pressure control (<130/80 mmHg); Mediterranean diet; daily aerobic physical activity (150 min/week); structured cognitive stimulation therapy.",
            "monitoring_cadence": "Montreal Cognitive Assessment (MoCA) every 6 months; annual brain MRI tracking white matter hyperintensities (Fazekas scale).",
            "clinical_thresholds": "Cognitive decline with temporal relationship to stroke or prominent executive dysfunction and neuroimaging evidence of cerebrovascular disease."
        },
        "patient_plain_language": "Vascular dementia happens when microscopic silent strokes or clogged small blood vessels starve brain tissue of oxygen over time. Unlike Alzheimer's where memory fades slowly and smoothly, vascular dementia often progresses in sudden stepwise drops: an abrupt change in problem-solving or walking, followed by stable periods.",
        "doctor_consultation_checklist": {
            "parameter_question": "What does my brain MRI show regarding silent small-vessel strokes and white matter changes?",
            "safety_question": "Are we aggressively controlling my blood pressure and cholesterol to prevent the next step down?",
            "action_threshold_question": "Would a memory medicine (like Donepezil) provide any benefit for my thinking speed?"
        },
        "red_flags": [
            "Sudden focal neurological deficits (weakness, speech slurring) indicating a new acute stroke",
            "Severe swallowing difficulties with aspiration pneumonia risk"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Vascular dementia is cognitive decline caused by impaired blood flow and silent strokes in the brain.",
                "plain_analogy": "A computerized system experiencing stepwise slowdowns as individual circuit wires lose power.",
                "lifestyle_action": "Maintain blood pressure below 130/80, eat a heart-healthy diet, and walk 30 minutes daily."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Atorvastatin 80 mg",
                    "Aspirin 81 mg",
                    "Amlodipine / Lisinopril",
                    "Donepezil"
                ],
                "dosing_gdmt": "Intensive vascular GDMT; Donepezil 5-10 mg daily for mixed pathology.",
                "black_box_warning": "Avoid blood pressure overtreatment causing orthostatic cerebral hypoperfusion in elderly.",
                "organ_clearance_cutoffs": "No specific renal clearance limits for antiplatelets."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHA-VASCOG",
                "pmid_or_doi": "10.1161/STR.0b013e3182299496",
                "cebm_level": 1,
                "sample_size": 5200,
                "endpoints": "Rigorous vascular risk modification slows progressive cognitive deterioration in small-vessel disease."
            }
        }
    },
    {
        "id": "DOC-CARD-350",
        "icd10": "G31.09",
        "condition": "Frontotemporal Dementia (Behavioral Variant FTD / Pick's Disease)",
        "specialty": "Neurology & Psychiatry",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Consensus Criteria & Cochrane",
        "source_body": "Brain & Lancet Neurology",
        "citation": "Rascovsky K et al. Diagnostic Criteria for Behavioral Variant Frontotemporal Dementia (bvFTD). Brain. 2011;134(9):2456-2477.",
        "doi_or_source": "10.1093/brain/awr179",
        "clinical_evidence": "Cholinesterase inhibitors (Donepezil) and Memantine are ineffective and frequently worsen behavioral symptoms in FTD. Low-dose selective serotonin reuptake inhibitors (Trazodone 50-150 mg/day, Sertraline 50-100 mg/day) significantly reduce disinhibition, hyperorality, compulsions, and aggression (p=0.003).",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured non-pharmacological behavioral interventions; simplify daily environments; lock cupboards to manage carbohydrate gorging/hyperorality; legal and financial power of attorney planning early; caregiver support groups.",
            "monitoring_cadence": "Neuropsychiatric Inventory (NPI) and Frontal Behavioral Inventory (FBI) every 3-6 months; brain MRI/PET (frontal/anterior temporal hypometabolism).",
            "clinical_thresholds": "Early behavioral disinhibition, apathy, loss of empathy, hyperorality, and executive deficits with preserved visual-spatial skills."
        },
        "patient_plain_language": "Frontotemporal dementia attacks the frontal lobes of the brain—the centers responsible for manners, empathy, judgment, and self-control. Unlike Alzheimer's, memory stays sharp early on, but the person's personality changes dramatically. They may become tactless, rude, eat massive amounts of sweets, or lose all interest in loved ones.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has a brain MRI or PET scan confirmed shrinkage in the front parts of my loved one's brain?",
            "safety_question": "Why should we avoid standard Alzheimer's memory pills that could make behavioral agitation worse?",
            "action_threshold_question": "What gentle medications (like Trazodone or SSRIs) can help calm compulsive pacing or sweet cravings?"
        },
        "red_flags": [
            "Aggressive or disinhibited behaviors putting patient or family safety at risk",
            "Rapidly progressive swallowing problems or motor neuron weakness (FTD-ALS overlap)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Frontotemporal dementia is a brain disease that primarily changes personality, behavior, and language rather than memory.",
                "plain_analogy": "The brakes and steering wheel of the personality failing while the memory engine keeps running.",
                "lifestyle_action": "Create calm predictable routines, secure food and credit cards, and join dedicated caregiver support networks."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Trazodone (Desyrel)",
                    "Sertraline (Zoloft)",
                    "Quetiapine (low-dose PRN)"
                ],
                "dosing_gdmt": "Trazodone 50-150 mg at bedtime for agitation/sleep; Sertraline 50-100 mg daily for compulsions.",
                "black_box_warning": "Avoid cholinesterase inhibitors (Donepezil/Rivastigmine) which exacerbate agitation in FTD.",
                "organ_clearance_cutoffs": "Caution with antipsychotics due to high extrapyramidal sensitivity in FTD."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "bvFTD-CONSENSUS",
                "pmid_or_doi": "10.1093/brain/awr179",
                "cebm_level": 1,
                "sample_size": 1600,
                "endpoints": "Serotonergic therapy significantly dampens behavioral disinhibition and caregiver distress scores."
            }
        }
    },
    {
        "id": "DOC-CARD-351",
        "icd10": "G91.2",
        "condition": "Normal Pressure Hydrocephalus (NPH)",
        "specialty": "Neurology & Neurosurgery",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Guideline & Dutch NPH Study",
        "source_body": "Neurosurgery & Lancet Neurology",
        "citation": "Marmarou A et al. Development and Validation of the International Guidelines for the Management of Idiopathic Normal Pressure Hydrocephalus. Neurosurgery. 2005;57(3_suppl):S1-S3.",
        "doi_or_source": "10.1227/01.neu.0000168188.25559.0e",
        "clinical_evidence": "Ventriculoperitoneal (VP) shunt placement achieves durable improvement in gait speed and balance in 75-80% of patients with positive high-volume spinal tap (30-50 mL CSF removal producing >=20% gait velocity increase; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "High-volume lumbar puncture (tap test) with quantitative pre- and post-tap timed 10-meter walk and cognitive testing; physical therapy for gait retraining; adjustable programmable shunt valve monitoring.",
            "monitoring_cadence": "Post-shunt clinical assessment at 1, 3, and 12 months; follow-up head CT to assess ventricular caliber.",
            "clinical_thresholds": "Classic triad: magnetic 'glue-footed' gait disturbance, urinary urgency/incontinence, and subcortical dementia ('wet, wacky, and wobbly') with ventriculomegaly disproportionate to sulcal enlargement (Evans index >0.30)."
        },
        "patient_plain_language": "Normal pressure hydrocephalus happens when excess spinal fluid slowly builds up in the deep cavities of your brain. Doctors remember the symptoms as 'wobbly, wet, and wacky': walking with wide, shuffling feet like they are stuck to the floor with glue, bladder urgency or accidents, and mild confusion. In many cases, placing an internal draining tube (shunt) can reverse the walking problems.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were my timed walking test results before and after the spinal fluid tap test?",
            "safety_question": "Does my brain scan show enlarged ventricles out of proportion to brain aging (Evans index >0.30)?",
            "action_threshold_question": "Am I a candidate for a programmable ventriculoperitoneal (VP) shunt surgery?"
        },
        "red_flags": [
            "Sudden headache, vomiting, or lethargy after shunt surgery (over-drainage subdural hematoma)",
            "Redness, swelling, or drainage along the shunt catheter track"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Normal pressure hydrocephalus is fluid buildup in brain cavities causing shuffling walking, urinary accidents, and memory decline.",
                "plain_analogy": "Water accumulating inside a basement drain that gently presses upward on walking and bladder controls.",
                "lifestyle_action": "Walk with a cane or walker to prevent falls, use scheduled bathroom trips, and track walking speed."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ventriculoperitoneal Shunt (Procedural - Definitive)",
                    "Acetazolamide (temporary bridge only)"
                ],
                "dosing_gdmt": "VP shunt with programmable gravitational valve; high-volume tap test 30-50 mL diagnostic.",
                "black_box_warning": "Shunt infection or malfunction requires prompt neurosurgical review.",
                "organ_clearance_cutoffs": "Zero systemic clearance restrictions for shunt."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DUTCH-NPH",
                "pmid_or_doi": "10.1227/01.neu.0000168188.25559.0e",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "VP shunt surgery improves gait velocity and eliminates falls in over 75% of selected NPH patients."
            }
        }
    },
    {
        "id": "DOC-CARD-352",
        "icd10": "E51.2",
        "condition": "Wernicke Encephalopathy (Acute Thiamine Deficiency)",
        "specialty": "Neurology & Emergency Medicine",
        "organ_system": "Nervous & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EFNS Clinical Practice Guideline",
        "source_body": "European Journal of Neurology",
        "citation": "Galvin R et al. EFNS Guidelines for Diagnosis, Prevention, and Treatment of Wernicke Encephalopathy. Eur J Neurol. 2010;17(12):1408-1418.",
        "doi_or_source": "10.1111/j.1468-1331.2010.03153.x",
        "clinical_evidence": "High-dose intravenous Thiamine (vitamin B1: 500 mg IV TID for 3-5 days, then 250 mg daily) initiated immediately before any glucose infusion cures oculomotor palsies within hours and prevents progression to irreversible Korsakoff amnestic syndrome (mortality 20% if untreated).",
        "solution_protocol": {
            "non_pharmacological_targets": "THIAMINE MUST PRECEED GLUCOSE: Infusing intravenous dextrose before thiamine exhausts residual cofactors and precipitates acute brainstem necrosis; treat concurrent hypomagnesemia (magnesium is cofactor for thiamine pyrophosphokinase).",
            "monitoring_cadence": "Continuous neurologic examination tracking nystagmus, ophthalmoplegia, and confusion.",
            "clinical_thresholds": "Classic triad (confusion, ataxia, ophthalmoplegia) is fully present in only 16-33% of patients; presence of any two Caine criteria in high-risk patients (alcohol use, bariatric surgery, hyperemesis) mandates immediate IV thiamine."
        },
        "patient_plain_language": "A severe brain emergency caused by total exhaustion of Vitamin B1 (thiamine)—often in people with chronic alcohol use, severe vomiting, or weight-loss surgery. Brain cells in your memory and balance centers starve of energy. Without immediate high-dose IV vitamin injections, it causes permanent memory loss where you cannot form new memories.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has high-dose intravenous Thiamine (500 mg IV) been started immediately before any sugar water (glucose)?",
            "safety_question": "Are we also giving intravenous magnesium to activate the thiamine vitamin?",
            "action_threshold_question": "Is my eye movement, balance, and orientation improving with the injections?"
        },
        "red_flags": [
            "Rapid progression to coma or circulatory collapse",
            "Persistent profound anterograde amnesia (Korsakoff syndrome)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Wernicke encephalopathy is an acute brain condition caused by thiamine (vitamin B1) deficiency, causing confusion, eye palsies, and unsteadiness.",
                "plain_analogy": "A power grid blackout in brain control centers because a single vital spark plug (thiamine) is missing.",
                "lifestyle_action": "Always take daily multivitamins, eat thiamine-rich foods, and seek emergency help for severe alcohol withdrawal."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Thiamine (Vitamin B1) IV",
                    "Magnesium Sulfate IV"
                ],
                "dosing_gdmt": "Thiamine 500 mg IV infused over 30 min TID for 3 days, followed by 250 mg daily; oral thiamine 100 mg TID maintenance.",
                "black_box_warning": "Never administer intravenous dextrose before thiamine in malnourished patients.",
                "organ_clearance_cutoffs": "Water-soluble vitamin; safe across renal and hepatic ranges."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EFNS-WERNICKE",
                "pmid_or_doi": "10.1111/j.1468-1331.2010.03153.x",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "High-dose parenteral thiamine reverses ocular paralysis in 92% and prevents Korsakoff dementia."
            }
        }
    },
    {
        "id": "DOC-CARD-353",
        "icd10": "K72.90",
        "condition": "Hepatic Encephalopathy (Hyperammonemia & Asterixis)",
        "specialty": "Gastroenterology & Hepatology",
        "organ_system": "Digestive & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD/EASL Practice Guideline",
        "source_body": "Hepatology",
        "citation": "Vilstrup H et al. Hepatic Encephalopathy in Chronic Liver Disease: 2014 Practice Guideline by AASLD and EASL. Hepatology. 2014;60(2):715-735.",
        "doi_or_source": "10.1002/hep.27210",
        "clinical_evidence": "Lactulose titrated to produce 2-3 soft bowel movements daily reduces blood ammonia and resolves encephalopathy in 80% of episodes. Adding Rifaximin (550 mg BID) to lactulose reduces recurrent hepatic encephalopathy hospitalizations by 58% (HR 0.42; 95% CI 0.28-0.64; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Maintain adequate protein intake (1.2-1.5 g/kg/day - protein restriction is harmful and accelerates sarcopenia); identify and treat precipitants (GI bleeding, infection/SBP, constipation, dehydration, sedatives).",
            "monitoring_cadence": "West Haven Criteria scoring for mental status; flapping tremor (asterixis) checks; serum ammonia has poor correlation with clinical severity and should not be used for serial monitoring.",
            "clinical_thresholds": "Grade 1 (mild confusion, sleep reversal) to Grade 4 (coma) on West Haven scale."
        },
        "patient_plain_language": "When the liver is severely scarred (cirrhosis), it cannot filter out normal toxins like ammonia produced by intestinal bacteria. The ammonia bypasses the liver and enters the brain, causing sluggish thinking, day-night sleep reversal, hand-flapping tremors (asterixis), and confusion.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many bowel movements am I having each day on my Lactulose medicine (target is 2 to 3 soft stools)?",
            "safety_question": "Should we add Rifaximin (an antibiotic pill that stays in the gut) to stop future hospital visits?",
            "action_threshold_question": "Have we checked for hidden infections, bleeding, or constipation that triggered this episode?"
        },
        "red_flags": [
            "Profound lethargy, inability to stay awake, or coma (Grade 3/4 Hepatic Encephalopathy)",
            "Vomiting blood or black tarry stools (variceal bleeding triggering ammonia spike)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hepatic encephalopathy is brain confusion caused by toxin buildup when the liver is failing.",
                "plain_analogy": "A water purification plant shutting down, allowing murky waste to reach the drinking taps.",
                "lifestyle_action": "Take Lactulose every day to ensure 2-3 soft stools, never skip meals, and avoid sleeping pills."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lactulose syrup",
                    "Rifaximin (Xifaxan)",
                    "Polyethylene Glycol (Miralax)"
                ],
                "dosing_gdmt": "Lactulose 20-30 g (30-45 mL) orally 2-4 times daily; Rifaximin 550 mg orally BID.",
                "black_box_warning": "Avoid sedatives, narcotics, and benzodiazepines which can precipitate coma.",
                "organ_clearance_cutoffs": "Lactulose and Rifaximin act locally in gut with negligible systemic clearance."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-HE",
                "pmid_or_doi": "10.1002/hep.27210",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "Lactulose plus Rifaximin combination slashes recurrent hepatic encephalopathy hospital admissions by 58%."
            }
        }
    },
    {
        "id": "DOC-CARD-354",
        "icd10": "F05",
        "condition": "Delirium (Acute Brain Failure / Toxic-Metabolic Encephalopathy)",
        "specialty": "Geriatrics & Critical Care",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AGS Clinical Practice Guideline",
        "source_body": "Journal of the American Geriatrics Society",
        "citation": "American Geriatrics Society. Clinical Practice Guideline for Postoperative Delirium in Older Adults. J Am Geriatr Soc. 2015;63(1):142-150.",
        "doi_or_source": "10.1111/jgs.13281",
        "clinical_evidence": "Multicomponent non-pharmacological interventions (Hospital Elder Life Program [HELP]: early mobilization, sleep hygiene, orientation clocks, hearing/vision aids, hydration) reduce delirium incidence by 44% (RR 0.56; p<0.001). Antipsychotics do NOT prevent or shorten delirium duration and are reserved strictly for severe dangerous agitation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Frequent reorientation (whiteboards, clocks, family presence); ensure glasses and hearing aids are in place; avoid physical restraints and urinary catheters; avoid anticholinergics, benzodiazepines, and diphenhydramine (Beers Criteria).",
            "monitoring_cadence": "Confusion Assessment Method (CAM or CAM-ICU) twice daily; monitor sleep-wake cycle.",
            "clinical_thresholds": "Acute onset and fluctuating course + inattention + either disorganized thinking or altered level of consciousness."
        },
        "patient_plain_language": "Delirium is sudden, temporary brain confusion caused by an underlying medical sickness (like a urinary infection, dehydration, pneumonia, or medication side effect). Unlike Alzheimer's, which develops over years, delirium strikes within hours or days, making the person confused, seeing things, or unusually sleepy.",
        "doctor_consultation_checklist": {
            "parameter_question": "What medical trigger (infection, medication, or dehydration) caused this sudden confusion?",
            "safety_question": "Are we avoiding sleeping pills and bladder catheters that make delirium worse?",
            "action_threshold_question": "How can family members stay at the bedside to help reorient and comfort the patient?"
        },
        "red_flags": [
            "Severe agitation attempting to pull out life-support lines or fall risk",
            "Hypoactive delirium with total lethargy and refusal to eat or drink"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Delirium is a sudden state of mental confusion and fluctuating attention caused by acute medical illness.",
                "plain_analogy": "A computer freezing and glitching because the electrical cord is loose or the room is overheating.",
                "lifestyle_action": "Keep natural daylight in the room, wear hearing aids and glasses, and have familiar family visit."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Non-pharmacological protocols (First Line)",
                    "Haloperidol (lowest dose only for severe threat)",
                    "Quetiapine"
                ],
                "dosing_gdmt": "HELP protocol; Haloperidol 0.25-0.5 mg IV/oral only if patient is a danger to self or others.",
                "black_box_warning": "Antipsychotics increase mortality in elderly dementia patients; use only as last resort.",
                "organ_clearance_cutoffs": "Avoid diphenhydramine and benzodiazepines."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AGS-DELIRIUM",
                "pmid_or_doi": "10.1111/jgs.13281",
                "cebm_level": 1,
                "sample_size": 4200,
                "endpoints": "Multicomponent non-drug interventions reduce hospital delirium episodes by 44% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-355",
        "icd10": "G37.2",
        "condition": "Central Pontine Myelinolysis (Osmotic Demyelination Syndrome)",
        "specialty": "Neurology & Nephrology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & Clinical Guideline",
        "source_body": "Lancet Neurology",
        "citation": "Sterns RH et al. Disorders of Plasma Sodium: Causes, Consequences, and Correction. Lancet. 2013;382(9897):1064-1075.",
        "doi_or_source": "10.1016/S0140-6736(13)61239-0",
        "clinical_evidence": "Strict limitation of sodium correction rates (<=8 mEq/L per 24 hours, or <=4-6 mEq/L in high-risk patients with malnutrition or liver disease) prevents osmotic demyelination. If overcorrection occurs, prompt re-lowering with D5W or Desmopressin stops myelinolysis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Calculate maximum allowable sodium rise per 24 hours; if sodium rises >8 mEq/L in first 24h, immediately administer IV 5% Dextrose in water (D5W) and Desmopressin (DDAVP 2 mcg IV) to halt brainstem osmotic shrinkage.",
            "monitoring_cadence": "Serum sodium every 2-4 hours during active correction; serial neurologic examination for pseudobulbar palsy.",
            "clinical_thresholds": "Delayed onset (2-6 days after rapid correction) of spastic quadriparesis, pseudobulbar palsy, and 'locked-in' syndrome."
        },
        "patient_plain_language": "A severe, preventable brainstem injury that happens when doctors or nurses raise very low blood sodium levels too quickly. Brain cells that adapted to low salt suddenly have water sucked out of them by high salt outside, causing the protective insulation around brainstem wires to dissolve.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are we checking my blood sodium every 2 to 4 hours to make sure it does not rise faster than 6 to 8 points a day?",
            "safety_question": "If my sodium is rising too fast, are we giving sugar-water or Desmopressin to slow it down?",
            "action_threshold_question": "Why must chronic low sodium be corrected very slowly over several days?"
        },
        "red_flags": [
            "Difficulty speaking, swallowing, or moving arms several days after sodium treatment (Locked-In Syndrome)",
            "Rapid spastic weakness in both legs"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Osmotic demyelination is brainstem nerve damage caused by correcting low blood sodium too rapidly.",
                "plain_analogy": "A sponge being dried out so violently with a hairdryer that its structure cracks and crumbles.",
                "lifestyle_action": "Ensure hospital medical teams monitor sodium hourly when correcting severe hyponatremia."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Dextrose 5% in Water IV (D5W)",
                    "Desmopressin (DDAVP) IV"
                ],
                "dosing_gdmt": "D5W infusion 3-5 mL/kg/h + Desmopressin 1-2 mcg IV to re-lower sodium if overcorrected.",
                "black_box_warning": "Never allow sodium to rise >8 mEq/L in 24 hours.",
                "organ_clearance_cutoffs": "Strict protocolized monitoring in ICU."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ODS-SAFETY",
                "pmid_or_doi": "10.1016/S0140-6736(13)61239-0",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Strict sodium correction ceilings (<=8 mEq/L/day) reduce osmotic demyelination incidence to <0.05%."
            }
        }
    },
    {
        "id": "DOC-CARD-356",
        "icd10": "G23.2",
        "condition": "Multiple System Atrophy (MSA / Shy-Drager Syndrome)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Movement Disorder Society Consensus",
        "source_body": "Movement Disorders",
        "citation": "Poewe W et al. Multiple System Atrophy: A Progress Report. Mov Disord. 2022;37(4):699-712.",
        "doi_or_source": "10.1002/mds.28985",
        "clinical_evidence": "Multiple system atrophy is an aggressive alpha-synucleinopathy combining profound autonomic failure (orthostatic hypotension, urinary incontinence) with parkinsonism (MSA-P) or cerebellar ataxia (MSA-C). Unlike Parkinson's, levodopa response is poor or transient. Fludrocortisone, Midodrine, and Droxidopa manage disabling orthostasis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Waist-high compression stockings (30-40 mmHg); elevate head of bed 30-45 degrees; high fluid (2.5 L) and salt (6-10 g) intake; speech therapy for stridor and dysphagia screening.",
            "monitoring_cadence": "Unified MSA Rating Scale (UMSARS) every 3-6 months; standing and supine BP log; nocturnal polysomnography for laryngeal stridor.",
            "clinical_thresholds": "Severe autonomic failure + poorly levodopa-responsive parkinsonism or cerebellar ataxia confirms probable MSA."
        },
        "patient_plain_language": "Multiple system atrophy is a rare, aggressive nerve disorder that attacks both your movement controls and your body's automatic systems. It causes Parkinson's-like stiffness and balance loss along with severe drops in blood pressure when standing, bladder accidents, and breathing noises during sleep.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my poor response to Sinemet (Levodopa) suggest MSA rather than regular Parkinson's?",
            "safety_question": "What medications (like Midodrine or Droxidopa) will keep my blood pressure up when I stand?",
            "action_threshold_question": "Should we check for laryngeal stridor (throat whistling during sleep)?"
        },
        "red_flags": [
            "High-pitched harsh breathing sound during sleep (laryngeal stridor - requires prompt CPAP or tracheostomy evaluation)",
            "Recurrent falls from severe orthostatic blood pressure drops"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Multiple system atrophy is a progressive brain disorder affecting movement, balance, and automatic functions like blood pressure and bladder.",
                "plain_analogy": "An engine losing both its transmission gear control and its automatic electrical cooling fan simultaneously.",
                "lifestyle_action": "Wear waist-high compression tights, drink water before rising, and use a wheelchair or walker for safety."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Droxidopa (Northera)",
                    "Midodrine hydrochloride",
                    "Fludrocortisone",
                    "Levodopa/Carbidopa (trial)"
                ],
                "dosing_gdmt": "Droxidopa 100-600 mg TID; Midodrine 2.5-10 mg TID; Fludrocortisone 0.1-0.2 mg daily.",
                "black_box_warning": "Midodrine/Droxidopa: Supine hypertension risk; take last dose 4 hours before lying down.",
                "organ_clearance_cutoffs": "Titrate based on standing blood pressure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MDS-MSA",
                "pmid_or_doi": "10.1002/mds.28985",
                "cebm_level": 1,
                "sample_size": 1900,
                "endpoints": "Targeted autonomic vasoactive therapy improves standing time and reduces syncope in >70% of MSA patients."
            }
        }
    },
    {
        "id": "DOC-CARD-357",
        "icd10": "G23.1",
        "condition": "Progressive Supranuclear Palsy (Steele-Richardson-Olszewski)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Movement Disorder Society Criteria",
        "source_body": "Movement Disorders",
        "citation": "Hoglinger GU et al. Clinical Diagnosis of Progressive Supranuclear Palsy: The MDS Criteria. Mov Disord. 2017;32(6):853-864.",
        "doi_or_source": "10.1002/mds.26987",
        "clinical_evidence": "PSP is a 4-repeat tauopathy characterized by vertical supranuclear gaze palsy (inability to look down), axial rigidity, early unexplained backward falls, and fronto-executive cognitive slowing. Levodopa response is minimal. Physical therapy targeting backward stability and prism glasses improve functional mobility.",
        "solution_protocol": {
            "non_pharmacological_targets": "Fall prevention: weighted walker (U-Step walker) and home safety modifications; speech therapy for severe dysarthria and dysphagia; prism glasses to compensate for vertical gaze palsy.",
            "monitoring_cadence": "PSP Rating Scale (PSPRS) every 6 months; formal swallowing evaluation to prevent aspiration pneumonia.",
            "clinical_thresholds": "Vertical supranuclear gaze palsy (downward worse than upward) + prominent postural instability with backward falls within first 3 years."
        },
        "patient_plain_language": "Progressive supranuclear palsy is an aggressive Parkinson's-like condition. The hallmark signs are an inability to look down (vertical eye palsy) and sudden backward falls as if someone shoved you from behind. Patients have a wide-eyed, unblinking facial expression and speech becomes muffled and slurred.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my eye exam confirm that I cannot easily look down toward my feet?",
            "safety_question": "Why do standard Parkinson's medications not work as well for my symptoms?",
            "action_threshold_question": "What weighted walker and swallowing exercises will prevent falls and choking?"
        },
        "red_flags": [
            "Frequent unexplained backward falls causing head trauma or hip fractures",
            "Severe coughing or choking while eating (aspiration pneumonia risk)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Progressive supranuclear palsy causes severe balance problems, frequent backward falls, and difficulty moving eyes up and down.",
                "plain_analogy": "A ship whose downward periscope is stuck and whose balance ballast is tipping backward.",
                "lifestyle_action": "Use a specialized weighted walker, install grab bars throughout the home, and eat thickened soft foods."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Levodopa/Carbidopa (limited benefit)",
                    "Amantadine",
                    "Coenzyme Q10"
                ],
                "dosing_gdmt": "Levodopa trial up to 1000 mg/day (taper if no benefit within 2 months); Amantadine 100 mg BID.",
                "black_box_warning": "Antipsychotics worsen rigidity and should be avoided.",
                "organ_clearance_cutoffs": "Dose reduction in renal impairment for amantadine."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MDS-PSP",
                "pmid_or_doi": "10.1002/mds.26987",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "MDS diagnostic criteria achieve 88% sensitivity and 96% specificity in differentiating PSP from Parkinson's."
            }
        }
    },
    {
        "id": "DOC-CARD-358",
        "icd10": "G31.83",
        "condition": "Dementia with Lewy Bodies (DLB)",
        "specialty": "Neurology & Psychiatry",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: DLB Consortium Consensus",
        "source_body": "Neurology",
        "citation": "McKeith IG et al. Diagnosis and Management of Dementia with Lewy Bodies: Fourth Consensus Report of the DLB Consortium. Neurology. 2017;89(1):88-100.",
        "doi_or_source": "10.1212/WNL.0000000000004058",
        "clinical_evidence": "Cholinesterase inhibitors (Donepezil 5-10 mg, Rivastigmine patch 9.5-13.3 mg/24h) significantly improve cognition, visual hallucinations, and apathy in DLB. FIRST-GENERATION ANTIPSYCHOTICS (HALOPERIDOL) ARE BLACK-BOX CONTRAINDICATED due to severe life-threatening neuroleptic sensitivity (precipitating irreversible parkinsonism and death in >50%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Consistent daily routines; low lighting management to reduce visual misperceptions/hallucinations; safe sleep environment for REM sleep behavior disorder (dream enactment with punching/kicking); physical therapy for Parkinsonian gait.",
            "monitoring_cadence": "Mini-Mental State Examination (MMSE) and neuropsychiatric inventory every 3-6 months; dopamine transporter (DaT) SPECT imaging.",
            "clinical_thresholds": "Core features: fluctuating cognition with pronounced variations in attention, recurrent well-formed visual hallucinations, REM sleep behavior disorder, and spontaneous parkinsonism."
        },
        "patient_plain_language": "Lewy body dementia is the second most common form of progressive dementia. It combines memory changes with vivid visual hallucinations (seeing small animals, people, or children that are not there), fluctuating alertness from hour to hour, acting out dreams while asleep, and Parkinson's-like slow walking.",
        "doctor_consultation_checklist": {
            "parameter_question": "Why must my doctor NEVER give me standard antipsychotic medicines like Haloperidol?",
            "safety_question": "Will a memory patch (Rivastigmine) help calm my vivid visual hallucinations?",
            "action_threshold_question": "Does acting out my dreams at night confirm Lewy body dementia?"
        },
        "red_flags": [
            "Severe neuroleptic sensitivity reaction (acute rigidity, immobility, and fever after receiving an antipsychotic drug)",
            "Severe falls from fluctuating balance and orthostatic blood pressure drops"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dementia with Lewy bodies causes memory loss combined with visual hallucinations, fluctuating alertness, and walking stiffness.",
                "plain_analogy": "A movie projector with a flickering bulb and double exposures showing images that are not there.",
                "lifestyle_action": "Keep nightlights on to reduce visual illusions, cushion the bed area, and avoid standard sedative pills."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rivastigmine transdermal patch (Exelon)",
                    "Donepezil (Aricept)",
                    "Melatonin / Clonazepam for RBD"
                ],
                "dosing_gdmt": "Rivastigmine 4.6 mg/24h patch titrated to 9.5-13.3 mg/24h; Melatonin 3-10 mg at bedtime for dream enactment.",
                "black_box_warning": "First-generation antipsychotics are strictly contraindicated (severe neuroleptic sensitivity reaction).",
                "organ_clearance_cutoffs": "Rivastigmine patch bypasses hepatic first-pass metabolism."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DLB-CONSORTIUM",
                "pmid_or_doi": "10.1212/WNL.0000000000004058",
                "cebm_level": 1,
                "sample_size": 2900,
                "endpoints": "Cholinesterase inhibitors improve cognitive fluctuation and visual hallucinations in >70% of DLB patients."
            }
        }
    },
    {
        "id": "DOC-CARD-359",
        "icd10": "G40.209",
        "condition": "Temporal Lobe Epilepsy (Focal Impaired Awareness Seizures)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ILAE Guidelines & Cochrane Review",
        "source_body": "Epilepsia & Lancet",
        "citation": "Kwan P et al. Definition of Drug-Resistant Epilepsy: Consensus Proposal by the ILAE. Epilepsia. 2010;51(6):1069-1077.",
        "doi_or_source": "10.1111/j.1528-1167.2009.02397.x",
        "clinical_evidence": "Second-generation antiseizure medications (Lamotrigine 100-200 mg BID, Levetiracetam 500-1500 mg BID, Lacosamide 100-200 mg BID) achieve seizure freedom in 65% of patients. In drug-resistant mesial temporal lobe epilepsy with hippocampal sclerosis, anterior temporal lobectomy achieves seizure freedom in 58% vs 8% medical therapy (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Maintain strict sleep hygiene (sleep deprivation is a primary seizure trigger); driving restrictions per state law until 6-12 months seizure-free; avoid alcohol; seizure safety counseling (shower instead of bath).",
            "monitoring_cadence": "Routine and sleep-deprived EEG; high-resolution 3T epilepsy-protocol MRI brain; therapeutic drug monitoring.",
            "clinical_thresholds": "Focal seizures preceded by an epigastric rising aura, dejavu, lip-smacking automatisms, and post-ictal confusion."
        },
        "patient_plain_language": "Temporal lobe epilepsy causes focal seizures that start in your brain's memory and emotion center. They often begin with an 'aura'—a rising butterfly feeling in the stomach, an intense feeling of dejavu, or smelling phantom burnt toast—followed by staring blankly, lip-smacking, and confusion.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my 3-Tesla brain MRI show any scarring in my hippocampus (hippocampal sclerosis)?",
            "safety_question": "Which seizure medication has the lowest risk of tiredness or mood changes for me?",
            "action_threshold_question": "If medications do not stop my staring spells, am I a candidate for epilepsy surgery?"
        },
        "red_flags": [
            "Seizures lasting >5 minutes or multiple seizures without regaining consciousness (Status Epilepticus - Call 911)",
            "Head injury or submersion injury during seizure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Temporal lobe epilepsy causes focal seizures with strange stomach sensations, dejavu, and staring spells.",
                "plain_analogy": "A short-circuit glitch in the hard drive of the brain's memory filing cabinet.",
                "lifestyle_action": "Take your seizure pill at the exact same times every day, get 8 hours of sleep, and shower instead of taking baths."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lamotrigine (Lamictal)",
                    "Levetiracetam (Keppra)",
                    "Lacosamide (Vimpat)"
                ],
                "dosing_gdmt": "Lamotrigine titrated slowly over 6 weeks to 100-200 mg BID; Levetiracetam 500-1500 mg BID.",
                "black_box_warning": "Lamotrigine: Severe life-threatening rash (Stevens-Johnson syndrome) with fast titration.",
                "organ_clearance_cutoffs": "Dose reduction in renal impairment for Levetiracetam and Lacosamide."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ILAE-EPILEPSY",
                "pmid_or_doi": "10.1111/j.1528-1167.2009.02397.x",
                "cebm_level": 1,
                "sample_size": 4100,
                "endpoints": "Epilepsy surgery achieves seizure freedom in 58% of drug-resistant temporal lobe epilepsy compared to 8% medication alone."
            }
        }
    },
    {
        "id": "DOC-CARD-360",
        "icd10": "G40.901",
        "condition": "Convulsive Status Epilepticus (Prolonged Seizure Emergency)",
        "specialty": "Neurology & Emergency Medicine",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AES Guideline & ESETT Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "Kapur J et al. Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus (ESETT). N Engl J Med. 2019;381(22):2103-2113.",
        "doi_or_source": "10.1056/NEJMoa1905795",
        "clinical_evidence": "The landmark ESETT randomized multicenter trial (n=384 patients) proved that Levetiracetam (60 mg/kg), Fosphenytoin (20 mg PE/kg), and Valproate (40 mg/kg) IV had equal efficacy (approximately 47% seizure cessation within 60 min; p=0.71) as second-line therapy following initial IV Lorazepam (0.1 mg/kg) in benzodiazepine-refractory status epilepticus.",
        "solution_protocol": {
            "non_pharmacological_targets": "Time is brain: initiate therapy at 5 minutes; Phase 1 (0-5 min): airway, oxygen, fingerstick glucose; Phase 2 (5-20 min): IV Lorazepam 4 mg or IM Midazolam 10 mg; Phase 3 (20-40 min): IV Levetiracetam or Fosphenytoin; Phase 4 (>40 min): general anesthesia intubation with Propofol/Midazolam.",
            "monitoring_cadence": "Continuous EEG monitoring to detect non-convulsive status epilepticus; arterial blood gas; serial CK and troponin.",
            "clinical_thresholds": "Continuous convulsive seizure activity lasting >=5 minutes, or >=2 distinct seizures without full recovery of consciousness."
        },
        "patient_plain_language": "Status epilepticus is a life-threatening medical emergency where a continuous convulsive seizure lasts for more than 5 minutes, or multiple seizures occur back-to-back without waking up. The brain's electrical storm will not stop on its own, risking permanent brain damage, hyperthermia, and heart failure.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has a full emergency dose of IV Ativan (Lorazepam) or IM Midazolam been given immediately?",
            "safety_question": "Which second-line intravenous seizure medication (Keppra, Fosphenytoin, or Depakote) is being infused right now?",
            "action_threshold_question": "Are we preparing for continuous brain wave (EEG) monitoring in the intensive care unit?"
        },
        "red_flags": [
            "Seizure activity exceeding 5 minutes duration (Immediate Emergency Medical Services / 911)",
            "Severe hypoxemia, aspiration, or severe metabolic lactic acidosis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Status epilepticus is a prolonged continuous seizure lasting over 5 minutes that requires emergency hospital intervention.",
                "plain_analogy": "An electrical short-circuit that sets the whole electrical grid on fire and cannot trip its circuit breaker.",
                "lifestyle_action": "Anyone having an active seizure lasting >3-5 minutes must be given emergency nasal/rectal medicine and 911 called immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lorazepam IV (Ativan)",
                    "Midazolam IM/intranasal",
                    "Levetiracetam IV (Keppra)",
                    "Fosphenytoin IV"
                ],
                "dosing_gdmt": "Lorazepam 0.1 mg/kg (up to 4 mg) IV push; if no IV, Midazolam 10 mg IM; followed by Levetiracetam 60 mg/kg IV.",
                "black_box_warning": "Propylene glycol toxicity with high-dose lorazepam infusions; monitor gap acidosis.",
                "organ_clearance_cutoffs": "Rapid fosphenytoin infusion causes hypotension and arrhythmias; max rate 150 mg PE/min."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESETT",
                "pmid_or_doi": "10.1056/NEJMoa1905795",
                "cebm_level": 2,
                "sample_size": 384,
                "endpoints": "Early benzodiazepine followed by second-line IV anticonvulsant stops refractory status epilepticus in >47% within 60 minutes."
            }
        }
    }
]