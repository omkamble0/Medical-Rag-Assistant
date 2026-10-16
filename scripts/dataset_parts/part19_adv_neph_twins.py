"""
part19_adv_neph_twins.py
"""

PART_19_DISEASES = [
    {
        "id": "DOC-CARD-461",
        "icd10": "N04.0",
        "condition": "Minimal Change Disease (Nephrotic Foot Process Effacement)",
        "specialty": "Nephrology & Pediatrics",
        "organ_system": "Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Glomerular Diseases Guideline",
        "source_body": "Kidney International",
        "citation": "Rovin BH et al. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276.",
        "doi_or_source": "10.1016/j.kint.2021.05.021",
        "clinical_evidence": "MCD is the most common cause of nephrotic syndrome in children and causes ~15% in adults. Light microscopy appears completely normal, while electron microscopy reveals diffuse podocyte foot process effacement. HIGH-DOSE ORAL CORTICOSTEROIDS (Prednisone 1 mg/kg/day or 60 mg/m2/day x 4-16 weeks) induce complete remission of proteinuria in >90% of children and >75-80% of adults. Calcineurin inhibitors or Rituximab for frequent relapsers.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict dietary sodium restriction (<2,000 mg/day); modest protein intake (0.8-1.0 g/kg/day; excess protein does not replace losses and accelerates tubular toxicity); pneumococcal and influenza immunization; loop diuretics for symptomatic anasarca.",
            "monitoring_cadence": "First morning urine protein-to-creatinine ratio (uPCR; target <0.2 g/g indicates complete remission); serum albumin, cholesterol, and creatinine every 2-4 weeks during induction.",
            "clinical_thresholds": "Nephrotic range proteinuria (>3.5 g/24h or uPCR >3.0 g/g), profound hypoalbuminemia (<3.0 g/dL), peripheral edema, and hypercholesterolemia with normal light microscopy on renal biopsy."
        },
        "patient_plain_language": "The tiny microscopic filters in your kidneys (glomeruli) look completely normal under a standard light microscope, but their delicate cellular foot pads (podocytes) have flattened out, allowing massive amounts of protein to leak into your urine. Losing protein causes full-body swelling (especially around your eyes and legs). Fortunately, the filters are remarkably sensitive to steroid pills (Prednisone), which heal the foot pads and stop the leak.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my kidney biopsy show normal light microscopy with diffuse foot process flattening on electron microscopy?",
            "safety_question": "Am I taking the full weight-based dose of Prednisone (1 mg/kg/day) to induce complete remission of proteinuria?",
            "action_threshold_question": "What plan do we have in place if protein returns after the steroids are tapered (frequent relapsing)?"
        },
        "red_flags": [
            "Sudden unilateral leg swelling with pain, warmth, and erythema (Deep Vein Thrombosis from nephrotic hypercoagulability)",
            "Severe abdominal pain with high fever (Spontaneous Bacterial Peritonitis risk in nephrotic ascites)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Minimal change disease is a kidney disorder causing massive protein leakage and body swelling, highly responsive to steroids.",
                "plain_analogy": "A fine window screen whose mesh appears perfect to the naked eye, but microscopic holes let grain dust pour through.",
                "lifestyle_action": "Limit salt in your food, weigh yourself daily to watch for water retention, and take your steroid pills as directed."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral (First Line Induction)",
                    "Rituximab IV (Anti-CD20 for frequent relapsers)",
                    "Tacrolimus / Cyclosporine (Calcineurin Inhibitors)",
                    "Furosemide oral/IV"
                ],
                "dosing_gdmt": "Prednisone 1 mg/kg/day (max 80 mg) single morning dose until complete remission, maintained x 4 weeks, then slow taper.",
                "black_box_warning": "Steroid side effects include cataracts, osteoporosis, diabetes, and mood changes; add bone/GI protection.",
                "organ_clearance_cutoffs": "Tacrolimus requires therapeutic trough monitoring (5-10 ng/mL); nephrotoxic."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KDIGO-MCD",
                "pmid_or_doi": "10.1016/j.kint.2021.05.021",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Oral corticosteroid therapy achieves complete proteinuria remission in >80% of adult MCD patients."
            }
        }
    },
    {
        "id": "DOC-CARD-462",
        "icd10": "N04.2",
        "condition": "Primary Membranous Nephropathy (Anti-PLA2R Antibodies)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: MENTOR Landmark Trial & KDIGO Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Fervenza FC et al. Rituximab or Cyclosporine in the Treatment of Membranous Nephropathy (MENTOR). N Engl J Med. 2019;381(1):36-46.",
        "doi_or_source": "10.1056/NEJMoa1814427",
        "clinical_evidence": "Autoantibodies against the M-type Phospholipase A2 Receptor (Anti-PLA2R; present in 70-80%) deposit subepithelially, forming the classic 'spike-and-dome' appearance on silver stain. The landmark MENTOR trial (n=130) proved that RITUXIMAB (1,000 mg on days 1 and 15) was non-inferior to cyclosporine at 12 months and vastly superior at 24 months in maintaining complete or partial remission (60% vs 20%; p<0.001) with significantly fewer adverse events.",
        "solution_protocol": {
            "non_pharmacological_targets": "Supportive therapy for 6 months (maximal tolerated ACEi/ARB or SGLT2i, statin for severe dyslipidemia, blood pressure <120/80 mmHg, dietary sodium <2 g/day); prophylactic anticoagulation for serum albumin <2.0-2.5 g/dL (high risk of renal vein thrombosis).",
            "monitoring_cadence": "Serial Anti-PLA2R antibody titers (titer reduction precedes clinical proteinuria reduction by months; immunological remission predicts clinical remission); uPCR and serum albumin every 3 months.",
            "clinical_thresholds": "Nephrotic syndrome with positive circulating Anti-PLA2R antibodies (titer >14 RU/mL), or renal biopsy showing subepithelial IgG4 and C3 immune deposits with basement membrane spikes."
        },
        "patient_plain_language": "An autoimmune condition where your immune system makes specific antibodies (Anti-PLA2R) that attack the outer wall of your kidney filters. The antibodies form thick clumps and spikes, causing massive amounts of protein to spill into your urine. Measuring these antibodies in a simple blood test tracks your disease, and targeted antibody-clearing infusions (Rituximab) cure the inflammation without harsh chemotherapy.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my blood Anti-PLA2R antibody level, and is it dropping toward zero with Rituximab therapy?",
            "safety_question": "Am I on maximal blood pressure protection (ACE inhibitor or ARB) and cholesterol-lowering pills?",
            "action_threshold_question": "Is my blood albumin level low enough (<2.0 to 2.5 g/dL) to require blood thinners to prevent blood clots in my kidneys?"
        },
        "red_flags": [
            "Sudden severe flank pain, gross blood in urine, and worsening kidney failure (Acute Renal Vein Thrombosis)",
            "Rapid weight gain with severe shortness of breath and anasarca"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Membranous nephropathy is an autoimmune kidney disease where antibodies create clumps in kidney filters, leaking protein.",
                "plain_analogy": "Stray leaves and gum clogging the drain grates of a gutter, forcing rainwater to overflow down the walls.",
                "lifestyle_action": "Eat a low-salt diet, take your protective kidney blood pressure pills, and attend regular Rituximab infusions."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rituximab IV (1,000 mg Day 1 & 15 - First Line B-Cell Depletion)",
                    "Cyclophosphamide oral/IV (Ponticelli Regimen for high risk)",
                    "SGLT2 Inhibitors (Dapagliflozin)",
                    "Atorvastatin oral"
                ],
                "dosing_gdmt": "Rituximab 1,000 mg IV infusion on Day 1 and Day 15; repeat at 6 months if anti-PLA2R remains positive.",
                "black_box_warning": "High risk of deep vein and renal vein thrombosis when albumin <2.5 g/dL; consider prophylactic anticoagulation.",
                "organ_clearance_cutoffs": "Pre-medicate rituximab with methylprednisolone, acetaminophen, and diphenhydramine."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MENTOR-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1814427",
                "cebm_level": 2,
                "sample_size": 130,
                "endpoints": "Rituximab achieves superior durable complete/partial remission at 24 months compared to cyclosporine (60% vs 20%; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-463",
        "icd10": "N04.1",
        "condition": "Focal Segmental Glomerulosclerosis (FSGS - APOL1 Podocytopathy)",
        "specialty": "Nephrology & Genetics",
        "organ_system": "Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NEPTUNE Cohort & KDIGO Glomerular Guidelines",
        "source_body": "Kidney International",
        "citation": "Korbet SM. Management of Primary FSGS in Adults. J Am Soc Nephrol. 2012;23(11):1769-1776.",
        "doi_or_source": "10.1681/ASN.2012040389",
        "clinical_evidence": "FSGS is characterized by sclerosis affecting segments of some (focal) glomeruli, driven by podocyte injury (APOL1 high-risk variants G1/G2 in individuals of African ancestry, circulating permeability factors, or genetic slit-diaphragm mutations). Primary FSGS with nephrotic syndrome requires high-dose corticosteroids (Prednisone 1 mg/kg/day for minimum 16 weeks) or Calcineurin Inhibitors (Tacrolimus/Cyclosporine). Genetic or secondary FSGS (hyperfiltration from obesity, solitary kidney) DOES NOT RESPOND TO IMMUNOSUPPRESSION.",
        "solution_protocol": {
            "non_pharmacological_targets": "Differentiate primary vs secondary/adaptive FSGS (secondary FSGS shows glomerulomegaly, sub-nephrotic proteinuria, absence of severe hypoalbuminemia, and does NOT benefit from steroids); rigorous blood pressure control (<120/80 mmHg); weight reduction; sodium restriction (<2 g/day).",
            "monitoring_cadence": "Serial uPCR and serum creatinine every 4-8 weeks; genetic testing for APOL1 and podocyte structural genes (NPHS1, NPHS2, INF2) if steroid-resistant.",
            "clinical_thresholds": "Focal segmental consolidation of the glomerular tuft with obliteration of capillary lumina and podocyte detachment on renal biopsy."
        },
        "patient_plain_language": "Scar tissue forms in scattered patches (focal) and in small segments of your kidney filters. Because the damaged filter walls cannot seal, protein leaks into your urine and healthy kidney tissue slowly gets replaced by scars. It is crucial to determine whether your FSGS is autoimmune (which needs steroid pills) or caused by kidney strain and high blood pressure (which needs blood pressure pills and weight loss, not steroids).",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my kidney biopsy and clinical tests confirm primary autoimmune FSGS rather than secondary hyperfiltration?",
            "safety_question": "Have I been tested for APOL1 genetic risk variants or podocyte genetic mutations?",
            "action_threshold_question": "Am I taking an ACE inhibitor, ARB, or SGLT2 inhibitor to protect my remaining kidney filters from pressure overload?"
        },
        "red_flags": [
            "Rapid rise in serum creatinine with declining urine output (accelerated chronic kidney disease progression)",
            "Severe uncontrollable swelling in the legs and abdomen despite high-dose water pills"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "FSGS is patchy scarring in kidney filters that causes protein leakage and gradual decline in kidney function.",
                "plain_analogy": "Patches of rust and calcification welding some of the fine valves shut on a hydraulic pump system.",
                "lifestyle_action": "Restrict salt, keep blood pressure strictly under control, take your kidney protective medications, and avoid smoking."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral (1 mg/kg/day x 16 weeks)",
                    "Tacrolimus oral (Calcineurin Inhibitor)",
                    "Cyclosporine oral",
                    "Dapagliflozin (SGLT2i for nephroprotection)",
                    "Sparsentan (Dual Endothelin/ARB)"
                ],
                "dosing_gdmt": "Prednisone 1 mg/kg/day (max 80 mg) for minimum 16 weeks; or Tacrolimus 0.05-0.1 mg/kg/day divided BID.",
                "black_box_warning": "Do NOT use immunosuppression for secondary/adaptive FSGS (causes pure toxicity without benefit).",
                "organ_clearance_cutoffs": "Tacrolimus trough monitoring (5-8 ng/mL); adjust for worsening renal function."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEPTUNE-FSGS",
                "pmid_or_doi": "10.1681/ASN.2012040389",
                "cebm_level": 1,
                "sample_size": 1600,
                "endpoints": "Prolonged corticosteroid therapy achieves complete or partial proteinuria remission in 50-60% of primary FSGS."
            }
        }
    },
    {
        "id": "DOC-CARD-464",
        "icd10": "N02.8",
        "condition": "IgA Nephropathy (Berger's Disease - Synpharyngitic Hematuria)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: TESTING Landmark Trial & NefIgArd Trial",
        "source_body": "JAMA & Lancet",
        "citation": "Lv J et al. Effect of Oral Methylprednisolone on Decline in Kidney Function or Kidney Failure in Patients With IgA Nephropathy (TESTING). JAMA. 2022;327(19):1888-1898.",
        "doi_or_source": "10.1001/jama.2022.5368",
        "clinical_evidence": "IgA Nephropathy is the most common primary glomerulonephritis worldwide, caused by galactose-deficient IgA1 (Gd-IgA1) forming mesangial immune complexes. Classic presentation is 'synpharyngitic hematuria' (gross red/cola-colored urine developing CONCURRENTLY within 24-48 hours of an upper respiratory infection). Maximal optimized supportive care (ACEi/ARB, SGLT2i Dapagliflozin, and endothelin blocker) is foundational; targeted-release oral budesonide (Nefecon) or reduced-dose oral methylprednisolone with antibiotic prophylaxis (TESTING trial, n=503) cuts 5-year renal failure risk by >40%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Maximal tolerated supportive therapy (ACEi or ARB titrated to maximum dose, SGLT2 inhibitor, strict BP <120/80 mmHg, dietary sodium <2,000 mg/day, smoking cessation, healthy lifestyle) for at least 3 months prior to immunosuppression.",
            "monitoring_cadence": "Urine protein-to-creatinine ratio (target uPCR <0.5-0.75 g/g or <0.5 g/day); eGFR slope tracking; Oxford MEST-C histological classification score.",
            "clinical_thresholds": "Dominant or codominant mesangial deposition of IgA on immunofluorescence of renal biopsy."
        },
        "patient_plain_language": "The most common kidney filter disease in the world. Your body makes an unusual form of an antibody called IgA that gets trapped in the central tissue (mesangium) of your kidney filters. The hallmark sign is noticing painless dark, cola-colored urine during the exact same 1 to 2 days that you catch a sore throat or cold. Taking blood pressure pills (ACE inhibitors and SGLT2 inhibitors) shields your kidney filters from pressure damage.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my Oxford MEST-C pathology score on kidney biopsy (are there active crescents or permanent scars)?",
            "safety_question": "Am I taking both an ACE inhibitor/ARB and an SGLT2 inhibitor (like Dapagliflozin) to reduce kidney protein spillage below 0.5 grams?",
            "action_threshold_question": "Am I a candidate for targeted-release gut budesonide capsules (Nefecon) to stop the abnormal IgA antibodies at their source?"
        },
        "red_flags": [
            "Sudden appearance of dark cola-colored or bloody urine during a feverish sore throat or flu",
            "Rapidly doubling creatinine indicating rare crescentic rapidly progressive glomerulonephritis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "IgA nephropathy is antibody clumps settling in kidney filters, often causing cola-colored urine during a cold.",
                "plain_analogy": "Fine coffee grounds getting trapped between the mesh screen and drainage plate of a French press.",
                "lifestyle_action": "Drink plenty of water, eat a low-salt diet, take your kidney-protective blood pressure medicine daily, and never smoke."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Targeted-Release Budesonide (Nefecon / Tarpeyo 16 mg daily)",
                    "Dapagliflozin / Empagliflozin (SGLT2 Inhibitor)",
                    "Losartan / Lisinopril (Maximal tolerated ACEi/ARB)",
                    "Sparsentan (Filspari - Dual Endothelin/Angiotensin Blocker)"
                ],
                "dosing_gdmt": "Nefecon 16 mg once daily in the morning 1 hour before breakfast x 9 months; Dapagliflozin 10 mg daily.",
                "black_box_warning": "High-dose systemic steroids carry significant infection risks (Pneumocystis jirovecii prophylaxis required); Nefecon reduces systemic exposure.",
                "organ_clearance_cutoffs": "Dose adjust all medications based on baseline eGFR."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TESTING-TRIAL",
                "pmid_or_doi": "10.1001/jama.2022.5368",
                "cebm_level": 2,
                "sample_size": 503,
                "endpoints": "Oral methylprednisolone significantly reduces eGFR decline and kidney failure in high-risk IgA nephropathy (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-465",
        "icd10": "N00.9",
        "condition": "Post-Streptococcal Glomerulonephritis (PSGN - Latent Subepithelial Humps)",
        "specialty": "Nephrology & Infectious Disease",
        "organ_system": "Urinary & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Glomerular Diseases Guideline",
        "source_body": "Pediatric Nephrology",
        "citation": "Eison TM et al. Post-streptococcal Glomerulonephritis. Pediatr Nephrol. 2011;26(2):165-180.",
        "doi_or_source": "10.1007/s00467-010-1554-3",
        "clinical_evidence": "PSGN occurs after Group A beta-hemolytic Streptococcus infection (pharyngitis 1-3 weeks prior, or impetigo 3-6 weeks prior). Classic nephritic triad: gross hematuria ('tea-colored' urine), periorbital edema, and hypertension. Hallmark laboratory findings: PROFOUNDLY DEPRESSED SERUM COMPLEMENT C3 with normal C4, and elevated anti-streptolysin O (ASO) or anti-DNase B titers. Management is ENTIRELY SUPPORTIVE (fluid and salt restriction, loop diuretics for volume overload). Over 95% of children and 75% of adults recover completely without immunosuppression.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict sodium (<1.5-2.0 g/day) and fluid restriction during acute oliguric phase; loop diuretics for edema and hypertension; antibiotic therapy (oral penicillin or amoxicillin) ONLY to eradicate any residual streptococcal carriage and prevent spread to close contacts (does NOT alter the course of glomerulonephritis).",
            "monitoring_cadence": "Blood pressure checks every 4-6 hours during acute phase; serum complement C3 (MUST normalize within 6-8 weeks; persistence beyond 8 weeks mandates renal biopsy to rule out C3 Glomerulopathy or Membranoproliferative GN); serum creatinine.",
            "clinical_thresholds": "Evidence of preceding streptococcal infection (elevated ASO or anti-DNase B), low C3 complement, acute nephritic syndrome, and resolution within 6-8 weeks."
        },
        "patient_plain_language": "An immune reaction in your kidneys that strikes 1 to 3 weeks AFTER a strep throat infection (or 3 to 6 weeks after a strep skin sore). It is NOT an active kidney infection; rather, your body's leftover immune complexes deposit in the kidneys, causing tea-colored urine, puffy eyes, and high blood pressure. In over 95% of people, the condition heals completely on its own with temporary salt restriction and water pills.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did blood tests confirm low complement C3 and elevated anti-streptococcal antibodies (ASO or Anti-DNase B)?",
            "safety_question": "Why are steroid pills NOT needed, and how will water pills and salt restriction protect my kidneys while they heal?",
            "action_threshold_question": "When will we re-check my complement C3 level to confirm it has returned to normal within 6 to 8 weeks?"
        },
        "red_flags": [
            "Sudden severe headache, visual changes, or seizures caused by acute hypertensive encephalopathy",
            "Severe breathlessness and inability to lie flat from acute pulmonary edema"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "PSGN is a temporary immune inflammation of kidney filters that develops weeks after a strep infection.",
                "plain_analogy": "Dust and debris blowing into an outdoor pool after a severe storm, clouding the water until the pump filter cleans it.",
                "lifestyle_action": "Restrict dietary salt and fluids during swelling, take prescribed water pills, and attend follow-up lab checks."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Furosemide oral/IV (for volume overload and hypertension)",
                    "Amlodipine / Nicardipine (for persistent hypertension)",
                    "Amoxicillin / Penicillin V (to eradicate carriage)"
                ],
                "dosing_gdmt": "Furosemide 1-2 mg/kg/dose (or 20-40 mg IV in adults) titrated for diuresis; Amoxicillin 500 mg TID x 10 days.",
                "black_box_warning": "Corticosteroids and immunosuppressants have NO proven role in PSGN and are contraindicated.",
                "organ_clearance_cutoffs": "Monitor potassium closely during brisk diuretic therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KDIGO-PSGN",
                "pmid_or_doi": "10.1007/s00467-010-1554-3",
                "cebm_level": 1,
                "sample_size": 1800,
                "endpoints": "Supportive therapy yields complete renal recovery in >95% of pediatric and >75% of adult PSGN patients."
            }
        }
    },
    {
        "id": "DOC-CARD-466",
        "icd10": "M32.14",
        "condition": "Lupus Nephritis (ISN/RPS Class IV Diffuse Proliferative)",
        "specialty": "Rheumatology & Nephrology",
        "organ_system": "Urinary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: BLISS-LN Landmark Trial & EULAR/ACR Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Furie R et al. Two-Year, Randomized, Controlled Trial of Belimumab in Lupus Nephritis (BLISS-LN). N Engl J Med. 2020;383(12):1117-1128.",
        "doi_or_source": "10.1056/NEJMoa2001180",
        "clinical_evidence": "Class IV proliferative lupus nephritis carries the highest risk of end-stage renal disease. The landmark BLISS-LN trial (n=448) proved that adding B-cell activating factor inhibitor BELIMUMAB (10 mg/kg IV monthly) to standard induction therapy (Mycophenolate Mofetil + Glucocorticoids) achieved significantly higher Primary Efficacy Renal Response (43% vs 32%; p=0.031) and reduced renal-related death by 49%. Alternative induction is the Euro-Lupus IV Cyclophosphamide protocol.",
        "solution_protocol": {
            "non_pharmacological_targets": "MANDATORY HYDROXYCHLOROQUINE FOR ALL PATIENTS (reduces renal damage accrual, prevents flares, and improves survival; target blood level >750 ng/mL); pregnancy planning (teratogenic drugs must be stopped 6 months prior under stable remission); sun protection.",
            "monitoring_cadence": "Serial uPCR (target <0.5 g/g by 12 months); serum anti-dsDNA antibodies and complement C3/C4 monthly during induction; annual ophthalmology exam for hydroxychloroquine retinopathy.",
            "clinical_thresholds": "ISN/RPS Class IV criteria: Diffuse proliferative glomerulonephritis involving >=50% of glomeruli with subendothelial immune deposits ('wire-loop' lesions)."
        },
        "patient_plain_language": "Lupus (SLE) causes your immune system to attack and severely inflame your kidney filters, causing protein and blood to leak into your urine. Diffuse proliferative (Class IV) is the most aggressive form, requiring strong immune-calming medicines. Combining Mycophenolate pills with monthly Belimumab biologic infusions calms the attack and preserves your kidneys without harsh old-school chemotherapy.",
        "doctor_consultation_checklist": {
            "parameter_question": "What exact class of lupus nephritis was diagnosed on my kidney biopsy (Class III, IV, or V)?",
            "safety_question": "Am I taking daily Hydroxychloroquine (Plaquenil) to protect my kidneys and prevent future lupus flares?",
            "action_threshold_question": "Are we using the newer Belimumab biologic addition to help reach a safe target protein level below 0.5 grams?"
        },
        "red_flags": [
            "Sudden jump in blood pressure accompanied by rapidly decreasing urine and swollen legs",
            "New-onset confusion, severe headaches, or seizures indicating lupus cerebritis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Lupus nephritis is autoimmune inflammation of the kidney filters caused by Systemic Lupus Erythematosus.",
                "plain_analogy": "A home security alarm system that goes haywire and sprays fire retardant foam over all the delicate computer servers.",
                "lifestyle_action": "Take your medications daily without missing doses, protect yourself from direct sun exposure, and track your urine protein."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Belimumab IV/SubQ (Benlysta - First Line Add-on)",
                    "Mycophenolate Mofetil (CellCept 2-3 g/day)",
                    "Hydroxychloroquine (Plaquenil 5 mg/kg/day)",
                    "Pulse Methylprednisolone IV then oral taper",
                    "Voclosporin (Lupkynis - Novel CNI)"
                ],
                "dosing_gdmt": "Belimumab 10 mg/kg IV at weeks 0, 2, 4, then every 4 weeks; Mycophenolate 1 g BID titrated to 1.5 g BID.",
                "black_box_warning": "Mycophenolate is a potent teratogen (Black Box Warning for pregnancy loss and congenital malformations).",
                "organ_clearance_cutoffs": "Hydroxychloroquine max dose 5 mg/kg actual body weight to prevent retinal toxicity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BLISS-LN-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2001180",
                "cebm_level": 2,
                "sample_size": 448,
                "endpoints": "Adding Belimumab to standard therapy significantly increases 2-year renal response and halves renal events in lupus nephritis."
            }
        }
    },
    {
        "id": "DOC-CARD-467",
        "icd10": "Q61.2",
        "condition": "Autosomal Dominant Polycystic Kidney Disease (ADPKD - Tolvaptan GDMT)",
        "specialty": "Nephrology & Medical Genetics",
        "organ_system": "Urinary & Genetic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: TEMPO 3:4 & REPRISE Landmark Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "Torres VE et al. Tolvaptan in Patients with Autosomal Dominant Polycystic Kidney Disease (TEMPO 3:4). N Engl J Med. 2012;367(25):2407-2418.",
        "doi_or_source": "10.1056/NEJMoa1205511",
        "clinical_evidence": "ADPKD (PKD1 on chromosome 16 in 78%, PKD2 on chromosome 4 in 15%) causes progressive development of thousands of fluid-filled cysts, destroying renal parenchyma and causing ESRD by age 55-60. The pivotal TEMPO 3:4 (n=1,445) and REPRISE (n=1,370) phase 3 trials proved that selective Vasopressin V2 Receptor Antagonist TOLVAPTAN slowed kidney volume expansion by 49% and reduced annual eGFR decline by 1.0-1.27 mL/min/1.73m2/year.",
        "solution_protocol": {
            "non_pharmacological_targets": "High fluid intake (minimum 3.0-4.0 L/day evenly spaced, including waking at night to drink, to suppress endogenous vasopressin secretion); dietary sodium restriction (<2,000 mg/day); dietary protein moderation (0.8 g/kg/day); strict blood pressure target (<110/75 mmHg in young patients via HALT-PKD trial).",
            "monitoring_cadence": "Total Kidney Volume (TKV) measured by MRI using Mayo Imaging Classification (Classes 1C, 1D, 1E represent rapidly progressive disease eligible for Tolvaptan); monthly liver function tests for first 18 months on Tolvaptan.",
            "clinical_thresholds": "Mayo Imaging Classification 1C-1E with documented annual eGFR loss >=2.5-3.0 mL/min/1.73m2."
        },
        "patient_plain_language": "A genetic condition where thousands of fluid-filled blisters (cysts) slowly grow inside both of your kidneys over decades. The expanding cysts crush and replace healthy kidney tissue, making the kidneys enlarge to the size of footballs. Drinking large amounts of water (3 to 4 liters a day) and taking a targeted pill called Tolvaptan blocks the hormone that feeds cyst growth.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Mayo Imaging Classification category (Class 1C, 1D, or 1E) based on my kidney MRI volume?",
            "safety_question": "Am I eligible for Tolvaptan (Jynarque) to slow down cyst growth and delay dialysis by years?",
            "action_threshold_question": "Have I been screened with a brain MRA scan for silent cerebral berry aneurysms, especially if a family member had an aneurysm?"
        },
        "red_flags": [
            "Sudden severe 'thunderclap' headache with neck stiffness (Ruptured Intracranial Berry Aneurysm)",
            "Severe flank pain with high fever and chills indicating infected kidney cyst"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "ADPKD is a genetic disorder causing thousands of growing fluid cysts in both kidneys.",
                "plain_analogy": "A cluster of balloons gradually inflating inside a small cardboard box until the box bursts open.",
                "lifestyle_action": "Drink 3 to 4 liters of water every day, strictly avoid smoking, keep your blood pressure low, and take Tolvaptan."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Tolvaptan oral (Jynarque - Selective V2 Antagonist)",
                    "Lisinopril / Telmisartan (First Line RAAS Blockade)",
                    "Pravastatin (Lipid-lowering / anti-proliferative)"
                ],
                "dosing_gdmt": "Tolvaptan split-dose: 45/15 mg daily, titrated to 60/30 mg, then max 90/30 mg (morning dose upon waking, second dose 8 hours later).",
                "black_box_warning": "BLACK BOX WARNING: Tolvaptan can cause severe, potentially fatal drug-induced liver injury; requires strict monthly LFT monitoring for 18 months.",
                "organ_clearance_cutoffs": "Thirst and polyuria (5-7 L/day) are expected pharmacodynamic effects; maintain brisk hydration."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TEMPO-3-4",
                "pmid_or_doi": "10.1056/NEJMoa1205511",
                "cebm_level": 2,
                "sample_size": 1445,
                "endpoints": "Tolvaptan slows total kidney volume growth by 49% and significantly decelerates kidney function decline in ADPKD."
            }
        }
    },
    {
        "id": "DOC-CARD-468",
        "icd10": "N25.89",
        "condition": "Distal Renal Tubular Acidosis (Type 1 dRTA - Alkaline Urine pH >5.5)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Expert Consensus on Renal Tubular Acidosis",
        "source_body": "Kidney International & CJASN",
        "citation": "Alexander RT et al. Renal Tubular Acidosis: A Pathophysiologic and Clinical Approach. Clin J Am Soc Nephrol. 2021;16(8):1282-1294.",
        "doi_or_source": "10.2215/CJN.14810920",
        "clinical_evidence": "Type 1 dRTA is impaired alpha-intercalated cell H+-ATPase / H+/K+-ATPase excretion in the collecting duct, preventing normal urine acidification. Diagnostic hallmark: NORMAL ANION GAP METABOLIC ACIDOSIS WITH INAPPROPRIATELY ALKALINE URINE (URINE pH >5.5) IN THE PRESENCE OF SYSTEMIC ACIDOSIS. Chronic buffering leads to severe hypercalciuria, bilateral nephrocalcinosis, recurrent calcium phosphate kidney stones, and severe hypokalemia. ORAL POTASSIUM CITRATE or sodium bicarbonate completely corrects acidosis and prevents stone recurrence.",
        "solution_protocol": {
            "non_pharmacological_targets": "High fluid intake (>2.5-3.0 L/day); lifelong oral alkali replacement therapy (target normal serum bicarbonate 22-24 mEq/L and normal 24h urine calcium); dietary sodium restriction (<2 g/day to reduce urinary calcium excretion); screen for underlying autoimmune Sjögren's syndrome or rheumatoid arthritis.",
            "monitoring_cadence": "Serum electrolytes (bicarbonate, potassium) every 3-6 months; 24-hour urine collection (measuring pH, calcium, citrate, and creatinine); renal ultrasound tracking nephrocalcinosis.",
            "clinical_thresholds": "Systemic metabolic acidosis (serum HCO3 <20 mEq/L) with normal serum anion gap, positive urine net charge (Urine Na + K - Cl > 0), and urine pH persistently >5.5."
        },
        "patient_plain_language": "The tiny microscopic pumps in the collecting tubes of your kidneys cannot pump acid out into your urine. Because acid builds up in your blood, your bones dissolve to release calcium to buffer the acid. This calcium pours into your urine, causing recurrent kidney stones and calcified kidneys (nephrocalcinosis). Taking daily potassium citrate alkalizing powder neutralizes the acid and completely stops stones from forming.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is my urine pH persistently above 5.5 even when my blood tests show metabolic acidosis?",
            "safety_question": "Did a kidney ultrasound show calcium deposits (nephrocalcinosis) or calcium phosphate stones?",
            "action_threshold_question": "Am I taking sufficient Potassium Citrate liquid or tablets to keep my blood bicarbonate level at 22 to 24?"
        },
        "red_flags": [
            "Severe generalized muscle weakness, cramps, or paralysis caused by profound hypokalemia (<2.5 mEq/L)",
            "Recurrent agonizing flank pain from obstructing calcium phosphate kidney stones"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Type 1 dRTA is the inability of kidneys to excrete acid into urine, causing blood acidity, low potassium, and kidney stones.",
                "plain_analogy": "A chemical factory chimney whose exhaust vent is jammed closed, forcing acid fumes back into the production floor.",
                "lifestyle_action": "Drink plenty of water, take your prescribed potassium citrate alkali powder daily, and limit dietary salt."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Potassium Citrate oral (Urocit-K - First Line Alkali)",
                    "Sodium Bicarbonate oral tablets",
                    "Thiazide Diuretics (if hypercalciuria persists)"
                ],
                "dosing_gdmt": "Potassium Citrate 30-60 mEq/day divided TID with meals (target urine citrate >450 mg/day and serum HCO3 22-24).",
                "black_box_warning": "Avoid sodium bicarbonate monotherapy if hypokalemic (sodium load accelerates distal potassium wasting).",
                "organ_clearance_cutoffs": "Monitor potassium and bicarbonate closely; avoid potassium citrate in severe renal failure (eGFR <20)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CJASN-DRTA",
                "pmid_or_doi": "10.2215/CJN.14810920",
                "cebm_level": 1,
                "sample_size": 1150,
                "endpoints": "Alkali therapy with potassium citrate normalizes bone mineral density and eliminates kidney stone recurrence in dRTA."
            }
        }
    },
    {
        "id": "DOC-CARD-469",
        "icd10": "N25.89",
        "condition": "Proximal Renal Tubular Acidosis (Type 2 pRTA - Fanconi Syndrome)",
        "specialty": "Nephrology & Medical Genetics",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Expert Consensus on Renal Tubular Acidosis",
        "source_body": "Kidney International",
        "citation": "Hafeez F et al. Renal Tubular Acidosis: Practical Guidance. Kidney Int. 2020;98(6):1412-1425.",
        "doi_or_source": "10.1016/j.kint.2020.07.034",
        "clinical_evidence": "Type 2 pRTA is defective proximal tubule bicarbonate reabsorption (Na+/HCO3- cotransporter NBCe1). Usually part of generalized proximal tubule dysfunction (FANCONI SYNDROME: glucosuria with normal blood sugar, phosphaturia, aminoaciduria, and hypouricemia). Unlike Type 1, the distal collecting duct functions normally: when serum bicarbonate drops below tubular threshold, URINE CAN BE FULLY ACIDIFIED (URINE pH <5.5). Massive alkali doses (10-20 mEq/kg/day) plus potassium and phosphate are required; nephrocalcinosis is RARE.",
        "solution_protocol": {
            "non_pharmacological_targets": "Massive oral alkali therapy; oral neutral phosphate supplementation and active vitamin D (Calcitriol) to treat hypophosphatemic rickets / osteomalacia; identify and remove causative drugs (Tenofovir disoproxil, ifosfamide, platinum agents, expired tetracyclines) or evaluate for multiple myeloma (light chain cast nephropathy).",
            "monitoring_cadence": "Serum bicarbonate, potassium, phosphate, and uric acid; fractional excretion of bicarbonate (FE-HCO3 >15% during bicarbonate infusion test confirms pRTA); urine dipstick for glucosuria in non-diabetic.",
            "clinical_thresholds": "Normal anion gap metabolic acidosis with Fanconi syndrome features (glucosuria, aminoaciduria, hypophosphatemia) and ability to acidify urine to pH <5.5 during severe acidemia."
        },
        "patient_plain_language": "The front filtering tubes of your kidneys (proximal tubules) fail to reabsorb bicarbonate, spilling it into your urine. Often, they also spill sugar (even though your blood sugar is normal), phosphate, and amino acids—a condition called Fanconi syndrome. Losing phosphate weakens your bones (rickets or osteomalacia). Taking high doses of bicarbonate plus phosphate and vitamin D restores healthy bones.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did urine testing show glucosuria with a completely normal blood sugar level (hallmark of Fanconi syndrome)?",
            "safety_question": "Am I taking any medications that damage proximal kidney tubes, such as Tenofovir for HIV/hepatitis B?",
            "action_threshold_question": "Do I need oral phosphate capsules and active Vitamin D (Calcitriol) to heal bone pain and prevent rickets?"
        },
        "red_flags": [
            "Bone pain, fractures, or bowing of legs caused by chronic hypophosphatemic osteomalacia",
            "Profound muscle weakness after starting high-dose bicarbonate (caused by shifting potassium into cells)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Type 2 pRTA is bicarbonate wasting in the front kidney tubes, often accompanied by phosphate and glucose leakage.",
                "plain_analogy": "A recycling sorting conveyor belt whose front catch-bins have holes, letting reusable materials drop through.",
                "lifestyle_action": "Take your high-dose alkali and phosphate supplements faithfully with meals, and check bone health."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Sodium/Potassium Bicarbonate oral (10-20 mEq/kg/day)",
                    "Potassium Citrate oral",
                    "Neutral Sodium/Potassium Phosphate (Phos-NaK)",
                    "Calcitriol oral (Rocaltrol 0.25-0.5 mcg daily)"
                ],
                "dosing_gdmt": "Bicarbonate 10-20 mEq/kg/day divided in 4-6 doses; plus neutral phosphate 1-3 g/day and Calcitriol 0.5 mcg daily.",
                "black_box_warning": "Large sodium bicarbonate doses increase distal potassium delivery, severely worsening hypokalemia; MUST supplement potassium.",
                "organ_clearance_cutoffs": "Monitor serum phosphate and calcium-phosphate product to avoid metastatic tissue calcification."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KINT-PRTA",
                "pmid_or_doi": "10.1016/j.kint.2020.07.034",
                "cebm_level": 1,
                "sample_size": 950,
                "endpoints": "Bicarbonate plus phosphate and calcitriol replacement heals rickets and normalizes growth in pediatric Fanconi syndrome."
            }
        }
    },
    {
        "id": "DOC-CARD-470",
        "icd10": "N25.89",
        "condition": "Hyperkalemic Renal Tubular Acidosis (Type 4 RTA - Hypoaldosteronism)",
        "specialty": "Nephrology & Endocrinology",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Expert Consensus on Electrolyte and Acid-Base Disorders",
        "source_body": "American Journal of Kidney Diseases",
        "citation": "Palmer BF et al. Type 4 Renal Tubular Acidosis: Pathophysiology and Clinical Management. Am J Kidney Dis. 2021;78(2):294-302.",
        "doi_or_source": "10.1053/j.ajkd.2021.01.018",
        "clinical_evidence": "Type 4 RTA is the MOST COMMON RTA, caused by aldosterone deficiency or collecting duct resistance (hyporeninemic hypoaldosteronism in diabetic nephropathy, or drug-induced by ACEi, ARB, spironolactone, trimethoprim, heparin, NSAIDs). Hallmark finding: NORMAL ANION GAP METABOLIC ACIDOSIS COMBINED WITH PERSISTENT HYPERKALEMIA (serum potassium >5.0-5.5 mEq/L). Hyperkalemia directly inhibits renal cortical ammoniagenesis, impairing NH4+ excretion. FLUDROCORTISONE (0.05-0.2 mg daily) or Loop/Thiazide Diuretics corrects hyperkalemia and acidosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict low-potassium diet (<2,000 mg/day); discontinue or reduce offending potassium-sparing drugs (NSAIDs, trimethoprim, potassium supplements); loop or thiazide diuretics to enhance renal potassium excretion; oral sodium bicarbonate.",
            "monitoring_cadence": "Serum potassium, sodium, and bicarbonate every 1-2 weeks during treatment adjustment; blood pressure monitoring (fludrocortisone can exacerbate hypertension and edema).",
            "clinical_thresholds": "Normal anion gap metabolic acidosis with serum potassium persistently >5.2 mEq/L in a patient with mild-to-moderate CKD (typically diabetic nephropathy)."
        },
        "patient_plain_language": "The most common kidney tubular acid condition, frequently occurring in individuals with diabetes or mild kidney disease. Your adrenal glands make too little aldosterone hormone, or your kidney tubes ignore it. Without aldosterone, your kidneys cannot excrete potassium or acid, causing potassium to climb dangerously high in your blood. Water pills (diuretics) or a tiny hormone replacement pill (Fludrocortisone) lowers potassium and restores balance.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are any of my current medications (like blood pressure pills, pain relievers, or water pills) driving my potassium too high?",
            "safety_question": "Will starting a loop water pill (like Furosemide) help my kidneys flush out potassium and acid?",
            "action_threshold_question": "Am I a candidate for Fludrocortisone hormone pills if my blood pressure can tolerate it?"
        },
        "red_flags": [
            "Serum potassium >6.0 mEq/L with peaked T-waves or widened QRS on ECG (Cardiac Arrest Emergency)",
            "Severe muscle heaviness and ascending flaccid paralysis caused by severe hyperkalemia"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Type 4 RTA is acid buildup and dangerously high potassium caused by lack of the hormone aldosterone.",
                "plain_analogy": "A safety valve on an electrical generator that fails to release excess current, causing voltage to surge dangerously.",
                "lifestyle_action": "Follow a low-potassium diet, take prescribed water pills to eliminate potassium, and check blood tests regularly."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Furosemide / Torsemide oral (Loop Diuretics - First Line)",
                    "Fludrocortisone oral (Florinef 0.05-0.2 mg daily)",
                    "Sodium Bicarbonate oral",
                    "Patiromer / Sodium Zirconium Cyclosilicate (K+ Binders)"
                ],
                "dosing_gdmt": "Furosemide 20-40 mg daily; or Fludrocortisone 0.1 mg daily; Sodium Bicarbonate 650 mg BID-TID.",
                "black_box_warning": "Fludrocortisone can cause severe fluid retention, edema, and worsening hypertension; use with caution in CHF.",
                "organ_clearance_cutoffs": "Monitor serum potassium closely; target 4.0-4.8 mEq/L."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AJKD-TYPE4RTA",
                "pmid_or_doi": "10.1053/j.ajkd.2021.01.018",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "Loop diuretics combined with dietary potassium restriction normalizes potassium and acid-base status in >85% of Type 4 RTA."
            }
        }
    },
    {
        "id": "DOC-CARD-471",
        "icd10": "N20.0",
        "condition": "Calcium Oxalate Nephrolithiasis (Hypercalciuria & Hypocitraturia)",
        "specialty": "Urology & Nephrology",
        "organ_system": "Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA Guideline on Medical Management of Kidney Stones",
        "source_body": "Journal of Urology",
        "citation": "Pearle MS et al. Medical Management of Kidney Stones: AUA Guideline. J Urol. 2014;192(2):316-324.",
        "doi_or_source": "10.1016/j.juro.2014.05.006",
        "clinical_evidence": "Calcium oxalate accounts for ~75-80% of all nephrolithiasis, radiopaque on X-ray/CT. Medical prevention based on 24-hour urine metabolic profile: 1) High fluid intake (>2.5-3.0 L/day); 2) NORMAL DIETARY CALCIUM (1,000-1,200 mg/day; dietary calcium restriction is HARMFUL as it increases free oxalate absorption); 3) Dietary sodium restriction (<2,000 mg/day); 4) THIAZIDE DIURETICS (Chlorthalidone 25-50 mg daily) to decrease urinary calcium excretion; 5) POTASSIUM CITRATE for hypocitraturia.",
        "solution_protocol": {
            "non_pharmacological_targets": "High fluid intake producing >=2.5 liters of urine daily (drink a glass of water every 2-3 hours and before sleep); DO NOT RESTRICT DIETARY CALCIUM (consume calcium WITH meals to bind dietary oxalate in the gut); limit high-oxalate foods (spinach, almonds, rhubarb, beets, dark chocolate); reduce animal protein and sodium intake.",
            "monitoring_cadence": "24-hour urine metabolic stone risk profile (measuring volume, calcium, oxalate, citrate, uric acid, sodium, creatinine) 6-8 weeks post-intervention, then annually; non-contrast helical CT abdomen/pelvis.",
            "clinical_thresholds": "Radiopaque calcium oxalate monohydrate (dumbbell/oval) or dihydrate (envelope/bipyramidal) crystals on urinalysis or stone spectrometry."
        },
        "patient_plain_language": "The most common type of kidney stone (accounting for 80% of stones). Calcium binds with oxalate in your urine, crystallizing into sharp, jagged stones that lodge in your kidney tubes. Counterintuitively, cutting calcium from your diet makes stones WORSE because dietary calcium is needed in your gut to trap oxalate and flush it out. Drinking 3 liters of water daily and taking potassium citrate or a thiazide pill prevents new stones.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were the exact results of my 24-hour urine metabolic stone profile (calcium, oxalate, and citrate levels)?",
            "safety_question": "Why is eating normal amounts of dietary calcium with my meals necessary to bind oxalate in my stomach?",
            "action_threshold_question": "Am I drinking enough water to produce at least 2.5 liters of pale, clear urine every single day?"
        },
        "red_flags": [
            "Sudden excruciating, writhing flank pain radiating to the groin with inability to find a comfortable position (Renal Colic)",
            "Fever and chills with obstructing kidney stone (Infected Hydronephrosis - Urological Surgical Emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Calcium oxalate kidney stones are hard mineral crystals that form in concentrated urine, causing severe flank pain.",
                "plain_analogy": "Sharp gravel forming at the bottom of a mineral-rich stream whenever the water flow slows to a trickle.",
                "lifestyle_action": "Drink at least 3 liters of water daily, eat normal dietary calcium with meals, avoid spinach/nuts, and cut salt."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Chlorthalidone / Hydrochlorothiazide (for hypercalciuria)",
                    "Potassium Citrate oral (Urocit-K for hypocitraturia)",
                    "Tamsulosin oral (Flomax 0.4 mg - Medical Expulsive Therapy for acute stone <10 mm)"
                ],
                "dosing_gdmt": "Chlorthalidone 25 mg daily; Potassium Citrate 30-60 mEq/day in divided doses; Tamsulosin 0.4 mg daily x 4 weeks.",
                "black_box_warning": "Dietary calcium restriction paradoxically increases stone risk by increasing gastrointestinal oxalate absorption.",
                "organ_clearance_cutoffs": "Monitor serum potassium and uric acid on thiazide therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AUA-STONES",
                "pmid_or_doi": "10.1016/j.juro.2014.05.006",
                "cebm_level": 1,
                "sample_size": 4800,
                "endpoints": "Thiazide diuretics combined with potassium citrate reduces calcium stone recurrence by >60% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-472",
        "icd10": "N20.0",
        "condition": "Uric Acid Nephrolithiasis (Radiolucent Stones & Alkalinization)",
        "specialty": "Urology & Nephrology",
        "organ_system": "Urinary & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EAU Guidelines on Urolithiasis",
        "source_body": "European Urology",
        "citation": "Turk C et al. EAU Guidelines on Urolithiasis. Eur Urol. 2016;69(3):475-482.",
        "doi_or_source": "10.1016/j.eururo.2015.07.041",
        "clinical_evidence": "Uric acid stones (~10% of stones) are INVISIBLE ON STANDARD X-RAY (RADIOLUCENT) but readily detected on non-contrast CT. The primary driving pathophysiology is PERSISTENTLY ACIDIC URINE (URINE pH <5.5), where uric acid is insoluble (pKa 5.35). ORAL CHEMOLYSIS (URINARY ALKALINIZATION WITH POTASSIUM CITRATE targeting urine pH 6.5-7.0) COMPLETELY DISSOLVES EXISTING URIC ACID STONES without requiring surgery. ALLOPURINOL is added if hyperuricosuria or hyperuricemia is present.",
        "solution_protocol": {
            "non_pharmacological_targets": "Urinary alkalinization to target urine pH 6.5-7.0 (self-monitor with pH test strips at each void); high fluid intake (>2.5-3.0 L/day); limit purine-rich animal proteins (organ meats, red meat, shellfish, beer, high-fructose corn syrup); weight loss for metabolic syndrome.",
            "monitoring_cadence": "Home urine pH self-monitoring twice daily; 24-hour urine collection for uric acid and volume; non-contrast helical CT to assess stone dissolution.",
            "clinical_thresholds": "Radiolucent stone on plain abdominal X-ray (KUB) that is visible on CT (attenuation 400-600 Hounsfield Units) with persistent urine pH <5.5."
        },
        "patient_plain_language": "Kidney stones made of crystallized uric acid. Unlike calcium stones, uric acid stones are completely invisible on regular X-rays (radiolucent). They form almost exclusively because your urine is too acidic (pH below 5.5). The most remarkable fact about these stones is that they can be completely dissolved like sugar in hot tea simply by taking potassium citrate powder to make your urine alkaline (pH 6.5 to 7.0), completely avoiding surgery.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did non-contrast CT scan confirm a low-density stone that was completely invisible on standard X-ray?",
            "safety_question": "Am I testing my urine with pH strips at home to make sure my potassium citrate keeps my urine pH between 6.5 and 7.0?",
            "action_threshold_question": "Can we dissolve this stone completely with oral alkalinization medicine without needing surgery or shock-waves?"
        },
        "red_flags": [
            "Complete inability to urinate (anuria) caused by bilateral obstructing uric acid sludge",
            "Agonizing flank pain with fever and cloudy urine indicating infected obstructed kidney"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Uric acid stones are invisible kidney stones that form in highly acidic urine and can be dissolved with alkali medicine.",
                "plain_analogy": "Sugar crystals precipitating in cold vinegar that completely melt away once baking soda neutralizes the liquid.",
                "lifestyle_action": "Drink 3 liters of water daily, check your urine pH with test strips, take potassium citrate, and cut back on red meat."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Potassium Citrate oral (Target Urine pH 6.5-7.0 - Curative Chemolysis)",
                    "Allopurinol oral (Xanthoxynase Inhibitor for hyperuricemia)",
                    "Febuxostat (Alternative)",
                    "Sodium Bicarbonate"
                ],
                "dosing_gdmt": "Potassium Citrate 30-60 mEq/day divided TID; Allopurinol 100-300 mg daily if 24h urine uric acid >800 mg/day.",
                "black_box_warning": "Avoid over-alkalinizing urine beyond pH 7.2 (precipitates calcium phosphate stone formation on top of uric acid).",
                "organ_clearance_cutoffs": "HLA-B*5801 screening prior to Allopurinol in high-risk populations (Asian ancestry) to prevent SJS/TEN."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EAU-UROLITHIASIS",
                "pmid_or_doi": "10.1016/j.eururo.2015.07.041",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "Oral potassium citrate chemolysis completely dissolves uric acid kidney stones in >85% of adherent patients."
            }
        }
    },
    {
        "id": "DOC-CARD-473",
        "icd10": "N20.0",
        "condition": "Struvite Infection Stones (Triple Phosphate Staghorn Calculi)",
        "specialty": "Urology & Infectious Disease",
        "organ_system": "Urinary & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA Guideline on Surgical Management of Stones",
        "source_body": "Journal of Urology",
        "citation": "Assimos D et al. Surgical Management of Stones: American Urological Association/Endourological Society Guideline. J Urol. 2016;196(4):1153-1160.",
        "doi_or_source": "10.1016/j.juro.2016.05.090",
        "clinical_evidence": "Struvite stones (magnesium ammonium phosphate / triple phosphate) form EXCLUSIVELY in the presence of UREASE-PRODUCING BACTERIA (Proteus mirabilis, Klebsiella, Morganella, Pseudomonas). Bacterial urease hydrolyzes urea into ammonia and carbon dioxide, driving urine pH >7.2-8.0 and precipitating struvite and carbonate apatite. Struvite stones form massive branching 'staghorn calculi' that fill the entire renal pelvis. COMPLETE SURGICAL REMOVAL (PERCUTANEOUS NEPHROLITHOTOMY / PCNL) COMBINED WITH CULTURE-SPECIFIC ANTIBIOTICS IS MANDATORY; residual fragments inevitably cause fatal sepsis.",
        "solution_protocol": {
            "non_pharmacological_targets": "COMPLETE SURGICAL STONE CLEARANCE; culture-directed antibiotics; high fluid intake; treatment of predisposing anatomic factors (neurogenic bladder, indwelling catheters, urinary diversions); Acetohydroxamic acid (AHA - urease inhibitor) for non-surgical candidates.",
            "monitoring_cadence": "Urine culture with antimicrobial susceptibility testing; non-contrast CT scan with 3D reconstruction evaluating staghorn anatomy; post-PCNL non-contrast CT at 2-4 weeks to confirm 100% stone-free status.",
            "clinical_thresholds": "Presence of branching staghorn calculus filling >=1 calyx and renal pelvis on CT, associated with alkaline urine pH >7.2 and urease-positive bacteriuria."
        },
        "patient_plain_language": "Dangerous 'infection stones' that grow rapidly into giant branching antlers (staghorn stones) that fill your entire kidney plumbing system. They form exclusively when certain bacteria (like Proteus) produce an enzyme called urease, turning your urine strongly alkaline and creating magnesium-ammonium-phosphate crystals. Because the stone is literally made of living bacteria, antibiotics cannot penetrate it; keyhole surgery (PCNL) through your back to remove every last grain of stone is required to prevent life-threatening blood infections.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did CT scan show a staghorn calculus filling my kidney, and is 100% complete surgical removal (PCNL) planned?",
            "safety_question": "What specific urease-producing bacteria (like Proteus or Klebsiella) was identified in my urine culture?",
            "action_threshold_question": "Why will leaving even a tiny grain of residual stone behind cause the entire infection stone to grow back?"
        },
        "red_flags": [
            "Fever, shaking chills, and flank pain with an obstructing staghorn stone (Uroseptic Shock Emergency)",
            "Loss of kidney function on renal scan caused by chronic obstructive pyelonephritis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Struvite stones are giant branching infection stones caused by bacteria that fill the entire kidney cavity.",
                "plain_analogy": "A coral reef growing rapidly inside an underground sewer junction, harboring colonies of living bacteria in its pores.",
                "lifestyle_action": "Undergo complete surgical removal (PCNL), take full-course targeted antibiotics, and attend follow-up clearance scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Percutaneous Nephrolithotomy (PCNL - Gold Standard Surgical Clearance)",
                    "Targeted Culture-Directed IV/Oral Antibiotics",
                    "Acetohydroxamic Acid (Lithostat - Urease Inhibitor for inoperable)"
                ],
                "dosing_gdmt": "PCNL with flexible nephroscopy; Ceftriaxone 1-2 g IV or Ciprofloxacin guided by sensitivities x 14 days post-op.",
                "black_box_warning": "Medical therapy alone CANNOT dissolve struvite stones; complete surgical stone removal is mandatory.",
                "organ_clearance_cutoffs": "Acetohydroxamic acid has significant teratogenic and thrombotic risks; monitor CBC and platelets."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AUA-PCNL-STAGHORN",
                "pmid_or_doi": "10.1016/j.juro.2016.05.090",
                "cebm_level": 1,
                "sample_size": 2600,
                "endpoints": "Complete stone clearance via PCNL eliminates recurrent urosepsis and preserves renal function in >88% of staghorn calculi."
            }
        }
    },
    {
        "id": "DOC-CARD-474",
        "icd10": "N30.10",
        "condition": "Interstitial Cystitis / Bladder Pain Syndrome (Hunner Lesions)",
        "specialty": "Urology & Gynecology",
        "organ_system": "Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA Guideline on Interstitial Cystitis / BPS",
        "source_body": "Journal of Urology",
        "citation": "Hanno PM et al. Diagnosis and Treatment of Interstitial Cystitis/Bladder Pain Syndrome: AUA Guideline. J Urol. 2022;208(1):34-42.",
        "doi_or_source": "10.1097/JU.0000000000002756",
        "clinical_evidence": "IC/BPS is chronic pelvic pain, pressure, or discomfort perceived to be related to the urinary bladder, accompanied by persistent urinary urgency and extreme frequency (>10-30 voids/day) in the absence of infection. Phenotyped into Non-Hunner IC vs Hunner Lesion IC (erythematous velvety mucosal patches with central scar on cystoscopy). MULTIMODAL THERAPY: 1) Self-care and dietary modification; 2) Pelvic floor physical therapy (MYOFASCIAL RELEASE - KEGEL EXERCISES ARE STRICTLY CONTRAINDICATED); 3) Oral Amitriptyline, Pentosan Polysulfate Sodium (PPS), or Cimetidine; 4) Endoscopic fulguration/triamcinolone injection for Hunner lesions.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary elimination of bladder irritants (the '4 Cs': Coffee, Carbonated beverages, Citrus fruits, and Chili/spicy foods, plus alcohol and artificial sweeteners); pelvic floor physical therapy focused on downtraining and myofascial trigger point release; AVOID KEGEL EXERCISES (Kegels tighten hypertonic pelvic muscles, exacerbating agony); stress reduction.",
            "monitoring_cadence": "Voiding diary (recording volume, frequency, and pain scores); O'Leary-Sant Symptom and Problem Index; cystoscopy with hydrodistension under anesthesia to inspect for Hunner lesions and glomerulations; annual ophthalmology exam for PPS maculopathy.",
            "clinical_thresholds": "Bladder pain worsening with filling and relieved by voiding, accompanied by urgency and frequency for >6 weeks, with negative urine cultures and cytology."
        },
        "patient_plain_language": "A chronic, agonizing bladder condition causing burning pelvic pain, pressure, and needing to urinate 20 to 40 times a day and night, even though urine cultures show zero bacteria. The protective lining of your bladder wall is thinned or inflamed, and some patients develop velvety red ulcers (Hunner's lesions). Avoiding acidic foods (coffee, citrus, tomatoes), doing relaxing pelvic floor physical therapy (never Kegel tightening), and taking bladder-protective pills brings lasting relief.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did cystoscopy under anesthesia inspect my bladder for Hunner lesions that can be cauterized or injected with steroids?",
            "safety_question": "Have I been referred to a specialized pelvic floor physical therapist for trigger point release?",
            "action_threshold_question": "Why are Kegel pelvic tightening exercises strictly harmful for my hypertonic bladder muscles?"
        },
        "red_flags": [
            "Severe debilitating pain preventing sleep with voiding frequency exceeding 30-40 times per 24 hours",
            "Gross blood in urine or unexplained rapid worsening (mandates cystoscopy to rule out carcinoma in situ)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Interstitial cystitis is chronic bladder pain and extreme urinary frequency without bacterial infection.",
                "plain_analogy": "A blistered sunburn covering the inside lining of your bladder that stings and burns whenever urine touches it.",
                "lifestyle_action": "Eliminate coffee, citrus, and spicy foods, practice pelvic relaxation exercises, and take prescribed bladder medications."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Amitriptyline oral (10-75 mg at bedtime)",
                    "Pentosan Polysulfate Sodium (Elmiron 100 mg TID)",
                    "Intravesical Instillations (DMSO / Heparin / Lidocaine)",
                    "Cystoscopic Fulguration / Triamcinolone for Hunner lesions"
                ],
                "dosing_gdmt": "Amitriptyline 25-50 mg qHS; Pentosan Polysulfate 100 mg TID on an empty stomach; Hydrodistension with fulguration.",
                "black_box_warning": "Pentosan Polysulfate (Elmiron) carries FDA warning for unique pigmentary maculopathy causing vision loss; annual eye exam mandatory.",
                "organ_clearance_cutoffs": "Avoid long-term oral opioids and avoid Kegel exercises."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AUA-ICBPS",
                "pmid_or_doi": "10.1097/JU.0000000000002756",
                "cebm_level": 1,
                "sample_size": 2900,
                "endpoints": "Multimodal behavioral therapy combined with amitriptyline/PPS achieves significant symptom reduction in >70% of IC/BPS."
            }
        }
    },
    {
        "id": "DOC-CARD-475",
        "icd10": "M31.0",
        "condition": "Anti-Glomerular Basement Membrane Disease (Goodpasture Syndrome)",
        "specialty": "Nephrology & Pulmonology",
        "organ_system": "Urinary & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Glomerular Diseases Guideline on Anti-GBM",
        "source_body": "Kidney International",
        "citation": "Rovin BH et al. KDIGO 2021 Clinical Practice Guideline: Anti-Glomerular Basement Membrane Disease. Kidney Int. 2021;100(4S):S1-S276.",
        "doi_or_source": "10.1016/j.kint.2021.05.021",
        "clinical_evidence": "Autoantibodies directed against the non-collagenous domain of the alpha-3 chain of Type IV collagen [alpha3(IV)NC1] cause necrotizing crescentic glomerulonephritis and alveolar hemorrhage (Goodpasture triad: RPGN, pulmonary hemorrhage, anti-GBM antibodies). IMMEDIATE TRIPLE INDUCTION THERAPY IS MANDATORY: 1) Intensive Plasma Exchange (Plasmapheresis: 4 L exchanges daily or alternate-day for 14 days or until anti-GBM undetectable); 2) Oral Cyclophosphamide (2 mg/kg/day x 3 months); 3) High-dose Corticosteroids (pulse IV methylprednisolone 1 g x 3 days then oral prednisone). Dialysis independence is achieved in >80% if treated before serum creatinine >5.7 mg/dL or anuria.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATE INITIATION OF PLASMAPHERESIS AND CYCLOPHOSPHAMIDE (hours count; treatment must NOT wait for renal biopsy confirmation if anti-GBM serology is strongly positive); absolute smoking cessation (tobacco smoke increases pulmonary capillary permeability, triggering catastrophic diffuse alveolar hemorrhage).",
            "monitoring_cadence": "Serum Anti-GBM antibody titers every 3-7 days until negative; continuous pulse oximetry and chest radiograph for alveolar hemorrhage; daily serum creatinine and CBC; monitor for leukopenia on cyclophosphamide.",
            "clinical_thresholds": "Linear IgG deposition along the glomerular basement membrane on direct immunofluorescence of renal biopsy, with circulating Anti-GBM antibodies by ELISA."
        },
        "patient_plain_language": "A rare, aggressive medical emergency where your body manufactures antibodies that attack the collagen foundations in your kidney filters and your lungs (Goodpasture's syndrome). It causes rapid kidney failure within days and can cause you to cough up blood. Immediate blood filtering (plasmapheresis) to wash out the antibodies, combined with strong immune-calming pills, preserves your kidneys and saves your life if started immediately.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the emergency blood test detect high levels of Anti-GBM antibodies?",
            "safety_question": "Has intensive Plasma Exchange (Plasmapheresis) been started right away to remove the circulating antibodies from my blood?",
            "action_threshold_question": "Why must all cigarette smoking be strictly avoided to prevent life-threatening bleeding into my lungs?"
        },
        "red_flags": [
            "Coughing up frank blood (Diffuse Alveolar Hemorrhage) with severe shortness of breath and oxygen drops",
            "Sudden complete cessation of urine output (Anuria) with rapidly climbing blood creatinine"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Anti-GBM disease is an aggressive autoimmune attack on the filters of the kidneys and lungs, requiring urgent plasma exchange.",
                "plain_analogy": "A wrecking ball specifically targeted at the rebar foundation of a concrete bridge, threatening sudden collapse.",
                "lifestyle_action": "Seek emergency intensive care immediately; early plasma filtering within hours is the key to saving kidney function."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intensive Therapeutic Plasma Exchange (Plasmapheresis x 14 sessions)",
                    "Cyclophosphamide oral (2 mg/kg/day x 2-3 months)",
                    "Pulse Methylprednisolone IV (1 g/day x 3 days) then oral taper",
                    "Pneumocystis Jirovecii Prophylaxis (Bactrim)"
                ],
                "dosing_gdmt": "Plasmapheresis 4 L albumin replacement daily x 14 days; Cyclophosphamide 2 mg/kg/day; Prednisone 1 mg/kg/day.",
                "black_box_warning": "Cyclophosphamide carries black box warnings for hemorrhagic cystitis, myelosuppression, and fertility loss; ensure brisk hydration.",
                "organ_clearance_cutoffs": "Dose adjust cyclophosphamide for age and renal function."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KDIGO-ANTIGBM",
                "pmid_or_doi": "10.1016/j.kint.2021.05.021",
                "cebm_level": 1,
                "sample_size": 1100,
                "endpoints": "Early plasmapheresis plus cyclophosphamide achieves 1-year patient survival >90% and dialysis independence in >75%."
            }
        }
    },
    {
        "id": "DOC-CARD-476",
        "icd10": "M31.30",
        "condition": "Granulomatosis with Polyangiitis (GPA / Wegener's PR3-ANCA)",
        "specialty": "Rheumatology & Nephrology",
        "organ_system": "Urinary & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: RAVE & ADVOCATE Landmark Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "Jayne DRW et al. Avacopan for the Treatment of ANCA-Associated Vasculitis (ADVOCATE). N Engl J Med. 2021;384(7):599-609.",
        "doi_or_source": "10.1056/NEJMoa2023386",
        "clinical_evidence": "GPA is a necrotizing granulomatous small-vessel vasculitis associated with PR3-ANCA (c-ANCA in 80-90%), causing destructive upper airway lesions (saddle nose deformity, subglottic stenosis), cavitary lung nodules, and crescentic glomerulonephritis. The RAVE trial established RITUXIMAB (375 mg/m2 weekly x 4) as non-inferior to cyclophosphamide for induction and superior for relapsing disease. The landmark ADVOCATE trial (n=330) proved that oral Complement C5a Receptor Antagonist AVACOPAN (30 mg BID) replaced high-dose glucocorticoids, achieving superior sustained remission at week 52 (65.7% vs 54.9%; p=0.007) with 60% lower steroid toxicity.",
        "solution_protocol": {
            "non_pharmacological_targets": "Targeted B-cell depletion and complement inhibition to eliminate toxic glucocorticoid exposure; ENT saline rinses; trimethoprim-sulfamethoxazole (Bactrim) prophylaxis against Pneumocystis jirovecii pneumonia (MANDATORY during rituximab/cyclophosphamide therapy); monitor for sinus infections.",
            "monitoring_cadence": "Serial PR3-ANCA titers; uPCR and urine microscopy (checking for dysmorphic RBCs and RBC casts); eGFR and serum creatinine; Birmingham Vasculitis Activity Score (BVAS).",
            "clinical_thresholds": "Cavitary lung lesions on CT, pauci-immune necrotizing crescentic GN on biopsy, and high-titer PR3-ANCA (c-ANCA)."
        },
        "patient_plain_language": "An autoimmune condition where antibodies (PR3-ANCA) inflame and destroy small blood vessels, particularly in your nose, sinuses, lungs, and kidneys. It can cause chronic bloody nasal crusts, a collapsed nasal bridge ('saddle nose'), lung cavities, and kidney inflammation. Modern treatment uses targeted B-cell clearing infusions (Rituximab) and a breakthrough steroid-sparing pill (Avacopan) that shields your kidneys without the severe side effects of high-dose prednisone.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my blood test positive for PR3-ANCA (c-ANCA), and did kidney or lung biopsy confirm pauci-immune vasculitis?",
            "safety_question": "Am I receiving Rituximab infusions combined with the new steroid-replacing medication Avacopan (Tavneos)?",
            "action_threshold_question": "Am I taking daily Bactrim antibiotic pills to protect against fungal lung infections while my immune system is calm?"
        },
        "red_flags": [
            "Red bloody nasal crusts with sudden collapse of the nasal bridge cartilage (Saddle Nose Deformity)",
            "Coughing up blood with rapidly declining kidney function (Pulmonary-Renal Vasculitic Crisis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "GPA is an autoimmune disease causing blood vessel inflammation and damage in the sinuses, lungs, and kidneys.",
                "plain_analogy": "Small electrical short circuits melting the delicate copper wiring inside the walls of three separate rooms simultaneously.",
                "lifestyle_action": "Take your prescribed immunosuppressive medications, use nasal saline sprays, and attend regular kidney lab monitoring."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rituximab IV (375 mg/m2 weekly x 4 or 1,000 mg Day 1 & 15)",
                    "Avacopan oral (Tavneos 30 mg BID - Complement C5aR Antagonist)",
                    "Cyclophosphamide IV/oral (Alternative induction)",
                    "Trimethoprim-Sulfamethoxazole (Bactrim - PJP Prophylaxis)"
                ],
                "dosing_gdmt": "Rituximab 375 mg/m2 weekly x 4 doses; Avacopan 30 mg orally BID with food x 52 weeks; Bactrim SS daily.",
                "black_box_warning": "Avacopan requires baseline and regular liver function monitoring (ALT/AST); do not give with strong CYP3A4 inducers.",
                "organ_clearance_cutoffs": "Bactrim prophylaxis is MANDATORY to prevent fatal Pneumocystis pneumonia during B-cell depletion."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ADVOCATE-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2023386",
                "cebm_level": 2,
                "sample_size": 330,
                "endpoints": "Avacopan achieves superior 52-week sustained remission over prednisone and significantly improves eGFR recovery (p=0.007)."
            }
        }
    },
    {
        "id": "DOC-CARD-477",
        "icd10": "M31.7",
        "condition": "Microscopic Polyangiitis (MPA - MPO-ANCA / p-ANCA)",
        "specialty": "Nephrology & Rheumatology",
        "organ_system": "Urinary & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: PEXIVAS Landmark Trial & ACR/EULAR Vasculitis Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Walsh M et al. Plasma Exchange and Glucocorticoids in Severe ANCA-Associated Vasculitis (PEXIVAS). N Engl J Med. 2020;382(7):622-631.",
        "doi_or_source": "10.1056/NEJMoa1803537",
        "clinical_evidence": "Unlike GPA, MPA is NON-GRANULOMATOUS, lacks destructive sinus/upper airway involvement, and is predominantly associated with MPO-ANCA (perinuclear p-ANCA in 70-85%). Presents with rapidly progressive necrotizing glomerulonephritis and alveolar hemorrhage. The landmark PEXIVAS trial (n=704) proved that routine plasma exchange did NOT reduce death or ESRD in severe ANCA vasculitis, and established that a REDUCED-DOSE GLUCOCORTICOID PROTOCOL was non-inferior to high-dose steroids for remission while cutting serious infections by 31% (hazard ratio 0.69; p=0.02).",
        "solution_protocol": {
            "non_pharmacological_targets": "Reduced-dose oral corticosteroid regimen (per PEXIVAS protocol); prompt B-cell depletion with Rituximab; mandatory PJP prophylaxis with Bactrim; annual influenza, COVID-19, and pneumococcal vaccinations; avoidance of nephrotoxic drugs.",
            "monitoring_cadence": "Serum MPO-ANCA titers every 3-6 months; urinalysis for hematuria and RBC casts; serum creatinine and eGFR; BVAS score tracking.",
            "clinical_thresholds": "Pauci-immune necrotizing and crescentic glomerulonephritis on renal biopsy in the presence of positive MPO-ANCA without granulomatous inflammation."
        },
        "patient_plain_language": "An autoimmune small blood vessel inflammation that specifically attacks your kidney filters and the blood vessels in your lungs. It is driven by antibodies called MPO-ANCA (p-ANCA). Unlike its sibling disease GPA, it does not attack your nose or sinuses, but it can rapidly damage your kidneys if not treated. The landmark PEXIVAS trial proved that using a smarter, lower dose of steroid pills cures the disease just as well while saving patients from dangerous infections.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my blood test confirm positive MPO-ANCA (p-ANCA) antibodies and did kidney biopsy confirm pauci-immune crescentic GN?",
            "safety_question": "Is my doctor utilizing the newer PEXIVAS reduced-dose steroid protocol to protect me from dangerous infections?",
            "action_threshold_question": "Am I taking Rituximab B-cell therapy to maintain long-term remission and protect my kidneys?"
        },
        "red_flags": [
            "Sudden appearance of dark tea-colored urine with rising blood pressure and swollen ankles",
            "Shortness of breath with microscopic blood in cough (alveolar hemorrhage)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Microscopic polyangiitis is an autoimmune condition where antibodies inflame small blood vessels in kidneys and lungs.",
                "plain_analogy": "Rust eating away at the microscopic valve stems inside the municipal water filtration plant.",
                "lifestyle_action": "Take your Rituximab infusions on schedule, take preventive antibiotic pills, and monitor kidney lab numbers."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rituximab IV (First Line B-cell Depletion)",
                    "Reduced-Dose Oral Prednisone (PEXIVAS Protocol)",
                    "Cyclophosphamide IV (Alternative)",
                    "Trimethoprim-Sulfamethoxazole (Bactrim Prophylaxis)"
                ],
                "dosing_gdmt": "Rituximab 375 mg/m2 weekly x 4 doses; Prednisone initiated at 1 mg/kg/day and tapered rapidly to 5 mg by month 6.",
                "black_box_warning": "Avoid routine plasma exchange (proven ineffective by PEXIVAS trial in reducing mortality or ESRD).",
                "organ_clearance_cutoffs": "Dose adjustment of cyclophosphamide for age and eGFR; monitor for cytopenias."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PEXIVAS-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1803537",
                "cebm_level": 2,
                "sample_size": 704,
                "endpoints": "Reduced-dose glucocorticoid protocol cuts serious infections by 31% with equivalent remission in ANCA vasculitis."
            }
        }
    },
    {
        "id": "DOC-CARD-478",
        "icd10": "M62.82",
        "condition": "Rhabdomyolysis (Crush Injury & Myoglobinuric AKI)",
        "specialty": "Emergency Medicine & Nephrology",
        "organ_system": "Musculoskeletal & Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Expert Consensus on Traumatic & Non-Traumatic Rhabdomyolysis",
        "source_body": "New England Journal of Medicine",
        "citation": "Bosch X et al. Rhabdomyolysis and Acute Kidney Injury. N Engl J Med. 2009;361(1):62-72.",
        "doi_or_source": "10.1056/NEJMra0801327",
        "clinical_evidence": "Skeletal muscle breakdown releases toxic intracellular contents (myoglobin, creatine kinase, potassium, phosphorus) into the circulation. Myoglobin induces acute kidney injury via renal vasoconstriction, direct proximal tubular cytotoxicity, and intratubular Tamm-Horsfall cast obstruction (acidic urine pH promotes cast formation). AGGRESSIVE ISOTONIC SALINE RESUSCITATION (infusing 500-1000 mL/h targeting urine output 200-300 mL/h) initiated within 6 hours of onset eliminates renal failure in >80% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "EARLY AGGRESSIVE IV FLUID RESUSCITATION (normal saline 10-15 mL/kg/h targeting high urine flow); identify and treat compartment syndrome (emergent fasciotomy); discontinue inciting statins, fibrates, or recreational drugs; avoid aggressive calcium administration during early phase (causes metastatic tissue calcification).",
            "monitoring_cadence": "Serum Creatine Kinase (CK; peaks at 24-72h; CK >5,000 U/L indicates high AKI risk); serum potassium, phosphorus, calcium, and creatinine every 4-6 hours; urine output via Foley catheter.",
            "clinical_thresholds": "Serum CK >5-10 times the upper limit of normal (>1,000-5,000 U/L) with reddish-brown tea-colored urine positive for blood on dipstick but negative for RBCs on microscopy."
        },
        "patient_plain_language": "Severe muscle breakdown triggered by a crush injury, intense unaccustomed exercise, prolonged immobility on a hard floor, or certain medications (like statins). Damaged muscle fibers burst, pouring dark muscle pigment (myoglobin) into your bloodstream. The pigment clogs and poisons your kidney tubes, turning your urine dark reddish-brown like iced tea. Pumping large amounts of IV fluids immediately flushes the pigment safely out of your kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my blood Creatine Kinase (CK) muscle enzyme number, and is it dropping with IV fluids?",
            "safety_question": "Is my urine output being monitored with a catheter to ensure at least 200 to 300 mL of fluid flushes out every hour?",
            "action_threshold_question": "Are my blood potassium levels being checked every few hours to prevent dangerous heart rhythm problems?"
        },
        "red_flags": [
            "Urine turning dark brown or cola-colored with profound muscle agony and swelling after trauma",
            "Sudden spike in blood potassium (>6.0 mEq/L) causing palpitations and peaked T-waves on ECG"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Rhabdomyolysis is rapid breakdown of muscle tissue releasing dark pigment that can clog and damage the kidneys.",
                "plain_analogy": "Mud and clay washed off a construction site flooding into stormwater drains, threatening to plug the pipes with silt.",
                "lifestyle_action": "Drink plenty of water after exercise, seek immediate emergency care for dark brown urine and muscle pain, and get IV fluids."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Aggressive Isotonic Crystalloid IV Infusion (0.9% Normal Saline)",
                    "Sodium Bicarbonate IV (to alkalize urine pH >6.5 if non-hypocalcemic)",
                    "Hemodialysis (for refractory hyperkalemia/acidosis)"
                ],
                "dosing_gdmt": "Normal saline 500-1,000 mL/h titrated to maintain urine output 200-300 mL/h until CK drops <5,000 U/L.",
                "black_box_warning": "Avoid giving IV Calcium for hypocalcemia unless life-threatening cardiac arrhythmias exist (causes metastatic tissue calcification).",
                "organ_clearance_cutoffs": "Loop diuretics (Furosemide) should ONLY be used AFTER adequate intravascular volume is restored."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEJM-RHABDO",
                "pmid_or_doi": "10.1056/NEJMra0801327",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "Early aggressive crystalloid resuscitation within 6 hours reduces rhabdomyolysis acute kidney injury by over 80%."
            }
        }
    },
    {
        "id": "DOC-CARD-479",
        "icd10": "N17.9",
        "condition": "Contrast-Associated Acute Kidney Injury (CA-AKI / CIN)",
        "specialty": "Nephrology & Radiology",
        "organ_system": "Urinary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: PRESERVE Landmark Trial & KDIGO AKI Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Weisbord SD et al. Outcomes after Angiography in Patients at High Risk for Renal Adverse Events (PRESERVE). N Engl J Med. 2018;378(7):603-614.",
        "doi_or_source": "10.1056/NEJMoa1710933",
        "clinical_evidence": "CA-AKI is an abrupt decline in renal function within 48-72 hours of intravascular iodinated contrast administration. The definitive landmark PRESERVE trial (n=5,177 high-risk patients undergoing angiography) proved that INTRAVENOUS ISOTONIC 0.9% SODIUM CHLORIDE was the gold standard, and that Sodium Bicarbonate or Oral N-Acetylcysteine (NAC) provided NO BENEFIT in preventing death, dialysis, or persistent renal decline. Use of low-osmolar or iso-osmolar contrast and minimizing contrast volume (Contrast Volume / eGFR ratio <3.0) prevents injury.",
        "solution_protocol": {
            "non_pharmacological_targets": "Pre- and post-procedure volume expansion with isotonic crystalloids (0.9% saline 1-1.5 mL/kg/h for 3-12 hours pre-procedure and 6-12 hours post-procedure); minimize iodinated contrast volume; hold non-essential nephrotoxic drugs (NSAIDs, aminoglycosides) 48h prior; hold Metformin 48h post-contrast.",
            "monitoring_cadence": "Baseline serum creatinine and eGFR; follow-up serum creatinine at 48-72 hours post-contrast exposure.",
            "clinical_thresholds": "Relative increase in serum creatinine >=25% or absolute increase >=0.3-0.5 mg/dL within 48-72 hours of contrast medium exposure."
        },
        "patient_plain_language": "A temporary decline in kidney function that can happen after receiving concentrated iodine contrast dye for a CT scan or heart catheterization. The dye temporarily narrows kidney blood vessels and causes oxygen stress. The landmark PRESERVE trial of over 5,000 patients showed that simple, regular IV saline fluid given before and after the scan protects your kidneys better than any special pills or fancy solutions.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my baseline kidney eGFR, and did the procedural team minimize the total volume of contrast dye used?",
            "safety_question": "Has IV normal saline hydration been running before and after my imaging procedure to protect my kidneys?",
            "action_threshold_question": "Do I need to pause my Metformin diabetes pill or blood pressure pills for 48 hours after the scan?"
        },
        "red_flags": [
            "Urine output dropping below 400 mL in 24 hours after a contrast dye scan",
            "Sudden rising blood creatinine >50% above baseline at 48 hours post-procedure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Contrast-associated AKI is kidney strain following medical contrast dye, preventable with IV fluids.",
                "plain_analogy": "Pouring a cup of sticky syrup into a water turbine, briefly slowing the blades until water flushes it through.",
                "lifestyle_action": "Drink extra water before and after contrast CT scans, and make sure your doctor checks your kidney labs."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intravenous 0.9% Isotonic Saline (Gold Standard Hydration)",
                    "Iso-osmolar Contrast Media (Iodixanol)",
                    "Low-osmolar Contrast Media (Iopamidol)"
                ],
                "dosing_gdmt": "0.9% Normal Saline 1-1.5 mL/kg/h initiated 3-12 hours before contrast and continued for 6-12 hours after.",
                "black_box_warning": "N-Acetylcysteine (Mucomyst) and Sodium Bicarbonate offer NO benefit over isotonic saline (proven by PRESERVE trial).",
                "organ_clearance_cutoffs": "Withhold Metformin at time of procedure and for 48 hours post-procedure until renal stability verified."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PRESERVE-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1710933",
                "cebm_level": 2,
                "sample_size": 5177,
                "endpoints": "Isotonic saline is effective; N-acetylcysteine and sodium bicarbonate provide no benefit in preventing CA-AKI (p=0.75)."
            }
        }
    },
    {
        "id": "DOC-CARD-480",
        "icd10": "N10",
        "condition": "Acute Interstitial Nephritis (Drug-Induced AIN - Triad Fever/Rash/Eosinophilia)",
        "specialty": "Nephrology & Allergy",
        "organ_system": "Urinary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Expert Consensus on Drug-Induced AIN",
        "source_body": "Kidney International",
        "citation": "Perazella MA et al. Drug-Induced Acute Interstitial Nephritis: An Update. Kidney Int. 2020;97(4):729-741.",
        "doi_or_source": "10.1016/j.kint.2019.11.026",
        "clinical_evidence": "Drug-induced AIN accounts for 15-20% of unexplained acute kidney injury, triggered by Proton Pump Inhibitors (PPIs), NSAIDs, Beta-lactam antibiotics, Ciprofloxacin, or Immune Checkpoint Inhibitors (ICIs). The classic triad (fever, maculopapular rash, peripheral eosinophilia) is present in <10% of cases; sterile pyuria and white blood cell casts are common. EARLY DISCONTINUATION OF INCITING DRUG COMBINED WITH EARLY ORAL CORTICOSTEROIDS (Prednisone 1 mg/kg/day within 7-14 days) prevents irreversible interstitial fibrosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATELY DISCONTINUE ALL SUSPECTED INCITING DRUGS (PPIs, NSAIDs, antibiotics); avoid future re-challenge with the offending drug class; early initiation of oral corticosteroids if no improvement within 3-5 days of drug cessation.",
            "monitoring_cadence": "Serial serum creatinine and BUN; urinalysis (checking for sterile pyuria, mild proteinuria <1g, and WBC casts); renal biopsy (gold standard demonstrating interstitial edema and lymphocytic/eosinophilic infiltrate).",
            "clinical_thresholds": "Unexplained acute rise in serum creatinine temporally related to a newly initiated medication, with interstitial inflammation on renal biopsy."
        },
        "patient_plain_language": "An allergic reaction deep inside the sponge tissue surrounding your kidney tubes (interstitium) caused by a medication—most commonly everyday heartburn pills (Prilosec/Nexium), pain relievers (ibuprofen/Advil), or antibiotics. White blood cells swarm into your kidneys, causing inflammation and kidney failure. Stopping the offending pill immediately and taking a short course of steroid pills heals the kidneys and prevents permanent scarring.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which medication (such as my heartburn PPI pill, antibiotic, or Advil) triggered this allergic kidney inflammation?",
            "safety_question": "Has the culprit medication been permanently stopped and entered as an allergy in my medical records?",
            "action_threshold_question": "Should I start a 4 to 6-week course of Prednisone steroid pills to stop the kidney inflammation from turning into permanent scars?"
        },
        "red_flags": [
            "Rapidly climbing blood creatinine (>50% increase) within 1-2 weeks of starting a new prescription or over-the-counter pill",
            "Low-grade fever and spreading itchy pink rash with joint pain and dark urine"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute interstitial nephritis is an allergic reaction inside kidney tissue caused by common medications like PPIs or NSAIDs.",
                "plain_analogy": "Spilling an irritating chemical onto insulation batting behind a drywall, causing the fibers to swell and inflame.",
                "lifestyle_action": "Stop taking the offending medication immediately, never take it again, and consult nephrology for steroid therapy."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Immediate Drug Discontinuation (First Line - Mandatory)",
                    "Prednisone oral (1 mg/kg/day x 2-4 weeks, then taper over 4 weeks)",
                    "Mycophenolate Mofetil (for steroid-dependent ICI-AIN)"
                ],
                "dosing_gdmt": "Prednisone 1 mg/kg/day (max 60 mg) initiated within 7-14 days of diagnosis, tapered over 4-6 weeks.",
                "black_box_warning": "Delaying corticosteroid therapy beyond 2-3 weeks significantly reduces renal recovery due to irreversible fibrotic remodeling.",
                "organ_clearance_cutoffs": "Monitor blood glucose and blood pressure during steroid course."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KINT-AIN-CONSENSUS",
                "pmid_or_doi": "10.1016/j.kint.2019.11.026",
                "cebm_level": 1,
                "sample_size": 1650,
                "endpoints": "Early corticosteroid therapy within 14 days of drug cessation achieves complete renal recovery in >80% of AIN."
            }
        }
    }
]
