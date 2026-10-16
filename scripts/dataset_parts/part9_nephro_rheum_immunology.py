"""
part9_nephro_rheum_immunology.py
"""

PART_9_DISEASES = [
    {
        "id": "DOC-CARD-261",
        "icd10": "N02.8",
        "condition": "IgA Nephropathy (Berger's Disease)",
        "specialty": "Nephrology",
        "organ_system": "Renal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (TESTING Trial) & NEJM (NefIgArd)",
        "citation": "Lv J et al. Effect of Oral Methylprednisolone on Clinical Outcomes in Patients With IgA Nephropathy: The TESTING Randomized Clinical Trial. JAMA. 2022;327(19):1888-1898.",
        "doi_or_source": "10.1001/jama.2022.6768",
        "clinical_evidence": "In the landmark multicenter Phase 3 TESTING trial (n=503 patients with IgA nephropathy, proteinuria >=1 g/day, and eGFR 20-120 mL/min/1.73m2 despite optimized renin-angiotensin system blockade), reduced-dose oral methylprednisolone (0.4 mg/kg/day with Pneumocystis jirovecii prophylaxis) significantly reduced the primary composite renal outcome (40% eGFR decline, end-stage kidney disease [ESKD], or renal death) by 47% compared with placebo over 4.2 years (hazard ratio 0.53; 95% CI 0.39-0.72; p<0.001). Targeted-release budesonide (Nefecon, NefIgArd trial) and dual endothelin/angiotensin receptor antagonists (sparsentan, PROTECT trial) achieve robust proteinuria reduction (>40%) and preserve eGFR.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction to <2,000 mg/day (enhances antiproteinuric efficacy of RAS inhibitors); moderate dietary protein intake (0.8 g/kg/day); smoking cessation; blood pressure control to <120/80 mmHg.",
            "monitoring_cadence": "Urine protein-to-creatinine ratio (UPCR) or 24-hour urine protein, serum creatinine, and estimated GFR every 1-3 months; blood pressure checks weekly; screen for microscopic hematuria.",
            "clinical_thresholds": "Persistent proteinuria >0.75-1.0 g/day despite >=90 days of maximally tolerated ACEi/ARB and SGLT2i therapy indicates high risk of progression to ESKD, mandating targeted release budesonide or systemic immunosuppression."
        },
        "patient_plain_language": "IgA nephropathy (Berger's disease) is an autoimmune kidney disease where an abnormal form of an antibody called Immunoglobulin A (IgA)—which normally protects you from throat and lung infections—clumps together and gets trapped in the microscopic filters of your kidneys (glomeruli). This causes inflammation, microscopic bleeding into the urine (often turning urine pink or tea-colored during a cold), and slow kidney scarring.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current 24-hour urine protein level (or urine protein-to-creatinine ratio) and my eGFR kidney filtration score?",
            "safety_question": "Am I on maximum guideline-directed kidney protection (an ACE inhibitor/ARB plus an SGLT2 inhibitor like dapagliflozin)?",
            "action_threshold_question": "Would I benefit from gut-targeted budesonide (Tarpeyo) or sparsentan to shut down the abnormal IgA production at the source?"
        },
        "red_flags": [
            "Sudden dark cola-colored or bloody urine (gross hematuria) after a sore throat, new swelling in the eyelids and legs, or blood pressure spiking over 160/100 mmHg"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "IgA nephropathy is an autoimmune kidney disorder in which antibodies called IgA build up in the kidneys, causing inflammation that can damage kidney tissues.",
                "plain_analogy": "Sticky antibody clumps jamming up the microscopic filter screens in your kidneys like sand caught in a pool filter.",
                "lifestyle_action": "Strictly limit salt to under 2,000 mg daily. Maintain blood pressure strictly below 120/80. Avoid smoking."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Budesonide Targeted-Release (Tarpeyo)", "Sparsentan (Filspari)", "Dapagliflozin (Farxiga)", "Lisinopril", "Losartan"],
                "dosing_gdmt": "Tarpeyo 16 mg once daily in the morning for 9 months. Or Sparsentan 200 mg daily (titrated to 400 mg daily). Dapagliflozin 10 mg daily.",
                "black_box_warning": "Sparsentan: Embryo-fetal toxicity and hepatotoxicity; monthly liver transaminases (ALT/AST) and pregnancy tests required.",
                "organ_clearance_cutoffs": "Monitor eGFR and potassium; SGLT2 inhibitors provide nephroprotection down to eGFR >=20 mL/min/1.73m2."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TESTING / NefIgArd",
                "pmid_or_doi": "10.1001/jama.2022.6768",
                "cebm_level": 2,
                "sample_size": 503,
                "endpoints": "Composite of 40% eGFR decline, ESKD, or renal death reduced by 47% with methylprednisolone (HR 0.53; p<0.001); Tarpeyo reduces 2-year eGFR loss by 50%."
            }
        }
    },
    {
        "id": "DOC-CARD-262",
        "icd10": "N04.2",
        "condition": "Membranous Nephropathy",
        "specialty": "Nephrology",
        "organ_system": "Renal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (MENTOR Trial) & KDIGO Guidelines",
        "citation": "Fervenza FC et al. Rituximab or Cyclosporine in the Treatment of Membranous Nephropathy (MENTOR). N Engl J Med. 2019;381(1):36-46.",
        "doi_or_source": "10.1056/NEJMoa1814427",
        "clinical_evidence": "Primary Membranous Nephropathy (pMN) is an autoimmune podocytopathy and the leading cause of primary nephrotic syndrome in adults, driven in 70-80% by circulating autoantibodies against the M-type phospholipase A2 receptor (anti-PLA2R1-Ab) or thrombospondin type-1 domain-containing 7A (anti-THSD7A-Ab). In the landmark randomized MENTOR trial (n=130 patients with proteinuria >=5 g/day despite 3 months of RAS blockade), intravenous rituximab (1,000 mg on days 1 and 15, repeated at 6 months if proteinuria declined by >25%) was noninferior to cyclosporine at 12 months and vastly superior at 24 months in maintaining complete or partial clinical remission (60% rituximab vs 20% cyclosporine; p<0.001). Relapse rates were dramatically lower with rituximab (5% vs 46%). Monitoring anti-PLA2R antibody titers predicts clinical proteinuria remission by 3-6 months.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction (<2,000 mg/day); dietary protein moderation (0.8 g/kg/day); prophylactic anticoagulation for serum albumin <2.0-2.5 g/dL with high thromboembolic risk (CHA2DS2-VASc or Padua score); high-intensity statin.",
            "monitoring_cadence": "Quantitative serum anti-PLA2R antibody titers and 24-hour urine protein at 1, 3, 6, and 12 months; complete remission defined as proteinuria <0.3 g/day with stable eGFR; partial remission as proteinuria <3.5 g/day with >50% reduction from baseline.",
            "clinical_thresholds": "Anti-PLA2R titer >50 RU/mL with nephrotic-range proteinuria (>3.5 g/day) and low serum albumin (<3.0 g/dL) classifies as high or very high risk, requiring immediate immunosuppression with Rituximab or Cyclophosphamide."
        },
        "patient_plain_language": "Membranous nephropathy is an autoimmune kidney disease where your body produces antibodies (most commonly anti-PLA2R antibodies) that attack the outside surface of your kidney's filtering units. The filters become thickened and leaky, allowing large amounts of protein (albumin) to spill out into your urine. Losing this protein causes fluid to pool in your body, producing heavy swelling (edema) in your legs, ankles, and face.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my blood anti-PLA2R antibody titer and my 24-hour urine protein measurement?",
            "safety_question": "Is my blood albumin low enough (below 2.0-2.5 g/dL) that I need a preventative blood thinner to prevent dangerous vein blood clots?",
            "action_threshold_question": "Am I scheduled for B-cell targeted rituximab infusions to turn off the antibody attack?"
        },
        "red_flags": [
            "Sudden swelling and pain in one leg (deep vein thrombosis), sudden chest pain and shortness of breath (pulmonary embolism), or flank pain with blood in urine (renal vein thrombosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Membranous nephropathy is a kidney disorder that leads to changes and inflammation of the structures inside the kidney that help filter wastes and fluids.",
                "plain_analogy": "The kidney's fine mesh filters developing large holes from an antibody attack, letting essential protein leak into the urine.",
                "lifestyle_action": "Strictly limit dietary salt to reduce swelling. Take cholesterol medication. Watch legs closely for deep vein clot swelling."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Rituximab (Rituxan)", "Cyclophosphamide", "Cyclosporine", "Tacrolimus", "Dapagliflozin"],
                "dosing_gdmt": "Rituximab 1,000 mg IV on days 1 and 15 (repeated at 6 months if proteinuria improved by >25% but incomplete remission).",
                "black_box_warning": "Rituximab: Fatal infusion reactions, severe mucocutaneous reactions, hepatitis B reactivation, and progressive multifocal leukoencephalopathy (PML).",
                "organ_clearance_cutoffs": "Screen for hepatitis B (HBsAg and anti-HBc) and latent tuberculosis prior to initiation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MENTOR Trial",
                "pmid_or_doi": "10.1056/NEJMoa1814427",
                "cebm_level": 2,
                "sample_size": 130,
                "endpoints": "24-month sustained remission achieved in 60% with rituximab vs 20% cyclosporine (p<0.001); relapse rate reduced from 46% to 5%."
            }
        }
    },
    {
        "id": "DOC-CARD-263",
        "icd10": "N04.0",
        "condition": "Minimal Change Disease",
        "specialty": "Nephrology",
        "organ_system": "Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Clinical Practice Guideline & Evidence Synthesis",
        "source_body": "Kidney International (KDIGO Glomerular Diseases)",
        "citation": "Rovin BH et al. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276.",
        "doi_or_source": "10.1016/j.kint.2021.05.021",
        "clinical_evidence": "Minimal Change Disease (MCD) is the predominant cause of nephrotic syndrome in children (70-90%) and accounts for 10-15% of adult nephrotic syndrome. It is characterized clinically by abrupt-onset massive selective proteinuria (predominantly albuminuria), profound hypoalbuminemia (<2.5 g/dL), severe generalized anasarca, and hypercholesterolemia, with normal blood pressure and preserved eGFR. Light microscopy reveals normal-appearing glomeruli, immunofluorescence is negative for immune complexes, and electron microscopy demonstrates pathognomonic diffuse effacement of podocyte foot processes. Oral corticosteroids (prednisone 1 mg/kg/day, max 80 mg daily) achieve complete remission in >90% of children (within 4 weeks) and 75-80% of adults (within 12-16 weeks), though 50-70% experience steroid-dependent or frequent relapses requiring calcineurin inhibitors (tacrolimus/cyclosporine) or rituximab.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction (<1,500-2,000 mg/day); dietary protein moderation (0.8-1.0 g/kg/day); loop diuretic titration combined with oral potassium replacement for severe fluid retention; compression stockings.",
            "monitoring_cadence": "Daily first-morning urine dipstick for protein at home (urine protein negative or trace for 3 consecutive days defines remission); weekly body weight tracking; serum albumin, creatinine, and lipid panel every 4 weeks during steroid induction.",
            "clinical_thresholds": "Urine dipstick protein >=3+ for 3 consecutive days signifies disease relapse, requiring immediate restart of full-dose oral corticosteroids."
        },
        "patient_plain_language": "Minimal change disease is a kidney condition that causes your kidneys to suddenly leak massive amounts of protein into your urine. When viewed under an ordinary optical microscope, the kidney filters look almost completely normal (minimal change). However, under a powerful electron microscope, the tiny interlocking foot-like cells (podocytes) that act as the kidney's strainer are swollen and flattened out. Fortunately, it usually responds very quickly to steroid medication.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my 24-hour urine protein level and has my morning home urine dipstick turned completely negative for protein?",
            "safety_question": "What is our precise plan for slowly tapering my oral prednisone over several months once my proteinuria reaches zero?",
            "action_threshold_question": "If my disease relapses when tapering steroids, would a non-steroid medication like rituximab or tacrolimus be appropriate?"
        },
        "red_flags": [
            "Sudden severe abdominal pain with high fever (spontaneous bacterial peritonitis in nephrotic ascites), severe leg pain with swelling (blood clot), or oliguria"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Minimal change disease is a kidney disorder that can lead to nephrotic syndrome, causing large amounts of protein to be lost in the urine.",
                "plain_analogy": "The microscopic foot-pads of the kidney's filter cells flattening out, opening up gaps that dump protein into the urine.",
                "lifestyle_action": "Check first-morning urine protein dipstick daily. Restrict sodium. Weigh yourself every morning to spot fluid accumulation."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone Oral", "Tacrolimus", "Cyclosporine", "Rituximab", "Cyclophosphamide"],
                "dosing_gdmt": "Prednisone 1 mg/kg daily (max 80 mg) until complete remission (minimum 4 weeks; max 16 weeks in adults), followed by a slow 6-month taper.",
                "black_box_warning": "Tacrolimus: Increased risk of serious infections and malignancies (lymphomas); monitor trough blood levels (target 5-10 ng/mL).",
                "organ_clearance_cutoffs": "Provide bone protection (calcium + vitamin D) and gastroprotection (PPI) during high-dose steroid therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KDIGO Glomerular Guidelines",
                "pmid_or_doi": "10.1016/j.kint.2021.05.021",
                "cebm_level": 1,
                "sample_size": 3400,
                "endpoints": "Steroid therapy achieves complete remission in >80% of adults within 16 weeks; rituximab achieves 75% relapse-free survival in steroid-dependent disease."
            }
        }
    },
    {
        "id": "DOC-CARD-264",
        "icd10": "N04.1",
        "condition": "Focal Segmental Glomerulosclerosis (FSGS)",
        "specialty": "Nephrology",
        "organ_system": "Renal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (DUET & DUPLEX Trials) & KDIGO",
        "citation": "Trachtman H et al. Efficacy and safety of sparsentan in patients with focal segmental glomerulosclerosis (DUET). Lancet. 2018;391(10129):1313-1324.",
        "doi_or_source": "10.1016/S0140-6736(18)30320-5",
        "clinical_evidence": "Focal Segmental Glomerulosclerosis (FSGS) is a clinicopathologic pattern of podocyte injury characterized by sclerosis in portions (segmental) of some (focal) glomeruli, categorized by the Columbia classification into collapsing, tip, cellular, perihilar, and not-otherwise-specified (NOS) variants. In the multicenter randomized double-blind Phase 2/3 DUET trial (n=109 patients with biopsy-proven primary FSGS), the first-in-class dual endothelin type A and angiotensin II receptor antagonist sparsentan produced a significantly greater reduction in proteinuria at 8 weeks compared with active irbesartan control (-45% vs -19%; p=0.006), with 28% achieving complete or partial remission (vs 9% irbesartan; p=0.02). Calcineurin inhibitors (cyclosporine/tacrolimus) achieve remission in 50-60% of steroid-resistant primary FSGS. Secondary/adaptive FSGS (driven by hyperfiltration from obesity, reduced nephron mass, or reflux) is non-immunologic and managed with maximal hemodynamic RAS/SGLT2 inhibition.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict dietary sodium restriction (<2,000 mg/day); dietary protein moderation (0.8 g/kg/day); weight normalization targeting BMI <25 kg/m2 in adaptive FSGS; blood pressure control to <120/80 mmHg.",
            "monitoring_cadence": "Urine protein-to-creatinine ratio (UPCR) and estimated GFR monthly during induction, then every 3 months; liver transaminases (ALT/AST) monthly on sparsentan.",
            "clinical_thresholds": "Primary FSGS with nephrotic proteinuria (>3.5 g/day) and hypoalbuminemia requires high-dose oral corticosteroids (prednisone 1 mg/kg/day for up to 16 weeks); failure to achieve >50% proteinuria drop defines steroid resistance."
        },
        "patient_plain_language": "Focal segmental glomerulosclerosis (FSGS) is a kidney disease that causes scarring in the microscopic filters of your kidneys. 'Focal' means only some of the filters are damaged, and 'segmental' means only a section of each filter is scarred. Because the filters are scarred and torn, protein leaks out into your urine, causing heavy swelling in your legs and belly, high cholesterol, and gradual decline in kidney function.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which Columbia histological subtype (e.g. tip lesion, collapsing variant) did my kidney biopsy show?",
            "safety_question": "Do I have primary autoimmune FSGS (which needs immunosuppressants) or secondary adaptive FSGS (which needs blood pressure and weight control)?",
            "action_threshold_question": "Has my genetic testing (for APOL1 high-risk genotypes or podocyte mutations) been completed?"
        },
        "red_flags": [
            "Rapid drop in urine output, swelling rapidly spreading into the abdomen and lungs, sudden shortness of breath, or blood pressure climbing over 170/100 mmHg"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Focal segmental glomerulosclerosis is a disease in which scar tissue develops on the parts of the kidneys that filter waste from the blood.",
                "plain_analogy": "Permanent scar patches forming on the kidney's filter screens, allowing protein to slip through into the urine.",
                "lifestyle_action": "Strictly limit salt intake. Maintain ideal body weight. Take kidney-protective blood pressure medications daily."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Sparsentan (Filspari)", "Prednisone", "Cyclosporine", "Tacrolimus", "Dapagliflozin"],
                "dosing_gdmt": "Sparsentan 200 mg PO daily for 14 days, then titrate to 400 mg daily. High-dose Prednisone 1 mg/kg daily for 12-16 weeks.",
                "black_box_warning": "Sparsentan: Embryo-fetal toxicity and risk of hepatotoxicity; monthly transaminases (ALT/AST) and pregnancy testing required.",
                "organ_clearance_cutoffs": "Monitor eGFR and potassium; SGLT2 inhibitors and ARBs provide additive antiproteinuric benefit."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DUET / DUPLEX",
                "pmid_or_doi": "10.1016/S0140-6736(18)30320-5",
                "cebm_level": 2,
                "sample_size": 109,
                "endpoints": "Proteinuria reduced by 45% with sparsentan vs 19% irbesartan (p=0.006); partial/complete remission achieved in 28% vs 9%."
            }
        }
    },
    {
        "id": "DOC-CARD-265",
        "icd10": "Q61.2",
        "condition": "Autosomal Dominant Polycystic Kidney Disease (ADPKD)",
        "specialty": "Nephrology",
        "organ_system": "Renal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (TEMPO 3:4 & REPRISE Trials) & KDIGO",
        "citation": "Torres VE et al. Tolvaptan in Patients with Autosomal Dominant Polycystic Kidney Disease (TEMPO 3:4). N Engl J Med. 2012;367(25):2407-2418.",
        "doi_or_source": "10.1056/NEJMoa1205511",
        "clinical_evidence": "Autosomal Dominant Polycystic Kidney Disease (ADPKD) is the most common monogenic kidney disorder, caused by mutations in PKD1 (chromosome 16, 78% of cases, more severe with median ESKD age 58) or PKD2 (chromosome 4, 15%, median ESKD age 79), leading to progressive cystogenesis that destroys renal parenchyma. In the landmark Phase 3 TEMPO 3:4 trial (n=1445 patients with total kidney volume [TKV] >=750 mL and CrCl >=60 mL/min), tolvaptan (a selective vasopressin V2-receptor antagonist, titrated to 45/15 to 90/30 mg daily) significantly slowed the annual rate of TKV growth over 3 years (2.8% per year vs 5.5% with placebo; p<0.001) and significantly reduced annual eGFR decline (-2.72 vs -3.70 mL/min/1.73m2; p<0.001). The REPRISE trial confirmed preserved eGFR benefit in later-stage disease (eGFR 25-65 mL/min/1.73m2). Baseline Mayo Classification (Classes 1A-1E based on height-adjusted TKV) reliably predicts rapid disease progression.",
        "solution_protocol": {
            "non_pharmacological_targets": "High water intake (>3-4 liters daily spread evenly through day and night to suppress endogenous vasopressin secretion); dietary sodium restriction (<2,000 mg/day); avoidance of caffeine (which increases intracellular cyclic AMP and cyst growth); strict blood pressure control (<120/80 mmHg).",
            "monitoring_cadence": "Serum ALT, AST, and total bilirubin monthly for the first 18 months of tolvaptan therapy, then every 3 months for life (REMS requirement); annual MRI measuring total kidney volume (TKV); estimated GFR quarterly.",
            "clinical_thresholds": "Rapidly progressive disease (Mayo Class 1C, 1D, or 1E; annual eGFR decline >=3.0 mL/min/1.73m2; or TKV >750 mL) in patients aged 18-55 with eGFR >25 mL/min qualifies for disease-modifying tolvaptan therapy."
        },
        "patient_plain_language": "Autosomal dominant polycystic kidney disease (ADPKD) is an inherited genetic condition that causes hundreds of fluid-filled cysts to grow and enlarge inside your kidneys over time. As the cysts multiply and expand, the kidneys can grow to the size of footballs, crowding out healthy kidney tissue and causing high blood pressure, flank pain, kidney stones, and gradual kidney failure. Each child of an affected parent has a 50% chance of inheriting the gene.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my height-adjusted Total Kidney Volume (TKV) on MRI and my Mayo risk classification (Class 1A through 1E)?",
            "safety_question": "What liver enzyme monitoring is required while taking tolvaptan (Jynarque) to protect my liver?",
            "action_threshold_question": "How many liters of water should I drink each day to naturally suppress vasopressin hormone and slow cyst growth?"
        },
        "red_flags": [
            "Severe sharp flank pain with high fever and shaking chills (infected kidney cyst), sudden frank red blood in urine, or severe sudden thunderclap headache (suspect Berry Aneurysm)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Polycystic kidney disease is an inherited disorder in which clusters of cysts develop primarily within your kidneys, causing them to enlarge and lose function.",
                "plain_analogy": "Fluid-filled water balloons growing and multiplying inside the kidney, slowly crowding out normal working kidney tissue.",
                "lifestyle_action": "Drink 3 to 4 liters of water daily. Strictly restrict salt to under 2,000 mg. Avoid excessive caffeine."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Tolvaptan (Jynarque)", "Lisinopril", "Telmisartan", "Amlodipine"],
                "dosing_gdmt": "Tolvaptan: Start 45 mg upon waking + 15 mg 8 hours later; titrate to 60/30 mg, then 90/30 mg daily based on tolerability.",
                "black_box_warning": "Tolvaptan: Potential for fatal acute liver failure; restricted distribution via the Jynarque REMS program requiring monthly LFTs.",
                "organ_clearance_cutoffs": "Contraindicated in patients with uncorrected hypovolemia, inability to sense thirst, or baseline severe hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TEMPO 3:4 / REPRISE",
                "pmid_or_doi": "10.1056/NEJMoa1205511",
                "cebm_level": 2,
                "sample_size": 1445,
                "endpoints": "Rate of total kidney volume expansion slowed by 50% (2.8% vs 5.5%/year; p<0.001); eGFR decline slowed by 1.0 mL/min/year."
            }
        }
    },
    {
        "id": "DOC-CARD-266",
        "icd10": "M32.14",
        "condition": "Lupus Nephritis",
        "specialty": "Nephrology",
        "organ_system": "Renal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (BLISS-LN Trial) & The Lancet (AURORA Trial)",
        "citation": "Furie R et al. Two-Year, Randomized, Controlled Trial of Belimumab in Lupus Nephritis (BLISS-LN). N Engl J Med. 2020;383(12):1117-1128.",
        "doi_or_source": "10.1056/NEJMoa2001180",
        "clinical_evidence": "Lupus nephritis (LN) is a major organ-threatening manifestation of Systemic Lupus Erythematosus (SLE), occurring in up to 50% of patients and classified by ISN/RPS into Classes I through VI (Class III focal and Class IV diffuse proliferative carrying the highest risk of progression to end-stage renal disease). In the landmark Phase 3 BLISS-LN trial (n=448 patients with active Class III, IV, or V LN receiving standard therapy with mycophenolate or cyclophosphamide), adding intravenous belimumab (a BLyS/BAFF inhibitor, 10 mg/kg) significantly increased Primary Efficacy Renal Response at 2 years compared with standard therapy alone (43% vs 32%; odds ratio 1.6; 95% CI 1.0-2.3; p=0.03) and halved the risk of a renal-related event or death (hazard ratio 0.51; p=0.001). The Phase 3 AURORA trial demonstrated that adding voclosporin (a novel calcineurin inhibitor) to mycophenolate doubled the complete renal response rate at 1 year (41% vs 23%; p<0.0001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Universal background therapy with hydroxychloroquine (targeting 5 mg/kg actual body weight/day; reduces renal flares and mortality); strict photoprotection (broad-spectrum SPF 50+ sunscreen); sodium restriction (<2,000 mg/day).",
            "monitoring_cadence": "Urine protein-to-creatinine ratio (UPCR), serum creatinine, anti-dsDNA antibody titers, and serum complement C3/C4 monthly for the first 6 months, then every 3 months; annual dilated ophthalmology slit-lamp exam.",
            "clinical_thresholds": "Proteinuria >0.5 g/day, cellular red blood cell casts, or unexplained rise in serum creatinine mandates diagnostic percutaneous renal biopsy to establish ISN/RPS class and activity/chronicity index."
        },
        "patient_plain_language": "Lupus nephritis is kidney inflammation caused by systemic lupus erythematosus (SLE), an autoimmune disease. In lupus, your immune system generates autoantibodies that mistakenly attack your own organs. When these antibody complexes lodge inside your kidney's filters, they cause swelling, inflammation, protein leakage, and high blood pressure. Left untreated, it can permanently scar the kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my kidney biopsy class (Class III, IV, or V) and what were the activity and chronicity scores?",
            "safety_question": "Am I on hydroxychloroquine as foundational protection, and should we add belimumab (Benlysta) or voclosporin to my mycophenolate?",
            "action_threshold_question": "What is our target reduction in urine protein at 6 and 12 months to confirm complete renal remission?"
        },
        "red_flags": [
            "Sudden severe swelling in face and legs, frothy bubbly urine, shortness of breath from fluid in lungs, or high spiking blood pressure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Lupus nephritis is an inflammation of the kidneys caused by systemic lupus erythematosus (SLE), an autoimmune disease.",
                "plain_analogy": "Autoimmune antibody clusters settling into kidney filters like sticky residue, causing the filters to leak protein and swell.",
                "lifestyle_action": "Take hydroxychloroquine daily. Wear sunblock every day (UV rays trigger flares). Restrict salt intake."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Belimumab (Benlysta)", "Voclosporin (Lupkynis)", "Mycophenolate Mofetil (CellCept)", "Hydroxychloroquine", "Cyclophosphamide"],
                "dosing_gdmt": "Standard: Mycophenolate 2-3 g/day + Hydroxychloroquine 200-400 mg/day. Add Belimumab 10 mg/kg IV or Voclosporin 23.7 mg PO BID.",
                "black_box_warning": "Mycophenolate: Embryo-fetal toxicity and spontaneous abortions. Voclosporin: Nephrotoxicity and serious infections.",
                "organ_clearance_cutoffs": "Monitor eGFR; adjust voclosporin dose if eGFR drops by >20% on consecutive measurements."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BLISS-LN / AURORA",
                "pmid_or_doi": "10.1056/NEJMoa2001180",
                "cebm_level": 2,
                "sample_size": 448,
                "endpoints": "Primary renal response increased by 49% with belimumab (43% vs 32%; p=0.03); risk of renal event or death halved (HR 0.51; p=0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-267",
        "icd10": "M31.30",
        "condition": "ANCA-Associated Vasculitis (Granulomatosis with Polyangiitis)",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (ADVOCATE Trial & RAVE Trial) & ACR Guidelines",
        "citation": "Jayne DRW et al. Avacopan for the Treatment of ANCA-Associated Vasculitis (ADVOCATE). N Engl J Med. 2021;384(7):599-609.",
        "doi_or_source": "10.1056/NEJMoa2023386",
        "clinical_evidence": "Granulomatosis with Polyangiitis (GPA, formerly Wegener's) and Microscopic Polyangiitis (MPA) are necrotizing small-vessel vasculitides associated with antineutrophil cytoplasmic antibodies (PR3-ANCA / c-ANCA in 85% of GPA; MPO-ANCA / p-ANCA in 70% of MPA). In the landmark Phase 3 ADVOCATE trial (n=330 patients with active ANCA vasculitis), the oral complement C5a receptor antagonist avacopan (30 mg BID) was noninferior to prednisone at week 26 and significantly superior to standard tapering prednisone in achieving sustained disease remission at 52 weeks (Birmingham Vasculitis Activity Score [BVAS] of 0 without relapse: 65.7% vs 54.9%; difference 12.5 percentage points; 95% CI 2.6-22.3; p=0.007 for superiority). Avacopan also significantly improved eGFR (+7.3 vs +4.1 mL/min/1.73m2; p=0.029) and eliminated glucocorticoid-related toxicity. In the RAVE trial, Rituximab (375 mg/m2 weekly for 4 doses) was proven noninferior to cyclophosphamide for induction and superior in relapsing disease (67% vs 42%; p=0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Pneumocystis jirovecii pneumonia (PJP) prophylaxis with trimethoprim-sulfamethoxazole (800/160 mg three times weekly) is mandatory during induction immunosuppression; ENT saline nasal rinses for crusting rhinitis; annual influenza and pneumococcal immunizations.",
            "monitoring_cadence": "Birmingham Vasculitis Activity Score (BVAS) at every visit; serial PR3/MPO-ANCA titers, ESR, CRP, urinalysis for microscopic hematuria/RBC casts, and serum creatinine every 2-4 weeks during induction, then every 3 months; serial chest CT.",
            "clinical_thresholds": "Rapidly progressive crescentic glomerulonephritis (doubling of serum creatinine) or diffuse alveolar hemorrhage (coughing blood with bilateral ground glass on chest CT) warrants pulse IV methylprednisolone (1 g daily for 3 days) and plasma exchange."
        },
        "patient_plain_language": "ANCA-associated vasculitis (such as Granulomatosis with Polyangiitis) is an autoimmune disorder where your immune system produces abnormal autoantibodies called ANCA that cause severe swelling and inflammation in your small blood vessels. The inflammation attacks blood vessels in your nose, sinuses, lungs, and kidneys. Symptoms often start like a severe sinus infection with bloody crusting, coughing up blood, and rapid kidney inflammation.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Birmingham Vasculitis Activity Score (BVAS) and my PR3 or MPO-ANCA antibody level?",
            "safety_question": "Am I on preventative antibiotics (Bactrim) to protect against Pneumocystis lung infections while my immune system is suppressed?",
            "action_threshold_question": "Can we use avacopan (Tavneos) to minimize or eliminate high-dose steroid medications and protect my kidneys?"
        },
        "red_flags": [
            "Coughing up frank red blood (alveolar hemorrhage), sudden severe shortness of breath, blood in the urine with rapidly climbing creatinine, or hearing loss"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Granulomatosis with polyangiitis is a rare disease that causes inflammation of the blood vessels, which restricts blood flow to various organs, most often the lungs and kidneys.",
                "plain_analogy": "Autoimmune fire burning inside the walls of small blood vessels in the sinuses, lungs, and kidneys.",
                "lifestyle_action": "Take daily preventative antibiotics (Bactrim) without fail. Use saline nasal washes for sinus crusts. Monitor urine."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Avacopan (Tavneos)", "Rituximab (Rituxan)", "Cyclophosphamide", "Prednisone", "Trimethoprim/Sulfamethoxazole"],
                "dosing_gdmt": "Avacopan 30 mg orally BID with food PLUS Rituximab 375 mg/m2 IV weekly for 4 weeks. PJP: Bactrim SS 1 tab daily.",
                "black_box_warning": "Avacopan: Hepatotoxicity; monitor liver transaminases (ALT/AST) and total bilirubin monthly for 6 months, then quarterly.",
                "organ_clearance_cutoffs": "Contraindicated in severe hepatic impairment (Child-Pugh C); monitor for neutropenia with rituximab."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ADVOCATE",
                "pmid_or_doi": "10.1056/NEJMoa2023386",
                "cebm_level": 2,
                "sample_size": 330,
                "endpoints": "Sustained disease remission at 52 weeks achieved in 65.7% with avacopan vs 54.9% with prednisone (p=0.007 for superiority); eGFR improved."
            }
        }
    },
    {
        "id": "DOC-CARD-268",
        "icd10": "M45.9",
        "condition": "Ankylosing Spondylitis (Axial Spondyloarthritis)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (MEASURE 1 & 2 Trials) & ACR/SAA Guidelines",
        "citation": "Baeten D et al. Secukinumab, an Interleukin-17A Inhibitor, in Ankylosing Spondylitis (MEASURE 1 & 2). N Engl J Med. 2015;373(26):2534-2548.",
        "doi_or_source": "10.1056/NEJMoa1505066",
        "clinical_evidence": "Ankylosing Spondylitis (AS / radiographic axial spondyloarthritis) is a chronic inflammatory arthritis predominantly affecting the axial skeleton and sacroiliac joints, strongly associated with HLA-B27 (>85-90%). Inflammatory back pain criteria (Calin/ASAS criteria: onset <45 years, insidious onset, improvement with exercise, no improvement with rest, pain at night) distinguish it from mechanical back pain. Pelvic radiography demonstrating bilateral Grade >=2 or unilateral Grade >=3 sacroiliitis (modified New York criteria) or active sacroiliac bone marrow edema on STIR MRI confirms the diagnosis. In the landmark Phase 3 MEASURE 1 and 2 trials (n=590 patients), secukinumab (an anti-IL-17A monoclonal antibody, 150 mg subcutaneous) significantly improved ASAS20 response rates at week 16 compared with placebo (61% vs 28%; p<0.001) and sustained clinical remission and spinal mobility out to 5 years. First-line therapy with continuous NSAIDs reduces radiographic spinal syndesmophyte progression.",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily specialized spine-extension physical therapy and swimming; structured posture training; sleep on a firm mattress with a thin neck pillow; absolute smoking cessation (smoking accelerates spinal fusion and syndesmophyte bridging).",
            "monitoring_cadence": "Bath Ankylosing Spondylitis Disease Activity Index (BASDAI) and Ankylosing Spondylitis Disease Activity Score (ASDAS-CRP) every 3-6 months; annual cervical and lumbar spine radiographs (mSASSS score) to track bony bridging; screening for acute anterior uveitis.",
            "clinical_thresholds": "High disease activity (ASDAS >=2.1 or BASDAI >=4.0) refractory to at least two different full-dose NSAIDs over 4-6 weeks indicates mandatory escalation to a biologic (TNF inhibitor or IL-17A inhibitor)."
        },
        "patient_plain_language": "Ankylosing spondylitis is an inflammatory arthritis that primarily attacks the joints of your spine and pelvis (sacroiliac joints). Unlike ordinary mechanical back pain that gets worse with exercise, ankylosing spondylitis causes deep lower back stiffness that feels worst when resting in bed and dramatically improves after you get up and move around. Over years, the chronic inflammation can cause the spinal vertebrae to fuse together into a stiff 'bamboo spine'.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Bath Ankylosing Spondylitis Disease Activity Index (BASDAI) and ASDAS-CRP score?",
            "safety_question": "Am I HLA-B27 positive, and does my pelvic MRI show active bone marrow inflammation in my sacroiliac joints?",
            "action_threshold_question": "Should I step up from daily anti-inflammatory pills to an IL-17 inhibitor (like secukinumab) or TNF blocker to prevent spinal fusion?"
        },
        "red_flags": [
            "Sudden severe red, painful, light-sensitive eye (acute anterior uveitis), sudden severe neck or back pain after a minor bump or fall (spinal fracture), or chest wall rigidity"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ankylosing spondylitis is an inflammatory disease that, over time, can cause some of the bones in the spine (vertebrae) to fuse.",
                "plain_analogy": "Chronic inflammation turning the flexible spinal joints into solid bone bridges, like melting wax fusing vertebrae together.",
                "lifestyle_action": "Exercise and stretch daily. Practice swimming. Sleep flat on your back without large pillows. Never smoke."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Secukinumab (Cosentyx)", "Adalimumab (Humira)", "Infliximab", "Upadacitinib (Rinvoq)", "Celecoxib"],
                "dosing_gdmt": "Secukinumab 150 mg subcutaneous injection at weeks 0, 1, 2, 3, 4, then every 4 weeks. Full-dose Celecoxib 200 mg BID.",
                "black_box_warning": "TNF & IL-17 Inhibitors: Increased risk of serious infections (tuberculosis, fungal); rule out latent TB prior to starting.",
                "organ_clearance_cutoffs": "Avoid IL-17 inhibitors (secukinumab, ixekizumab) in patients with active inflammatory bowel disease (Crohn's/colitis)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MEASURE 1 & 2",
                "pmid_or_doi": "10.1056/NEJMoa1505066",
                "cebm_level": 2,
                "sample_size": 590,
                "endpoints": "ASAS20 response achieved in 61% with secukinumab vs 28% placebo (p<0.001); spinal mobility preserved and radiographic progression halted."
            }
        }
    },
    {
        "id": "DOC-CARD-269",
        "icd10": "L40.50",
        "condition": "Psoriatic Arthritis",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (DISCOVER-1 & 2 Trials) & ACR/NPF Guidelines",
        "citation": "Mease PJ et al. Guselkumab in patients with active psoriatic arthritis (DISCOVER-2). Lancet. 2020;395(10230):1126-1140.",
        "doi_or_source": "10.1016/S0140-6736(20)30263-4",
        "clinical_evidence": "Psoriatic Arthritis (PsA) is a multifaceted inflammatory musculoskeletal disease occurring in up to 30% of patients with plaque psoriasis, involving six clinical domains: peripheral arthritis (often asymmetric, involving distal interphalangeal [DIP] joints), axial disease, enthesitis (inflammation at tendon insertion sites, e.g. Achilles tendonitis), dactylitis ('sausage digits'), skin psoriasis, and nail dystrophy (nail pitting and onycholysis in >80%). Classification Criteria for Psoriatic Arthritis (CASPAR score >=3) provides 91% sensitivity and 99% specificity. In the landmark Phase 3 DISCOVER-2 trial (n=739 biologic-naive patients with active PsA), the IL-23 p19-subunit inhibitor guselkumab (100 mg SC every 4 or 8 weeks) significantly improved ACR20 response rates at week 24 compared with placebo (64% vs 33%; p<0.0001) with marked complete clearance of skin psoriasis (PASI 90 in 70%), resolution of dactylitis/enthesitis, and significant inhibition of radiographic joint destruction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Low-impact aerobic conditioning and resistance training; occupational therapy for hand splinting; weight reduction (obesity impairs biologic response rates by 50%); Mediterranean anti-inflammatory diet.",
            "monitoring_cadence": "Psoriatic Arthritis Disease Activity Score (PASDAS) or Clinical Disease Activity Index for Psoriatic Arthritis (cDaPSA) every 3 months; annual plain radiographs of hands and feet (assessing erosions, joint space narrowing, and 'pencil-in-cup' deformities).",
            "clinical_thresholds": "Active disease refractory to oral disease-modifying antirheumatic drugs (Methotrexate 15-25 mg/week) or severe axial/enthesitis disease warrants immediate biologic initiation (IL-23, IL-17, or TNF inhibitor)."
        },
        "patient_plain_language": "Psoriatic arthritis is an autoimmune condition that causes joint pain, swelling, and stiffness in people who have the skin condition psoriasis. It causes painful inflammation in your finger and toe joints, swollen 'sausage-like' fingers and toes (dactylitis), tender heels where the Achilles tendon attaches, and pitted, crumbly fingernails. Early treatment prevents permanent joint damage.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current swollen and tender joint count, and does my CASPAR score confirm psoriatic arthritis?",
            "safety_question": "Does my joint disease also involve my spine (axial disease), and which biologic will treat both my skin and joints best?",
            "action_threshold_question": "Do my hand and foot X-rays show any permanent bone erosions or joint narrowing?"
        },
        "red_flags": [
            "Severe swelling and pain in an entire finger or toe making it look like a sausage (dactylitis), severe morning stiffness lasting >2 hours, or sudden red painful eye"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Psoriatic arthritis is a form of arthritis that affects some people who have psoriasis — a condition that features red patches of skin topped with silvery scales.",
                "plain_analogy": "Skin psoriasis inflammation driving deeper into the body, inflaming the tendon attachments and finger joints.",
                "lifestyle_action": "Engage in low-impact swimming and walking. Protect hands with supportive grips. Keep body weight within healthy range."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Guselkumab (Tremfya)", "Risankizumab (Skyrizi)", "Ixekizumab (Taltz)", "Adalimumab", "Methotrexate"],
                "dosing_gdmt": "Guselkumab 100 mg subcutaneous injection at week 0, week 4, then every 8 weeks. Methotrexate 15-25 mg weekly + Folic acid 1 mg daily.",
                "black_box_warning": "Biologics: Increased risk of serious bacterial, mycobacterial (TB), and fungal infections; screen for latent TB.",
                "organ_clearance_cutoffs": "Monitor CBC and liver transaminases quarterly on methotrexate; avoid methotrexate in liver disease or pregnancy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DISCOVER-2",
                "pmid_or_doi": "10.1016/S0140-6736(20)30263-4",
                "cebm_level": 2,
                "sample_size": 739,
                "endpoints": "ACR20 response achieved in 64% with guselkumab vs 33% placebo (p<0.0001); radiographic structural joint damage significantly inhibited."
            }
        }
    },
    {
        "id": "DOC-CARD-270",
        "icd10": "M34.0",
        "condition": "Systemic Sclerosis (Scleroderma)",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (SENSCIS Trial) & ACR/EULAR Recommendations",
        "citation": "Distler O et al. Nintedanib for Systemic Sclerosis-Associated Interstitial Lung Disease (SENSCIS). N Engl J Med. 2019;380(26):2518-2528.",
        "doi_or_source": "10.1056/NEJMoa1903076",
        "clinical_evidence": "Systemic Sclerosis (SSc / Scleroderma) is a systemic autoimmune disease characterized by microvascular obliteration, immune activation, and widespread progressive tissue fibrosis of the skin and internal organs. Subdivided into Limited Cutaneous SSc (lcSSc: CREST syndrome; anti-centromere antibodies [ACA] in 60-80%; high risk of pulmonary arterial hypertension) and Diffuse Cutaneous SSc (dcSSc: skin thickening proximal to elbows/knees; anti-Scl-70/topoisomerase I or anti-RNA polymerase III; high risk of interstitial lung disease and scleroderma renal crisis). In the landmark Phase 3 SENSCIS trial (n=576 patients with SSc-ILD), the intracellular tyrosine kinase inhibitor nintedanib (150 mg BID) significantly reduced the annual rate of decline in Forced Vital Capacity (FVC) by 44% compared with placebo (-52.4 mL/year vs -93.3 mL/year; difference 41.0 mL/year; 95% CI 2.9-79.0; p=0.04). In early progressive dcSSc, tocilizumab (anti-IL-6 receptor) preserves lung function.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of cold exposure and thermal layered mittens for Raynaud's; elevation of head of bed and small frequent meals for severe esophageal dysmotility; skin moisturization; pulmonary rehabilitation.",
            "monitoring_cadence": "Quarterly pulmonary function testing (FVC and DLCO); annual screening transthoracic echocardiogram assessing tricuspid regurgitant velocity for pulmonary hypertension; daily home blood pressure monitoring (to catch Scleroderma Renal Crisis immediately); modified Rodnan skin score (mRSS).",
            "clinical_thresholds": "New-onset hypertension (BP >140/90) or unexplained rise in serum creatinine in dcSSc indicates impending Scleroderma Renal Crisis, mandating immediate emergency ACE inhibitor therapy (captopril); high-dose corticosteroids (>15 mg/day) are strictly contraindicated as they precipitate renal crisis."
        },
        "patient_plain_language": "Systemic sclerosis (scleroderma) is an autoimmune disorder that causes your body to produce far too much collagen, a tough scar-like protein. Extra collagen builds up in your skin, blood vessels, and internal organs. It causes the skin on your fingers, hands, and face to become tight, hard, and shiny, makes fingers turn white in the cold (Raynaud's), causes chronic acid reflux, and can cause stiff scarring in your lungs.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my modified Rodnan skin score, and did my lung function test (FVC and DLCO) show any signs of lung scarring (pulmonary fibrosis)?",
            "safety_question": "Do I have anti-RNA polymerase III antibodies, and am I monitoring my blood pressure every single day at home to catch a renal crisis early?",
            "action_threshold_question": "Why should I strictly avoid taking high-dose prednisone steroid pills with my type of scleroderma?"
        },
        "red_flags": [
            "Sudden severe blood pressure spike (>160/100 mmHg) with headache or blurry vision (Scleroderma Renal Crisis emergency), sudden breathlessness, or black painful sores on fingertips"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Scleroderma is a group of rare diseases that involve the hardening and tightening of the skin and connective tissues.",
                "plain_analogy": "An overproduction of tough scar protein that shrink-wraps the skin, blood vessels, and internal lungs like stiff leather.",
                "lifestyle_action": "Check blood pressure daily at home. Keep hands and feet warm with thermal gloves. Eat upright and stay sitting up after meals."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Nintedanib (Ofev)", "Tocilizumab (Actemra)", "Mycophenolate Mofetil", "Captopril (Emergency Renal Crisis)", "Nifedipine ER"],
                "dosing_gdmt": "Nintedanib 150 mg orally BID with food. For Scleroderma Renal Crisis: Captopril 12.5-25 mg PO q8h titrated rapidly to lower SBP.",
                "black_box_warning": "Systemic Corticosteroids: High doses (>15 mg daily) trigger life-threatening Scleroderma Renal Crisis; strictly avoid.",
                "organ_clearance_cutoffs": "Monitor liver function tests baseline and monthly for 3 months with nintedanib; manage diarrhea with loperamide."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SENSCIS Trial",
                "pmid_or_doi": "10.1056/NEJMoa1903076",
                "cebm_level": 2,
                "sample_size": 576,
                "endpoints": "Annual rate of FVC decline slowed by 44% with nintedanib (-52.4 vs -93.3 mL/year; p=0.04); effect consistent across subgroups."
            }
        }
    },
    {
        "id": "DOC-CARD-271",
        "icd10": "M35.00",
        "condition": "Sjögren's Syndrome",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACR/EULAR Classification Criteria & Guidelines",
        "source_body": "Annals of the Rheumatic Diseases & Arthritis & Rheumatology",
        "citation": "Shiboski CH et al. 2016 American College of Rheumatology/European League Against Rheumatism classification criteria for primary Sjögren's syndrome. Ann Rheum Dis. 2017;76(1):9-16.",
        "doi_or_source": "10.1136/annrheumdis-2016-210571",
        "clinical_evidence": "Primary Sjögren's Syndrome is a systemic autoimmune exocrinopathy characterized by lymphocytic infiltration of salivary and lacrimal glands, resulting in classic sicca syndrome (xerophthalmia [dry eyes] and xerostomia [dry mouth]). Diagnostic classification requires a weighted score >=4 based on: positive anti-SSA/Ro antibodies (weight 3); labial salivary gland biopsy showing focal lymphocytic sialadenitis with focus score >=1 focus per 4 mm2 (weight 3); ocular staining score >=5 or van Bijsterveld score >=4 (weight 1); Schirmer's test <=5 mm in 5 minutes (weight 1); and unstimulated whole saliva flow rate <=0.1 mL/min (weight 1). Patients face a 15- to 20-fold increased lifetime risk of B-cell non-Hodgkin lymphoma (predominantly MALT lymphoma in parotid glands), heralded by persistent parotid swelling, purpura, monoclonal gammopathy, and low complement C4.",
        "solution_protocol": {
            "non_pharmacological_targets": "Frequent preservative-free artificial tears and nocturnal ocular lubricating ointments; silicone punctal plugs; sugar-free chewing gum or xylitol lozenges; meticulous dental hygiene and fluoride varnish applications every 3-6 months; home ultrasonic room humidifiers.",
            "monitoring_cadence": "Oral dental examination every 3-4 months; biannual rheumatologic review with serum protein electrophoresis (SPEP), quantitative immunoglobulins, and complement C3/C4 (screening for cryoglobulinemia and lymphoma); annual chest radiography.",
            "clinical_thresholds": "Extraglandular systemic manifestations (inflammatory polyarthritis, cutaneous vasculitis, interstitial lung disease, or renal tubular acidosis) warrant systemic disease-modifying therapy with Hydroxychloroquine, Azathioprine, or Rituximab."
        },
        "patient_plain_language": "Sjögren's syndrome is an autoimmune disease where your body's immune system attacks its own moisture-producing glands, primarily the tear glands in your eyes and the saliva glands in your mouth. This leads to chronic, severe dry eyes (feeling like grit or sand is trapped under your eyelids), dry mouth (difficulty swallowing dry crackers or speaking without sipping water), rampant tooth decay, and joint stiffness.",
        "doctor_consultation_checklist": {
            "parameter_question": "Were my anti-SSA (Ro) antibody and anti-SSB (La) antibody blood tests positive?",
            "safety_question": "What fluoride treatments and saliva stimulants (such as pilocarpine or cevimeline) should I use to protect my teeth from rapid decay?",
            "action_threshold_question": "How often should my salivary glands and lymph nodes be examined to screen for lymphoma?"
        },
        "red_flags": [
            "Persistent, painless, firm enlargement of a parotid saliva gland under the ear, purple spots on lower legs (palpable purpura), or night sweats"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sjögren syndrome is an autoimmune disorder in which immune cells attack and destroy the glands that produce tears and saliva.",
                "plain_analogy": "The immune system turning off the body's moisture faucets, leaving the eyes, mouth, and joints dry like a desert.",
                "lifestyle_action": "Use preservative-free eye drops hourly. Drink water constantly. Brush teeth after every meal and apply prescription fluoride gel."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Pilocarpine (Salagen)", "Cevimeline (Evoxac)", "Cyclosporine Ophthalmic (Restasis)", "Lifitegrast (Xiidra)", "Hydroxychloroquine"],
                "dosing_gdmt": "Pilocarpine 5 mg orally 3-4 times daily with meals. Restasis 0.05% 1 drop in both eyes BID. Hydroxychloroquine 200-400 mg daily for joint pains.",
                "black_box_warning": "Pilocarpine: Sweating, flushing, urinary urgency, and bronchospasm; contraindicated in uncontrolled asthma or acute angle-closure glaucoma.",
                "organ_clearance_cutoffs": "Monitor for cholinergic adverse effects; schedule regular eye exams on hydroxychloroquine to prevent retinal toxicity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACR/EULAR Sjögren Criteria",
                "pmid_or_doi": "10.1136/annrheumdis-2016-210571",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "Classification criteria achieve 96% sensitivity and 95% specificity; early punctal occlusion and muscarinic agonists improve quality of life scores."
            }
        }
    },
    {
        "id": "DOC-CARD-272",
        "icd10": "M33.90",
        "condition": "Dermatomyositis & Polymyositis",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (ProDERM Trial) & EULAR/ACR Guidelines",
        "citation": "Aggarwal R et al. Intravenous Immunoglobulin in Dermatomyositis: The ProDERM Randomized, Double-Blind Phase 3 Trial. N Engl J Med. 2022;387(14):1264-1274.",
        "doi_or_source": "10.1056/NEJMoa2117912",
        "clinical_evidence": "Dermatomyositis (DM) and Polymyositis (PM) are idiopathic inflammatory myopathies characterized by symmetric, progressive, proximal muscle weakness (neck flexors, deltoids, hip flexors) and elevated skeletal muscle enzymes (creatine kinase [CK] typically 10-50x ULN, aldolase, LDH). Dermatomyositis features pathognomonic cutaneous signs: heliotrope rash (violaceous erythema with periorbital edema), Gottron's papules (violaceous scaly papules over MCP and PIP joints), and shawl/V-sign rashes. In the landmark international Phase 3 ProDERM trial (n=95 patients with active dermatomyositis), high-dose intravenous immunoglobulin (IVIG 2.0 g/kg every 4 weeks for 16 weeks) achieved a Total Improvement Score (TIS) >=20 in 78.7% of patients compared with 43.8% on placebo (difference 34.9 percentage points; 95% CI 16.7-52.8; p=0.001) with marked recovery in muscle strength (MMT-8) and skin disease (CDASI). Extensive age-appropriate cancer screening (CT chest/abdomen/pelvis, mammography, colonoscopy) is mandatory, as DM carries a 5- to 6-fold increased risk of paraneoplastic malignancy (particularly with anti-TIF1-gamma or anti-NXP2 autoantibodies).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict photoprotection with broad-spectrum SPF 50+ sunscreen (ultraviolet light directly flares cutaneous and muscle disease); speech-language pathology swallowing evaluation for pharyngeal weakness; physical therapy for range of motion.",
            "monitoring_cadence": "Manual Muscle Testing (MMT-8), serum creatine kinase (CK), and aldolase every 4 weeks during induction, then every 3 months; comprehensive paraneoplastic malignancy screening at diagnosis and annually for 3 years; baseline high-resolution chest CT (screening for rapidly progressive interstitial lung disease with anti-MDA5).",
            "clinical_thresholds": "Rapidly progressive dysphagia (aspiration risk) or rapidly declining FVC on pulmonary function tests warrants pulse IV methylprednisolone (1 g daily for 3 days) combined with IVIG."
        },
        "patient_plain_language": "Dermatomyositis is a rare inflammatory disease marked by muscle weakness and distinctive skin rashes. Your immune system attacks blood vessels and muscle fibers, causing weakness in the muscles closest to the center of your body—making it hard to lift your arms to wash your hair, climb stairs, or stand up from a deep chair. In dermatomyositis, it also causes a reddish-purple rash around the eyelids (heliotrope rash) and purple bumps across the knuckles (Gottron's papules).",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current serum creatine kinase (CK) blood level and what did my myositis-specific antibody panel show?",
            "safety_question": "Have I had a full cancer screening evaluation (CT scans and cancer checks) to rule out an underlying tumor triggering this immune reaction?",
            "action_threshold_question": "Would I benefit from monthly IVIG infusions (Octagam) alongside my steroids to help rebuild my muscle strength faster?"
        },
        "red_flags": [
            "Choking when swallowing food or liquids, inability to lift your head off the pillow, sudden rapid breathlessness, or painful ulcers on fingertips (anti-MDA5 myositis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dermatomyositis is an inflammatory muscle disease that causes muscle weakness and distinctive skin rashes.",
                "plain_analogy": "Autoimmune inflammation attacking the electrical and fuel cables of the upper arm and leg muscles, leaving them weak and tired.",
                "lifestyle_action": "Wear sunblock every day without fail. Do gentle muscle stretches. Avoid falls by using handrails on stairs."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Intravenous Immune Globulin (Octagam 10%)", "Prednisone Oral", "Methotrexate", "Azathioprine", "Rituximab"],
                "dosing_gdmt": "IVIG 2 g/kg total dose divided over 2 consecutive days every 4 weeks. High-dose Prednisone 1 mg/kg daily tapered over 6-12 months.",
                "black_box_warning": "IVIG: Thrombosis, acute renal failure, and aseptic meningitis; ensure adequate pre-hydration and monitor renal function.",
                "organ_clearance_cutoffs": "Screen for latent infections prior to initiating immunosuppression; monitor liver enzymes and blood counts monthly."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ProDERM Trial",
                "pmid_or_doi": "10.1056/NEJMoa2117912",
                "cebm_level": 2,
                "sample_size": 95,
                "endpoints": "Total Improvement Score >=20 achieved in 78.7% with IVIG vs 43.8% placebo (p=0.001); manual muscle testing score and cutaneous scores improved."
            }
        }
    },
    {
        "id": "DOC-CARD-273",
        "icd10": "M35.2",
        "condition": "Behçet's Disease",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (RELIEF Trial) & EULAR Recommendations",
        "citation": "Hatemi G et al. Trial of Apremilast for Oral Ulcers in Behçet's Syndrome (RELIEF). N Engl J Med. 2019;381(20):1918-1928.",
        "doi_or_source": "10.1056/NEJMoa1816594",
        "clinical_evidence": "Behçet's disease is a variable-vessel systemic vasculitis characterized by recurrent, painful aphthous oral ulcers (present in >98%), recurrent genital ulcers, cutaneous lesions (erythema nodosum, pseudofolliculitis), and sight-threatening posterior uveitis / retinal vasculitis. International Criteria for Behçet's Disease (ICBD score >=4) provides 94% sensitivity and 96% specificity; strong genetic association with HLA-B*51. Pathergy testing (sterile pustule developing 24-48h after skin needle prick) is highly specific. In the multicenter double-blind Phase 3 RELIEF trial (n=207 patients with active oral ulcers), the oral phosphodiesterase-4 (PDE4) inhibitor apremilast (30 mg BID) significantly reduced the daily area under the curve for number of oral ulcers over 12 weeks compared with placebo (129.5 vs 222.1; p<0.001) and cleared oral ulcers in 52.9% vs 22.3% (p<0.001) with marked pain relief. In sight-threatening uveitis, TNF-alpha inhibitors (infliximab/adalimumab) achieve remission in >85%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Topical corticosteroid pastes (triamcinolone in Orabase) applied to oral ulcers; antimicrobial mouthwashes (chlorhexidine); avoidance of spicy, acidic, or abrasive foods during active oral flares; sunglasses for ocular photophobia.",
            "monitoring_cadence": "Behçet's Disease Current Activity Form (BDCAF) at every visit; regular slit-lamp dilated ophthalmology examination (screening for silent retinal vasculitis and hypopyon uveitis); vascular Doppler ultrasound or CT angiography for vascular aneurysms/thrombosis.",
            "clinical_thresholds": "Posterior uveitis, retinal vasculitis, pulmonary artery aneurysms, or central nervous system involvement (Neuro-Behçet) mandates emergency high-dose IV methylprednisolone and biologic TNF inhibitor therapy (Infliximab)."
        },
        "patient_plain_language": "Behçet's disease is a rare autoimmune disorder that causes inflammation in blood vessels throughout your body. The most common hallmark is having recurrent, painful canker sores in your mouth that look like normal ulcers but occur frequently and take longer to heal. It also causes painful ulcers in the genital area, acne-like skin bumps, swollen joints, and inflammation inside the eye that can threaten vision if not treated promptly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are my oral and genital ulcers responding to treatment, and was my HLA-B51 genetic marker checked?",
            "safety_question": "Has my eye doctor examined the back of my retina with a dilated slit-lamp exam to ensure there is no hidden retinal vasculitis?",
            "action_threshold_question": "Would oral apremilast (Otezla) or colchicine help stop my recurrent mouth sores from coming back?"
        },
        "red_flags": [
            "Sudden floaters, blurry vision, or painful red eye (acute uveitis), sudden coughing up blood (pulmonary artery aneurysm), or severe headache with fever"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Behçet disease is a rare disorder that causes blood vessel inflammation throughout your body, leading to mouth sores, eye inflammation, and skin lesions.",
                "plain_analogy": "An autoimmune reaction causing painful blisters and inflammation in mucous membranes and blood vessel linings.",
                "lifestyle_action": "Avoid citrus and hot spicy foods during mouth ulcer flares. Use soft toothbrushes. See an eye specialist promptly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Apremilast (Otezla)", "Colchicine", "Infliximab", "Adalimumab", "Azathioprine"],
                "dosing_gdmt": "Oral ulcers: Apremilast 30 mg orally BID (titrated over 5 days). Prevention: Colchicine 0.5-1.5 mg daily. Severe uveitis: Infliximab 5 mg/kg IV.",
                "black_box_warning": "Infliximab: Increased risk of serious fungal, bacterial, and opportunistic infections; screen for latent TB and hepatitis B.",
                "organ_clearance_cutoffs": "Reduce apremilast to 30 mg once daily if eGFR <30 mL/min; monitor for gastrointestinal side effects (nausea/diarrhea)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "RELIEF Trial",
                "pmid_or_doi": "10.1056/NEJMoa1816594",
                "cebm_level": 2,
                "sample_size": 207,
                "endpoints": "Area under curve for oral ulcers reduced by 42% with apremilast vs placebo (p<0.001); complete clearance in 53% vs 22%; oral ulcer pain significantly reduced."
            }
        }
    },
    {
        "id": "DOC-CARD-274",
        "icd10": "M30.0",
        "condition": "Polyarteritis Nodosa (PAN)",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACR/EULAR Clinical Practice Guideline & French Vasculitis Study",
        "source_body": "Arthritis & Rheumatology (ACR Guideline) & Medicine",
        "citation": "Chung SA et al. 2021 American College of Rheumatology/Vasculitis Foundation Guideline for the Management of Polyarteritis Nodosa. Arthritis Rheumatol. 2021;73(8):1384-1393.",
        "doi_or_source": "10.1002/art.41743",
        "clinical_evidence": "Polyarteritis Nodosa (PAN) is a systemic necrotizing vasculitis of medium-sized and small muscular arteries, classically sparing the venous system, pulmonary arteries, and glomeruli (not ANCA-associated). A significant subset is secondary to chronic Hepatitis B virus (HBV) infection. Pathology shows transmural fibrinoid necrosis and segmental aneurysmal dilatations with thrombosis. Catheter-directed visceral angiography or CT angiography characteristically demonstrates multiple microaneurysms and arterial occlusions ('string-of-beads' appearance) in mesenteric, renal, and hepatic vasculatures. Clinical hallmarks include mononeuritis multiplex (asymmetric foot/wrist drop in >60%), livedo reticularis, testicular pain, and renovascular hypertension. Prognosis is stratified using the Five-Factor Score (FFS: proteinuria >1g/day, renal insufficiency, cardiomyopathy, severe GI involvement, CNS involvement). Remission is achieved in >80% with combined high-dose corticosteroids and cyclophosphamide.",
        "solution_protocol": {
            "non_pharmacological_targets": "Physical and occupational therapy with ankle-foot orthoses (AFO splints) for peroneal nerve foot drop; screening for Hepatitis B and Hepatitis C virus; blood pressure control with calcium channel blockers.",
            "monitoring_cadence": "Birmingham Vasculitis Activity Score (BVAS) and neurological examination every 4 weeks; serum creatinine, BUN, liver enzymes, and urinalysis; repeat visceral angiography if mesenteric ischemia suspected.",
            "clinical_thresholds": "Severe organ-threatening disease (Five-Factor Score >=1, e.g., acute abdomen, gastrointestinal perforation, cardiomyopathy, or acute renal failure) warrants pulse IV methylprednisolone (1 g daily for 3 days) plus IV cyclophosphamide (0.5-0.75 g/m2 monthly)."
        },
        "patient_plain_language": "Polyarteritis nodosa (PAN) is a serious autoimmune condition where your immune system attacks and inflames medium-sized blood vessels in your body, particularly in your nerves, kidneys, skin, and bowels. As the inflamed artery walls weaken, tiny balloon-like pouches (aneurysms) form along the blood vessels like beads on a string, cutting off blood flow. Common signs include severe nerve pain and sudden weakness (like being unable to lift your foot, called foot drop), deep muscle aches, and purplish lace-like skin discoloration.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Five-Factor Score (FFS) and did my mesenteric or renal angiogram show microaneurysms?",
            "safety_question": "Have I been tested for hepatitis B virus, which requires antiviral therapy (entecavir) rather than immunosuppression?",
            "action_threshold_question": "Do I need an ankle-foot orthosis (foot brace) to help me walk safely while my damaged leg nerve heals?"
        },
        "red_flags": [
            "Sudden severe abdominal pain with rigid abdomen (mesenteric bowel perforation), sudden wrist or foot drop, testicular pain, or blood pressure spiking dangerously"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Polyarteritis nodosa is a rare disease that results from blood vessel inflammation causing injury to organ systems, most commonly nerves, kidneys, and skin.",
                "plain_analogy": "Inflammatory weak spots forming in medium-sized blood pipes, causing them to bulge out like tiny balloons and choke off blood flow to nerves and organs.",
                "lifestyle_action": "Wear supportive ankle braces to prevent tripping. Check blood pressure regularly. Complete the full course of immune medications."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone Oral", "Methylprednisolone IV", "Cyclophosphamide (Cytoxan)", "Entecavir (for HBV-PAN)", "Azathioprine"],
                "dosing_gdmt": "Severe PAN: Methylprednisolone 1,000 mg IV daily for 3 days, then Prednisone 1 mg/kg daily PLUS Cyclophosphamide 0.5-0.75 g/m2 IV monthly for 6 months.",
                "black_box_warning": "Cyclophosphamide: Hemorrhagic cystitis, myelosuppression, and secondary malignancies (bladder cancer); hydrate aggressively.",
                "organ_clearance_cutoffs": "Monitor CBC and urinalysis weekly on cyclophosphamide; give Mesna with high doses to prevent bladder injury."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "French Vasculitis Study Group PAN",
                "pmid_or_doi": "10.1002/art.41743",
                "cebm_level": 1,
                "sample_size": 1500,
                "endpoints": "Combined cyclophosphamide and steroid therapy achieves complete remission in >80% of severe PAN; 5-year survival exceeds 80%."
            }
        }
    },
    {
        "id": "DOC-CARD-275",
        "icd10": "D69.0",
        "condition": "Henoch-Schönlein Purpura (IgA Vasculitis)",
        "specialty": "Rheumatology",
        "organ_system": "Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR/PRINTO/PRES Classification Criteria & Guideline",
        "source_body": "Annals of the Rheumatic Diseases & Cochrane Review",
        "citation": "Ozen S et al. EULAR/PRINTO/PRES criteria for Henoch-Schönlein purpura (IgA vasculitis). Ann Rheum Dis. 2010;69(5):798-806.",
        "doi_or_source": "10.1136/ard.2009.116657",
        "clinical_evidence": "Henoch-Schönlein Purpura (HSP, now classified as IgA Vasculitis [IgAV]) is the most common systemic vasculitis of childhood (over 90% of cases in children <10 years), characterized by immune complex deposition of galactose-deficient IgA1 in small vessels (capillaries, venules, arterioles). The validated EULAR/PRINTO/PRES criteria mandate palpable purpura (non-thrombocytopenic petechiae and raised purpura distributed predominantly on dependent lower extremities and buttocks) plus at least one of four features: (1) acute diffuse colicky abdominal pain; (2) any biopsy showing predominant IgA deposition; (3) acute arthritis or arthralgia; and (4) renal involvement (hematuria >5 RBCs/HPF, red blood cell casts, or proteinuria >0.3 g/24h). The disease is self-limiting in >85% of cases within 4 to 8 weeks. Long-term morbidity is entirely determined by the severity of nephritis (HSP nephritis), which develops in 30-50% and requires longitudinal urinalysis surveillance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bed rest and leg elevation during acute lower extremity purpuric flares; adequate oral hydration; avoidance of unnecessary NSAIDs during active nephritis (use acetaminophen for joint arthralgia).",
            "monitoring_cadence": "Serial urinalysis (screening for microscopic hematuria and proteinuria) and blood pressure at diagnosis, weekly for 1 month, every 2 weeks for month 2, and monthly through month 6; serum creatinine if proteinuria develops.",
            "clinical_thresholds": "Nephrotic-range proteinuria (UPCR >2.0 mg/mg), macroscopic hematuria with hypertension, or declining eGFR warrants diagnostic kidney biopsy and high-dose corticosteroid/ACE inhibitor therapy."
        },
        "patient_plain_language": "Henoch-Schönlein purpura (IgA vasculitis) is an illness that causes tiny blood vessels in the skin, joints, intestines, and kidneys to become swollen and leaky. It often strikes children and young adults a couple of weeks after a simple cold or respiratory virus. The classic sign is a raised, bumpy, reddish-purple spotted rash (palpable purpura) on the legs and buttocks, accompanied by aching knees and ankles and crampy belly pain.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my child's urine show any protein or red blood cells on the dipstick test?",
            "safety_question": "How often should we check blood pressure and urine samples over the next 6 months to ensure the kidneys remain completely healthy?",
            "action_threshold_question": "Are oral steroids needed to ease severe abdominal cramping and joint swelling?"
        },
        "red_flags": [
            "Severe colicky abdominal pain with bloody bowel movements (suspect bowel intussusception emergency), vomiting, swollen scrotum in boys, or dark cola-colored urine"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Henoch-Schönlein purpura is a disorder that causes small blood vessels in the skin, joints, intestines, and kidneys to become inflamed and bleed.",
                "plain_analogy": "A temporary immune overreaction following a cold that makes small blood vessels in the legs and intestines leak tiny spots of blood.",
                "lifestyle_action": "Rest and elevate legs. Avoid aspirin and ibuprofen if kidneys are involved. Check urine tests regularly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Acetaminophen", "Prednisone Oral (Short course)", "Lisinopril", "Azathioprine"],
                "dosing_gdmt": "For severe abdominal pain or joint swelling: Prednisone 1-2 mg/kg/day orally for 1-2 weeks, followed by a taper. For persistent proteinuria: ACEi.",
                "black_box_warning": "Corticosteroids: Relieve gastrointestinal pain and arthralgia but do not prevent the long-term development of nephritis.",
                "organ_clearance_cutoffs": "Monitor for intussusception (telescoping bowel) via abdominal ultrasound if severe abdominal colic occurs."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EULAR/PRINTO HSP Criteria",
                "pmid_or_doi": "10.1136/ard.2009.116657",
                "cebm_level": 1,
                "sample_size": 2400,
                "endpoints": "Criteria achieve 100% sensitivity and 87% specificity; spontaneous complete recovery occurs in >85%; <2% progress to chronic renal failure."
            }
        }
    },
    {
        "id": "DOC-CARD-276",
        "icd10": "Q79.60",
        "condition": "Ehlers-Danlos Syndrome (Hypermobile & Vascular)",
        "specialty": "Genetics & Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial & Guidelines",
        "source_body": "The Lancet (BBEST Trial) & International EDS Consortium",
        "citation": "Ong KT et al. Effect of celiprolol on prevention of cardiovascular events in vascular Ehlers-Danlos syndrome: a prospective randomised, open, blinded-endpoints trial (BBEST). Lancet. 2010;376(9751):1476-1484.",
        "doi_or_source": "10.1016/S0140-6736(10)60960-9",
        "clinical_evidence": "Ehlers-Danlos Syndromes (EDS) are a clinically and genetically heterogeneous group of hereditary connective tissue disorders characterized by joint hypermobility, skin hyperextensibility, and generalized tissue fragility. Hypermobile EDS (hEDS) is the most prevalent, diagnosed clinically using the 2017 International Consortium criteria (Beighton generalized hypermobility score >=5 in adults, soft/velvety hyperextensible skin, piezogenic papules, recurrent joint subluxations, and chronic musculoskeletal pain). Vascular EDS (vEDS) is the severe life-threatening subtype caused by autosomal dominant mutations in the COL3A1 gene (type III procollagen), characterized by translucent thin skin, easy bruising, and spontaneous arterial dissections/ruptures (aorta, iliac, mesenteric, carotid) or hollow organ perforation (colon, gravid uterus). In the landmark randomized BBEST trial in vEDS (n=53), the cardioselective beta-blocker with beta-2 agonist properties celiprolol (up to 400 mg daily) significantly reduced the composite endpoint of arterial rupture, dissection, or death by 64% over 5 years (hazard ratio 0.36; 95% CI 0.15-0.88; p=0.018).",
        "solution_protocol": {
            "non_pharmacological_targets": "Closed-chain, low-resistance core stabilization and isometric physical therapy (avoiding joint hyper-extension and high-impact contact sports); wearing a medical alert bracelet for vEDS; mandatory avoidance of invasive arterial angiographies, colonoscopies, or elective surgeries in vEDS (high risk of arterial tearing).",
            "monitoring_cadence": "Comprehensive Beighton hypermobility scale at baseline; annual non-contrast MRA or CTA from skull base to pelvis for vascular surveillance in vEDS; annual echocardiogram assessing aortic root diameter; bone density scan.",
            "clinical_thresholds": "Unexplained acute chest, back, abdominal, or flank pain in a patient with confirmed or suspected COL3A1 vascular EDS mandates immediate non-contrast cross-sectional vascular imaging to rule out arterial dissection."
        },
        "patient_plain_language": "Ehlers-Danlos syndrome (EDS) is a group of inherited genetic conditions that affect collagen, the fibrous 'glue' that gives strength and support to your joints, skin, ligaments, and blood vessels. In hypermobile EDS, joints are extremely loose and flexible ('double-jointed'), easily popping out of place, accompanied by chronic pain and velvety skin. In the rare vascular type, blood vessel walls are fragile, requiring careful blood pressure control to protect internal arteries.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my Beighton joint hypermobility score, and do I meet the 2017 international criteria for hypermobile EDS?",
            "safety_question": "Have we ordered genetic panel testing for COL3A1 to rule out vascular Ehlers-Danlos syndrome?",
            "action_threshold_question": "What specialized physical therapy exercises (isometric stabilizing rather than stretching) will best protect my joints from dislocating?"
        },
        "red_flags": [
            "Sudden severe tearing pain in your chest, belly, or back (vascular dissection emergency), sudden shortness of breath from a collapsed lung, or severe rectal bleeding"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ehlers-Danlos syndromes are a group of inherited disorders that affect your connective tissues — primarily your skin, joints, and blood vessel walls.",
                "plain_analogy": "Faulty collagen glue in the body's building blocks, making joints loose like overstretched rubber bands and tissues fragile.",
                "lifestyle_action": "Avoid contact sports, heavy lifting, and stretching yoga. Focus on muscle strengthening around joints. Wear medical alert ID."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Celiprolol (for Vascular EDS)", "Losartan", "Acetaminophen", "Duloxetine (for chronic pain)"],
                "dosing_gdmt": "For Vascular EDS: Celiprolol 100-200 mg daily titrated to 400 mg daily. For chronic musculoskeletal pain: Duloxetine 30-60 mg daily.",
                "black_box_warning": "Invasive Endovascular Catheterization: High risk of catastrophic arterial tearing in vEDS; use non-invasive MRA/CTA.",
                "organ_clearance_cutoffs": "Target blood pressure <120/80 mmHg with beta-blockers/ARBs to reduce pulsatile mechanical stress on fragile vascular walls."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BBEST Trial",
                "pmid_or_doi": "10.1016/S0140-6736(10)60960-9",
                "cebm_level": 2,
                "sample_size": 53,
                "endpoints": "Arterial rupture, dissection, or death reduced by 64% with celiprolol (HR 0.36; p=0.018); arterial wall mechanical stability improved."
            }
        }
    },
    {
        "id": "DOC-CARD-277",
        "icd10": "G90.50",
        "condition": "Complex Regional Pain Syndrome (CRPS)",
        "specialty": "Neurology & Pain Medicine",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Association for the Study of Pain (IASP) Budapest Criteria",
        "source_body": "Pain (IASP Budapest Criteria) & Cochrane Reviews",
        "citation": "Harden RN et al. Validation of proposed diagnostic criteria (the 'Budapest Criteria') for Complex Regional Pain Syndrome. Pain. 2010;150(2):268-274.",
        "doi_or_source": "10.1016/j.pain.2010.04.030",
        "clinical_evidence": "Complex Regional Pain Syndrome (CRPS, formerly Reflex Sympathetic Dystrophy [CRPS Type 1] and Causalgia [CRPS Type 2 with defined major nerve lesion]) is a debilitating chronic neuropathic pain condition, typically developing after a limb trauma, fracture, or surgery, characterized by continuing pain disproportionate in time or degree to the inciting event. The validated IASP Budapest Clinical Diagnostic Criteria (sensitivity 99%, specificity 68%) require continuing disproportionate pain plus at least 1 symptom in 3 of 4 categories and at least 1 sign in 2 of 4 categories: (1) Sensory: hyperalgesia or allodynia; (2) Vasomotor: temperature asymmetry (>1°C) or skin color changes; (3) Sudomotor/Edema: edema or sweating changes; (4) Motor/Trophic: decreased range of motion, motor weakness, tremor, or dystonia, and abnormal hair, nail, or skin trophic changes. Early functional physical therapy combined with graded motor imagery (GMI) and mirror therapy reduces pain scores significantly.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate, aggressive functional physical and occupational therapy focused on active movement and weight-bearing; Graded Motor Imagery (GMI: left/right limb judgment, imagined movements, and mirror therapy); desensitization therapy using textured cloths; contrast baths.",
            "monitoring_cadence": "Numeric Pain Rating Scale (NPRS) and Budapest sign category scoring at every visit; bilateral limb skin temperature infrared measurement; functional goniometric joint range of motion.",
            "clinical_thresholds": "Refractory pain preventing active rehabilitation warrants diagnostic and therapeutic sympathetic nerve block (stellate ganglion block for upper extremity; lumbar sympathetic block for lower extremity) or spinal cord stimulation (SCS)."
        },
        "patient_plain_language": "Complex regional pain syndrome (CRPS) is a severe, chronic nerve pain condition that usually develops in an arm or leg after an injury, sprain, fracture, or surgery. The pain is far more intense, burning, and longer-lasting than the original injury. The affected limb becomes hypersensitive to touch (even a light bedsheet brushing against the skin feels agonizing), swells, changes color (turning red, purple, or mottled), and feels hot or ice-cold compared to the other limb.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my affected limb meet the IASP Budapest criteria for Complex Regional Pain Syndrome?",
            "safety_question": "Can we start graded motor imagery and mirror visual therapy right away to retrain the pain maps in my brain?",
            "action_threshold_question": "Would a sympathetic nerve block (stellate ganglion or lumbar sympathetic block) help break the pain cycle so I can participate in physical therapy?"
        },
        "red_flags": [
            "Severe progressive limb dystonia (hand curling into a tight fist or foot twisting inward), rapid bone thinning on X-ray, or skin breakdown with non-healing ulcers"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Complex regional pain syndrome is a form of chronic pain that usually affects an arm or a leg, typically developing after an injury or surgery.",
                "plain_analogy": "A fire alarm that continues blaring at maximum volume months after the original small kitchen fire has already been put out.",
                "lifestyle_action": "Do not immobilize the limb in a cast. Keep moving the fingers or toes gently. Practice desensitization with soft fabrics."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Gabapentin", "Pregabalin (Lyrica)", "Duloxetine", "Topical Lidocaine 5% Patch", "Intravenous Pamidronate"],
                "dosing_gdmt": "Gabapentin 300 mg at bedtime, titrated up to 900-1200 mg TID. Or Pregabalin 75-150 mg BID. Topical Lidocaine patches 12 hours on/off.",
                "black_box_warning": "Gabapentinoids: Serious respiratory depression when co-administered with central nervous system depressants or opioids.",
                "organ_clearance_cutoffs": "Adjust gabapentin dose based on creatinine clearance; avoid long-term opioid reliance which induces hyperalgesia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Budapest Validation Study",
                "pmid_or_doi": "10.1016/j.pain.2010.04.030",
                "cebm_level": 1,
                "sample_size": 1130,
                "endpoints": "Budapest criteria achieve 99% diagnostic sensitivity; early physical therapy and graded motor imagery achieve significant pain reduction."
            }
        }
    },
    {
        "id": "DOC-CARD-278",
        "icd10": "M50.10",
        "condition": "Cervical Radiculopathy (Cervical Spondylosis)",
        "specialty": "Neurology & Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: North American Spine Society (NASS) Evidence-Based Guideline",
        "source_body": "Spine Journal (NASS Guidelines) & Cochrane Database",
        "citation": "Bono CM et al. An evidence-based clinical guideline for the diagnosis and treatment of cervical radiculopathy from degenerative disorders. Spine J. 2011;11(1):64-72.",
        "doi_or_source": "10.1016/j.spinee.2010.10.023",
        "clinical_evidence": "Cervical radiculopathy is neurological dysfunction caused by mechanical compression or inflammatory irritation of a cervical spinal nerve root, most commonly resulting from cervical disk herniation (20-25%) or degenerative foraminal stenosis from uncovertebral/facet spondylosis (70-75%), predominantly involving C6 (biceps reflex, thumb sensation, wrist extension) and C7 (triceps reflex, middle finger sensation, elbow extension). Clinical provocative testing (Spurling's neck compression test [specificity 93%], shoulder abduction relief test [Bakody sign, specificity 90%], and upper limb tension test of Elvey [sensitivity 97%]) has high diagnostic accuracy. In high-quality randomized trials, conservative multimodal therapy (cervical mechanical traction, physical therapy, short-course NSAIDs/oral steroids) resolves radicular symptoms in 75-90% of patients without surgery over 2 to 3 months. Anterior cervical discectomy and fusion (ACDF) achieves rapid, reliable pain relief in refractory cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Home cervical mechanical intermittent traction therapy (10-15 lbs for 15-20 minutes daily); directional McKenzie neck extension exercises; ergonomic computer workstation optimization (raising monitors to eye level; avoiding 'tech-neck' forward flexed posture).",
            "monitoring_cadence": "Neck Disability Index (NDI) and visual analog pain scores at 2, 6, and 12 weeks; motor strength grading (0-5) in upper extremity myotomes (deltoid, biceps, wrist extensors, triceps, hand intrinsics); cervical spine MRI without contrast.",
            "clinical_thresholds": "Progressive focal motor deficit (e.g. wrist drop or triceps weakness dropping to Grade 3/5) or symptoms of cervical myelopathy (hyperreflexia, Hoffman's sign, gait ataxia) mandates urgent surgical decompression (ACDF)."
        },
        "patient_plain_language": "Cervical radiculopathy, commonly called a 'pinched nerve in the neck', occurs when a nerve root leaving your spinal cord in your neck is squeezed or irritated by a bulging spinal disc or arthritic bone spur. This pinched nerve sends sharp, electric, shooting pain, numbness, and tingling travelling down your neck and shoulder, through your arm, and into your fingers.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which specific cervical nerve root level (like C6 or C7) is compressed on my cervical spine MRI?",
            "safety_question": "Do I have any signs of cervical myelopathy (spinal cord compression, such as clumpy clumsy hands or unsteady balance)?",
            "action_threshold_question": "Would a course of physical therapy combined with cervical traction or a targeted epidural steroid injection relieve my shooting arm pain?"
        },
        "red_flags": [
            "Rapidly worsening weakness in your arm or hand (inability to lift arm or open jars), unsteady balance when walking, or numbness in both hands and feet (Cervical Myelopathy)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cervical radiculopathy is a pinched nerve in the neck caused by a herniated disk or bone spur pressing on the nerve roots.",
                "plain_analogy": "A garden hose being stepped on where it exits the wall (neck), shutting off the water flow and sending tingling sparks down to the nozzle (hand).",
                "lifestyle_action": "Avoid looking down at phones (raise screens to eye level). Use a supportive ergonomic neck pillow. Practice gentle chin-tuck exercises."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Meloxicam", "Gabapentin", "Methylprednisolone Dose Pack", "Cyclobenzaprine", "Dexamethasone (Transforaminal ESI)"],
                "dosing_gdmt": "Acute flare: Methylprednisolone dose pack (6-day oral taper) + Meloxicam 15 mg daily. Neuropathic pain: Gabapentin 300-600 mg TID.",
                "black_box_warning": "Cervical Epidural Steroid Injections: Serious neurologic events including spinal cord infarction, stroke, and quadriplegia; use real-time fluoroscopy.",
                "organ_clearance_cutoffs": "Monitor for NSAID gastrointestinal and renal toxicity; short courses preferred."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NASS Cervical Radiculopathy",
                "pmid_or_doi": "10.1016/j.spinee.2010.10.023",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Conservative multimodal therapy achieves complete resolution in 80-90%; ACDF provides rapid neurological decompression in refractory deficits."
            }
        }
    },
    {
        "id": "DOC-CARD-279",
        "icd10": "M75.0",
        "condition": "Adhesive Capsulitis (Frozen Shoulder)",
        "specialty": "Orthopedics & Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Randomized Trials",
        "source_body": "Cochrane Database of Systematic Reviews & BMJ",
        "citation": "Page MJ et al. Manual therapy and exercise for adhesive capsulitis (frozen shoulder). Cochrane Database Syst Rev. 2014;2014(8):CD011275.",
        "doi_or_source": "10.1002/14651858.CD011275",
        "clinical_evidence": "Adhesive Capsulitis (frozen shoulder) is a progressive fibro-inflammatory contracture of the glenohumeral joint capsule, characterized by capsular thickening, volume reduction, and obliteration of the axillary recess, strongly associated with diabetes mellitus (prevalence up to 20%), thyroid disorders, and prolonged immobilization. It progresses classically through 3 distinct phases: (1) Freezing phase (2-9 months, severe pain worse at night); (2) Frozen phase (4-12 months, profound restriction of both active AND passive glenohumeral motion in a capsular pattern [external rotation > abduction > internal rotation]); and (3) Thawing phase (5-24 months, gradual restoration of motion). Cochrane systematic reviews confirm that ultrasound-guided intra-articular corticosteroid injection (triamcinolone 40 mg) combined with gentle home stretching provides superior early pain relief and functional motion recovery compared with physical therapy alone (standardized mean difference -0.73; p<0.001). Image-guided capsular distension (hydrodilatation) provides rapid capsular mechanical stretching.",
        "solution_protocol": {
            "non_pharmacological_targets": "Gentle, non-aggressive active-assisted range of motion exercises (pendulum Codman exercises, wall-climbing finger stretches, and gentle pulley stretches) within pain-free limits (aggressive forced stretching exacerbates capsular inflammation); moist heat before stretching.",
            "monitoring_cadence": "Goniometric measurement of active and passive glenohumeral external rotation, forward flexion, and abduction every 4-6 weeks; Shoulder Pain and Disability Index (SPADI) scoring.",
            "clinical_thresholds": "Severe frozen phase with passive external rotation <30 degrees refractory to 3-6 months of conservative therapy warrants glenohumeral hydrodilatation or arthroscopic capsular release."
        },
        "patient_plain_language": "Adhesive capsulitis, commonly known as 'frozen shoulder', is a condition where the strong connective tissue capsule surrounding your shoulder joint becomes thick, tight, and severely inflamed. The capsule shrinks and loses its normal lubricating fluid, making the shoulder joint physically 'freeze' in place. It becomes agonizingly painful to reach overhead, fasten a seatbelt, or put your arm through a jacket sleeve, and the arm cannot be moved even when someone else gently tries to lift it for you.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my measured passive external rotation in degrees compared to my healthy shoulder?",
            "safety_question": "Would an ultrasound-guided steroid injection directly into my shoulder joint capsule help 'thaw' the joint and relieve my night pain?",
            "action_threshold_question": "Should I be tested for diabetes or thyroid disease, which are strong risk factors for developing frozen shoulder?"
        },
        "red_flags": [
            "Complete inability to move the shoulder accompanied by high fever and red warm skin (septic arthritis emergency), severe numbness in the arm, or neck pain radiating past elbow"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Frozen shoulder, also known as adhesive capsulitis, is a condition characterized by stiffness and pain in your shoulder joint.",
                "plain_analogy": "The shoulder joint's protective sleeve shrinking like a wool sweater washed in hot water, trapping the arm bone in a tight grip.",
                "lifestyle_action": "Do gentle pendulum swings daily. Apply warm compresses before stretching. Never force the shoulder past sharp pain."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Triamcinolone Acetonide (Intra-articular)", "Methylprednisolone Acetate", "Naproxen", "Acetaminophen"],
                "dosing_gdmt": "Intra-articular injection: Triamcinolone acetonide 40 mg mixed with 3-4 mL 1% lidocaine under ultrasound guidance into glenohumeral joint.",
                "black_box_warning": "Joint Injections: Monitor diabetic patients closely as intra-articular steroids cause transient blood glucose spikes for 48-72 hours.",
                "organ_clearance_cutoffs": "Limit glenohumeral steroid injections to a maximum of 2-3 per year to avoid cartilage chondrotoxicity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Cochrane Frozen Shoulder Review",
                "pmid_or_doi": "10.1002/14651858.CD011275",
                "cebm_level": 1,
                "sample_size": 1850,
                "endpoints": "Intra-articular steroid injection achieves superior rapid pain relief and range of motion recovery vs physiotherapy alone (SMD -0.73; p<0.001); hydrodilatation accelerates thawing."
            }
        }
    },
    {
        "id": "DOC-CARD-280",
        "icd10": "M70.60",
        "condition": "Greater Trochanteric Pain Syndrome (Trochanteric Bursitis)",
        "specialty": "Orthopedics & Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Multicenter Trial",
        "source_body": "British Journal of Sports Medicine (BJSM) & Cochrane",
        "citation": "Mellor R et al. Education plus exercise versus corticosteroid injection use versus a wait and see approach on global outcome and pain from gluteal tendinopathy: prospective, single blinded, randomised clinical trial. BMJ. 2018;361:k1662.",
        "doi_or_source": "10.1136/bmj.k1662.",
        "clinical_evidence": "Greater Trochanteric Pain Syndrome (GTPS, formerly trochanteric bursitis) is an umbrella term encompassing gluteus medius/minimus tendinopathy, partial or full-thickness tears, and trochanteric bursal inflammation, predominantly affecting women aged >50. Diagnostic hallmark is point tenderness elicited directly over the greater trochanter of the femur, exacerbated by lying on the affected side, prolonged standing, single-leg stance for 30 seconds (reproduction of pain, sensitivity 100%), and resisted hip abduction in 90 degrees flexion. In the landmark randomized clinical trial (n=204 patients), load management education plus targeted isometric/eccentric gluteal strengthening exercises achieved superior global recovery at 1 year compared with corticosteroid injection (78% vs 58%; difference 20 percentage points; 95% CI 7-34; p=0.003) and had a vastly lower recurrence rate. Radial extracorporeal shockwave therapy (rESWT) provides significant clinical improvement in recalcitrant tendinopathy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Gluteal load management education: avoid crossing legs while seated; place a pillow between knees when sleeping on unaffected side; avoid standing with hip hitched to one side; progressive isometric gluteal strengthening (side-lying clam-shells, bridge exercises, resistance band lateral walks).",
            "monitoring_cadence": "Victorian Institute of Sport Assessment-Gluteal (VISA-G) questionnaire and numerical pain scale at 4, 8, 12 weeks; pelvic radiograph to rule out hip osteoarthritis; non-contrast hip MRI if non-responsive to identify full-thickness gluteal tendon avulsions.",
            "clinical_thresholds": "Refractory pain preventing sleep and ambulation despite 6 weeks of targeted physiotherapy warrants an ultrasound-guided trochanteric bursa corticosteroid injection or radial shockwave therapy."
        },
        "patient_plain_language": "Greater trochanteric pain syndrome (often called trochanteric bursitis) is a condition that causes sharp or aching pain on the outside of your hip and upper thigh. While previously thought to just be an inflamed fluid sac (bursa), it is most often caused by wear-and-tear or micro-tears in the strong gluteal hip tendons that anchor your buttock muscles to the hip bone. The pain is triggered by lying on that side in bed, climbing stairs, or walking long distances.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my hip pain stem primarily from gluteal tendinopathy or trochanteric bursitis on my physical exam and MRI?",
            "safety_question": "What specific hip-loading habits (like crossing my legs or sleeping without a pillow between my knees) should I stop doing immediately?",
            "action_threshold_question": "Would targeted tendon-strengthening exercises or shockwave therapy provide a better long-term cure than a temporary cortisone shot?"
        },
        "red_flags": [
            "Sudden severe inability to bear any weight on the leg after a fall (suspect hip fracture), persistent groin pain, fever with hot red swelling over the hip, or severe night pain waking you from sleep"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Trochanteric bursitis is inflammation of the bursa, a fluid-filled sac on the outer point of the hip, causing pain along the outer hip and thigh.",
                "plain_analogy": "The heavy-duty tendon straps connecting your buttock muscles to your outer hip bone becoming frayed and inflamed from repetitive friction.",
                "lifestyle_action": "Sleep with a pillow between your knees. Never cross your legs while sitting. Perform daily gluteal strengthening exercises."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Triamcinolone Acetonide (Bursal Injection)", "Meloxicam", "Ibuprofen", "Topical Diclofenac Gel"],
                "dosing_gdmt": "Ultrasound-guided trochanteric bursa injection: Triamcinolone 40 mg + 1% Lidocaine 3-5 mL. Topical Diclofenac gel 4g TID to lateral hip.",
                "black_box_warning": "Direct tendon injections: Avoid injecting corticosteroids directly into the gluteus medius tendon substance to prevent tendon rupture.",
                "organ_clearance_cutoffs": "Oral NSAIDs show modest benefit; targeted exercise therapy provides far superior 1-year outcomes."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BMJ Gluteal Tendinopathy",
                "pmid_or_doi": "10.1136/bmj.k1662.",
                "cebm_level": 1,
                "sample_size": 204,
                "endpoints": "Targeted exercise plus education achieved 78% 1-year success vs 58% with steroid injection (p=0.003); recurrence significantly lower with exercise."
            }
        }
    }
]
