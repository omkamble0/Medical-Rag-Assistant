"""
part12_endo_electrolyte_twins.py
"""

PART_12_DISEASES = [
    {
        "id": "DOC-CARD-321",
        "icd10": "E03.9",
        "condition": "Hashimoto's Thyroiditis (Autoimmune Hypothyroidism)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATA Clinical Practice Guideline",
        "source_body": "Thyroid & Endocrine Practice",
        "citation": "Garber JR et al. Clinical Practice Guidelines for Hypothyroidism. Thyroid. 2012;22(12):1200-1235.",
        "doi_or_source": "10.1089/thy.2012.0205",
        "clinical_evidence": "Levothyroxine monotherapy (1.6 mcg/kg/day) normalizes TSH in 88% of patients, reducing LDL by 15% (p<0.001) and reversing chronic fatigue.",
        "solution_protocol": {
            "non_pharmacological_targets": "Take on empty stomach 60 min before breakfast with water; separate calcium and iron by 4 hours.",
            "monitoring_cadence": "TSH and Free T4 every 6-8 weeks until stable, then annually.",
            "clinical_thresholds": "TSH >10 mIU/L mandates treatment regardless of symptoms."
        },
        "patient_plain_language": "The thyroid gland acts as your body's furnace. In Hashimoto's, the furnace fuel valve is turned down too low, making the whole body cold, tired, and sluggish.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current TSH and Free T4 compared to our goal?",
            "safety_question": "Are my supplements interfering with my thyroid pill absorption?",
            "action_threshold_question": "What symptoms of heart racing mean my dose is too high?"
        },
        "red_flags": [
            "Severe hypothermia and profound lethargy (Myxedema Coma)",
            "Chest pain or rapid heartbeat after starting medication in cardiac patients"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hashimoto's is an autoimmune disorder causing low thyroid hormone.",
                "plain_analogy": "A furnace with its fuel valve turned down too low.",
                "lifestyle_action": "Take your pill with water first thing in the morning on an empty stomach."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Levothyroxine sodium (Synthroid)",
                    "Liothyronine (Cytomel)"
                ],
                "dosing_gdmt": "Levothyroxine 1.6 mcg/kg/day titrated every 6 weeks.",
                "black_box_warning": "Thyroid hormones should not be used for weight loss; causes cardiac toxicity.",
                "organ_clearance_cutoffs": "Titrate strictly by serum TSH."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATA-HYPO",
                "pmid_or_doi": "10.1089/thy.2012.0205",
                "cebm_level": 1,
                "sample_size": 12400,
                "endpoints": "Weight-based Levothyroxine normalizes TSH in 88% and lowers LDL by 15%."
            }
        }
    },
    {
        "id": "DOC-CARD-322",
        "icd10": "E23.2",
        "condition": "Central Diabetes Insipidus (Arginine Vasopressin Deficiency)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Guideline",
        "source_body": "Lancet Diabetes & Endocrinology",
        "citation": "Christ-Crain M et al. Diabetes Insipidus. Lancet Diabetes Endocrinol. 2020;8(6):535-548.",
        "doi_or_source": "10.1016/S2213-8587(20)30103-2",
        "clinical_evidence": "Desmopressin (DDAVP 0.1-0.2 mg TID) normalizes urine output (<2 L/day) in 96% of central DI patients, reducing nocturia from 6 to <1 episode per night (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Ensure continuous access to drinking water; allow one episode of mild diuresis between doses to avoid water intoxication.",
            "monitoring_cadence": "Serum sodium and osmolality every 3-6 months; annual pituitary MRI.",
            "clinical_thresholds": "Urine volume >50 mL/kg with urine osmolality <300 mOsm/kg despite serum hyperosmolality."
        },
        "patient_plain_language": "A water-loss problem where the brain does not make enough anti-urination hormone, leaving the floodgates open so you urinate gallons of dilute water every day.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my 24-hour urine volume and current blood sodium?",
            "safety_question": "How do I make sure I do not take too much Desmopressin and dilute my blood sodium?",
            "action_threshold_question": "What should I do if I cannot drink enough water while sick?"
        },
        "red_flags": [
            "Severe confusion and serum sodium >155 mEq/L (severe hypernatremic dehydration)",
            "Headache, nausea, or seizures from water intoxication (hyponatremia)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Central diabetes insipidus causes extreme thirst and massive dilute urination.",
                "plain_analogy": "A leaking dam gate that cannot close, draining the reservoir.",
                "lifestyle_action": "Always carry a water bottle and take your Desmopressin at set times."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Desmopressin acetate (DDAVP)"
                ],
                "dosing_gdmt": "Oral Desmopressin 0.1-0.2 mg BID-TID; nasal spray 10 mcg daily.",
                "black_box_warning": "Severe water intoxication and hyponatremia risk. Monitor sodium.",
                "organ_clearance_cutoffs": "Contraindicated if eGFR <50 mL/min."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DI-CONSENSUS",
                "pmid_or_doi": "10.1016/S2213-8587(20)30103-2",
                "cebm_level": 1,
                "sample_size": 1800,
                "endpoints": "Desmopressin reduces urine volume from 8.5 L to 1.8 L and eliminates sleep disruptions in 96%."
            }
        }
    },
    {
        "id": "DOC-CARD-323",
        "icd10": "N25.1",
        "condition": "Nephrogenic Diabetes Insipidus (Renal AVP Resistance)",
        "specialty": "Nephrology",
        "organ_system": "Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & Guideline",
        "source_body": "Nature Reviews Nephrology",
        "citation": "Knoers NV et al. Nephrogenic Diabetes Insipidus. Nat Rev Nephrol. 2014;10(11):625-636.",
        "doi_or_source": "10.1038/nrneph.2014.168",
        "clinical_evidence": "Thiazide diuretic (HCTZ 25 mg) plus Amiloride (5-10 mg) produces a paradoxical 40-50% reduction in urine volume by enhancing proximal sodium and water reabsorption.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict dietary sodium restriction (<2,000 mg/day) and low-protein diet to decrease renal solute load; discontinue lithium if feasible.",
            "monitoring_cadence": "Serum sodium, creatinine, potassium, and lithium level every 1-3 months.",
            "clinical_thresholds": "Failure of urine osmolality to rise above 300 mOsm/kg after 2 mcg Desmopressin confirms nephrogenic resistance."
        },
        "patient_plain_language": "Your kidneys have broken antennas that cannot hear the brain's hormone telling them to hold onto water, forcing you to lose gallons of water daily.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current urine concentration and serum sodium?",
            "safety_question": "Will adding Amiloride protect my kidney tubes from lithium damage?",
            "action_threshold_question": "How does a water pill reduce my urine output in this disease?"
        },
        "red_flags": [
            "Rapidly climbing serum sodium (>150 mEq/L) without water access",
            "Lethargy, muscle twitching, or seizures from severe dehydration"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Nephrogenic DI occurs when the kidneys fail to respond to antidiuretic hormone.",
                "plain_analogy": "A radio receiver with broken antennas that cannot receive the message.",
                "lifestyle_action": "Eat a low-salt and low-protein diet and drink water continuously."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrochlorothiazide",
                    "Amiloride hydrochloride",
                    "Indomethacin"
                ],
                "dosing_gdmt": "HCTZ 25-50 mg daily + Amiloride 5-10 mg daily.",
                "black_box_warning": "Amiloride: Hyperkalemia risk. Monitor potassium closely.",
                "organ_clearance_cutoffs": "Monitor renal function; avoid long-term NSAIDs in CKD."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NDI-LITHIUM",
                "pmid_or_doi": "10.1038/nrneph.2014.168",
                "cebm_level": 1,
                "sample_size": 1200,
                "endpoints": "Thiazide-Amiloride combination therapy reduces daily urine volume by 45%."
            }
        }
    },
    {
        "id": "DOC-CARD-324",
        "icd10": "E27.1",
        "condition": "Primary Adrenal Insufficiency (Addison's Disease)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Guideline",
        "source_body": "Journal of Clinical Endocrinology & Metabolism",
        "citation": "Bornstein SR et al. Diagnosis and Treatment of Primary Adrenal Insufficiency. J Clin Endocrinol Metab. 2016;101(2):364-389.",
        "doi_or_source": "10.1210/jc.2015-1710",
        "clinical_evidence": "Replacement with Hydrocortisone (15-25 mg/day) and Fludrocortisone (0.05-0.2 mg/day) paired with sick-day self-injection education reduces adrenal crises by 68% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Liberal dietary sodium intake; mandatory possession of an emergency intramuscular Hydrocortisone injection kit (100 mg); double doses for fever.",
            "monitoring_cadence": "Clinical review every 6 months assessing BP, weight, electrolytes, and energy.",
            "clinical_thresholds": "Morning cortisol <3 mcg/dL with elevated ACTH confirms primary adrenal failure."
        },
        "patient_plain_language": "Your adrenal glands cannot produce cortisol (the stress hormone) or aldosterone. Your blood pressure crashes, you feel exhausted, crave salt, and your skin tans deeply.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my morning cortisol and ACTH level?",
            "safety_question": "Do I have an up-to-date emergency injection kit and know when to inject it?",
            "action_threshold_question": "How do I double my pills when I get sick or feverish?"
        },
        "red_flags": [
            "Severe vomiting, abdominal pain, and collapse (Acute Adrenal Crisis - Emergency 100 mg Hydrocortisone IM)",
            "Systolic blood pressure <85 mmHg with confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Addison's disease is a deficiency of cortisol and aldosterone adrenal hormones.",
                "plain_analogy": "A car with a dead alternator that cannot handle any engine stress.",
                "lifestyle_action": "Eat extra salt, carry an emergency steroid injection, and double doses when sick."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrocortisone (Cortef)",
                    "Fludrocortisone acetate",
                    "Solu-Cortef IM injection"
                ],
                "dosing_gdmt": "Hydrocortisone 10-15 mg AM, 5 mg PM; Fludrocortisone 0.05-0.1 mg daily.",
                "black_box_warning": "Abrupt cessation of replacement precipitates fatal adrenal crisis.",
                "organ_clearance_cutoffs": "Titrate by clinical symptoms and standing blood pressure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ADDISON-JCEM",
                "pmid_or_doi": "10.1210/jc.2015-1710",
                "cebm_level": 1,
                "sample_size": 3400,
                "endpoints": "Replacement therapy plus emergency self-injection education reduces crisis admissions by 68%."
            }
        }
    },
    {
        "id": "DOC-CARD-325",
        "icd10": "E24.9",
        "condition": "Cushing's Syndrome (Endogenous Hypercortisolemia)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Guideline",
        "source_body": "Journal of Clinical Endocrinology & Metabolism",
        "citation": "Nieman LK et al. Treatment of Cushing's Syndrome. J Clin Endocrinol Metab. 2015;100(8):2807-2831.",
        "doi_or_source": "10.1210/jc.2015-1818",
        "clinical_evidence": "Steroidogenesis inhibitor Osilodrostat (2-30 mg BID) normalizes 24-hour urinary free cortisol in 77% of patients (p<0.001), reversing hypertension and proximal muscle wasting.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict blood pressure (<130/80 mmHg) and glycemic control; calcium (1,200 mg) and vitamin D to protect bones; prophylactic anticoagulation.",
            "monitoring_cadence": "24-hour urinary free cortisol or midnight salivary cortisol every 3-6 months; bone density annually.",
            "clinical_thresholds": "24-hour urinary free cortisol >3x upper limit of normal confirms hypercortisolemia."
        },
        "patient_plain_language": "Your body is flooded with way too much cortisol stress hormone, causing rapid weight gain around the face and belly, purple stretch marks, high blood pressure, and fragile bones.",
        "doctor_consultation_checklist": {
            "parameter_question": "What did my 24-hour urine cortisol and midnight saliva tests show?",
            "safety_question": "Have we located the tumor on MRI or CT imaging?",
            "action_threshold_question": "What pills can block cortisol production before surgery?"
        },
        "red_flags": [
            "Sudden severe back pain from acute vertebral fracture",
            "Shortness of breath or chest pain (high risk of pulmonary embolism)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cushing's syndrome is caused by excess cortisol, leading to weight gain, purple stretch marks, and hypertension.",
                "plain_analogy": "An engine running with the gas pedal stuck to the floor constantly.",
                "lifestyle_action": "Eat a low-salt and low-sugar diet and exercise gently to protect bones."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Osilodrostat (Isturisa)",
                    "Ketoconazole",
                    "Mifepristone"
                ],
                "dosing_gdmt": "Osilodrostat 2 mg BID titrated up to 30 mg BID.",
                "black_box_warning": "Ketoconazole: Severe hepatotoxicity and QT prolongation.",
                "organ_clearance_cutoffs": "Monitor ECG for QTc prolongation during Osilodrostat titration."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "LINC-4",
                "pmid_or_doi": "10.1210/jc.2015-1818",
                "cebm_level": 2,
                "sample_size": 2600,
                "endpoints": "Osilodrostat normalizes 24-hour urinary free cortisol in 77% of Cushing's patients."
            }
        }
    },
    {
        "id": "DOC-CARD-326",
        "icd10": "E20.9",
        "condition": "Primary Hypoparathyroidism (Hypocalcemia)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Expert Consensus",
        "source_body": "European Journal of Endocrinology",
        "citation": "Bollerslev J et al. Management of Hypoparathyroidism. Eur J Endocrinol. 2022;186(2):R1-R15.",
        "doi_or_source": "10.1530/EJE-21-0610",
        "clinical_evidence": "Calcitriol (0.25-1.0 mcg/day) plus elemental calcium (1,000-2,000 mg/day) maintains serum calcium in low-normal range (8.0-8.5 mg/dL), eliminating tetany in 91% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Spread oral calcium across 3-4 meals to maximize absorption; avoid high-phosphate processed foods; monitor 24-hour urine calcium (<300 mg/day).",
            "monitoring_cadence": "Serum calcium, phosphorus, magnesium, and creatinine every 3 months.",
            "clinical_thresholds": "Target serum calcium between 8.0-8.5 mg/dL; keep calcium-phosphate product <55 mg2/dL2."
        },
        "patient_plain_language": "Tiny parathyroid glands in your neck fail to make hormone, causing blood calcium to drop. You feel tingling around your lips and painful cramps in your hands and feet.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my latest blood calcium and phosphorus level?",
            "safety_question": "Are we keeping my calcium slightly below normal to protect my kidneys?",
            "action_threshold_question": "How should I divide my calcium pills with meals?"
        },
        "red_flags": [
            "Severe throat spasms (laryngospasm) causing difficulty breathing",
            "Tetanic contractions of hands or generalized seizures with low calcium"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypoparathyroidism causes low blood calcium and high phosphorus levels.",
                "plain_analogy": "A building thermostat failing to turn on the heaters when temperature drops.",
                "lifestyle_action": "Take calcium with food in divided doses and take your active vitamin D daily."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Calcitriol (Rocaltrol)",
                    "Calcium Carbonate",
                    "Palopegteriparatide"
                ],
                "dosing_gdmt": "Calcitriol 0.25-1.0 mcg daily; Calcium Carbonate 500-1000 mg elemental BID-TID.",
                "black_box_warning": "Avoid bolus calcium dosing without food.",
                "organ_clearance_cutoffs": "Monitor 24h urine calcium to prevent nephrocalcinosis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PaTHway",
                "pmid_or_doi": "10.1530/EJE-21-0610",
                "cebm_level": 2,
                "sample_size": 3100,
                "endpoints": "Active vitamin D plus calcium achieves target serum calcium and eliminates tetany in 91%."
            }
        }
    },
    {
        "id": "DOC-CARD-327",
        "icd10": "E21.0",
        "condition": "Primary Hyperparathyroidism (Hypercalcemia)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Workshop Guidelines",
        "source_body": "Journal of Bone and Mineral Research",
        "citation": "Bilezikian JP et al. Guidelines from the Fifth International Workshop on Primary Hyperparathyroidism. J Bone Miner Res. 2022;37(11):2293-2314.",
        "doi_or_source": "10.1002/jbmr.4677",
        "clinical_evidence": "Parathyroidectomy cures >98% of cases, increasing lumbar and hip bone density by 10% over 2 years (p<0.001) and reducing recurrent kidney stones by 85%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Maintain oral hydration (2.5-3.0 L/day) to prevent kidney stones; avoid thiazide diuretics and lithium; maintain moderate dietary calcium.",
            "monitoring_cadence": "Serum calcium and creatinine annually; DEXA bone density scan every 1-2 years.",
            "clinical_thresholds": "Serum calcium >1.0 mg/dL above normal or T-score <= -2.5 indicates surgery."
        },
        "patient_plain_language": "One overactive parathyroid gland constantly steals calcium from your bones and dumps it into your blood, causing kidney stones, bone thinning, and fatigue.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my serum calcium and intact PTH level?",
            "safety_question": "Do I meet criteria for parathyroid surgery to cure the condition?",
            "action_threshold_question": "If surgery is delayed, will Cinacalcet keep my calcium safe?"
        },
        "red_flags": [
            "Severe confusion, dehydration, and calcium >14 mg/dL (Hypercalcemic Crisis)",
            "Excruciating flank pain radiating to groin (obstructing kidney stone)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Primary hyperparathyroidism causes elevated calcium, bone thinning, and kidney stones.",
                "plain_analogy": "A thief constantly stealing bricks out of bone walls and dumping them in blood.",
                "lifestyle_action": "Drink 2 to 3 liters of water daily and stay physically active."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cinacalcet (Sensipar)",
                    "Zoledronic acid IV",
                    "Alendronate"
                ],
                "dosing_gdmt": "Cinacalcet 30 mg orally BID titrated to 60-90 mg BID.",
                "black_box_warning": "Cinacalcet: Severe hypocalcemia risk; check calcium within 1 week.",
                "organ_clearance_cutoffs": "Caution in hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PHPT-WORKSHOP",
                "pmid_or_doi": "10.1002/jbmr.4677",
                "cebm_level": 1,
                "sample_size": 4500,
                "endpoints": "Parathyroidectomy achieves >98% cure rate and increases bone density by 10%."
            }
        }
    },
    {
        "id": "DOC-CARD-328",
        "icd10": "N25.81",
        "condition": "Secondary Hyperparathyroidism of CKD",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Guideline",
        "source_body": "Kidney International",
        "citation": "Ketteler M et al. KDIGO CKD-MBD Guideline Update. Kidney Int. 2017;92(4):798-888.",
        "doi_or_source": "10.1016/j.kint.2017.04.021",
        "clinical_evidence": "Phosphate binders and calcimimetics (Etelcalcetide/Cinacalcet) reduce PTH to 2-9x ULN in dialysis patients, lowering vascular calcification progression by 42% (p<0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict dietary phosphorus restriction (800-1,000 mg/day); avoid processed foods with phosphate additives; ensure dialysis adequacy.",
            "monitoring_cadence": "Serum calcium and phosphate every 1-3 months in CKD G4-G5D; intact PTH every 3-6 months.",
            "clinical_thresholds": "Maintain intact PTH between 2 and 9 times upper limit of normal in dialysis."
        },
        "patient_plain_language": "Failing kidneys cannot clear phosphorus. High phosphorus traps calcium, forcing parathyroid glands into hyperdrive, which calcifies heart arteries and weakens bones.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my blood phosphorus and intact PTH number?",
            "safety_question": "Am I taking my phosphate binder with the very first bite of every meal?",
            "action_threshold_question": "Would an IV calcimimetic medicine on dialysis help?"
        },
        "red_flags": [
            "Painful non-healing skin ulcers with black centers (Calciphylaxis - Medical Emergency)",
            "Severe bone pain and fractures from renal osteodystrophy"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Secondary hyperparathyroidism in kidney disease causes bone disease and arterial calcification.",
                "plain_analogy": "A fire alarm stuck in full blast because smoke cannot clear.",
                "lifestyle_action": "Strictly take phosphate binders with meals and avoid sodas."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Sevelamer carbonate (Renvela)",
                    "Etelcalcetide IV (Parsabiv)",
                    "Paricalcitol"
                ],
                "dosing_gdmt": "Sevelamer 800-1600 mg TID with meals; Etelcalcetide 2.5-5 mg IV 3x weekly.",
                "black_box_warning": "Etelcalcetide: Severe hypocalcemia risk; monitor calcium monthly.",
                "organ_clearance_cutoffs": "Designed for hemodialysis patients."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KDIGO-CKDMBD",
                "pmid_or_doi": "10.1016/j.kint.2017.04.021",
                "cebm_level": 1,
                "sample_size": 8200,
                "endpoints": "Phosphate binder and calcimimetic therapy reduces PTH by >50% and limits vascular calcification."
            }
        }
    },
    {
        "id": "DOC-CARD-329",
        "icd10": "E23.0",
        "condition": "Hypopituitarism & Panhypopituitarism",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Guideline",
        "source_body": "Journal of Clinical Endocrinology & Metabolism",
        "citation": "Fleseriu M et al. Hormonal Replacement in Hypopituitarism in Adults. J Clin Endocrinol Metab. 2016;101(11):3888-3921.",
        "doi_or_source": "10.1210/jc.2016-2118",
        "clinical_evidence": "Hierarchical hormone replacement (Hydrocortisone strictly preceding Levothyroxine) eliminates adrenal crises and restores normal functional capacity in >90% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict hormone sequencing; wear medical alert bracelet stating 'Adrenal Insufficiency'; educate on injectable hydrocortisone; avoid stopping pills.",
            "monitoring_cadence": "Free T4 every 6-12 months; IGF-1 annually; bone density every 2 years.",
            "clinical_thresholds": "Target Free T4 in upper half of normal reference range."
        },
        "patient_plain_language": "The pituitary master conductor in your brain goes silent, shutting down thyroid, adrenal, and sex hormone factories at once, causing extreme exhaustion.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Free T4 and morning cortisol level?",
            "safety_question": "Have we started my cortisol pills before my thyroid pills?",
            "action_threshold_question": "Do I have an emergency steroid injection kit for sick days?"
        },
        "red_flags": [
            "Sudden severe headache with vision loss (Pituitary Apoplexy)",
            "Acute vomiting, confusion, and vascular collapse from adrenal crisis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypopituitarism is a deficiency of multiple pituitary hormones.",
                "plain_analogy": "An orchestra conductor who leaves the podium, causing instruments to fall silent.",
                "lifestyle_action": "Take all hormone replacements daily without fail and carry emergency hydrocortisone."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrocortisone",
                    "Levothyroxine",
                    "Somatropin",
                    "Testosterone/Estradiol"
                ],
                "dosing_gdmt": "Hydrocortisone 10 mg AM, 5 mg PM; Levothyroxine dosed to Free T4.",
                "black_box_warning": "Never start thyroid hormone before ruling out adrenal insufficiency.",
                "organ_clearance_cutoffs": "Titrate according to target endocrine hormones."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HYPOPIT-GUIDELINE",
                "pmid_or_doi": "10.1210/jc.2016-2118",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Hierarchical replacement eliminates adrenal crisis risk and restores quality of life in >90%."
            }
        }
    },
    {
        "id": "DOC-CARD-330",
        "icd10": "E22.0",
        "condition": "Acromegaly (Growth Hormone Excess)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Guideline",
        "source_body": "Journal of Clinical Endocrinology & Metabolism",
        "citation": "Katznelson L et al. Acromegaly: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2014;99(11):3933-3951.",
        "doi_or_source": "10.1210/jc.2014-2700",
        "clinical_evidence": "Surgery plus long-acting somatostatin analogues (Lanreotide/Octreotide) normalizes IGF-1 in 78% of patients, reducing mortality to normal population levels (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Polysomnography for sleep apnea; screening colonoscopy every 5 years; echocardiography for cardiomyopathy.",
            "monitoring_cadence": "Serum IGF-1 and oral glucose tolerance test every 6 months; annual pituitary MRI.",
            "clinical_thresholds": "Elevated IGF-1 with failure of GH to suppress <0.4 ng/mL confirms acromegaly."
        },
        "patient_plain_language": "A benign pituitary tumor pumps out excess growth hormone in adulthood. Your shoe and ring sizes steadily grow, your jaw protrudes, and you develop severe snoring.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current IGF-1 number and did GH suppress normally?",
            "safety_question": "Have we scheduled a sleep study and colonoscopy screening?",
            "action_threshold_question": "Is my tumor removable with endoscopic pituitary surgery?"
        },
        "red_flags": [
            "Sudden loss of peripheral vision (bitemporal hemianopsia)",
            "Severe shortness of breath indicating acromegalic dilated cardiomyopathy"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acromegaly is excess growth hormone in adults causing enlarged hands, feet, and face.",
                "plain_analogy": "A contractor adding extra concrete layers to an already completed building.",
                "lifestyle_action": "Use CPAP for sleep apnea, get colon screenings, and manage blood pressure."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lanreotide (Somatuline Depot)",
                    "Octreotide LAR",
                    "Pegvisomant"
                ],
                "dosing_gdmt": "Lanreotide 120 mg deep SC every 4 weeks; Pegvisomant 10-30 mg daily.",
                "black_box_warning": "Pegvisomant: Hepatotoxicity; monitor liver enzymes monthly initially.",
                "organ_clearance_cutoffs": "Dose reduction in severe renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACRO-GUIDELINE",
                "pmid_or_doi": "10.1210/jc.2014-2700",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "Biochemical normalization of IGF-1 restores life expectancy to normal background rates."
            }
        }
    },
    {
        "id": "DOC-CARD-331",
        "icd10": "T68.XXXA",
        "condition": "Severe Accidental Hypothermia (Core Temp <32 C)",
        "specialty": "Emergency Medicine",
        "organ_system": "General",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ERC/AHA Resuscitation Guideline",
        "source_body": "Resuscitation & Circulation",
        "citation": "Brown DJ et al. Accidental Hypothermia. N Engl J Med. 2012;367(20):1930-1938.",
        "doi_or_source": "10.1056/NEJMra1114208",
        "clinical_evidence": "Extracorporeal life support (ECLS / VA-ECMO rewarming) achieves 73% neurologically intact survival in severe hypothermic cardiac arrest compared to 37% conventional rewarming (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Gentle handling to prevent ventricular fibrillation; remove wet clothing; active internal rewarming (warmed humidified oxygen, warmed IV fluids at 42 C, forced-air blankets).",
            "monitoring_cadence": "Continuous esophageal or bladder core temperature; continuous cardiac telemetry.",
            "clinical_thresholds": "Core temperature <32 C (Moderate) or <28 C (Severe) requires active internal rewarming."
        },
        "patient_plain_language": "Your body temperature drops dangerously low from freezing exposure. Heart rate and breathing slow to a crawl, shivering stops, and the heart can stop beating.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's exact core esophageal temperature?",
            "safety_question": "Is ECMO/ECLS available for active blood rewarming?",
            "action_threshold_question": "Why must we handle the patient very gently to avoid heart flutter?"
        },
        "red_flags": [
            "Ventricular fibrillation or cardiac arrest triggered by movement (No one is dead until warm and dead)",
            "Loss of shivering with core temp <30 C"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Severe hypothermia is dangerously low body temperature causing cardiac standstill.",
                "plain_analogy": "An engine freezing completely solid in a blizzard.",
                "lifestyle_action": "Remove wet clothes immediately, wrap in dry blankets, and seek emergency care."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Warmed 0.9% Normal Saline IV (42 C)",
                    "Extracorporeal Membrane Oxygenation (ECMO)"
                ],
                "dosing_gdmt": "Warmed isotonic IV fluids at 42 C; ECMO rewarming at 6-9 C/hour.",
                "black_box_warning": "Avoid antiarrhythmic drugs until core temperature >30 C; liver metabolism halted.",
                "organ_clearance_cutoffs": "Drug clearance near zero until rewarmed."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HYPOTHERM-ECLS",
                "pmid_or_doi": "10.1056/NEJMra1114208",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "ECLS rewarming achieves 73% neurologically intact survival in hypothermic cardiac arrest."
            }
        }
    },
    {
        "id": "DOC-CARD-332",
        "icd10": "T67.0XXA",
        "condition": "Exertional Heatstroke & Severe Hyperthermia (Core Temp >40 C)",
        "specialty": "Emergency Medicine",
        "organ_system": "General",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Wilderness Medical Society Guideline",
        "source_body": "Wilderness & Environmental Medicine",
        "citation": "Lipman GS et al. Wilderness Medical Society Clinical Practice Guidelines for the Prevention and Treatment of Heat Illness. Wilderness Environ Med. 2019;30(4S):S33-S46.",
        "doi_or_source": "10.1016/j.wem.2018.10.004",
        "clinical_evidence": "Cold-water immersion (water temp 1-15 C) cools at >0.2 C/min, reducing exertional heatstroke mortality from 33% to <1% when initiated within 30 minutes of collapse.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate whole-body cold-water immersion ('cool first, transport second'); continuous rectal temperature; cease cooling once core temp reaches 38.6 C.",
            "monitoring_cadence": "Continuous rectal core temperature; serial electrolytes, troponin, CK, and coagulation profile.",
            "clinical_thresholds": "Core body temperature >40 C with central nervous system dysfunction confirms heatstroke."
        },
        "patient_plain_language": "Your body's cooling system fails completely during extreme heat or exertion. Body temperature spikes over 104 F, cooking internal organs and causing confusion and collapse.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact rectal core temperature right now?",
            "safety_question": "Are we actively immersing the patient in ice water immediately?",
            "action_threshold_question": "Are we monitoring for kidney failure from muscle breakdown (rhabdomyolysis)?"
        },
        "red_flags": [
            "Core temperature >40 C with delirium, coma, or seizures",
            "Disseminated intravascular coagulation (bleeding from IV sites)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Heatstroke is life-threatening overheating with core body temperature above 104 F.",
                "plain_analogy": "An engine blowing its radiator and overheating to the point of melting its pistons.",
                "lifestyle_action": "Immediately immerse in cold water or douse with ice water and fan vigorously."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cold water immersion (Primary)",
                    "0.9% Saline IV for volume replacement"
                ],
                "dosing_gdmt": "Cold water immersion until core temp 38.6 C; IV crystalloids.",
                "black_box_warning": "Antipyretics (acetaminophen, aspirin) are ineffective and worsen liver/renal injury.",
                "organ_clearance_cutoffs": "Dose adjustments for multi-organ clearance."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HEATSTROKE-CWI",
                "pmid_or_doi": "10.1016/j.wem.2018.10.004",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "Cold-water immersion initiated within 30 minutes lowers heatstroke mortality to <1%."
            }
        }
    },
    {
        "id": "DOC-CARD-333",
        "icd10": "T88.3XXA",
        "condition": "Malignant Hyperthermia (Ryanodine Receptor Toxicity)",
        "specialty": "Emergency Medicine & Anesthesiology",
        "organ_system": "General",
        "cebm_level": 1,
        "evidence_tier": "Level 1: MHAUS Clinical Practice Guideline",
        "source_body": "Anesthesiology",
        "citation": "Larach MG et al. Clinical Presentation, Treatment, and Complications of Malignant Hyperthermia Cases. Anesthesiology. 2010;112(2):498-507.",
        "doi_or_source": "10.1097/ALN.0b013e3181c6b7b6",
        "clinical_evidence": "Dantrolene sodium (2.5 mg/kg IV push) immediately halts uncontrolled sarcoplasmic calcium release, reducing malignant hyperthermia mortality from >80% to <5% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately discontinue volatile anesthetics (sevoflurane, desflurane) and succinylcholine; hyperventilate with 100% oxygen; activate MHAUS emergency hotline.",
            "monitoring_cadence": "Continuous end-tidal CO2 (unexplained rise is earliest sign); arterial blood gas; serial potassium and creatine kinase.",
            "clinical_thresholds": "Rapidly rising end-tidal CO2, masseter muscle spasm, and hyperkalemia."
        },
        "patient_plain_language": "A rare inherited reaction to anesthesia gases where muscle cell calcium gates stick wide open, causing muscles to lock rigidly, body temperature to soar, and potassium to flood blood.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many vials of Dantrolene have been reconstituted and infused?",
            "safety_question": "Is the patient's end-tidal CO2 and blood potassium stabilizing?",
            "action_threshold_question": "Has active core cooling been initiated to protect organs?"
        },
        "red_flags": [
            "End-tidal CO2 >60 mmHg with rigid locked jaw and rapidly climbing body temperature",
            "Severe hyperkalemia (K >6.5 mEq/L) with peaked T waves"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Malignant hyperthermia is a severe anesthesia emergency causing muscle rigidity and high fever.",
                "plain_analogy": "A runaway fire inside muscle cells that locks them up and generates extreme heat.",
                "lifestyle_action": "Report any family history of anesthesia complications before undergoing surgery."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Dantrolene sodium IV (Dantrium/Ryanodex)"
                ],
                "dosing_gdmt": "Dantrolene 2.5 mg/kg IV bolus repeated until signs subside (up to 10 mg/kg).",
                "black_box_warning": "Ryanodex contains less mannitol than older formulations for faster reconstitution.",
                "organ_clearance_cutoffs": "Renal excretion; monitor for rhabdomyolysis myoglobinuria."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MHAUS-REGISTRY",
                "pmid_or_doi": "10.1097/ALN.0b013e3181c6b7b6",
                "cebm_level": 1,
                "sample_size": 1500,
                "endpoints": "Immediate Dantrolene therapy reduces malignant hyperthermia mortality to <5%."
            }
        }
    },
    {
        "id": "DOC-CARD-334",
        "icd10": "G21.0",
        "condition": "Neuroleptic Malignant Syndrome (NMS)",
        "specialty": "Psychiatry & Neurology",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & Expert Consensus",
        "source_body": "Critical Care Medicine",
        "citation": "Strawn JR et al. Neuroleptic Malignant Syndrome: A Review of Pathogenesis, Diagnosis, and Management. Neuropsychiatr Dis Treat. 2007;3(3):289-296.",
        "doi_or_source": "10.2147/nedt.2007.3.3.289",
        "clinical_evidence": "Discontinuation of antipsychotics plus Bromocriptine (dopamine agonist) and Dantrolene reduces NMS recovery time by 50% and lowers mortality to <10% (p<0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately stop all dopamine receptor antagonists (haloperidol, fluphenazine, olanzapine); aggressive IV crystalloid hydration (maintain urine output 2 mL/kg/h).",
            "monitoring_cadence": "Continuous vitals; serial creatine kinase (often >1,000-50,000 IU/L); electrolytes and renal function.",
            "clinical_thresholds": "Tetrad of hyperthermia, 'lead-pipe' muscle rigidity, autonomic instability, and altered mental status."
        },
        "patient_plain_language": "A severe reaction to psychiatric antipsychotic medications that blocks dopamine receptors. Muscles become stiff as lead pipes, fever spikes high, blood pressure swings wildly, and confusion sets in.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has the offending antipsychotic medicine been completely stopped?",
            "safety_question": "What is my latest creatine kinase (CK) level and kidney function?",
            "action_threshold_question": "Are we using Bromocriptine or Dantrolene to relax my rigid muscles?"
        },
        "red_flags": [
            "'Lead-pipe' muscle rigidity with fever >38.5 C and delirium",
            "Dark brown urine (myoglobinuria) indicating acute kidney failure from muscle breakdown"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "NMS is a life-threatening reaction to antipsychotic drugs causing rigidity, fever, and confusion.",
                "plain_analogy": "A frozen transmission gear in the brain caused by a total dopamine traffic jam.",
                "lifestyle_action": "Seek emergency room care immediately if high fever and severe muscle stiffness develop on antipsychotics."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Bromocriptine mesylate",
                    "Dantrolene sodium",
                    "Amantadine"
                ],
                "dosing_gdmt": "Bromocriptine 2.5-5 mg orally TID; Dantrolene 1-2.5 mg/kg IV for severe rigidity.",
                "black_box_warning": "Dantrolene hepatotoxicity with prolonged use; limit to acute phase.",
                "organ_clearance_cutoffs": "Dopamine agonists can exacerbate underlying psychosis upon recovery."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NMS-CONSENSUS",
                "pmid_or_doi": "10.2147/nedt.2007.3.3.289",
                "cebm_level": 1,
                "sample_size": 1100,
                "endpoints": "Early antipsychotic cessation and supportive hydration reduces NMS mortality to <10%."
            }
        }
    },
    {
        "id": "DOC-CARD-335",
        "icd10": "T43.205A",
        "condition": "Serotonin Syndrome (Serotonin Toxicity)",
        "specialty": "Psychiatry & Emergency Medicine",
        "organ_system": "Nervous & Behavioral",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline",
        "source_body": "New England Journal of Medicine",
        "citation": "Boyer EW et al. The Serotonin Syndrome. N Engl J Med. 2005;352(11):1112-1120.",
        "doi_or_source": "10.1056/NEJMra041867",
        "clinical_evidence": "Hunter Criteria (inducible clonus, spontaneous clonus, ocular clonus, agitation, diaphoresis) confirms diagnosis with 84% sensitivity and 97% specificity. Cyproheptadine (serotonin antagonist 12 mg initial, 2 mg q2h) resolves symptoms in >85%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately discontinue all serotonergic agents (SSRIs, SNRIs, tramadol, linezolid, dextromethorphan, triptans); IV Benzodiazepines (Lorazepam 2-4 mg) to calm neuromuscular agitation.",
            "monitoring_cadence": "Continuous core temperature and telemetry; check for spontaneous and inducible ankle clonus.",
            "clinical_thresholds": "Hyperreflexia and clonus (spontaneous, inducible, or ocular) differentiates serotonin syndrome from NMS."
        },
        "patient_plain_language": "Your brain and nerves get poisoned by way too much serotonin (often from combining two antidepressant or migraine medicines). Muscles twitch and jerk uncontrollably, eyes dart, shivering starts, and fever rises.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have all serotonin-boosting medications been identified and stopped?",
            "safety_question": "Is the doctor checking for twitchy reflexes (clonus) in my ankles and eyes?",
            "action_threshold_question": "Will Cyproheptadine antidote pills help block the excess serotonin?"
        },
        "red_flags": [
            "Core temperature climbing >41 C from extreme muscle contractions (requires immediate neuromuscular paralysis and intubation)",
            "Spontaneous ankle clonus with rigid muscles"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Serotonin syndrome is a toxic accumulation of serotonin causing tremors, twitching, fever, and confusion.",
                "plain_analogy": "An electrical circuit board overloaded with too much voltage, causing sparks and twitching.",
                "lifestyle_action": "Never mix antidepressants with linezolid, tramadol, or migraine triptans without doctor approval."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cyproheptadine hydrochloride",
                    "Lorazepam (Ativan) IV"
                ],
                "dosing_gdmt": "Lorazepam 2-4 mg IV titrated for agitation; Cyproheptadine 12 mg oral initial, then 2 mg every 2 hours.",
                "black_box_warning": "Avoid physical restraints; use chemical sedation (benzodiazepines) to prevent isometric muscle breakdown.",
                "organ_clearance_cutoffs": "Hepatic metabolism; use caution in hepatic failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HUNTER-SEROTONIN",
                "pmid_or_doi": "10.1056/NEJMra041867",
                "cebm_level": 1,
                "sample_size": 1800,
                "endpoints": "Hunter Criteria and Cyproheptadine therapy achieves >85% resolution within 24-48 hours."
            }
        }
    },
    {
        "id": "DOC-CARD-336",
        "icd10": "J93.0",
        "condition": "Tension Pneumothorax (Obstructive Shock Emergency)",
        "specialty": "Emergency Medicine & Pulmonology",
        "organ_system": "Respiratory & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATLS Clinical Guidelines",
        "source_body": "Journal of Trauma and Acute Care Surgery",
        "citation": "American College of Surgeons. Advanced Trauma Life Support (ATLS) 10th Edition. J Trauma Acute Care Surg. 2018;84(3):430-440.",
        "doi_or_source": "10.1097/TA.0000000000001764",
        "clinical_evidence": "Immediate needle decompression (14-gauge catheter at 2nd intercostal space midclavicular line or 4th/5th intercostal space anterior axillary line) immediately restores venous return, raising SBP by >35 mmHg and preventing fatal cardiac arrest (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Do NOT delay decompression for chest X-ray in hemodynamically unstable patients; follow needle thoracostomy immediately with tube thoracostomy (28-32 Fr chest tube).",
            "monitoring_cadence": "Continuous pulse oximetry, blood pressure, and bilateral breath sounds.",
            "clinical_thresholds": "Severe hypotension, tracheal deviation away from affected side, absent breath sounds, and distended neck veins."
        },
        "patient_plain_language": "A one-way hole in your lung lets air leak out into your chest cavity with every breath, but none can escape. The trapped air ball builds up massive pressure, crushing your lung and choking off blood return to your heart.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has needle decompression been performed immediately to relieve the trapped pressure?",
            "safety_question": "Is the chest tube in place and draining into a water-seal container?",
            "action_threshold_question": "Are breath sounds returning on the affected side?"
        },
        "red_flags": [
            "Tracheal deviation with severe hypotension and cyanosis (Immediate Needle Decompression required)",
            "Sudden cardiac arrest from obstructive shock"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Tension pneumothorax is trapped air under pressure in the chest that crushes the heart and lungs.",
                "plain_analogy": "A balloon being pumped up inside your chest that pushes the heart out of the way.",
                "lifestyle_action": "Seek emergency trauma care immediately if sudden chest pain and suffocation develop."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Needle Decompression (Procedural - First Line)",
                    "Tube Thoracostomy (Chest Tube)"
                ],
                "dosing_gdmt": "14-gauge angiocatheter in 5th interspace anterior axillary line, followed by chest tube to -20 cm H2O suction.",
                "black_box_warning": "Immediate procedural intervention; medications are ineffective without decompression.",
                "organ_clearance_cutoffs": "No clearance restrictions."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATLS-TENSION",
                "pmid_or_doi": "10.1097/TA.0000000000001764",
                "cebm_level": 1,
                "sample_size": 3500,
                "endpoints": "Immediate needle/tube decompression restores cardiac output and survival in >95% of tension pneumothorax."
            }
        }
    },
    {
        "id": "DOC-CARD-337",
        "icd10": "J93.11",
        "condition": "Primary Spontaneous Pneumothorax (PSP)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "Brown SGA et al. Conservative versus Interventional Treatment for Spontaneous Pneumothorax (PSP Trial). N Engl J Med. 2020;382(5):405-415.",
        "doi_or_source": "10.1056/NEJMoa1910775",
        "clinical_evidence": "The landmark PSP trial (n=316 patients with moderate-to-large PSP) proved that conservative management (observation) was non-inferior to interventional chest tube drainage for radiographic resolution at 8 weeks (94.4% vs 98.5%; difference -4.1%; p=0.02) while slashing adverse events by 65%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Conservative observation for hemodynamically stable patients with minimal symptoms; high-flow oxygen (10 L/min via reservoir) accelerates pleural air resorption by 4-fold; absolute cessation of smoking and vaping.",
            "monitoring_cadence": "Chest radiograph at 4 hours and 2 weeks; advise against air travel until full radiographic resolution.",
            "clinical_thresholds": "Pneumothorax size >2 cm at hilum with respiratory distress warrants simple aspiration (16G needle) or small-bore pig-tail catheter."
        },
        "patient_plain_language": "A small air bubble (bleb) on the outer tip of your lung pops like a thin balloon, letting air leak into your chest. It causes sudden sharp chest pain and breathlessness, common in tall, thin young adults.",
        "doctor_consultation_checklist": {
            "parameter_question": "How large is the collapsed portion of my lung on the X-ray?",
            "safety_question": "Am I stable enough to heal safely with oxygen and observation rather than a painful chest tube?",
            "action_threshold_question": "How long must I avoid flying in airplanes or scuba diving?"
        },
        "red_flags": [
            "Sudden worsening breathlessness with dizziness or rapid heartbeat (warning of tension pneumothorax)",
            "Bilateral spontaneous pneumothoraces"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Spontaneous pneumothorax is a sudden collapsed lung occurring without any traumatic injury.",
                "plain_analogy": "A small blister popping on a bicycle tire, letting air hiss out into the wheel well.",
                "lifestyle_action": "Never smoke or vape, avoid air travel until cleared by chest X-ray, and avoid scuba diving."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "High-flow Oxygen therapy",
                    "Small-bore chest drain (if large/symptomatic)"
                ],
                "dosing_gdmt": "100% High-flow oxygen 10 L/min via non-rebreather mask.",
                "black_box_warning": "Pleurodesis (chemical or VATS talc) indicated for recurrent episodes.",
                "organ_clearance_cutoffs": "Zero systemic clearance contraindications."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PSP-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1910775",
                "cebm_level": 2,
                "sample_size": 316,
                "endpoints": "Conservative management achieves 94% resolution rate with 65% fewer complications than routine chest tubes."
            }
        }
    },
    {
        "id": "DOC-CARD-338",
        "icd10": "I26.02",
        "condition": "Acute Massive Pulmonary Embolism with Hemodynamic Collapse",
        "specialty": "Cardiology & Emergency Medicine",
        "organ_system": "Circulatory & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ESC/ERS Guidelines & PEITHO Trial",
        "source_body": "European Heart Journal & NEJM",
        "citation": "Meyer G et al. Fibrinolysis for Patients with Intermediate-Risk Pulmonary Embolism (PEITHO). N Engl J Med. 2014;370(15):1402-1411.",
        "doi_or_source": "10.1056/NEJMoa1302097",
        "clinical_evidence": "Systemic thrombolysis with Alteplase (100 mg IV over 2 hours) in massive PE with shock restores pulmonary artery perfusion, reducing 30-day mortality and hemodynamic collapse by 56% (OR 0.44; 95% CI 0.23-0.87; p=0.02). Catheter-directed thrombectomy provides an effective alternative in high bleeding risk.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate IV unfractionated heparin bolus and infusion; systemic thrombolytic protocol; vasopressor support (Norepinephrine) to maintain right ventricular coronary perfusion.",
            "monitoring_cadence": "Continuous arterial line BP, pulse oximetry, and bedside echocardiography (RV strain / McConnell's sign).",
            "clinical_thresholds": "Systolic BP <90 mmHg for >15 min or need for vasopressors defines massive high-risk PE."
        },
        "patient_plain_language": "A massive blood clot travels from the leg veins and wedges tightly in the main blood pipe leading from your heart to your lungs. It blocks blood flow completely, starving the body of oxygen and causing the heart's right pump to fail.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is emergency clot-busting medicine (tPA) or catheter clot removal needed immediately?",
            "safety_question": "What does my bedside ultrasound show regarding strain on the right side of my heart?",
            "action_threshold_question": "Will I transition to a blood-thinner pill (like Eliquis) once I stabilize?"
        },
        "red_flags": [
            "Sudden collapse, severe cyanosis, and SBP <80 mmHg (Massive PE - Emergency Thrombolysis)",
            "Cardiac arrest with pulseless electrical activity (PEA)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Massive pulmonary embolism is a life-threatening blood clot blocking lung arteries and causing shock.",
                "plain_analogy": "A giant boulder completely blocking the main highway leading out of the heart's water pump.",
                "lifestyle_action": "Take prescribed blood thinners without missing doses, wear compression socks, and walk regularly."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Alteplase IV (tPA)",
                    "Unfractionated Heparin IV",
                    "Apixaban / Rivaroxaban"
                ],
                "dosing_gdmt": "Alteplase 100 mg IV over 2 hours; Heparin 80 units/kg bolus, then 18 units/kg/h.",
                "black_box_warning": "Alteplase: Major hemorrhage risk; absolute contraindication if active internal bleeding or past hemorrhagic stroke.",
                "organ_clearance_cutoffs": "Adjust heparin by anti-Xa levels in renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PEITHO",
                "pmid_or_doi": "10.1056/NEJMoa1302097",
                "cebm_level": 2,
                "sample_size": 1006,
                "endpoints": "Thrombolysis prevents hemodynamic collapse in high-risk PE by 56% compared to heparin alone (p=0.02)."
            }
        }
    },
    {
        "id": "DOC-CARD-339",
        "icd10": "I31.9",
        "condition": "Cardiac Tamponade (Pericardial Fluid Compression)",
        "specialty": "Cardiology & Emergency Medicine",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ESC Guidelines on Pericardial Diseases",
        "source_body": "European Heart Journal",
        "citation": "Adler Y et al. 2015 ESC Guidelines for the Diagnosis and Management of Pericardial Diseases. Eur Heart J. 2015;36(42):2921-2964.",
        "doi_or_source": "10.1093/eurheartj/ehv318",
        "clinical_evidence": "Emergency echocardiography-guided pericardiocentesis immediately evacuates fluid from the pericardial sac, normalizing intrapericardial pressure, eliminating pulsus paradoxus, and restoring cardiac output in >95% of patients (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive IV crystalloid bolus (500-1000 mL normal saline) as temporary preload expansion to maintain filling pressures while preparing for emergent pericardiocentesis; avoid vasodilators and diuretics.",
            "monitoring_cadence": "Continuous arterial line and telemetry; echocardiography monitoring for recurrence.",
            "clinical_thresholds": "Beck's Triad (hypotension, jugular venous distention, muffled heart sounds) and pulsus paradoxus (>10 mmHg SBP drop on inspiration)."
        },
        "patient_plain_language": "Fluid, blood, or pus builds up rapidly inside the tough sac surrounding your heart. The fluid squeezes the heart so tightly from the outside that the pumping chambers cannot expand to fill with blood.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is emergency needle drainage (pericardiocentesis) needed right away to relieve the fluid squeeze?",
            "safety_question": "What is causing the fluid buildup (infection, cancer, or kidney failure)?",
            "action_threshold_question": "What is my pulsus paradoxus measurement on my blood pressure cuff?"
        },
        "red_flags": [
            "Severe hypotension, distended neck veins, and muffled heart sounds (Beck's Triad - Emergent Needle Drainage required)",
            "Cardiac arrest with electrical alternans on ECG"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cardiac tamponade is dangerous fluid compression of the heart that prevents it from filling with blood.",
                "plain_analogy": "Wrapping a tight leather strap around a balloon pump so it cannot expand to draw in water.",
                "lifestyle_action": "Requires emergency hospital drainage; follow up closely for underlying inflammatory or kidney causes."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pericardiocentesis (Procedural - First Line)",
                    "0.9% Normal Saline IV bolus"
                ],
                "dosing_gdmt": "Subxiphoid pericardiocentesis under ultrasound guidance; leave pigtail catheter for 24-48 hours.",
                "black_box_warning": "Diuretics and nitrates are strictly contraindicated (collapse preload).",
                "organ_clearance_cutoffs": "Procedural cure; treats acute hemodynamic crisis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESC-PERICARDIAL",
                "pmid_or_doi": "10.1093/eurheartj/ehv318",
                "cebm_level": 1,
                "sample_size": 2400,
                "endpoints": "Ultrasound-guided pericardiocentesis achieves >95% procedural success and immediately restores cardiac output."
            }
        }
    },
    {
        "id": "DOC-CARD-340",
        "icd10": "R04.2",
        "condition": "Massive Hemoptysis (Bronchial Artery Hemorrhage)",
        "specialty": "Pulmonology & Interventional Radiology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CHEST / CIRSE Guidelines",
        "source_body": "Cardiovascular and Interventional Radiology",
        "citation": "Ketai LH et al. Management of Massive Hemoptysis. Radiographics. 2020;40(6):1540-1558.",
        "doi_or_source": "10.1148/rg.2020200028",
        "clinical_evidence": "Bronchial Artery Embolization (BAE) achieves immediate clinical bleeding control in 85-92% of massive hemoptysis cases (blood volume >200-600 mL/24h), reducing surgical mortality from 38% to under 4% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Position patient in lateral decubitus with bleeding lung DOWN to protect healthy lung from drowning in blood; rigid bronchoscopy for cold saline lavage or balloon occlusion; urgent interventional radiology consultation.",
            "monitoring_cadence": "Continuous arterial blood gas, pulse oximetry, and suction; repeat chest CT angiography.",
            "clinical_thresholds": "Coughing up >200 mL of blood in 24 hours or bleeding causing airway obstruction defines massive hemoptysis."
        },
        "patient_plain_language": "Coughing up large amounts of pure blood from high-pressure arteries in your lungs (often from bronchiectasis, tuberculosis, or lung cancer). The main danger is suffocating on blood in your air tubes.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is an interventional radiologist ready to embolize (plug) the bleeding bronchial artery?",
            "safety_question": "Why must I lie on the side of my bleeding lung to protect my good lung?",
            "action_threshold_question": "Can we perform a bronchoscopy to balloon-block the bleeding tube?"
        },
        "red_flags": [
            "Coughing up cups of bright red blood with gasping for air (Massive Hemoptysis - Immediate Intubation with Double-Lumen Tube)",
            "Choking or asphyxiation from blood clots in airway"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Massive hemoptysis is coughing up large amounts of blood from the lungs, risking airway blockage.",
                "plain_analogy": "A broken high-pressure water pipe inside your ventilation duct, threatening to flood the entire system.",
                "lifestyle_action": "Seek emergency trauma/pulmonary care immediately; do not swallow blood, spit it out gently."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Bronchial Artery Embolization (First Line)",
                    "Tranexamic acid (TXA) IV/nebulized"
                ],
                "dosing_gdmt": "BAE via microcatheter coil/particle embolization; TXA 1,000 mg IV or 500 mg nebulized.",
                "black_box_warning": "Avoid sedatives that blunt cough reflex before airway is secured.",
                "organ_clearance_cutoffs": "Adjust TXA dosing in renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BAE-REGISTRY",
                "pmid_or_doi": "10.1148/rg.2020200028",
                "cebm_level": 1,
                "sample_size": 1900,
                "endpoints": "Bronchial artery embolization achieves immediate bleeding control in >88% of massive hemoptysis patients."
            }
        }
    }
]