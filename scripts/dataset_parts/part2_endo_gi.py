"""
part2_endo_gi.py
"""

PART_2_DISEASES = [
    {
        "id": "DOC-CARD-121",
        "icd10": "E27.1",
        "condition": "Primary Adrenal Insufficiency (Addison's Disease)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "J Clin Endocrinol Metab",
        "citation": "Bornstein SR et al. Diagnosis and Treatment of Primary Adrenal Insufficiency: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2016;101(2):364-389.",
        "doi_or_source": "10.1210/jc.2015-1710",
        "clinical_evidence": "Primary adrenal insufficiency results from autoimmune destruction of the adrenal cortex (80-90% of cases in developed nations), leading to deficient glucocorticoid, mineralocorticoid, and adrenal androgen production. Standard confirmation requires cosyntropin (synthetic ACTH 250 mcg) stimulation test yielding peak serum cortisol < 18 mcg/dL (500 nmol/L) at 30 or 60 min with elevated plasma ACTH (>2x ULN). Maintenance therapy requires hydrocortisone (15-25 mg/day divided 2-3 doses) plus fludrocortisone (0.05-0.2 mg/day). Patient education on emergency 'sick-day rules' (doubling/tripling oral doses) and injectable hydrocortisone (100 mg IM) prevents fatal adrenal crises.",
        "solution_protocol": {
            "non_pharmacological_targets": "Always wear medical alert jewelry; maintain unrestricted sodium intake; carry intramuscular emergency hydrocortisone kit at all times.",
            "monitoring_cadence": "Annual clinical review assessing blood pressure, postural vitals, serum sodium, potassium, and plasma renin activity; annual screening for autoimmune thyroiditis.",
            "clinical_thresholds": "Peak cortisol < 18 mcg/dL on 250 mcg ACTH stimulation establishes adrenal insufficiency; elevated plasma renin guides fludrocortisone titration."
        },
        "patient_plain_language": "Addison's disease is like having an empty battery in your body's stress hormone factory. Your adrenal glands cannot make cortisol, the vital hormone that keeps your blood pressure stable, manages energy, and protects you during illness.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my plasma renin activity and blood potassium level to see if my fludrocortisone dose needs adjustment?",
            "safety_question": "Do I have an active prescription for an emergency 100 mg hydrocortisone intramuscular injection vial and does my family know how to give it?",
            "action_threshold_question": "When I develop a fever, vomiting, or stomach flu, exactly how many times should I double my hydrocortisone pills?"
        },
        "red_flags": [
            "Severe persistent vomiting, sudden profound hypotension (systolic BP < 90), extreme lethargy, hypothermia, or sudden vascular collapse (Adrenal Crisis Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-122",
        "icd10": "E24.9",
        "condition": "Cushing's Syndrome (Hypercortisolism)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "J Clin Endocrinol Metab",
        "citation": "Nieman LK et al. The Diagnosis of Cushing's Syndrome: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2008;93(5):1526-1540.",
        "doi_or_source": "10.1210/jc.2008-0125",
        "clinical_evidence": "Endogenous hypercortisolism causes central obesity, proximal muscle weakness, wide violaceous striae (>1 cm), facial plethora, osteopenia, and severe neuropsychiatric symptoms. Diagnosis requires at least two concordant first-line screening tests: 24-hour urinary free cortisol (UFC >3x ULN), late-night salivary cortisol (>145 ng/dL on 2 separate evenings), or overnight 1-mg dexamethasone suppression test (serum cortisol > 1.8 mcg/dL at 8 AM). Cushing disease (ACTH-secreting pituitary adenoma, 70%) is treated with transsphenoidal adenomectomy; adrenal adenomas require laparoscopic adrenalectomy. Steroidogenesis inhibitors (ketoconazole, metyrapone, osilodrostat) serve as bridge or adjuvant medical therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction (<2,000 mg/day) to manage cortisol-mediated hypertension; high-protein diet to counter catabolic muscle wasting; falls prevention for fragile bones.",
            "monitoring_cadence": "Post-surgical morning serum cortisol checking on postoperative days 1-3 to confirm remission (<2 mcg/dL indicates cure); periodic DEXA scans.",
            "clinical_thresholds": "Post-dexamethasone cortisol > 1.8 mcg/dL indicates lack of physiological suppression."
        },
        "patient_plain_language": "Cushing's syndrome is like your body's stress alarm getting permanently stuck in the 'ON' position. An excess of cortisol hormone leads to sudden weight gain around your waist and face, muscle weakness in your thighs, easy bruising, and high blood pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were the exact results of my 24-hour urine cortisol or late-night salivary cortisol tests?",
            "safety_question": "If I undergo pituitary surgery, will I need temporary replacement hydrocortisone tablets to avoid sudden adrenal withdrawal?",
            "action_threshold_question": "Should we order a dedicated pituitary MRI or adrenal CT scan based on my blood ACTH levels?"
        },
        "red_flags": [
            "Sudden severe lower extremity pain and swelling (high DVT/PE risk from hypercoagulability), acute mania/psychosis, or severe opportunistic fungal infections"
        ]
    },
    {
        "id": "DOC-CARD-123",
        "icd10": "E21.0",
        "condition": "Primary Hyperparathyroidism",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Workshop Consensus Guidelines",
        "source_body": "J Bone Miner Res",
        "citation": "Bilezikian JP et al. Evaluation and Management of Primary Hyperparathyroidism: Summary Statement and Guidelines from the Fifth International Workshop. J Bone Miner Res. 2022;37(11):2293-2314.",
        "doi_or_source": "10.1002/jbmr.4677",
        "clinical_evidence": "Primary hyperparathyroidism (PHPT) is characterized by hypercalcemia driven by autonomously elevated or inappropriately normal intact parathyroid hormone (PTH), primarily caused by a single benign parathyroid adenoma (85%). Classic clinical manifestations include nephrolithiasis, cortical bone resorption (osteoporosis at the distal 1/3 radius), constipation, and cognitive impairment. Parathyroidectomy provides definitive surgical cure with >95% success. Surgical criteria for asymptomatic patients include: serum calcium > 1.0 mg/dL above normal ULN, T-score ≤ -2.5 at lumbar spine, hip, or 1/3 radius, age < 50 years, eGFR < 60 mL/min, or 24-hour urinary calcium > 250 mg (women) / 300 mg (men).",
        "solution_protocol": {
            "non_pharmacological_targets": "Adequate daily oral hydration (2-3 liters water daily) to reduce calcium nephrolithiasis risk; maintain moderate dietary calcium intake (1,000 mg/day; calcium restriction triggers higher PTH output); avoid thiazide diuretics and lithium.",
            "monitoring_cadence": "Annual serum calcium, albumin, creatinine, and eGFR; DEXA bone mineral density every 1-2 years.",
            "clinical_thresholds": "Serum calcium > 1.0 mg/dL above ULN or T-score ≤ -2.5 at forearm/spine/hip meets surgical indication."
        },
        "patient_plain_language": "Primary hyperparathyroidism occurs when one of the four tiny rice-sized glands behind your thyroid produces too much parathyroid hormone. This hormone strips calcium from your bones and dumps it into your bloodstream, weakening bones and forming kidney stones.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my ionized calcium, intact PTH, and 24-hour urinary calcium excretion?",
            "safety_question": "Am I currently taking any medications like hydrochlorothiazide that artificially elevate calcium levels?",
            "action_threshold_question": "Based on my bone density DEXA scan and age, do I meet criteria for curative parathyroid adenoma surgery?"
        },
        "red_flags": [
            "Severe hypercalcemic crisis (calcium > 14 mg/dL) presenting with lethargy, intractable nausea, confusion, cardiac arrhythmias, or coma"
        ]
    },
    {
        "id": "DOC-CARD-124",
        "icd10": "E20.9",
        "condition": "Hypoparathyroidism",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Society of Endocrinology Clinical Guideline",
        "source_body": "Eur J Endocrinol",
        "citation": "Bollerslev J et al. European Society of Endocrinology Clinical Guideline: Treatment of chronic hypoparathyroidism in adults. Eur J Endocrinol. 2015;173(2):G1-G20.",
        "doi_or_source": "10.1530/EJE-15-0628",
        "clinical_evidence": "Hypoparathyroidism results in hypocalcemia, hyperphosphatemia, and hypercalciuria due to absent or inadequate PTH secretion (most commonly iatrogenic after total thyroidectomy or neck dissection). Neuromuscular irritability manifests as perioral numbness, paresthesias, Chvostek's/Trousseau's signs, carpopedal spasms, and laryngospasm. Standard therapy relies on oral calcium carbonate/citrate (1,000-3,000 mg/day elemental) combined with active vitamin D metabolites (calcitriol 0.25-2.0 mcg/day). The therapeutic objective is maintaining serum albumin-adjusted calcium in the low-normal range (8.0-8.5 mg/dL) while avoiding hypercalciuria (24-hr urine calcium < 300 mg/day) to prevent nephrocalcinosis and renal failure.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary phosphate restriction (limit processed colas, preserved cheeses); split calcium supplement dosing across 3-4 meals to maximize gut absorption.",
            "monitoring_cadence": "Serum calcium, albumin, phosphorus, and magnesium every 3-6 months; annual 24-hour urinary calcium and renal ultrasound.",
            "clinical_thresholds": "Target corrected calcium 8.0-8.5 mg/dL; keep calcium-phosphate product < 55 mg²/dL² to avoid ectopic tissue calcification."
        },
        "patient_plain_language": "Hypoparathyroidism is a shortage of parathyroid hormone, usually after neck or thyroid surgery. Without this hormone, calcium levels in your blood drop dangerously low, causing tingling in your fingertips and lips, painful muscle cramps, and tremors.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current corrected blood calcium and phosphorus level?",
            "safety_question": "Is my calcitriol and calcium dose keeping my 24-hour urine calcium low enough to protect my kidneys from stone formation?",
            "action_threshold_question": "At what degree of finger numbness or muscle twitching should I take an extra rescue calcium tablet or seek emergency care?"
        },
        "red_flags": [
            "Severe painful muscle tetany, carpopedal spasm, laryngeal stridor (throat closing), or new generalized seizures (Severe Hypocalcemia Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-125",
        "icd10": "E78.01",
        "condition": "Familial Hypercholesterolemia (HeFH)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Atherosclerosis Society Consensus Statement",
        "source_body": "Eur Heart J",
        "citation": "Cuchel M et al. 2023 Update on European Atherosclerosis Society Consensus Statement on Familial Hypercholesterolaemia: new treatments and clinical guidance. Eur Heart J. 2023;44(25):2277-2291.",
        "doi_or_source": "10.1093/eurheartj/ehad224",
        "clinical_evidence": "Heterozygous familial hypercholesterolemia (HeFH) is a dominant monogenic disorder (prevalence ~1:250) caused by mutations in LDLR, APOB, or PCSK9, leading to lifelong severe LDL-C elevation (>190 mg/dL in adults) and a >10-fold increased lifetime risk of premature coronary artery disease. Dutch Lipid Clinic Network criteria score clinical history, tendon xanthomas, and LDL-C levels. First-line therapy mandates high-intensity statin therapy (atorvastatin 80 mg or rosuvastatin 40 mg) combined early with ezetimibe 10 mg (adds ~24% reduction), and PCSK9 monoclonal antibodies (evolocumab or alirocumab; adds ~50-60% reduction, FOURIER and ODYSSEY OUTCOMES trials) to achieve LDL-C targets (<55 mg/dL for secondary prevention; <70 mg/dL for primary prevention).",
        "solution_protocol": {
            "non_pharmacological_targets": "Heart-healthy Mediterranean diet low in saturated fats (<7% daily calories) and trans fats; avoidance of smoking; cascade genetic testing for all first-degree relatives.",
            "monitoring_cadence": "Lipid panel every 6-12 weeks until target LDL-C is attained, then every 6-12 months; baseline coronary artery calcium (CAC) scoring or CT coronary angiography.",
            "clinical_thresholds": "LDL-C ≥ 190 mg/dL in untreated adults or ≥ 155 mg/dL in untreated children strongly suggests HeFH; treatment target < 55 mg/dL if established ASCVD."
        },
        "patient_plain_language": "Familial hypercholesterolemia is an inherited gene mutation that prevents your liver from filtering 'bad' LDL cholesterol from your blood. Because cholesterol builds up from childhood, plaque forms in heart arteries decades earlier than normal unless treated with medication.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current LDL cholesterol level on my combination statin and ezetimibe regimen?",
            "safety_question": "Do I qualify for a PCSK9 inhibitor injection to reach my target LDL-C under 55 mg/dL?",
            "action_threshold_question": "How should my children and siblings be screened with genetic testing and lipid panels?"
        },
        "red_flags": [
            "New onset exertional chest tightness, radiating jaw/arm pain, or sudden shortness of breath indicating premature coronary ischemia"
        ]
    },
    {
        "id": "DOC-CARD-126",
        "icd10": "E29.1",
        "condition": "Male Hypogonadism (Testosterone Deficiency)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "J Clin Endocrinol Metab",
        "citation": "Bhasin S et al. Testosterone Therapy in Men With Hypogonadism: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2018;103(5):1715-1744.",
        "doi_or_source": "10.1210/jc.2018-00229",
        "clinical_evidence": "Diagnosis of male hypogonadism requires persistent low morning fasting total testosterone (<300 ng/dL [10.4 nmol/L] on two separate occasions drawn between 8 AM and 10 AM) accompanied by unequivocal signs and symptoms: diminished libido, erectile dysfunction, decreased spontaneous erections, loss of axillary/pubic hair, and osteopenia. Serum LH and FSH differentiate primary (hypergonadotropic, testicular failure) from secondary (hypogonadotropic, hypothalamic-pituitary pathology). The TRAVERSE trial (NEJM 2023) demonstrated noninferiority of testosterone replacement therapy (TRT) regarding major adverse cardiac events in men with confirmed hypogonadism and pre-existing CVD. TRT is contraindicated in active prostate cancer, PSA > 4.0 ng/mL, severe untreated sleep apnea, or baseline hematocrit > 50%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Weight loss (5-10% weight loss increases endogenous testosterone in obese men); progressive resistance strength training; structured management of obstructive sleep apnea.",
            "monitoring_cadence": "Morning total testosterone, hematocrit, and digital rectal exam/PSA at 3, 6, and 12 months after initiating therapy; then annually.",
            "clinical_thresholds": "Target mid-normal morning total testosterone (400-700 ng/dL); withhold or titrate down if hematocrit exceeds 54% to prevent erythrocytosis-induced thrombosis."
        },
        "patient_plain_language": "Male hypogonadism happens when a man's testicles or pituitary gland produce abnormally low levels of testosterone. This can cause persistent fatigue, loss of muscle mass, decreased sex drive, low mood, and thinning bones.",
        "doctor_consultation_checklist": {
            "parameter_question": "Were my two morning fasting testosterone levels both under 300 ng/dL, and what were my LH and FSH levels?",
            "safety_question": "What is my baseline PSA and hematocrit level before starting testosterone therapy?",
            "action_threshold_question": "If I am planning on having children in the near future, should we use hCG or clomiphene instead of testosterone to preserve my fertility?"
        },
        "red_flags": [
            "Hematocrit rising above 54% (high risk of blood clots/stroke), acute urinary retention, or sudden testicular swelling/palpable mass"
        ]
    },
    {
        "id": "DOC-CARD-127",
        "icd10": "E28.2",
        "condition": "Polycystic Ovary Syndrome (PCOS)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Evidence-based Guideline",
        "source_body": "Fertil Steril",
        "citation": "Teede HJ et al. Recommendations from the 2023 international evidence-based guideline for the assessment and management of polycystic ovary syndrome. Fertil Steril. 2023;120(4):767-793.",
        "doi_or_source": "10.1016/j.fertnstert.2023.07.025",
        "clinical_evidence": "Rotterdam diagnostic criteria require 2 out of 3 features: oligo- or anovulation, clinical and/or biochemical signs of hyperandrogenism (Ferriman-Gallwey hirsutism score ≥ 4-6, elevated free/total testosterone), and polycystic ovaries on ultrasound (≥20 follicles per ovary or ovarian volume ≥10 mL), after excluding thyroid disease, hyperprolactinemia, and non-classic congenital adrenal hyperplasia. Insulin resistance drives excess ovarian theca cell androgen production. Combined oral contraceptives (COCs) are first-line for irregular menses and hyperandrogenism; metformin improves insulin sensitivity and metabolic parameters; letrozole is first-line for ovulation induction in infertility (surpassing clomiphene in the PPCOS II trial; NEJM 2014).",
        "solution_protocol": {
            "non_pharmacological_targets": "5-10% body weight reduction restores regular ovulatory cycles in over 50% of overweight patients; low-glycemic index dietary regimen; regular aerobic and resistance exercise.",
            "monitoring_cadence": "Oral glucose tolerance test (OGTT) or HbA1c every 1-3 years; lipid profile every 2 years; regular blood pressure checks; endometrial ultrasound if amenorrhea > 3 months.",
            "clinical_thresholds": "Unscheduled amenorrhea > 90 days requires progestin-induced withdrawal bleed or ultrasound to rule out endometrial hyperplasia."
        },
        "patient_plain_language": "PCOS is a hormonal and metabolic imbalance where ovaries make slightly higher levels of androgen hormones and eggs don't release predictably every month. This causes irregular periods, facial hair growth, acne, and difficulty getting pregnant.",
        "doctor_consultation_checklist": {
            "parameter_question": "What are my fasting glucose, HbA1c, and lipid results to check for insulin resistance?",
            "safety_question": "If my periods come less often than every 3 months, do I need progestin pills to protect my uterine lining from abnormal cell growth?",
            "action_threshold_question": "If I am ready to get pregnant, should we start letrozole as the first-line medication to help me ovulate?"
        },
        "red_flags": [
            "Abnormal heavy uterine bleeding causing acute lightheadedness or anemia, severe pelvic pain with fever, or sudden severe depression/suicidal ideation"
        ]
    },
    {
        "id": "DOC-CARD-128",
        "icd10": "K27.9",
        "condition": "Peptic Ulcer Disease (PUD)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline",
        "source_body": "Am J Gastroenterol",
        "citation": "Chey WD et al. ACG Clinical Guideline: Treatment of Helicobacter pylori Infection. Am J Gastroenterol. 2017;112(2):212-239.",
        "doi_or_source": "10.1038/ajg.2016.563",
        "clinical_evidence": "Peptic ulcer disease involves mucosal breaks ≥ 5 mm in the stomach or duodenum extending into the muscularis propria, primarily driven by Helicobacter pylori infection or nonsteroidal anti-inflammatory drug (NSAID) use. Esophagogastroduodenoscopy (EGD) provides definitive diagnosis and endoscopic Forrest classification for bleeding risk. H. pylori eradication with 14-day bismuth quadruple therapy (PPI + bismuth subcitrate + metronidazole + tetracycline) achieves >85-90% cure rates despite clarithromycin resistance, reducing ulcer recurrence from >60% to <5%. Eradication must be confirmed via urea breath test or stool antigen ≥ 4 weeks post-treatment and ≥ 2 weeks off PPI therapy. NSAID ulcers require PPI therapy and switching to celecoxib or acetaminophen.",
        "solution_protocol": {
            "non_pharmacological_targets": "Complete cessation of tobacco and NSAIDs (ibuprofen, naproxen); avoidance of heavy alcohol ingestion; structured stress reduction.",
            "monitoring_cadence": "Urea breath test or stool antigen test ≥ 4 weeks after antibiotic completion; repeat EGD in 8-12 weeks for gastric ulcers to verify healing and rule out malignancy.",
            "clinical_thresholds": "Active ulcer with visible bleeding vessel (Forrest Ia/Ib/IIa) mandates endoscopic dual therapy (hemoclip + epinephrine) plus high-dose IV PPI infusion for 72 hours."
        },
        "patient_plain_language": "A peptic ulcer is an open sore on the lining of your stomach or upper intestine, most often caused by a stomach bacterium called H. pylori or frequent use of pain relievers like ibuprofen. When the stomach's protective mucus layer breaks down, stomach acid irritates the tissue.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my ulcer tested for H. pylori infection during endoscopy or with a breath test?",
            "safety_question": "Which over-the-counter pain medications can I safely take without irritating my stomach lining?",
            "action_threshold_question": "If I had a gastric ulcer, do I need a repeat endoscopy in 8 to 12 weeks to ensure it has healed completely?"
        },
        "red_flags": [
            "Vomiting coffee-ground material or bright red blood (hematemesis), passing pitch-black tarry stools (melena), or sudden sharp 'board-like' rigid belly pain (perforation)"
        ]
    },
    {
        "id": "DOC-CARD-129",
        "icd10": "B18.1",
        "condition": "Chronic Hepatitis B Infection",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidelines",
        "source_body": "Hepatology",
        "citation": "Terrault NA et al. Update on prevention, diagnosis, and treatment of chronic hepatitis B: AASLD 2018 hepatitis B guidance. Hepatology. 2018;67(4):1560-1599.",
        "doi_or_source": "10.1002/hep.29800",
        "clinical_evidence": "Chronic hepatitis B (persistence of HBsAg > 6 months) causes immune-mediated necroinflammation, progressing to cirrhosis and hepatocellular carcinoma (HCC). Treatment indications depend on serum HBV DNA levels, ALT elevations, and stage of liver fibrosis (transient elastography / FibroScan). Nucleos(t)ide analogues with high genetic barrier to resistance (entecavir 0.5 mg daily, tenofovir disoproxil fumarate [TDF] 300 mg daily, or tenofovir alafenamide [TAF] 25 mg daily) suppress viral replication to undetectable levels in >95% of adherent patients, reversing fibrosis and dramatically reducing HCC incidence. HCC surveillance with abdominal ultrasound ± alpha-fetoprotein (AFP) every 6 months is mandatory for all cirrhotic patients, Asian men >40, Asian women >50, and African Americans >20.",
        "solution_protocol": {
            "non_pharmacological_targets": "Complete abstinence from alcohol; vaccination against Hepatitis A; weight management to avoid concurrent MAFLD/steatohepatitis; family screening for HBsAg and anti-HBs.",
            "monitoring_cadence": "HBV DNA, ALT, and hepatic panel every 3-6 months; abdominal ultrasound ± serum AFP every 6 months for HCC surveillance; renal function and bone density monitoring if on TDF.",
            "clinical_thresholds": "HBV DNA > 2,000 IU/mL with ALT > 2x ULN or significant fibrosis (F2 or greater) mandates antiviral therapy; any cirrhosis with detectable HBV DNA requires immediate treatment."
        },
        "patient_plain_language": "Chronic hepatitis B is a persistent viral infection in your liver. While many people have zero symptoms for years, the virus can quietly damage liver cells over time. Daily antiviral pills can suppress the virus so low that it stops causing harm and prevents liver scarring.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current blood viral load (HBV DNA in IU/mL) and ALT liver enzyme level?",
            "safety_question": "Is it time for my 6-month liver ultrasound and AFP cancer screening test?",
            "action_threshold_question": "Have my immediate household contacts and partner been tested and vaccinated for Hepatitis B?"
        },
        "red_flags": [
            "Yellowing of skin or eyes (jaundice), abdominal fluid swelling (ascites), confusion or sleep cycle reversal (hepatic encephalopathy), or vomiting blood"
        ]
    },
    {
        "id": "DOC-CARD-130",
        "icd10": "K31.84",
        "condition": "Gastroparesis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline",
        "source_body": "Am J Gastroenterol",
        "citation": "Camilleri M et al. Clinical Guideline: Management of Gastroparesis. Am J Gastroenterol. 2022;117(8):1197-1220.",
        "doi_or_source": "10.14309/ajg.0000000000001874",
        "clinical_evidence": "Gastroparesis is a chronic neuromuscular gastric disorder characterized by delayed gastric emptying without mechanical mechanical obstruction, most commonly idiopathic (50%) or diabetic (30%). Gold-standard diagnosis requires 4-hour solid-phase gastric emptying scintigraphy (GES) showing > 10% gastric retention at 4 hours or > 60% at 2 hours. Management begins with dietary modifications (small, frequent, low-fat, low-insoluble-fiber meals). In diabetes, strict glycemic control is paramount because acute hyperglycemia (>200 mg/dL) slows gastric peristalsis. Prokinetic therapy includes metoclopramide (FDA-approved, limited to <12 weeks when possible due to tardive dyskinesia risk) or erythromycin; oral dopamine antagonist domperidone is utilized under special programs. Refractory cases may benefit from gastric peroral endoscopic myotomy (G-POEM).",
        "solution_protocol": {
            "non_pharmacological_targets": "Consume 4-6 small meals daily; choose homogenized, pureed, or liquid nutrients; chew thoroughly; avoid high-fiber foods (oranges, broccoli) that form bezoars; remain upright for 2 hours post-meal.",
            "monitoring_cadence": "Nutritional panel (micronutrients, vitamins D, B12, iron) every 6-12 months; continuous glucose monitoring in diabetic patients; neurological assessment for dyskinesias if on metoclopramide.",
            "clinical_thresholds": "Gastric retention > 10% at 4 hours on standardized solid meal scintigraphy confirms delayed gastric emptying."
        },
        "patient_plain_language": "Gastroparesis, or 'stomach paralysis', means the stomach muscles take far too long to push food into the intestines, even though there is no physical blockage. Food sits in the stomach for hours, leading to early fullness, nausea, bloating, and vomiting.",
        "doctor_consultation_checklist": {
            "parameter_question": "What percentage of food remained in my stomach at hour 4 on my gastric emptying scan?",
            "safety_question": "If I am taking metoclopramide (Reglan), what subtle muscle twitches should I look out for to stop it before permanent side effects occur?",
            "action_threshold_question": "Should I work with a specialized gastrointestinal dietitian to design a blenderized or liquid meal plan to maintain my weight?"
        },
        "red_flags": [
            "Inability to tolerate any liquids for >24 hours, significant involuntary weight loss (>10% body weight), or signs of severe dehydration (dark concentrated urine, postural fainting)"
        ]
    },
    {
        "id": "DOC-CARD-131",
        "icd10": "K22.0",
        "condition": "Achalasia",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline",
        "source_body": "Am J Gastroenterol",
        "citation": "Vaezi MF et al. ACG Clinical Guideline: Diagnosis and Management of Achalasia. Am J Gastroenterol. 2020;115(9):1393-1411.",
        "doi_or_source": "10.14309/ajg.0000000000000731",
        "clinical_evidence": "Achalasia is a primary esophageal motility disorder characterized by loss of myenteric plexus inhibitory ganglion cells, causing incomplete lower esophageal sphincter (LES) relaxation and absent peristalsis. Patients present with progressive dysphagia to both solids and liquids, regurgitation of undigested food, chest pain, and weight loss. High-resolution manometry (HRM) is the gold standard diagnostic tool, categorizing disease via Chicago Classification: Type I (classic), Type II (panesophageal pressurization; >90% treatment response), and Type III (spastic). Diagnosis requires Integrated Relaxation Pressure (IRP > 15 mmHg) and 100% aperistalsis. Definitive therapies disrupt LES smooth muscle: Pneumatic balloon dilation (PD), laparoscopic Heller myotomy (LHM with partial fundoplication), or peroral endoscopic myotomy (POEM; European achalasia trial demonstrated >85-90% success rates at 2-5 years, Eckardt score ≤ 3).",
        "solution_protocol": {
            "non_pharmacological_targets": "Eat slowly; chew food to a liquid consistency; drink warm water with meals; elevate head of bed 30 degrees to prevent nocturnal pulmonary aspiration.",
            "monitoring_cadence": "Eckardt clinical symptom score tracking every 3-6 months post-procedure; timed barium esophagram at 1 year post-treatment; surveillance EGD for late squamous dysplasia in longstanding disease.",
            "clinical_thresholds": "Integrated relaxation pressure (IRP) > 15 mmHg on high-resolution manometry with 100% aperistalsis confirms diagnosis; post-treatment Eckardt score ≤ 3 indicates clinical remission."
        },
        "patient_plain_language": "Achalasia is a condition where the muscular valve at the bottom of your swallowing tube (the esophagus) cannot relax to let food drop into your stomach, and the esophagus loses its ability to squeeze food down. Food and liquids pool in your chest, causing regurgitation.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which specific Chicago classification type (Type I, II, or III) was identified on my high-resolution manometry study?",
            "safety_question": "If I undergo POEM or Heller myotomy, will I need daily acid-suppressing medication to prevent acid reflux afterwards?",
            "action_threshold_question": "What is my current Eckardt symptom score and does my esophageal barium emptying show adequate clearance?"
        },
        "red_flags": [
            "Severe nocturnal coughing choking fits indicating airway aspiration of esophageal contents, progressive severe malnutrition, or sudden food impaction"
        ]
    },
    {
        "id": "DOC-CARD-132",
        "icd10": "K52.839",
        "condition": "Microscopic Colitis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AGA Institute Clinical Practice Guideline",
        "source_body": "Gastroenterology",
        "citation": "Feuerstein JD et al. AGA Clinical Practice Guidelines on the Management of Microscopic Colitis. Gastroenterology. 2016;150(1):242-246.",
        "doi_or_source": "10.1053/j.gastro.2015.11.008",
        "clinical_evidence": "Microscopic colitis encompasses lymphocytic colitis (≥20 intraepithelial lymphocytes per 100 surface epithelial cells) and collagenous colitis (subepithelial collagen band thickness ≥ 10 µm), presenting with chronic, non-bloody, watery diarrhea (often 5-15 bowel movements/day), fecal urgency, nocturnal diarrhea, and fecal incontinence. Macroscopic colonoscopy appearance is typically normal, making systematic mucosal biopsies throughout the ascending, transverse, and descending colon mandatory. First-line medical therapy is oral budesonide (9 mg/day for 6-8 weeks; Cochrane Meta-analysis RR for clinical remission 3.18, 95% CI 2.04-4.97). Discontinuation of potential offending triggers (NSAIDs, PPIs, SSRIs, statins) is recommended. Low-dose budesonide (3-6 mg/day) maintains remission in frequent relapsers.",
        "solution_protocol": {
            "non_pharmacological_targets": "Identify and eliminate dietary triggers (caffeine, artificial sweeteners like sorbitol, dairy if lactase deficient); stop non-essential NSAIDs and PPIs; pelvic floor muscle training for fecal urgency.",
            "monitoring_cadence": "Clinical symptom assessment and stool frequency logs every 4 weeks during induction; electrolytes and renal function if high-volume diarrhea.",
            "clinical_thresholds": "Clinical remission defined as < 3 stools per day and < 1 watery stool per day on a standardized diary."
        },
        "patient_plain_language": "Microscopic colitis is an inflammatory bowel condition where the large intestine looks completely normal to the naked eye during a colonoscopy, but shows inflammation when examined under a microscope. It causes frequent, sudden, watery diarrhea without blood.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my colon biopsies confirm lymphocytic or collagenous microscopic colitis?",
            "safety_question": "Could any of my current daily medications, like omeprazole or ibuprofen, be triggering this bowel inflammation?",
            "action_threshold_question": "How long should I stay on the 9 mg budesonide course, and how will we taper the dose to keep symptoms from returning?"
        },
        "red_flags": [
            "Severe dehydration with postural dizziness, unintentional profound weight loss, or high fevers with severe abdominal cramping"
        ]
    },
    {
        "id": "DOC-CARD-133",
        "icd10": "K75.4",
        "condition": "Autoimmune Hepatitis (AIH)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidance",
        "source_body": "Hepatology",
        "citation": "Mack CL et al. Diagnosis and Management of Autoimmune Hepatitis in Adults and Children: 2019 Practice Guidance and Guidelines From the AASLD. Hepatology. 2020;72(2):696-722.",
        "doi_or_source": "10.1002/hep.31065",
        "clinical_evidence": "Autoimmune hepatitis is a chronic immune-mediated hepatic necroinflammation characterized by hypergammaglobulinemia (elevated IgG), circulating autoantibodies (Type 1: ANA, ASMA; Type 2: anti-LKM1), and interface hepatitis with plasma cell infiltrates on liver biopsy. Untreated, 5-year survival is <50% in severe disease. Standard induction therapy consists of oral prednisone (30-60 mg/day tapered) or budesonide (9 mg/day in non-cirrhotic patients) combined with azathioprine (1-2 mg/kg/day). Thiopurine methyltransferase (TPMT) and NUDT15 genotype/phenotype testing prior to azathioprine initiation prevents life-threatening myelosuppression. Treatment aims for complete biochemical remission (normalization of both serum transaminases and IgG levels), which must be maintained for ≥ 2 years before attempting cautiously supervised withdrawal.",
        "solution_protocol": {
            "non_pharmacological_targets": "Complete abstinence from alcohol; vaccination against hepatitis A and B; baseline DEXA scan and calcium/vitamin D supplementation while on systemic corticosteroids.",
            "monitoring_cadence": "ALT, AST, total bilirubin, and IgG every 2-4 weeks during induction, then every 3 months during maintenance; annual CBC to monitor azathioprine bone marrow toxicity.",
            "clinical_thresholds": "Complete biochemical response requires normalization of AST, ALT, and total serum IgG below upper limit of normal."
        },
        "patient_plain_language": "Autoimmune hepatitis is a condition where your own immune defense system gets confused and attacks your liver cells as if they were invaders. If untreated, this causes chronic inflammation and scarring, but immunosuppressive medications can put the disease into remission.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have my AST, ALT, and IgG levels normalized to confirm my disease is in complete remission?",
            "safety_question": "Was my TPMT enzyme level checked before starting azathioprine to prevent low blood counts?",
            "action_threshold_question": "Are my bones being protected with calcium, vitamin D, and a bone density scan while taking steroid medications?"
        },
        "red_flags": [
            "Development of new jaundice (yellow eyes/skin), fluid accumulation in the abdomen (ascites), easy bruising, or mental confusion (hepatic encephalopathy)"
        ]
    },
    {
        "id": "DOC-CARD-134",
        "icd10": "K74.3",
        "condition": "Primary Biliary Cholangitis (PBC)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD Practice Guidance",
        "source_body": "Hepatology",
        "citation": "Lindor KD et al. Primary Biliary Cholangitis: 2018 Practice Guidance from the AASLD. Hepatology. 2019;69(1):394-419.",
        "doi_or_source": "10.1002/hep.30145",
        "clinical_evidence": "Primary biliary cholangitis is a chronic autoimmune cholestatic liver disease predominantly affecting women (9:1 ratio), characterized by progressive immune destruction of intrahepatic interlobular bile ducts. Hallmark diagnosis requires ≥2 of 3 criteria: sustained elevated alkaline phosphatase (ALP > 1.5x ULN), presence of antimitochondrial antibodies (AMA titer ≥ 1:40, found in >95% of patients), and compatible liver biopsy findings (florid duct lesions). First-line therapy is oral ursodeoxycholic acid (UDCA 13-15 mg/kg/day), which delays disease progression, prolongs transplant-free survival, and normalizes life expectancy in complete biochemical responders (Paris II criteria: ALP and AST ≤ 1.5x ULN with normal bilirubin at 1 year). Incomplete responders are escalated to second-line obeticholic acid or PPAR agonists (bezafibrate/elafibranor).",
        "solution_protocol": {
            "non_pharmacological_targets": "Skin care protocols for chronic pruritus (mild cool baths, emollients); fat-soluble vitamin supplementation (Vitamins A, D, E, K); regular weight-bearing exercise to prevent osteoporosis.",
            "monitoring_cadence": "Alkaline phosphatase, total bilirubin, AST/ALT every 3-6 months; annual fat-soluble vitamin levels (A, D, E, INR); DEXA bone density scan every 2-3 years; HCC screening ultrasound every 6 months if cirrhotic.",
            "clinical_thresholds": "Alkaline phosphatase > 1.67x ULN or elevated total bilirubin after 12 months of UDCA therapy indicates incomplete response and need for second-line therapy."
        },
        "patient_plain_language": "Primary biliary cholangitis is an autoimmune condition where the immune system attacks and damages the tiny drainage tubes (bile ducts) inside your liver. When bile gets trapped, it leaks into the bloodstream, causing deep itching, fatigue, and eventual liver scarring.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current alkaline phosphatase and total bilirubin level on my current UDCA dose?",
            "safety_question": "Am I on the correct weight-based dose of ursodiol (13 to 15 milligrams per kilogram of body weight)?",
            "action_threshold_question": "What effective treatments, such as bile acid binding resins or newer therapies, can help relieve my severe skin itching?"
        },
        "red_flags": [
            "Dark tea-colored urine with pale clay-colored stools, sudden onset jaundice, vomiting blood, or swelling in the legs and abdomen"
        ]
    },
    {
        "id": "DOC-CARD-135",
        "icd10": "K85.90",
        "condition": "Acute Pancreatitis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline",
        "source_body": "Am J Gastroenterol",
        "citation": "Tenner S et al. American College of Gastroenterology Guideline: Management of Acute Pancreatitis. Am J Gastroenterol. 2024;119(3):411-437.",
        "doi_or_source": "10.14309/ajg.0000000000002645",
        "clinical_evidence": "Diagnosis requires at least 2 of 3 Atlanta criteria: characteristic epigastric pain radiating to the back, serum lipase or amylase > 3x the upper limit of normal, and characteristic cross-sectional imaging findings (contrast-enhanced CT or MRI). Gallstones (40-50%) and alcohol (30%) are leading etiologies. Landmark WATERFALL trial (NEJM 2022) demonstrated that aggressive fluid resuscitation significantly increased fluid overload (20.5% vs 6.3%) without improving clinical outcomes compared to moderate resuscitation (Lactated Ringer's 1.5 mL/kg/hr after 10 mL/kg bolus if hypovolemic). Prophylactic antibiotics are strictly not recommended. Early oral refeeding with a low-fat solid or liquid diet as soon as ileus has resolved and pain improves shortens hospital stay and reduces infectious complications.",
        "solution_protocol": {
            "non_pharmacological_targets": "Complete abstinence from alcohol and tobacco; cholecystectomy during index admission for mild biliary pancreatitis to prevent recurrent life-threatening attacks; low-fat dietary intake.",
            "monitoring_cadence": "Frequent vital signs, urine output (>0.5 mL/kg/hr), hematocrit, and blood urea nitrogen (BUN) checks in the first 24-48 hours; repeat ultrasound or MRCP if etiology unclear.",
            "clinical_thresholds": "Rising BUN (>20 mg/dL or any increase at 24 hours) or hematocrit > 44% signals hemoconcentration and increased risk of pancreatic necrosis."
        },
        "patient_plain_language": "Acute pancreatitis is sudden, severe inflammation of the pancreas gland behind your stomach. Digestive enzymes that the pancreas normally sends to your intestines become prematurely active inside the pancreas itself, irritating and digesting its own delicate tissues.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was the identified cause of my pancreatitis (gallstones, high triglycerides, medications, or alcohol)?",
            "safety_question": "If gallstones caused my attack, will my gallbladder be safely removed before I am discharged from the hospital?",
            "action_threshold_question": "When can I safely resume drinking liquids and eating a low-fat diet?"
        },
        "red_flags": [
            "Severe unremitting abdominal pain, difficulty breathing, high fever with chills, low blood pressure, or blueish bruising around the belly button (Cullen's sign)"
        ]
    },
    {
        "id": "DOC-CARD-136",
        "icd10": "K64.9",
        "condition": "Hemorrhoidal Disease and Anal Fissure",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASCRS Clinical Practice Guideline",
        "source_body": "Dis Colon Rectum",
        "citation": "Davis BR et al. The American Society of Colon and Rectal Surgeons Clinical Practice Guidelines for the Management of Hemorrhoids. Dis Colon Rectum. 2018;61(3):284-292.",
        "doi_or_source": "10.1097/DCR.0000000000001030",
        "clinical_evidence": "Hemorrhoids are vascular cushions in the anal canal; enlargement and distal displacement result in bleeding, prolapse, and thrombosis. Internal hemorrhoids present with painless bright red rectal bleeding on toilet paper or in bowl; external hemorrhoids cause hygiene issues or acute severe pain when thrombosed. Anal fissures are longitudinal mucosal tears distal to the dentate line causing sharp knife-like pain during defecation and bright rectal streaks. Cochrane meta-analysis confirms dietary fiber supplementation (25-35 g/day) and water intake reduce bleeding by 50%. First-line medical therapy for chronic fissures is topical calcium channel blockers (diltiazem 2% ointment) or topical nitroglycerin 0.4% ointment for 6-8 weeks (heals 65-75% by relaxing internal anal sphincter hypertonicity). Office procedures (rubber band ligation) treat persistent Grade I-III internal hemorrhoids.",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily dietary fiber intake of 25-35 grams (soluble psyllium supplement); 2 liters water daily; avoid straining or sitting on toilet > 3-5 minutes; warm sitz baths for 10-15 minutes twice daily.",
            "monitoring_cadence": "Clinical reassessment after 6-8 weeks of topical therapy; diagnostic anoscopy/flexible sigmoidoscopy to confirm diagnosis and exclude colorectal malignancy in adults ≥ 45 or those with red flags.",
            "clinical_thresholds": "Acutely thrombosed external hemorrhoid presenting within 72 hours of symptom onset benefits from simple office surgical excision under local anesthesia."
        },
        "patient_plain_language": "Hemorrhoids are swollen, inflamed blood vessel cushions in your lower rectum, while an anal fissure is a small crack or tear in the delicate skin of the anus. Hard stools and straining stretch these tissues, causing bright red bleeding and sharp stinging pain with bowel movements.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my examination show internal hemorrhoids, an external clot, or an anal fissure?",
            "safety_question": "Do I need an anoscopy, sigmoidoscopy, or screening colonoscopy to make sure the bleeding is not from higher in my colon?",
            "action_threshold_question": "Would a prescription diltiazem ointment or a simple office rubber band procedure resolve my symptoms faster?"
        },
        "red_flags": [
            "Large volume maroon or dark bloody stools, stools mixed with blood clots, lightheadedness on standing, or unexplained new bowel habit changes"
        ]
    },
    {
        "id": "DOC-CARD-137",
        "icd10": "K57.32",
        "condition": "Acute Diverticulitis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AGA Clinical Practice Guideline",
        "source_body": "Gastroenterology",
        "citation": "Peery AF et al. American Gastroenterological Association Clinical Practice Update on Medical Management of Colonic Diverticulitis: Expert Review. Gastroenterology. 2021;160(3):906-911.",
        "doi_or_source": "10.1053/j.gastro.2020.09.053",
        "clinical_evidence": "Acute diverticulitis represents inflammation and micro-perforation of a colonic diverticulum, predominantly in the sigmoid and descending colon. Contrast-enhanced abdominal pelvic CT is the imaging gold standard (sensitivity/specificity >95%), differentiating uncomplicated (localized colonic wall thickening and pericolic fat stranding) from complicated disease (abscess, macroperforation/peritonitis, fistula, or stricture). Randomized clinical trials (AVOD and DIABOLO) demonstrated that systemic antibiotics do not improve recovery time, complication rates, or recurrence in immunocompetent patients with mild, uncomplicated diverticulitis, supporting conservative outpatient observation without antibiotics. Colonoscopy is recommended 6-8 weeks post-resolution of complicated or first-episode diverticulitis to rule out misdiagnosed colorectal carcinoma (present in 2-4%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Clear liquid diet for 2-3 days during acute painful phase, advancing to regular diet as tolerated; high-fiber diet long term; avoidance of NSAIDs; regular physical activity.",
            "monitoring_cadence": "Outpatient clinical check at 48-72 hours; diagnostic colonoscopy 6-8 weeks after complete symptom resolution.",
            "clinical_thresholds": "Pelvic abscess ≥ 3-4 cm on CT warrants percutaneous catheter drainage; generalized peritonitis (Hinchey III/IV) requires emergent operative intervention."
        },
        "patient_plain_language": "Diverticulitis occurs when small pouches in your colon wall become inflamed or irritated. This typically causes sharp aching pain in the lower left side of your belly, mild fever, and nausea.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my CT scan show uncomplicated diverticulitis or is there an abscess or perforation?",
            "safety_question": "Based on current guidelines, do I actually require antibiotic pills or will a clear liquid diet and rest allow it to resolve safely?",
            "action_threshold_question": "When should my follow-up colonoscopy be scheduled after this flare-up has completely resolved?"
        },
        "red_flags": [
            "Severe rigid abdominal guarding (hard board-like abdomen), persistent high fevers (>101°F / 38.3°C), intractable vomiting, or dizziness on standing"
        ]
    },
    {
        "id": "DOC-CARD-138",
        "icd10": "K90.89",
        "condition": "Small Intestinal Bacterial Overgrowth (SIBO)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline",
        "source_body": "Am J Gastroenterol",
        "citation": "Pimentel M et al. ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth. Am J Gastroenterol. 2020;115(2):165-178.",
        "doi_or_source": "10.14309/ajg.0000000000000501",
        "clinical_evidence": "SIBO is defined as excessive colonic-type bacterial colonization in the small intestine (≥ 10³ colony-forming units/mL on duodenal aspirate culture), or positive non-invasive breath testing (increase in breath hydrogen ≥ 20 ppm above baseline within 90 minutes or breath methane ≥ 10 ppm at any time [intestinal methanogen overgrowth, IMO] using glucose or lactulose substrate). Patients experience chronic postprandial bloating, flatulence, watery diarrhea, abdominal discomfort, and in severe cases, fat-soluble vitamin malabsorption (A, D, E) and B12 deficiency from bacterial deconjugation of bile acids. Rifaximin (550 mg three times daily for 14 days) is the evidence-based first-line non-absorbable antibiotic, producing symptom response in >60-70% of hydrogen-predominant SIBO. Methane-positive IMO requires dual therapy (rifaximin + neomycin or metronidazole).",
        "solution_protocol": {
            "non_pharmacological_targets": "Temporary low-FODMAP diet to decrease rapidly fermentable oligosaccharides, disaccharides, monosaccharides, and polyols; spacing meals 4-5 hours apart to promote migrating motor complex (MMC) cleansing waves.",
            "monitoring_cadence": "Clinical symptom review at 2-4 weeks post-antibiotic treatment; repeat breath testing only if symptoms fail to resolve or rapidly recur; periodic serum B12 and vitamin D levels.",
            "clinical_thresholds": "Hydrogen rise ≥ 20 ppm within 90 minutes or methane ≥ 10 ppm establishes positive breath test."
        },
        "patient_plain_language": "SIBO occurs when bacteria that normally belong in the large intestine migrate backwards and colonize the small intestine in high numbers. When you eat carbohydrates, these bacteria ferment the food prematurely, creating large amounts of hydrogen or methane gas that cause severe bloating, pain, and diarrhea.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my breath test show excess hydrogen, excess methane gas, or both?",
            "safety_question": "Does my treatment plan include a 14-day course of rifaximin, and will my insurance require prior authorization?",
            "action_threshold_question": "What dietary approach or prokinetic gut medication can prevent the bacteria from regrowing after antibiotics?"
        },
        "red_flags": [
            "Severe unintentional weight loss, oily foul-smelling stools that float (steatorrhea), severe macrocytic anemia, or chronic edema from protein-losing enteropathy"
        ]
    },
    {
        "id": "DOC-CARD-139",
        "icd10": "K22.70",
        "condition": "Barrett's Esophagus",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline",
        "source_body": "Am J Gastroenterol",
        "citation": "Shaheen NJ et al. ACG Clinical Guideline: Diagnosis and Management of Barrett's Esophagus. Am J Gastroenterol. 2022;117(4):559-587.",
        "doi_or_source": "10.14309/ajg.0000000000001680",
        "clinical_evidence": "Barrett's esophagus (BE) is the metaplastic replacement of normal squamous esophageal epithelium by specialized columnar epithelium with goblet cells (intestinal metaplasia), extending ≥ 1 cm proximal to the gastroesophageal junction, resulting from chronic GERD. BE is the sole established precursor to esophageal adenocarcinoma. Screening with high-definition endoscopy is recommended in men with chronic GERD symptoms (>5 years) and ≥2 risk factors (age >50, Caucasian, central obesity, history of smoking, first-degree relative with BE/cancer). All patients require once-daily PPI maintenance therapy. Endoscopic surveillance follows the Seattle biopsy protocol (4-quadrant biopsies every 2 cm): non-dysplastic BE requires repeat EGD every 3-5 years; confirmed low-grade or high-grade dysplasia warrants endoscopic eradication therapy (radiofrequency ablation [RFA] ± endoscopic mucosal resection [EMR]).",
        "solution_protocol": {
            "non_pharmacological_targets": "Smoking cessation; weight loss to decrease intra-abdominal pressure; avoid lying flat within 3 hours of meals; elevate head of bed 6 inches.",
            "monitoring_cadence": "Endoscopic surveillance every 3-5 years for non-dysplastic BE; every 6-12 months for confirmed low-grade dysplasia without ablation; immediate ablation for confirmed high-grade dysplasia.",
            "clinical_thresholds": "Length ≥ 1 cm with histological intestinal metaplasia confirms BE; any dysplasia must be independently confirmed by an expert gastrointestinal pathologist."
        },
        "patient_plain_language": "Barrett's esophagus happens when years of acid reflux irritate the bottom of your swallowing tube. To protect itself from stomach acid, the lining transforms its delicate cells into tougher, intestinal-type cells. Because these changed cells carry a small risk of turning cancerous over time, doctors monitor them with regular cameras.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured length (Prague classification C and M criteria) of my Barrett's segment?",
            "safety_question": "Were my biopsy specimens checked by a dedicated gastrointestinal pathologist to confirm there is no dysplasia (precancerous change)?",
            "action_threshold_question": "When is my next surveillance endoscopy due, and would I benefit from endoscopic radiofrequency ablation?"
        },
        "red_flags": [
            "New or worsening difficulty swallowing food (dysphagia), food sticking in your chest, vomiting blood, or unintended progressive weight loss"
        ]
    },
    {
        "id": "DOC-CARD-140",
        "icd10": "A04.72",
        "condition": "Clostridioides difficile Infection (CDI)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA/SHEA Clinical Practice Guideline",
        "source_body": "Clin Infect Dis",
        "citation": "Johnson S et al. Clinical Practice Guideline by the Infectious Diseases Society of America (IDSA) and Society for Healthcare Epidemiology of America (SHEA): 2021 Focused Update Guidelines on Management of Clostridioides difficile Infection in Adults. Clin Infect Dis. 2021;73(5):e1029-e1044.",
        "doi_or_source": "10.1093/cid/ciab549",
        "clinical_evidence": "C. difficile infection is toxin-mediated colitis typically precipitated by broad-spectrum antibiotic exposure (clindamycin, fluoroquinolones, cephalosporins) disrupting colon microbiota. Diagnosis requires ≥ 3 unformed liquid stools in 24 hours plus laboratory confirmation: multi-step testing with NAAT/PCR and toxin EIA or cell cytotoxicity assay. The 2021 IDSA guidelines designate fidaxomicin (200 mg orally twice daily for 10 days) as the preferred first-line agent over oral vancomycin (125 mg orally four times daily for 10 days), demonstrating sustained clinical cure and significantly lower recurrence rates (15% vs 25%, p=0.005). Metronidazole is no longer recommended for non-severe CDI. Recurrent CDI is treated with tapered vancomycin, fidaxomicin, or fecal microbiota transplantation (FMT / live biotherapeutic products, e.g., fecal microbiota spores, live-brpk / Rebyota / Vowst).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict hand hygiene with soap and water (alcohol-based hand rubs do NOT kill C. diff bacterial spores); contact isolation precautions; immediate discontinuation of inciting broad-spectrum antibiotics.",
            "monitoring_cadence": "Clinical symptom resolution (stool frequency and consistency); follow-up 'test of cure' stool testing is strictly contraindicated because spores persist after cure.",
            "clinical_thresholds": "Severe CDI defined by WBC ≥ 15,000 cells/µL or serum creatinine > 1.5 mg/dL; fulminant CDI defined by hypotension, shock, ileus, or megacolon."
        },
        "patient_plain_language": "C. diff is a stubborn bacterial infection of the colon that takes over when strong antibiotics wipe out your bowel's normal 'friendly' bacteria. C. diff bacteria release toxins that cause severe diarrhea, fever, and intestinal inflammation.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my stool positive for active C. diff toxin and is my infection classified as mild or severe based on my white blood cell count?",
            "safety_question": "Can I receive fidaxomicin instead of vancomycin to give me the lowest chance of the infection coming back?",
            "action_threshold_question": "Should we discontinue my other antibiotics or acid-suppressing heartburn medications to help my gut microbiome heal?"
        },
        "red_flags": [
            "Severe abdominal distention with stopping of bowel movements (toxic megacolon / paralytic ileus), low blood pressure, confusion, or WBC count > 30,000"
        ]
    }
]