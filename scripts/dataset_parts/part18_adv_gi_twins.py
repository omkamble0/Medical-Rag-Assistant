"""
part18_adv_gi_twins.py
"""

PART_18_DISEASES = [
    {
        "id": "DOC-CARD-441",
        "icd10": "K74.3",
        "condition": "Primary Biliary Cholangitis (PBC - Anti-Mitochondrial Antibodies)",
        "specialty": "Hepatology & Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidelines on PBC",
        "source_body": "Hepatology",
        "citation": "Lindor KD et al. Primary Biliary Cholangitis: 2018 Practice Guidance from the American Association for the Study of Liver Diseases. Hepatology. 2019;69(1):394-419.",
        "doi_or_source": "10.1002/hep.30145",
        "clinical_evidence": "URSODEOXYCHOLIC ACID (UDCA 13-15 mg/kg/day) is the foundational first-line therapy, delaying histological progression and significantly prolonging transplant-free survival (Paris II criteria: normal bilirubin and alkaline phosphatase <1.5x ULN). In inadequate responders (~40%), adding Obeticholic Acid or Bezafibrate/PPAR agonists normalizes liver biochemistry and halts fibrosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Lifelong adherence to UDCA; manage severe pruritus with bile acid sequestrants (Cholestyramine); screening for osteoporosis with DXA scan (PBC markedly accelerates metabolic bone disease); fat-soluble vitamin supplementation (A, D, E, K).",
            "monitoring_cadence": "Alkaline phosphatase (ALP), total bilirubin, and liver enzymes every 3-6 months; annual transient elastography (FibroScan) tracking liver stiffness; screening for esophageal varices if cirrhosis suspected.",
            "clinical_thresholds": "Alkaline phosphatase >1.5x ULN with positive Anti-Mitochondrial Antibodies (AMA titer >=1:40) confirms PBC without requiring liver biopsy."
        },
        "patient_plain_language": "An autoimmune condition where your body's immune system slowly attacks and destroys the microscopic bile ducts inside your liver. When bile cannot drain, it backs up into liver cells and spills into your blood, causing severe full-body skin itching (pruritus) and deep exhaustion. Taking a natural bile acid pill (Ursodiol) daily protects your liver cells and prevents cirrhosis.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my blood test show positive Anti-Mitochondrial Antibodies (AMA) and elevated alkaline phosphatase?",
            "safety_question": "Am I taking the correct weight-based dose of Ursodiol (13 to 15 mg per kilogram of body weight)?",
            "action_threshold_question": "Have I had a bone density (DXA) scan to check for osteoporosis, which is very common with PBC?"
        },
        "red_flags": [
            "Rapid onset of yellow jaundice with dark urine and pale clay-colored stools",
            "Vomiting blood or black stools indicating bleeding esophageal varices from portal hypertension"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "PBC is an autoimmune liver disease causing slow destruction of small bile ducts, leading to itching and fatigue.",
                "plain_analogy": "Tiny drainage ditches inside a farm field becoming clogged with debris, causing water to pool and rot the crop roots.",
                "lifestyle_action": "Take Ursodiol daily with meals, take cholestyramine for severe itching (spaced 4 hours apart), and exercise."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ursodeoxycholic Acid (UDCA / Ursodiol - First Line)",
                    "Obeticholic Acid (Ocaliva - Second Line FXR Agonist)",
                    "Cholestyramine oral (for pruritus)",
                    "Bezafibrate / Fenofibrate"
                ],
                "dosing_gdmt": "Ursodiol 13-15 mg/kg/day divided BID with meals; Obeticholic Acid 5 mg daily titrated to 10 mg.",
                "black_box_warning": "Obeticholic acid carries black box warning for hepatic decompensation/death in decompensated cirrhosis (Child-Pugh B/C).",
                "organ_clearance_cutoffs": "Cholestyramine must be taken at least 2-4 hours before or after Ursodiol to avoid binding."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-PBC",
                "pmid_or_doi": "10.1002/hep.30145",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "UDCA prolongs 10-year transplant-free survival to >85% in PBC patients who achieve biochemical response."
            }
        }
    },
    {
        "id": "DOC-CARD-442",
        "icd10": "K83.01",
        "condition": "Primary Sclerosing Cholangitis (PSC - Large Duct Beaded Strictures)",
        "specialty": "Gastroenterology & Hepatology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD PSC Practice Guidance",
        "source_body": "Hepatology",
        "citation": "Bowlus CL et al. AASLD Practice Guidance on Primary Sclerosing Cholangitis and Cholangiocarcinoma. Hepatology. 2023;77(2):659-702.",
        "doi_or_source": "10.1097/HEP.0000000000000043",
        "clinical_evidence": "PSC causes progressive fibrosing obliterative cholangitis of intra- and extra-hepatic bile ducts ('string-of-beads' / multifocal strictures on MRCP). 70-80% of patients have comorbid Inflammatory Bowel Disease (predominantly Ulcerative Colitis). PSC carries an intense 400-fold elevated risk of CHOLANGIOCARCINOMA (bile duct cancer). ANNUAL SURVEILLANCE with MRCP and CA 19-9, plus ANNUAL SCREENING COLONOSCOPY for colorectal cancer, is mandatory.",
        "solution_protocol": {
            "non_pharmacological_targets": "Screening colonoscopy at time of PSC diagnosis (even if asymptomatic) and annually thereafter due to aggressive right-sided colon cancer risk; endoscopic balloon dilation (without stenting) for dominant biliary strictures; complete alcohol abstinence.",
            "monitoring_cadence": "Annual MRCP and serum CA 19-9 for cholangiocarcinoma surveillance; annual surveillance colonoscopy with random biopsies; liver function tests every 3-6 months.",
            "clinical_thresholds": "Multifocal strictures and segmental dilatations ('beaded appearance') of intrahepatic and/or extrahepatic bile ducts on MRCP/ERCP with negative IgG4 serology."
        },
        "patient_plain_language": "A chronic disease that causes inflammation, scarring, and tightening of the medium and large bile pipes inside and outside your liver. Over 70% of people with PSC also have Ulcerative Colitis. Because the scarred ducts carry a significant risk of developing bile duct cancer (cholangiocarcinoma), having a yearly MRI scan and yearly colonoscopy is absolutely essential.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did Magnetic Resonance Cholangiopancreatography (MRCP) confirm the classic beaded pattern of my bile ducts?",
            "safety_question": "Have I had a colonoscopy to check for silent Ulcerative Colitis, and am I scheduled for annual surveillance?",
            "action_threshold_question": "Is my yearly screening MRI (MRCP) and CA 19-9 blood test scheduled to detect early bile duct tumors?"
        },
        "red_flags": [
            "Sudden high fever, shaking chills, and worsening jaundice (Bacterial Cholangitis from dominant stricture)",
            "Unexplained rapid weight loss with surging CA 19-9 tumor marker (>100 U/mL)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "PSC is chronic inflammation and scarring of large bile ducts, tightly linked with ulcerative colitis.",
                "plain_analogy": "Underground plumbing pipes developing thick mineral crusts and narrow kinks along their entire length.",
                "lifestyle_action": "Attend yearly MRCP scans and colonoscopies without fail, report any fevers immediately, and avoid alcohol."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Endoscopic Balloon Dilation (for dominant strictures)",
                    "Ursodeoxycholic Acid (low/moderate dose 13-15 mg/kg)",
                    "Broad-spectrum IV Antibiotics (for acute cholangitis)",
                    "Liver Transplantation (Curative for end-stage)"
                ],
                "dosing_gdmt": "Ursodiol 13-15 mg/kg/day; endoscopic balloon dilatation of dominant strictures with brush cytology/FISH.",
                "black_box_warning": "HIGH-DOSE Ursodiol (28-30 mg/kg/day) is HARMFUL and strictly contraindicated (doubles mortality/liver transplantation).",
                "organ_clearance_cutoffs": "Dose adjustments for liver failure; refer early for liver transplantation evaluation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-PSC",
                "pmid_or_doi": "10.1097/HEP.0000000000000043",
                "cebm_level": 1,
                "sample_size": 2400,
                "endpoints": "Endoscopic balloon dilation of dominant strictures preserves biliary drainage and delays liver failure."
            }
        }
    },
    {
        "id": "DOC-CARD-443",
        "icd10": "K75.4",
        "condition": "Autoimmune Hepatitis (Type 1 Anti-SMA & Hypergammaglobulinemia)",
        "specialty": "Hepatology",
        "organ_system": "Digestive & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidance on AIH",
        "source_body": "Hepatology",
        "citation": "Mack CL et al. Diagnosis and Management of Autoimmune Hepatitis in Adults and Children: 2019 Practice Guidance. Hepatology. 2020;72(2):671-722.",
        "doi_or_source": "10.1002/hep.31065",
        "clinical_evidence": "AIH is characterized by female predominance, circulating autoantibodies (Anti-Smooth Muscle Antibody / ASMA or ANA in Type 1; Anti-LKM1 in Type 2), elevated serum IgG (>1.2x ULN), and interface hepatitis on liver biopsy. COMBINATION INDUCTION THERAPY (Oral Prednisone 30 mg/day tapered to 10 mg + Azathioprine 1-2 mg/kg/day) achieves complete biochemical and histological remission in >85% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "TPMT (thiopurine methyltransferase) or NUDT15 enzyme testing MANDATORY prior to azathioprine initiation to prevent fatal bone marrow aplasia; complete alcohol avoidance; maintenance therapy for minimum 2-3 years before considering withdrawal.",
            "monitoring_cadence": "Liver enzymes (ALT/AST), total IgG, and total bilirubin monthly during induction, then every 3-6 months; CBC monitoring on azathioprine; repeat liver biopsy prior to treatment withdrawal.",
            "clinical_thresholds": "Simplified AIH diagnostic score >=7 points (autoantibodies, IgG, liver histology, absence of viral hepatitis) indicates definitive AIH."
        },
        "patient_plain_language": "Your own immune system mistakes your liver cells for foreign invaders and attacks them, driving up liver enzymes into the hundreds or thousands. If untreated, it causes rapid cirrhosis. Taking a combination of steroid pills (Prednisone) and an immune-calming pill (Azathioprine) successfully cools down the immune attack in over 85% of people.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my liver biopsy confirm interface hepatitis, and did blood tests show elevated IgG antibodies and anti-smooth muscle antibodies?",
            "safety_question": "Was my TPMT enzyme level tested before starting Azathioprine to make sure my bone marrow will be safe?",
            "action_threshold_question": "How long must I maintain normal liver enzymes (usually at least 2 to 3 years) before discussing tapering medicines?"
        },
        "red_flags": [
            "Sudden development of confusion, flapping hands (asterixis), and jaundice (Acute-on-chronic Liver Failure)",
            "White blood cell or platelet count crashing on Azathioprine (bone marrow suppression)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Autoimmune hepatitis is an immune disease where antibodies attack liver cells, causing high inflammation.",
                "plain_analogy": "A security guard dog turning around and biting the home residents it was trained to protect.",
                "lifestyle_action": "Take your immunosuppressive pills on schedule, have monthly blood tests, and never drink alcohol."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral (Induction 30-60 mg daily)",
                    "Azathioprine oral (Imuran 1-2 mg/kg/day)",
                    "Budesonide oral (alternative for non-cirrhotic AIH)",
                    "Mycophenolate Mofetil (Second Line)"
                ],
                "dosing_gdmt": "Prednisone 30 mg daily tapered over 4 weeks to 10 mg daily + Azathioprine 50-100 mg daily.",
                "black_box_warning": "Budesonide is STRICTLY CONTRAINDICATED in cirrhotic patients due to reduced first-pass clearance and portal vein thrombosis.",
                "organ_clearance_cutoffs": "Azathioprine requires regular CBC monitoring for leukopenia; adjust dose for TPMT intermediate activity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-AIH",
                "pmid_or_doi": "10.1002/hep.31065",
                "cebm_level": 1,
                "sample_size": 1950,
                "endpoints": "Prednisone plus azathioprine combination induces durable histological remission in >85% of AIH patients."
            }
        }
    },
    {
        "id": "DOC-CARD-444",
        "icd10": "E83.01",
        "condition": "Wilson's Disease (Hepatolenticular Degeneration - Copper Overload)",
        "specialty": "Medical Genetics & Hepatology",
        "organ_system": "Metabolic & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EASL Clinical Practice Guidelines on Wilson's Disease",
        "source_body": "Journal of Hepatology",
        "citation": "European Association for the Study of the Liver. EASL Clinical Practice Guidelines: Wilson's Disease. J Hepatol. 2012;56(3):671-685.",
        "doi_or_source": "10.1016/j.jhep.2011.11.007",
        "clinical_evidence": "Autosomal recessive ATP7B mutation impairs biliary copper excretion, causing toxic copper accumulation in liver, basal ganglia (dysarthria, dystonia, parkinsonism), and cornea (Kayser-Fleischer rings on slit-lamp). CHELATION THERAPY WITH PENICILLAMINE OR TRIENTINE promotes massive urinary copper excretion, while Oral Zinc blocks intestinal copper absorption. Lifelong therapy is mandatory; abrupt discontinuation causes fatal acute liver failure.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict low-copper diet (avoid shellfish, chocolate, mushrooms, nuts, organ meats, liver); avoid copper cookware and check copper plumbing pipes; lifelong medication adherence (never skip doses); family genetic screening.",
            "monitoring_cadence": "24-hour urinary copper excretion (baseline >100 mcg/24h; on chelation target 200-500 mcg/24h); slit-lamp eye examination; serum ceruloplasmin; non-ceruloplasmin-bound (free) copper.",
            "clinical_thresholds": "Low serum ceruloplasmin (<20 mg/dL), 24-hour urine copper >100 mcg, presence of Kayser-Fleischer rings, or liver copper concentration >250 mcg/g dry weight."
        },
        "patient_plain_language": "A genetic condition where your liver cannot pump extra dietary copper into bile. Over years, toxic copper piles up inside your liver and brain, causing cirrhosis, tremors, muscle stiffness, and golden-brown copper rings around your eyes (Kayser-Fleischer rings). Daily copper-binding medicine (Trientine or Penicillamine) flushes copper out in your urine.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did a specialized eye slit-lamp exam check for Kayser-Fleischer copper rings in my corneas?",
            "safety_question": "What was my 24-hour urine copper level, and is it in the correct target range on my copper-binding medication?",
            "action_threshold_question": "Why is it strictly dangerous to ever stop my copper medication, even for a few weeks?"
        },
        "red_flags": [
            "Acute hemolytic anemia combined with rapid liver failure and dark brown urine (Wilsonian Crisis)",
            "Sudden onset of slurred speech, tremors, swallowing difficulty, or personality changes"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Wilson's disease is genetic copper buildup in the liver and brain causing cirrhosis and tremors.",
                "plain_analogy": "A copper coin bank with no release latch, eventually overflowing and jamming the entire cash register.",
                "lifestyle_action": "Take your copper-chelating medicine daily on an empty stomach, avoid copper-rich foods, and get eye exams."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Trientine Dihydrochloride (First Line Chelator)",
                    "D-Penicillamine oral",
                    "Zinc Acetate (Galzin - Maintenance/Blocker)",
                    "Pyridoxine (Vitamin B6 25-50 mg daily with Penicillamine)"
                ],
                "dosing_gdmt": "Trientine 750-1,500 mg/day divided BID-TID on an empty stomach; Zinc Acetate 50 mg TID 1 hour before meals.",
                "black_box_warning": "Penicillamine causes paradoxical worsening of neurological symptoms in up to 30%; requires concurrent Pyridoxine.",
                "organ_clearance_cutoffs": "Regular monitoring of 24-hour urine copper, complete blood count, and urinalysis (proteinuria risk)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EASL-WILSON",
                "pmid_or_doi": "10.1016/j.jhep.2011.11.007",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "Lifelong copper chelation reverses hepatic dysfunction and prevents neurological disability in >90% of adherent patients."
            }
        }
    },
    {
        "id": "DOC-CARD-445",
        "icd10": "E83.110",
        "condition": "Hereditary Hemochromatosis (C282Y HFE Iron Overload)",
        "specialty": "Hematology & Hepatology",
        "organ_system": "Metabolic & Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidelines on Hemochromatosis",
        "source_body": "Hepatology",
        "citation": "Bacon BR et al. Diagnosis and Management of Hemochromatosis: 2011 Practice Guideline by AASLD. Hepatology. 2011;54(1):328-346.",
        "doi_or_source": "10.1002/hep.24330",
        "clinical_evidence": "Homozygosity for C282Y mutation in the HFE gene causes uncontrolled intestinal iron absorption, leading to parenchymal iron deposition ('Bronze Diabetes', cirrhosis, dilated cardiomyopathy, and pseudogout chondrocalcinosis). THERAPEUTIC PHLEBOTOMY (removing 500 mL blood weekly or biweekly until serum ferritin reaches 50-100 mcg/L) normalizes lifespan and prevents cirrhosis if started before advanced fibrosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Therapeutic phlebotomy schedule adherence; avoid medicinal iron and vitamin C supplements (vitamin C accelerates free iron absorption and cardiac toxicity); avoid raw shellfish (fatal Vibrio vulnificus septicemia); limit alcohol.",
            "monitoring_cadence": "Transferrin saturation (fasting >45% is highly sensitive) and serum ferritin every 2-4 phlebotomies during depletion, then every 6 months during maintenance; HFE gene testing.",
            "clinical_thresholds": "C282Y homozygosity (or C282Y/H63D compound heterozygosity) with transferrin saturation >=45% and elevated ferritin."
        },
        "patient_plain_language": "Your body absorbs far too much iron from ordinary food because of a genetic mutation in the HFE gene. The excess iron cannot be excreted, so it rusts and deposits inside your liver, heart, joints, and pancreas ('Bronze Diabetes'). The treatment is remarkably simple and natural: having a pint of blood removed (therapeutic phlebotomy) regularly until iron stores reach normal levels.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my fasting transferrin saturation percentage and total ferritin number?",
            "safety_question": "Did genetic testing confirm C282Y homozygosity in my HFE gene?",
            "action_threshold_question": "How frequently do I need therapeutic blood draws (phlebotomy) to reach a target ferritin of 50 to 100?"
        },
        "red_flags": [
            "Ferritin >1,000 mcg/L with elevated liver enzymes (indicates high risk for cirrhosis and hepatocellular carcinoma)",
            "Eating raw oysters or clams leading to sudden high fever and septic shock (Vibrio vulnificus emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hemochromatosis is genetic iron overload where the body absorbs too much iron, damaging internal organs.",
                "plain_analogy": "An automated coal feeder on a furnace that won't turn off, choking the firebox with heavy coal slag.",
                "lifestyle_action": "Undergo regular therapeutic blood donation (phlebotomy), never eat raw shellfish, and avoid iron vitamins."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Therapeutic Phlebotomy (Gold Standard Curative Therapy)",
                    "Deferasirox oral (Jadenu - Iron Chelator for non-phlebotomy candidates)",
                    "Deferoxamine IV/SubQ"
                ],
                "dosing_gdmt": "Phlebotomy of 500 mL (removes ~200-250 mg iron) weekly until ferritin 50-100 mcg/L; then maintenance 2-4x/year.",
                "black_box_warning": "Avoid oral Vitamin C supplements during active iron overload (mobilizes free iron into cardiac tissue).",
                "organ_clearance_cutoffs": "Monitor hemoglobin/hematocrit before each phlebotomy (hold if Hgb <11 g/dL)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-HEMOCHRO",
                "pmid_or_doi": "10.1002/hep.24330",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Early therapeutic phlebotomy before cirrhosis normalizes long-term life expectancy to match the general population."
            }
        }
    },
    {
        "id": "DOC-CARD-446",
        "icd10": "K31.84",
        "condition": "Gastroparesis (Delayed Gastric Emptying / Diabetic Gastroparesis)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline on Gastroparesis",
        "source_body": "American Journal of Gastroenterology",
        "citation": "Camilleri M et al. Clinical Guideline: Management of Gastroparesis. Am J Gastroenterol. 2022;117(8):1197-1226.",
        "doi_or_source": "10.14309/ajg.0000000000001874",
        "clinical_evidence": "Gastroparesis presents with chronic nausea, early satiety, and postprandial vomiting without mechanical obstruction. 4-hour Gastric Emptying Scintigraphy (GES) showing >10% retention at 4 hours establishes diagnosis. METOCLOPRAMIDE (oral or nasal spray Gimoti) remains the only FDA-approved medication, improving gastric motility via 5-HT4 agonism and D2 antagonism. G-POEM (Gastric Peroral Endoscopic Myotomy) provides durable surgical pyloromyotomy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary modification (small, frequent, low-fat, low-insoluble-fiber meals; blenderized liquid meals; sit upright for 2 hours post-meal); strict glycemic control in diabetics (acute hyperglycemia >200 mg/dL directly inhibits gastric motility); avoid opioids and GLP-1 receptor agonists.",
            "monitoring_cadence": "4-hour solid-phase gastric emptying scintigraphy (holding prokinetics and narcotics 48-72h prior); serial HbA1c and nutritional panel; monitor for involuntary facial movements.",
            "clinical_thresholds": "Gastric retention >60% at 2 hours or >10% at 4 hours on standardized solid-phase radiolabeled meal."
        },
        "patient_plain_language": "The muscular pump of your stomach becomes sluggish and partly paralyzed (often caused by diabetes or nerve injury). Food sits in your stomach for hours without moving into your intestines, causing you to feel stuffed after just a few bites, nauseated, and vomiting undigested food eaten hours earlier. Eating small, low-fiber, blended meals helps gravity pull food down.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my 4-hour gastric emptying stomach scan confirm delayed retention greater than 10%?",
            "safety_question": "Am I taking any medications that freeze stomach motility, such as GLP-1 weight-loss injections or opioids?",
            "action_threshold_question": "Why is Metoclopramide restricted to short courses, and what involuntary facial twitching signs should I watch for?"
        },
        "red_flags": [
            "Involuntary lip smacking, tongue thrusting, or facial grimacing (Tardive Dyskinesia from Metoclopramide - STOP IMMEDIATELY)",
            "Severe persistent vomiting causing profound hypokalemia, metabolic alkalosis, and acute kidney injury"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Gastroparesis is delayed emptying of the stomach causing nausea, early fullness, and vomiting.",
                "plain_analogy": "A kitchen sink garbage disposal running at 10% speed, causing food waste to back up and sit in the basin.",
                "lifestyle_action": "Eat 5-6 small low-fat meals daily, chew thoroughly, stay upright after eating, and avoid GLP-1 drugs."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Metoclopramide oral/nasal (Reglan / Gimoti - FDA Approved)",
                    "Domperidone oral (Expanded Access D2 Antagonist)",
                    "Erythromycin oral/IV (Motilin Agonist)",
                    "G-POEM (Endoscopic Pyloromyotomy)"
                ],
                "dosing_gdmt": "Metoclopramide 5-10 mg orally 30 min before meals and at bedtime (maximum 12 weeks duration).",
                "black_box_warning": "Metoclopramide black box warning for irreversible Tardive Dyskinesia; strictly avoid beyond 12 weeks.",
                "organ_clearance_cutoffs": "Dose reduction by 50% in renal impairment (eGFR <40 mL/min)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-GASTROPARESIS",
                "pmid_or_doi": "10.14309/ajg.0000000000001874",
                "cebm_level": 1,
                "sample_size": 2200,
                "endpoints": "Dietary modification plus short-course prokinetics reduces nausea and postprandial vomiting in >70% of gastroparesis."
            }
        }
    },
    {
        "id": "DOC-CARD-447",
        "icd10": "K22.0",
        "condition": "Esophageal Achalasia (Aperistalsis & Non-Relaxing LES)",
        "specialty": "Gastroenterology & Thoracic Surgery",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Achalasia Guidelines & POEM Randomized Trials",
        "source_body": "American Journal of Gastroenterology & NEJM",
        "citation": "Vaezi MF et al. ACG Clinical Guidelines: Diagnosis and Management of Achalasia. Am J Gastroenterol. 2020;115(9):1393-1411.",
        "doi_or_source": "10.14309/ajg.0000000000000731",
        "clinical_evidence": "Loss of inhibitory myenteric ganglion cells causes absent esophageal peristalsis and failed relaxation of the lower esophageal sphincter (LES). HIGH-RESOLUTION MANOMETRY (HRM utilizing Chicago Classification v4.0: integrated relaxation pressure / IRP elevated) is the diagnostic gold standard. POEM (Peroral Endoscopic Myotomy) or Laparoscopic Heller Myotomy with fundoplication provides >90% long-term dysphagia relief.",
        "solution_protocol": {
            "non_pharmacological_targets": "Chew food thoroughly, drink carbonated water with meals (hydrostatic pressure aids emptying); avoid eating within 3-4 hours of lying down; sleep with head of bed elevated 30 degrees.",
            "monitoring_cadence": "High-resolution esophageal manometry; timed barium esophagram (measuring column height at 1, 2, and 5 minutes); upper endoscopy (to rule out pseudoachalasia from gastroesophageal junction adenocarcinoma).",
            "clinical_thresholds": "Eckardt Symptom Score >3; Chicago Classification Type I (classic), Type II (pan-esophageal pressurization - best response), or Type III (spastic)."
        },
        "patient_plain_language": "The muscular ring at the bottom of your swallowing tube (lower esophageal sphincter) stays clamped shut like a clenched fist and refuses to open when you swallow. Food and liquids pile up in your esophagus, causing severe difficulty swallowing, chest pain, and regurgitation of undigested meals. A minimally invasive procedure (POEM) cuts the tight muscle ring open, letting food drop freely into your stomach.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which Chicago Classification subtype (Type I, II, or III) was diagnosed on my high-resolution manometry test?",
            "safety_question": "Am I a candidate for Peroral Endoscopic Myotomy (POEM) or Laparoscopic Heller Myotomy to cut the tight muscle?",
            "action_threshold_question": "Did upper endoscopy rule out a hidden tumor at the stomach junction (pseudoachalasia)?"
        },
        "red_flags": [
            "Waking up coughing and choking on regurgitated food (Aspiration Pneumonia risk)",
            "Rapid unexplained weight loss with inability to keep liquids down"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Achalasia is a swallowing disorder where the lower esophagus muscle fails to relax and open.",
                "plain_analogy": "A locked exit turnstile at a train station that refuses to turn, causing commuters to back up in the tunnel.",
                "lifestyle_action": "Chew food into fine paste, drink water with meals, never eat before bed, and consult for POEM myotomy."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Peroral Endoscopic Myotomy (POEM - Endoscopic)",
                    "Laparoscopic Heller Myotomy with Dor/Toupet Fundoplication",
                    "Pneumatic Balloon Dilation (30-35-40 mm)",
                    "Botulinum Toxin Injection (for high surgical risk)"
                ],
                "dosing_gdmt": "POEM or Heller Myotomy is definitive; Botulinum Toxin 100 units injected into 4 quadrants of LES.",
                "black_box_warning": "Botox injections provide only short-term relief (6-12 months) and cause transmural scarring that complicates future surgery.",
                "organ_clearance_cutoffs": "Proton pump inhibitors post-POEM to treat iatrogenic gastroesophageal acid reflux."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POEM-VS-HELLER",
                "pmid_or_doi": "10.1056/NEJMoa1905380",
                "cebm_level": 2,
                "sample_size": 221,
                "endpoints": "POEM is non-inferior to laparoscopic Heller myotomy in relieving dysphagia at 2 years (83.0% vs 81.7%; p=0.007)."
            }
        }
    },
    {
        "id": "DOC-CARD-448",
        "icd10": "K22.5",
        "condition": "Zenker's Diverticulum (Killian Triangle Pharyngeal Pouch)",
        "specialty": "Otolaryngology & Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASGE Guideline on Zenker Diverticulum",
        "source_body": "Gastrointestinal Endoscopy",
        "citation": "Faulx MD et al. The Role of Endoscopy in the Management of Patients with Zenker's Diverticulum. Gastrointest Endosc. 2014;79(4):554-559.",
        "doi_or_source": "10.1016/j.gie.2013.09.006",
        "clinical_evidence": "Failure of cricopharyngeus muscle relaxation causes high intraluminal pressure, herniating pharyngeal mucosa through Killian's triangle (anatomical weak spot between thyropharyngeus and cricopharyngeus). Presents with oropharyngeal dysphagia, regurgitation of foul undigested food hours later, halitosis, and gurgling in the neck. ENDOSCOPIC CRICOPHARYNGEAL MYOTOMY (flexible or rigid endoscopic diverticulotomy / Z-POEM) achieves >90% symptom resolution.",
        "solution_protocol": {
            "non_pharmacological_targets": "Chew food thoroughly; drink liquids between mouthfuls; sleep with head of bed elevated; speech-language pathology swallowing therapy post-myotomy.",
            "monitoring_cadence": "Barium swallow / esophagram (diagnostic test of choice showing posterior sacculation at C5-C6 level); upper endoscopy must be performed with EXTREME CAUTION (high risk of blind pouch perforation).",
            "clinical_thresholds": "Presence of posterior diverticulum pouch at the pharyngoesophageal junction on dynamic video fluoroscopic swallowing study."
        },
        "patient_plain_language": "A small outpouching or pocket forms at the back of your throat, right above your swallowing tube. Food gets trapped inside this pouch instead of going down to your stomach. Hours or days later, trapped undigested food regurgitates back into your mouth with a foul smell (halitosis) and loud gurgling noises in your neck. A quick endoscopic laser or scissor myotomy cuts the pouch wall, allowing food to slide straight down.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did a barium swallow X-ray confirm the size and location of my Zenker's throat pouch?",
            "safety_question": "Am I a candidate for minimally invasive endoscopic myotomy (Z-POEM or stapling) through the mouth without neck incisions?",
            "action_threshold_question": "Why should standard endoscopies and blind feeding tubes be avoided or performed with extreme caution?"
        },
        "red_flags": [
            "Sudden choking spell during sleep followed by fever and cough (Aspiration Pneumonia from trapped food)",
            "Complete inability to swallow saliva with neck tenderness (Impaction or perforation)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Zenker's diverticulum is an outpouching in the back of the throat that catches food, causing regurgitation and bad breath.",
                "plain_analogy": "A secret pocket inside a mail chute where letters catch and pile up instead of sliding down into the collection bin.",
                "lifestyle_action": "Chew food into fine pieces, drink water after each bite, and consult for endoscopic pouch division."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Flexible Endoscopic Cricopharyngeal Myotomy (Z-POEM)",
                    "Rigid Transoral Stapling Diverticulotomy",
                    "Open Cricopharyngeal Myotomy with Diverticulectomy"
                ],
                "dosing_gdmt": "Transoral endoscopic division of the cricopharyngeal septum; clear liquid diet for 24-48h post-procedure.",
                "black_box_warning": "WARNING: Blind insertion of nasogastric tubes or blind endoscopy risks fatal pharyngeal perforation into the mediastinum.",
                "organ_clearance_cutoffs": "No systemic pharmacotherapy treats Zenker's pouch; anatomical correction is required."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASGE-ZENKER",
                "pmid_or_doi": "10.1016/j.gie.2013.09.006",
                "cebm_level": 1,
                "sample_size": 1150,
                "endpoints": "Endoscopic cricopharyngeal myotomy resolves dysphagia in >90% of Zenker's patients with <3% complication rate."
            }
        }
    },
    {
        "id": "DOC-CARD-449",
        "icd10": "K52.831",
        "condition": "Microscopic Colitis: Collagenous Colitis (Subepithelial Band)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AGA Clinical Practice Guideline on Microscopic Colitis",
        "source_body": "Gastroenterology",
        "citation": "Fernandez-Banares F et al. AGA Institute Clinical Practice Guideline on the Medical Management of Microscopic Colitis. Gastroenterology. 2016;150(1):242-246.",
        "doi_or_source": "10.1053/j.gastro.2015.11.008",
        "clinical_evidence": "Collagenous colitis presents with chronic, profuse, watery, non-bloody diarrhea (>4-10 bowel movements/day) with completely NORMAL-APPEARING colonic mucosa on colonoscopy. Diagnosis requires random colonic mucosal biopsies showing a thickened subepithelial collagen band (>10 micrometers). ORAL BUDESONIDE (9 mg/day x 6-8 weeks) is the gold standard Level 1 therapy, inducing clinical remission in >80-88% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinue potential offending medications (NSAIDs, Proton Pump Inhibitors, SSRIs, H2 blockers, Statins); avoid caffeine, artificial sweeteners (sorbitol), and dairy during flares; adequate hydration.",
            "monitoring_cadence": "Stool frequency and consistency tracking (diarrhea diary); screening for celiac disease (present in 5-10% of microscopic colitis); repeat colonoscopy only if refractory to budesonide.",
            "clinical_thresholds": "Subepithelial collagen band >10 micrometers on trichrome stain with chronic inflammatory infiltrate in lamina propria."
        },
        "patient_plain_language": "A condition causing chronic, watery diarrhea (often 5 to 10 watery stools a day) where your colon appears 100% healthy and pink on colonoscopy. The inflammation is only visible under a microscope, where a thick band of collagen scar tissue lines the bowel wall. Specialized gut-targeted steroid pills (Budesonide) heal the microscopic inflammation in over 85% of people.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did colon biopsy specimens taken from throughout my colon confirm the thick collagen band under the microscope?",
            "safety_question": "Have we stopped common medication triggers like ibuprofen (Advil), omeprazole (Prilosec), or sertraline (Zoloft)?",
            "action_threshold_question": "Have I been screened for Celiac disease (gluten allergy), which often occurs alongside collagenous colitis?"
        },
        "red_flags": [
            "Severe watery diarrhea (>10 bowel movements/day) causing dizziness, postural hypotension, and acute kidney injury",
            "Unexplained significant weight loss (>10% body weight) and profound fatigue"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Collagenous colitis is chronic watery diarrhea caused by a microscopic layer of collagen scar tissue in the colon.",
                "plain_analogy": "A porous filter cloth that has a layer of plastic wrap glued across it, preventing water from being absorbed.",
                "lifestyle_action": "Take Budesonide as prescribed, stop all NSAID painkillers and heartburn pills, and stay hydrated."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Budesonide oral (Entocort EC - 9 mg daily First Line)",
                    "Cholestyramine oral (for bile acid diarrhea overlap)",
                    "Bismuth Subsalicylate (Pepto-Bismol)",
                    "Anti-TNF (Infliximab for refractory)"
                ],
                "dosing_gdmt": "Budesonide 9 mg once daily in the morning x 6-8 weeks; then taper to 6 mg daily x 2-4 weeks, then 3 mg daily.",
                "black_box_warning": "Budesonide undergoes 90% first-pass hepatic metabolism, drastically reducing systemic steroid side effects.",
                "organ_clearance_cutoffs": "Avoid strong CYP3A4 inhibitors (grapefruit juice, ketoconazole) which increase budesonide bioavailability."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AGA-COLLAGENOUS",
                "pmid_or_doi": "10.1053/j.gastro.2015.11.008",
                "cebm_level": 1,
                "sample_size": 1200,
                "endpoints": "Oral budesonide induces complete clinical remission in 88% of patients with collagenous colitis."
            }
        }
    },
    {
        "id": "DOC-CARD-450",
        "icd10": "K52.832",
        "condition": "Microscopic Colitis: Lymphocytic Colitis (Intraepithelial Lymphocytes)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: UEG/EMCG Microscopic Colitis Guidelines",
        "source_body": "United European Gastroenterology Journal",
        "citation": "Miehlke S et al. European Guidelines on Microscopic Colitis: United European Gastroenterology and European Microscopic Colitis Group. United European Gastroenterol J. 2021;9(1):13-37.",
        "doi_or_source": "10.1177/2050640620982229",
        "clinical_evidence": "Unlike collagenous colitis which features a thick collagen band, Lymphocytic Colitis is characterized by marked intraepithelial lymphocytosis (>=20 lymphocytes per 100 surface epithelial cells) with normal collagen thickness. Presents with identical severe watery diarrhea and normal endoscopic appearance. ORAL BUDESONIDE (9 mg/day) achieves clinical response in >85%; high overlap with Celiac Disease (serological screening mandatory).",
        "solution_protocol": {
            "non_pharmacological_targets": "Mandatory screening for Celiac Disease with anti-tTG IgA serology; elimination of triggering drugs (NSAIDs, PPIs, SSRIs, checkpoint inhibitors); maintenance budesonide at lowest effective dose (3-6 mg/day) if relapses occur.",
            "monitoring_cadence": "Diarrhea symptom tracking (target <3 stools/day and no watery stools); annual assessment for celiac disease and autoimmune thyroiditis.",
            "clinical_thresholds": ">=20 intraepithelial lymphocytes (IELs) per 100 surface epithelial cells on colon biopsy with normal subepithelial collagen band (<10 micrometers)."
        },
        "patient_plain_language": "Similar to collagenous colitis, lymphocytic colitis causes persistent, watery diarrhea with completely normal-looking bowel lining during a colonoscopy. Under the microscope, large armies of immune lymphocytes crowd between your intestinal cells. Taking gut-targeted Budesonide capsules clears the immune cells, and testing for celiac disease is mandatory.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my colon biopsies show more than 20 intraepithelial lymphocytes per 100 cells without a collagen band?",
            "safety_question": "Has my blood been tested for Celiac disease (tissue transglutaminase IgA antibody)?",
            "action_threshold_question": "What is my tapering schedule for Budesonide capsules once my watery diarrhea resolves?"
        },
        "red_flags": [
            "Nocturnal fecal incontinence and severe dehydration with electrolyte imbalance (hypokalemia)",
            "New-onset bloody stools (indicates alternative diagnosis such as IBD or ischemic colitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Lymphocytic colitis is an immune condition where white blood cells crowd into the colon lining, causing watery diarrhea.",
                "plain_analogy": "A peaceful park lawn overrun by thousands of unexpected protestors, trampling the grass and disrupting drainage.",
                "lifestyle_action": "Take Budesonide daily, get tested for gluten intolerance (celiac disease), and eliminate trigger medications."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Budesonide oral (9 mg daily - Gold Standard)",
                    "Loperamide oral (Imodium - for mild symptoms)",
                    "Bile Acid Sequestrants (Cholestyramine)",
                    "Immunomodulators (Azathioprine / 6-MP)"
                ],
                "dosing_gdmt": "Budesonide 9 mg once daily x 6-8 weeks; maintenance dose 3-6 mg daily for recurrent flares.",
                "black_box_warning": "Discontinue budesonide slowly over weeks to avoid rapid disease rebound.",
                "organ_clearance_cutoffs": "Dose adjustments for hepatic impairment; monitor for adrenal insufficiency upon cessation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "UEG-LYMPHOCYTIC",
                "pmid_or_doi": "10.1177/2050640620982229",
                "cebm_level": 1,
                "sample_size": 1350,
                "endpoints": "Budesonide 9 mg daily achieves clinical response in 86% of patients with lymphocytic colitis."
            }
        }
    },
    {
        "id": "DOC-CARD-451",
        "icd10": "K86.81",
        "condition": "Exocrine Pancreatic Insufficiency (EPI - Severe Steatorrhea)",
        "specialty": "Gastroenterology & Pancreatology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline on Chronic Pancreatitis & EPI",
        "source_body": "American Journal of Gastroenterology",
        "citation": "Gardner TB et al. ACG Clinical Guideline: Chronic Pancreatitis. Am J Gastroenterol. 2020;115(3):322-339.",
        "doi_or_source": "10.14309/ajg.0000000000000535",
        "clinical_evidence": "EPI results from destruction of >90% of pancreatic acinar tissue (chronic pancreatitis, cystic fibrosis, pancreatic resection), causing maldigestion of fats and fat-soluble vitamins (A, D, E, K). Fecal Elastase-1 (<100 mcg/g stool) confirms severe EPI. PANCREATIC ENZYME REPLACEMENT THERAPY (PERT: minimum 40,000-50,000 USP lipase units per full meal) taken DURING meals normalizes fat absorption and halts debilitating weight loss.",
        "solution_protocol": {
            "non_pharmacological_targets": "Take PERT capsules DURING meals and snacks (halfway through eating, not before or after); do NOT restrict dietary fat (fat provides essential calories; enzymes digest it); abstain completely from alcohol and tobacco; fat-soluble vitamin supplements.",
            "monitoring_cadence": "Fecal elastase-1 (FEC); annual fat-soluble vitamin panel (serum 25-OH Vitamin D, Vitamin A, Vitamin E, PT/INR); DXA bone mineral density every 2 years.",
            "clinical_thresholds": "Fecal Elastase-1 <200 mcg/g stool (moderate EPI) or <100 mcg/g stool (severe EPI) with foul-smelling, bulky, floating, oily stools (steatorrhea)."
        },
        "patient_plain_language": "Your pancreas has lost its ability to manufacture digestive enzymes (lipase, protease, amylase). Because dietary fats cannot be digested, they pass straight through into your stool, causing pale, greasy, foul-smelling stools that float and stick to the toilet bowl, along with weight loss. Taking natural pancreatic enzyme capsules with every meal restores normal digestion.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my fecal elastase-1 test below 100 mcg/g confirming severe pancreatic enzyme deficiency?",
            "safety_question": "Am I taking at least 40,000 to 50,000 lipase units of enzyme capsules with every full meal, swallowed DURING the meal?",
            "action_threshold_question": "Have my blood levels of fat-soluble vitamins (A, D, E, and K) and bone density been checked?"
        },
        "red_flags": [
            "Rapid severe weight loss with profound muscle wasting and fat-soluble vitamin deficiencies (osteomalacia, night blindness)",
            "Stools that leave an oily orange or yellow film floating on the toilet water"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "EPI is the inability of the pancreas to make digestive enzymes, causing greasy diarrhea and weight loss.",
                "plain_analogy": "A detergent dispenser in a dishwasher that runs completely empty, leaving plates coated in greasy food film.",
                "lifestyle_action": "Take your enzyme capsules with the first bites of every meal and snack, eat healthy fats, and never skip enzymes."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pancrelipase (Creon / Zenpep / Pancreaze - Enteric-Coated)",
                    "Proton Pump Inhibitors (adjunct to prevent gastric acid degradation)",
                    "Fat-Soluble Vitamins (A, D, E, K)"
                ],
                "dosing_gdmt": "Creon 40,000-50,000 USP lipase units with main meals, 20,000-25,000 with snacks; swallow whole with water.",
                "black_box_warning": "Do NOT crush or chew enteric-coated microspheres (inactivates enzymes and causes severe mouth ulcers).",
                "organ_clearance_cutoffs": "Excessive doses (>10,000 units lipase/kg/day) carry risk of fibrosing colonopathy in children with cystic fibrosis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-EPI-PANCREAS",
                "pmid_or_doi": "10.14309/ajg.0000000000000535",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "Adequate PERT dosing eliminates steatorrhea, halts weight loss, and normalizes fat-soluble vitamin levels in >85% of EPI."
            }
        }
    },
    {
        "id": "DOC-CARD-452",
        "icd10": "K86.0",
        "condition": "Chronic Calcific Pancreatitis (Intractable Pain & Duct Stones)",
        "specialty": "Gastroenterology & Pancreatology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: HaPanEU European Guidelines on Chronic Pancreatitis",
        "source_body": "United European Gastroenterology Journal",
        "citation": "Dominguez-Munoz JE et al. Recommendations from the United European Gastroenterology Evidence-Based Guidelines for Chronic Pancreatitis (HaPanEU). United European Gastroenterol J. 2018;6(2):143-160.",
        "doi_or_source": "10.1177/2050640618768007",
        "clinical_evidence": "Chronic irreversible inflammation causes acinar atrophy, periductal fibrosis, and intraductal calcified stones, resulting in debilitating abdominal pain, EPI, and pancreatogenic diabetes (Type 3c). Extracorporeal Shock Wave Lithotripsy (ESWL) combined with ERCP stone extraction and stenting relieves ductal hypertension; surgical drainage (Frey or Puestow procedure) provides superior long-term pain relief over endoscopy for large duct disease.",
        "solution_protocol": {
            "non_pharmacological_targets": "COMPLETE AND ABSOLUTE ABSTINENCE FROM ALCOHOL AND TOBACCO (smoking accelerates calcification and increases pancreatic adenocarcinoma risk 10-fold); small frequent low-fat meals; non-opioid multimodal analgesia (pregabalin/gabapentin).",
            "monitoring_cadence": "Pancreatic protocol CT or MRI/MRCP (showing main pancreatic duct dilatation >5 mm with intraductal calculi and parenchymal atrophy); annual screening for Type 3c diabetes (HbA1c and fasting glucose).",
            "clinical_thresholds": "Presence of coarse parenchymal or intraductal calcifications on CT with Cambridge Grade 3-4 ductal changes on MRCP."
        },
        "patient_plain_language": "Permanent, irreversible scarring and calcium stones form inside the drainage ducts of your pancreas (most often from heavy alcohol use, smoking, or genetics). The blocked ducts build up extreme pressure, causing severe, boring abdominal pain that shoots straight through to your back. Quitting smoking and alcohol is mandatory, and shock-wave therapy or surgery can remove the stones to relieve the pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did CT imaging show calcified stones blocking my main pancreatic duct, and is the duct widened?",
            "safety_question": "Am I a candidate for shock-wave lithotripsy (ESWL) or surgical duct drainage (Puestow procedure) to relieve pain?",
            "action_threshold_question": "Am I being monitored for Pancreatogenic Type 3c Diabetes, which requires careful insulin management?"
        },
        "red_flags": [
            "Severe persistent epigastric pain boring through to the back requiring escalating opioid doses",
            "Sudden development of painless jaundice or weight loss (Pancreatic Adenocarcinoma surveillance)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Chronic pancreatitis is permanent scarring and stone formation in the pancreas causing chronic pain.",
                "plain_analogy": "A clogged concrete drainage trough filled with hardened gravel, causing water pressure to back up and crack the foundation.",
                "lifestyle_action": "Abstain 100% from alcohol and tobacco, eat small meals, and consult pancreatobiliary surgery for duct clearance."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pancreatic Enzyme Replacement (Creon)",
                    "Pregabalin / Gabapentin (Neuropathic Pain)",
                    "ESWL + Endoscopic Pancreatic Stenting",
                    "Surgical Drainage (Frey / Puestow Procedure)"
                ],
                "dosing_gdmt": "Creon 50,000 units with meals; Pregabalin 75-150 mg BID; ESWL to pulverize intraductal stones.",
                "black_box_warning": "Avoid long-term opioid monotherapy (high risk of opioid-induced hyperalgesia and addiction).",
                "organ_clearance_cutoffs": "Renal adjustments for pregabalin/gabapentin."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HAPANEU-CP",
                "pmid_or_doi": "10.1177/2050640618768007",
                "cebm_level": 1,
                "sample_size": 2600,
                "endpoints": "Surgical drainage (Frey/Puestow) provides durable pain relief in >75% of patients with obstructive chronic pancreatitis."
            }
        }
    },
    {
        "id": "DOC-CARD-453",
        "icd10": "I82.0",
        "condition": "Budd-Chiari Syndrome (Hepatic Venous Outflow Obstruction)",
        "specialty": "Hepatology & Interventional Radiology",
        "organ_system": "Circulatory & Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EASL Clinical Practice Guidelines on Vascular Diseases of the Liver",
        "source_body": "Journal of Hepatology",
        "citation": "European Association for the Study of the Liver. EASL Clinical Practice Guidelines: Vascular Diseases of the Liver. J Hepatol. 2016;64(1):179-202.",
        "doi_or_source": "10.1016/j.jhep.2015.09.004",
        "clinical_evidence": "Thrombosis or obstruction of the hepatic veins or suprahepatic IVC leads to extreme hepatic sinusoidal congestion, ischemic centrilobular necrosis, and acute liver failure or cirrhosis. Over 80% of patients have an underlying myeloproliferative neoplasm (JAK2 V617F mutation). STEPWISE MANAGEMENT STRATEGY: 1) Lifelong therapeutic anticoagulation; 2) Angioplasty/stenting for short stenosis; 3) Early TIPS (Transjugular Intrahepatic Portosystemic Shunt) if medical failure, yielding >85% 5-year survival.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate therapeutic anticoagulation (low-molecular-weight heparin transitioned to DOAC or warfarin); complete screening for thrombophilia and JAK2 V617F mutation (bone marrow biopsy if indicated); sodium restriction and loop diuretics for ascites.",
            "monitoring_cadence": "Doppler ultrasound of hepatic veins and IVC (showing absent or reversed flow, spiderweb collaterals); serial liver function tests, creatinine, and ascites volume; TIPS Doppler patency surveillance every 6 months.",
            "clinical_thresholds": "Partial or complete obstruction of hepatic venous outflow in the absence of right heart failure or constrictive pericarditis."
        },
        "patient_plain_language": "A rare and dangerous blood clot forms in the main drainage veins leaving your liver (hepatic veins). Because blood can enter the liver through arteries but cannot drain out, the liver swells with trapped blood like an over-filled water balloon, causing rapid abdominal fluid buildup (ascites), liver pain, and liver failure. Immediate blood thinners and an internal vein bypass stent (TIPS) save the liver.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did Doppler ultrasound or CT angiogram confirm clot blockage in my hepatic drainage veins?",
            "safety_question": "Have I been tested for the JAK2 genetic blood mutation or underlying clotting disorders?",
            "action_threshold_question": "Is early TIPS stent bypass scheduled to relieve the trapped blood pressure inside my liver?"
        },
        "red_flags": [
            "Rapid massive accumulation of tense abdominal ascites with severe right upper quadrant pain and jaundice",
            "Sudden lethargy, confusion, or flapping tremor indicating acute hepatic encephalopathy and liver failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Budd-Chiari syndrome is a blood clot blocking the veins that drain blood out of the liver.",
                "plain_analogy": "The main drainpipe under a sink suddenly freezing shut with a thick ice plug while the faucet is still running.",
                "lifestyle_action": "Take therapeutic blood thinners faithfully, restrict salt, and undergo specialized TIPS stent placement if needed."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Therapeutic Anticoagulation (Heparin / DOAC / Warfarin - Lifelong)",
                    "TIPS (Transjugular Intrahepatic Portosystemic Shunt)",
                    "Percutaneous Balloon Angioplasty / Stenting",
                    "Furosemide + Spironolactone (for ascites)"
                ],
                "dosing_gdmt": "Therapeutic LMWH (Enoxaparin 1 mg/kg q12h) transitioned to Warfarin (INR 2.0-3.0) or DOAC; TIPS for non-responders.",
                "black_box_warning": "Anticoagulation ALONE fails in >75% of symptomatic patients; early TIPS is critical to prevent irreversible cirrhosis.",
                "organ_clearance_cutoffs": "Monitor for post-TIPS hepatic encephalopathy and shunt stenosis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EASL-BUDD-CHIARI",
                "pmid_or_doi": "10.1016/j.jhep.2015.09.004",
                "cebm_level": 1,
                "sample_size": 1100,
                "endpoints": "Stepwise strategy including early TIPS achieves >85% 5-year overall survival in Budd-Chiari syndrome."
            }
        }
    },
    {
        "id": "DOC-CARD-454",
        "icd10": "K65.2",
        "condition": "Spontaneous Bacterial Peritonitis (SBP - Ascitic PMN >=250/mcL)",
        "specialty": "Hepatology & Gastroenterology",
        "organ_system": "Digestive & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidance on Ascites & SBP",
        "source_body": "Hepatology",
        "citation": "Biggins SW et al. Diagnosis, Evaluation, and Management of Ascites, Spontaneous Bacterial Peritonitis and Hepatorenal Syndrome: 2021 Practice Guidance. Hepatology. 2021;74(2):1014-1048.",
        "doi_or_source": "10.1002/hep.31884",
        "clinical_evidence": "SBP is an acute bacterial infection of ascitic fluid without an evident intra-abdominal surgical source. Diagnostic paracentesis is MANDATORY in any cirrhotic patient hospitalized with ascites. Ascitic Polymorphonuclear (PMN) count >=250 cells/mcL mandates immediate empiric IV Ceftriaxone (2 g/day x 5 days) COMBINED WITH INTRAVENOUS ALBUMIN (1.5 g/kg at diagnosis, followed by 1.0 g/kg on day 3), which reduces hepatorenal syndrome from 33% to 10% and mortality from 29% to 10% (p=0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Diagnostic paracentesis BEFORE starting antibiotics; IV albumin infusion protocol; lifelong secondary antibiotic prophylaxis (daily oral Ciprofloxacin or Bactrim) upon SBP resolution; sodium restriction.",
            "monitoring_cadence": "Ascitic fluid analysis (cell count with differential, albumin, protein, culture in blood culture bottles at bedside); serum creatinine and BUN daily; repeat paracentesis at 48 hours if no clinical improvement.",
            "clinical_thresholds": "Ascitic fluid absolute neutrophil count (total WBC x % neutrophils) >=250 cells/mcL confirms SBP."
        },
        "patient_plain_language": "A severe, life-threatening bacterial infection that develops spontaneously inside the fluid pool in your belly (ascites) in patients with liver cirrhosis. It may cause mild fever, abdominal discomfort, or simply sudden confusion. Tapping the belly fluid with a thin needle (paracentesis) is urgent; treatment requires IV antibiotics plus human albumin protein infusions to protect your kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the fluid tap show an absolute neutrophil count of 250 or higher in my belly fluid?",
            "safety_question": "Has intravenous Albumin protein been infused (1.5 grams/kg today and 1.0 gram/kg on day 3) to prevent kidney failure?",
            "action_threshold_question": "Which daily preventive antibiotic pill (such as Ciprofloxacin or Bactrim) will I take long-term to prevent SBP from returning?"
        },
        "red_flags": [
            "Sudden confusion, drowsiness, or personality change (Hepatic Encephalopathy triggered by SBP)",
            "Rapid drop in urine output with rising blood creatinine (Hepatorenal Syndrome AKI)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "SBP is a dangerous bacterial infection of fluid in the abdomen in patients with advanced liver disease.",
                "plain_analogy": "A garden water barrel that has turned murky and infected with bacteria, threatening to poison the pump attached to it.",
                "lifestyle_action": "Never ignore fever or abdominal pain with liver cirrhosis; seek emergency paracentesis and IV albumin."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ceftriaxone IV (2 g daily x 5 days)",
                    "Intravenous Albumin (1.5 g/kg Day 1, 1.0 g/kg Day 3 - MANDATORY)",
                    "Secondary Prophylaxis (Ciprofloxacin 500 mg daily or TMP-SMX DS daily)"
                ],
                "dosing_gdmt": "Ceftriaxone 2 g IV q24h x 5 days; Albumin 1.5 g/kg IV within 6 hours of diagnosis, then 1.0 g/kg on day 3.",
                "black_box_warning": "Failing to give IV Albumin with antibiotics triples the risk of fatal hepatorenal syndrome and renal failure.",
                "organ_clearance_cutoffs": "Dose adjust prophylactic antibiotics based on renal function."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-SBP-ALBUMIN",
                "pmid_or_doi": "10.1002/hep.31884",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Adding IV Albumin to third-generation cephalosporins reduces hepatorenal syndrome from 33% to 10% and mortality by 66% (p=0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-455",
        "icd10": "K76.7",
        "condition": "Hepatorenal Syndrome (HRS-AKI - Refractory Vasoplegia)",
        "specialty": "Hepatology & Nephrology",
        "organ_system": "Urinary & Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CONFIRM Landmark Trial & AASLD Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Wong F et al. Terlipressin plus Albumin for the Treatment of Type 1 Hepatorenal Syndrome (CONFIRM). N Engl J Med. 2021;384(9):818-827.",
        "doi_or_source": "10.1056/NEJMoa2008290",
        "clinical_evidence": "HRS-AKI is functional renal failure in advanced cirrhosis driven by extreme splanchnic arterial vasodilation and renal vasoconstriction, occurring without structural parenchymal kidney damage. In the phase 3 CONFIRM trial (n=300), TERLIPRESSIN (IV bolus or continuous infusion) COMBINED WITH IV ALBUMIN achieved significantly higher verified HRS reversal (32% vs 17%; p=0.006) and lowered dialysis dependence compared to placebo.",
        "solution_protocol": {
            "non_pharmacological_targets": "HOLD ALL DIURETICS (spironolactone, furosemide) and vasodilators; volume challenge with 20-25% IV Albumin (1 g/kg/day for 2 consecutive days, max 100 g/day); evaluate urgently for Liver Transplantation (definitive curative treatment).",
            "monitoring_cadence": "Continuous pulse oximetry (Terlipressin carries risk of serious respiratory failure and ischemic events); serum creatinine every 12-24 hours; urine output tracking via Foley catheter.",
            "clinical_thresholds": "Diagnosis of cirrhosis with ascites, acute kidney injury (creatinine rise >=0.3 mg/dL within 48h or >=50% baseline), NO response after 2 consecutive days of diuretic withdrawal and IV albumin resuscitation, and absence of shock or nephrotoxic drugs."
        },
        "patient_plain_language": "A severe complication of advanced liver disease where your kidneys shut down, not because the kidneys themselves are diseased, but because extreme dilation of belly blood vessels starves the kidneys of blood pressure. Stopping all water pills and infusing a specialized vasoconstrictor drug (Terlipressin) with concentrated Albumin protein forces blood back into the kidneys while waiting for a liver transplant.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have all water pills (diuretics) and blood pressure medicines been completely stopped?",
            "safety_question": "Did two days of IV Albumin fluid challenge fail to improve my kidney numbers, confirming true Hepatorenal Syndrome?",
            "action_threshold_question": "Is IV Terlipressin being administered with albumin to constrict belly vessels and restore blood flow to my kidneys?"
        },
        "red_flags": [
            "Sudden drop in oxygen saturation (<90%) during Terlipressin therapy (indicates fatal pulmonary edema risk)",
            "Complete cessation of urine output (Anuria) with blood creatinine climbing >3-4 mg/dL"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hepatorenal syndrome is kidney failure caused by severe circulatory changes in advanced liver disease.",
                "plain_analogy": "A city water system where all side hydrants are wide open, leaving zero water pressure to reach the municipal filtration plant.",
                "lifestyle_action": "Requires immediate intensive hospital care with Terlipressin and albumin infusions, and urgent liver transplant listing."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Terlipressin IV (Vasopressin V1a Agonist)",
                    "Intravenous 20-25% Albumin (20-40 g/day maintenance)",
                    "Norepinephrine IV + Albumin (ICU alternative)",
                    "Liver Transplantation (Definitive Cure)"
                ],
                "dosing_gdmt": "Terlipressin 0.85-1.0 mg IV q6h (or continuous infusion 2-4 mg/day) titrated to max 2 mg q6h; plus Albumin 20-40 g/day.",
                "black_box_warning": "BLACK BOX WARNING: Terlipressin can cause fatal respiratory failure and ischemic complications; contraindicated in severe hypoxemia (SpO2 <90%).",
                "organ_clearance_cutoffs": "Stop terlipressin if serum creatinine returns to baseline or if severe ischemic events/pulmonary edema occur."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CONFIRM-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2008290",
                "cebm_level": 2,
                "sample_size": 300,
                "endpoints": "Terlipressin plus albumin achieves verified reversal of Hepatorenal Syndrome in 32% vs 17% with placebo (p=0.006)."
            }
        }
    },
    {
        "id": "DOC-CARD-456",
        "icd10": "K72.90",
        "condition": "Hepatic Encephalopathy (West Haven Neuropsychiatric Staging)",
        "specialty": "Hepatology & Critical Care",
        "organ_system": "Digestive & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD/EASL Practice Guideline on Hepatic Encephalopathy",
        "source_body": "Hepatology",
        "citation": "Vilstrup H et al. Hepatic Encephalopathy in Chronic Liver Disease: 2014 Practice Guideline by AASLD and EASL. Hepatology. 2014;60(2):715-735.",
        "doi_or_source": "10.1002/hep.27210",
        "clinical_evidence": "Impaired hepatic clearance and portosystemic shunting allow neurotoxins (ammonia) to cross the blood-brain barrier, causing astrocyte swelling and cognitive impairment. NON-ABSORBABLE DISACCHARIDE LACTULOSE (titrated to achieve 2-3 soft bowel movements daily) is first-line therapy. RIFAXIMIN (550 mg BID; non-absorbable rifamycin antibiotic) added to lactulose reduces recurrence by 58% (p<0.001) and hospitalizations by 50%. PROTEIN RESTRICTION IS STRICTLY HARMFUL.",
        "solution_protocol": {
            "non_pharmacological_targets": "AVOID DIETARY PROTEIN RESTRICTION (outdated and harmful; cirrhotic patients require 1.2-1.5 g/kg/day of protein to prevent muscle wasting, which worsens ammonia clearance); identify precipitating factors (constipation, GI bleed, infection, hypokalemia, sedatives); fall precautions.",
            "monitoring_cadence": "West Haven criteria staging (Grade 1 euphoria/anxiety to Grade 4 coma); number of bowel movements per day (target 2-3); venous ammonia levels have POOR correlation with severity (do NOT dose lactulose to ammonia levels).",
            "clinical_thresholds": "Presence of asterixis (flapping tremor of outstretched hands), inverted sleep-wake cycle, and cognitive slowing in a patient with cirrhosis."
        },
        "patient_plain_language": "When the liver is severely scarred or bypassed by shunts, it cannot filter ammonia and digestive toxins produced by gut bacteria. These toxins reach your brain, causing sleepiness during the day, insomnia at night, confusion, and a flapping hand tremor (asterixis). Taking Lactulose syrup (to produce 2 to 3 soft bowel movements a day) and Rifaximin pills flushes the toxins out through your intestines.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was the specific trigger that caused this confusion episode (such as an infection, constipation, or dehydration)?",
            "safety_question": "Am I taking enough Lactulose syrup to produce exactly 2 to 3 soft bowel movements every day?",
            "action_threshold_question": "Why is cutting protein from my diet dangerous and harmful for my liver and muscle health?"
        },
        "red_flags": [
            "Sudden deep unresponsiveness or coma (West Haven Grade 4 - requires ICU airway protection)",
            "Flapping tremor of hands (Asterixis) with complete disorientation to time and place"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hepatic encephalopathy is brain fog and confusion caused by toxins that a damaged liver cannot filter.",
                "plain_analogy": "A home air filtration system whose carbon filter has expired, letting smoke and fumes circulate into the bedrooms.",
                "lifestyle_action": "Take your Lactulose syrup every day to maintain 2-3 soft stools, take Rifaximin, and eat adequate protein."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lactulose oral/enema (First Line Non-absorbable Disaccharide)",
                    "Rifaximin oral (Xifaxan 550 mg BID - Class I Add-on)",
                    "Branched-Chain Amino Acids (BCAA)",
                    "Polyethylene Glycol (PEG 3350)"
                ],
                "dosing_gdmt": "Lactulose 20-30 g (30-45 mL) orally 2-4 times daily titrated to 2-3 soft bowel movements/day; Rifaximin 550 mg BID.",
                "black_box_warning": "Over-titration of lactulose causes severe diarrhea, hypernatremic dehydration, and prerenal acute kidney injury.",
                "organ_clearance_cutoffs": "Rifaximin is minimally absorbed (<0.4%); no dosage adjustment required in renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD-HE-GUIDELINE",
                "pmid_or_doi": "10.1002/hep.27210",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "Adding Rifaximin to lactulose cuts hepatic encephalopathy hospital readmissions by 50% and maintains remission in >78%."
            }
        }
    },
    {
        "id": "DOC-CARD-457",
        "icd10": "K20.0",
        "condition": "Eosinophilic Esophagitis (EoE - Trachealization & Food Impaction)",
        "specialty": "Gastroenterology & Allergy",
        "organ_system": "Digestive & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: LIBERTY EoE TREET Trial & AGA/JTF Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Dellon ES et al. Dupilumab in Adults and Adolescents with Eosinophilic Esophagitis (LIBERTY EoE TREET). N Engl J Med. 2022;387(25):2317-2330.",
        "doi_or_source": "10.1056/NEJMoa2205982",
        "clinical_evidence": "EoE is a chronic Th2-mediated allergic inflammation of the esophagus characterized by mucosal eosinophilia (>=15 eosinophils per high-power field). In the pivotal phase 3 LIBERTY EoE TREET trial (n=321), subcutaneous DUPILUMAB (300 mg weekly) achieved histological remission (<6 eosinophils/HPF) in 60% vs 5% placebo (p<0.001) and significantly improved Dysphagia Symptom Questionnaire scores. Swallowed topical fluticasone/budesonide or 6-food elimination diet (6FED) are alternative first-line therapies.",
        "solution_protocol": {
            "non_pharmacological_targets": "Chew food thoroughly; drink water between bites; 6-food elimination diet (eliminate milk, wheat, egg, soy, nuts, seafood) with gradual reintroduction; avoid eating dry meats or dense bread without liquids.",
            "monitoring_cadence": "Upper endoscopy with esophageal biopsies (minimum 6 biopsies from proximal and distal esophagus); EREFS endoscopic score (Edema, Rings/trachealization, Exudates, Furrows, Strictures).",
            "clinical_thresholds": ">=15 intraepithelial eosinophils per high-power field (HPF) on esophageal biopsy after ruling out secondary causes of eosinophilia."
        },
        "patient_plain_language": "An allergic inflammation inside your swallowing tube (esophagus) triggered by common foods (most often cow's milk and wheat). Allergy cells (eosinophils) pack into the tissue, making the tube stiff, narrow, and ribbed like a vacuum cleaner hose (trachealization). Food—especially steak, dry chicken, or dense bread—suddenly gets stuck midway down your chest, causing a terrifying choking blockage.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my esophageal biopsies show more than 15 eosinophils per high-power field?",
            "safety_question": "Am I a candidate for weekly Dupilumab biologic injections (Dupixent) or swallowed topical steroid slurry?",
            "action_threshold_question": "Have we tried eliminating dairy and wheat from my diet to identify the food allergy trigger?"
        },
        "red_flags": [
            "Complete food impaction where meat is stuck and you cannot swallow your own saliva (Emergency Endoscopy needed)",
            "Severe chest pain during swallowing after food gets stuck (indicates esophageal tear or perforation)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "EoE is an allergic condition where immune cells inflame and stiffen the esophagus, causing food to get stuck.",
                "plain_analogy": "A smooth slide that becomes rough and ribbed like washboard gravel, causing sliders to get stuck halfway down.",
                "lifestyle_action": "Chew food into fine pieces, drink plenty of water with meals, and discuss Dupilumab or swallowed steroids."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Dupilumab SubQ (Dupixent 300 mg weekly - FDA Approved)",
                    "Swallowed Topical Fluticasone / Budesonide Slurry",
                    "Proton Pump Inhibitors (Omeprazole 20-40 mg BID)",
                    "Endoscopic Esophageal Dilation"
                ],
                "dosing_gdmt": "Dupilumab 300 mg SC once weekly; or Budesonide 1-2 mg swallowed oral slurry BID (mix with sucralose).",
                "black_box_warning": "Swallowed topical steroids can cause esophageal candidiasis (thrush in 10-15%); rinse mouth without swallowing water.",
                "organ_clearance_cutoffs": "Do NOT drink or eat for 30 minutes after swallowing topical steroid slurry."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "LIBERTY-EOE-TREET",
                "pmid_or_doi": "10.1056/NEJMoa2205982",
                "cebm_level": 2,
                "sample_size": 321,
                "endpoints": "Dupilumab weekly achieves histological remission in 60% and significantly reduces swallowing difficulty (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-458",
        "icd10": "K21.01",
        "condition": "Severe Erosive Reflux Esophagitis (Los Angeles Grade C/D)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG GERD Clinical Practice Guideline",
        "source_body": "American Journal of Gastroenterology",
        "citation": "Katz PO et al. ACG Clinical Guideline for the Diagnosis and Management of Gastroesophageal Reflux Disease. Am J Gastroenterol. 2022;117(1):27-56.",
        "doi_or_source": "10.14309/ajg.0000000000001538",
        "clinical_evidence": "Severe erosive esophagitis (LA Grade C with confluent mucosal breaks >5 mm across folds, or LA Grade D involving >=75% of circumference) carries high risk for peptic stricture, severe ulcer bleeding, and Barrett's metaplasia. HIGH-DOSE PROTON PUMP INHIBITOR (PPI BID x 8-12 weeks) is mandatory, achieving mucosal healing in >85-90%. REPEAT SURVEILLANCE ENDOSCOPY AT 8-12 WEEKS IS MANDATORY to verify complete mucosal healing and rule out occult Barrett's esophagus or dysplasia.",
        "solution_protocol": {
            "non_pharmacological_targets": "Elevate head of bed 6-8 inches; avoid eating within 3 hours of reclining; weight loss in overweight individuals; tobacco and alcohol cessation; avoid chocolate, peppermint, and trigger acidic foods.",
            "monitoring_cadence": "Surveillance upper endoscopy at 8-12 weeks post-intensive PPI therapy; screening for Barrett's esophagus; high-resolution manometry and 24-hour pH-impedance if considering anti-reflux surgery.",
            "clinical_thresholds": "Los Angeles Classification Grade C (continuous mucosal breaks between >=2 mucosal folds, involving <75% of circumference) or Grade D (breaks involving >=75% of circumference)."
        },
        "patient_plain_language": "Stomach acid and bile splash backward into your lower esophagus with such harsh intensity that they burn deep, raw, bleeding ulcers across the delicate pink lining. It causes agonizing burning in your chest (heartburn), pain when swallowing, and can heal into tight scars (strictures) or precancerous changes (Barrett's). Taking strong acid-blocking medicine twice daily for 2 to 3 months is necessary to allow the ulcers to heal.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my reflux categorized as severe Los Angeles Grade C or Grade D on my endoscopy report?",
            "safety_question": "Am I taking my Proton Pump Inhibitor 30 to 60 minutes BEFORE breakfast and dinner for maximum acid suppression?",
            "action_threshold_question": "Is my follow-up endoscopy scheduled in 8 to 12 weeks to confirm that the raw ulcers have healed and check for Barrett's?"
        },
        "red_flags": [
            "Food sticking in the mid-chest when swallowing (indicates fibrous peptic stricture requiring dilation)",
            "Vomiting coffee-ground material or passing pitch-black tarry stools (ulcer hemorrhage)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Severe erosive esophagitis is deep ulceration and chemical burns in the swallowing tube caused by stomach acid.",
                "plain_analogy": "Battery acid splashing out of a car battery onto bare metal, eating away raw trenches and causing rust.",
                "lifestyle_action": "Take your acid-reducing pill twice daily before meals, elevate the head of your bed, and get a follow-up scope."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Proton Pump Inhibitors (Esomeprazole / Rabeprazole / Omeprazole BID)",
                    "Potassium-Competitive Acid Blockers (Vonoprazan)",
                    "Sucralfate oral suspension",
                    "Laparoscopic Nissen Fundoplication / TIF"
                ],
                "dosing_gdmt": "Esomeprazole 40 mg orally twice daily (30-60 min before meals) x 8-12 weeks; Vonoprazan 20 mg daily.",
                "black_box_warning": "LA Grade C and D esophagitis MANDATE long-term maintenance PPI therapy to prevent stricture recurrence.",
                "organ_clearance_cutoffs": "Monitor magnesium and vitamin B12 levels during long-term high-dose PPI therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-GERD-GUIDELINE",
                "pmid_or_doi": "10.14309/ajg.0000000000001538",
                "cebm_level": 1,
                "sample_size": 3500,
                "endpoints": "High-dose PPI therapy achieves complete mucosal healing in 90% of severe erosive esophagitis within 8 weeks."
            }
        }
    },
    {
        "id": "DOC-CARD-459",
        "icd10": "K31.811",
        "condition": "Gastric Antral Vascular Ectasia (GAVE - 'Watermelon Stomach')",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASGE Guideline on Endoscopic Therapy for GAVE",
        "source_body": "Gastrointestinal Endoscopy",
        "citation": "Chavez-Tapia NC et al. Endoscopic Management of Gastric Antral Vascular Ectasia. Gastrointest Endosc. 2018;87(4):943-952.",
        "doi_or_source": "10.1016/j.gie.2017.11.025",
        "clinical_evidence": "GAVE presents with longitudinal red stripes radiating from the pylorus ('watermelon stomach') or diffuse punctate spots, consisting of ectatic mucosal capillaries with fibrin thrombi. Highly associated with systemic sclerosis (scleroderma) and cirrhosis. Unlike portal hypertensive gastropathy, GAVE DOES NOT RESPOND TO PORTAL PRESSURE LOWERING (TIPS OR BETA-BLOCKERS ARE INEFFECTIVE). ENDOSCOPIC ARGON PLASMA COAGULATION (APC) or Radiofrequency Ablation (RFA) is the primary therapy, eliminating transfusion dependence in >75%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Repeated endoscopic ablation sessions (APC or RFA) spaced 4-6 weeks apart until complete obliteration of ectasias; oral or IV iron replacement; blood transfusion support as needed; avoid NSAIDs and anticoagulants.",
            "monitoring_cadence": "Serial complete blood count (CBC measuring hemoglobin and MCV); upper endoscopy every 4-6 weeks during treatment phase, then every 6-12 months for surveillance.",
            "clinical_thresholds": "Characteristic endoscopic appearance of parallel red columns radiating from the pylorus ('watermelon stripes') or diffuse 'honeycomb' antral ectasias."
        },
        "patient_plain_language": "The tiny microscopic blood vessels inside the lower part of your stomach (antrum) become enlarged, fragile, and twisted, forming distinctive red stripes that look like the stripes on a watermelon rind ('Watermelon Stomach'). These fragile vessels constantly ooze microscopic amounts of blood into your stomach, leading to severe chronic anemia and fatigue. Burning the vessels closed with a gentle beam of argon gas during an endoscopy stops the bleeding.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my endoscopy show the classic 'watermelon stomach' stripes or diffuse honeycombed red spots in my lower stomach?",
            "safety_question": "Why did my doctor explain that liver pressure pills (beta-blockers) and TIPS bypass do not work for GAVE?",
            "action_threshold_question": "How many sessions of Argon Plasma Coagulation (APC) laser burning will I need to stop my anemia?"
        },
        "red_flags": [
            "Sudden drop in hemoglobin causing extreme shortness of breath, dizziness, and fainting",
            "Passing black, foul-smelling stools (melena) indicating an active acute bleed"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "GAVE (watermelon stomach) is enlarged, fragile blood vessels in the stomach that look like watermelon stripes and cause anemia.",
                "plain_analogy": "Worn, thin brake pads that continuously rub against the metal wheel drum, leaving red rust dust everywhere.",
                "lifestyle_action": "Attend all scheduled endoscopy laser sessions, take prescribed iron supplements, and never take ibuprofen."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Argon Plasma Coagulation (APC - First Line Endoscopic)",
                    "Radiofrequency Ablation (RFA - Barrx)",
                    "Intravenous Iron Infusions (Ferric Carboxymaltose)",
                    "Endoscopic Band Ligation (EBL)"
                ],
                "dosing_gdmt": "APC delivered at 30-40 watts, argon gas flow 1.0-1.5 L/min; repeat sessions every 4-6 weeks until cleared.",
                "black_box_warning": "GAVE does NOT respond to portal hypotensive therapy (beta-blockers or TIPS have zero efficacy and add toxicity).",
                "organ_clearance_cutoffs": "Check iron saturation and ferritin; administer IV iron for iron-deficiency anemia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASGE-GAVE",
                "pmid_or_doi": "10.1016/j.gie.2017.11.025",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "Endoscopic APC/RFA eliminates transfusion dependence in 78% of patients with GAVE within 3-4 sessions."
            }
        }
    },
    {
        "id": "DOC-CARD-460",
        "icd10": "K31.82",
        "condition": "Dieulafoy's Lesion (Submucosal Caliber-Persistent Arterial Bleed)",
        "specialty": "Gastroenterology & Emergency Medicine",
        "organ_system": "Digestive & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASGE Guideline on Non-Variceal Upper GI Bleeding",
        "source_body": "Gastrointestinal Endoscopy",
        "citation": "Barkun AN et al. Management of Nonvariceal Upper Gastrointestinal Bleeding: Guideline Recommendations From the International Consensus Group. Ann Intern Med. 2019;171(11):805-822.",
        "doi_or_source": "10.7326/M19-1795",
        "clinical_evidence": "A Dieulafoy lesion is a developmental vascular anomaly consisting of an abnormally large, tortuous, caliber-persistent submucosal artery (1-3 mm diameter) that erodes through overlying mucosa without prior ulceration, typically on the gastric lesser curvature (within 6 cm of GE junction). Presents with massive, recurrent, life-threatening hematemesis. ENDOSCOPIC MECHANICAL THERAPY (HEMOCLIP APPLICATION OR ENDOSCOPIC BAND LIGATION) achieves >90-95% primary hemostasis and superior re-bleeding prevention compared to injection monotherapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate hemodynamic resuscitation with IV crystalloids and packed red blood cells; continuous high-dose IV proton pump inhibitor infusion; strict avoidance of NSAIDs, antiplatelets, and anticoagulants until vessel is secured.",
            "monitoring_cadence": "Continuous vital sign monitoring in ICU; repeat endoscopy at 24 hours if rebleeding suspected; transcatheter arterial embolization (TAE) readiness if endoscopic therapy fails.",
            "clinical_thresholds": "Endoscopic visualization of an isolated, minute mucosal defect (<2-5 mm) with arterial spurting, non-bleeding pumping vessel, or adherent clot, surrounded by entirely normal mucosa."
        },
        "patient_plain_language": "A surprisingly dangerous, abnormally thick artery running just beneath the surface of your stomach wall. Because it is unusually large and does not narrow down into tiny capillaries like normal vessels, even tiny friction can cause it to wear through the stomach lining. It bursts like a tiny punctured garden hose, causing sudden, massive vomiting of bright red blood. Putting microscopic metal clips or tight rubber bands on the artery during endoscopy seals it shut permanently.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the endoscopy team find and seal the single pumping artery with endoscopic metal clips or rubber bands?",
            "safety_question": "Has my stomach been examined thoroughly to ensure there are no surrounding ulcers or other abnormal vessels?",
            "action_threshold_question": "If the metal clips cannot stop the bleeding, is interventional radiology ready to perform catheter coil embolization?"
        },
        "red_flags": [
            "Sudden massive vomiting of bright red blood or large dark clots with dizziness and blood pressure collapse",
            "Severe lightheadedness, pale sweaty skin, and fainting upon standing"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dieulafoy's lesion is a large, abnormally positioned artery in the stomach wall that suddenly ruptures and bleeds heavily.",
                "plain_analogy": "A buried underground water main pipe sticking too close to the lawn surface, getting nicked and spurting a geyser.",
                "lifestyle_action": "Seek immediate 911 emergency medical care for vomiting blood; endoscopic clipping stops the artery permanently."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Endoscopic Hemoclip Placement (First Line Mechanical)",
                    "Endoscopic Band Ligation (EBL)",
                    "Transcatheter Arterial Embolization (TAE - Interventional Radiology)",
                    "High-Dose IV PPI (Pantoprazole 80 mg bolus + 8 mg/h)"
                ],
                "dosing_gdmt": "Endoscopic placement of 2-4 mechanical hemoclips directly across the vessel; Pantoprazole 80 mg IV then 8 mg/h x 72h.",
                "black_box_warning": "Epinephrine injection monotherapy is INADEQUATE and carries unacceptable 35% rebleeding rate; MUST combine with mechanical clip.",
                "organ_clearance_cutoffs": "Zero permanent medical contraindications once vessel is clipped; adjust anticoagulants."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DIEULAFOY-HEMOSTASIS",
                "pmid_or_doi": "10.7326/M19-1795",
                "cebm_level": 1,
                "sample_size": 1650,
                "endpoints": "Mechanical endoscopic clipping achieves primary hemostasis in 96% of Dieulafoy lesions with <5% rebleed rate."
            }
        }
    }
]
