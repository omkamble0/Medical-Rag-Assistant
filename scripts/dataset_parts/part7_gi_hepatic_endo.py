"""
part7_gi_hepatic_endo.py
"""

PART_7_DISEASES = [
    {
        "id": "DOC-CARD-221",
        "icd10": "K22.70",
        "condition": "Barrett's Esophagus",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (AIM Dysplasia Trial) & ACG Guidelines",
        "citation": "Shaheen NJ et al. Radiofrequency ablation in Barrett's esophagus with dysplasia (AIM Dysplasia). N Engl J Med. 2009;360(22):2277-2288.",
        "doi_or_source": "10.1056/NEJMoa0808145",
        "clinical_evidence": "In the landmark multicenter sham-controlled AIM Dysplasia trial (n=127 patients with dysplastic Barrett's esophagus), radiofrequency ablation (RFA) resulted in complete eradication of low-grade dysplasia in 90.5% of patients (vs 22.7% sham; p<0.001) and complete eradication of high-grade dysplasia in 81.0% (vs 19.0% sham; p<0.001) at 12 months. RFA was associated with less disease progression (3.6% vs 16.3%; p=0.03) and fewer esophageal adenocarcinomas (1.2% vs 9.3%; p=0.045). Continuous high-dose proton pump inhibitor (PPI) therapy reduces risk of progression to neoplastic dysplasia by 71% (OR 0.29; 95% CI 0.12-0.79).",
        "solution_protocol": {
            "non_pharmacological_targets": "Elevation of head of bed by 6 inches; avoidance of recumbency within 3 hours of meals; cessation of tobacco; weight reduction targeting BMI <25 kg/m2.",
            "monitoring_cadence": "High-definition white light endoscopy with Seattle biopsy protocol (4-quadrant biopsies every 1-2 cm) every 3-5 years for non-dysplastic Barrett's; every 6-12 months for confirmed low-grade dysplasia; endoscopic eradication for high-grade dysplasia.",
            "clinical_thresholds": "Confirmation of low-grade or high-grade dysplasia by an expert gastrointestinal pathologist triggers endoscopic radiofrequency ablation (RFA) or endoscopic mucosal resection (EMR)."
        },
        "patient_plain_language": "Barrett's esophagus is a condition where chronic acid reflux from the stomach damages the lower lining of your food pipe (esophagus). Over years of acid exposure, the normal pale pink esophageal lining changes into a salmon-pink tissue that resembles the lining of your intestines. It requires regular camera checks (endoscopies) because of a small risk of developing cancer.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured length of my Barrett's segment (Prague classification C and M criteria), and were any precancerous cells (dysplasia) found?",
            "safety_question": "Should I be taking my proton pump inhibitor twice a day rather than once daily to maximize acid suppression?",
            "action_threshold_question": "At what point would I be a candidate for endoscopic radiofrequency ablation (heat-treating the precancerous lining)?"
        },
        "red_flags": [
            "Food sticking or getting trapped when swallowing (dysphagia), painful swallowing (odynophagia), vomiting blood, or unexplained rapid weight loss"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Barrett's esophagus is a condition in which the flat pink lining of the swallowing tube that connects the mouth to the stomach becomes damaged by acid reflux.",
                "plain_analogy": "The food pipe lining changing its texture to resemble stomach lining as a calloused shield against acid.",
                "lifestyle_action": "Never lie flat after eating. Raise the head of your bed 6 inches. Avoid late-night snacking and acidic triggers."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Esomeprazole", "Omeprazole", "Pantoprazole", "Dexlansoprazole"],
                "dosing_gdmt": "Omeprazole 20-40 mg daily or Esomeprazole 40 mg daily taken 30-60 minutes prior to the first meal of the day.",
                "black_box_warning": "Long-term PPI use: Increased risk of Clostridioides difficile-associated diarrhea, hypomagnesemia, and bone fractures.",
                "organ_clearance_cutoffs": "Monitor serum magnesium and vitamin B12 annually on continuous long-term PPI therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AIM Dysplasia",
                "pmid_or_doi": "10.1056/NEJMoa0808145",
                "cebm_level": 2,
                "sample_size": 127,
                "endpoints": "Complete eradication of high-grade dysplasia in 81.0% with RFA vs 19.0% sham (p<0.001); cancer progression reduced by 87%."
            }
        }
    },
    {
        "id": "DOC-CARD-222",
        "icd10": "K22.0",
        "condition": "Achalasia",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (POEM vs LHM) & ACG Guidelines",
        "citation": "Werner YB et al. Endoscopic or Surgical Myotomy in Patients with Idiopathic Achalasia (POEM vs LHM). N Engl J Med. 2019;381(23):2219-2229.",
        "doi_or_source": "10.1056/NEJMoa1905380",
        "clinical_evidence": "In the landmark multicenter randomized noninferiority trial (n=221 patients with treatment-naive achalasia followed for 2 years), peroral endoscopic myotomy (POEM) was noninferior to laparoscopic Heller myotomy (LHM) plus Dor fundoplication with respect to clinical treatment success (Eckardt score <=3: 83.0% POEM vs 81.7% LHM; difference 1.4 percentage points; 95% CI -8.7 to 11.4; p=0.007 for noninferiority). Reflux esophagitis was more common after POEM at 2 years (44% vs 29%; p=0.03). High-resolution esophageal manometry (HRM) using the Chicago Classification (Type I, II, III) is the diagnostic gold standard; Type II achieves the highest treatment response (>90%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Chewing food thoroughly into a fine liquid slurry; drinking carbonated or warm water with meals to facilitate gravity-assisted emptying; sleeping with head of bed elevated 30 degrees.",
            "monitoring_cadence": "Post-procedure Eckardt symptom score at 3, 6, 12, and 24 months; timed barium esophagogram (TBE) measuring barium column height at 1, 2, and 5 minutes post-intervention; surveillance endoscopy every 3 years for megaesophagus.",
            "clinical_thresholds": "Integrated relaxation pressure (IRP) >15 mmHg on high-resolution manometry combined with an Eckardt symptom score >3 indicates treatment failure requiring pneumatic dilation or repeat myotomy."
        },
        "patient_plain_language": "Achalasia is a rare swallowing disorder where the nerves in your food pipe (esophagus) become damaged and stop working. The food pipe loses its normal muscular squeezing waves, and the muscular valve at the bottom entrance to the stomach (lower esophageal sphincter) fails to relax and open. Food and liquids get stuck in your chest and back up into your throat.",
        "doctor_consultation_checklist": {
            "parameter_question": "What achalasia subtype (Type I, II, or III) did my high-resolution manometry demonstrate?",
            "safety_question": "Am I a better candidate for peroral endoscopic myotomy (POEM) or laparoscopic surgical Heller myotomy with a partial anti-reflux wrap?",
            "action_threshold_question": "What is my current Eckardt symptom score and what barium column height on timed X-ray indicates successful opening?"
        },
        "red_flags": [
            "Waking up choking or coughing on undigested food (nocturnal regurgitation / aspiration pneumonia), progressive severe weight loss, or food becoming completely impacted"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Achalasia is a rare disorder that makes it hard for foods and liquids to pass into your stomach because the valve at the bottom of the food pipe does not open.",
                "plain_analogy": "A bottleneck muscular gate at the bottom of the food pipe that stays locked shut, causing food traffic jams in the chest.",
                "lifestyle_action": "Eat small, soft meals slowly with plenty of warm liquids. Never eat within 4 hours of sleeping."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Botulinum Toxin Type A (Endoscopic)", "Isosorbide Dinitrate", "Nifedipine", "Pantoprazole"],
                "dosing_gdmt": "Definitive: POEM or Heller myotomy. Medical bridge for poor surgical candidates: Nifedipine 10-20 mg sublingual 30 min before meals or Botox 100 units.",
                "black_box_warning": "Botulinum toxin: Potential distant spread of toxin causing swallowing and breathing difficulties.",
                "organ_clearance_cutoffs": "Monitor for post-myotomy GERD; maintenance PPI (Pantoprazole 40 mg daily) recommended for post-POEM esophagitis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POEM vs LHM",
                "pmid_or_doi": "10.1056/NEJMoa1905380",
                "cebm_level": 2,
                "sample_size": 221,
                "endpoints": "POEM noninferior to Heller myotomy for 2-year clinical success (Eckardt score <=3: 83.0% vs 81.7%; p=0.007); reflux esophagitis 44% vs 29%."
            }
        }
    },
    {
        "id": "DOC-CARD-223",
        "icd10": "K20.0",
        "condition": "Eosinophilic Esophagitis (EoE)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (Dupilumab EoE Trial) & ACG/AGA Guidelines",
        "citation": "Dellon ES et al. Dupilumab in Adults and Adolescents with Eosinophilic Esophagitis. N Engl J Med. 2022;387(25):2317-2330.",
        "doi_or_source": "10.1056/NEJMoa2205982",
        "clinical_evidence": "In the landmark 3-part multicenter Phase 3 trial (n=321 patients aged >=12 with active EoE despite high-dose PPI therapy), subcutaneous dupilumab (300 mg weekly) achieved histologic remission (<=6 eosinophils per high-power field [HPF]) in 60% of patients compared to only 5% with placebo in Part A (p<0.001) and 59% vs 6% in Part B (p<0.001). Dupilumab significantly improved dysphagia symptom scores (-21.9 vs -9.6 points; p<0.001) and increased esophageal distensibility while reducing endoscopic visual scores (trachealization rings, furrows, exudates, and strictures). Swallowed topical fluticasone or budesonide suspension achieves histologic remission in 65-75% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Empiric food elimination diets (6-food elimination diet: milk, wheat, egg, soy, nuts, seafood; or stepped 2-food diet: dairy and gluten); eating slowly with copious sips of water; avoiding dry meats without sauce.",
            "monitoring_cadence": "Follow-up esophagogastroduodenoscopy (EGD) with at least 6 biopsies (distal and proximal esophagus) 8-12 weeks after initiating or altering medical or dietary therapy.",
            "clinical_thresholds": "Peak mucosal eosinophil count >=15 eosinophils/HPF on esophageal biopsy establishes diagnosis; esophageal luminal diameter <13 mm with food impactions warrants gentle serial endoscopic balloon dilation."
        },
        "patient_plain_language": "Eosinophilic esophagitis (EoE) is an allergic inflammatory condition of your food pipe (esophagus). Certain foods you eat trigger specialized allergy white blood cells called eosinophils to gather in the lining of your esophagus. This causes the lining to swell, develop stiff circular rings, and narrow down, making dense foods like chicken, steak, or bread catch and feel stuck in your chest.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was the highest eosinophil count per high-power field on my latest esophageal biopsies?",
            "safety_question": "Would I benefit more from a targeted food elimination diet, swallowed topical asthma steroids, or the biologic injection dupilumab?",
            "action_threshold_question": "What emergency steps should I take if a piece of food becomes completely stuck and I cannot swallow my own saliva?"
        },
        "red_flags": [
            "Complete inability to swallow saliva (acute esophageal food bolus impaction requiring emergent endoscopic removal), severe chest pain, or vomiting blood"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Eosinophilic esophagitis is a chronic, allergic inflammatory disease of the esophagus that causes difficulty swallowing and food impaction.",
                "plain_analogy": "An allergic asthma-like reaction occurring inside the food pipe, causing it to swell and narrow so solid foods get stuck.",
                "lifestyle_action": "Chew food into fine paste. Drink water with every bite. Trial eliminating dairy and wheat from your diet."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Dupilumab Subcutaneous", "Budesonide Oral Suspension (Jorveza)", "Fluticasone Propionate (Swallowed)", "Omeprazole"],
                "dosing_gdmt": "Dupilumab 300 mg subcutaneous injection once weekly. Or Budesonide 1-2 mg mixed with sucralose/honey swallowed twice daily.",
                "black_box_warning": "Dupilumab: Monitor for conjunctivitis, keratitis, and eosinophilic pneumonia; avoid abrupt cessation of systemic steroids.",
                "organ_clearance_cutoffs": "No dose adjustment required for renal or mild hepatic impairment; rinse mouth after swallowed steroids to prevent oral thrush."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "LIBERTY-EoE",
                "pmid_or_doi": "10.1056/NEJMoa2205982",
                "cebm_level": 2,
                "sample_size": 321,
                "endpoints": "Histologic remission (<=6 eos/HPF) achieved in 60% with dupilumab vs 5% placebo (p<0.001); Dysphagia Symptom Questionnaire improved significantly."
            }
        }
    },
    {
        "id": "DOC-CARD-224",
        "icd10": "K31.84",
        "condition": "Gastroparesis (Diabetic & Idiopathic)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Evidence Synthesis",
        "source_body": "American College of Gastroenterology (ACG) Guidelines",
        "citation": "Camilleri M et al. Clinical Guideline: Management of Gastroparesis. Am J Gastroenterol. 2022;117(8):1197-1226.",
        "doi_or_source": "10.14309/ajg.0000000000001874",
        "clinical_evidence": "The ACG Gastroparesis Guidelines establish standardized 4-hour solid-phase gastric emptying scintigraphy (GES) with a low-fat egg meal as the diagnostic standard. Gastric retention >10% at 4 hours (or >60% at 2 hours) confirms delayed gastric emptying in the absence of mechanical obstruction. In diabetic gastroparesis, optimizing glycemic control (targeting HbA1c <7.0%) is critical, as acute hyperglycemia (>200 mg/dL) directly inhibits antral contractions. Metoclopramide remains the only FDA-approved oral prokinetic medication, but therapy must be limited to <12 weeks due to risk of tardive dyskinesia.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary modification: 5-6 small-volume meals daily; low-fiber (<2-3 g/meal to prevent bezoar formation); low-fat (<40 g/day); caloric fluids (soups, shakes); walking for 15-30 minutes post-prandially.",
            "monitoring_cadence": "Quarterly Gastroparesis Cardinal Symptom Index (GCSI) score tracking; baseline and monthly neurological screen for extrapyramidal symptoms (AIMS scale) while on metoclopramide.",
            "clinical_thresholds": "Gastric retention >35% at 4 hours classifies as severe gastroparesis; intractable vomiting resulting in dehydration, weight loss >10%, or electrolyte derangements warrants gastric electrical stimulation or G-POEM."
        },
        "patient_plain_language": "Gastroparesis is a condition where the muscles in your stomach work too slowly or stop squeezing altogether, delaying the normal movement of food down into your intestines. Even when there is no physical blockage, food sits in your stomach for hours, leading to premature fullness after just a few bites, nausea, bloating, and vomiting.",
        "doctor_consultation_checklist": {
            "parameter_question": "What percentage of food remained in my stomach at the 4-hour mark on my nuclear gastric emptying scan?",
            "safety_question": "What are the earliest facial twitching or involuntary movement signs (tardive dyskinesia) I should watch for while taking metoclopramide?",
            "action_threshold_question": "Are my diabetes medications (such as GLP-1 receptor agonists or pramlintide) worsening my stomach emptying delays?"
        },
        "red_flags": [
            "Inability to keep liquids down for >24 hours with dark concentrated urine, intractable vomiting, severe crampy abdominal pain, or confusion from low potassium"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Gastroparesis is a disorder that slows or stops the movement of food from your stomach to your small intestine, even though there is no blockage.",
                "plain_analogy": "A stomach pump that has lost its horsepower, leaving food sitting motionless in the tank like water in a clogged drain.",
                "lifestyle_action": "Eat 6 tiny, low-fat, low-fiber meals every day. Puree vegetables. Drink liquids separate from solids."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Metoclopramide Oral / Nasal Spray", "Erythromycin", "Domperidone (Investigational IND)", "Ondansetron"],
                "dosing_gdmt": "Metoclopramide 5-10 mg orally 30 minutes before meals and at bedtime (maximum 40 mg/day for <=12 weeks).",
                "black_box_warning": "Metoclopramide: Tardive dyskinesia, an irreversible, involuntary movement disorder; risk increases with treatment duration and total cumulative dose.",
                "organ_clearance_cutoffs": "Reduce dose by 50% in patients with creatinine clearance <40 mL/min; discontinue immediately if muscle tics develop."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG Gastroparesis Guidelines",
                "pmid_or_doi": "10.14309/ajg.0000000000001874",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Standardized low-fat low-fiber dietary intervention reduces GCSI symptom scores by 38%; metoclopramide accelerates gastric emptying by 25-40%."
            }
        }
    },
    {
        "id": "DOC-CARD-225",
        "icd10": "E16.4",
        "condition": "Zollinger-Ellison Syndrome (Gastrinoma)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Consensus Review",
        "source_body": "National Comprehensive Cancer Network (NCCN) & Lancet",
        "citation": "Jensen RT et al. Zollinger-Ellison syndrome (gastrinoma): current approach to diagnosis and management. Lancet Oncol. 2008;9(6):600-610.",
        "doi_or_source": "10.1016/S1470-2045(08)70155-2",
        "clinical_evidence": "Zollinger-Ellison Syndrome (ZES) is caused by a neuroendocrine gastrin-secreting tumor (gastrinoma), located predominantly within the 'gastrinoma triangle' (duodenum and pancreas). Approximately 25-30% of cases occur as part of Multiple Endocrine Neoplasia Type 1 (MEN1). Hypergastrinemia causes marked hyperchlorhydria, resulting in severe refractory peptic ulcerations, gastroesophageal reflux, and secretory diarrhea (inactivation of pancreatic lipase by low pH). Diagnosis is established by fasting serum gastrin >1,000 pg/mL (in the presence of gastric pH <2) or a positive secretin stimulation test (rise in serum gastrin >120 pg/mL). High-dose PPI therapy eliminates acid hypersecretion and peptic complications in >98% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Zero alcohol and NSAID intake; 68Ga-DOTATATE PET/CT imaging for precision functional tumor localization; genetic screening for MEN1 (menin gene mutation) and serum calcium/PTH testing.",
            "monitoring_cadence": "Gastric acid output testing (target basal acid output [BAO] <10 mEq/h; <5 mEq/h in prior acid surgery); annual 68Ga-DOTATATE PET/CT and serum chromogranin A / gastrin.",
            "clinical_thresholds": "Localized sporadic gastrinoma without distant liver metastases mandates surgical exploratory laparotomy, duodenotomy, and lymph node dissection for curative resection."
        },
        "patient_plain_language": "Zollinger-Ellison syndrome is a rare digestive disorder where tiny tumors called gastrinomas form in your pancreas or the first part of your small intestine. These tumors release large surges of a hormone called gastrin. The gastrin stimulates your stomach to produce massive amounts of burning acid, causing severe recurrent ulcers and chronic watery diarrhea.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my fasting serum gastrin level and was my gastric fluid pH checked to ensure it was truly acidic?",
            "safety_question": "Have we checked my blood calcium and parathyroid hormone levels to rule out genetic Multiple Endocrine Neoplasia type 1 (MEN1)?",
            "action_threshold_question": "What does my 68Ga-DOTATATE PET scan show regarding whether the tumor can be completely removed surgically?"
        },
        "red_flags": [
            "Sudden severe rigid board-like belly pain (perforated ulcer), vomiting coffee-ground blood, black tarry bowel movements, or severe dizziness"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Zollinger-Ellison syndrome is a condition in which the stomach produces too much acid, caused by one or more tumors called gastrinomas.",
                "plain_analogy": "A runaway gas pedal in your stomach's acid factory, pumping out dangerous floods of burning acid non-stop.",
                "lifestyle_action": "Take high-dose PPI medication consistently without skipping doses. Avoid all NSAID pain relievers."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Pantoprazole Oral / IV", "Omeprazole", "Lansoprazole", "Octreotide"],
                "dosing_gdmt": "Omeprazole 60 mg daily (or 40 mg BID), titrated upward to 80-120 mg daily until basal acid output is <10 mEq/h.",
                "black_box_warning": "High-dose PPI: Risk of profound acid rebound if abruptly discontinued; maintain continuous dosing.",
                "organ_clearance_cutoffs": "Monitor bone density and serum magnesium; octreotide/somatostatin analogues used for metastatic disease."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NIH ZES Prospective Cohort",
                "pmid_or_doi": "10.1016/S1470-2045(08)70155-2",
                "cebm_level": 1,
                "sample_size": 850,
                "endpoints": "High-dose PPI achieves control of acid hypersecretion in >98%; curative surgical resection achieves 15-year survival >85%."
            }
        }
    },
    {
        "id": "DOC-CARD-226",
        "icd10": "K52.83",
        "condition": "Microscopic Colitis (Collagenous & Lymphocytic)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & ACG Guideline",
        "source_body": "Cochrane Database of Systematic Reviews & AGA Guidelines",
        "citation": "Stewart FA et al. Budesonide for induction of remission in microscopic colitis. Cochrane Database Syst Rev. 2017;7(7):CD006438.",
        "doi_or_source": "10.1002/14651858.CD006438.pub3",
        "clinical_evidence": "In a Cochrane systematic review of 11 randomized controlled trials (n=556 patients with collagenous or lymphocytic colitis), oral budesonide (9 mg daily for 6-8 weeks) was highly effective for induction of clinical remission compared with placebo (73% vs 22%; relative risk 3.01; 95% CI 2.18-4.14; p<0.00001; NNT = 2). Budesonide also provided significant histologic remission (RR 2.76; p<0.0001) and substantial quality of life improvements. Low-dose budesonide (3-6 mg daily) maintained clinical remission in 75% at 6 months (vs 25% placebo; p<0.0001). Diagnosis requires routine mucosal biopsies of normal-appearing colon (showing subepithelial collagen band >10 microns in collagenous colitis, or >20 intraepithelial lymphocytes per 100 enterocytes in lymphocytic colitis).",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinuation of offending drug triggers (NSAIDs, PPIs, SSRIs, and statins are strongly associated triggers); elimination of caffeine, artificial sweeteners (sorbitol/mannitol), and high-fat foods; smoking cessation.",
            "monitoring_cadence": "Clinical tracking of daily bowel movement frequency (target <3 loose stools/day); repeat colonoscopy only if 'red flag' symptoms develop or failure to respond to budesonide.",
            "clinical_thresholds": "Persisting watery diarrhea (>3 stools/day) despite 8 weeks of budesonide warrants screening for concomitant celiac disease (present in 5-10%) and bile acid malabsorption."
        },
        "patient_plain_language": "Microscopic colitis is an inflammatory bowel disorder that causes frequent, watery, non-bloody diarrhea, especially in older adults. When a doctor looks inside your colon with a camera, the colon lining looks completely normal and healthy to the naked eye. However, when small pinch biopsies are examined under a microscope, inflammation or an abnormal band of scar protein (collagen) is revealed.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my colon biopsies confirm lymphocytic colitis or collagenous colitis under the microscope?",
            "safety_question": "Which of my regular medications (like ibuprofen, stomach acid pills, or antidepressants) could be causing this colon inflammation?",
            "action_threshold_question": "How will we taper my budesonide steroid dose once my watery bowel movements return to normal?"
        },
        "red_flags": [
            "Bloody diarrhea, high fever, unintended severe weight loss, severe nocturnal fecal incontinence, or signs of severe dehydration"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Microscopic colitis is an inflammation of the large intestine (colon) that can only be seen with a microscope, causing persistent watery diarrhea.",
                "plain_analogy": "A colon that looks immaculate from the outside, but has hidden microscopic inflammation on the cellular level that prevents water absorption.",
                "lifestyle_action": "Stop all NSAID pain relievers. Cut out caffeine, dairy, and artificial sweeteners. Stay well hydrated with electrolyte drinks."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Budesonide Delayed-Release (Entocort EC)", "Loperamide", "Cholestyramine", "Bismuth Subsalicylate"],
                "dosing_gdmt": "Induction: Budesonide 9 mg once daily in the morning for 6-8 weeks. Maintenance for relapsing disease: Budesonide 3-6 mg daily.",
                "black_box_warning": "Budesonide: Significant CYP3A4 metabolism; avoid concurrent grapefruit juice or strong CYP3A4 inhibitors (ketoconazole).",
                "organ_clearance_cutoffs": "Extensive first-pass hepatic metabolism (90%); use caution in severe hepatic impairment (Child-Pugh C)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Cochrane Microscopic Colitis",
                "pmid_or_doi": "10.1002/14651858.CD006438.pub3",
                "cebm_level": 1,
                "sample_size": 556,
                "endpoints": "Clinical remission induced in 73% with budesonide vs 22% placebo (RR 3.01; p<0.00001; NNT=2); maintenance remission 75% vs 25%."
            }
        }
    },
    {
        "id": "DOC-CARD-227",
        "icd10": "K91.2",
        "condition": "Short Bowel Syndrome (Intestinal Failure)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (STEPS Trial) & ASPEN Guidelines",
        "citation": "Jeppesen PB et al. Teduglutide reduces need for parenteral support in patients with short-bowel syndrome (STEPS). Gut. 2011;60(7):902-914.",
        "doi_or_source": "10.1136/gut.2010.218271",
        "clinical_evidence": "In the landmark double-blind Phase 3 STEPS trial (n=86 short bowel syndrome patients dependent on parenteral nutrition/IV support), subcutaneous teduglutide (a GLP-2 analogue, 0.05 mg/kg/day for 24 weeks) significantly reduced weekly parenteral nutrition volume requirements by >=20% in 63% of patients (vs 30% placebo; p=0.002). The absolute reduction in weekly parenteral volume was 4.4 L in teduglutide vs 2.3 L in placebo (p<0.001), with 54% of treated patients able to eliminate >=1 day of parenteral support per week. Teduglutide enhances intestinal mucosal hyperplasia, expands crypt depth and villus height, and boosts intestinal fluid and nutrient absorption.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary adaptation: hyperphagic eating (30-40 kcal/kg/day); complex carbohydrates (50-60%); oral rehydration solution (ORS) with 90 mmol/L sodium; restriction of hypertonic sweet fluids and high-oxalate foods to prevent kidney stones.",
            "monitoring_cadence": "Weekly 24-hour fluid balance and urinary sodium excretion (target urinary sodium >20-30 mmol/L indicating euvolemia); monthly micronutrients (zinc, copper, selenium, fat-soluble vitamins A, D, E, K); baseline colonoscopy prior to teduglutide.",
            "clinical_thresholds": "Remaining small bowel length <150 cm without colon, or <60 cm with colon-in-continuity defines high risk for permanent parenteral support dependence."
        },
        "patient_plain_language": "Short bowel syndrome occurs when you are missing a large portion of your small intestine (usually after surgeries for bowel clots, Crohn's disease, or injury). Because the intestine is much shorter than normal, your body cannot absorb enough fluids, calories, vitamins, and minerals from eating, resulting in severe diarrhea, dehydration, and the need for liquid nutrition through an intravenous vein drip.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured length of my remaining functional small bowel in centimeters, and is my colon connected in continuity?",
            "safety_question": "Am I a candidate for teduglutide (GLP-2 hormone injection) to help grow my intestinal lining and reduce my weekly IV infusion days?",
            "action_threshold_question": "What daily urine output volume and urine sodium measurement confirms that my body is adequately hydrated?"
        },
        "red_flags": [
            "Fever, shivering, or chills while connected to a central venous catheter (PICC/Port line infection), sudden dizziness upon standing, or extreme muscle cramps"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Short bowel syndrome is a condition in which your body cannot absorb enough fluids and nutrients because part of the small intestine is missing.",
                "plain_analogy": "A highway detour that cut out 80% of the shopping exits, so your body drives right through without picking up groceries.",
                "lifestyle_action": "Sip specialized oral rehydration solution (not plain water). Eat small, high-calorie meals throughout the day."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Teduglutide (Gattex)", "Loperamide", "Diphenoxylate/Atropine", "Octreotide"],
                "dosing_gdmt": "Teduglutide 0.05 mg/kg once daily subcutaneous injection. High-dose Loperamide 4-8 mg 30 minutes before meals.",
                "black_box_warning": "Teduglutide: Potential acceleration of gastrointestinal polyp growth and neoplasia; colonoscopy required prior to initiation.",
                "organ_clearance_cutoffs": "Reduce teduglutide dose by 50% in moderate-to-severe renal impairment (CrCl <50 mL/min)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "STEPS",
                "pmid_or_doi": "10.1136/gut.2010.218271",
                "cebm_level": 2,
                "sample_size": 86,
                "endpoints": "63% achieved >=20% reduction in weekly IV parenteral volume (vs 30% placebo; p=0.002); 54% eliminated >=1 day of IV infusions per week."
            }
        }
    },
    {
        "id": "DOC-CARD-228",
        "icd10": "K63.821",
        "condition": "Small Intestinal Bacterial Overgrowth (SIBO)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (TARGET 1 & 2) & ACG SIBO Clinical Guideline",
        "citation": "Pimentel M et al. Rifaximin therapy for patients with irritable bowel syndrome without constipation (TARGET 1 & 2). N Engl J Med. 2011;364(1):22-32.",
        "doi_or_source": "10.1056/NEJMoa1004409",
        "clinical_evidence": "The landmark double-blind Phase 3 TARGET 1 and TARGET 2 trials (n=1260 patients with IBS-D/SIBO) demonstrated that a 14-day course of oral rifaximin (550 mg three times daily) significantly improved global IBS/SIBO symptoms (40.7% vs 31.7% placebo; p<0.001) and relieved bloating (40.2% vs 30.3%; p<0.001) for up to 10 weeks post-treatment. Retreatment with rifaximin upon symptom recurrence maintains efficacy without generating antimicrobial resistance (TARGET 3). Standardized glucose or lactulose breath testing showing an early rise in hydrogen >=20 ppm within 90 minutes (or methane >=10 ppm, diagnostic of Intestinal Methanogen Overgrowth [IMO]) confirms the diagnosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Temporary low-FODMAP dietary protocol for 4-6 weeks to reduce substrate fermentation; spacing meals by 4-5 hours to promote Phase III migrating motor complex (MMC) motility; daily prokinetic support.",
            "monitoring_cadence": "Follow-up hydrogen/methane breath test 4 weeks post-antimicrobial completion in persistent symptoms; clinical symptom log assessing bloating, stool frequency, and Bristol Stool Chart.",
            "clinical_thresholds": "Methane peak >=10 ppm on breath test indicates methanogen overgrowth (Methanobrevibacter smithii) requiring dual therapy (Rifaximin 550 mg TID + Neomycin 500 mg BID for 14 days)."
        },
        "patient_plain_language": "Small intestinal bacterial overgrowth (SIBO) occurs when bacteria that normally live harmlessly in your large colon back up and multiply inside your small intestine. When you eat foods containing sugars and carbohydrates, these out-of-place bacteria rapidly ferment the food, producing massive clouds of hydrogen or methane gas that cause painful bloating, gas, abdominal cramping, and chronic diarrhea.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my breath test show elevated hydrogen (diarrhea-predominant) or methane gas (constipation-predominant overgrowth)?",
            "safety_question": "Should we combine neomycin or metronidazole with rifaximin if my methane gas levels are over 10 ppm?",
            "action_threshold_question": "What bedtime gut-motility medication (prokinetic) should I take after completing antibiotics to keep the bacteria from migrating back?"
        },
        "red_flags": [
            "Severe unintended weight loss, chronic pale bulky foul-smelling stools that float (steatorrhea), severe fatigue, or low vitamin B12 / iron deficiency anemia"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Small intestinal bacterial overgrowth occurs when there is an abnormal increase in the bacterial population in the small intestine.",
                "plain_analogy": "Colonic bacteria trespassing into the small intestine, throwing a fermenting party every time you eat carbohydrates.",
                "lifestyle_action": "Follow a low-FODMAP diet for 4 weeks. Leave 4-hour fasting windows between meals to let natural gut sweeping waves work."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Rifaximin (Xifaxan)", "Neomycin", "Metronidazole", "Low-Dose Naltrexone", "Prucalopride"],
                "dosing_gdmt": "Hydrogen SIBO: Rifaximin 550 mg PO TID for 14 days. Methane IMO: Rifaximin 550 mg TID + Neomycin 500 mg BID for 14 days.",
                "black_box_warning": "Neomycin: Nephrotoxicity and irreversible ototoxicity (hearing loss and tinnitus); monitor renal function and auditory symptoms.",
                "organ_clearance_cutoffs": "Rifaximin has <0.4% systemic absorption; safe in mild-to-moderate liver disease without dosage adjustment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TARGET 1 & 2",
                "pmid_or_doi": "10.1056/NEJMoa1004409",
                "cebm_level": 2,
                "sample_size": 1260,
                "endpoints": "Global symptom relief in 40.7% with rifaximin vs 31.7% placebo (p<0.001); daily bloating relief improved significantly for 10 weeks."
            }
        }
    },
    {
        "id": "DOC-CARD-229",
        "icd10": "K75.4",
        "condition": "Autoimmune Hepatitis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Cohort Meta-Analysis",
        "source_body": "AASLD Guidelines & Journal of Hepatology",
        "citation": "Mack CL et al. Diagnosis and Management of Autoimmune Hepatitis in Adults and Children: 2019 Practice Guidance and Guidelines From the AASLD. Hepatology. 2020;72(2):696-722.",
        "doi_or_source": "10.1002/hep.31065",
        "clinical_evidence": "Autoimmune Hepatitis (AIH) is characterized by hypergammaglobulinemia (elevated IgG >1.1x ULN), circulating autoantibodies (ANA and SMA in Type 1; anti-LKM1 or anti-LC1 in Type 2), and interface hepatitis on liver biopsy. The Revised Original Score (>15 definite) and Simplified Diagnostic Criteria (>7 definite) achieve >95% diagnostic sensitivity and specificity. Combined induction therapy with prednisone (30-60 mg/day tapered) plus azathioprine (1-2 mg/kg/day) or budesonide (9 mg/day) produces complete biochemical remission (normalization of transaminases and IgG) in >85% of patients while minimizing corticosteroid adverse events. 10-year survival exceeds 90% with sustained biochemical remission.",
        "solution_protocol": {
            "non_pharmacological_targets": "Zero alcohol consumption; annual hepatitis A and B immunizations; screening for concurrent autoimmune diseases (thyroiditis in 15%, celiac disease in 5%).",
            "monitoring_cadence": "Serum ALT, AST, total bilirubin, and IgG every 2-4 weeks during induction until remission, then every 3-6 months lifelong; thiopurine methyltransferase (TPMT) genotyping prior to azathioprine.",
            "clinical_thresholds": "Failure of transaminases to decline by >50% within 4 weeks of therapy, or development of hepatic encephalopathy or coagulopathy (INR >1.5) triggers liver transplant evaluation."
        },
        "patient_plain_language": "Autoimmune hepatitis is a chronic disease where your body's immune defense system mistakenly identifies your own liver cells as foreign invaders and attacks them. This causes continuous inflammation, swelling, and scarring of the liver. Without medication to quiet down the overactive immune system, it can eventually lead to permanent liver cirrhosis.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current serum IgG level and have my liver enzymes (AST/ALT) returned to completely normal levels?",
            "safety_question": "Was my thiopurine methyltransferase (TPMT) enzyme checked to ensure I can metabolize azathioprine safely without bone marrow toxicity?",
            "action_threshold_question": "How long will I need to stay in complete biochemical remission before we consider tapering down to a maintenance dose?"
        },
        "red_flags": [
            "Yellowing of the whites of your eyes or skin (jaundice), abdominal swelling with fluid (ascites), confusion or memory lapses (encephalopathy), or vomiting blood"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Autoimmune hepatitis is liver inflammation that occurs when your body's immune system turns against liver cells.",
                "plain_analogy": "Friendly fire inside the body, where immune soldiers mistakenly bombard healthy liver cells.",
                "lifestyle_action": "Zero alcohol intake. Get vaccinated against hepatitis A and B. Take immune-suppressing medications at the exact same time daily."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone", "Azathioprine", "Budesonide", "Mycophenolate Mofetil", "Tacrolimus"],
                "dosing_gdmt": "Induction: Prednisone 30 mg daily + Azathioprine 50 mg daily, tapering prednisone to 5-10 mg daily while titrating azathioprine to 1-2 mg/kg/day.",
                "black_box_warning": "Azathioprine: Increased risk of malignancies (lymphomas) and severe bone marrow suppression (leukopenia/pancytopenia).",
                "organ_clearance_cutoffs": "Avoid in patients with homozygous TPMT or NUDT15 deficiency; monitor CBC and platelets every 2-4 weeks initially."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD AIH Guidelines",
                "pmid_or_doi": "10.1002/hep.31065",
                "cebm_level": 1,
                "sample_size": 2600,
                "endpoints": "Prednisone + azathioprine achieves complete biochemical remission in >85%; 10-year overall survival exceeds 90% in treated patients."
            }
        }
    },
    {
        "id": "DOC-CARD-230",
        "icd10": "K74.3",
        "condition": "Primary Biliary Cholangitis (PBC)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (POISE Trial) & AASLD Practice Guidance",
        "citation": "Nevens F et al. A Placebo-Controlled Trial of Obeticholic Acid in Primary Biliary Cholangitis (POISE). N Engl J Med. 2016;375(7):631-643.",
        "doi_or_source": "10.1056/NEJMoa1509840",
        "clinical_evidence": "Primary Biliary Cholangitis (PBC, formerly cirrhosis) is an autoimmune destruction of intrahepatic interlobular bile ducts, characterized by antimitochondrial antibodies (AMA titer >=1:40, specificity >98%) and elevated alkaline phosphatase (ALP). First-line therapy with ursodeoxycholic acid (UDCA 13-15 mg/kg/day) normalizes survival when biochemical response is achieved (Paris II or Toronto criteria: ALP <1.67x ULN and normal bilirubin). In the landmark Phase 3 POISE trial (n=217 patients with inadequate response or intolerance to UDCA), adding obeticholic acid (5-10 mg daily) achieved the composite biochemical endpoint in 46-47% vs 10% placebo (p<0.001) with marked reductions in ALP, bilirubin, and liver fibrosis markers.",
        "solution_protocol": {
            "non_pharmacological_targets": "Adequate dietary calcium (1,200 mg/day) and vitamin D (800-2,000 IU/day) to prevent accelerated metabolic bone disease; gentle skin moisturizers and cool baths for severe pruritus.",
            "monitoring_cadence": "Serum alkaline phosphatase (ALP), total bilirubin, and ALT/AST every 3-6 months; bone mineral density scan (DEXA) every 2 years; transient elastography (FibroScan) annually; screening for fat-soluble vitamin deficiencies (A, D, E, K).",
            "clinical_thresholds": "ALP >1.67x ULN or total bilirubin >ULN after 12 months on optimal UDCA therapy defines non-response, requiring second-line add-on therapy (PPAR agonists such as bezafibrate/elafibranor or obeticholic acid)."
        },
        "patient_plain_language": "Primary biliary cholangitis (PBC) is an autoimmune condition where your immune system slowly attacks and destroys the microscopic bile ducts inside your liver. These ducts are tiny drainage tubes that carry bile (digestive fluid) out of the liver. When the tubes are damaged, toxic bile backs up inside the liver, causing liver scarring, deep fatigue, and severe skin itching.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current alkaline phosphatase (ALP) level and has it dropped below 1.67 times the normal limit on my medication?",
            "safety_question": "How should we treat my intense skin itching (pruritus)—would cholestyramine, rifampin, or naltrexone be safe for me?",
            "action_threshold_question": "Has my bone mineral density been checked with a DEXA scan to screen for osteoporosis caused by bile malabsorption?"
        },
        "red_flags": [
            "Yellowing of the skin or eyes (jaundice), swelling of the abdomen with fluid (ascites), vomiting blood from enlarged veins (variceal bleed), or confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Primary biliary cholangitis is an autoimmune disease of the liver that slowly destroys the small bile ducts in the liver.",
                "plain_analogy": "Corroded microscopic drainage pipes in the liver that leak toxic bile fluid back into the liver cells, causing inflammation.",
                "lifestyle_action": "Take ursodiol consistently with meals. Protect your bones with calcium and vitamin D. Avoid scratching itchy skin."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Ursodiol (UDCA)", "Obeticholic Acid (Ocaliva)", "Elafibranor", "Cholestyramine"],
                "dosing_gdmt": "First-line: Ursodiol 13-15 mg/kg daily in 2-4 divided doses with food. Second-line: Obeticholic acid 5 mg daily, titrated to 10 mg.",
                "black_box_warning": "Obeticholic Acid: Hepatic decompensation and death in patients with decompensated cirrhosis (Child-Pugh B or C).",
                "organ_clearance_cutoffs": "Contraindicated in patients with complete biliary obstruction or decompensated cirrhosis; monitor LFTs quarterly."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POISE",
                "pmid_or_doi": "10.1056/NEJMoa1509840",
                "cebm_level": 2,
                "sample_size": 217,
                "endpoints": "Composite endpoint (ALP <1.67x ULN + normal bilirubin) met in 47% with obeticholic acid vs 10% placebo (p<0.001); liver stiffness improved."
            }
        }
    },
    {
        "id": "DOC-CARD-231",
        "icd10": "K83.01",
        "condition": "Primary Sclerosing Cholangitis (PSC)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Surveillance Cohorts",
        "source_body": "AASLD Practice Guidelines & The Lancet",
        "citation": "Bowlus CL et al. AASLD Practice Guidance on Primary Sclerosing Cholangitis and Cholangiocarcinoma. Hepatology. 2023;77(2):659-702.",
        "doi_or_source": "10.1097/HEP.0000000000000044",
        "clinical_evidence": "Primary Sclerosing Cholangitis (PSC) is a progressive fibro-obliterative disease of intrahepatic and extrahepatic bile ducts strongly associated with inflammatory bowel disease (IBD, present in 70-80% of patients, predominantly ulcerative colitis). Magnetic resonance cholangiopancreatography (MRCP) is the diagnostic imaging modality of choice, showing characteristic multifocal strictures and segmental dilatations ('beading' pattern) without diagnostic autoantibodies. Patients face a 400-fold increased risk of cholangiocarcinoma (lifetime risk 10-20%) and a marked risk of colorectal carcinoma (4-fold higher than IBD alone). Surveillance with annual MRCP + CA 19-9 and annual colonoscopy with random biopsies is mandatory.",
        "solution_protocol": {
            "non_pharmacological_targets": "Annual screening colonoscopy with random 4-quadrant biopsies from cecum to rectum for colorectal dysplasia; fat-soluble vitamin (A, D, E, K) supplementation; avoidance of alcohol.",
            "monitoring_cadence": "Annual MRCP and serum CA 19-9 for cholangiocarcinoma surveillance; serum alkaline phosphatase, bilirubin, and liver panel every 3-6 months; bone mineral density every 2-3 years.",
            "clinical_thresholds": "Rapid worsening of jaundice, fever, chills, or development of a 'dominant stricture' (diameter <1.5 mm in common bile duct or <1.0 mm in hepatic duct) mandates ERCP with brush cytology and FISH to exclude cholangiocarcinoma."
        },
        "patient_plain_language": "Primary sclerosing cholangitis (PSC) is an inflammatory disease that causes scarring and narrowing in the medium and large bile ducts both inside and outside your liver. The bile tubes become stiff, blocked, and beaded like a string of knotted ropes. Because bile cannot drain into the intestines, it backs up, causing liver damage. It is closely linked to ulcerative colitis.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my MRCP scan show any 'dominant strictures' that need endoscopic balloon widening and cancer cell brushings?",
            "safety_question": "Am I scheduled for my annual colonoscopy with biopsies to monitor for precancerous colon cells linked to my bowel disease?",
            "action_threshold_question": "What is my revised Mayo PSC risk score and when should I be listed for a liver transplant consultation?"
        },
        "red_flags": [
            "High fever with shaking chills and right upper abdominal pain (bacterial cholangitis), sudden dark tea-colored urine, pale stools, or severe jaundice"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Primary sclerosing cholangitis is a long-term progressive disease of the liver and gallbladder marked by inflammation and scarring of the bile ducts.",
                "plain_analogy": "Hardened, scarred bile drain pipes that pinch shut like knotted garden hoses, trapping bile inside the liver.",
                "lifestyle_action": "Undergo annual colonoscopy and annual MRI scans without exception. Take fat-soluble vitamin supplements."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Ceftriaxone (for acute cholangitis)", "Ciprofloxacin", "Ursodiol (Low-dose 13-15 mg/kg)", "Cholestyramine"],
                "dosing_gdmt": "Acute bacterial cholangitis: Ceftriaxone 1-2g IV daily + Metronidazole 500 mg TID. Pruritus: Cholestyramine 4g BID.",
                "black_box_warning": "High-dose Ursodiol (28-30 mg/kg): Contraindicated in PSC; clinical trials showed doubled rates of death and liver transplantation.",
                "organ_clearance_cutoffs": "Monitor CA 19-9; values >129 U/mL have 79% sensitivity and 98% specificity for cholangiocarcinoma in PSC."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASLD PSC Guidelines",
                "pmid_or_doi": "10.1097/HEP.0000000000000044",
                "cebm_level": 1,
                "sample_size": 3900,
                "endpoints": "Surveillance with annual MRCP and colonoscopy detects cholangiocarcinoma and colorectal dysplasia at early resectable stages; liver transplant 5-year survival >85%."
            }
        }
    },
    {
        "id": "DOC-CARD-232",
        "icd10": "E83.01",
        "condition": "Wilson's Disease (Hepatolenticular Degeneration)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & International Registry",
        "source_body": "AASLD Practice Guidelines & European Association for the Study of the Liver (EASL)",
        "citation": "Schilsky ML et al. A multidisciplinary approach to the diagnosis and management of Wilson disease. Hepatology. 2023;77(4):1428-1455.",
        "doi_or_source": "10.1097/HEP.0000000000000126",
        "clinical_evidence": "Wilson's disease is an autosomal recessive disorder of copper metabolism caused by mutations in the ATP7B gene on chromosome 13, leading to impaired biliary copper excretion and defective ceruloplasmin incorporation. Toxic copper accumulates sequentially in the liver, brain (basal ganglia/lenticular nuclei), cornea (Kayser-Fleischer rings present in >95% of neurologic cases), and kidneys. Diagnostic hallmarks include decreased serum ceruloplasmin (<20 mg/dL), elevated 24-hour urinary copper excretion (>40-100 mcg/24h), and hepatic parenchymal copper concentration >250 mcg/g dry weight on liver biopsy. Leipzig diagnostic score >=4 establishes definitive diagnosis. Chelation therapy with penicillamine or trientine halts disease progression and reverses hepatic/neurologic deficits in >80%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict lifelong avoidance of copper-rich foods (organ meats/liver, shellfish/oysters, dark chocolate, mushrooms, nuts); testing household drinking water for copper pipes; slit-lamp ophthalmologic exam.",
            "monitoring_cadence": "24-hour urinary copper and non-ceruloplasmin-bound (free) copper every 3-6 months (target 24h urine copper on chelator 200-500 mcg/day; on zinc maintenance <75 mcg/day); complete blood count and urinalysis (monitoring chelator toxicity).",
            "clinical_thresholds": "Acute fulminant liver failure (marked by Coombs-negative hemolytic anemia, AST:ALT ratio >2.2, and alkaline phosphatase to total bilirubin ratio <4.0) has near 100% mortality without emergent liver transplantation."
        },
        "patient_plain_language": "Wilson's disease is an inherited genetic condition where your body cannot get rid of excess copper from the foods you eat. Instead of releasing extra copper into your digestive bile, the copper builds up in your liver and then spills over into your brain and eyes. This can cause liver damage, tremors, difficulty speaking, mood changes, and a distinctive golden-brown ring around the iris of your eye (Kayser-Fleischer ring).",
        "doctor_consultation_checklist": {
            "parameter_question": "What were my 24-hour urinary copper excretion and serum ceruloplasmin levels, and did my eye exam show Kayser-Fleischer rings?",
            "safety_question": "What are the earliest warning signs of bone marrow suppression or kidney damage from penicillamine or trientine?",
            "action_threshold_question": "Should my brothers, sisters, and children undergo genetic ATP7B mutation screening for Wilson's disease?"
        },
        "red_flags": [
            "Sudden severe yellow jaundice accompanied by extreme tiredness, anemia with dark cola-colored urine (acute hemolytic crisis), or rapid onset confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Wilson disease is an inherited disorder in which excessive amounts of copper accumulate in the body, particularly in the liver, brain, and eyes.",
                "plain_analogy": "A broken copper filter in the liver, causing toxic copper dust to accumulate in your liver and brain machinery.",
                "lifestyle_action": "Avoid shellfish, liver, dark chocolate, and nuts. Test household tap water for copper. Take chelating medication on an empty stomach."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Penicillamine (Cuprimine)", "Trientine Hydrochloride", "Zinc Acetate (Galzin)"],
                "dosing_gdmt": "Chelation: Penicillamine 250-500 mg PO QID on empty stomach (1 hour before or 2 hours after meals) + Pyridoxine (vitamin B6) 25-50 mg daily.",
                "black_box_warning": "Penicillamine: Aplastic anemia, agranulocytosis, thrombocytopenia, and fatal glomerulonephritis (Goodpasture syndrome).",
                "organ_clearance_cutoffs": "Monitor CBC and urinalysis weekly for 1 month, then monthly; discontinue immediately if severe proteinuria (>1 g/day) develops."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EASL/AASLD Wilson Guidance",
                "pmid_or_doi": "10.1097/HEP.0000000000000126",
                "cebm_level": 1,
                "sample_size": 1750,
                "endpoints": "Chelation therapy achieves clinical stabilization and reversal of hepatic dysfunction in >85%; early treatment normalizes life expectancy."
            }
        }
    },
    {
        "id": "DOC-CARD-233",
        "icd10": "E83.110",
        "condition": "Hereditary Hemochromatosis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Evidence Review",
        "source_body": "AASLD Guidelines & New England Journal of Medicine",
        "citation": "Kowdley KV et al. ACG Clinical Guideline: Hereditary Hemochromatosis. Am J Gastroenterol. 2019;114(8):1202-1218.",
        "doi_or_source": "10.14309/ajg.0000000000000315",
        "clinical_evidence": "Hereditary hemochromatosis is an autosomal recessive iron overload disorder caused primarily by homozygous C282Y mutations (or C282Y/H63D compound heterozygosity) in the HFE gene on chromosome 6, resulting in deficiency of the iron-regulatory peptide hepcidin. Unchecked ferroportin activity causes progressive intestinal iron hyperabsorption (2-4 mg/day vs 1 mg normal). Progressive iron deposition in hepatocytes, pancreatic islets, myocardium, pituitary, and synovium causes the classic 'bronze diabetes' tetrad (cirrhosis, diabetes mellitus, hyperpigmentation, and arthropathy). Diagnostic screening begins with fasting transferrin saturation (>45% in women, >50% in men) and serum ferritin (>200 ng/mL in women, >300 ng/mL in men), followed by HFE genetic testing. Therapeutic phlebotomy initiated prior to cirrhosis development restores normal life expectancy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoidance of iron supplements, multivitamin preparations containing iron, and high-dose vitamin C (>500 mg/day, which accelerates iron absorption); absolute avoidance of raw or undercooked shellfish (prevents lethal Vibrio vulnificus septicemia); alcohol abstinence.",
            "monitoring_cadence": "Weekly or biweekly therapeutic phlebotomy (500 mL blood removal per session) until serum ferritin reaches 50-100 ng/mL (induction phase), followed by maintenance phlebotomy every 2-4 months for life; screening liver ultrasound every 6 months if cirrhosis present.",
            "clinical_thresholds": "Serum ferritin >1,000 ng/mL with elevated AST/ALT carries high risk of advanced bridging fibrosis or cirrhosis, mandating non-invasive elastography or liver biopsy."
        },
        "patient_plain_language": "Hereditary hemochromatosis is a genetic 'iron overload' disorder where your digestive system absorbs far more iron from your food than your body can ever use. Because your body has no natural way to get rid of extra iron, the iron builds up over decades in your liver, heart, pancreas, and joints. The standard treatment is simple and life-saving: regularly donating a pint of blood (therapeutic phlebotomy) to pull the excess iron out.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current transferrin saturation percentage and serum ferritin level?",
            "safety_question": "Have we checked for liver scarring (fibrosis) with a FibroScan, especially if my ferritin is over 1,000 ng/mL?",
            "action_threshold_question": "How often do I need therapeutic phlebotomy (blood removal) to maintain my ferritin in the safe 50-100 ng/mL range?"
        },
        "red_flags": [
            "Severe pain and swelling after handling or eating raw seafood (Vibrio vulnificus infection), rapid irregular heartbeats, or severe right upper belly pain"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hemochromatosis is a disorder where too much iron builds up in your body, sometimes called iron overload.",
                "plain_analogy": "A rusty storage tank: your body absorbs double the normal iron and has no exit valve, so iron rusts and damages your organs.",
                "lifestyle_action": "Avoid iron pills and vitamin C supplements. Never eat raw oysters. Regular blood removal keeps iron levels safe."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Therapeutic Phlebotomy", "Deferasirox", "Deferoxamine"],
                "dosing_gdmt": "Induction Phlebotomy: 500 mL (removes ~250 mg elemental iron) weekly or biweekly until serum ferritin reaches 50-100 ng/mL.",
                "black_box_warning": "Deferasirox: Renal failure, hepatic failure, and fatal gastrointestinal hemorrhage; reserve for patients with phlebotomy contraindications.",
                "organ_clearance_cutoffs": "Monitor hemoglobin/hematocrit before each phlebotomy session; hold if hemoglobin drops <11 g/dL."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG Hemochromatosis Guidelines",
                "pmid_or_doi": "10.14309/ajg.0000000000000315",
                "cebm_level": 1,
                "sample_size": 4800,
                "endpoints": "Phlebotomy prior to onset of cirrhosis or diabetes normalizes long-term life expectancy; 10-year survival equals age-matched controls."
            }
        }
    },
    {
        "id": "DOC-CARD-234",
        "icd10": "K76.7",
        "condition": "Hepatorenal Syndrome (HRS-AKI)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (CONFIRM Trial) & AASLD Practice Guidance",
        "citation": "Wong F et al. Terlipressin plus Albumin for the Treatment of Type 1 Hepatorenal Syndrome (CONFIRM). N Engl J Med. 2021;384(9):818-827.",
        "doi_or_source": "10.1056/NEJMoa2008290",
        "clinical_evidence": "Hepatorenal syndrome acute kidney injury (HRS-AKI) is a severe form of functional renal failure occurring in advanced cirrhosis with ascites, driven by extreme splanchnic arterial vasodilation that triggers reflex renal vasoconstriction. In the landmark multicenter double-blind Phase 3 CONFIRM trial (n=300 patients with HRS-AKI), terlipressin plus IV albumin was significantly superior to placebo plus albumin in achieving verified HRS reversal (sustained serum creatinine <=1.5 mg/dL without renal replacement therapy for at least 10 days: 32% vs 17%; p=0.006). Terlipressin also improved renal function before liver transplantation (34% vs 17%; p=0.002). Definitive curative therapy remains orthotopic liver transplantation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate cessation of all diuretics (furosemide, spironolactone); absolute avoidance of nephrotoxic medications (NSAIDs, aminoglycosides, IV radiocontrast); diagnostic paracentesis to rule out spontaneous bacterial peritonitis (SBP).",
            "monitoring_cadence": "Serum creatinine, BUN, and electrolytes every 12-24 hours; continuous pulse oximetry and cardiopulmonary monitoring (monitoring for terlipressin-induced pulmonary edema and ischemic events); strict hourly urine output.",
            "clinical_thresholds": "Increase in serum creatinine >=0.3 mg/dL within 48h (or >=50% from baseline) that fails to reverse after 48 hours of diuretic withdrawal and IV albumin volume expansion (1 g/kg/day, max 100 g/day) establishes HRS-AKI."
        },
        "patient_plain_language": "Hepatorenal syndrome is a severe medical emergency where the kidneys suddenly stop functioning properly because of advanced liver disease (cirrhosis). The damaged liver causes large blood vessels in your abdomen to widen excessively, stealing blood away from your kidneys. The kidneys react by clamping down their own blood vessels, shutting down urine production.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current serum creatinine and has it improved after stopping water pills and receiving IV albumin?",
            "safety_question": "Are my oxygen levels and lungs being closely monitored while receiving terlipressin to watch for fluid overload?",
            "action_threshold_question": "What is my calculated MELD-Na score and has my liver transplant listing been expedited for dual liver-kidney allocation?"
        },
        "red_flags": [
            "Severe drop in urine output (scant or zero urine over 12 hours), progressive confusion (hepatic encephalopathy), shortness of breath, or blue fingers/toes"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hepatorenal syndrome is a type of progressive kidney failure that occurs in people with severe liver damage.",
                "plain_analogy": "The kidneys going into a state of shock and clamping their pipes shut because a scarred liver is hoarding all the body's blood flow.",
                "lifestyle_action": "Hospital ICU treatment required immediately. Stop all water pills. Strict fluid and sodium restriction."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Terlipressin IV (Terlivaz)", "Albumin Human 20-25% IV", "Norepinephrine IV", "Octreotide"],
                "dosing_gdmt": "Terlipressin 0.85 mg IV every 6 hours (titrated to 1.7 mg q6h if Cr does not decrease by >=30% by day 4) PLUS Albumin 20-40 g/day.",
                "black_box_warning": "Terlipressin: Serious or fatal respiratory failure; monitor oxygenation and avoid in patients with severe fluid overload (SpO2 <90%).",
                "organ_clearance_cutoffs": "Contraindicated in patients with active coronary artery disease, peripheral ischemia, or severe hypoxia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CONFIRM",
                "pmid_or_doi": "10.1056/NEJMoa2008290",
                "cebm_level": 2,
                "sample_size": 300,
                "endpoints": "Verified HRS reversal doubled with terlipressin vs placebo (32% vs 17%; p=0.006); need for pre-transplant dialysis significantly reduced."
            }
        }
    },
    {
        "id": "DOC-CARD-235",
        "icd10": "K72.90",
        "condition": "Hepatic Encephalopathy",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (Rifaximin HE Trial) & AASLD/EASL Guidelines",
        "citation": "Bass NM et al. Rifaximin treatment in hepatic encephalopathy. N Engl J Med. 2010;362(12):1071-1081.",
        "doi_or_source": "10.1056/NEJMoa0907893",
        "clinical_evidence": "Hepatic encephalopathy (HE) is a spectrum of neuropsychiatric abnormalities in patients with liver dysfunction and portosystemic shunting, driven by hyperammonemia crossing the blood-brain barrier and causing astrocyte swelling. In the landmark multicenter double-blind Phase 3 trial (n=299 patients in remission from recurrent HE), combination therapy with rifaximin (550 mg BID) plus lactulose significantly reduced the risk of an acute HE breakthrough episode by 58% compared with placebo over 6 months (22.1% vs 45.9%; hazard ratio 0.42; 95% CI 0.28-0.64; p<0.001; NNT = 4). Rifaximin also reduced HE-related hospitalizations by 50% (HR 0.50; p=0.01). First-line lactulose titration targeting 2-3 soft bowel movements daily remains the cornerstone.",
        "solution_protocol": {
            "non_pharmacological_targets": "Adequate daily dietary protein intake (1.2-1.5 g/kg/day, emphasizing dairy and vegetable proteins; protein restriction is harmful and worsens muscle wasting); search and correct precipitating factors (constipation, GI bleeding, infection, hypokalemia, sedatives).",
            "monitoring_cadence": "West Haven criteria mental status staging at each clinical review; Number Connection Test (NCT-A) or Animal Naming Test for minimal hepatic encephalopathy; serum electrolytes (especially potassium).",
            "clinical_thresholds": "West Haven Grade III/IV encephalopathy (somnolence, confusion, or coma) requires emergency intensive care admission and airway protection (endotracheal intubation) to prevent aspiration."
        },
        "patient_plain_language": "Hepatic encephalopathy is a decline in brain function that happens when your liver is too damaged to filter out normal toxins from your blood. Toxic substances, especially ammonia produced by gut bacteria when digesting protein, build up in your bloodstream and travel to your brain. This causes forgetfulness, day-night sleep reversal, sluggish thinking, flapping hand tremors (asterixis), and confusion.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current West Haven grade of encephalopathy, and are my lactulose doses producing 2 to 3 soft bowel movements every day?",
            "safety_question": "Am I on rifaximin along with my lactulose to provide the best protection against emergency hospitalizations?",
            "action_threshold_question": "Are there any sleeping pills, sedatives, or narcotics that I must strictly avoid to prevent triggering brain confusion?"
        },
        "red_flags": [
            "Severe confusion, inability to recognize family members, profound lethargy where the patient cannot be easily awakened, or slurred incoherent speech"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hepatic encephalopathy is a nervous system disorder caused by severe liver disease, where toxins build up in the blood and affect brain function.",
                "plain_analogy": "A toxic smog cloud reaching the brain because the liver's exhaust filter has broken down.",
                "lifestyle_action": "Take lactulose every single day without skipping doses. Maintain normal protein intake. Avoid all sleeping pills and tranquilizers."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Lactulose Oral Solution", "Rifaximin (Xifaxan 550 mg)", "Lactitol Oral", "L-Ornithine L-Aspartate"],
                "dosing_gdmt": "Lactulose 20-30 g (30-45 mL) orally 3-4 times daily titrated to achieve 2-3 soft bowel movements/day PLUS Rifaximin 550 mg BID.",
                "black_box_warning": "Lactulose: Excessive diuresis and diarrhea can cause severe hypernatremia, dehydration, and paradoxical worsening of HE.",
                "organ_clearance_cutoffs": "Monitor serum electrolytes (sodium and potassium) frequently; hypokalemia worsens renal ammonia production."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEJM Rifaximin HE",
                "pmid_or_doi": "10.1056/NEJMoa0907893",
                "cebm_level": 2,
                "sample_size": 299,
                "endpoints": "Breakthrough HE episodes reduced by 58% (HR 0.42; p<0.001; NNT=4); hospitalizations reduced by 50% (HR 0.50; p=0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-236",
        "icd10": "K86.1",
        "condition": "Chronic Pancreatitis",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Evidence Synthesis",
        "source_body": "American College of Gastroenterology (ACG) Guidelines",
        "citation": "Gardner TB et al. ACG Clinical Guideline: Chronic Pancreatitis. Am J Gastroenterol. 2020;115(3):322-339.",
        "doi_or_source": "10.14309/ajg.0000000000000535",
        "clinical_evidence": "Chronic pancreatitis is an irreversible fibro-inflammatory syndrome resulting in progressive destruction of pancreatic exocrine parenchyma and islet architecture. Alcohol consumption and tobacco smoking act synergistically as the leading etiologic drivers (TIGAR-O classification). Cross-sectional imaging (CT, MRI/MRCP, or endoscopic ultrasound [EUS]) establishes the diagnosis via classic structural hallmarks: parenchymal calcifications, ductal dilatations with strictures (chain of lakes appearance), and intraductal calculi. Smoking cessation reduces the rate of disease progression and reduces the 12-fold elevated risk of pancreatic ductal adenocarcinoma. Antioxidant supplementation and high-dose pancreatic enzyme replacement therapy (PERT) relieve pain and malabsorption.",
        "solution_protocol": {
            "non_pharmacological_targets": "Complete and permanent cessation of alcohol and tobacco smoking; 5-6 small meals daily; moderate healthy fat intake without extreme restriction; fat-soluble vitamin supplementation.",
            "monitoring_cadence": "Annual fecal elastase-1 testing (monitoring exocrine insufficiency); annual fasting blood glucose and HbA1c (screening for pancreatogenic Type 3c diabetes); annual contrast MRI/MRCP or EUS; bone mineral density every 2 years.",
            "clinical_thresholds": "Intractable opioid-dependent abdominal pain with a dilated main pancreatic duct (>=5-7 mm) warrants surgical drainage (Frey or Puestow procedure) or endoscopic stenting."
        },
        "patient_plain_language": "Chronic pancreatitis is long-term, permanent inflammation and scarring of your pancreas, the organ tucked behind your stomach that makes digestive juices and insulin. Over time, the constant inflammation destroys healthy pancreas tissue and causes chalky stones to form inside the pancreatic ducts. This leads to persistent upper belly pain, malabsorption, and weight loss.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my CT or MRCP scan show pancreatic duct dilation or calcified stones that could be relieved with an endoscopic or surgical drainage procedure?",
            "safety_question": "Am I taking enough digestive enzymes with every meal to absorb my food and prevent weight loss?",
            "action_threshold_question": "Have we tested my blood sugar to screen for Type 3c pancreatogenic diabetes?"
        },
        "red_flags": [
            "Severe unrelenting abdominal pain boring through to the back with intractable vomiting, high fever with chills (infected pseudocyst), or yellowing of the skin"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Chronic pancreatitis is long-term inflammation of the pancreas that leads to permanent damage and impairs digestion.",
                "plain_analogy": "A scarred and hardened digestive engine with blocked internal plumbing, unable to pump out digestive juices.",
                "lifestyle_action": "Absolute zero alcohol and tobacco. Eat small, frequent meals. Take digestive enzymes with the very first bite of every meal."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Pancrelipase (Creon / Zenpep)", "Pregabalin", "Tramadol", "Antioxidants (Selenium, Vitamin C/E)"],
                "dosing_gdmt": "Pancrelipase 40,000-50,000 USP lipase units per full meal and 20,000-25,000 units with snacks; swallow whole with liquid.",
                "black_box_warning": "Pancrelipase: Fibrosing colonopathy reported with extremely high doses (>10,000 lipase units/kg/day); do not exceed recommended dosing.",
                "organ_clearance_cutoffs": "Derived from porcine pancreatic tissue; use caution in patients with porcine protein hypersensitivity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG Chronic Pancreatitis",
                "pmid_or_doi": "10.14309/ajg.0000000000000535",
                "cebm_level": 1,
                "sample_size": 2900,
                "endpoints": "Surgical decompression (Frey/Puestow) achieves superior pain relief to endoscopic stenting at 5 years (80% vs 38%; p=0.042); smoking cessation reduces cancer risk."
            }
        }
    },
    {
        "id": "DOC-CARD-237",
        "icd10": "K86.81",
        "condition": "Pancreatic Exocrine Insufficiency (PEI)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Meta-Analysis",
        "source_body": "Cochrane Database of Systematic Reviews & United European Gastroenterology (UEG)",
        "citation": "de la Iglesia-Garcia D et al. Efficacy of pancreatic enzyme replacement therapy in chronic pancreatitis: systematic review and meta-analysis. Gut. 2017;66(8):1354-1365.",
        "doi_or_source": "10.1136/gutjnl-2016-312529",
        "clinical_evidence": "Pancreatic exocrine insufficiency (PEI) results when functional pancreatic enzyme secretion drops below 10% of physiological capacity, leading to severe fat and protein maldigestion. In a systematic review and meta-analysis of 14 randomized controlled trials (n=518 patients), enteric-coated pancreatic enzyme replacement therapy (PERT) significantly increased the coefficient of fat absorption (CFA) by 13.9 percentage points compared with placebo (mean CFA 83.7% vs 69.8%; 95% CI 9.9-17.9; p<0.00001). PERT also improved coefficient of nitrogen absorption, relieved steatorrhea, and produced substantial weight gain. Fecal elastase-1 (FE-1) <200 mcg/g stool (severe if <100 mcg/g) is the non-invasive diagnostic standard (sensitivity 95% in moderate-to-severe PEI).",
        "solution_protocol": {
            "non_pharmacological_targets": "Do not restrict dietary fat (fat restriction exacerbates weight loss and fat-soluble vitamin depletion); consume 5-6 small energy-dense meals; take PERT capsules distributed throughout the meal rather than before or after.",
            "monitoring_cadence": "Quarterly body weight and nutritional parameters (BMI, serum albumin, prealbumin); biannual serum fat-soluble vitamins (A, 25-OH vitamin D, E, and INR/vitamin K); bone densitometry (DEXA) every 2 years.",
            "clinical_thresholds": "Fecal elastase-1 <100 mcg/g stool with persistent diarrhea or weight loss requires escalating PERT dosage (up to 75,000-80,000 lipase units/meal) and co-administration of a PPI to prevent gastric acid degradation of enzymes."
        },
        "patient_plain_language": "Pancreatic exocrine insufficiency (PEI) means your pancreas does not produce enough digestive enzymes to break down the food you eat. Because dietary fats cannot be digested and absorbed, they pass straight through your bowels. This leads to large, greasy, pale, foul-smelling stools that float in the toilet bowl (steatorrhea), along with stomach rumbles, weight loss, and vitamin deficiencies.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my fecal elastase-1 level in my stool sample, and does it indicate severe pancreatic enzyme deficiency?",
            "safety_question": "How many enzyme capsules should I take with large meals versus small snacks, and should I add a proton pump inhibitor to make them work better?",
            "action_threshold_question": "Have we checked my blood levels of fat-soluble vitamins (vitamins A, D, E, and K) to treat hidden nutritional deficiencies?"
        },
        "red_flags": [
            "Severe unintended weight loss, chronic pale bulky floating diarrhea with an oily film on toilet water, easy bruising (vitamin K deficiency), or bone fractures"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Pancreatic exocrine insufficiency is a condition where the pancreas does not produce enough enzymes to digest food, leading to malabsorption.",
                "plain_analogy": "Eating a healthy meal, but lacking the chemical scissors (enzymes) needed to cut up the food so your body can absorb it.",
                "lifestyle_action": "Take enzyme pills with the very first bite of food. Do not skip enzymes with snacks. Never crush or chew the capsules."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Pancrelipase (Creon)", "Zenpep", "Pancreaze", "Pertzye", "Viokace"],
                "dosing_gdmt": "Starting dose: 500 lipase units/kg/meal (typically 40,000-50,000 USP units with full meals and 25,000 units with snacks); adjust based on stool consistency.",
                "black_box_warning": "Pancrelipase: Do not exceed 2,500 lipase units/kg/meal or 10,000 units/kg/day to prevent fibrosing colonopathy.",
                "organ_clearance_cutoffs": "In patients with incomplete response, add Omeprazole 20 mg daily to increase duodenal pH and prevent gastric lipase denaturation."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PERT Meta-Analysis",
                "pmid_or_doi": "10.1136/gutjnl-2016-312529",
                "cebm_level": 1,
                "sample_size": 518,
                "endpoints": "Coefficient of fat absorption increased by 13.9% with PERT (p<0.00001); steatorrhea and abdominal cramping significantly reduced."
            }
        }
    },
    {
        "id": "DOC-CARD-238",
        "icd10": "E24.9",
        "condition": "Cushing's Syndrome & Disease",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "Endocrine Society & NEJM",
        "citation": "Nieman LK et al. The Diagnosis of Cushing's Syndrome: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2008;93(5):1526-1540.",
        "doi_or_source": "10.1210/jc.2008-0125",
        "clinical_evidence": "Cushing's syndrome results from prolonged, inappropriate tissue exposure to excess glucocorticoids, most commonly iatrogenic, or endogenous (Cushing's disease due to an ACTH-secreting pituitary adenoma in 70-80% of endogenous cases). Diagnostic confirmation requires at least two concordant first-line tests: 24-hour urinary free cortisol (UFC >3x ULN), late-night salivary cortisol (>2 elevated measurements, sensitivity/specificity >95%), or 1-mg overnight dexamethasone suppression test (serum cortisol post-dex >1.8 mcg/dL / >50 nmol/L). Plasma ACTH differentiates ACTH-dependent (>20 pg/mL) from ACTH-independent (<5 pg/mL, adrenal source) disease. First-line therapy for Cushing's disease is transsphenoidal pituitary adenomectomy (initial cure rate 70-85%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction (<2,000 mg/day); dietary calcium and vitamin D supplementation; blood pressure and glycemic optimization; psychological support for emotional lability.",
            "monitoring_cadence": "Post-operative morning serum cortisol at 24-48 hours post-transsphenoidal surgery (cortisol <2-5 mcg/dL confirms surgical cure and temporary adrenal insufficiency); long-term annual biochemical surveillance for tumor recurrence.",
            "clinical_thresholds": "Severe hypercortisolemia with hypokalemia, opportunistic infections, severe psychosis, or acute thromboembolism warrants immediate medical adrenal suppression (Ketoconazole, Osilodrostat, or Metyrapone) followed by urgent surgery."
        },
        "patient_plain_language": "Cushing's syndrome is a hormone disorder caused by having too much cortisol (the body's primary stress hormone) in your bloodstream for long periods. Cortisol is essential for life, but excessive amounts cause a rounded 'moon face', fat buildup on the back of the neck ('buffalo hump'), wide purple stretch marks across the belly, fragile skin that bruises easily, muscle weakness, and high blood pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "What did my 24-hour urine cortisol and midnight saliva cortisol tests show, and was my post-dexamethasone cortisol suppressed?",
            "safety_question": "Is my excess cortisol coming from a pituitary adenoma (Cushing's disease), an adrenal tumor, or an outside steroid medication?",
            "action_threshold_question": "Will I need temporary steroid replacement pills (hydrocortisone) after surgery while my remaining normal adrenal glands wake back up?"
        },
        "red_flags": [
            "Severe proximal muscle weakness (inability to stand from a chair without using arms), sudden high fever with pneumonia, severe psychosis, or blood clots in legs"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cushing syndrome is a disorder that occurs when your body makes too much of the hormone cortisol over a long period of time.",
                "plain_analogy": "A stress hormone thermostat stuck on maximum heat, breaking down muscle and depositing fat in the face and neck.",
                "lifestyle_action": "Limit sodium to prevent fluid retention. Protect thin skin from bruises. Engage in low-impact walking to rebuild leg muscle."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Osilodrostat (Isturisa)", "Ketoconazole", "Mifepristone (Korlym)", "Pasireotide", "Metyrapone"],
                "dosing_gdmt": "Osilodrostat 2 mg orally BID, titrated every 1-2 weeks up to 30 mg BID based on 24-hour urinary free cortisol.",
                "black_box_warning": "Mifepristone: Absolute contraindication in pregnancy (potent antiprogestational agent); monitor for hypokalemia and QTc prolongation.",
                "organ_clearance_cutoffs": "Monitor ECG for QTc prolongation with osilodrostat and ketoconazole; check liver enzymes weekly for ketoconazole."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Endocrine Society Cushing",
                "pmid_or_doi": "10.1210/jc.2008-0125",
                "cebm_level": 1,
                "sample_size": 2200,
                "endpoints": "Transsphenoidal pituitary surgery achieves 70-85% initial remission in microadenomas; osilodrostat normalizes UFC in 86% of persistent patients."
            }
        }
    },
    {
        "id": "DOC-CARD-239",
        "icd10": "E27.1",
        "condition": "Primary Adrenal Insufficiency (Addison's Disease)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "Endocrine Society & Lancet Diabetes & Endocrinology",
        "citation": "Bornstein SR et al. Diagnosis and Treatment of Primary Adrenal Insufficiency: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2016;101(2):364-389.",
        "doi_or_source": "10.1210/jc.2015-1710",
        "clinical_evidence": "Primary Adrenal Insufficiency (Addison's disease) is the destruction or dysfunction of the entire adrenal cortex, leading to combined deficiency of glucocorticoids (cortisol) and mineralocorticoids (aldosterone). Autoimmune adrenalitis (marked by 21-hydroxylase antibodies) accounts for >80-90% of cases in developed nations. Diagnostic gold standard is the high-dose synthetic ACTH (Cosyntropin 250 mcg) stimulation test; a peak serum cortisol <18 mcg/dL (<500 nmol/L) at 30 or 60 minutes establishes adrenal insufficiency, with plasma ACTH markedly elevated (>2x ULN). Hyponatremia, hyperkalemia, and generalized cutaneous hyperpigmentation (palmar creases, vermilion border, buccal mucosa) are pathognomonic hallmarks.",
        "solution_protocol": {
            "non_pharmacological_targets": "Mandatory medical alert bracelet ('Adrenal Insufficiency - Takes Steroids'); provision of an emergency injectable hydrocortisone kit (100 mg Act-O-Vial IM) with patient/family injection training; liberal dietary salt intake.",
            "monitoring_cadence": "Clinical review every 6 months assessing energy, blood pressure (lying and standing), body weight, and serum electrolytes; annual TSH and screening for autoimmune polyglandular syndromes (APS-1 and APS-2).",
            "clinical_thresholds": "Intercurrent physiological stress (fever >38°C, severe illness, dental surgery) requires immediate 'sick-day rules' (doubling or tripling oral hydrocortisone dose); major trauma or vomiting requires immediate 100 mg IM hydrocortisone."
        },
        "patient_plain_language": "Addison's disease is an autoimmune condition where your adrenal glands (tiny hormone factories sitting on top of your kidneys) become damaged and stop producing vital hormones called cortisol and aldosterone. Cortisol helps you handle stress and keep blood pressure steady, while aldosterone balances salt and water. Without these hormones, you develop deep fatigue, weight loss, salt cravings, low blood pressure, and a darkened skin tan.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my daily hydrocortisone and fludrocortisone replacement schedule, and are my blood potassium and sodium levels well balanced?",
            "safety_question": "Does my family know exactly how and when to inject my emergency 100 mg hydrocortisone rescue shot into my thigh muscle?",
            "action_threshold_question": "How do I adjust my daily steroid pills (sick-day rules) when I catch the flu, have dental surgery, or develop a fever?"
        },
        "red_flags": [
            "Severe vomiting or diarrhea, sudden severe abdominal pain, dizziness upon standing, systolic BP <90 mmHg, confusion, or collapse (Acute Adrenal Crisis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Addison disease is a disorder that occurs when the adrenal glands do not produce enough of their hormones.",
                "plain_analogy": "The body's primary stress engine running completely out of oil; without cortisol, any small stress or infection causes an engine stall.",
                "lifestyle_action": "Wear a medical alert bracelet at all times. Carry an emergency hydrocortisone injection kit everywhere. Never skip doses."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Hydrocortisone (Cortef)", "Fludrocortisone Acetate", "Prednisone", "Solu-Cortef (Emergency IM)"],
                "dosing_gdmt": "Hydrocortisone 15-25 mg/day in 2-3 divided doses (e.g. 10 mg at waking, 5 mg midday, 2.5 mg early evening) PLUS Fludrocortisone 0.05-0.2 mg daily.",
                "black_box_warning": "Under-replacement leads to fatal adrenal crisis; over-replacement causes osteoporosis, obesity, and cardiovascular morbidity.",
                "organ_clearance_cutoffs": "Titrate fludrocortisone based on seated/standing blood pressure, absence of orthostasis, and normal serum potassium."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Endocrine Society Addison Guidance",
                "pmid_or_doi": "10.1210/jc.2015-1710",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Circadian hydrocortisone dosing combined with emergency sick-day education reduces adrenal crisis admissions by 60%; normal life expectancy restored."
            }
        }
    },
    {
        "id": "DOC-CARD-240",
        "icd10": "E26.01",
        "condition": "Primary Hyperaldosteronism (Conn's Syndrome)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Endocrine Society Clinical Practice Guideline",
        "source_body": "Endocrine Society & The Lancet Diabetes & Endocrinology",
        "citation": "Funder JW et al. The Management of Primary Aldosteronism: Case Detection, Diagnosis, and Treatment: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2016;101(5):1889-1916.",
        "doi_or_source": "10.1210/jc.2015-4061",
        "clinical_evidence": "Primary Aldosteronism (PA) is the most common cause of secondary hypertension, accounting for 5-10% of all hypertensive patients and >20% of resistant hypertension. Autonomous aldosterone secretion by an adrenal adenoma (Conn's syndrome, 35%) or bilateral adrenal hyperplasia (60%) suppresses renin, causing sodium retention, potassium wasting, and target-organ damage disproportionate to blood pressure elevation (4-fold higher stroke, 6-fold higher myocardial infarction, and 12-fold higher atrial fibrillation risk). Initial screening requires the plasma aldosterone-to-renin ratio (ARR >20-30 with plasma aldosterone >10-15 ng/dL). Confirmatory testing (oral sodium loading or saline infusion test) followed by adrenal venous sampling (AVS) accurately distinguishes unilateral from bilateral disease with >95% accuracy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction (<2,000 mg/day; high dietary sodium worsens aldosterone-mediated vascular and myocardial fibrosis); alcohol moderation; aerobic physical conditioning.",
            "monitoring_cadence": "Home blood pressure monitoring weekly; serum potassium and creatinine at 2 weeks post-mineralocorticoid receptor antagonist initiation, then every 3-6 months; post-operative renin/aldosterone testing.",
            "clinical_thresholds": "Unilateral aldosterone hypersecretion confirmed by adrenal venous sampling (lateralization ratio >4:1 on AVS) indicates candidacy for curative laparoscopic unilateral adrenalectomy."
        },
        "patient_plain_language": "Primary hyperaldosteronism (Conn's syndrome) is a hormonal cause of severe high blood pressure. Your adrenal glands produce far too much of a hormone called aldosterone. Aldosterone tells your kidneys to hold onto excessive amounts of salt and water while dumping potassium into your urine. This drives blood pressure high and makes it resistant to standard blood pressure medications.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my aldosterone-to-renin ratio (ARR), and were my blood pressure medications adjusted before the blood test to ensure accuracy?",
            "safety_question": "Do I have a single benign nodule on one adrenal gland that can be cured with surgery, or do both glands have hyperplasia requiring pill therapy?",
            "action_threshold_question": "If I take spironolactone or eplerenone, what is my target serum potassium level and how often should my kidney function be checked?"
        },
        "red_flags": [
            "Severe refractory blood pressure (>180/110 mmHg), profound muscle weakness or cramps (severe hypokalemia), heart palpitations, or chest pressure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Primary aldosteronism is a condition in which the adrenal glands produce too much aldosterone, leading to high blood pressure and low potassium.",
                "plain_analogy": "An overactive salt valve in the adrenal glands, forcing the kidneys to stockpile salt and water while discarding potassium.",
                "lifestyle_action": "Strictly restrict dietary salt to under 2g daily. Check home blood pressure twice daily. Report muscle weakness."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Spironolactone (Aldactone)", "Eplerenone (Inspra)", "Amiloride"],
                "dosing_gdmt": "Spironolactone 25-50 mg daily, titrated up to 100-200 mg daily. Alternatively, Eplerenone 25-50 mg BID (fewer anti-androgenic side effects).",
                "black_box_warning": "Spironolactone: Tumors in rodent models; reserve for approved indications; monitor for hyperkalemia.",
                "organ_clearance_cutoffs": "Contraindicated in severe renal impairment (eGFR <30 mL/min) or serum potassium >5.0 mEq/L at baseline."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Endocrine Society Conn Guidance",
                "pmid_or_doi": "10.1210/jc.2015-4061",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "Unilateral laparoscopic adrenalectomy achieves complete biochemical cure in >98% and blood pressure cure in 50-60%; medical therapy normalizes cardiovascular risk."
            }
        }
    }
]