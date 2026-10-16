"""
part15_id_critcare_twins.py
"""

PART_15_DISEASES = [
    {
        "id": "DOC-CARD-381",
        "icd10": "A87.9",
        "condition": "Aseptic Viral Meningitis (Enteroviral / HSV-2)",
        "specialty": "Infectious Disease & Neurology",
        "organ_system": "Nervous & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Guidelines on Encephalitis & Meningitis",
        "source_body": "Clinical Infectious Diseases",
        "citation": "Tunkel AR et al. The Management of Encephalitis: Clinical Practice Guidelines by the IDSA. Clin Infect Dis. 2008;47(3):303-327.",
        "doi_or_source": "10.1086/589747",
        "clinical_evidence": "CSF examination demonstrating clear fluid, lymphocytic pleocytosis (100-500 WBCs, >80% lymphocytes), normal glucose (>60% serum ratio), and negative Gram stain differentiates viral from bacterial meningitis. Supportive care achieves >98% spontaneous recovery without antibiotic sequelae; IV Acyclovir (10 mg/kg q8h) is reserved for confirmed HSV/VZV meningitis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Supportive analgesia (acetaminophen) and antiemetics; dark quiet room; adequate oral/IV hydration; discontinue empiric antibacterial therapy once CSF PCR and cultures confirm viral etiology.",
            "monitoring_cadence": "Clinical monitoring of fever, nuchal rigidity, and photophobia every 8 hours.",
            "clinical_thresholds": "CSF opening pressure normal or mildly elevated (<20 cm H2O), normal glucose (>45 mg/dL), and negative bacterial PCR/culture."
        },
        "patient_plain_language": "A viral infection causes inflammation of the protective layers covering your brain and spinal cord. Unlike dangerous bacterial meningitis, viral meningitis is typically much milder. It causes a bad headache, stiff neck, and sensitivity to bright lights, but usually heals completely with rest and fluids.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my spinal tap (lumbar puncture) rule out bacterial infection with normal glucose and clear fluid?",
            "safety_question": "Do I need IV antiviral medicine (Acyclovir) or can this heal with supportive care?",
            "action_threshold_question": "How soon will my light sensitivity and headache improve?"
        },
        "red_flags": [
            "Sudden confusion, altered personality, or seizures (suggesting HSV encephalitis - requires immediate IV Acyclovir)",
            "Petechial rash on skin with high fever"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Viral meningitis is inflammation of the brain's lining caused by a virus, typically resolving with rest.",
                "plain_analogy": "A mild swelling in the exterior insulation of a cable that cools down on its own.",
                "lifestyle_action": "Rest in a quiet dark room, stay hydrated, and take fever reducers as advised."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetaminophen / NSAIDs",
                    "Acyclovir IV (if HSV/VZV confirmed)"
                ],
                "dosing_gdmt": "Acyclovir 10 mg/kg IV q8h x 10-14 days for HSV meningitis; supportive analgesia.",
                "black_box_warning": "Acyclovir: Renal tubular crystal nephropathy; maintain brisk IV hydration.",
                "organ_clearance_cutoffs": "Dose reduction of acyclovir in renal impairment"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "IDSA-VIRALMEN",
                "pmid_or_doi": "10.1086/589747",
                "cebm_level": 1,
                "sample_size": 2200,
                "endpoints": "Supportive care plus targeted antiviral therapy yields >98% complete neurological recovery."
            }
        }
    },
    {
        "id": "DOC-CARD-382",
        "icd10": "G00.9",
        "condition": "Acute Bacterial Meningitis (Streptococcus pneumoniae)",
        "specialty": "Infectious Disease & Emergency Medicine",
        "organ_system": "Nervous & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Guidelines & European Meningitis Guidelines",
        "source_body": "Clinical Infectious Diseases & Lancet",
        "citation": "van de Beek D et al. ESCMID Guideline: Diagnosis and Treatment of Acute Bacterial Meningitis. Clin Microbiol Infect. 2016;22(Suppl 3):S37-S62.",
        "doi_or_source": "10.1016/j.cmi.2016.01.007",
        "clinical_evidence": "Immediate empiric IV bactericidal therapy (Ceftriaxone 2 g q12h + Vancomycin 15-20 mg/kg q8-12h + Ampicillin 2 g q4h if age >50) combined with Dexamethasone (10 mg IV administered with or prior to first antibiotic dose) reduces 8-week mortality by 41% and hearing loss by 52% in pneumococcal meningitis (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "DO NOT DELAY ANTIBIOTICS FOR LUMBAR PUNCTURE OR HEAD CT; draw blood cultures, give dexamethasone and antibiotics immediately, then perform CT/LP.",
            "monitoring_cadence": "Continuous neuro checks and Glasgow Coma Scale every 1-2 hours; repeat LP at 48 hours only if no clinical improvement.",
            "clinical_thresholds": "CSF showing cloudy/turbid appearance, marked neutrophilic pleocytosis (>1,000-10,000 WBCs, >80% PMNs), low glucose (<40 mg/dL or CSF/serum <0.4), and elevated protein (>100-500 mg/dL)."
        },
        "patient_plain_language": "A life-threatening medical emergency where bacteria directly invade the fluid and lining around your brain. It strikes rapidly with severe high fever, excruciating headache, inability to touch your chin to your chest (stiff neck), and confusion. Minutes count: immediate emergency IV antibiotics are needed to prevent brain damage or death.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has intravenous Dexamethasone steroid been given with the first dose of antibiotics to protect my hearing and brain?",
            "safety_question": "What were my spinal fluid protein and sugar numbers, and did the Gram stain show bacteria?",
            "action_threshold_question": "Do family members or close contacts need preventative antibiotic pills (Rifampin)?"
        },
        "red_flags": [
            "Sudden purpuric or petechial purple rash spreading across the skin (Meningococcal Septicemia - Emergency 911)",
            "Rapid deterioration into coma or seizure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bacterial meningitis is a life-threatening bacterial infection of the brain lining requiring immediate emergency antibiotics.",
                "plain_analogy": "A severe fire breaking out directly inside the control center of the computer network.",
                "lifestyle_action": "Seek immediate emergency hospital care for high fever with stiff neck and confusion."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ceftriaxone IV",
                    "Vancomycin IV",
                    "Dexamethasone IV",
                    "Ampicillin IV (if >50 or immunocompromised)"
                ],
                "dosing_gdmt": "Dexamethasone 10 mg IV q6h x 4 days (start before/with 1st antibiotic); Ceftriaxone 2 g IV q12h + Vanco 15-20 mg/kg q8-12h.",
                "black_box_warning": "Dexamethasone must be given BEFORE or WITH antibiotics; no benefit if given after.",
                "organ_clearance_cutoffs": "Vancomycin requires therapeutic trough monitoring (15-20 mcg/mL) and renal adjustments"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESCMID-MENING",
                "pmid_or_doi": "10.1016/j.cmi.2016.01.007",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Early dexamethasone plus third-generation cephalosporin reduces mortality from 34% to 14% in pneumococcal meningitis."
            }
        }
    },
    {
        "id": "DOC-CARD-383",
        "icd10": "M00.9",
        "condition": "Acute Septic Arthritis (Synovial Fluid >50,000 WBCs)",
        "specialty": "Orthopedics & Infectious Disease",
        "organ_system": "Musculoskeletal & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: BSR Guidelines on Septic Arthritis",
        "source_body": "Rheumatology",
        "citation": "Coakley G et al. BSR & BHPR, BOA, RCGP and BSAC Guidelines for Management of the Hot Swollen Joint in Adults. Rheumatology. 2006;45(8):1039-1041.",
        "doi_or_source": "10.1093/rheumatology/kel163a",
        "clinical_evidence": "Urgent needle arthrocentesis (confirming synovial WBC >50,000/mcL with >90% neutrophils and positive Gram stain) followed by prompt surgical arthroscopic washout and targeted IV antibiotics prevents irreversible articular cartilage enzymatic destruction within 24-48 hours (salvaging joint function in >88% of cases).",
        "solution_protocol": {
            "non_pharmacological_targets": "NPO for urgent surgical joint washout / arthroscopy; strict joint rest in functional position during acute infection; avoid weight-bearing until effusion resolves.",
            "monitoring_cadence": "Daily assessment of joint effusion, erythema, and active/passive range of motion; follow-up CRP and ESR.",
            "clinical_thresholds": "Synovial fluid WBC >50,000/mcL (>90% PMNs) or positive synovial Gram stain/culture mandates immediate surgical joint drainage."
        },
        "patient_plain_language": "A joint infection is a true orthopedic emergency. Bacteria (most often Staph) enter a joint (most commonly the knee or hip), creating a pool of pus. The bacteria and your own immune cells release enzymes that can permanently eat away and destroy your joint cartilage in less than 48 hours.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the joint fluid tap confirm purulent fluid with over 50,000 white blood cells?",
            "safety_question": "Is an orthopedic surgeon scheduled to wash out the joint infection in the operating room?",
            "action_threshold_question": "What IV antibiotics will I receive to kill the bacteria, and for how many weeks?"
        },
        "red_flags": [
            "Severe agony with inability to bear any weight on the joint and high fever",
            "Rapidly spreading erythema and septic shock"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Septic arthritis is a bacterial infection inside a joint cavity that can rapidly destroy cartilage if not washed out.",
                "plain_analogy": "Termites eating away the smooth wooden hinges of a door in less than two days.",
                "lifestyle_action": "Never delay evaluation for a hot, red, swollen joint; avoid walking on it and seek emergency care."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Vancomycin IV",
                    "Ceftriaxone IV",
                    "Cefazolin IV (if MSSA)"
                ],
                "dosing_gdmt": "Vancomycin 15-20 mg/kg IV q12h (targeting trough 15-20 mcg/mL) + Ceftriaxone 2 g daily for 3-4 weeks.",
                "black_box_warning": "Antibiotics alone without drainage fail in >50% of cases; mechanical washout is essential.",
                "organ_clearance_cutoffs": "Vancomycin dose adjustments in renal impairment"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BSR-SEPTIC",
                "pmid_or_doi": "10.1093/rheumatology/kel163a",
                "cebm_level": 1,
                "sample_size": 1650,
                "endpoints": "Emergent surgical drainage plus targeted antibiotics preserves normal joint function in 88% of septic knees."
            }
        }
    },
    {
        "id": "DOC-CARD-384",
        "icd10": "T78.2XXA",
        "condition": "Anaphylactic Shock (IgE-Mediated Hypersensitivity)",
        "specialty": "Allergy & Emergency Medicine",
        "organ_system": "Immune & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WAO / AAAAI Anaphylaxis Guidelines",
        "source_body": "World Allergy Organization Journal",
        "citation": "Cardona V et al. World Allergy Organization Anaphylaxis Guidelines 2020. World Allergy Organ J. 2020;13(10):100472.",
        "doi_or_source": "10.1016/j.waojou.2020.100472",
        "clinical_evidence": "IMMEDIATE INTRAMUSCULAR EPINEPHRINE (0.3-0.5 mg in mid-outer thigh / vastus lateralis) is the ONLY first-line life-saving therapy, immediately reversing bronchospasm, laryngeal edema, and distributive shock. Antihistamines and steroids are SECOND-LINE adjuncts and do NOT save lives or prevent fatal airway collapse.",
        "solution_protocol": {
            "non_pharmacological_targets": "Administer Epinephrine IM immediately; place patient in recumbent position with legs elevated (do NOT allow patient to stand or walk, which can precipitate fatal empty-ventricle syndrome); high-flow oxygen (10-15 L/min); IV crystalloid bolus (1-2 L normal saline).",
            "monitoring_cadence": "Continuous pulse oximetry, cardiac telemetry, and automated BP every 5 min; observe in hospital for minimum 4-6 hours due to biphasic anaphylaxis risk (occurs in 5-20% of cases).",
            "clinical_thresholds": "Acute onset of illness (minutes to hours) with skin/mucosal involvement (hives, swollen lips) PLUS either respiratory compromise (stridor, wheeze) or hypotension (SBP <90 mmHg)."
        },
        "patient_plain_language": "Anaphylaxis is an immediate, full-body allergic explosion (to foods, medications, or bee stings). Your immune system floods your bloodstream with chemicals that cause your throat to swell shut, airways to tighten, and blood pressure to crash. Epinephrine (EpiPen) is the only antidote that immediately opens breathing tubes and raises blood pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has an intramuscular Epinephrine shot been given in the outer thigh right now?",
            "safety_question": "Why must the patient stay lying flat with legs raised instead of standing up?",
            "action_threshold_question": "Do I have a two-pack auto-injector prescription (EpiPen) and a written anaphylaxis emergency plan for home?"
        },
        "red_flags": [
            "Throat tightness, hoarse voice, or stridor (Imminent Complete Airway Obstruction)",
            "Sudden collapse with undetectable blood pressure within minutes of exposure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Anaphylactic shock is a severe, life-threatening allergic reaction causing breathing difficulties and shock.",
                "plain_analogy": "An all-out false alarm that sets off sprinkler flooding and structural blast doors throughout a building.",
                "lifestyle_action": "Always carry two Epinephrine auto-injectors at all times, use it immediately for throat swelling, and call 911."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Epinephrine IM (0.3-0.5 mg 1:1,000 - FIRST LINE)",
                    "0.9% Normal Saline IV bolus",
                    "Diphenhydramine (Benadryl) IV",
                    "Methylprednisolone IV"
                ],
                "dosing_gdmt": "Epinephrine 0.3-0.5 mg IM in anterolateral thigh, repeat every 5-15 min PRN; IV fluids 1-2 L rapid bolus.",
                "black_box_warning": "NEVER substitute antihistamines or steroids for epinephrine; delay in epinephrine is the #1 predictor of fatal anaphylaxis.",
                "organ_clearance_cutoffs": "No contraindications to epinephrine in a life-threatening anaphylactic emergency"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WAO-ANAPHYLAXIS",
                "pmid_or_doi": "10.1016/j.waojou.2020.100472",
                "cebm_level": 1,
                "sample_size": 5400,
                "endpoints": "Early intramuscular epinephrine administration within 30 minutes reduces biphasic reactions and hospital admissions by 76%."
            }
        }
    },
    {
        "id": "DOC-CARD-385",
        "icd10": "R65.21",
        "condition": "Septic Shock (Sepsis-3 Refractory Vasoplegia)",
        "specialty": "Critical Care & Infectious Disease",
        "organ_system": "Circulatory & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Surviving Sepsis Campaign Guidelines",
        "source_body": "Critical Care Medicine & Intensive Care Medicine",
        "citation": "Evans L et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit Care Med. 2021;49(11):e1063-e1143.",
        "doi_or_source": "10.1097/CCM.0000000000005337",
        "clinical_evidence": "The Hour-1 Sepsis Bundle (measure lactate, blood cultures prior to antibiotics, broad-spectrum IV antimicrobials within 1 hour, 30 mL/kg crystalloids for MAP <65 or lactate >=4, and Norepinephrine vasopressor) slashes in-hospital mortality from 46% to under 25% (p<0.001). Adding Vasopressin (0.03 units/min) reduces tachyarrhythmias and norepinephrine requirements.",
        "solution_protocol": {
            "non_pharmacological_targets": "Initiate broad-spectrum IV antimicrobials within 1 hour; infuse 30 mL/kg balanced crystalloids (Lactated Ringer's) within 3 hours; dynamic measures of fluid responsiveness (passive leg raise, stroke volume variation) rather than static CVP; source control within 6-12 hours.",
            "monitoring_cadence": "Arterial line continuous BP monitoring targeting MAP >=65 mmHg; serial blood lactate every 2-4 hours until clearance (<2.0 mmol/L).",
            "clinical_thresholds": "Persisting hypotension requiring vasopressors to maintain MAP >=65 mmHg AND serum lactate >2.0 mmol/L despite adequate fluid resuscitation."
        },
        "patient_plain_language": "Septic shock happens when a severe infection triggers an overwhelming body-wide inflammatory storm. Your blood vessels relax and dilate like leaky pipes, dropping blood pressure dangerously low so that vital organs (kidneys, liver, brain) starve of blood and oxygen.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are broad-spectrum antibiotics and 30 mL/kg IV fluids running within the first hour?",
            "safety_question": "Is Norepinephrine running via central line to keep my mean blood pressure above 65 mmHg?",
            "action_threshold_question": "Is my blood lactate dropping, confirming that my tissues are getting enough oxygen?"
        },
        "red_flags": [
            "Serum lactate >4.0 mmol/L with systolic BP <80 mmHg despite 3 liters of IV fluids",
            "Anuria (<0.3 mL/kg/h urine) and cold, mottled extremities indicating multi-organ failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Septic shock is life-threatening organ failure and dangerously low blood pressure caused by severe infection.",
                "plain_analogy": "A city-wide water pressure collapse caused by thousands of burst pipes all leaking at once.",
                "lifestyle_action": "Never ignore high fever with severe confusion, rapid breathing, and weakness; seek emergency ICU care immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Norepinephrine bitartrate (First-line vasopressor)",
                    "Vasopressin infusion",
                    "Hydrocortisone IV (for refractory shock)",
                    "Piperacillin/Tazobactam + Vancomycin"
                ],
                "dosing_gdmt": "Norepinephrine 0.05-0.5 mcg/kg/min titrated to MAP >=65; Vasopressin fixed at 0.03 units/min; Hydrocortisone 200 mg/day.",
                "black_box_warning": "Vasopressors through peripheral lines carry extravasation tissue necrosis risk; transition to central line.",
                "organ_clearance_cutoffs": "Intensive ICU multi-organ monitoring"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SSC-GUIDELINES",
                "pmid_or_doi": "10.1097/CCM.0000000000005337",
                "cebm_level": 1,
                "sample_size": 8500,
                "endpoints": "Hour-1 bundle compliance reduces sepsis mortality by over 40% in international multicenter cohorts."
            }
        }
    },
    {
        "id": "DOC-CARD-386",
        "icd10": "L03.90",
        "condition": "Acute Cellulitis & Erysipelas (Group A Streptococcus)",
        "specialty": "Dermatology & Infectious Disease",
        "organ_system": "Integumentary & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Practice Guidelines for SSTIs",
        "source_body": "Clinical Infectious Diseases",
        "citation": "Stevens DL et al. Practice Guidelines for the Diagnosis and Management of Skin and Soft Tissue Infections: 2014 Update by the IDSA. Clin Infect Dis. 2014;59(2):e10-e52.",
        "doi_or_source": "10.1093/cid/ciu296",
        "clinical_evidence": "In non-purulent acute cellulitis (predominantly beta-hemolytic Streptococcus, 73%), targeted oral beta-lactam monotherapy (Cephalexin 500 mg QID or Amoxicillin 500 mg TID for 5-7 days) achieves 96% clinical cure, proving that routine coverage for MRSA is unnecessary and increases broad-spectrum resistance without clinical benefit.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict leg elevation (elevate affected limb above heart level for at least 30 min 3-4 times daily; speeds resolution by reducing dependent lymphatic pooling); mark leading edge with surgical pen to track progression; treat predisposing tinea pedis (athlete's foot) to eliminate bacterial entry portals.",
            "monitoring_cadence": "Inspect demarcated redness border at 24 and 48 hours; check for regional lymphangitis.",
            "clinical_thresholds": "Spreading erythema, warmth, edema, and tenderness without fluctuant purulence defines non-purulent cellulitis."
        },
        "patient_plain_language": "Cellulitis is a bacterial infection of the deep layers of your skin, most commonly on the lower leg. Bacteria enter through a tiny scratch, dry crack, or athlete's foot. The skin becomes bright red, swollen, warm, and tender to the touch like a painful sunburn that slowly spreads.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the doctor draw an ink line around the red border to track whether it is shrinking with antibiotics?",
            "safety_question": "Can this non-purulent cellulitis be treated with standard Cephalexin pills without heavy MRSA drugs?",
            "action_threshold_question": "Why is keeping my leg propped up on pillows above heart level so vital for my healing?"
        },
        "red_flags": [
            "Rapidly spreading redness advancing >2 cm per hour with blistering or extreme pain out of proportion (warning of Necrotizing Fasciitis)",
            "High fever with chills and low blood pressure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cellulitis is a bacterial skin infection causing spreading redness, warmth, swelling, and pain.",
                "plain_analogy": "A localized grass fire spreading steadily across a field of dry brush.",
                "lifestyle_action": "Elevate your swollen leg on pillows, keep the skin clean and moisturized, and complete all antibiotic pills."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cephalexin (Keflex)",
                    "Cefazolin IV",
                    "Amoxicillin",
                    "Trimethoprim/Sulfamethoxazole (if purulent/MRSA)"
                ],
                "dosing_gdmt": "Cephalexin 500 mg orally QID x 5-7 days; Cefazolin 1-2 g IV q8h for hospitalized patients.",
                "black_box_warning": "Penicillin/cephalosporin allergy warrants clindamycin or vancomycin.",
                "organ_clearance_cutoffs": "Dose reduction of cephalexin in severe renal impairment"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "IDSA-SSTI",
                "pmid_or_doi": "10.1093/cid/ciu296",
                "cebm_level": 1,
                "sample_size": 4100,
                "endpoints": "5-7 days of targeted beta-lactam therapy achieves 96% cure in non-purulent cellulitis with leg elevation."
            }
        }
    },
    {
        "id": "DOC-CARD-387",
        "icd10": "I87.2",
        "condition": "Stasis Dermatitis (Venous Incompetence & Hemosiderin)",
        "specialty": "Dermatology & Vascular",
        "organ_system": "Integumentary & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & SVS/AVF Guidelines",
        "source_body": "Journal of Vascular Surgery",
        "citation": "O'Donnell TF et al. Management of Venous Leg Ulcers: Clinical Practice Guidelines of the Society for Vascular Surgery and American Venous Forum. J Vasc Surg. 2014;60(2_suppl):3S-59S.",
        "doi_or_source": "10.1016/j.jvs.2014.04.049",
        "clinical_evidence": "Stasis dermatitis is a chronic non-infectious inflammatory dermatosis caused by ambulatory venous hypertension. Antibiotics are completely ineffective and contribute to high rates of contact dermatitis. Graduated compression therapy (20-30 mmHg stockings) combined with mid-potency topical corticosteroids (Triamcinolone 0.1% ointment) resolves inflammation and reduces venous ulcer recurrence by 56% (RR 0.44; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily use of 20-30 mmHg graduated compression stockings (apply first thing in the morning); elevate legs above heart level whenever sitting; thick bland emollients (petrolatum/ceramides) applied immediately after bathing; avoid topical neomycin/bacitracin (high sensitization risk).",
            "monitoring_cadence": "Duplex venous ultrasound to assess superficial and deep venous reflux; inspect for shallow malleolar ulcers.",
            "clinical_thresholds": "Bilateral symmetric lower extremity erythema, brown hemosiderin staining, pitting edema, and dry eczematous skin in a patient with chronic venous insufficiency."
        },
        "patient_plain_language": "Stasis dermatitis is a common condition that is frequently mistaken for an infection (cellulitis). Weak valves in your leg veins let blood pool in your lower legs. The sluggish pressure forces tiny drops of blood into the skin, leaving rust-colored brown stains (hemosiderin) and red, itchy, flaky skin on both shins.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the fact that both my legs are red and brown prove this is venous stasis rather than an infection?",
            "safety_question": "Why should I avoid antibiotic creams and pills that could cause allergic contact dermatitis?",
            "action_threshold_question": "What strength compression stockings (like 20-30 mmHg) will keep the fluid from pooling in my lower legs?"
        },
        "red_flags": [
            "Development of an open, painful wound on the inner ankle (Venous Stasis Ulcer)",
            "Sudden unilateral swelling, warmth, and calf pain concerning for Deep Vein Thrombosis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Stasis dermatitis is chronic skin inflammation and brown discoloration caused by poor vein circulation in the legs.",
                "plain_analogy": "Water pooling at the base of a foundation wall, causing the exterior paint to peel and rust.",
                "lifestyle_action": "Wear graduated compression socks every day, elevate your legs when sitting, and apply thick moisturizers."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Triamcinolone acetonide 0.1% ointment",
                    "Graduated Compression Stockings (20-30 mmHg)",
                    "Petrolatum emollient"
                ],
                "dosing_gdmt": "Triamcinolone 0.1% ointment applied BID for 1-2 weeks during inflammatory flares; daily compression.",
                "black_box_warning": "Oral antibiotics are NOT indicated for stasis dermatitis and cause severe drug resistance/sensitization.",
                "organ_clearance_cutoffs": "Topical therapy has zero systemic clearance restrictions"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SVS-VENOUS",
                "pmid_or_doi": "10.1016/j.jvs.2014.04.049",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "Graduated compression therapy resolves stasis dermatitis and reduces ulcer recurrence by 56% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-388",
        "icd10": "M72.6",
        "condition": "Necrotizing Fasciitis (Flesh-Eating Surgical Emergency)",
        "specialty": "General Surgery & Infectious Disease",
        "organ_system": "Integumentary & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WSES Guidelines on Soft Tissue Infections",
        "source_body": "World Journal of Emergency Surgery",
        "citation": "Sartelli M et al. 2018 WSES/SIS-E Consensus Conference: Recommendations for the Management of Severe Skin and Soft-Tissue Infections. World J Emerg Surg. 2018;13:58.",
        "doi_or_source": "10.1186/s13017-018-0219-9",
        "clinical_evidence": "Immediate surgical fasciotomy with wide radical operative debridement within 12 hours of presentation slashes mortality from >70% to under 15% (p<0.001). Triple broad-spectrum antimicrobial therapy (Meropenem 1 g q8h + Vancomycin 15-20 mg/kg + Clindamycin 900 mg q8h for toxin suppression) halts bacterial exotoxin synthesis.",
        "solution_protocol": {
            "non_pharmacological_targets": "DO NOT DELAY SURGICAL EXPLORATION FOR IMAGING OR LABS; emergent operative exploration (the 'finger test' revealing dishwater fluid and lack of tissue resistance); second-look debridement mandatory within 24 hours.",
            "monitoring_cadence": "LRINEC (Laboratory Risk Indicator for Necrotizing Fasciitis) score >=6 indicates high risk; intensive ICU hemodynamic monitoring.",
            "clinical_thresholds": "Hallmark triad: 'Pain completely out of proportion to skin appearance', rapid tracking erythema, skin bullae/necrosis, and wooden-hard induration."
        },
        "patient_plain_language": "Necrotizing fasciitis (flesh-eating infection) is a catastrophic surgical emergency. Fast-moving bacteria travel along the deep tissue sheets (fascia) beneath the skin, releasing toxins that kill blood vessels and rot tissue. Pain is blindingly excruciating even when the surface skin only looks mildly red.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is an emergency surgeon scrubbed and taking the patient directly to the operating room for surgical tissue debridement?",
            "safety_question": "Is high-dose IV Clindamycin running to turn off the bacteria's poison toxin production?",
            "action_threshold_question": "When is the mandatory 'second-look' surgery scheduled within 24 hours to check for clean margins?"
        },
        "red_flags": [
            "Blinding pain out of proportion with grey skin bullae and crepitus (crackling air in tissues)",
            "Septic shock with sudden numbness in the painful skin (indicating cutaneous nerve death)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Necrotizing fasciitis is a rapid, life-threatening infection of deep tissues requiring emergency surgery to remove dead flesh.",
                "plain_analogy": "A fast-burning fire traveling silently behind the drywall of a house before smoke appears on the surface.",
                "lifestyle_action": "Never ignore extreme agonizing skin pain that feels far worse than the skin looks; call 911 immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Radical Surgical Debridement (Primary - Life-Saving)",
                    "Clindamycin IV (toxin-suppression)",
                    "Meropenem IV",
                    "Vancomycin IV"
                ],
                "dosing_gdmt": "Meropenem 1 g IV q8h + Vancomycin 15-20 mg/kg q12h + Clindamycin 900 mg IV q8h (blocks Strep exotoxin).",
                "black_box_warning": "Antibiotics without emergent surgical debridement carry 100% mortality.",
                "organ_clearance_cutoffs": "Intensive ICU resuscitation; renal replacement therapy for septic AKI"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WSES-NECFASC",
                "pmid_or_doi": "10.1186/s13017-018-0219-9",
                "cebm_level": 1,
                "sample_size": 1420,
                "endpoints": "Emergent surgical debridement within 12 hours reduces necrotizing fasciitis mortality from 70% to 15% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-389",
        "icd10": "A48.3",
        "condition": "Staphylococcal Toxic Shock Syndrome (TSS Toxin-1)",
        "specialty": "Infectious Disease & Critical Care",
        "organ_system": "Infectious & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CDC Clinical Criteria & IDSA Guidance",
        "source_body": "Clinical Infectious Diseases",
        "citation": "Chuang YY et al. Toxic Shock Syndrome in Children and Adults. Clin Infect Dis. 2005;40(8):1202-1205.",
        "doi_or_source": "10.1086/428731",
        "clinical_evidence": "TSS is driven by bacterial superantigens (TSST-1 or enterotoxins) that cross-link MHC Class II and T-cell receptors, triggering a massive cytokine storm. Clindamycin (900 mg IV q8h) suppresses bacterial protein exotoxin synthesis by >95%, significantly outperforming standard cell-wall beta-lactams alone. Intravenous Immunoglobulin (IVIG 1-2 g/kg) neutralizes circulating superantigens.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate source control: remove tampons, nasal packings, surgical wound packings; inspect all surgical incisions (even benign-appearing wounds can harbor TSST-1 producers); aggressive crystalloid resuscitation (often requires 6-10 L in 24h).",
            "monitoring_cadence": "Continuous arterial line BP and cardiac telemetry; serial liver and renal profiles; full body skin inspection for desquamation.",
            "clinical_thresholds": "Five mandatory criteria: fever >38.9 C, diffuse macular erythroderma ('sunburn rash'), hypotension (SBP <90 mmHg), multisystem involvement (>=3 organ systems), and late desquamation (1-2 weeks on palms/soles)."
        },
        "patient_plain_language": "Toxic shock syndrome is an overwhelming immune reaction to a toxin produced by common Staph bacteria (often associated with high-absorbency tampons or wound packings). The toxin supercharges your immune cells, causing a sudden high fever, widespread sunburn-like skin rash, vomiting, and a dangerous drop in blood pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have all potential sources (tampons, nasal packing, surgical dressings) been removed and cultured?",
            "safety_question": "Is IV Clindamycin running to shut down the bacteria's toxin-manufacturing machinery?",
            "action_threshold_question": "Are we giving IVIG (antibodies) to neutralize the circulating superantigen toxins?"
        },
        "red_flags": [
            "Sudden high fever with a red sunburn-like rash covering the whole body and blood pressure collapse",
            "Confusion with peeling skin on palms and soles"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Toxic shock syndrome is a severe bacterial illness caused by superantigen toxins, leading to shock and skin peeling.",
                "plain_analogy": "A supercharged electrical short that trips every alarm and circuit breaker in the entire facility.",
                "lifestyle_action": "Change tampons every 4-8 hours, keep surgical wounds clean, and seek immediate emergency care for sudden high fever and rash."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Clindamycin IV (Toxin suppressor)",
                    "Vancomycin IV or Cefazolin IV",
                    "Intravenous Immunoglobulin (IVIG)"
                ],
                "dosing_gdmt": "Clindamycin 900 mg IV q8h + Vancomycin 15-20 mg/kg q12h; IVIG 1 g/kg on day 1, then 0.5 g/kg on days 2-3.",
                "black_box_warning": "Clindamycin is bacteriostatic; combine with bactericidal agent (vancomycin or cefazolin).",
                "organ_clearance_cutoffs": "Intensive ICU fluid resuscitation for massive capillary leak"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CDC-TSS",
                "pmid_or_doi": "10.1086/428731",
                "cebm_level": 1,
                "sample_size": 980,
                "endpoints": "Adding Clindamycin to neutralize superantigen synthesis reduces toxic shock mortality from 30% to under 8%."
            }
        }
    },
    {
        "id": "DOC-CARD-390",
        "icd10": "L51.2",
        "condition": "Stevens-Johnson Syndrome & Toxic Epidermal Necrolysis (SJS/TEN)",
        "specialty": "Dermatology & Critical Care",
        "organ_system": "Integumentary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: British Association of Dermatologists Guidelines",
        "source_body": "British Journal of Dermatology",
        "citation": "Creamer D et al. UK Guidelines for the Management of Stevens-Johnson Syndrome/Toxic Epidermal Necrolysis in Adults. Br J Dermatol. 2016;174(6):1194-1227.",
        "doi_or_source": "10.1111/bjd.14530",
        "clinical_evidence": "IMMEDIATE CESSATION OF ALL INCITING MEDICATIONS (allopurinol, carbamazepine, lamotrigine, sulfonamides, nevirapine, NSAIDs) and transfer to an accredited Burn ICU slashes mortality by 60%. Cyclosporine (3-5 mg/kg/day) or Etanercept (50 mg SC single dose) halts Fas-FasL mediated keratinocyte apoptosis, reducing epidermal detachment and mortality (p=0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Transfer immediately to a specialized Burn Intensive Care Unit; strict reverse isolation (wound care identical to major second-degree thermal burns); daily amniotic membrane ophthalmology care to prevent blinding symblepharon scarring; avoid skin debridement (keep detached epidermis as biological dressing).",
            "monitoring_cadence": "SCORTEN mortality risk score calculated on days 1 and 3; daily mapping of epidermal detachment percentage (% BSA with positive Nikolsky sign).",
            "clinical_thresholds": "SJS: <10% BSA detachment; SJS/TEN overlap: 10-30% BSA; TEN: >30% BSA detachment with hemorrhagic mucosal involvement (eyes, mouth, genitalia)."
        },
        "patient_plain_language": "SJS and TEN are life-threatening allergic reactions to medications where your body attacks its own skin and mucous membranes. The top layer of your skin blisters, dies, and peels off in huge sheets like severe second-degree scald burns. Raw painful sores develop inside your mouth, lips, eyes, and genital areas.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has the culprit medication been permanently identified and red-flagged in my electronic health record?",
            "safety_question": "Am I being transferred to a specialized burn center for gentle biological dressings and pain control?",
            "action_threshold_question": "Has an eye specialist (ophthalmologist) evaluated my eyes daily to prevent scarring and vision loss?"
        },
        "red_flags": [
            "Skin peeling off in sheets with light rubbing (positive Nikolsky sign) covering >10% of body",
            "Bleeding crusted lips with severe eye pain and inability to swallow"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "SJS/TEN is a severe, life-threatening drug reaction causing widespread blistering and peeling of skin and mucous membranes.",
                "plain_analogy": "A severe chemical peel reaction where the skin's surface wallpaper completely separates from the drywall underneath.",
                "lifestyle_action": "Never take a medication that previously caused hives or mouth sores; carry an allergy passport at all times."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cyclosporine IV/oral",
                    "Etanercept (Enbrel)",
                    "High-potency Ophthalmic Lubricants / Amniotic membrane"
                ],
                "dosing_gdmt": "Cyclosporine 3-5 mg/kg/day divided BID x 10 days, then tapered; or Etanercept 50 mg SC once.",
                "black_box_warning": "Corticosteroids are controversial in late TEN due to elevated sepsis risk; avoid silver sulfadiazine.",
                "organ_clearance_cutoffs": "Burn ICU supportive care with careful fluid and electrolyte management"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BAD-SJSTEN",
                "pmid_or_doi": "10.1111/bjd.14530",
                "cebm_level": 1,
                "sample_size": 1250,
                "endpoints": "Early transfer to Burn ICU plus targeted Cyclosporine/Etanercept lowers SJS/TEN mortality by over 50%."
            }
        }
    },
    {
        "id": "DOC-CARD-391",
        "icd10": "D72.110",
        "condition": "DRESS Syndrome (Drug Reaction with Eosinophilia and Systemic Symptoms)",
        "specialty": "Dermatology & Allergy",
        "organ_system": "Integumentary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: RegiSCAR Consensus Criteria",
        "source_body": "British Journal of Dermatology",
        "citation": "Kardaun SH et al. The European Registry of Severe Cutaneous Adverse Reactions (RegiSCAR): DRESS Validation. Br J Dermatol. 2013;169(5):1071-1080.",
        "doi_or_source": "10.1111/bjd.12579",
        "clinical_evidence": "Systemic Corticosteroids (Prednisone 0.5-1.0 mg/kg/day tapered slowly over 8-12 weeks) are the gold standard, reversing life-threatening visceral organ involvement (interstitial nephritis, acute hepatitis, myocarditis) in 85% of cases. Rapid tapering (<4-6 weeks) triggers severe autoimmune flares and HHV-6 viral reactivation.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATELY STOP INCITING DRUG (aromatic anticonvulsants, allopurinol, sulfasalazine, vancomycin, minocycline); monitor liver and renal function; screening for HHV-6 and CMV viral reactivation; screen for late-onset autoimmune thyroiditis (Hashimoto's) at 6-12 months.",
            "monitoring_cadence": "Weekly liver function tests (ALT/AST), creatinine, CBC with differential (absolute eosinophil count); serial ECG and troponin for silent myocarditis.",
            "clinical_thresholds": "RegiSCAR criteria: Delayed onset (2-8 weeks after drug initiation), fever >38.5 C, facial edema + morbilliform rash, atypical lymphocytosis or eosinophilia (>=700/mcL), and internal organ involvement (>=1 organ)."
        },
        "patient_plain_language": "DRESS syndrome is a delayed, severe allergy to a medication that strikes 2 to 8 weeks after starting the pill. It causes a high fever, severe facial swelling, an itchy red rash covering the whole body, and high levels of allergic allergy cells (eosinophils) that inflame internal organs like the liver, heart, and kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has the offending medication (started 2 to 8 weeks ago) been identified and permanently stopped?",
            "safety_question": "Are we testing my liver enzymes, kidney function, and heart troponin for internal organ inflammation?",
            "action_threshold_question": "Why must my steroid medication (Prednisone) be tapered very slowly over 2 to 3 months to prevent a rebound flare?"
        },
        "red_flags": [
            "Severe chest pain or shortness of breath (acute hypersensitivity myocarditis - high mortality risk)",
            "Jaundice with rapidly climbing liver enzymes (acute liver failure)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "DRESS syndrome is a delayed, dangerous drug allergy causing high fever, facial swelling, rash, and internal organ damage.",
                "plain_analogy": "A time-bomb drug reaction that explodes weeks after starting a pill, damaging liver and kidney filters.",
                "lifestyle_action": "Always report a spreading rash with fever that develops weeks after starting a new prescription medicine."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral / Methylprednisolone IV",
                    "Topical Corticosteroids",
                    "IVIG (if refractory)"
                ],
                "dosing_gdmt": "Prednisone 1 mg/kg/day until clinical improvement, then very slow taper over minimum 8-12 weeks.",
                "black_box_warning": "Do NOT taper steroids rapidly (<4 weeks) as this triggers severe visceral relapse and HHV-6 reactivation.",
                "organ_clearance_cutoffs": "Adjust dosing in hepatic impairment; monitor for steroid-induced hyperglycemia"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "RegiSCAR-DRESS",
                "pmid_or_doi": "10.1111/bjd.12579",
                "cebm_level": 1,
                "sample_size": 1180,
                "endpoints": "Slow-taper systemic corticosteroid protocol resolves visceral organ failure in 85% of DRESS patients."
            }
        }
    },
    {
        "id": "DOC-CARD-392",
        "icd10": "T79.A1XA",
        "condition": "Acute Compartment Syndrome (Traumatic Limb Ischemia)",
        "specialty": "Orthopedics & Emergency Medicine",
        "organ_system": "Musculoskeletal & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAOS Clinical Practice Guideline",
        "source_body": "Journal of the American Academy of Orthopaedic Surgeons",
        "citation": "American Academy of Orthopaedic Surgeons. Management of Acute Compartment Syndrome: Clinical Practice Guideline. J Am Acad Orthop Surg. 2019;27(12):e577-e582.",
        "doi_or_source": "10.5435/JAAOS-D-19-00165",
        "clinical_evidence": "Emergent surgical fasciotomy (complete release of all anatomic compartments, e.g., 4-compartment fasciotomy for lower leg) within 6 hours of onset salvages functional limb viability in >90% of patients, reducing amputation and permanent Volkmann contracture from 45% to <4% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "REMOVE ALL CIRCULAR CASTS, SPLINTS, AND CONSTRICTIVE BANDAGES DOWN TO BARE SKIN IMMEDIATELY (reduces intracompartmental pressure by 50-85%); position limb AT HEART LEVEL (do NOT elevate, as elevation lowers perfusion pressure); emergency orthopedic surgery consultation.",
            "monitoring_cadence": "Serial compartment pressure measurements with Stryker needle; monitor for myoglobinuric acute kidney injury.",
            "clinical_thresholds": "Delta pressure (Diastolic BP minus Intracompartmental Pressure) <=30 mmHg is the definitive diagnostic threshold for emergency fasciotomy."
        },
        "patient_plain_language": "Compartment syndrome is a surgical emergency that happens after a broken bone or crushing injury. Muscles are bundled inside tight, non-stretchable fibrous envelopes (compartments). Swelling or internal bleeding raises pressure inside the envelope so high that blood flow stops, suffocating muscle and nerve fibers within hours.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my measured compartment pressure and calculated delta pressure (Diastolic BP minus muscle pressure)?",
            "safety_question": "Have all casts, bandages, and splints been removed down to bare skin immediately?",
            "action_threshold_question": "Is an orthopedic surgeon ready to perform emergency keyhole incisions (fasciotomy) to release the pressure?"
        },
        "red_flags": [
            "Excruciating, unrelenting pain with passive stretching of toes or fingers (Earliest and most sensitive clinical sign)",
            "Loss of distal pulse and cold pale limb (Late finding signifying irreversible muscle death)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute compartment syndrome is dangerous pressure buildup inside a muscle bundle after injury that cuts off blood flow.",
                "plain_analogy": "An over-inflated tire inside a rigid metal safe, squeezing and crushing the delicate fuel lines inside.",
                "lifestyle_action": "Seek emergency orthopedic care immediately for severe swelling and pain after a fracture or crush injury."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Emergency Surgical Fasciotomy (First Line - Mandatory)",
                    "0.9% Normal Saline IV for myoglobinuria"
                ],
                "dosing_gdmt": "Complete surgical release of all fascial compartments; leave incisions open with wound VAC for delayed closure.",
                "black_box_warning": "Do NOT elevate the limb above the heart; keep at heart level to maintain perfusion gradient.",
                "organ_clearance_cutoffs": "Immediate surgery; drug therapy cannot relieve mechanical pressure"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAOS-COMPARTMENT",
                "pmid_or_doi": "10.5435/JAAOS-D-19-00165",
                "cebm_level": 1,
                "sample_size": 1350,
                "endpoints": "Fasciotomy performed within 6 hours prevents muscle necrosis and amputation in >90% of compartment syndromes."
            }
        }
    },
    {
        "id": "DOC-CARD-393",
        "icd10": "I82.409",
        "condition": "Deep Vein Thrombosis of Lower Extremity (DVT)",
        "specialty": "Hematology & Vascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CHEST Guideline on Antithrombotic Therapy",
        "source_body": "Chest",
        "citation": "Stevens SM et al. Antithrombotic Therapy for VTE Disease: CHEST Guideline and Expert Panel Report. Chest. 2021;160(6):e545-e608.",
        "doi_or_source": "10.1016/j.chest.2021.07.055",
        "clinical_evidence": "Direct Oral Anticoagulants (DOACs: Apixaban 10 mg BID x 7 days then 5 mg BID; or Rivaroxaban 15 mg BID x 21 days then 20 mg daily) are Level 1 preferred over Warfarin, achieving equivalent efficacy in preventing recurrent VTE while reducing major bleeding by 40% and intracranial hemorrhage by 65% (p<0.001) without requiring routine INR monitoring.",
        "solution_protocol": {
            "non_pharmacological_targets": "Early ambulation as tolerated once anticoagulated (bedrest is harmful and increases thrombus propagation); graduated compression stockings (20-30 mmHg) to prevent Post-Thrombotic Syndrome (PTS); identify and eliminate modifiable risk factors (estrogen pills, long flights).",
            "monitoring_cadence": "Complete duplex ultrasound of affected limb; repeat ultrasound at 3-6 months to establish baseline residual vein obstruction.",
            "clinical_thresholds": "Wells DVT score >=2 indicates DVT likely (mandates duplex ultrasound); Wells <2 with negative high-sensitivity D-dimer safely rules out DVT without imaging."
        },
        "patient_plain_language": "A blood clot forms inside the deep veins of your calf or thigh. It blocks blood from flowing smoothly back to your heart, causing painful swelling, warmth, and heaviness in one leg. The greatest danger is that a piece of the clot can break loose and travel to your lungs, causing a life-threatening pulmonary embolism.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were my venous ultrasound results, and does the clot involve the thigh (proximal) or calf (distal)?",
            "safety_question": "Will I take an oral blood-thinner pill (like Eliquis or Xarelto) without needing weekly blood tests?",
            "action_threshold_question": "How long must I take the blood thinner (typically 3 to 6 months for a first clot)?"
        },
        "red_flags": [
            "Sudden shortness of breath, chest pain when breathing in, or coughing up blood (Pulmonary Embolism - Call 911)",
            "Severe swelling with blue, cold foot (Phlegmasia Cerulea Dolens - Limb-Threatening Emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Deep vein thrombosis is a blood clot inside deep leg veins causing painful swelling and risk of lung clots.",
                "plain_analogy": "A heavy roadblock inside a major underground drainage pipe, causing sewage water to back up and swell the street.",
                "lifestyle_action": "Walk regularly, take your prescribed blood-thinner pills every day, and avoid sitting motionless for hours."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Apixaban (Eliquis)",
                    "Rivaroxaban (Xarelto)",
                    "Enoxaparin (Lovenox) SC",
                    "Dabigatran (Pradaxa)"
                ],
                "dosing_gdmt": "Apixaban 10 mg orally BID x 7 days, then 5 mg BID x 3-6 months; or Rivaroxaban 15 mg BID x 21 days then 20 mg daily.",
                "black_box_warning": "DOACs: Major bleeding risk; do not miss doses due to short half-life.",
                "organ_clearance_cutoffs": "Apixaban dose reduction (2.5 mg BID) if age >=80, weight <=60 kg, or creatinine >=1.5 mg/dL"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CHEST-DVT",
                "pmid_or_doi": "10.1016/j.chest.2021.07.055",
                "cebm_level": 1,
                "sample_size": 8900,
                "endpoints": "DOAC therapy reduces major bleeding by 40% and intracranial hemorrhage by 65% compared to warfarin in acute DVT."
            }
        }
    },
    {
        "id": "DOC-CARD-394",
        "icd10": "M71.20",
        "condition": "Ruptured Baker's Popliteal Cyst (Pseudothrombophlebitis)",
        "specialty": "Orthopedics & Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & Ultrasound Criteria",
        "source_body": "Arthritis Care & Research",
        "citation": "Handy JR. Popliteal Cysts in Adults: A Review. Semin Arthritis Rheum. 2001;31(2):108-118.",
        "doi_or_source": "10.1053/sarh.2001.27659",
        "clinical_evidence": "Rupture of a popliteal (Baker's) cyst releases inflammatory synovial fluid into the gastrocnemius-soleus intermuscular plane, perfectly mimicking acute deep vein thrombosis (pseudothrombophlebitis). Lower extremity duplex ultrasound showing a non-occluded compressible popliteal vein and extravasated fluid in the calf muscle bellies rules out DVT, preventing unnecessary and dangerous anticoagulation.",
        "solution_protocol": {
            "non_pharmacological_targets": "RICE protocol (Rest, Ice wrapped in towels, Compression wrap, Limb Elevation); intra-articular knee corticosteroid injection (Triamcinolone 40 mg) to treat underlying knee osteoarthritis or meniscal tear; avoid anticoagulants.",
            "monitoring_cadence": "Duplex ultrasound to confirm patent deep venous system; recheck calf swelling at 1 week.",
            "clinical_thresholds": "Presence of the 'crescent sign' (crescentic bruising/ecchymosis beneath the lateral or medial malleolus) with ultrasound confirming ruptured cyst."
        },
        "patient_plain_language": "A Baker's cyst is a fluid-filled sac behind your knee caused by arthritis or cartilage tears. If the sac pops, the fluid spills down into your calf muscle. It causes sudden, severe calf pain, swelling, and redness that looks and feels exactly like a dangerous blood clot (DVT). An ultrasound quickly proves the vein is open and the fluid is outside the vein.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my leg ultrasound confirm my veins are completely clear of blood clots?",
            "safety_question": "Does the bruising around my ankle (crescent sign) confirm the knee cyst popped?",
            "action_threshold_question": "Will a cortisone injection into my knee joint stop fluid from filling the cyst again?"
        },
        "red_flags": [
            "Unable to rule out DVT without a venous duplex ultrasound (mandatory to prevent pulmonary embolism)",
            "Severe calf swelling with sensory loss or pale cold foot"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A ruptured Baker's cyst is fluid leaking from a knee joint into the calf muscle, mimicking a blood clot.",
                "plain_analogy": "A water balloon bursting behind the knee hinge and draining water down into the calf boot.",
                "lifestyle_action": "Rest with your leg propped up on pillows, apply ice packs wrapped in towels, and treat the underlying knee joint arthritis."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Triamcinolone acetonide intra-articular",
                    "Acetaminophen / Ibuprofen",
                    "Supportive compression sleeve"
                ],
                "dosing_gdmt": "Intra-articular knee injection of Triamcinolone 40 mg; oral analgesics as needed.",
                "black_box_warning": "Anticoagulants are NOT indicated and can cause intramuscular hematoma if mistakenly prescribed.",
                "organ_clearance_cutoffs": "Safe across renal ranges for intra-articular therapies"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BAKER-ULTRASOUND",
                "pmid_or_doi": "10.1053/sarh.2001.27659",
                "cebm_level": 1,
                "sample_size": 1100,
                "endpoints": "Bedside ultrasound differentiates ruptured Baker's cyst from DVT with 100% diagnostic accuracy."
            }
        }
    },
    {
        "id": "DOC-CARD-395",
        "icd10": "K85.90",
        "condition": "Acute Pancreatitis (Atlanta Criteria / Lipase >3x ULN)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline & WATERFALL Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "de-Madaria E et al. Aggressive versus Moderate Fluid Resuscitation in Acute Pancreatitis (WATERFALL). N Engl J Med. 2022;387(11):989-1000.",
        "doi_or_source": "10.1056/NEJMoa2202884",
        "clinical_evidence": "The landmark WATERFALL multicenter randomized trial (n=249 patients) proved that MODERATE fluid resuscitation with Lactated Ringer's (1.5 mL/kg/h without bolus, or 10 mL/kg bolus only if hypovolemic) was superior to aggressive hydration (20 mL/kg bolus + 3 mL/kg/h), reducing fluid overload by 3-fold (20.5% vs 6.3%; p=0.004) without compromising clinical outcomes. Early oral feeding (within 24 hours) reduces hospital stay.",
        "solution_protocol": {
            "non_pharmacological_targets": "Goal-directed moderate fluid resuscitation with Lactated Ringer's; early oral feeding with low-fat solid or liquid diet as tolerated; multimodal analgesia (avoid routine Demerol); urgent ERCP within 24 hours only if concurrent acute cholangitis.",
            "monitoring_cadence": "Monitor hematocrit, BUN, creatinine, and urine output every 12 hours; systemic inflammatory response syndrome (SIRS) scoring.",
            "clinical_thresholds": "Diagnosis requires 2 of 3: epigastric pain radiating to back, serum lipase/amylase >3x ULN, and characteristic findings on CT/MRI or ultrasound."
        },
        "patient_plain_language": "Acute pancreatitis is sudden inflammation of your pancreas (most commonly caused by gallstones or heavy alcohol). Digestive enzymes that normally break down food in your intestines get activated prematurely inside the pancreas itself, literally starting to digest the gland from the inside out, causing severe boring stomach pain radiating to your back.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my lipase level and did my ultrasound show gallstones in my gallbladder?",
            "safety_question": "Are we giving gentle IV fluids (Lactated Ringer's) while carefully monitoring to avoid fluid overload in my lungs?",
            "action_threshold_question": "Can I start sipping liquids and eating low-fat foods as soon as my nausea and pain improve?"
        },
        "red_flags": [
            "Severe persistent vomiting, low blood pressure, and dark bruised flanks (Grey Turner / Cullen sign)",
            "Shortness of breath indicating Acute Respiratory Distress Syndrome (ARDS)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute pancreatitis is sudden, severe inflammation of the pancreas causing intense upper belly pain radiating to the back.",
                "plain_analogy": "A chemical factory whose caustic cleaning chemicals leak and begin dissolving the factory walls.",
                "lifestyle_action": "Drink plenty of water, strictly avoid all alcohol and smoking, and eat low-fat meals."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lactated Ringer's IV (Goal-directed moderate)",
                    "Multimodal IV analgesia (Hydromorphone/Acetaminophen)"
                ],
                "dosing_gdmt": "Lactated Ringer's 1.5 mL/kg/h adjusted based on hematocrit and BUN; early oral diet within 24h.",
                "black_box_warning": "Prophylactic antibiotics are NOT recommended in acute pancreatitis (do not prevent infected necrosis).",
                "organ_clearance_cutoffs": "Adjust fluid rates in heart failure or end-stage renal disease"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WATERFALL",
                "pmid_or_doi": "10.1056/NEJMoa2202884",
                "cebm_level": 2,
                "sample_size": 249,
                "endpoints": "Moderate fluid resuscitation slashes fluid overload by 3-fold without increasing necrotizing pancreatitis."
            }
        }
    },
    {
        "id": "DOC-CARD-396",
        "icd10": "K63.1",
        "condition": "Perforated Viscus & Pneumoperitoneum (Rigid Abdomen)",
        "specialty": "General Surgery & Emergency Medicine",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WSES Guidelines on Peritonitis",
        "source_body": "World Journal of Emergency Surgery",
        "citation": "Sartelli M et al. 2016 WSES Guidelines on Intra-Abdominal Infections. World J Emerg Surg. 2016;11:33.",
        "doi_or_source": "10.1186/s13017-016-0089-y",
        "clinical_evidence": "Emergent exploratory laparotomy or laparoscopy for source control (ulcer repair with Graham omental patch, bowel resection, or Hartmann procedure) and extensive peritoneal lavage within 6-12 hours of perforation reduces septic shock mortality from >60% to under 15% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "STRICT NPO; wide-bore nasogastric tube decompression; aggressive IV crystalloid resuscitation; broad-spectrum IV antibiotics covering enterics and anaerobes (Piperacillin/Tazobactam 4.5 g q6h); emergency surgery consultation.",
            "monitoring_cadence": "Continuous arterial line BP and hourly urine output; serial lactate and blood gases.",
            "clinical_thresholds": "Upright chest X-ray or non-contrast abdominal CT showing subdiaphragmatic free air (pneumoperitoneum) with board-like involuntary abdominal guarding."
        },
        "patient_plain_language": "A hole has burst completely open in the wall of your stomach or intestines (often from a deep bleeding ulcer, diverticulitis, or trauma). Stomach acid, food, and millions of bacteria leak directly into your sterile abdominal cavity, triggering intense peritonitis where your belly muscles freeze rock-hard like a wooden board.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my upright chest X-ray show free air bubbles trapped beneath my diaphragm?",
            "safety_question": "Is the surgical team ready for emergency exploratory surgery to wash out my belly and patch the hole?",
            "action_threshold_question": "Are broad-spectrum IV antibiotics infusing to prevent overwhelming septic shock?"
        },
        "red_flags": [
            "Sudden agonizing belly pain where the stomach becomes rigid as a stone board (Involuntary Guarding)",
            "Septic shock with crashing blood pressure and rapid shallow breathing"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Perforated viscus is a hole in the stomach or bowel leaking digestive contents into the belly cavity, requiring emergency surgery.",
                "plain_analogy": "A hole blown through the side of an engine boiler, venting boiling acid and steam into the passenger cabin.",
                "lifestyle_action": "Never eat or drink anything if sudden agonizing belly pain strikes; seek immediate trauma/emergency surgical care."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Emergency Surgical Repair (Graham patch / Resection)",
                    "Piperacillin/Tazobactam IV (Zosyn)",
                    "Vancomycin IV"
                ],
                "dosing_gdmt": "Zosyn 4.5 g IV q6h + Vancomycin 15-20 mg/kg q12h; IV crystalloid resuscitation.",
                "black_box_warning": "Immediate surgical source control is mandatory; antibiotics alone carry near 100% mortality.",
                "organ_clearance_cutoffs": "Renal dose adjustment for antibiotics in septic acute kidney injury"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WSES-PERITONITIS",
                "pmid_or_doi": "10.1186/s13017-016-0089-y",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Surgical source control within 12 hours reduces peritonitis mortality from >60% to 15%."
            }
        }
    },
    {
        "id": "DOC-CARD-397",
        "icd10": "K83.09",
        "condition": "Acute Ascending Cholangitis (Charcot's Triad & Sepsis)",
        "specialty": "Gastroenterology & General Surgery",
        "organ_system": "Digestive & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Tokyo Guidelines 2018 (TG18)",
        "source_body": "Journal of Hepato-Biliary-Pancreatic Sciences",
        "citation": "Kiriyama S et al. Tokyo Guidelines 2018: Diagnostic Criteria and Severity Assessment of Acute Cholangitis. J Hepatobiliary Pancreat Sci. 2018;25(1):17-30.",
        "doi_or_source": "10.1002/jhbp.512",
        "clinical_evidence": "Emergent biliary decompression via Endoscopic Retrograde Cholangiopancreatography (ERCP with sphincterotomy and stent placement within 24 hours for moderate/severe cholangitis) reduces mortality from >80% to under 8% (p<0.001). Broad-spectrum IV antibiotics (Ceftriaxone + Metronidazole or Piperacillin/Tazobactam) treat biliary bacteremia.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate hospital admission; NPO; aggressive IV crystalloid resuscitation; emergent gastroenterology consultation for ERCP biliary decompression; correct coagulopathy with vitamin K/FFP prior to sphincterotomy.",
            "monitoring_cadence": "Continuous vitals monitoring in ICU; serial bilirubin, liver enzymes, CBC, and lactate every 12 hours.",
            "clinical_thresholds": "Charcot's Triad (fever, jaundice, right upper quadrant pain) or Reynolds' Pentad (+ hypotension and altered mental status) confirms life-threatening suppurative cholangitis."
        },
        "patient_plain_language": "Acute cholangitis is a severe, life-threatening infection of the bile duct pipes draining your liver. A gallstone blocks the main pipe, trapping bile. Bacteria multiply rapidly in the stagnant pool under extreme pressure, leaking bacteria and toxins directly into your bloodstream, causing high fevers, yellow jaundice, and severe upper right belly pain.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is an emergency ERCP endoscopy scheduled within 24 hours to pull out the obstructing gallstone and drain the pus?",
            "safety_question": "What are my bilirubin and white blood cell levels?",
            "action_threshold_question": "Are broad-spectrum IV antibiotics running to clear the infection from my bloodstream?"
        },
        "red_flags": [
            "Fever, yellow skin/eyes, belly pain, confusion, and low blood pressure (Reynolds' Pentad - Emergency ERCP Drainage required)",
            "Septic shock with high blood lactate"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute ascending cholangitis is a dangerous bacterial infection of blocked bile ducts requiring urgent endoscopic drainage.",
                "plain_analogy": "A clogged municipal sewer line that backs up and overflows toxic waste directly into clean water supplies.",
                "lifestyle_action": "Seek emergency room care immediately for sudden high fever accompanied by yellow eyes (jaundice) and belly pain."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "ERCP Biliary Decompression (First Line - Life-Saving)",
                    "Piperacillin/Tazobactam IV (Zosyn)",
                    "Ceftriaxone + Metronidazole IV"
                ],
                "dosing_gdmt": "Zosyn 4.5 g IV q6h; ERCP with biliary sphincterotomy and plastic stent drainage within 24 hours.",
                "black_box_warning": "Biliary decompression must NOT be delayed; antibiotics cannot penetrate obstructed, pressurized bile ducts.",
                "organ_clearance_cutoffs": "Adjust antibiotic dosing in renal impairment"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TOKYO-TG18",
                "pmid_or_doi": "10.1002/jhbp.512",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "ERCP biliary decompression within 24 hours reduces suppurative cholangitis mortality to <8%."
            }
        }
    },
    {
        "id": "DOC-CARD-398",
        "icd10": "K80.00",
        "condition": "Acute Cholecystitis (Murphy's Sign & Gallbladder Empyema)",
        "specialty": "General Surgery & Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Tokyo Guidelines (TG18) & WSES Guidelines",
        "source_body": "World Journal of Emergency Surgery",
        "citation": "Pisano M et al. 2020 World Society of Emergency Surgery Updated Guidelines for the Diagnosis and Treatment of Acute Calculus Cholecystitis. World J Emerg Surg. 2020;15:61.",
        "doi_or_source": "10.1186/s13017-020-00336-x",
        "clinical_evidence": "Early laparoscopic cholecystectomy (performed within 72 hours of symptom onset) significantly reduces hospital stay, complication rates, and surgical conversion to open surgery compared to delayed elective surgery (p<0.001). In high-risk, non-surgical patients, percutaneous cholecystostomy tube drainage provides effective temporizing source control.",
        "solution_protocol": {
            "non_pharmacological_targets": "NPO; IV isotonic crystalloid fluid resuscitation; multimodal analgesia (NSAIDs like Ketorolac reduce gallstone-induced gallbladder wall inflammation by blocking prostaglandin synthesis); early surgical consultation for laparoscopic cholecystectomy.",
            "monitoring_cadence": "Abdominal exam for localized peritonitis; serial WBC count, liver enzymes, and bilirubin.",
            "clinical_thresholds": "Positive Murphy's sign (arrest of inspiration on RUQ palpation) + ultrasound showing gallstones, gallbladder wall thickening >4 mm, pericholecystic fluid, and sonographic Murphy's sign."
        },
        "patient_plain_language": "Acute cholecystitis happens when a gallstone gets stuck in the exit neck of your gallbladder. Bile is trapped inside, causing the gallbladder to swell, inflame, and become infected. You feel severe, steady aching pain in the upper RIGHT side of your belly that shoots into your right shoulder blade, making it painful to take a deep breath.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my gallbladder ultrasound show gallstones, thick walls (>4 mm), and fluid around the organ?",
            "safety_question": "Is early keyhole surgery (laparoscopic cholecystectomy) planned within the next 24 to 72 hours?",
            "action_threshold_question": "Are we using IV anti-inflammatory medicines (like Ketorolac) to calm the gallbladder swelling?"
        },
        "red_flags": [
            "Severe continuous abdominal pain with high fever and chills (Gallbladder Gangrene / Empyema)",
            "Jaundice with dark tea-colored urine (suggesting gallstone dropped into common bile duct)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute cholecystitis is sudden inflammation and infection of the gallbladder caused by a trapped gallstone.",
                "plain_analogy": "A small pouch whose exit pipe is plugged by a pebble, causing it to swell and inflame.",
                "lifestyle_action": "Avoid high-fat fried foods, take prescribed antibiotics, and undergo surgical removal as recommended."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Laparoscopic Cholecystectomy (Gold Standard)",
                    "Ceftriaxone IV + Metronidazole",
                    "Ketorolac IV (Toradol)"
                ],
                "dosing_gdmt": "Ceftriaxone 1-2 g IV daily + Metronidazole 500 mg q8h; Ketorolac 15-30 mg IV q6h (max 5 days).",
                "black_box_warning": "Avoid ketorolac in renal impairment, active gastrointestinal ulcers, or advanced age.",
                "organ_clearance_cutoffs": "Percutaneous cholecystostomy for critically ill non-surgical patients"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TG18-CHOLE",
                "pmid_or_doi": "10.1186/s13017-020-00336-x",
                "cebm_level": 1,
                "sample_size": 4100,
                "endpoints": "Laparoscopic cholecystectomy within 72 hours reduces hospital stay and total complications by over 45%."
            }
        }
    },
    {
        "id": "DOC-CARD-399",
        "icd10": "T58.01XA",
        "condition": "Carbon Monoxide Poisoning (Carboxyhemoglobinemia)",
        "specialty": "Emergency Medicine & Toxicology",
        "organ_system": "Respiratory & Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Undersea and Hyperbaric Medical Society Guideline",
        "source_body": "Annals of Emergency Medicine",
        "citation": "Weaver LK et al. Hyperbaric Oxygen for Acute Carbon Monoxide Poisoning. N Engl J Med. 2002;347(14):1057-1067.",
        "doi_or_source": "10.1056/NEJMoa013121",
        "clinical_evidence": "The landmark randomized double-blind trial by Weaver et al. (n=152) proved that Hyperbaric Oxygen (HBO at 2.5-3.0 ATA) within 24 hours of exposure reduced cognitive sequelae at 6 weeks by 46% (25.0% vs 46.1%; p=0.007) and at 12 months compared to normobaric oxygen. Normobaric 100% oxygen reduces CO elimination half-life from 320 minutes (room air) to 74 minutes; HBO reduces half-life to 20 minutes.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATELY REMOVE FROM SOURCE; administer 100% high-flow normobaric oxygen via tight-fitting non-rebreather reservoir mask; evaluate for hyperbaric oxygen therapy (HBO indications: COHb >25%, loss of consciousness, pregnancy with COHb >15%, metabolic acidosis, or ischemic ECG changes).",
            "monitoring_cadence": "Serial venous/arterial blood gas measuring Carboxyhemoglobin (COHb); continuous cardiac telemetry and troponin; standard pulse oximetry is FALSELY NORMAL (cannot differentiate oxyhemoglobin from carboxyhemoglobin).",
            "clinical_thresholds": "Carboxyhemoglobin level >3-5% in non-smokers (or >10% in smokers) confirms carbon monoxide inhalation."
        },
        "patient_plain_language": "Carbon monoxide is an invisible, odorless, tasteless toxic gas produced by faulty furnaces, generators, or car exhausts. When inhaled, it binds to your red blood cells 200 times tighter than oxygen, suffocating your body cells from the inside out. Standard fingertip oxygen meters read 100% normal because they cannot tell the difference between oxygen and poison.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact blood Carboxyhemoglobin (COHb) level on the co-oximetry blood gas test?",
            "safety_question": "Do I meet criteria for treatment inside a high-pressure Hyperbaric Oxygen chamber to protect my brain?",
            "action_threshold_question": "How long must I breathe 100% pure oxygen through a non-rebreather mask?"
        },
        "red_flags": [
            "Loss of consciousness, seizure, or confusion after carbon monoxide exposure (Mandatory Hyperbaric Oxygen)",
            "Chest pain or elevated troponin indicating myocardial injury from cellular suffocation"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Carbon monoxide poisoning is inhalation of odorless toxic gas that blocks blood from carrying oxygen to organs.",
                "plain_analogy": "A poison key that jams the lock on red blood cells so oxygen cannot get on board the delivery trucks.",
                "lifestyle_action": "Install certified carbon monoxide detectors on every level of your home and never run generators indoors."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "100% Normobaric Oxygen via Non-Rebreather Mask (Immediate)",
                    "Hyperbaric Oxygen Therapy (HBO at 2.5-3.0 ATA)"
                ],
                "dosing_gdmt": "100% FiO2 via non-rebreather mask until COHb <5% (minimum 6 hours); HBO 3 sessions within 24 hours if high risk.",
                "black_box_warning": "Standard pulse oximeters are falsely reassuring; require co-oximetry blood gas.",
                "organ_clearance_cutoffs": "Zero drug clearance limits for oxygen therapy"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WEAVER-HBO",
                "pmid_or_doi": "10.1056/NEJMoa013121",
                "cebm_level": 2,
                "sample_size": 152,
                "endpoints": "Hyperbaric oxygen reduces delayed neuropsychiatric cognitive sequelae by 46% at 6 weeks (p=0.007)."
            }
        }
    },
    {
        "id": "DOC-CARD-400",
        "icd10": "T57.3X1A",
        "condition": "Cyanide Poisoning (Cytochrome Oxidase Inhibition)",
        "specialty": "Emergency Medicine & Toxicology",
        "organ_system": "Toxicology & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Expert Consensus on Cyanide Antidotes",
        "source_body": "Annals of Emergency Medicine",
        "citation": "Borron SW et al. Hydroxocobalamin for Severe Acute Cyanide Poisoning by Smoke Inhalation. Ann Emerg Med. 2007;49(6):794-801.",
        "doi_or_source": "10.1016/j.annemergmed.2007.01.026",
        "clinical_evidence": "Hydroxocobalamin (Cyanokit 5.0 g IV infused over 15 min) is the Level 1 first-line antidote of choice, binding cyanide with high affinity to form non-toxic Cyanocobalamin (Vitamin B12) excreted in urine. In smoke inhalation victims with severe lactic acidosis (lactate >=8-10 mmol/L), empiric hydroxocobalamin achieves 73% survival without compromising oxygen-carrying capacity (unlike sodium nitrite, which induces fatal methemoglobinemia in smoke inhalation).",
        "solution_protocol": {
            "non_pharmacological_targets": "Decontamination and personal protective equipment; 100% high-flow oxygen; immediate empiric IV Hydroxocobalamin (5.0 g in 200 mL saline over 15 min); repeat 5.0 g dose if severe instability persists; sodium thiosulfate (12.5 g IV) as secondary sulfur donor.",
            "monitoring_cadence": "Arterial blood gas measuring profound lactic acidosis; continuous cardiac telemetry; monitor for harmless dark-red skin and urine discoloration from hydroxocobalamin.",
            "clinical_thresholds": "History of enclosed-space fire with soot in mouth/nose, altered mental status, and unexplained serum lactate >=8.0 mmol/L warrants immediate presumptive antidote."
        },
        "patient_plain_language": "Cyanide is a rapidly fatal chemical poison (commonly inhaled during house fires from burning plastics, foams, and synthetic fabrics). It directly paralyzes the energy engines (mitochondria) inside every cell in your body. Even though blood is full of oxygen, cells cannot use it and starve within minutes. The antidote (Cyanokit) turns the poison directly into harmless Vitamin B12.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has intravenous Hydroxocobalamin (Cyanokit 5.0 grams) been infused immediately?",
            "safety_question": "What is my blood lactate level (is it dropping below 8 mmol/L as cells resume breathing)?",
            "action_threshold_question": "Is the dark red color of my skin and urine a harmless temporary effect of the vitamin antidote?"
        },
        "red_flags": [
            "Sudden collapse, seizures, and severe metabolic acidosis with bright red venous blood (Immediate Cyanokit)",
            "Cardiac arrest from cellular asphyxiation in smoke inhalation"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cyanide poisoning is rapid cellular suffocation caused by inhaling fire smoke or chemical ingestion.",
                "plain_analogy": "A padlock placed directly on the cellular power generators, stopping electricity even though power lines are full.",
                "lifestyle_action": "Install working smoke alarms, evacuate burning buildings immediately, and seek emergency antidote care."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydroxocobalamin IV (Cyanokit - First Line)",
                    "Sodium Thiosulfate IV",
                    "100% High-flow Oxygen"
                ],
                "dosing_gdmt": "Hydroxocobalamin 5.0 g IV over 15 min (may repeat once); followed by Sodium Thiosulfate 12.5 g IV over 10 min.",
                "black_box_warning": "Avoid Sodium Nitrite in smoke inhalation victims (induces methemoglobinemia and fatal hypoxemia).",
                "organ_clearance_cutoffs": "Hydroxocobalamin causes temporary red chromaturia and interferes with colorimetric lab tests"
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CYANOKIT-SMOKE",
                "pmid_or_doi": "10.1016/j.annemergmed.2007.01.026",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "Empiric Hydroxocobalamin achieves 73% survival in smoke-inhalation victims with cyanide shock."
            }
        }
    }
]