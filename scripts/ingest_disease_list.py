"""
AegisMed Unified Ingestion Engine (100 Landmark Verified Research-Backed Conditions)
Combines List 1 (001-050), List 2 (051-080), and List 3 (081-100).
Generates:
1. api/app/data/imported_knowledge.json
2. web/src/lib/suggestions.ts (rich search chips and guidelines)
"""

import sys
import json
import re
from pathlib import Path
from typing import Any, Dict, List

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

DATA_JSON_PATH = Path("api/app/data/imported_knowledge.json")
SUGGESTIONS_TS_PATH = Path("web/src/lib/suggestions.ts")

ALL_DISEASES: List[Dict[str, Any]] = [
  # ── LIST 1 (001 - 050) ────────────────────────────────────────────
  {
    "id": "DOC-CARD-001",
    "condition": "Essential Hypertension",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline & Network Meta-Analysis",
    "source_body": "ACC/AHA & JAMA",
    "citation": "Whelton PK et al. 2017/2024 ACC/AHA High Blood Pressure Clinical Practice Guideline; JAMA Network Meta-Analysis (49 RCTs, n=124,300).",
    "doi_or_source": "10.1161/HYP.0000000000000065",
    "clinical_evidence": "Meta-analysis confirms lowering SBP by 10 mmHg reduces major cardiovascular events by 20%, stroke by 27%, and heart failure by 28%. First-line pharmacological classes (thiazide diuretics, CCBs, ACEi/ARBs) demonstrate equivalent mortality reduction; CCBs excel in stroke prevention (RR 0.82), while ACEi/ARBs offer superior renal protection in diabetic cohorts (HR 0.68).",
    "solution_protocol": {
      "non_pharmacological_targets": "DASH diet adherence (approx. 11 mmHg SBP reduction in hypertensive adults); dietary sodium restriction to <1,500 mg/day (or at least 1,000 mg/day reduction); aerobic exercise 90-150 min/week; potassium supplementation (3,500-5,000 mg/day via diet unless CKD present).",
      "monitoring_cadence": "Standardized home blood pressure monitoring (HBPM): 2 morning and 2 evening readings for 7 consecutive days prior to clinical review.",
      "clinical_thresholds": "Stage 1: 130-139 / 80-89 mmHg (lifestyle modification + 10-year ASCVD risk stratification); Stage 2: ≥140/90 mmHg (lifestyle + combination guideline therapy)."
    },
    "patient_plain_language": "Blood pressure is the force of blood pushing against the walls of your arteries. When it stays high, it slowly damages your blood vessels like running water at too high a pressure through household pipes.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my average home blood pressure reading, and what is our exact target goal?",
      "safety_question": "Are there any over-the-counter decongestants or pain relievers (like NSAIDs) that could raise my blood pressure?",
      "action_threshold_question": "At what specific blood pressure reading should I call your office versus going to emergency care?"
    },
    "red_flags": [
      "Systolic BP > 180 mmHg or diastolic > 120 mmHg accompanied by chest pain, shortness of breath, back pain, or vision changes (Hypertensive Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-002",
    "condition": "Heart Failure with Reduced Ejection Fraction (HFrEF)",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (PARADIGM-HF)",
    "citation": "McMurray JJV et al. Angiotensin-Neprilysin Inhibition versus Enalapril in Heart Failure (PARADIGM-HF). N Engl J Med. 2014;371:993-1004.",
    "doi_or_source": "10.1056/NEJMoa1409077",
    "clinical_evidence": "In 8,442 patients with HFrEF (LVEF ≤40%), Sacubitril/Valsartan reduced composite CV death or heart failure hospitalization by 20% compared to Enalapril (HR 0.80; 95% CI 0.73-0.87; p<0.001). All-cause mortality was reduced by 16% (p<0.001). Guideline-directed medical therapy (GDMT) establishes foundational four-pillar therapy: ARNI/ACEi, beta-blockers, MRA, and SGLT2i.",
    "solution_protocol": {
      "non_pharmacological_targets": "Daily morning weight tracking; sodium restriction to <2,000-3,000 mg/day; fluid moderation (1.5-2.0 L/day) in congested patients; structured cardiac rehabilitation program.",
      "monitoring_cadence": "Serum potassium and eGFR checks 1-2 weeks after initiating or titrating neurohormonal antagonists.",
      "clinical_thresholds": "Monitor LVEF via echocardiogram every 6-12 months following optimization of medical therapy."
    },
    "patient_plain_language": "Heart failure means your heart muscle is pumping less efficiently than normal, making it harder to supply oxygen to your organs. It does not mean your heart has stopped beating.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my latest ejection fraction percentage, and is my heart function stable or improving?",
      "safety_question": "How much daily fluid should I drink, and what sudden weight gain warrants adjusting my diuretic?",
      "action_threshold_question": "What level of leg swelling or breathlessness while lying flat indicates my fluid balance is worsening?"
    },
    "red_flags": [
      "Weight gain >2-3 lbs in 24 hours or 5 lbs in one week",
      "Inability to lie flat without severe air hunger (orthopnea)",
      "Pink frothy sputum"
    ]
  },
  {
    "id": "DOC-CARD-003",
    "condition": "Atrial Fibrillation & Stroke Prophylaxis",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Double-Blind RCT",
    "source_body": "NEJM (ARISTOTLE)",
    "citation": "Granger CB et al. Apixaban versus Warfarin in Patients with Atrial Fibrillation (ARISTOTLE). N Engl J Med. 2011;365:981-992.",
    "doi_or_source": "10.1056/NEJMoa1107039",
    "clinical_evidence": "Apixaban was superior to Warfarin in preventing stroke or systemic embolism (HR 0.79; 95% CI 0.66-0.95; p=0.01 for superiority) with a 31% reduction in major bleeding (HR 0.69; 95% CI 0.60-0.80; p<0.001) and a significant reduction in all-cause mortality (HR 0.89; p=0.047). ACC/AHA guidelines strongly recommend DOACs over vitamin K antagonists in non-valvular AF.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict alcohol cessation/reduction; screening and management of obstructive sleep apnea; weight loss target of ≥10% in obese patients to reduce AF recurrence.",
      "monitoring_cadence": "Annual renal function (CrCl/eGFR) assessment to ensure appropriate DOAC dosing cutoffs (more frequent if CrCl 30-50 mL/min).",
      "clinical_thresholds": "Anticoagulation recommended based on CHA2DS2-VASc score (≥2 in males, ≥3 in females)."
    },
    "patient_plain_language": "Atrial fibrillation is an irregular, quivering heartbeat in the top chambers of your heart. Because blood does not pump out smoothly, it can pool and form clots that travel to the brain, causing a stroke.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my CHA2DS2-VASc stroke risk score, and what does it mean for my treatment plan?",
      "safety_question": "What signs of hidden bleeding (like dark stools or unusual bruising) should I monitor for on blood thinners?",
      "action_threshold_question": "If my heart suddenly beats erratically or fast, how long should I wait before seeking emergency medical care?"
    },
    "red_flags": [
      "Sudden facial droop, arm weakness, or speech slurring (FAST criteria for stroke)",
      "Uncontrolled bleeding from minor cuts, coughing up blood, or black tarry stools"
    ]
  },
  {
    "id": "DOC-CARD-004",
    "condition": "Hypercholesterolemia & Atherosclerotic Cardiovascular Disease (ASCVD)",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Major Clinical Practice Guideline",
    "source_body": "AHA/ACC/Multisociety",
    "citation": "Grundy SM et al. 2018/2019 AHA/ACC/AACVPR/AAPA/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Blood Cholesterol.",
    "doi_or_source": "10.1161/CIR.0000000000000625",
    "clinical_evidence": "Extensive meta-analyses of Cholesterol Treatment Trialists (CTT) show a 21% reduction in major vascular events per 1.0 mmol/L (~39 mg/dL) reduction in LDL-C. High-intensity statin therapy reduces LDL-C by ≥50%, moderate-intensity by 30-49%. Addition of non-statins (Ezetimibe, PCSK9 inhibitors) yields proportional additional cardiovascular event risk reductions.",
    "solution_protocol": {
      "non_pharmacological_targets": "Mediterranean or plant-forward dietary pattern: saturated fat <7% of total calories; elimination of trans fats; 25-30 g/day dietary fiber (7-13 g soluble fiber).",
      "monitoring_cadence": "Fasting lipid profile evaluated 4-12 weeks after initiating lifestyle or therapy changes; then every 3-12 months thereafter.",
      "clinical_thresholds": "Primary prevention: 10-year ASCVD risk threshold ≥7.5% warrants statin discussion; secondary prevention: target LDL-C <55 mg/dL (<1.4 mmol/L) in very high-risk individuals."
    },
    "patient_plain_language": "Cholesterol is a fatty substance your body needs, but too much 'bad' LDL cholesterol builds up inside your artery walls like rust in pipes, narrowing the pathway for blood to flow.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current LDL cholesterol level, and what is our target percentage reduction?",
      "safety_question": "If I experience unexplained muscle aches, how can we determine if it is related to my cholesterol regimen?",
      "action_threshold_question": "Would checking a coronary artery calcium (CAC) scan help clarify my personal 10-year risk?"
    },
    "red_flags": [
      "Acute crushing chest pressure radiating to the neck, jaw, or left arm",
      "Sudden shortness of breath on mild exertion"
    ]
  },
  {
    "id": "DOC-CARD-005",
    "condition": "Deep Vein Thrombosis (DVT) & Pulmonary Embolism (PE)",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "CHEST",
    "citation": "Stevens SM et al. Antithrombotic Therapy for VTE Disease: CHEST Guideline and Expert Panel Report. CHEST. 2021;160(6):e545-e608.",
    "doi_or_source": "10.1016/j.chest.2021.07.055",
    "clinical_evidence": "CHEST guidelines strongly recommend DOACs (Apixaban, Rivaroxaban, Dabigatran, Edoxaban) over Vitamin K antagonists for initial and long-term VTE management in non-cancer patients (Grade 1B). Minimum treatment duration for provoked VTE is 3 months; extended unprovoked VTE anticoagulation carries a >80% relative risk reduction in recurrent thrombosis.",
    "solution_protocol": {
      "non_pharmacological_targets": "Early ambulation over bed rest once therapeutic anticoagulation is started; graduated compression stockings for symptom relief in post-thrombotic syndrome.",
      "monitoring_cadence": "Periodic bleeding risk reassessment (e.g., HAS-BLED); baseline CBC, renal function, and liver enzymes.",
      "clinical_thresholds": "Diagnostic workup driven by validated clinical prediction scores (Wells DVT/PE score) followed by high-sensitivity D-dimer or compression ultrasonography/CT pulmonary angiography."
    },
    "patient_plain_language": "A DVT is a blood clot that forms in the deep veins of your leg. If part of the clot breaks free and travels to the lungs, it is called a pulmonary embolism (PE), which is a serious medical emergency.",
    "doctor_consultation_checklist": {
      "parameter_question": "Was my blood clot considered 'provoked' (caused by travel, surgery, or injury) or unprovoked?",
      "safety_question": "How long will I need to be on blood thinning therapy, and what activities should I modify?",
      "action_threshold_question": "What calf circumference difference or degree of swelling warrants an urgent ultrasound check?"
    },
    "red_flags": [
      "Sudden shortness of breath, sharp chest pain when breathing in, or coughing up blood (Signs of PE)",
      "Unilateral leg swelling with intense calf pain and warm, discolored skin"
    ]
  },
  {
    "id": "DOC-CARD-006",
    "condition": "Stable Ischemic Heart Disease & Angina",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Randomized Controlled Trial",
    "source_body": "NEJM (ISCHEMIA)",
    "citation": "Maron DJ et al. Initial Invasive versus Conservative Strategy for Stable Coronary Disease (ISCHEMIA). N Engl J Med. 2020;382:1395-1407.",
    "doi_or_source": "10.1056/NEJMoa1915925",
    "clinical_evidence": "In 5,179 patients with moderate or severe ischemia, an initial invasive strategy (angiography and revascularization plus medical therapy) did not reduce major ischemic cardiovascular events or all-cause death compared to an initial conservative strategy of optimal medical therapy alone (cumulative 5-year event rate 13.3% vs. 15.5%; p=0.34). Revascularization improved quality of life and angina symptoms in daily angina sufferers.",
    "solution_protocol": {
      "non_pharmacological_targets": "Supervised exercise training (30-60 min of moderate-intensity aerobic exercise 5+ days/week); smoking cessation (absolute risk reduction of CV events >30%); stress management protocols.",
      "monitoring_cadence": "Angina symptom frequency documentation (Seattle Angina Questionnaire); annual review of exercise tolerance.",
      "clinical_thresholds": "Revascularization reserved for failure of optimal medical therapy to control symptoms or left main stem/high-risk anatomy."
    },
    "patient_plain_language": "Stable angina is chest tightness or discomfort that occurs predictably during physical effort or stress, caused by narrowed arteries temporarily restricting blood flow to the heart muscle.",
    "doctor_consultation_checklist": {
      "parameter_question": "How does my stress test result classify the degree of blood flow restriction in my heart?",
      "safety_question": "How many minutes of rest should relieve my typical chest tightness before I consider it an emergency?",
      "action_threshold_question": "What is our plan if my typical symptoms begin occurring with less physical exertion?"
    },
    "red_flags": [
      "Chest discomfort occurring at rest, lasting longer than 15-20 minutes, or not relieved by rest (Unstable Angina / MI)"
    ]
  },
  {
    "id": "DOC-CARD-007",
    "condition": "Type 2 Diabetes Mellitus",
    "specialty": "Endocrinology",
    "organ_system": "Endocrine / Metabolic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Major Clinical Practice Guideline",
    "source_body": "ADA",
    "citation": "American Diabetes Association Professional Practice Committee. Standards of Care in Diabetes—2024. Diabetes Care. 2024;47(Suppl 1):S1-S343.",
    "doi_or_source": "10.2337/dc24-SINT",
    "clinical_evidence": "Targeted HbA1c control (<7.0% for most non-pregnant adults) significantly reduces microvascular complications (retinopathy, nephropathy, neuropathy). For individuals with established ASCVD, heart failure, or CKD, SGLT2 inhibitors and GLP-1 receptor agonists confer organ-protective benefits independent of baseline HbA1c or background metformin use (UKPDS, EMPA-REG, LEADER).",
    "solution_protocol": {
      "non_pharmacological_targets": "Weight reduction goal of ≥5-10% to improve glycemic control; 150 min/week moderate-to-vigorous aerobic exercise plus 2-3 sessions resistance training; carbohydrate counting and reduction in ultra-processed sugars.",
      "monitoring_cadence": "HbA1c testing twice yearly if meeting treatment goals; quarterly if therapy has changed or targets are unmet. Annual urine albumin-to-creatinine ratio (uACR) and dilated retinal exam.",
      "clinical_thresholds": "Standard glycemic target: HbA1c <7.0% (53 mmol/mol); pre-prandial glucose 80-130 mg/dL; post-prandial glucose <180 mg/dL."
    },
    "patient_plain_language": "In type 2 diabetes, your body’s cells become resistant to insulin—the key that lets sugar enter your cells for energy. Because the lock doesn't work, sugar builds up in your bloodstream.",
    "doctor_consultation_checklist": {
      "parameter_question": "What was my most recent HbA1c percentage, and is that customized safely for my age and health?",
      "safety_question": "Do any of my medications carry a risk of low blood sugar (hypoglycemia), and what symptoms should I look for?",
      "action_threshold_question": "What are my annual screening results for kidney function (uACR) and nerve health?"
    },
    "red_flags": [
      "Blood glucose >250 mg/dL with nausea, vomiting, abdominal pain, and rapid deep breathing (Diabetic Ketoacidosis / HHS)",
      "Blood glucose <70 mg/dL with confusion, sweating, shakiness, or loss of consciousness"
    ]
  },
  {
    "id": "DOC-CARD-008",
    "condition": "Obesity & Weight Management",
    "specialty": "Endocrinology",
    "organ_system": "Endocrine / Metabolic",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (SURMOUNT-1)",
    "citation": "Jastreboff AM et al. Tirzepatide Once Weekly for the Treatment of Obesity (SURMOUNT-1). N Engl J Med. 2022;387:205-216.",
    "doi_or_source": "10.1056/NEJMoa2206038",
    "clinical_evidence": "In 2,539 adults with obesity, Tirzepatide (dual GIP/GLP-1 receptor agonist) at 15 mg weekly achieved a mean weight reduction of 20.9% (-23.6 kg) at 72 weeks compared to 3.1% in placebo (p<0.001). Over 91% of participants in the 15 mg cohort achieved ≥5% weight loss, accompanied by significant reductions in blood pressure, fasting insulin, and lipid parameters.",
    "solution_protocol": {
      "non_pharmacological_targets": "Prescribed energy deficit of 500-750 kcal/day; high dietary protein intake (1.2-1.5 g/kg ideal body weight) combined with resistance training to preserve lean skeletal muscle mass during weight loss.",
      "monitoring_cadence": "Monthly weight and GI tolerability tracking during dose escalation; baseline and periodic lipid panels and glycemic status.",
      "clinical_thresholds": "Pharmacotherapy indicated for BMI ≥30 kg/m², or BMI ≥27 kg/m² with at least one weight-related comorbidity (e.g., hypertension, dyslipidemia, T2D, OSA)."
    },
    "patient_plain_language": "Obesity is a complex, chronic biological condition where appetite hormones and metabolism make it difficult to maintain a lower body weight, not simply a matter of willpower.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current BMI, and how is excess weight affecting my blood pressure and metabolic labs?",
      "safety_question": "How can I prevent muscle loss and nutrient deficiencies while losing weight?",
      "action_threshold_question": "What behavioral, nutritional, and medical tools are appropriate for my weight loss goal?"
    },
    "red_flags": [
      "Severe persistent abdominal pain radiating to the back with vomiting (Signs of pancreatitis or gallbladder disease)"
    ]
  },
  {
    "id": "DOC-CARD-009",
    "condition": "Metabolic Dysfunction-Associated Steatohepatitis (MASH / NASH)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive / Hepatic",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (MAESTRO-NASH)",
    "citation": "Harrison SA et al. A Phase 3, Randomized, Controlled Trial of Resmetirom in NASH with Liver Fibrosis (MAESTRO-NASH). N Engl J Med. 2024;390:497-509.",
    "doi_or_source": "10.1056/NEJMoa2309000",
    "clinical_evidence": "In 966 patients with biopsy-proven MASH and fibrosis stages F1B-F3, Resmetirom (thyroid hormone receptor-beta agonist) achieved MASH resolution with no worsening of fibrosis in 29.9% (100 mg) vs. 9.7% (placebo) (p<0.001), and fibrosis improvement of at least one stage with no worsening of NAFLD activity score in 25.9% vs. 14.2% (p<0.001).",
    "solution_protocol": {
      "non_pharmacological_targets": "7-10% total body weight reduction leads to steatohepatitis resolution and possible fibrosis regression; complete elimination of sugar-sweetened beverages and high-fructose corn syrup; Mediterranean dietary pattern.",
      "monitoring_cadence": "Non-invasive fibrosis assessment every 1-2 years using FIB-4 score calculation and transient elastography (FibroScan).",
      "clinical_thresholds": "FIB-4 score <1.30 rules out advanced fibrosis with high negative predictive value (>90%); FIB-4 >2.67 indicates high risk requiring hepatology evaluation."
    },
    "patient_plain_language": "MASH is an advanced form of fatty liver where excess fat stored in liver cells causes inflammation and scarring (fibrosis), similar to how skin forms a scar after an injury.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my calculated FIB-4 score, and does it show signs of liver stiffness or scarring?",
      "safety_question": "Are there any dietary supplements or medications I should avoid to protect my liver?",
      "action_threshold_question": "How frequently should we perform a liver ultrasound or FibroScan to track liver fat?"
    },
    "red_flags": [
      "Yellowing of the eyes or skin (jaundice)",
      "Abdominal swelling (ascites), confusion, or vomiting blood"
    ]
  },
  {
    "id": "DOC-CARD-010",
    "condition": "Primary Hypothyroidism",
    "specialty": "Endocrinology",
    "organ_system": "Endocrine",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ATA / AACE",
    "citation": "Garber JR et al. Clinical Practice Guidelines for Hypothyroidism in Adults. Endocr Pract. 2012;18(6):988-1028 (Reaffirmed 2023).",
    "doi_or_source": "10.4158/EP12280.GL",
    "clinical_evidence": "Guidelines establish Levothyroxine monotherapy as standard of care. Full replacement dose is approximately 1.6 mcg/kg/day in healthy adults, with lower initiation doses (25-50 mcg) in elderly patients or those with coronary artery disease to avoid precipitating cardiac ischemia. Routine addition of Liothyronine (T3) is not recommended by consensus due to lack of sustained RCT benefit.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict administration timing: Take on an empty stomach with a full glass of water 30-60 minutes before breakfast, or at bedtime (3-4 hours after the last meal); separate by ≥4 hours from calcium, iron, or antacids.",
      "monitoring_cadence": "Serum TSH reassessment 6-8 weeks after any dose adjustment or brand change; annual monitoring once clinically euthyroid.",
      "clinical_thresholds": "Target TSH range: 0.5-4.5 mIU/L (adjusted to 4.0-7.0 mIU/L in elderly adults >70-80 years to prevent overreplacement osteopenia/AFib)."
    },
    "patient_plain_language": "Your thyroid gland in your neck produces hormones that set your body's metabolic speed. In hypothyroidism, the gland is underactive, causing your body's engines to slow down.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current TSH number, and what specific range are we targeting for me?",
      "safety_question": "Do any of my other daily vitamins or iron supplements block thyroid hormone absorption?",
      "action_threshold_question": "If my fatigue or cold sensitivity changes, how soon should we re-test my blood levels?"
    },
    "red_flags": [
      "Extreme lethargy, hypothermia, slow heart rate, and confusion (Myxedema Coma)"
    ]
  },
  {
    "id": "DOC-CARD-011",
    "condition": "Polycystic Ovary Syndrome (PCOS)",
    "specialty": "Women's Health",
    "organ_system": "Reproductive / Endocrine",
    "cebm_level": 1,
    "evidence_tier": "Level 1: International Evidence-Based Guideline",
    "source_body": "ESHRE / ASRM / Monash",
    "citation": "Teede HJ et al. Recommendations from the 2023 International Evidence-based Guideline for the Assessment and Management of Polycystic Ovary Syndrome. Hum Reprod. 2023;38(9):1655-1679.",
    "doi_or_source": "10.1093/humrep/dead156",
    "clinical_evidence": "Diagnosis confirmed via Rotterdam criteria (2 of 3: oligo/anovulation, hyperandrogenism, polycystic ovaries on ultrasound). Lifestyle intervention is first-line management for all presentations. Combined oral contraceptives are first-line pharmacological treatment for irregular cycles and hirsutism. Metformin is recommended for metabolic features and glycemic control (SMD -0.45 on BMI/insulin). Letrozole is first-line ovulation induction agent over Clomiphene (NEJM PPCOS II).",
    "solution_protocol": {
      "non_pharmacological_targets": "5-10% weight loss restores regular ovulatory cycles in up to 50% of women; regular physical activity (minimum 150 min/week moderate intensity plus muscle strengthening); low glycemic index dietary emphasis.",
      "monitoring_cadence": "Baseline oral glucose tolerance test (OGTT) and lipid profile; repeat OGTT every 1-3 years based on metabolic risk.",
      "clinical_thresholds": "Endometrial protection protocol: ensure at least 4 withdrawal bleeds per year to prevent endometrial hyperplasia."
    },
    "patient_plain_language": "PCOS is a hormonal imbalance that affects how ovaries develop and release eggs, often linked to insulin resistance, causing irregular periods, acne, and excess hair growth.",
    "doctor_consultation_checklist": {
      "parameter_question": "Have we screened my insulin resistance and glucose tolerance with an OGTT test?",
      "safety_question": "How are we protecting my uterine lining if I go several months without a period?",
      "action_threshold_question": "If I plan to conceive, how soon should we discuss ovulation induction options?"
    },
    "red_flags": [
      "Extremely heavy vaginal bleeding soaking more than two pads per hour for over two consecutive hours"
    ]
  },
  {
    "id": "DOC-CARD-012",
    "condition": "Adult Persistent Asthma",
    "specialty": "Pulmonology",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Global Evidence-Based Strategy",
    "source_body": "GINA",
    "citation": "Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention (2024 Update). GINA Report.",
    "doi_or_source": "https://ginasthma.org/reports/",
    "clinical_evidence": "GINA Track 1 establishes low-dose ICS-Formoterol as the preferred reliever across all asthma severities. SYGMA 1 and 2 trials (NEJM 2018) proved as-needed ICS-Formoterol reduces severe exacerbations by 60-64% compared to SABA-only therapy, while reducing steroid exposure by 75-83%. SABA monotherapy is strongly discouraged due to increased risk of airway hyperresponsiveness and death.",
    "solution_protocol": {
      "non_pharmacological_targets": "Identification and mitigation of environmental triggers (tobacco smoke, indoor dust mites, animal dander, mold); written personalized Asthma Action Plan; inhaler technique demonstration at every clinical visit.",
      "monitoring_cadence": "Peak expiratory flow (PEF) home monitoring during symptom flare-ups; clinical follow-up 1-3 months after initiating controller therapy.",
      "clinical_thresholds": "Step-up or step-down evaluation based on symptom control validated questionnaires (e.g., Asthma Control Test [ACT] score ≥20 indicates control)."
    },
    "patient_plain_language": "Asthma is chronic inflammation of your airways that makes them swollen, sensitive, and tight when irritated. Using a rescue inhaler that contains both a muscle relaxer and a gentle anti-inflammatory calms the swelling instantly.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my inhaler prescription an anti-inflammatory reliever (Track 1) or a traditional fast-acting bronchodilator alone?",
      "safety_question": "Can you check my physical inhaler technique right now to make sure the medicine reaches deep into my lungs?",
      "action_threshold_question": "What exact peak flow reading or symptom frequency should trigger my written Asthma Action Plan?"
    },
    "red_flags": [
      "Struggling to speak in full sentences due to breathlessness",
      "Ribs or neck pulling in hard when inhaling (intercostal retractions)",
      "Peak flow reading <50% of personal best"
    ]
  },
  {
    "id": "DOC-CARD-013",
    "condition": "Chronic Obstructive Pulmonary Disease (COPD)",
    "specialty": "Pulmonology",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Global Practice Strategy & Multicenter RCTs",
    "source_body": "GOLD & NEJM (ETHOS)",
    "citation": "Global Strategy for Prevention, Diagnosis, and Management of COPD: 2024 Report (GOLD); Rabe KF et al. Triple Inhaled Therapy at Two Glucocorticoid Doses in COPD (ETHOS). N Engl J Med. 2020;383:35-48.",
    "doi_or_source": "10.1056/NEJMoa1916046",
    "clinical_evidence": "ETHOS trial (n=8,509) demonstrated single-inhaler triple therapy (ICS/LAMA/LABA) significantly reduced the rate of moderate or severe COPD exacerbations by 24% compared to LAMA/LABA dual therapy (p<0.001) and reduced all-cause mortality by 46% in patients with blood eosinophil counts ≥100 cells/μL and history of exacerbations.",
    "solution_protocol": {
      "non_pharmacological_targets": "Smoking cessation is the only intervention proven to slow FEV1 decline; pulmonary rehabilitation program (demonstrates Grade A evidence for reducing dyspnea and hospital admissions); pneumococcal, influenza, COVID-19, and RSV vaccinations.",
      "monitoring_cadence": "Post-bronchodilator spirometry documentation; annual review of inhaler delivery system adequacy and exacerbation frequency.",
      "clinical_thresholds": "Blood eosinophil count <100 cells/μL identifies patients unlikely to benefit from inhaled corticosteroids (increased pneumonia risk)."
    },
    "patient_plain_language": "COPD is long-term damage to the lungs and airways that causes them to become less elastic and easily clogged with mucus, making it harder to push air out when breathing.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current post-bronchodilator FEV1 percentage, and what GOLD group does that place me in?",
      "safety_question": "What are my blood eosinophil numbers, and do they indicate that steroid inhalers will help or hurt my lungs?",
      "action_threshold_question": "What changes in my phlegm color or volume signal the start of an infectious flare-up?"
    },
    "red_flags": [
      "Severe resting breathlessness accompanied by blue lips or fingertips (cyanosis)",
      "New confusion, extreme drowsiness, or morning headaches (Signs of hypercapnia/carbon dioxide retention)"
    ]
  },
  {
    "id": "DOC-CARD-014",
    "condition": "Community-Acquired Pneumonia (CAP)",
    "specialty": "Pulmonology",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ATS / IDSA",
    "citation": "Metlay JP et al. Diagnosis and Treatment of Adults with Community-Acquired Pneumonia: Official Clinical Practice Guideline of ATS and IDSA. Am J Respir Crit Care Med. 2019;200(7):e45-e67.",
    "doi_or_source": "10.1164/rccm.201908-1581ST",
    "clinical_evidence": "Clinical guideline establishes CURB-65 or Pneumonia Severity Index (PSI) to determine outpatient vs. inpatient site of care. For healthy outpatients without comorbidities, monotherapy with Amoxicillin (1 g TID) or Doxycycline is strongly recommended over macrolides due to widespread pneumococcal resistance. For patients with comorbidities, combination therapy (beta-lactam + macrolide) or respiratory fluoroquinolones is recommended.",
    "solution_protocol": {
      "non_pharmacological_targets": "Adequate oral hydration; early mobilization; temporary smoking cessation; fever management.",
      "monitoring_cadence": "Clinical reassessment at 48-72 hours to verify fever resolution and stabilization of vital signs.",
      "clinical_thresholds": "CURB-65 score: 0-1 points indicates suitability for outpatient therapy; ≥2 points suggests inpatient monitoring; ≥3 points warrants intensive care consideration."
    },
    "patient_plain_language": "Pneumonia is an infection that inflames the microscopic air sacs in one or both lungs, causing them to fill with fluid or pus, leading to cough, fever, and breathing trouble.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my CURB-65 pneumonia severity score, and is it completely safe for me to recover at home?",
      "safety_question": "How many days should I expect fever before we consider whether my antibiotic is working?",
      "action_threshold_question": "What oxygen saturation level on a home pulse oximeter should prompt immediate emergency care?"
    },
    "red_flags": [
      "Oxygen saturation drops below 92% on room air",
      "Confusion, persistent high fever unresponsive to medication, or inability to keep fluids down"
    ]
  },
  {
    "id": "DOC-CARD-015",
    "condition": "Obstructive Sleep Apnea (OSA)",
    "specialty": "Pulmonology",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AASM",
    "citation": "Patil SP et al. Treatment of Adult Obstructive Sleep Apnea with Positive Airway Pressure: An American Academy of Sleep Medicine Clinical Practice Guideline. J Clin Sleep Med. 2019;15(2):335-343.",
    "doi_or_source": "10.5664/jcsm.7640",
    "clinical_evidence": "Continuous Positive Airway Pressure (CPAP) is the gold standard therapy (AASM Grade Strong). Meta-analyses demonstrate CPAP reduces the Apnea-Hypopnea Index (AHI), decreases daytime sleepiness (Epworth Sleepiness Scale score reduction by 2.5-3.0 points), and lowers 24-hour mean blood pressure by 2.0-2.5 mmHg, especially in resistant hypertension.",
    "solution_protocol": {
      "non_pharmacological_targets": "Weight loss target of ≥10% body weight (reduces AHI by over 25%); complete avoidance of alcohol and sedatives within 4 hours of bedtime; positional therapy (avoiding supine sleeping position).",
      "monitoring_cadence": "Objective CPAP compliance monitoring (target ≥4 hours/night on ≥70% of nights) evaluated within 30-90 days.",
      "clinical_thresholds": "Mild OSA: AHI 5-14 events/hr; Moderate OSA: AHI 15-29 events/hr; Severe OSA: AHI ≥30 events/hr."
    },
    "patient_plain_language": "Sleep apnea happens when throat muscles relax during sleep, temporarily closing your airway like a squished straw and briefly stopping your breathing dozens of times every hour.",
    "doctor_consultation_checklist": {
      "parameter_question": "What was my Apnea-Hypopnea Index (AHI) from my sleep study, and did my oxygen levels drop significantly?",
      "safety_question": "What troubleshooting steps can we take if I struggle with CPAP mask leakage or nasal congestion?",
      "action_threshold_question": "If I cannot tolerate CPAP, would an oral mandibular advancement device be clinically suitable for me?"
    },
    "red_flags": [
      "Falling asleep while driving or operating machinery",
      "Waking up gasping or choking accompanied by severe chest pressure"
    ]
  },
  {
    "id": "DOC-CARD-016",
    "condition": "Chronic Kidney Disease (CKD)",
    "specialty": "Nephrology",
    "organ_system": "Renal",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (DAPA-CKD) & KDIGO",
    "citation": "Heerspink HJL et al. Dapagliflozin in Patients with Chronic Kidney Disease (DAPA-CKD). N Engl J Med. 2020;383:1436-1446; KDIGO 2024 Clinical Practice Guideline for CKD.",
    "doi_or_source": "10.1056/NEJMoa2024816",
    "clinical_evidence": "DAPA-CKD trial (n=4,304) demonstrated that in patients with eGFR 25-75 mL/min/1.73m² and urinary albumin-to-creatinine ratio (uACR) 200-5000 mg/g, Dapagliflozin reduced the composite risk of sustained ≥50% eGFR decline, end-stage kidney disease, or renal/CV death by 39% (HR 0.61; 95% CI 0.51-0.72; p<0.001). Benefits were consistent in non-diabetic CKD.",
    "solution_protocol": {
      "non_pharmacological_targets": "Dietary sodium restriction to <2.0 g/day (<5 g salt/day); adjusted protein intake (0.8 g/kg/day in non-dialysis CKD stage 3-5); avoid all nephrotoxic agents (NSAIDs, aminoglycosides, iodinated contrast where possible).",
      "monitoring_cadence": "Monitor eGFR and potassium within 2-4 weeks after initiating ACEi/ARB or SGLT2i. An initial eGFR dip of up to 30% is expected and hemodynamically reversible.",
      "clinical_thresholds": "Target blood pressure <120 mmHg systolic using standardized office measurement when tolerated."
    },
    "patient_plain_language": "Chronic kidney disease means your kidneys' microscopic filtering units are gradually scarred, reducing their ability to clean waste and excess fluid from your blood.",
    "doctor_consultation_checklist": {
      "parameter_question": "What are my current eGFR number and urine albumin (uACR) ratio, and what stage does that represent?",
      "safety_question": "Are there common over-the-counter pain medications like ibuprofen that could further injure my kidneys?",
      "action_threshold_question": "At what eGFR threshold should I establish formal care with a nephrology specialist?"
    },
    "red_flags": [
      "Severe shortness of breath, sudden widespread fluid retention, nausea, and metallic taste in mouth (Uremic symptoms)",
      "Serum potassium >6.0 mEq/L"
    ]
  },
  {
    "id": "DOC-CARD-017",
    "condition": "Benign Prostatic Hyperplasia (BPH)",
    "specialty": "Nephrology",
    "organ_system": "Genitourinary",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AUA / EAU",
    "citation": "Lerner LB et al. Management of Lower Urinary Tract Symptoms Attributed to Benign Prostatic Hyperplasia: AUA Guideline. J Urol. 2021;206(4):806-817.",
    "doi_or_source": "10.1097/JU.0000000000002183",
    "clinical_evidence": "AUA guidelines recommend alpha-1 adrenergic antagonists (Tamsulosin, Alfuzosin) for rapid relief of lower urinary tract symptoms (IPSS improvement 4-6 points). 5-alpha reductase inhibitors (Finasteride, Dutasteride) are indicated for enlarged prostates (>30 cc), reducing prostate volume by ~25% and long-term risk of acute urinary retention and surgery by 50% (MTOPS Trial, NEJM).",
    "solution_protocol": {
      "non_pharmacological_targets": "Fluid intake reduction in the 2-3 hours before bedtime; moderation of caffeine and alcohol intake; avoidance of decongestants and first-generation antihistamines which precipitate urinary retention.",
      "monitoring_cadence": "Reassess symptoms using validated International Prostate Symptom Score (IPSS) questionnaire at 4-12 weeks following therapy initiation.",
      "clinical_thresholds": "Post-void residual (PVR) volume evaluation via bladder ultrasound; PVR >200-300 mL requires urological review."
    },
    "patient_plain_language": "BPH is a non-cancerous enlargement of the prostate gland that surrounds the urethra, squeezing the tube like a thumb on a garden hose and making it harder to empty the bladder.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my IPSS symptom score, and did my bladder scan show significant leftover urine after voiding?",
      "safety_question": "Do my cold and allergy pills contain ingredients that could suddenly stop me from being able to urinate?",
      "action_threshold_question": "If medications do not relieve my nighttime waking, what minimally invasive procedures are options for me?"
    },
    "red_flags": [
      "Complete inability to pass urine despite an agonizingly full bladder (Acute Urinary Retention)",
      "Visible blood in urine or high fever with painful urination"
    ]
  },
  {
    "id": "DOC-CARD-018",
    "condition": "Uncomplicated Urinary Tract Infection (Cystitis)",
    "specialty": "Infectious Disease",
    "organ_system": "Genitourinary",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "IDSA / ESCMID",
    "citation": "Gupta K et al. International Clinical Practice Guidelines for the Treatment of Acute Uncomplicated Cystitis and Pyelonephritis in Women. Clin Infect Dis. 2011;52(5):e103-e120 (Reaffirmed 2023).",
    "doi_or_source": "10.1093/cid/ciq257",
    "clinical_evidence": "First-line empirical treatments with minimal resistance and collateral damage: Nitrofurantoin monohydrate/macrocrystals (100 mg BID for 5 days), Trimethoprim-sulfamethoxazole (160/800 mg BID for 3 days if local resistance <20%), or Fosfomycin trometamol (3 g single dose). Fluoroquinolones (Ciprofloxacin) must be avoided for uncomplicated cystitis due to disabling adverse events and resistance.",
    "solution_protocol": {
      "non_pharmacological_targets": "Increased daily water intake (additional 1.5 L/day proven in JAMA Internal Medicine RCT to reduce recurrent UTI by 48%); post-coital voiding; wipe front-to-back hygiene education.",
      "monitoring_cadence": "Follow-up required only if symptoms do not resolve within 48 hours of starting treatment or if symptoms recur within 2 weeks.",
      "clinical_thresholds": "Urine culture and antimicrobial susceptibility testing indicated in recurrent cases, atypical symptoms, or suspected pyelonephritis."
    },
    "patient_plain_language": "A bladder infection occurs when bacteria from nearby skin enter the urinary tract and multiply, causing inflammation that makes urinating feel burning and urgent.",
    "doctor_consultation_checklist": {
      "parameter_question": "Was a urine culture sent to the lab to verify that the bacteria is sensitive to my specific treatment?",
      "safety_question": "How many days should I expect burning to continue before we suspect the infection is resistant?",
      "action_threshold_question": "What warning signs would tell me the infection might be moving upward toward my kidneys?"
    },
    "red_flags": [
      "High fever, shaking chills, severe lower back or flank pain, and vomiting (Signs of Acute Pyelonephritis)"
    ]
  },
  {
    "id": "DOC-CARD-019",
    "condition": "Gastroesophageal Reflux Disease (GERD)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACG",
    "citation": "Katz PO et al. ACG Clinical Guideline for the Diagnosis and Management of Gastroesophageal Reflux Disease. Am J Gastroenterol. 2022;117(1):27-56.",
    "doi_or_source": "10.14309/ajg.0000000000001538",
    "clinical_evidence": "Proton Pump Inhibitors (PPIs) are the most effective therapy for erosive esophagitis healing (healing rates >80-90% vs. 50% with H2RAs). Guidelines recommend an 8-week course of once-daily PPI taken 30-60 minutes before the first meal of the day. Routine long-term high-dose therapy without objective confirmation or severe erosive disease is discouraged; deprescribing trials to the lowest effective dose are recommended.",
    "solution_protocol": {
      "non_pharmacological_targets": "Weight loss for overweight/obese patients; elevation of the head of the bed (6-8 inches) using bed risers or foam wedges; avoidance of late evening meals within 2-3 hours of lying flat; selective elimination of personal trigger foods (chocolate, caffeine, acidic foods).",
      "monitoring_cadence": "Assess symptom relief at 4 and 8 weeks; attempt step-down to as-needed H2RA or antacids if symptoms fully resolve.",
      "clinical_thresholds": "Upper endoscopy indicated for patients with alarm symptoms or non-responders to 8 weeks of twice-daily PPI therapy."
    },
    "patient_plain_language": "Acid reflux occurs when the muscular valve between your food pipe and stomach doesn't close tightly, allowing harsh stomach acid to splash back up into the sensitive esophagus.",
    "doctor_consultation_checklist": {
      "parameter_question": "How long should I remain on this medication before we attempt tapering down to a lower maintenance dose?",
      "safety_question": "Does my morning acid blocker need to be timed precisely before my first meal to work properly?",
      "action_threshold_question": "What symptoms would indicate that I need an upper endoscopy camera test?"
    },
    "red_flags": [
      "Difficulty swallowing (food feeling stuck in the chest/dysphagia)",
      "Painful swallowing (odynophagia), vomiting blood, or unexplained weight loss"
    ]
  },
  {
    "id": "DOC-CARD-020",
    "condition": "Irritable Bowel Syndrome (IBS)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACG",
    "citation": "Lacy BE et al. ACG Clinical Guideline: Management of Irritable Bowel Syndrome. Am J Gastroenterol. 2021;116(1):17-44.",
    "doi_or_source": "10.14309/ajg.0000000000001036",
    "clinical_evidence": "Diagnosis based on Rome IV criteria (recurrent abdominal pain ≥1 day/week associated with defecation or change in stool frequency/appearance). High-quality evidence supports soluble fiber (psyllium) over insoluble fiber (bran) (RR 0.79 for symptom persistence). A limited-time Low-FODMAP diet trial improves global symptoms (Grade conditional). Gut-directed hypnotherapy and neuromodulators (TCAs) exhibit strong NNT (NNT=4) for pain reduction via gut-brain axis modulation.",
    "solution_protocol": {
      "non_pharmacological_targets": "Structured 3-phase Low-FODMAP diet protocol (Restriction for 2-6 weeks, structured Reintroduction, Personalization) guided by a specialized GI dietitian; gut-directed cognitive behavioral therapy (CBT) or hypnotherapy.",
      "monitoring_cadence": "Evaluate clinical response 4-6 weeks after dietary or neuromodulator modifications.",
      "clinical_thresholds": "Serologic screening for Celiac Disease (tTG-IgA) and fecal calprotectin testing (<50 μg/g rules out IBD) mandatory prior to diagnosing IBS."
    },
    "patient_plain_language": "IBS is a disorder of the gut-brain connection where your intestines have become hypersensitive, causing abdominal cramping, bloating, diarrhea, or constipation without visible tissue damage.",
    "doctor_consultation_checklist": {
      "parameter_question": "Have we ruled out Celiac disease and inflammatory bowel disease with blood and stool lab checks?",
      "safety_question": "How long should I stay on a restrictive Low-FODMAP diet before systematically testing which foods trigger me?",
      "action_threshold_question": "Could gut-directed therapy or gut-brain nerve medications help calm my abdominal hypersensitivity?"
    },
    "red_flags": [
      "Unintentional weight loss, chronic nocturnal diarrhea that wakes you from sleep, or rectal bleeding"
    ]
  },
  {
    "id": "DOC-CARD-021",
    "condition": "Helicobacter pylori Infection",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline & Consensus",
    "source_body": "ACG & Maastricht VI",
    "citation": "Chey WD et al. ACG Clinical Guideline: Treatment of Helicobacter pylori Infection. Am J Gastroenterol. 2017;112(2):212-239; Malfertheiner P et al. Maastricht VI/Florence Consensus. Gut. 2022;71:1724-1762.",
    "doi_or_source": "10.1136/gutjnl-2022-327777",
    "clinical_evidence": "Due to clarithromycin resistance exceeding 15-20% globally, 14-day Bismuth Quadruple Therapy (PPI + Bismuth subsalicylate + Metronidazole + Tetracycline) is the first-line treatment regimen, achieving eradication rates >85-90%. Clarithromycin triple therapy is now restricted only to regions with proven local resistance <15%. Eradication significantly reduces peptic ulcer recurrence and gastric cancer risk.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict compliance counseling (completing full 14 days without missing doses is the primary determinant of cure); avoidance of NSAIDs and alcohol during eradication.",
      "monitoring_cadence": "Mandatory test-of-cure testing at least 4 weeks post-antimicrobial therapy and at least 2 weeks after stopping PPIs.",
      "clinical_thresholds": "Post-treatment verification performed via Urea Breath Test (UBT), stool antigen test, or endoscopy biopsy. Serology antibody tests cannot be used for cure confirmation."
    },
    "patient_plain_language": "H. pylori is a tough spiral-shaped bacteria that burrows into the mucous lining of your stomach, causing ulcers and long-term inflammation that must be cleared with a multi-step regimen.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is the regimen we are choosing a 14-day bismuth-based quadruple therapy to overcome antibiotic resistance?",
      "safety_question": "How many weeks after finishing all pills must I wait before taking my breath or stool test of cure?",
      "action_threshold_question": "Do I need to temporarily stop my heartburn acid medications before taking my verification test?"
    },
    "red_flags": [
      "Vomiting dark material that looks like coffee grounds, or passing black, foul-smelling stools"
    ]
  },
  {
    "id": "DOC-CARD-022",
    "condition": "Celiac Disease",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACG",
    "citation": "Rubio-Tapia A et al. ACG Clinical Guidelines: Diagnosis and Management of Celiac Disease. Am J Gastroenterol. 2023;118(1):59-76.",
    "doi_or_source": "10.14309/ajg.0000000000002075",
    "clinical_evidence": "Primary diagnosis requires serologic IgA tissue transglutaminase (tTG-IgA) testing with concurrent total IgA levels to rule out IgA deficiency. Confirmation in adults requires duodenal biopsy demonstrating intraepithelial lymphocytosis and villous atrophy (Marsh criteria). The only proven treatment is strict, lifelong adherence to a gluten-free diet (GFD), resulting in histological mucosal healing and prevention of lymphoma.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict elimination of all dietary gluten sources (wheat, rye, barley); consultation with an expert celiac clinical dietitian; education on preventing food cross-contamination in home kitchens.",
      "monitoring_cadence": "Serologic tTG-IgA antibody monitoring at 6 and 12 months post-GFD initiation, then annually to evaluate dietary compliance and intestinal healing.",
      "clinical_thresholds": "Patients must maintain an active, gluten-containing diet prior to diagnostic testing to avoid false-negative serologies and biopsies."
    },
    "patient_plain_language": "Celiac disease is an autoimmune condition where eating gluten (a protein in wheat, rye, and barley) triggers your immune system to attack and flatten the tiny finger-like villi in your small intestine that absorb nutrients.",
    "doctor_consultation_checklist": {
      "parameter_question": "Was my total IgA level checked alongside my tTG-IgA antibody test to ensure accurate lab results?",
      "safety_question": "Have we checked my baseline bone density (DEXA scan) and screened for iron and vitamin D deficiencies?",
      "action_threshold_question": "If my antibody levels stay elevated on a gluten-free diet, how do we identify hidden gluten sources?"
    },
    "red_flags": [
      "Severe malabsorption with rapid unexplained weight loss, fluid retention, or debilitating bone pain"
    ]
  },
  {
    "id": "DOC-CARD-023",
    "condition": "Major Depressive Disorder (MDD)",
    "specialty": "Psychiatry",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Comprehensive Network Meta-Analysis",
    "source_body": "The Lancet",
    "citation": "Cipriani A et al. Comparative Efficacy and Acceptability of 21 Antidepressant Drugs for the Acute Treatment of Adults with Major Depressive Disorder: A Systematic Review and Network Meta-Analysis. Lancet. 2018;391(10128):1357-1366.",
    "doi_or_source": "10.1016/S0140-6736(17)32802-7",
    "clinical_evidence": "Analysis of 522 RCTs (n=116,477) established that all 21 antidepressants were more effective than placebo (ORs 1.37 to 2.13). Escitalopram, Sertraline, Vortioxetine, and Agomelatine showed favorable balance of high response rates and lowest discontinuation rates. Combination of pharmacotherapy and evidence-based psychotherapy (CBT) achieves superior remission rates compared to either alone in moderate-to-severe depression.",
    "solution_protocol": {
      "non_pharmacological_targets": "Cognitive Behavioral Therapy (CBT), Behavioral Activation, or Interpersonal Psychotherapy (IPT); structured physical exercise (moderate intensity 3-5 times/week); sleep hygiene stabilization.",
      "monitoring_cadence": "Assess suicide risk and treatment tolerability at 1-2 weeks; assess clinical response at 4-6 weeks using validated score (PHQ-9).",
      "clinical_thresholds": "Full therapeutic trial requires minimum 6-8 weeks at therapeutic dose before determining treatment non-responsiveness or switching classes."
    },
    "patient_plain_language": "Major depression is a medical illness involving imbalances in brain circuits and neurotransmitters that affect your mood, energy, sleep, and outlook, not a character weakness.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my baseline score on the PHQ-9 depression scale, and what drop indicates progress?",
      "safety_question": "How many weeks will it take before I feel the full emotional and energy benefits of my therapy?",
      "action_threshold_question": "What is our plan for pairing counseling or cognitive therapy alongside medical treatment?"
    },
    "red_flags": [
      "Thoughts of self-harm, wanting to die, or formulating a suicide plan (Immediate Crisis Intercept: 988 / 112 / 911)"
    ]
  },
  {
    "id": "DOC-CARD-024",
    "condition": "Generalized Anxiety Disorder (GAD)",
    "specialty": "Psychiatry",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "NICE",
    "citation": "National Institute for Health and Care Excellence. Generalised Anxiety Disorder and Panic Disorder in Adults: Management (Clinical Guideline CG113). NICE. 2011 (Reaffirmed 2024).",
    "doi_or_source": "https://www.nice.org.uk/guidance/cg113",
    "clinical_evidence": "NICE stepped-care model recommends low-intensity psychological interventions first for mild symptoms, followed by high-intensity CBT or SSRIs (Sertraline first-line cost-effective choice) for persistent GAD. Benzodiazepines should not be used except for short-term crisis management (<2-4 weeks) due to rapid tolerance, dependence, and cognitive side effects.",
    "solution_protocol": {
      "non_pharmacological_targets": "Individual CBT (12-15 weekly sessions); progressive muscle relaxation; mindfulness-based stress reduction; caffeine reduction/elimination.",
      "monitoring_cadence": "Review clinical progress at 4, 8, and 12 weeks using GAD-7 scoring.",
      "clinical_thresholds": "GAD-7 score: 5-9 mild, 10-14 moderate, ≥15 severe anxiety."
    },
    "patient_plain_language": "Generalized anxiety disorder is when your brain’s alarm system gets stuck in overdrive, causing persistent, uncontrollable worry about everyday situations alongside physical tension.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current GAD-7 anxiety score, and what does it indicate about severity?",
      "safety_question": "Why are non-habit-forming medicines and CBT preferred over fast-acting tranquilizer pills for long-term health?",
      "action_threshold_question": "How can I access evidence-based cognitive behavioral therapy while starting medication?"
    },
    "red_flags": [
      "Sudden disabling panic attacks preventing basic daily functioning",
      "Co-occurring severe depressive thoughts or suicidal ideation"
    ]
  },
  {
    "id": "DOC-CARD-025",
    "condition": "Chronic Migraine",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline & Meta-Analysis",
    "source_body": "AHS & The Lancet Neurology",
    "citation": "Ailani J et al. The American Headache Society Consensus Statement: Update on Integrating New Migraine Treatments into Clinical Practice. Headache. 2021;61(7):1021-1039.",
    "doi_or_source": "10.1111/head.14153",
    "clinical_evidence": "Defined as ≥15 headache days/month for >3 months, with ≥8 days meeting migraine criteria. Calcitonin Gene-Related Peptide (CGRP) monoclonal antibodies (Erenumab, Fremanezumab, Galcanezumab) and OnabotulinumtoxinA significantly reduce monthly migraine days by 4-6 days (NNT=3-4). Acute therapy relies on triptans or gepants. Limiting acute medications is essential to prevent medication-overuse headache (MOH).",
    "solution_protocol": {
      "non_pharmacological_targets": "Structured headache diary maintenance; consistent sleep schedule; regular meals avoiding hypoglycemic dips; identification of specific dietary triggers; aerobic exercise.",
      "monitoring_cadence": "Monthly headache day tracking; evaluate preventive efficacy after a minimum 3-month trial (6 months for Botox).",
      "clinical_thresholds": "Medication-Overuse Headache prevention rule: Limit triptans and combination analgesics to <10 days/month, and simple analgesics to <15 days/month."
    },
    "patient_plain_language": "Migraine is not just a bad headache; it is a neurological event where waves of nerve sensitivity and swelling around blood vessels in your brain cause throbbing pain, nausea, and light sensitivity.",
    "doctor_consultation_checklist": {
      "parameter_question": "How many days per month do my headaches qualify me for preventive migraine therapies?",
      "safety_question": "Could taking over-the-counter pain relievers too often be causing rebound 'medication-overuse' headaches?",
      "action_threshold_question": "Am I a candidate for targeted preventive therapies like CGRP inhibitors or Botox?"
    },
    "red_flags": [
      "Thunderclap headache: Sudden severe headache reaching maximum intensity within one minute (Subarachnoid Hemorrhage)",
      "Headache accompanied by fever, stiff neck, confusion, or weakness on one side of the body"
    ]
  },
  {
    "id": "DOC-CARD-026",
    "condition": "Chronic Insomnia",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACP",
    "citation": "Qaseem A et al. Management of Chronic Insomnia Disorder in Adults: A Clinical Practice Guideline From the American College of Physicians. Ann Intern Med. 2016;165(2):125-133 (Reaffirmed 2023).",
    "doi_or_source": "10.7326/M15-2175",
    "clinical_evidence": "The ACP strongly recommends that all adult patients receive Cognitive Behavioral Therapy for Insomnia (CBT-I) as the initial treatment for chronic insomnia disorder (Grade: strong recommendation, high-quality evidence). CBT-I demonstrates superior sustained efficacy compared to sleep medications without risks of tolerance, rebound insomnia, or falls.",
    "solution_protocol": {
      "non_pharmacological_targets": "Multicomponent CBT-I protocol: Stimulus Control (bed only for sleep and intimacy; get out of bed if awake after 20 minutes), Sleep Restriction Therapy, cognitive restructuring of sleep worries, sleep hygiene optimization (cool dark room, eliminate screens 1 hour before bed).",
      "monitoring_cadence": "Daily sleep diary tracking (sleep latency, wake after sleep onset, total sleep time, sleep efficiency) over a 6-8 week intervention.",
      "clinical_thresholds": "Target sleep efficiency: >85% (Total Sleep Time / Total Time in Bed x 100)."
    },
    "patient_plain_language": "Chronic insomnia is when difficulty falling or staying asleep becomes a habitual pattern where your brain associates the bed with anxiety and wakefulness rather than rest.",
    "doctor_consultation_checklist": {
      "parameter_question": "How can I get enrolled in structured Cognitive Behavioral Therapy for Insomnia (CBT-I)?",
      "safety_question": "Why do major medical guidelines recommend therapy techniques over sleeping pills as the first choice?",
      "action_threshold_question": "How should I keep a two-week sleep diary to track my actual sleep efficiency?"
    },
    "red_flags": [
      "Falling asleep unexpectedly during active tasks like driving or operating equipment"
    ]
  },
  {
    "id": "DOC-CARD-027",
    "condition": "Early Alzheimer's Disease & Mild Cognitive Impairment",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (Clarity AD)",
    "citation": "van Dyck CH et al. Lecanemab in Early Alzheimer's Disease (Clarity AD). N Engl J Med. 2023;388:9-21.",
    "doi_or_source": "10.1056/NEJMoa2212948",
    "clinical_evidence": "In 1,795 patients with early Alzheimer's disease and confirmed amyloid pathology, Lecanemab (anti-amyloid protofibril antibody) reduced clinical decline on the Clinical Dementia Rating-Sum of Boxes (CDR-SB) by 27% at 18 months compared to placebo (difference -0.45; p<0.001). Amyloid-related imaging abnormalities (ARIA-E edema in 12.6%, ARIA-H microhemorrhages in 17.3%) necessitate rigorous MRI safety surveillance.",
    "solution_protocol": {
      "non_pharmacological_targets": "Rigorous cardiovascular risk factor management (blood pressure, diabetes, lipids); regular physical aerobic exercise; Mediterranean-DASH Intervention for Neurodegenerative Delay (MIND diet); cognitive engagement programs; caregiver support systems.",
      "monitoring_cadence": "Brain MRI safety surveillance at baseline, and prior to 5th, 7th, and 14th infusions to detect asymptomatic ARIA.",
      "clinical_thresholds": "ApoE epsilon 4 genotyping required prior to monoclonal therapy to evaluate ARIA risk (homozygotes carry highest risk)."
    },
    "patient_plain_language": "Alzheimer's disease involves the slow buildup of abnormal protein plaques and tangles in the brain, which gradually disrupt how brain cells communicate with each other, affecting memory and thinking.",
    "doctor_consultation_checklist": {
      "parameter_question": "What baseline cognitive tests (such as MoCA) and biomarker scans have confirmed my diagnosis?",
      "safety_question": "If considering anti-amyloid infusion therapies, what are the safety risks seen on brain MRI scans?",
      "action_threshold_question": "What community and cognitive resources can our family put in place now to plan ahead?"
    },
    "red_flags": [
      "Sudden rapid confusion developing over hours or days (indicates acute delirium, infection, or medication reaction)",
      "Unexplained focal neurological weakness or sudden visual changes"
    ]
  },
  {
    "id": "DOC-CARD-028",
    "condition": "Rheumatoid Arthritis (RA)",
    "specialty": "Rheumatology",
    "organ_system": "Musculoskeletal / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACR / EULAR",
    "citation": "Fraenkel L et al. 2021 American College of Rheumatology Guideline for the Treatment of Rheumatoid Arthritis. Arthritis Rheumatol. 2021;73(7):1108-1123.",
    "doi_or_source": "10.1002/art.41752",
    "clinical_evidence": "Guidelines strongly advocate a 'Treat-to-Target' strategy aiming for clinical remission or low disease activity. Methotrexate monotherapy is strongly recommended as first-line conventional synthetic DMARD over other csDMARDs or biologics. If disease activity remains moderate or high despite optimized oral/subcutaneous MTX, adding a biologic DMARD (TNF inhibitor) or targeted synthetic DMARD is recommended.",
    "solution_protocol": {
      "non_pharmacological_targets": "Joint-protective low-impact aerobic exercise and resistance training; hand therapy / occupational splinting; anti-inflammatory dietary emphasis; complete smoking cessation (smoking reduces MTX efficacy and worsens joint erosion).",
      "monitoring_cadence": "Monthly disease activity measurement (CDAI, SDAI, or DAS28) until remission/target is met; routine safety monitoring of CBC, ALT/AST, and creatinine every 8-12 weeks.",
      "clinical_thresholds": "Target: CDAI score ≤2.8 (remission) or ≤10 (low disease activity)."
    },
    "patient_plain_language": "Rheumatoid arthritis is an autoimmune condition where your immune system mistakenly attacks the lining of your joints (synovium), causing painful swelling that can damage bone over time if not calmed.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current clinical disease activity score (like CDAI), and are we aiming for full remission?",
      "safety_question": "What lab tests are being run to protect my liver and bone marrow while on disease-modifying therapy?",
      "action_threshold_question": "If morning joint stiffness lasts longer than one hour, does that mean my treatment needs adjustment?"
    },
    "red_flags": [
      "High fever and a single hot, severely swollen, red joint (Possible Septic Arthritis emergency)",
      "Numbness, tingling, or weakness in hands or feet (Vasculitis/neuropathy warning)"
    ]
  },
  {
    "id": "DOC-CARD-029",
    "condition": "Knee & Hip Osteoarthritis",
    "specialty": "Rheumatology",
    "organ_system": "Musculoskeletal",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "OARSI & ACR",
    "citation": "Bannuru RR et al. OARSI Guidelines for the Non-Surgical Management of Knee, Hip, and Polyarticular Osteoarthritis. Osteoarthritis Cartilage. 2019;27(11):1578-1589.",
    "doi_or_source": "10.1016/j.joca.2019.06.011",
    "clinical_evidence": "Core treatments strongly recommended for all individuals: structured land-based exercise, dietary weight management, and disease education. Topical NSAIDs (Diclofenac gel) are strongly recommended as first-line pharmacotherapy for knee OA due to equivalent analgesia to oral NSAIDs with minimal systemic adverse events. Oral opioids are strongly recommended against due to lack of long-term benefit and high toxicity.",
    "solution_protocol": {
      "non_pharmacological_targets": "Weight loss target of ≥5-10% in overweight patients (significantly reduces compressive knee joint loading forces by 4-fold); low-impact quadriceps strengthening, cycling, or aquatic exercise; assistive walking canes in contralateral hand.",
      "monitoring_cadence": "Reassess pain and joint function (WOMAC score) at 6-12 weeks following exercise program initiation.",
      "clinical_thresholds": "Total joint arthroplasty referral reserved for advanced structural joint damage with intractable pain and loss of independent mobility despite conservative therapy."
    },
    "patient_plain_language": "Osteoarthritis is a mechanical wear-and-repair process where the protective cartilage cushioning the ends of your bones gradually thins, causing stiffness and aching when moving.",
    "doctor_consultation_checklist": {
      "parameter_question": "How can physical therapy help strengthen the muscles around my joint to absorb walking impact?",
      "safety_question": "Why are topical anti-inflammatory skin gels safer for my stomach and heart than oral pain pills?",
      "action_threshold_question": "At what point in my mobility decline should I meet with an orthopedic surgeon to discuss joint replacement?"
    },
    "red_flags": [
      "Sudden inability to bear weight on the leg",
      "Joint becoming suddenly red, hot to the touch, and severely swollen"
    ]
  },
  {
    "id": "DOC-CARD-030",
    "condition": "Gout & Hyperuricemia",
    "specialty": "Rheumatology",
    "organ_system": "Musculoskeletal / Metabolic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACR",
    "citation": "FitzGerald JD et al. 2020 American College of Rheumatology Guideline for the Management of Gout. Arthritis Care Res. 2020;72(6):744-760.",
    "doi_or_source": "10.1002/acr.24380",
    "clinical_evidence": "Strong recommendation for a Treat-to-Target urate-lowering strategy. Allopurinol is the preferred first-line xanthine oxidase inhibitor. Indications for urate-lowering therapy (ULT): ≥1 subcutaneous tophi, radiographic damage, or ≥2 flares/year. Starting ULT at low dose (Allopurinol ≤100 mg/day, lower in CKD) and titrating upward to achieve target serum urate prevents mobilization flares.",
    "solution_protocol": {
      "non_pharmacological_targets": "Limiting intake of purine-rich foods (organ meats, shellfish), high-fructose corn syrup, and alcohol (especially beer); maintaining adequate daily water hydration; weight loss in overweight individuals.",
      "monitoring_cadence": "Serum urate testing every 2-5 weeks during titration until target is reached, then every 6 months. Concomitant anti-inflammatory flare prophylaxis (Colchicine 0.5-0.6 mg daily) for 3-6 months when initiating ULT.",
      "clinical_thresholds": "Serum urate target: <6.0 mg/dL (<360 μmol/L) for all patients (<5.0 mg/dL if tophi present) to ensure crystal dissolution."
    },
    "patient_plain_language": "Gout occurs when high levels of uric acid form sharp needle-like microscopic crystals in your joints (often the big toe), triggering intense, sudden pain and swelling.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my exact blood uric acid number, and are we below our goal of 6.0 mg/dL?",
      "safety_question": "Do I have flare-prevention medication (like low-dose colchicine) on hand while we slowly increase my uric-acid-lowering dose?",
      "action_threshold_question": "Should we test for the HLA-B*5801 gene before starting allopurinol if I am of Asian or African ancestry?"
    },
    "red_flags": [
      "High fever and chills accompanied by an excruciatingly swollen joint (Must rule out joint infection)"
    ]
  },
  {
    "id": "DOC-CARD-031",
    "condition": "Chronic Non-Specific Lower Back Pain",
    "specialty": "Rheumatology",
    "organ_system": "Musculoskeletal",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACP & The Lancet Series",
    "citation": "Qaseem A et al. Noninvasive Treatments for Acute, Subacute, and Chronic Low Back Pain: A Clinical Practice Guideline From the American College of Physicians. Ann Intern Med. 2017;166(7):514-530.",
    "doi_or_source": "10.7326/M16-2367",
    "clinical_evidence": "ACP guidelines recommend that clinicians and patients initially select nonpharmacological treatment with exercise, multidisciplinary rehabilitation, acupuncture, mindfulness-based stress reduction, or spinal manipulation (Grade: strong recommendation). Pharmacological therapy is secondary (NSAIDs first-line, Duloxetine second-line). Routine MRI imaging is strongly discouraged without red flags as it increases surgery rates without improving clinical outcomes.",
    "solution_protocol": {
      "non_pharmacological_targets": "Active physical therapy focusing on core stabilization, directional preference exercises, and graded active movement; avoidance of prolonged bed rest; cognitive behavioral approaches to address fear-avoidance behaviors.",
      "monitoring_cadence": "Reassess functional disability (Oswestry Disability Index [ODI] or Roland-Morris questionnaire) at 4-6 weeks.",
      "clinical_thresholds": "Imaging only indicated if pain persists >6 weeks with no response to therapy or if progressive neurological deficits appear."
    },
    "patient_plain_language": "Most lower back pain is related to muscle strain, ligament tension, and spinal disc irritation. Resting in bed actually delays recovery; gentle, steady movement is the best medicine for healing.",
    "doctor_consultation_checklist": {
      "parameter_question": "Why is an immediate MRI scan unnecessary if I do not have red-flag nerve symptoms?",
      "safety_question": "What specific active exercises or physical therapy routines are safest for my recovery?",
      "action_threshold_question": "What neurological symptoms (like leg weakness or numbness) require urgent evaluation?"
    },
    "red_flags": [
      "Loss of bowel or bladder control, or numbness around the groin/buttocks (Saddle Anesthesia: Cauda Equina Syndrome)",
      "New progressive weakness lifting your foot (Foot Drop)",
      "Unexplained fever and severe back pain in an immunocompromised individual"
    ]
  },
  {
    "id": "DOC-CARD-032",
    "condition": "Postmenopausal Osteoporosis",
    "specialty": "Endocrinology",
    "organ_system": "Skeletal",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "Endocrine Society",
    "citation": "Eastell R et al. Pharmacological Management of Osteoporosis in Postmenopausal Women: An Endocrine Society Clinical Practice Guideline. J Clin Endocrinol Metab. 2019;104(5):1595-1622.",
    "doi_or_source": "10.1210/jc.2019-00221",
    "clinical_evidence": "Guidelines recommend initial treatment with oral bisphosphonates (Alendronate, Risedronate) or IV Zoledronic acid for postmenopausal women at high risk of fractures, reducing vertebral fractures by ~50-70% and hip fractures by ~40% (FIT and HORIZON trials). In women at very high risk (T-score <-3.0 or prior fracture), an anabolic regimen (Teriparatide, Romosozumab) followed by antiresorptive therapy is recommended.",
    "solution_protocol": {
      "non_pharmacological_targets": "Daily total calcium intake of 1,200 mg (via diet preferred); Vitamin D3 supplementation to maintain serum 25(OH)D levels >30 ng/mL; weight-bearing and resistance exercises; home fall-prevention evaluation (removing tripping hazards, grab bars).",
      "monitoring_cadence": "DEXA scan every 1-2 years to evaluate bone mineral density response; consider bisphosphonate 'drug holiday' reassessment after 3-5 years of therapy.",
      "clinical_thresholds": "Osteoporosis defined by DEXA T-score ≤-2.5 at femoral neck or lumbar spine, or FRAX 10-year major osteoporotic fracture risk ≥20% / hip fracture risk ≥3%."
    },
    "patient_plain_language": "Osteoporosis is a silent thinning of your bones where bone tissue breaks down faster than it rebuilds, making your bones porous like a sponge and more vulnerable to fractures from minor falls.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my lowest DEXA T-score, and what is my calculated 10-year FRAX fracture probability?",
      "safety_question": "How should I position myself (sitting upright for 30 minutes) when taking morning bisphosphonate pills to protect my esophagus?",
      "action_threshold_question": "What balance exercises and physical therapy can I start to prevent accidental trips and falls?"
    },
    "red_flags": [
      "Sudden severe middle or lower back pain after bending or lifting (Signs of an acute vertebral compression fracture)"
    ]
  },
  {
    "id": "DOC-CARD-033",
    "condition": "Menopausal Vasomotor Symptoms & Hormone Therapy",
    "specialty": "Women's Health",
    "organ_system": "Endocrine / Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Position Statement & 20-Year RCT Follow-Up",
    "source_body": "The Menopause Society (NAMS) & JAMA",
    "citation": "The 2022/2023 Hormone Therapy Position Statement of The Menopause Society. Menopause. 2022;29(7):767-794; Manson JE et al. 20-Year Follow-up of WHI Trials. JAMA. 2024.",
    "doi_or_source": "10.1097/GME.0000000000002024",
    "clinical_evidence": "Systemic hormone therapy is the most effective treatment for vasomotor symptoms and the genitourinary syndrome of menopause. In women aged <60 years or within 10 years of menopause onset, the benefit-risk ratio is favorable for relief of hot flashes and fracture prevention without increased all-cause mortality. Women with an intact uterus require concurrent progestogen (e.g., micronized progesterone) to prevent endometrial cancer.",
    "solution_protocol": {
      "non_pharmacological_targets": "Layered breathable clothing; keeping ambient bedroom temperatures cool; avoidance of hot beverages, alcohol, and spicy foods; clinical hypnosis or cognitive behavioral therapy for hot flashes (Level 1 evidence for symptom reduction).",
      "monitoring_cadence": "Annual clinical reassessment of symptoms and risk profile (cardiovascular, breast, venous thromboembolism).",
      "clinical_thresholds": "Transdermal estradiol preferred over oral route in women with elevated baseline VTE risk, hypertension, or hypertriglyceridemia."
    },
    "patient_plain_language": "During perimenopause and menopause, your ovaries produce less estrogen, causing your brain's temperature control center to misfire and trigger sudden hot flashes and night sweats.",
    "doctor_consultation_checklist": {
      "parameter_question": "Am I within the standard 10-year window of menopause onset where hormone therapy benefits outweigh risks?",
      "safety_question": "If I still have my uterus, what type of progesterone will protect my uterine lining?",
      "action_threshold_question": "Are non-hormonal options (like NK3 receptor antagonists or SSRIs) appropriate for my symptom severity?"
    },
    "red_flags": [
      "Any unexpected vaginal bleeding occurring after menopause (Mandatory workup for endometrial pathology)"
    ]
  },
  {
    "id": "DOC-CARD-034",
    "condition": "Endometriosis & Chronic Pelvic Pain",
    "specialty": "Women's Health",
    "organ_system": "Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ESHRE",
    "citation": "Becker CM et al. ESHRE Guideline: Endometriosis. Hum Reprod Open. 2022;2022(2):hoac009.",
    "doi_or_source": "10.1093/hropen/hoac009",
    "clinical_evidence": "ESHRE guidelines recommend empirical medical treatment without requiring laparoscopic confirmation in patients with clinical suspicion. Combined oral contraceptives or progestogens (Dienogest 2 mg) are first-line hormonal therapies (Grade A). GnRH receptor antagonists (Elagolix, Relugolix; ELARIS trials, NEJM) significantly reduce dysmenorrhea and non-menstrual pelvic pain with add-back therapy to preserve bone density.",
    "solution_protocol": {
      "non_pharmacological_targets": "Pelvic floor physical therapy to address secondary pelvic myofascial pain and hypertonicity; transcutaneous electrical nerve stimulation (TENS); anti-inflammatory dietary approaches.",
      "monitoring_cadence": "Clinical symptom review at 3-6 months following initiation of hormonal suppression.",
      "clinical_thresholds": "Laparoscopic surgical excision indicated when medical treatment fails, when ovarian endometriomas >3 cm are present, or in deep infiltrating bowel/bladder disease."
    },
    "patient_plain_language": "Endometriosis occurs when tissue similar to the lining inside your uterus grows outside the womb on other pelvic organs, causing inflammation, scarring, and severe menstrual pain.",
    "doctor_consultation_checklist": {
      "parameter_question": "Can we start first-line hormonal symptom management without waiting for exploratory surgery?",
      "safety_question": "How will my treatment plan protect my fertility if I plan to become pregnant in the future?",
      "action_threshold_question": "Could pelvic floor physical therapy help relieve my deep chronic pelvic muscle tension?"
    },
    "red_flags": [
      "Acute, severe, one-sided pelvic pain with nausea and vomiting (Must rule out ovarian torsion or ruptured cyst)"
    ]
  },
  {
    "id": "DOC-CARD-035",
    "condition": "Preeclampsia Prevention & Management",
    "specialty": "Women's Health",
    "organ_system": "Cardiovascular / Placental",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Recommendation Statement & Practice Guideline",
    "source_body": "USPSTF & ACOG",
    "citation": "USPSTF. Aspirin Use to Prevent Preeclampsia and Related Morbidity and Mortality: Preventive Medication. JAMA. 2021;326(12):1185-1191; ACOG Practice Bulletin No. 222.",
    "doi_or_source": "10.1001/jama.2021.14781",
    "clinical_evidence": "The USPSTF and ACOG recommend low-dose aspirin (81-150 mg/day) prophylaxis initiated between 12 and 16 weeks of gestation (and continued until delivery) in pregnant individuals at high risk for preeclampsia (Grade B). Meta-analyses (ASPRE trial, NEJM) confirm low-dose aspirin reduces preterm preeclampsia by ~62% and intrauterine growth restriction by ~20%.",
    "solution_protocol": {
      "non_pharmacological_targets": "Frequent prenatal blood pressure monitoring; standardized protein-to-creatinine ratio (uPCR) testing; patient education on early symptom recognition.",
      "monitoring_cadence": "Weekly or bi-weekly prenatal blood pressure checks in high-risk pregnancies.",
      "clinical_thresholds": "Preeclampsia defined as BP ≥140/90 mmHg after 20 weeks gestation accompanied by proteinuria (uPCR ≥0.3 mg/mg) or new signs of end-organ dysfunction (thrombocytopenia, renal insufficiency, elevated transaminases)."
    },
    "patient_plain_language": "Preeclampsia is a pregnancy complication characterized by high blood pressure and signs of strain on other organs like kidneys and liver, typically appearing after 20 weeks of pregnancy.",
    "doctor_consultation_checklist": {
      "parameter_question": "Based on my medical history, should I take low-dose aspirin daily starting at 12-16 weeks?",
      "safety_question": "What blood pressure numbers should I look for when checking my blood pressure at home?",
      "action_threshold_question": "What subtle warning signs (like upper belly pain or visual changes) require an immediate trip to the maternity ward?"
    },
    "red_flags": [
      "Severe persistent headache unresponsive to acetaminophen",
      "Seeing spots, flashing lights, or sudden blurry vision",
      "Severe pain in the right upper belly beneath the ribs"
    ]
  },
  {
    "id": "DOC-CARD-036",
    "condition": "Gestational Diabetes Mellitus (GDM)",
    "specialty": "Women's Health",
    "organ_system": "Endocrine / Placental",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Practice Bulletin & Landmark Study",
    "source_body": "ACOG & HAPO Study",
    "citation": "ACOG Practice Bulletin No. 190: Gestational Diabetes Mellitus. Obstet Gynecol. 2018;131(2):e49-e64 (Reaffirmed 2023); HAPO Study Cooperative Research Group. N Engl J Med. 2008;358:1991-2002.",
    "doi_or_source": "10.1097/AOG.0000000000002501",
    "clinical_evidence": "HAPO study demonstrated strong, continuous linear associations between maternal glucose levels and adverse outcomes (birth weight >90th percentile, primary cesarean delivery, and neonatal hypoglycemia). First-line management is medical nutrition therapy and moderate exercise, which successfully manages 70-85% of GDM pregnancies. Insulin is the preferred first-line pharmacological treatment when glycemic goals are not met.",
    "solution_protocol": {
      "non_pharmacological_targets": "Individualized medical nutrition therapy emphasizing complex carbohydrates distributed across 3 meals and 2-3 snacks; post-prandial walking (15-30 minutes after meals improves glucose levels).",
      "monitoring_cadence": "Self-monitoring of blood glucose 4 times daily (fasting and 1 or 2 hours after each meal).",
      "clinical_thresholds": "ACOG Glycemic targets: Fasting blood glucose <95 mg/dL; 1-hour postprandial <140 mg/dL; or 2-hour postprandial <120 mg/dL."
    },
    "patient_plain_language": "Gestational diabetes is temporary high blood sugar that develops during pregnancy because placental hormones interfere with how your body uses its own insulin.",
    "doctor_consultation_checklist": {
      "parameter_question": "What are my daily fasting and post-meal blood sugar targets?",
      "safety_question": "How will we balance my diet to nourish baby's growth while keeping my blood sugar numbers flat?",
      "action_threshold_question": "When after delivery should I take my follow-up glucose test to confirm my blood sugar has returned to normal?"
    },
    "red_flags": [
      "Persistently elevated fasting blood glucose >110 mg/dL despite dietary management",
      "Sudden decrease in baby's regular movement patterns"
    ]
  },
  {
    "id": "DOC-CARD-037",
    "condition": "Pediatric Acute Otitis Media (AOM)",
    "specialty": "Pediatrics",
    "organ_system": "Otolaryngology",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAP",
    "citation": "Lieberthal AS et al. The Diagnosis and Management of Acute Otitis Media. Pediatrics. 2013;131(3):e964-e999 (Reaffirmed).",
    "doi_or_source": "10.1542/peds.2012-3488",
    "clinical_evidence": "AAP guidelines emphasize watchful waiting with initial pain management for 48-72 hours in children ≥2 years with uncomplicated unilateral AOM and mild symptoms, reducing unnecessary antibiotic exposure. When antibiotics are indicated (severe pain, fever ≥39°C, bilateral in children <2 years), high-dose Amoxicillin (80-90 mg/kg/day divided BID) is first-line to eradicate resistant Streptococcus pneumoniae.",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate, aggressive pain control using weight-based oral acetaminophen or ibuprofen; avoidance of secondhand tobacco smoke exposure; encouragement of breastfeeding; avoidance of bottle propping in bed.",
      "monitoring_cadence": "Mandatory clinical reassessment at 48-72 hours; if symptoms worsen or fail to improve, initiate antibiotic therapy or switch to Amoxicillin-Clavulanate.",
      "clinical_thresholds": "Diagnostic criteria require moderate-to-severe bulging of the tympanic membrane or new onset otorrhea not due to acute otitis externa."
    },
    "patient_plain_language": "An ear infection is inflammation and fluid trapped behind your child's eardrum, usually triggered by swelling from a common cold. Many mild ear infections resolve naturally with pain medicine.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my child an appropriate candidate for a 48-hour watchful waiting period with pain relievers before starting antibiotics?",
      "safety_question": "What is the exact weight-based dose of fever and pain medicine my child should take?",
      "action_threshold_question": "What ear symptoms or fever duration would indicate we need an immediate antibiotic prescription?"
    },
    "red_flags": [
      "Swelling, tenderness, and redness pushing the ear forward behind the ear bone (Mastoiditis)",
      "High fever accompanied by unusual lethargy, stiff neck, or extreme irritability"
    ]
  },
  {
    "id": "DOC-CARD-038",
    "condition": "Pediatric Asthma & Viral Wheeze",
    "specialty": "Pediatrics",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Global Evidence-Based Strategy",
    "source_body": "GINA",
    "citation": "Global Initiative for Asthma. Global Strategy for Asthma Management and Prevention (2024 Update): Section on Children 5 Years and Younger.",
    "doi_or_source": "https://ginasthma.org/reports/",
    "clinical_evidence": "For children ≤5 years with recurrent viral wheezing and intermittent symptoms, short-acting beta-2 agonists (SABA) via pressurized metered-dose inhaler (pMDI) with a valved holding chamber and mask are recommended. Daily controller therapy with low-dose inhaled corticosteroids (ICS) is indicated if symptom pattern is frequent (>3 episodes/year) or severe, significantly reducing exacerbation days and hospital admissions (CAMP study, NEJM).",
    "solution_protocol": {
      "non_pharmacological_targets": "Mandatory use of a spacer chamber with an appropriately sized face mask for all young children; elimination of indoor environmental tobacco smoke and wood smoke; avoidance of known pet or dust triggers.",
      "monitoring_cadence": "Clinical reassessment 4-6 weeks after initiating controller therapy; assess whether wheezing episodes are strictly viral or occur between colds.",
      "clinical_thresholds": "Step-down controller therapy should be considered once stability is maintained for 3 consecutive months."
    },
    "patient_plain_language": "In toddlers and young children, cold viruses can cause the small breathing tubes in their lungs to swell and whistle (wheeze), which is treated using inhalers with a clear spacer mask.",
    "doctor_consultation_checklist": {
      "parameter_question": "Can we practice using our spacer and mask in the clinic today to make sure my child gets the full dose?",
      "safety_question": "Does my child have purely viral-triggered wheeze or persistent asthma requiring daily maintenance?",
      "action_threshold_question": "What chest breathing retractions mean I need to bring my child to urgent care right away?"
    },
    "red_flags": [
      "Skin pulling in deeply between ribs or at the base of the neck with each breath (Severe retractions)",
      "Nostrils flaring, grunting sounds with breathing, or lips turning bluish"
    ]
  },
  {
    "id": "DOC-CARD-039",
    "condition": "Simple Febrile Seizures",
    "specialty": "Pediatrics",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAP",
    "citation": "Subcommittee on Febrile Seizures. Febrile Seizures: Guideline for the Neurodiagnostic Evaluation of the Child With a Simple Febrile Seizure. Pediatrics. 2011;127(2):389-394 (Reaffirmed).",
    "doi_or_source": "10.1542/peds.2010-3318",
    "clinical_evidence": "Simple febrile seizures (generalized, lasting <15 minutes, occurring once in 24 hours in a child aged 6-60 months) carry no increased risk of long-term neurological damage, intellectual disability, or significant epilepsy risk compared to the general population. Routine EEG, brain CT/MRI, and routine lumbar puncture are not recommended in well-appearing, fully immunized children with simple febrile seizures.",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate parent education: During a seizure, gently place child on their side (recovery position) on a soft surface, do not restrain them, never place anything in their mouth, time the duration; antipyretics provide comfort but do not prevent seizure recurrence.",
      "monitoring_cadence": "Identify and treat the underlying source of fever (viral URI, otitis media, roseola).",
      "clinical_thresholds": "Complex febrile seizure defined if focal features exist, duration >15 minutes, or recurs within 24 hours (requires thorough neurological evaluation)."
    },
    "patient_plain_language": "A simple febrile seizure is a brief, harmless convulsion triggered by a sudden spike in body temperature in young children whose developing brains are sensitive to rapid fever changes.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my child's seizure fit all the criteria of a 'simple' febrile seizure?",
      "safety_question": "What should I do immediately at home if a seizure ever happens again during a fever?",
      "action_threshold_question": "At what seizure time duration should I immediately call 911/emergency services?"
    },
    "red_flags": [
      "Seizure lasting longer than 5 minutes continuously (Call emergency services immediately)",
      "Child remains unusually unresponsive or has extreme neck stiffness after the post-seizure sleepiness clears"
    ]
  },
  {
    "id": "DOC-CARD-040",
    "condition": "Pediatric Attention-Deficit/Hyperactivity Disorder (ADHD)",
    "specialty": "Pediatrics",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline & Landmark RCT",
    "source_body": "AAP & MTA Study",
    "citation": "Wolraich ML et al. Clinical Practice Guideline for the Diagnosis, Evaluation, and Treatment of ADHD in Children and Adolescents. Pediatrics. 2019;144(4):e20192528; MTA Cooperative Group. Arch Gen Psychiatry. 1999;56:1073-1086.",
    "doi_or_source": "10.1542/peds.2019-2528",
    "clinical_evidence": "For preschool children (ages 4-5), parent training in behavior management (PTBM) is first-line treatment (Grade A). For elementary and high school students, FDA-approved medications (stimulants) combined with behavioral classroom interventions provide optimal outcome improvements (MTA study demonstrated combined treatment achieved best functional and social outcomes).",
    "solution_protocol": {
      "non_pharmacological_targets": "Behavioral parent training; classroom accommodations (504 Plan or Individualized Education Program [IEP]); structured daily routines, visual checklists, and positive reinforcement systems.",
      "monitoring_cadence": "Regular height, weight, blood pressure, and pulse monitoring during clinical visits; Vanderbilt ADHD teacher and parent rating scales to monitor medication titration.",
      "clinical_thresholds": "Diagnostic criteria require symptoms in ≥2 settings (home and school) persisting for >6 months with documented functional impairment."
    },
    "patient_plain_language": "ADHD is a neurodevelopmental condition where brain circuits that regulate attention, impulse control, and dopamine signals work differently, making sustained focus and sitting still challenging.",
    "doctor_consultation_checklist": {
      "parameter_question": "Have we gathered standardized Vanderbilt rating scales from both home and teachers to confirm the diagnosis?",
      "safety_question": "How will we monitor my child's appetite, sleep, and physical growth during medication titration?",
      "action_threshold_question": "What school accommodations (like a 504 plan) should we request to support their classroom learning?"
    },
    "red_flags": [
      "Development of sudden motor tics, severe emotional withdrawal, or acute mood swings on medication"
    ]
  },
  {
    "id": "DOC-CARD-041",
    "condition": "COVID-19 Acute Outpatient Management",
    "specialty": "Infectious Disease",
    "organ_system": "Respiratory / Systemic",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (EPIC-HR) & WHO",
    "citation": "Hammond J et al. Oral Nirmatrelvir for High-Risk, Nonhospitalized Adults with Covid-19 (EPIC-HR). N Engl J Med. 2022;386:1397-1408; WHO Therapeutics and COVID-19 Guideline.",
    "doi_or_source": "10.1056/NEJMoa2118542",
    "clinical_evidence": "In nonhospitalized high-risk adult outpatients, oral Nirmatrelvir/Ritonavir (Paxlovid) initiated within 5 days of symptom onset reduced COVID-19-related hospitalization or death by 89% compared to placebo (0.77% vs 6.31%; p<0.001). IV Remdesivir for 3 days represents an alternative high-efficacy antiviral option (PINETREE trial, 87% reduction). Concomitant drug interaction check is mandatory due to strong CYP3A4 inhibition by ritonavir.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict isolation according to public health guidelines; oral hydration; fever and body ache management with acetaminophen; prone resting positions.",
      "monitoring_cadence": "Home pulse oximetry monitoring twice daily throughout acute phase.",
      "clinical_thresholds": "Treatment must be initiated within 5 days of symptom onset. Dose adjustment mandatory in moderate renal impairment (eGFR 30-59 mL/min: 150 mg nirmatrelvir / 100 mg ritonavir BID); contraindicated in eGFR <30 mL/min."
    },
    "patient_plain_language": "COVID-19 is a viral respiratory infection that can cause severe lung inflammation in high-risk individuals. Antiviral pills work by stopping the virus from copying itself inside your cells, but must be started in the first few days of sickness.",
    "doctor_consultation_checklist": {
      "parameter_question": "Are my current kidney function numbers (eGFR) in the normal range for this antiviral pill?",
      "safety_question": "Can we double-check my complete daily medication list for drug interactions with ritonavir?",
      "action_threshold_question": "What drop in home oxygen saturation numbers means I should go to the emergency room?"
    },
    "red_flags": [
      "Oxygen saturation drops below 92% on room air",
      "Persistent chest pressure, severe shortness of breath at rest, or new confusion"
    ]
  },
  {
    "id": "DOC-CARD-042",
    "condition": "Atopic Dermatitis (Eczema)",
    "specialty": "Dermatology",
    "organ_system": "Integumentary / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAD",
    "citation": "Sidbury R et al. Guidelines of Care for the Management of Atopic Dermatitis in Adults. J Am Acad Dermatol. 2024;90(2):345-364.",
    "doi_or_source": "10.1016/jaad.2023.08.010",
    "clinical_evidence": "AAD guidelines emphasize basic barrier repair with bland emollient ointments as foundational therapy. Topical corticosteroids (TCS) are first-line prescription therapy for flares. Topical calcineurin inhibitors (Tacrolimus) and PDE-4 inhibitors (Crisaborole) are recommended for sensitive areas (face, neck, skin folds). For moderate-to-severe disease refractory to topicals, biologic therapy with Dupilumab (anti-IL-4Rα; LIBERTY AD trials, NEJM) provides significant clearance with an excellent safety profile.",
    "solution_protocol": {
      "non_pharmacological_targets": "'Soak and Seal' routine: Daily lukewarm baths/showers (5-10 minutes) followed immediately within 3 minutes by liberal application of thick petrolatum- or ceramide-based ointments; use of gentle, fragrance-free cleansers; wearing loose 100% cotton clothing.",
      "monitoring_cadence": "Reassess flare frequency at 4-8 weeks; transition to proactive twice-weekly maintenance application of topical therapies to previous flare sites.",
      "clinical_thresholds": "Assess disease severity using validated tools like EASI (Eczema Area and Severity Index) or SCORAD."
    },
    "patient_plain_language": "Eczema is a condition where your skin's outer moisture barrier is leaky and easily inflamed, allowing water to escape and irritants to enter, causing intensely itchy, red, cracked patches.",
    "doctor_consultation_checklist": {
      "parameter_question": "Which topical cream strength should I use on my body versus sensitive facial skin?",
      "safety_question": "How do I transition to a twice-weekly proactive routine once my skin redness clears up?",
      "action_threshold_question": "Would I be a candidate for targeted biologic injections if my eczema does not stay controlled with creams?"
    },
    "red_flags": [
      "Sudden painful outbreak of small dome-shaped blisters with fever (Eczema Herpeticum: Emergency)",
      "Spreading honey-colored crusted sores or skin that feels hot, swollen, and tender (Bacterial superinfection)"
    ]
  },
  {
    "id": "DOC-CARD-043",
    "condition": "Plaque Psoriasis",
    "specialty": "Dermatology",
    "organ_system": "Integumentary / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAD / NPF",
    "citation": "Elmets CA et al. Joint AAD-NPF Guidelines of Care for the Management and Treatment of Psoriasis with Biologics. J Am Acad Dermatol. 2019;80(4):1029-1072.",
    "doi_or_source": "10.1016/jaad.2018.11.058",
    "clinical_evidence": "For localized disease (<3% body surface area), high-potency topical corticosteroids combined with vitamin D analogues (Calcipotriene) are first-line. For moderate-to-severe disease (≥3-5% BSA or sensitive areas), targeted biologics (anti-IL-23: Risankizumab, Guselkumab; anti-IL-17: Secukinumab, Ixekizumab; anti-TNF: Adalimumab) achieve PASI 90 or PASI 100 skin clearance rates in 70-85% of patients (Phase 3 trials, NEJM/Lancet).",
    "solution_protocol": {
      "non_pharmacological_targets": "Regular daily emollient moisturization; screening for metabolic comorbidities (obesity, hypertension, diabetes) and cardiovascular risk reduction; smoking cessation; screening for psoriatic arthritis.",
      "monitoring_cadence": "Baseline screening for latent tuberculosis and hepatitis B/C prior to initiating biologic therapies; clinical follow-up at 12-16 weeks.",
      "clinical_thresholds": "Target: BSA <1% or PASI 90 response at 12-16 weeks."
    },
    "patient_plain_language": "Psoriasis is an autoimmune condition where immune signals cause skin cells to grow way too quickly—in days instead of weeks—piling up into thick, red plaques topped with silvery scales.",
    "doctor_consultation_checklist": {
      "parameter_question": "What percentage of my body surface area is affected by psoriasis?",
      "safety_question": "Are we screening for joint stiffness or tendon pain in my fingers and heels (psoriatic arthritis)?",
      "action_threshold_question": "What are the infection risks and monitoring requirements for modern biologic therapy options?"
    },
    "red_flags": [
      "Widespread fiery redness covering more than 90% of body skin with shivering and peeling (Erythrodermic Psoriasis)",
      "Sudden widespread eruption of small sterile pustules covering the body with fever (Generalized Pustular Psoriasis)"
    ]
  },
  {
    "id": "DOC-CARD-044",
    "condition": "Cellulitis & Purulent Skin Infections",
    "specialty": "Dermatology",
    "organ_system": "Integumentary",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "IDSA",
    "citation": "Stevens DL et al. Practice Guidelines for the Diagnosis and Management of Skin and Soft Tissue Infections: 2014 Update by the IDSA. Clin Infect Dis. 2014;59(2):e10-e52.",
    "doi_or_source": "10.1093/cid/ciu300",
    "clinical_evidence": "IDSA guidelines classify SSTIs into purulent (abscess, furuncle) and non-purulent (cellulitis, erysipelas). For non-purulent cellulitis, beta-lactam monotherapy covering Streptococcus (Cephalexin or Cefazolin) is recommended (5-day course proven equivalent to 10 days in JAMA RCT). For purulent infections, incision and drainage is the primary therapy; empirical CA-MRSA antibiotic coverage (Trimethoprim-sulfamethoxazole or Doxycycline) is added for systemic signs.",
    "solution_protocol": {
      "non_pharmacological_targets": "Elevation of the affected limb above the level of the heart to promote lymphatic drainage and accelerate resolution; skin demarcation with a pen line to monitor boundary progression; treatment of predisposing factors (e.g., tinea pedis athlete's foot).",
      "monitoring_cadence": "Reassess at 48 hours. Mild expansion of erythema in the first 24-48 hours can occur due to bacterial toxin release despite effective killing.",
      "clinical_thresholds": "Hospital admission indicated for systemic toxicity, hemodynamic instability, or failure of oral therapy after 48-72 hours."
    },
    "patient_plain_language": "Cellulitis is a bacterial infection of the deep skin layers and tissues, causing a localized patch of skin to become swollen, hot to the touch, and increasingly red.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my infection non-purulent (strep-type) or purulent with an abscess requiring drainage?",
      "safety_question": "How often each day should I keep my infected leg elevated above heart level to speed healing?",
      "action_threshold_question": "How far past the marked pen line must redness spread before I need immediate emergency re-evaluation?"
    },
    "red_flags": [
      "Pain that is out of proportion to the visible skin redness",
      "Skin showing dark purple blisters (bullae), skin sloughing, or crackling gas sensation under the skin (Necrotizing Fasciitis Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-045",
    "condition": "Clostridioides difficile Infection (CDI)",
    "specialty": "Infectious Disease",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "IDSA / SHEA",
    "citation": "Johnson S et al. Clinical Practice Guideline by the IDSA and SHEA: 2021 Focused Update Guidelines on Management of Clostridioides difficile Infection in Adults. Clin Infect Dis. 2021;73(5):e1029-e1044.",
    "doi_or_source": "10.1093/cid/ciab549",
    "clinical_evidence": "Guidelines strongly recommend Fidaxomicin (200 mg BID for 10 days) over oral Vancomycin (125 mg QID for 10 days) as the preferred initial treatment for non-severe and severe CDI (Grade: conditional recommendation), demonstrating superior sustained clinical response and significantly lower recurrence rates. Metronidazole is strongly discouraged. Fecal microbiota transplantation (FMT) is recommended for multiple recurrent CDI.",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate discontinuation of the inciting antibiotic if clinically feasible; strict contact precautions and hand hygiene with soap and water (alcohol sanitizers do not kill C. diff spores); avoid antimotility agents (e.g., Loperamide).",
      "monitoring_cadence": "Monitor stool frequency and consistency daily; test-of-cure testing is contraindicated as stool tests remain PCR-positive for weeks without active infection.",
      "clinical_thresholds": "Severe CDI defined by WBC ≥15,000 cells/μL or serum creatinine >1.5 mg/dL."
    },
    "patient_plain_language": "C. diff is a spore-forming bacterial infection of the colon that often takes over after antibiotics wipe out your bowel's normal, protective gut bacteria, causing severe watery diarrhea.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my C. diff episode classified as non-severe, severe, or recurrent?",
      "safety_question": "Why should I wash my hands with soap and water rather than alcohol hand sanitizer at home?",
      "action_threshold_question": "If my diarrhea resolves, why should we NOT run a follow-up stool test?"
    },
    "red_flags": [
      "Severe abdominal distension, cessation of stool passage accompanied by excruciating abdominal pain, high fever, and low blood pressure (Toxic Megacolon)"
    ]
  },
  {
    "id": "DOC-CARD-046",
    "condition": "Early Localized Lyme Disease",
    "specialty": "Infectious Disease",
    "organ_system": "Integumentary / Systemic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "IDSA / AAN / ACR",
    "citation": "Lantos PM et al. Clinical Practice Guidelines by the IDSA, AAN, and ACR: 2020 Guidelines for the Prevention, Diagnosis, and Treatment of Lyme Disease. Clin Infect Dis. 2021;72(1):e1-e48.",
    "doi_or_source": "10.1093/cid/ciaa1215",
    "clinical_evidence": "Patients with characteristic erythema migrans (EM) rash and history of potential tick exposure in an endemic area should be diagnosed and treated clinically without serologic testing (serology is insensitive in early localized disease, <40%). Oral Doxycycline (100 mg BID for 10-14 days) is first-line treatment. Single-dose prophylactic Doxycycline (200 mg) is recommended within 72 hours of removing an attached Ixodes scapularis tick after ≥36 hours of attachment.",
    "solution_protocol": {
      "non_pharmacological_targets": "Tick prevention education: Insect repellents with DEET or picaridin; wearing permethrin-treated clothing; full-body tick checks within 2 hours of outdoor exposure in wooded/grassy areas; tick removal using fine-tipped tweezers pulling straight up.",
      "monitoring_cadence": "Reassess clinical symptoms at 2-3 weeks; rash typically resolves within 1-2 weeks of initiating antibiotics.",
      "clinical_thresholds": "Two-tiered serological testing (ELISA followed by Western Blot or second enzyme immunoassay) reserved for disseminated disease stages (carditis, facial palsy, arthritis)."
    },
    "patient_plain_language": "Lyme disease is a bacterial infection transmitted by blacklegged deer ticks. In its early stage, it often causes an expanding circular 'bullseye' rash alongside flu-like tiredness and aches.",
    "doctor_consultation_checklist": {
      "parameter_question": "Since I have the characteristic expanding red rash, why is a blood antibody test unnecessary right now?",
      "safety_question": "How should I protect my skin from sun sensitivity while taking oral doxycycline?",
      "action_threshold_question": "What neurological symptoms (like facial muscle drooping) should I watch for over the next few weeks?"
    },
    "red_flags": [
      "Sudden weakness or drooping of one or both sides of the face (Bell's palsy)",
      "Irregular heartbeats, dizziness, or fainting episodes (Lyme Carditis)"
    ]
  },
  {
    "id": "DOC-CARD-047",
    "condition": "Colorectal Cancer Screening",
    "specialty": "Oncology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Recommendation Statement",
    "source_body": "USPSTF",
    "citation": "US Preventive Services Task Force. Screening for Colorectal Cancer: US Preventive Services Task Force Recommendation Statement. JAMA. 2021;325(19):1965-1977.",
    "doi_or_source": "10.1001/jama.2021.6238",
    "clinical_evidence": "The USPSTF recommends screening for colorectal cancer in all adults aged 45 to 75 years (Grade A). Multiple screening strategies demonstrate strong mortality reduction: Colonoscopy every 10 years, annual Fecal Immunochemical Test (FIT), or stool DNA-FIT (Cologuard) every 3 years. Any positive non-invasive stool test mandates follow-up diagnostic colonoscopy.",
    "solution_protocol": {
      "non_pharmacological_targets": "High dietary fiber intake; regular aerobic exercise; limitation of red and processed meats; smoking cessation and reduction in alcohol intake.",
      "monitoring_cadence": "Standard intervals: Colonoscopy every 10 years; annual high-sensitivity FIT; or flexible sigmoidoscopy every 5 years.",
      "clinical_thresholds": "Screening begins earlier (age 40 or 10 years before the youngest affected first-degree relative's diagnosis) in individuals with a family history of colorectal cancer."
    },
    "patient_plain_language": "Colorectal cancer screening checks for precancerous polyps (small growths on the inner colon wall) and removes them before they ever have the chance to transform into cancer.",
    "doctor_consultation_checklist": {
      "parameter_question": "Based on my family history, should I start my routine colon screening at age 45 or earlier?",
      "safety_question": "How do the benefits of a visual colonoscopy compare to an annual home stool test (FIT) for my personal risk?",
      "action_threshold_question": "If I choose a home stool test and it comes back positive, what is the timeline for my colonoscopy?"
    },
    "red_flags": [
      "Persistent visible blood in stool or black tarry stools",
      "Unexplained iron-deficiency anemia or sudden narrowing of stool diameter lasting several weeks"
    ]
  },
  {
    "id": "DOC-CARD-048",
    "condition": "Breast Cancer Screening",
    "specialty": "Oncology",
    "organ_system": "Breast / Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Recommendation Statement",
    "source_body": "USPSTF",
    "citation": "US Preventive Services Task Force. Screening for Breast Cancer: US Preventive Services Task Force Recommendation Statement. JAMA. 2024;331(22):1918-1930.",
    "doi_or_source": "10.1001/jama.2024.5534",
    "clinical_evidence": "The USPSTF recommends biennial screening mammography for women aged 40 to 74 years (Grade B). Collaborative modeling indicates that starting screening at age 40 rather than age 50 averts an additional 1.3 breast cancer deaths per 1,000 women screened, with favorable benefit-to-harm ratios regarding false-positive mammograms and benign biopsies.",
    "solution_protocol": {
      "non_pharmacological_targets": "Regular aerobic exercise; weight management post-menopause; limitation of alcohol intake (alcohol is a dose-dependent breast cancer risk factor); breast self-awareness of any changes.",
      "monitoring_cadence": "Biennial (every 2 years) digital mammography or digital breast tomosynthesis (3D mammography).",
      "clinical_thresholds": "Formal hereditary risk assessment (e.g., Tyrer-Cuzick model) and genetic counseling for BRCA1/2 recommended if significant family history of breast/ovarian cancer is present."
    },
    "patient_plain_language": "A screening mammogram is a low-dose X-ray picture of the breast used to detect tiny changes or early tumors long before they can ever be felt with a hand.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my mammogram report show that I have dense breast tissue, and should we consider supplemental ultrasound?",
      "safety_question": "How often should I schedule my routine mammograms based on my personal and family history?",
      "action_threshold_question": "What is the standard procedure if a screening mammogram detects an area that requires diagnostic views?"
    },
    "red_flags": [
      "A new firm, painless lump in the breast or armpit that does not fluctuate with the menstrual cycle",
      "Nipple retraction, spontaneous clear or bloody nipple discharge, or orange-peel skin dimpling (peau d'orange)"
    ]
  },
  {
    "id": "DOC-CARD-049",
    "condition": "Lung Cancer Screening",
    "specialty": "Oncology",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Recommendation Statement & Landmark RCT",
    "source_body": "USPSTF & NEJM (NLST)",
    "citation": "US Preventive Services Task Force. Screening for Lung Cancer: US Preventive Services Task Force Recommendation Statement. JAMA. 2021;325(10):962-970; National Lung Screening Trial. N Engl J Med. 2011;365:395-409.",
    "doi_or_source": "10.1001/jama.2021.1117",
    "clinical_evidence": "The USPSTF recommends annual screening for lung cancer with low-dose computed tomography (LDCT) in adults aged 50 to 80 years who have a 20 pack-year smoking history and currently smoke or have quit within the past 15 years (Grade B). The National Lung Screening Trial (NLST) demonstrated a 20% relative reduction in lung cancer mortality with LDCT compared to chest radiography.",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate, evidence-based smoking cessation counseling and pharmacotherapy at every screening encounter (smoking cessation reduces lung cancer mortality by >50% over time); radon exposure testing in the home.",
      "monitoring_cadence": "Annual low-dose helical CT scan until the person has not smoked for 15 years or reaches 80 years of age.",
      "clinical_thresholds": "Lung-RADS structured reporting criteria used to classify pulmonary nodule findings and dictate follow-up intervals."
    },
    "patient_plain_language": "Low-dose CT lung screening uses a quick, low-radiation scanner to take detailed cross-section images of your lungs to catch early-stage lung nodules when they are most curable.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my calculated smoking history meet the 20 pack-year threshold for annual low-dose CT scans?",
      "safety_question": "What resources and tools can we set up today to help me quit smoking permanently?",
      "action_threshold_question": "How are small, harmless lung spots (nodules) classified on the Lung-RADS score system?"
    },
    "red_flags": [
      "Coughing up blood or blood-streaked phlegm (Hemoptysis)",
      "New, persistent hoarseness, unexplained rapid weight loss, or shortness of breath"
    ]
  },
  {
    "id": "DOC-CARD-050",
    "condition": "Cervical Cancer Screening & HPV Triage",
    "specialty": "Oncology",
    "organ_system": "Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Recommendation Statement & Guidelines",
    "source_body": "USPSTF & ASCCP",
    "citation": "US Preventive Services Task Force. Screening for Cervical Cancer: US Preventive Services Task Force Recommendation Statement. JAMA. 2018;320(7):674-686; Perkins RB et al. 2019 ASCCP Risk-Based Management Consensus Guidelines. J Low Genit Tract Dis. 2020;24(2):102-131.",
    "doi_or_source": "10.1001/jama.2018.10897",
    "clinical_evidence": "USPSTF recommends screening for cervical cancer in women aged 21 to 65 years. Strategies: Cervical cytology (Pap smear) alone every 3 years for ages 21-29; for ages 30-65, options include high-risk HPV (hrHPV) testing alone every 5 years, hrHPV co-testing with cytology every 5 years, or cytology alone every 3 years. Primary hrHPV testing demonstrates superior sensitivity for detecting cervical intraepithelial neoplasia grade 3+ (CIN 3+).",
    "solution_protocol": {
      "non_pharmacological_targets": "HPV vaccination (Gardasil 9) recommended through age 26 (and shared clinical decision-making ages 27-45) to prevent over 90% of HPV-attributable cancers; smoking cessation (smoking impairs cervical clearance of high-risk HPV).",
      "monitoring_cadence": "Every 3 or 5 years depending on modality if prior screenings are negative.",
      "clinical_thresholds": "ASCCP management guidelines dictate whether a patient requires immediate colposcopy or short-interval 1-year repeat testing based on immediate and 5-year calculated CIN 3+ risk."
    },
    "patient_plain_language": "Cervical cancer screening checks the cells of your cervix for high-risk strains of the Human Papillomavirus (HPV) that can cause cell changes years before cervical cancer could develop.",
    "doctor_consultation_checklist": {
      "parameter_question": "Was my test a Pap smear alone, a high-risk HPV test, or both co-tested together?",
      "safety_question": "What is my recommended screening interval if my results are completely negative?",
      "action_threshold_question": "If my HPV test is positive for high-risk types, what are our next steps for a colposcopy examination?"
    },
    "red_flags": [
      "Abnormal vaginal bleeding between periods or after sexual intercourse",
      "Persistent pelvic pain or watery, bloody vaginal discharge with an unusual odor"
    ]
  },

  # ── LIST 2 (051 - 080) ────────────────────────────────────────────
  {
    "id": "DOC-CARD-051",
    "condition": "Crohn's Disease (Inflammatory Bowel Disease)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACG",
    "citation": "Lichtenstein GR et al. ACG Clinical Guideline: Management of Crohn's Disease in Adults. Am J Gastroenterol. 2018;113(4):481-517.",
    "doi_or_source": "10.1038/ajg.2018.27",
    "clinical_evidence": "Guidelines recommend a 'Treat-to-Target' strategy aiming for deep mucosal healing, not just symptom resolution. For moderate-to-severe disease, anti-TNF biologics (Infliximab, Adalimumab) or anti-integrins (Vedolizumab) are first-line to induce and maintain remission. Systemic corticosteroids should be used strictly for acute flares and never for maintenance due to severe long-term toxicity.",
    "solution_protocol": {
      "non_pharmacological_targets": "Absolute smoking cessation (smoking doubles the risk of surgical resection and disease recurrence); screening for malnutrition and bone density loss; exclusive enteral nutrition (EEN) in severe pediatric cases.",
      "monitoring_cadence": "Fecal calprotectin or C-reactive protein (CRP) every 3-6 months; endoscopic evaluation 6-12 months after starting a new biologic therapy to confirm mucosal healing.",
      "clinical_thresholds": "Surgical bowel resection is reserved for medication-refractory disease, strictures causing bowel obstruction, or fistulizing disease."
    },
    "patient_plain_language": "Crohn's disease is an autoimmune condition where your immune system attacks the lining of your digestive tract, causing deep ulcers, swelling, and scar tissue anywhere from the mouth to the colon.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current fecal calprotectin level, and does it show hidden inflammation even when I feel okay?",
      "safety_question": "What vaccines do I need to update before starting an immune-suppressing biologic medication?",
      "action_threshold_question": "If I experience a flare, what is our exit strategy to ensure I am not on steroid pills for too long?"
    },
    "red_flags": [
      "Inability to pass gas or stool, accompanied by severe abdominal pain and vomiting (Bowel Obstruction)",
      "High fever with a firm, extremely tender abdomen"
    ]
  },
  {
    "id": "DOC-CARD-052",
    "condition": "Ulcerative Colitis (Inflammatory Bowel Disease)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACG",
    "citation": "Rubin DT et al. ACG Clinical Guideline: Ulcerative Colitis in Adults. Am J Gastroenterol. 2019;114(3):384-413.",
    "doi_or_source": "10.14309/ajg.0000000000000152",
    "clinical_evidence": "Unlike Crohn's, UC is limited to the mucosal layer of the colon. For mild-to-moderate UC, topical (rectal) and oral 5-aminosalicylates (5-ASA/Mesalamine) are first-line. For moderate-to-severe disease, targeted biologics (Infliximab, Vedolizumab) or JAK inhibitors (Tofacitinib) are recommended. Annual surveillance colonoscopy is required after 8 years of disease due to significantly elevated colorectal cancer risk.",
    "solution_protocol": {
      "non_pharmacological_targets": "Maintaining hydration during severe diarrheal flares; avoidance of NSAIDs (ibuprofen, naproxen) which can trigger disease flares; iron supplementation for chronic blood loss.",
      "monitoring_cadence": "Endoscopic assessment 3-6 months after therapy initiation to confirm mucosal healing (Mayo Endoscopic Subscore of 0 or 1).",
      "clinical_thresholds": "Hospitalization indicated for acute severe ulcerative colitis (≥6 bloody bowel movements/day with systemic toxicity like fever or tachycardia)."
    },
    "patient_plain_language": "Ulcerative colitis is a chronic inflammatory disease that causes continuous superficial sores (ulcers) specifically along the inner lining of your large intestine and rectum, leading to bloody diarrhea.",
    "doctor_consultation_checklist": {
      "parameter_question": "Has my latest colonoscopy shown full mucosal healing, or just symptom improvement?",
      "safety_question": "Since I have had UC for several years, when do I need to start annual colon cancer screening?",
      "action_threshold_question": "Can I use mesalamine suppositories or enemas to target rectal inflammation directly?"
    },
    "red_flags": [
      "Passing more than 6 bloody stools a day accompanied by fever, rapid heart rate, and dizziness (Acute Severe UC)",
      "Sudden extreme abdominal swelling and pain (Toxic Megacolon)"
    ]
  },
  {
    "id": "DOC-CARD-053",
    "condition": "Peripheral Artery Disease (PAD)",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AHA / ACC",
    "citation": "Gerhard-Herman MD et al. 2016 AHA/ACC Guideline on the Management of Patients With Lower Extremity Peripheral Artery Disease. Circulation. 2017;135(12):e726-e779.",
    "doi_or_source": "10.1161/CIR.0000000000000471",
    "clinical_evidence": "Diagnosis is established by a resting Ankle-Brachial Index (ABI) ≤0.90. First-line therapy for intermittent claudication is Supervised Exercise Therapy (SET), which increases maximal walking distance by 100-150% (superior to pharmacotherapy). Antiplatelet therapy (Aspirin or Clopidogrel) and high-intensity statin therapy are mandatory to reduce the high risk of myocardial infarction and stroke in PAD patients.",
    "solution_protocol": {
      "non_pharmacological_targets": "Absolute smoking cessation (essential to prevent limb amputation); Supervised Exercise Therapy (treadmill walking to the point of moderate pain, resting, and repeating for 30-45 minutes, 3 times/week); strict foot care and daily inspections.",
      "monitoring_cadence": "Annual ABI assessment and clinical evaluation of walking distance capacity.",
      "clinical_thresholds": "Revascularization (endovascular or surgical bypass) is reserved for lifestyle-limiting claudication unresponsive to SET, or Critical Limb Ischemia (rest pain, non-healing ulcers)."
    },
    "patient_plain_language": "Peripheral artery disease is caused by cholesterol plaque building up in the arteries of your legs, reducing blood flow. This causes your leg muscles to cramp and ache when walking because they are starved of oxygen.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my Ankle-Brachial Index (ABI) score, and how severely does it indicate my blood flow is blocked?",
      "safety_question": "How can I safely walk through the muscle pain during exercise therapy to help my legs build new blood vessels?",
      "action_threshold_question": "At what point does poor circulation require meeting with a vascular surgeon?"
    },
    "red_flags": [
      "Severe pain in the toes or feet that wakes you up at night and improves when hanging feet off the bed (Rest Pain)",
      "A sore or ulcer on the foot or toe that turns black and does not heal (Critical Limb Ischemia)"
    ]
  },
  {
    "id": "DOC-CARD-054",
    "condition": "Systemic Lupus Erythematosus (SLE)",
    "specialty": "Rheumatology",
    "organ_system": "Immune / Systemic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: International Clinical Guideline",
    "source_body": "EULAR",
    "citation": "Fanouriakis A et al. 2019 Update of the EULAR Recommendations for the Management of Systemic Lupus Erythematosus. Ann Rheum Dis. 2019;78(6):736-745.",
    "doi_or_source": "10.1136/annrheumdis-2019-215089",
    "clinical_evidence": "Hydroxychloroquine is recommended for all patients with SLE, unless contraindicated, as it improves survival, reduces flares, and prevents organ damage (Grade A). Glucocorticoids should be used at the lowest possible dose (target ≤7.5 mg/day of prednisone) and tapered as soon as possible. Belimumab (anti-BAFF) is approved for autoantibody-positive SLE with inadequate response to standard therapy.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict sun protection (broad-spectrum sunscreen SPF >50, UV-protective clothing) as UV light triggers systemic flares; cardiovascular risk management (SLE carries a significantly elevated risk of premature atherosclerosis); avoidance of sulfa-containing antibiotics.",
      "monitoring_cadence": "Routine screening for lupus nephritis every 6-12 months (urinalysis and urine protein-to-creatinine ratio); annual baseline ophthalmologic exam for hydroxychloroquine retinal toxicity.",
      "clinical_thresholds": "Target: Clinical remission (SLEDAI = 0) or Low Disease Activity (LLDAS) without reliance on chronic systemic steroids."
    },
    "patient_plain_language": "Lupus is a chronic autoimmune disease where the immune system loses its ability to tell the difference between foreign invaders and your own healthy tissues, creating antibodies that attack skin, joints, and organs.",
    "doctor_consultation_checklist": {
      "parameter_question": "What are my current inflammatory markers and kidney protein levels?",
      "safety_question": "How frequently do I need to see an eye doctor to check for medication side effects from Hydroxychloroquine?",
      "action_threshold_question": "What specific symptoms (like foamy urine or severe chest pain when taking a breath) indicate a dangerous organ flare?"
    },
    "red_flags": [
      "Foamy urine or sudden swelling in the legs (Warning signs of Lupus Nephritis/kidney involvement)",
      "Sharp chest pain that gets worse when taking a deep breath (Pleurisy/Pericarditis)"
    ]
  },
  {
    "id": "DOC-CARD-055",
    "condition": "HIV Pre-Exposure Prophylaxis (PrEP)",
    "specialty": "Infectious Disease",
    "organ_system": "Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "CDC",
    "citation": "Centers for Disease Control and Prevention: US Public Health Service. Preexposure Prophylaxis for the Prevention of HIV Infection in the United States—2021 Update.",
    "doi_or_source": "https://www.cdc.gov/hiv/pdf/risk/prep/cdc-hiv-prep-guidelines-2021.pdf",
    "clinical_evidence": "Daily oral TDF/FTC (Truvada) or TAF/FTC (Descovy) reduces the risk of getting HIV from sex by about 99% when taken consistently. Long-acting injectable Cabotegravir (Apretude) given every 2 months was shown in HPTN 083/084 trials to be superior to daily oral PrEP in preventing HIV acquisition, offering an option for those with adherence challenges.",
    "solution_protocol": {
      "non_pharmacological_targets": "Concurrent use of condoms to prevent other sexually transmitted infections (STIs) which PrEP does not cover; adherence counseling.",
      "monitoring_cadence": "Mandatory clinic visits every 3 months for oral PrEP (every 2 months for injectable) to conduct HIV antigen/antibody testing, STI screening (syphilis, gonorrhea, chlamydia), and renal function monitoring.",
      "clinical_thresholds": "PrEP must be discontinued immediately and converted to full antiretroviral therapy (ART) if an HIV test returns positive to prevent drug resistance."
    },
    "patient_plain_language": "PrEP is a highly effective preventive medication (taken as a daily pill or bi-monthly injection) that builds a shield around your immune cells, preventing the HIV virus from establishing an infection if you are exposed.",
    "doctor_consultation_checklist": {
      "parameter_question": "Do my baseline kidney function labs allow me to safely take oral PrEP medication?",
      "safety_question": "What is the mandatory testing schedule for HIV and other STIs while I remain on this medication?",
      "action_threshold_question": "If I miss a dose of my daily pill, what steps should I take to ensure I remain protected?"
    },
    "red_flags": [
      "Flu-like symptoms (fever, swollen lymph nodes, rash) occurring shortly after a potential HIV exposure (Possible Acute HIV Infection)"
    ]
  },
  {
    "id": "DOC-CARD-056",
    "condition": "Chronic Hepatitis C (HCV)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive / Hepatic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AASLD / IDSA",
    "citation": "AASLD-IDSA HCV Guidance Panel. Hepatitis C Guidance 2023 Update: AASLD-IDSA Recommendations for Testing, Managing, and Treating Hepatitis C Virus Infection.",
    "doi_or_source": "https://www.hcvguidelines.org/",
    "clinical_evidence": "Direct-acting antivirals (DAAs) such as Sofosbuvir/Velpatasvir (Epclusa) or Glecaprevir/Pibrentasvir (Mavyret) achieve Sustained Virologic Response (SVR) — considered a virologic cure — in >95% of patients across all genotypes after 8 to 12 weeks of oral therapy. Treatment is recommended for all patients with chronic HCV infection, except those with short life expectancies.",
    "solution_protocol": {
      "non_pharmacological_targets": "Absolute avoidance of alcohol (accelerates liver fibrosis); vaccination against Hepatitis A and B; weight management to prevent concurrent fatty liver disease.",
      "monitoring_cadence": "HCV RNA quantitative test 12 weeks after completing DAA therapy to confirm Sustained Virologic Response (SVR12).",
      "clinical_thresholds": "Patients with established cirrhosis (F4 fibrosis) require lifelong hepatocellular carcinoma (HCC) surveillance with liver ultrasound every 6 months, even after HCV cure."
    },
    "patient_plain_language": "Hepatitis C is a viral infection that slowly damages the liver over decades. Modern antiviral pills can completely cure the infection in 8 to 12 weeks, stopping further liver damage.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my Hepatitis C genotype, and what stage of liver scarring (fibrosis) do I currently have?",
      "safety_question": "Will my current prescriptions or over-the-counter supplements interact with the antiviral pills?",
      "action_threshold_question": "Even after I am cured, will I need long-term liver ultrasounds because of existing scar tissue?"
    },
    "red_flags": [
      "Vomiting blood or passing black tarry stools (Signs of bleeding esophageal varices in advanced cirrhosis)",
      "New confusion or severe yellowing of the eyes (jaundice)"
    ]
  },
  {
    "id": "DOC-CARD-057",
    "condition": "Sickle Cell Disease",
    "specialty": "Hematology",
    "organ_system": "Circulatory / Blood",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ASH",
    "citation": "Chou ST et al. American Society of Hematology 2020 Guidelines for Sickle Cell Disease: Management of Acute and Chronic Pain. Blood Adv. 2020;4(10):2270-2300.",
    "doi_or_source": "10.1182/bloodadvances.2020001802",
    "clinical_evidence": "Hydroxyurea is the primary disease-modifying therapy, strongly recommended for adults with ≥3 moderate-to-severe pain crises per year, demonstrating significant reductions in vaso-occlusive crises, acute chest syndrome, and mortality. Rapid initiation of individualized IV opioids (within 30-60 minutes of triage) is the standard of care for acute vaso-occlusive crisis management in the ER.",
    "solution_protocol": {
      "non_pharmacological_targets": "Aggressive daily hydration; avoidance of extreme temperatures (both cold and excessive heat); routine folic acid supplementation; ensuring complete pneumococcal and meningococcal vaccinations due to functional asplenia.",
      "monitoring_cadence": "Annual Transcranial Doppler (TCD) screening in children (ages 2-16) to assess stroke risk; regular retinal exams and renal function screening.",
      "clinical_thresholds": "Target absolute neutrophil count (ANC) monitoring during Hydroxyurea titration to prevent severe myelosuppression."
    },
    "patient_plain_language": "Sickle cell disease is a genetic condition where red blood cells become hard and crescent-shaped instead of round and flexible, causing them to get stuck in small blood vessels, blocking oxygen and triggering severe pain.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my Hydroxyurea dose optimized to maximize my fetal hemoglobin levels?",
      "safety_question": "Do I have a personalized, written pain management plan to present to the emergency room during a crisis?",
      "action_threshold_question": "What specific fever temperature should prompt me to go to the emergency room immediately?"
    },
    "red_flags": [
      "Fever >101.3°F (38.5°C) in any patient with sickle cell (Medical Emergency due to infection risk)",
      "Sudden chest pain, cough, and shortness of breath (Acute Chest Syndrome)",
      "Sudden weakness or numbness on one side of the body (Stroke)"
    ]
  },
  {
    "id": "DOC-CARD-058",
    "condition": "Multiple Sclerosis (Relapsing-Remitting)",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System / Immune",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 RCT",
    "source_body": "NEJM (OPERA I/II)",
    "citation": "Hauser SL et al. Ocrelizumab versus Interferon Beta-1a in Relapsing Multiple Sclerosis (OPERA I and II). N Engl J Med. 2017;376:221-234.",
    "doi_or_source": "10.1056/NEJMoa1601277",
    "clinical_evidence": "In relapsing MS, high-efficacy Disease Modifying Therapies (DMTs) like Ocrelizumab (anti-CD20 monoclonal antibody) demonstrate superior efficacy over older therapies (Interferon beta-1a), lowering annualized relapse rates by 46% and significantly reducing disability progression. Early initiation of high-efficacy DMTs is increasingly recommended to preserve neurological reserve.",
    "solution_protocol": {
      "non_pharmacological_targets": "Vitamin D3 supplementation (maintaining levels >40 ng/mL); structured physical therapy to manage spasticity and gait; avoidance of extreme heat (Uhthoff's phenomenon, where heat temporarily worsens neurological symptoms).",
      "monitoring_cadence": "Brain and spinal MRI with contrast every 6-12 months to monitor for subclinical active inflammatory lesions; routine JC Virus antibody testing if on Natalizumab.",
      "clinical_thresholds": "Acute, disabling relapses are typically treated with high-dose IV methylprednisolone (1g/day for 3-5 days) to accelerate recovery, though this does not change long-term disease progression."
    },
    "patient_plain_language": "Multiple sclerosis is an autoimmune disease where the immune system attacks myelin, the protective insulation around nerve fibers in the brain and spinal cord, disrupting communication signals.",
    "doctor_consultation_checklist": {
      "parameter_question": "Did my recent MRI show any new active brain lesions compared to my last scan?",
      "safety_question": "What is my risk for opportunistic infections while on high-efficacy immune therapies?",
      "action_threshold_question": "How can I differentiate between a true MS relapse and a temporary worsening of old symptoms due to heat or stress?"
    },
    "red_flags": [
      "Sudden, painful loss of vision in one eye (Optic Neuritis)",
      "New profound weakness in the legs or loss of bowel/bladder control"
    ]
  },
  {
    "id": "DOC-CARD-059",
    "condition": "Pelvic Inflammatory Disease (PID)",
    "specialty": "Women's Health",
    "organ_system": "Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "CDC",
    "citation": "Workowski KA et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187.",
    "doi_or_source": "10.15585/mmwr.rr7004a1",
    "clinical_evidence": "Empiric, broad-spectrum treatment should be initiated in sexually active young women experiencing lower abdominal pain if cervical motion tenderness or adnexal tenderness is present on exam. Outpatient regimens must cover C. trachomatis, N. gonorrhoeae, and anaerobes: Ceftriaxone 500 mg IM (single dose) PLUS Doxycycline 100 mg BID for 14 days PLUS Metronidazole 500 mg BID for 14 days.",
    "solution_protocol": {
      "non_pharmacological_targets": "Abstinence from sexual intercourse until the patient and their partner(s) have completed the full antibiotic regimen and symptoms have resolved; expedited partner therapy (EPT) to prevent reinfection.",
      "monitoring_cadence": "Mandatory clinical re-evaluation within 48-72 hours to ensure symptom improvement (reduction in fever and abdominal tenderness).",
      "clinical_thresholds": "Hospitalization and IV antibiotics are required if pregnancy is present, oral fluids cannot be tolerated, or a tubo-ovarian abscess (TOA) is suspected on imaging."
    },
    "patient_plain_language": "Pelvic inflammatory disease is a serious bacterial infection of the female reproductive organs (uterus, fallopian tubes, and ovaries), often caused by untreated sexually transmitted infections, which can lead to infertility if not cured quickly.",
    "doctor_consultation_checklist": {
      "parameter_question": "Have we tested for both Chlamydia and Gonorrhea, and when will the results return?",
      "safety_question": "How can we arrange for my partner(s) to receive antibiotics so I do not get reinfected?",
      "action_threshold_question": "If my abdominal pain does not significantly improve within 3 days of starting antibiotics, what is our next step?"
    },
    "red_flags": [
      "High fever, severe nausea and vomiting, or fainting",
      "Sudden, sharp, unbearable pelvic pain (Potential ruptured abscess or ectopic pregnancy)"
    ]
  },
  {
    "id": "DOC-CARD-060",
    "condition": "Neonatal Hyperbilirubinemia (Jaundice)",
    "specialty": "Pediatrics",
    "organ_system": "Hepatic / Systemic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAP",
    "citation": "Kemper AR et al. Clinical Practice Guideline Revision: Management of Hyperbilirubinemia in the Newborn Infant 35 or More Weeks of Gestation. Pediatrics. 2022;150(3):e2022058859.",
    "doi_or_source": "10.1542/peds.2022-058859",
    "clinical_evidence": "The AAP provides age-in-hours specific nomograms for initiating phototherapy or exchange transfusion. Universal screening of Total Serum Bilirubin (TSB) or Transcutaneous Bilirubin (TcB) is recommended before hospital discharge. Phototherapy is highly effective at converting unconjugated bilirubin into water-soluble isomers for excretion, preventing bilirubin encephalopathy (kernicterus).",
    "solution_protocol": {
      "non_pharmacological_targets": "Frequent, exclusive breastfeeding (8-12 times per day) in the first days of life to promote bowel movements and enteral excretion of bilirubin; assessment by a lactation consultant to ensure adequate milk transfer.",
      "monitoring_cadence": "Follow-up bilirubin measurement within 24 to 48 hours after discharge, dictated specifically by the infant's age in hours and risk-zone plotting on the AAP nomogram.",
      "clinical_thresholds": "Direct (conjugated) bilirubin levels >20% of total bilirubin or >1.0 mg/dL require immediate evaluation for biliary atresia or hepatic pathology."
    },
    "patient_plain_language": "Jaundice is a common, temporary yellowing of a newborn's skin and eyes caused by a buildup of bilirubin, a yellow pigment created as the baby breaks down extra red blood cells faster than their immature liver can process.",
    "doctor_consultation_checklist": {
      "parameter_question": "Where does my baby's bilirubin level plot on the hour-specific risk chart?",
      "safety_question": "Is my baby transferring enough breast milk, and how many wet/dirty diapers should I look for daily?",
      "action_threshold_question": "When exactly is our follow-up pediatrician appointment scheduled to recheck the yellowing?"
    },
    "red_flags": [
      "The baby is extremely difficult to wake up, refuses to feed, or is entirely floppy/lethargic",
      "High-pitched crying or arching of the neck/back backwards",
      "Yellowing extending down past the belly button to the legs"
    ]
  },
  {
    "id": "DOC-CARD-061",
    "condition": "Acute Pancreatitis",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACG",
    "citation": "Tenner S et al. American College of Gastroenterology Guideline: Management of Acute Pancreatitis. Am J Gastroenterol. 2013;108(9):1400-1415 (Reaffirmed 2024).",
    "doi_or_source": "10.1038/ajg.2013.218",
    "clinical_evidence": "Aggressive early intravenous hydration (250-500 mL/hr of lactated Ringer's) within the first 12-24 hours is most beneficial to prevent tissue necrosis. Routine use of prophylactic antibiotics in severe acute pancreatitis is strongly discouraged. Early oral feeding (within 24 hours) with a low-fat solid diet is recommended over prolonged fasting (NPO) to protect the gut mucosal barrier.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict cessation of all alcohol consumption; early refeeding as tolerated by pain; ERCP intervention if concurrent acute cholangitis or biliary obstruction is present.",
      "monitoring_cadence": "Reassess fluid status (BUN, hematocrit, heart rate) every 6 hours during the first 24-48 hours.",
      "clinical_thresholds": "Diagnosis requires 2 of 3: Characteristic epigastric pain, serum lipase/amylase ≥3x upper limit of normal, or characteristic findings on CT/MRI."
    },
    "patient_plain_language": "Acute pancreatitis is a sudden, severe inflammation where the digestive enzymes made by the pancreas become activated too early, essentially digesting the pancreas itself and causing intense abdominal pain.",
    "doctor_consultation_checklist": {
      "parameter_question": "Are my kidney and hydration lab numbers (like BUN) improving with the IV fluids?",
      "safety_question": "Does my ultrasound show gallstones as the cause, and will I need my gallbladder removed?",
      "action_threshold_question": "How soon can I try to eat solid food again to help my intestines recover?"
    },
    "red_flags": [
      "Severe, piercing upper abdominal pain radiating straight through to the back, accompanied by intractable vomiting",
      "Fever, confusion, and a drop in blood pressure (Signs of systemic inflammatory response/SIRS)"
    ]
  },
  {
    "id": "DOC-CARD-062",
    "condition": "Cirrhosis & Portal Hypertension",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive / Hepatic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AASLD",
    "citation": "Garcia-Tsao G et al. Portal Hypertensive Bleeding in Cirrhosis: Risk Stratification, Diagnosis, and Management. Hepatology. 2017;65(1):310-335.",
    "doi_or_source": "10.1002/hep.28906",
    "clinical_evidence": "Non-selective beta-blockers (NSBBs: Propranolol, Nadolol, Carvedilol) or Endoscopic Band Ligation (EBL) are recommended for primary prophylaxis of medium-to-large esophageal varices to prevent catastrophic bleeding. NSBBs lower portal pressure by decreasing cardiac output and causing splanchnic vasoconstriction. Diuretics (Spironolactone + Furosemide ratio 100:40) remain first-line for ascites management.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict dietary sodium restriction (<2000 mg/day) for ascites control; high-protein, frequent-meal diet with late-evening snacks to prevent muscle wasting (sarcopenia); absolute alcohol cessation.",
      "monitoring_cadence": "Hepatocellular carcinoma (HCC) screening with liver ultrasound +/- alpha-fetoprotein every 6 months; endoscopic screening for varices every 1-3 years.",
      "clinical_thresholds": "Hepatic encephalopathy managed via lactulose titration to achieve 2-3 soft bowel movements daily, plus Rifaximin if recurrent."
    },
    "patient_plain_language": "Cirrhosis is severe scarring of the liver that blocks normal blood flow. This causes pressure to back up into the veins of your stomach and esophagus (portal hypertension), and fluid to leak into your belly (ascites).",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my MELD score, and how does it affect my position on the liver transplant waitlist?",
      "safety_question": "Is my blood pressure medication specifically meant to lower the pressure inside my liver veins to prevent bleeding?",
      "action_threshold_question": "What level of confusion or sleepiness (hepatic encephalopathy) should trigger a trip to the hospital?"
    },
    "red_flags": [
      "Vomiting bright red blood or passing dark, tarry stools (Ruptured Varices: Immediate Emergency)",
      "Sudden, severe confusion, disorientation, or extreme lethargy",
      "New fever combined with increasing abdominal swelling (Possible Spontaneous Bacterial Peritonitis)"
    ]
  },
  {
    "id": "DOC-CARD-063",
    "condition": "Acute Ischemic Stroke",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System / Vascular",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AHA / ASA",
    "citation": "Powers WJ et al. 2019 Update to the 2018 Guidelines for the Early Management of Patients With Acute Ischemic Stroke. Stroke. 2019;50(12):e344-e418.",
    "doi_or_source": "10.1161/STR.0000000000000211",
    "clinical_evidence": "Intravenous Tenecteplase or Alteplase (tPA) is strongly recommended for eligible patients presenting within 3.0 to 4.5 hours of symptom onset. Mechanical thrombectomy is the standard of care for large vessel occlusions (LVO) in the anterior circulation within 24 hours of last known normal, provided the patient meets specific clinical/imaging mismatch criteria (DAWN and DEFUSE-3 trials).",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate NPO (nothing by mouth) status until dysphagia screening clears to prevent aspiration pneumonia; permissive hypertension in the acute phase (do not lower BP unless >220/120 mmHg, or >185/110 if receiving tPA) to maintain brain perfusion.",
      "monitoring_cadence": "Neurological assessments (NIHSS) every 15 mins during and after IV thrombolysis for 2 hours, then every 30 mins for 6 hours.",
      "clinical_thresholds": "Time-is-brain metric: Target door-to-needle (tPA) time ≤60 minutes; door-to-device (thrombectomy) time ≤90 minutes."
    },
    "patient_plain_language": "An ischemic stroke happens when a blood clot blocks a blood vessel in the brain, cutting off oxygen. Brain cells die rapidly, so emergency clot-busting medicine or surgical clot removal must happen within hours.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is the exact 'last known normal' time for these stroke symptoms?",
      "safety_question": "Is the patient on any blood thinners at home that would make clot-busting medication unsafe?",
      "action_threshold_question": "Are they eligible for a mechanical clot retrieval procedure (thrombectomy) based on the CT scan?"
    },
    "red_flags": [
      "F.A.S.T: Sudden Facial drooping, Arm weakness, or Speech difficulty (Call 911 immediately)",
      "Sudden loss of vision in one eye or sudden severe difficulty walking"
    ]
  },
  {
    "id": "DOC-CARD-064",
    "condition": "Adult Epilepsy & Seizure Disorders",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAN / AES",
    "citation": "Kanner AM et al. Practice Guideline Update: Efficacy and Tolerability of the New Antiepileptic Drugs II. Neurology. 2018;91(2):82-90.",
    "doi_or_source": "10.1212/WNL.0000000000005756",
    "clinical_evidence": "Levetiracetam, Lamotrigine, and Zonisamide demonstrate Level A evidence for new-onset focal epilepsy in adults. Valproic acid remains highly effective for generalized epilepsy but carries severe teratogenic risks and is contraindicated in women of childbearing potential without strict contraception. Over 60-70% of patients achieve seizure freedom on monotherapy.",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict sleep hygiene (sleep deprivation is the most common seizure trigger); avoidance of excessive alcohol and illicit stimulants; driving restriction compliance per local laws (usually 3-6 months seizure-free).",
      "monitoring_cadence": "Therapeutic drug monitoring (checking blood levels) to establish individual baseline adherence and toxicity thresholds; routine DEXA scans (many anti-seizure meds deplete bone density).",
      "clinical_thresholds": "Diagnosis requires ≥2 unprovoked seizures occurring >24 hours apart, or 1 unprovoked seizure with an EEG/MRI showing high risk of recurrence."
    },
    "patient_plain_language": "Epilepsy is a neurological disorder where clusters of nerve cells in the brain sometimes signal abnormally, causing a sudden surge of electrical activity that results in a seizure.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my EEG test show a focal (starting in one spot) or generalized pattern?",
      "safety_question": "What are the long-term side effects of this medication on my bone health, liver, or future pregnancies?",
      "action_threshold_question": "What should my family do during a seizure, and at what minute mark should they call an ambulance?"
    },
    "red_flags": [
      "Status Epilepticus: Any seizure lasting longer than 5 minutes, or back-to-back seizures without waking up in between (Immediate Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-065",
    "condition": "Bipolar I Disorder",
    "specialty": "Psychiatry",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "CANMAT / ISBD",
    "citation": "Yatham LN et al. Canadian Network for Mood and Anxiety Treatments (CANMAT) and ISBD 2018 Guidelines for the Management of Patients with Bipolar Disorder. Bipolar Disord. 2018;20(2):97-170.",
    "doi_or_source": "10.1111/bdi.12609",
    "clinical_evidence": "First-line agents for acute mania include Lithium, Quetiapine, Divalproex, Asenapine, and Aripiprazole. For bipolar depression, Quetiapine, Lurasidone, and Lithium are first-line. Antidepressants (SSRIs/SNRIs) must be avoided as monotherapy in Bipolar I due to the high risk of triggering manic switching or rapid cycling.",
    "solution_protocol": {
      "non_pharmacological_targets": "Interpersonal and social rhythm therapy (IPSRT) to stabilize daily routines; strict sleep-wake cycle regulation; elimination of psychoactive substances (cannabis and stimulants strongly trigger mania).",
      "monitoring_cadence": "Lithium monitoring: Check serum levels every 3-6 months (target 0.6-0.8 mEq/L for maintenance), alongside renal function (eGFR) and thyroid function (TSH).",
      "clinical_thresholds": "Diagnosis of Bipolar I requires at least one lifetime manic episode lasting ≥7 days (or any duration if hospitalization is required)."
    },
    "patient_plain_language": "Bipolar disorder is a brain condition that causes extreme, uncontrollable shifts in mood, energy, and activity levels, ranging from deep depressions to euphoric or irritable 'manic' highs.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current Lithium blood level, and is it safely within the therapeutic window?",
      "safety_question": "How will we monitor my thyroid and kidney function while taking mood stabilizers?",
      "action_threshold_question": "What early warning signs of a manic episode (like needing less sleep) mean I should contact you immediately?"
    },
    "red_flags": [
      "Not sleeping for days without feeling tired, accompanied by severe impulsivity or grand delusions",
      "Severe depressive crash with suicidal thoughts (Call 988/Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-066",
    "condition": "Post-Traumatic Stress Disorder (PTSD)",
    "specialty": "Psychiatry",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "APA / VA/DoD",
    "citation": "Department of Veterans Affairs and Department of Defense. VA/DoD Clinical Practice Guideline for the Management of Posttraumatic Stress Disorder and Acute Stress Disorder. 2023.",
    "doi_or_source": "https://www.healthquality.va.gov/guidelines/mh/ptsd/",
    "clinical_evidence": "Trauma-focused psychotherapies (Prolonged Exposure [PE], Cognitive Processing Therapy [CPT], and EMDR) have the strongest evidence base and are recommended over pharmacotherapy as first-line interventions (Grade A). If medication is preferred, SSRIs (Sertraline, Paroxetine) or SNRIs (Venlafaxine) are first-line. Benzodiazepines are strongly recommended against due to interference with fear extinction and risk of substance abuse.",
    "solution_protocol": {
      "non_pharmacological_targets": "Trauma-focused CBT/CPT (typically 8-15 sessions); sleep hygiene optimization; avoidance of alcohol for self-medication.",
      "monitoring_cadence": "Symptom tracking using the PTSD Checklist (PCL-5) every 4 weeks to measure response to therapy.",
      "clinical_thresholds": "Prazosin may be considered for trauma-related nightmares (though recent RCTs show mixed overall efficacy compared to older data)."
    },
    "patient_plain_language": "PTSD is a condition where the brain's 'fight or flight' alarm system stays stuck in the ON position long after a traumatic event is over, causing flashbacks, nightmares, and severe anxiety.",
    "doctor_consultation_checklist": {
      "parameter_question": "Can you refer me to a therapist certified specifically in Prolonged Exposure or Cognitive Processing Therapy?",
      "safety_question": "Why are tranquilizers (benzodiazepines) harmful to the long-term recovery of PTSD?",
      "action_threshold_question": "What safe medications can help specifically target my severe trauma-related nightmares?"
    },
    "red_flags": [
      "Severe dissociation, losing touch with reality, or experiencing violent impulses",
      "Active thoughts of self-harm or suicide"
    ]
  },
  {
    "id": "DOC-CARD-067",
    "condition": "Sepsis & Septic Shock",
    "specialty": "Infectious Disease",
    "organ_system": "Systemic / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: International Clinical Guideline",
    "source_body": "Surviving Sepsis Campaign (SCC)",
    "citation": "Evans L et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit Care Med. 2021;49(11):e1063-e1143.",
    "doi_or_source": "10.1097/CCM.0000000000005337",
    "clinical_evidence": "The 'Hour-1 Bundle' is critical for mortality reduction: 1) Measure lactate, 2) Obtain blood cultures before antibiotics, 3) Administer broad-spectrum IV antibiotics, 4) Begin rapid 30 mL/kg IV crystalloid fluid resuscitation for hypotension or lactate ≥4 mmol/L, 5) Apply vasopressors (Norepinephrine first-line) if hypotensive during/after fluids. Every hour delay in antibiotics increases mortality.",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate source control (e.g., draining abscesses, removing infected catheters, surgical debridement of necrotic tissue) within 6-12 hours of diagnosis.",
      "monitoring_cadence": "Continuous arterial blood pressure monitoring, heart rate, and urine output (target >0.5 mL/kg/hr); serial lactate measurement every 2-4 hours to guide resuscitation.",
      "clinical_thresholds": "Target mean arterial pressure (MAP) of 65 mmHg in patients requiring vasopressors."
    },
    "patient_plain_language": "Sepsis is a life-threatening emergency where the body's immune system overreacts to an infection, causing widespread inflammation that damages tissues, drops blood pressure, and shuts down organs.",
    "doctor_consultation_checklist": {
      "parameter_question": "Has the lactic acid level in the blood been checked, and is it trending downward?",
      "safety_question": "Were blood cultures drawn before starting the broad-spectrum IV antibiotics?",
      "action_threshold_question": "Is the patient's blood pressure responding to IV fluids, or will they need medications (vasopressors) to support their heart?"
    },
    "red_flags": [
      "Extreme shivering, muscle pain, no urine output all day, severe breathlessness, and mottled/discolored skin (Medical Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-068",
    "condition": "Active Tuberculosis (TB)",
    "specialty": "Pulmonology",
    "organ_system": "Respiratory / Systemic",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ATS / CDC / IDSA",
    "citation": "Nahid P et al. Official American Thoracic Society/Centers for Disease Control and Prevention/Infectious Diseases Society of America Clinical Practice Guidelines: Treatment of Drug-Susceptible Tuberculosis. Clin Infect Dis. 2016;63(7):e147-e195.",
    "doi_or_source": "10.1093/cid/ciw376",
    "clinical_evidence": "Standard treatment for drug-susceptible active TB requires a 4-drug intensive phase for 2 months (Isoniazid [INH], Rifampin [RIF], Pyrazinamide [PZA], Ethambutol [EMB]), followed by a 2-drug continuation phase for 4 months (INH and RIF). Direct Observed Therapy (DOT) is the standard of care to ensure completion and prevent multi-drug resistant TB (MDR-TB).",
    "solution_protocol": {
      "non_pharmacological_targets": "Airborne infection isolation (negative pressure room) until the patient has 3 consecutive negative sputum smears; nutritional support.",
      "monitoring_cadence": "Baseline liver enzymes (AST/ALT/Bilirubin) and monthly monitoring due to hepatotoxicity of INH, RIF, and PZA; baseline visual acuity/color vision testing due to optic neuritis risk from Ethambutol.",
      "clinical_thresholds": "Sputum culture testing monthly until two consecutive negative cultures document clearance."
    },
    "patient_plain_language": "Tuberculosis is a serious bacterial infection that usually attacks the lungs. It requires a long, uninterrupted course of multiple antibiotics over 6 months to completely kill the tough bacteria and prevent it from mutating.",
    "doctor_consultation_checklist": {
      "parameter_question": "Are my monthly liver function blood tests normal while taking these strong antibiotics?",
      "safety_question": "Are you providing Pyridoxine (Vitamin B6) to prevent nerve tingling caused by the Isoniazid?",
      "action_threshold_question": "How many negative sputum tests do I need before I am no longer contagious to my family?"
    },
    "red_flags": [
      "Coughing up significant amounts of blood, severe sudden shortness of breath",
      "Yellowing of the eyes (jaundice), severe nausea, and dark urine (Signs of medication liver toxicity)"
    ]
  },
  {
    "id": "DOC-CARD-069",
    "condition": "Syphilis",
    "specialty": "Infectious Disease",
    "organ_system": "Systemic / Genitourinary",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "CDC",
    "citation": "Workowski KA et al. Sexually Transmitted Infections Treatment Guidelines, 2021. MMWR Recomm Rep. 2021;70(4):1-187.",
    "doi_or_source": "10.15585/mmwr.rr7004a1",
    "clinical_evidence": "Parenteral Penicillin G is the only therapy with documented efficacy across all stages of syphilis. Primary, secondary, and early latent syphilis require a single dose of Benzathine penicillin G (2.4 million units IM). Late latent or unknown duration requires 3 doses spaced 1 week apart. Neurosyphilis requires aqueous crystalline penicillin G IV for 10-14 days. Doxycycline is an alternative for penicillin-allergic non-pregnant patients.",
    "solution_protocol": {
      "non_pharmacological_targets": "Abstinence from sexual contact until the chancre/lesions are completely healed and at least 7 days post-treatment; mandatory partner notification and treatment; concurrent HIV testing.",
      "monitoring_cadence": "Quantitative non-treponemal tests (RPR or VDRL) at 6, 12, and 24 months post-treatment to confirm therapeutic response.",
      "clinical_thresholds": "Successful treatment is defined as a fourfold (two-dilution) decline in the RPR or VDRL titer (e.g., from 1:32 to 1:8) by 6-12 months."
    },
    "patient_plain_language": "Syphilis is a bacterial infection typically spread by sexual contact that progresses in stages. If treated early with a specific penicillin injection, it is easily cured, but left untreated, it can permanently damage the brain and heart.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my baseline RPR titer number, so we can prove the treatment worked in 6 months?",
      "safety_question": "Am I at risk for the Jarisch-Herxheimer reaction (fever and chills) in the 24 hours after my injection?",
      "action_threshold_question": "Since I have syphilis, have I also been screened for HIV and other STIs?"
    },
    "red_flags": [
      "New onset of vision loss, hearing loss, severe headaches, or altered mental status (Signs of Neurosyphilis requiring IV therapy)"
    ]
  },
  {
    "id": "DOC-CARD-070",
    "condition": "Bacterial Meningitis",
    "specialty": "Infectious Disease",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "IDSA",
    "citation": "Tunkel AR et al. Practice Guidelines for the Management of Bacterial Meningitis. Clin Infect Dis. 2004;39(9):1267-1284. (Updates via IDSA/AAN).",
    "doi_or_source": "10.1086/425368",
    "clinical_evidence": "Empiric antimicrobial therapy (IV Ceftriaxone + IV Vancomycin; add Ampicillin if >50 years or immunocompromised for Listeria coverage) must be initiated immediately, ideally within 60 minutes of presentation. Adjunctive Dexamethasone (0.15 mg/kg IV) given before or with the first dose of antibiotics significantly reduces neurological complications and mortality in adults with S. pneumoniae meningitis.",
    "solution_protocol": {
      "non_pharmacological_targets": "Droplet precautions isolation for the first 24 hours of targeted therapy (for N. meningitidis); close monitoring in an intensive care unit (ICU); elevation of the head of the bed to 30 degrees to reduce intracranial pressure.",
      "monitoring_cadence": "Frequent neurological checks (GCS scale, pupillary response); daily review of blood and CSF culture sensitivities to de-escalate antibiotics.",
      "clinical_thresholds": "Lumbar puncture (CSF analysis) is mandatory, but brain CT is required prior to LP if there is altered mental status, papilledema, or focal neurological deficits to prevent brain herniation."
    },
    "patient_plain_language": "Bacterial meningitis is a life-threatening infection of the membranes surrounding the brain and spinal cord, causing dangerous swelling that requires immediate emergency intravenous antibiotics.",
    "doctor_consultation_checklist": {
      "parameter_question": "Did the spinal fluid analysis confirm bacterial rather than viral meningitis?",
      "safety_question": "Will close family members need prophylactic antibiotics to prevent catching the infection?",
      "action_threshold_question": "What long-term neurological monitoring (like hearing tests) will be required after recovery?"
    },
    "red_flags": [
      "Sudden high fever, severe stiff neck (inability to touch chin to chest), and a dark purple non-fading rash (Immediate Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-071",
    "condition": "Hyperthyroidism & Graves' Disease",
    "specialty": "Endocrinology",
    "organ_system": "Endocrine",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ATA",
    "citation": "Ross DS et al. 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis. Thyroid. 2016;26(10):1343-1421.",
    "doi_or_source": "10.1089/thy.2016.0229",
    "clinical_evidence": "Methimazole (MMI) is the preferred first-line antithyroid drug over Propylthiouracil (PTU) due to PTU's risk of severe hepatotoxicity (except during the first trimester of pregnancy where PTU is preferred). Beta-blockers (e.g., Atenolol, Propranolol) are strongly recommended for symptomatic control of palpitations and tremors. Radioactive iodine or thyroidectomy are definitive treatments if medications fail or are contraindicated.",
    "solution_protocol": {
      "non_pharmacological_targets": "Smoking cessation is absolutely critical, as smoking significantly worsens Graves' ophthalmopathy (eye bulging); avoidance of excess dietary iodine (kelp, seaweed).",
      "monitoring_cadence": "Free T4 and Total T3 should be assessed 2-6 weeks after initiating or adjusting therapy. TSH may remain suppressed for months and is not a reliable early marker of recovery.",
      "clinical_thresholds": "Baseline CBC and liver profile (ALT/AST/Bilirubin) required before starting MMI, to monitor for agranulocytosis or hepatotoxicity."
    },
    "patient_plain_language": "Graves' disease is an autoimmune condition where antibodies act like a broken thermostat, telling your thyroid gland to constantly pump out hormones, making your metabolism race out of control.",
    "doctor_consultation_checklist": {
      "parameter_question": "Are we monitoring my Free T4 and T3 levels, since TSH can stay artificially low for months?",
      "safety_question": "What are the warning signs of agranulocytosis (a drop in white blood cells) while taking Methimazole?",
      "action_threshold_question": "If my eyes begin to bulge or feel gritty, when should I see an ophthalmologist?"
    },
    "red_flags": [
      "Sudden severe fever, rapid heart rate >140 bpm, confusion, and agitation (Thyroid Storm: Medical Emergency)",
      "High fever and sore throat while taking Methimazole (Requires immediate CBC to check white blood cells)"
    ]
  },
  {
    "id": "DOC-CARD-072",
    "condition": "Acute Kidney Injury (AKI)",
    "specialty": "Nephrology",
    "organ_system": "Renal",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "KDIGO",
    "citation": "KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney Int Suppl. 2012;2(1):1-138. (Reaffirmed core principles).",
    "doi_or_source": "10.1038/kisup.2012.1",
    "clinical_evidence": "AKI is defined by an increase in serum creatinine by ≥0.3 mg/dL within 48 hours, or ≥1.5x baseline within 7 days, or urine output <0.5 mL/kg/hr for 6 hours. Management is strictly driven by the cause (Pre-renal, Intrinsic, Post-renal). Rapid IV crystalloid volume expansion is required for hypovolemic pre-renal AKI. Nephrotoxic medications (NSAIDs, ACEi/ARBs, contrast) must be immediately discontinued.",
    "solution_protocol": {
      "non_pharmacological_targets": "Meticulous fluid balance tracking (strict inputs and outputs); renal ultrasound to rule out post-renal obstruction (e.g., enlarged prostate, kidney stones); adjustment of all renally cleared medications.",
      "monitoring_cadence": "Daily (or twice daily) serum creatinine, BUN, and electrolyte panels (especially potassium).",
      "clinical_thresholds": "Indications for urgent dialysis (AEIOU): Acidosis (severe), Electrolyte abnormalities (severe hyperkalemia), Intoxications, Overload of fluid, Uremia symptoms (pericarditis, encephalopathy)."
    },
    "patient_plain_language": "Acute kidney injury is a sudden drop in kidney function, often caused by severe dehydration, toxic medications, or a blockage, which prevents the kidneys from filtering toxins and making urine.",
    "doctor_consultation_checklist": {
      "parameter_question": "Have we paused my blood pressure pills (like ACE inhibitors) and ibuprofen until my kidneys recover?",
      "safety_question": "Did my kidney ultrasound show any blockages in my urinary tract?",
      "action_threshold_question": "Are my potassium levels safe, or do I need dietary restrictions or dialysis?"
    },
    "red_flags": [
      "Complete cessation of urine output for over 12 hours",
      "Severe shortness of breath, confusion, and nausea (Uremic syndrome or fluid in lungs)"
    ]
  },
  {
    "id": "DOC-CARD-073",
    "condition": "Idiopathic Pulmonary Fibrosis (IPF)",
    "specialty": "Pulmonology",
    "organ_system": "Respiratory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: International Clinical Guideline",
    "source_body": "ATS / ERS / JRS / ALAT",
    "citation": "Raghu G et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med. 2022;205(9):e18-e47.",
    "doi_or_source": "10.1164/rccm.202202-0399ST",
    "clinical_evidence": "Antifibrotic medications, Nintedanib (tyrosine kinase inhibitor) and Pirfenidone, are strongly recommended as they significantly slow the rate of Forced Vital Capacity (FVC) decline by approximately 50% (INPULSIS and ASCEND trials). Corticosteroids combined with immunosuppressants (azathioprine) are strongly recommended AGAINST, as they increase mortality and hospitalizations in IPF.",
    "solution_protocol": {
      "non_pharmacological_targets": "Pulmonary rehabilitation; long-term oxygen therapy for resting hypoxemia (SpO2 ≤88%); gastroesophageal reflux management (micro-aspiration contributes to fibrosis); early evaluation for lung transplantation.",
      "monitoring_cadence": "Pulmonary function tests (PFTs) assessing FVC and DLCO every 3-6 months.",
      "clinical_thresholds": "Diagnosis requires High-Resolution CT (HRCT) showing a Usual Interstitial Pneumonia (UIP) pattern (honeycombing, traction bronchiectasis) in the absence of alternative causes."
    },
    "patient_plain_language": "Idiopathic pulmonary fibrosis is a progressive disease where the delicate air sacs in the lungs become thick, stiff, and scarred like a dried sponge, making it difficult for oxygen to enter the bloodstream.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my current Forced Vital Capacity (FVC) percentage, and how fast is it declining?",
      "safety_question": "What are the common liver and gastrointestinal side effects of my antifibrotic medications?",
      "action_threshold_question": "At what oxygen saturation level during walking should I be prescribed home oxygen therapy?"
    },
    "red_flags": [
      "Sudden worsening of shortness of breath and cough over a few days (Acute Exacerbation of IPF, highly lethal)"
    ]
  },
  {
    "id": "DOC-CARD-074",
    "condition": "Heart Failure with Preserved Ejection Fraction (HFpEF)",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 2,
    "evidence_tier": "Level 2: Multicenter Phase 3 Double-Blind RCT",
    "source_body": "NEJM (EMPEROR-Preserved)",
    "citation": "Anker SD et al. Empagliflozin in Heart Failure with a Preserved Ejection Fraction. N Engl J Med. 2021;385:1451-1461.",
    "doi_or_source": "10.1056/NEJMoa2107038",
    "clinical_evidence": "In the EMPEROR-Preserved trial, Empagliflozin (SGLT2 inhibitor) reduced the combined risk of cardiovascular death or hospitalization for heart failure by 21% (HR 0.79; p<0.001) in patients with LVEF >40%. SGLT2 inhibitors (Empagliflozin, Dapagliflozin) are now the first proven disease-modifying therapy for HFpEF and are Class 2a recommendations in AHA/ACC guidelines. Loop diuretics (Furosemide) remain essential for symptom relief of congestion.",
    "solution_protocol": {
      "non_pharmacological_targets": "Aggressive management of comorbidities (hypertension, obesity, atrial fibrillation); sodium restriction (<2,000 mg/day); cardiac rehabilitation emphasizing aerobic capacity.",
      "monitoring_cadence": "Monitor BNP/NT-proBNP levels and renal function following initiation of diuretic or SGLT2i therapy.",
      "clinical_thresholds": "Diagnosis confirmed via echocardiography showing LVEF ≥50% with evidence of diastolic dysfunction (e.g., elevated filling pressures, left atrial enlargement) and elevated BNP."
    },
    "patient_plain_language": "In HFpEF (diastolic heart failure), your heart pumps with normal strength, but the heart muscle is too stiff to relax and fill with enough blood between beats, causing fluid to back up into the lungs and legs.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my echocardiogram show that my heart muscle is stiff or my left atrium is enlarged?",
      "safety_question": "Will adding an SGLT2 inhibitor lower my blood sugar too much if I do not have diabetes?",
      "action_threshold_question": "How should I adjust my daily water pill (diuretic) if my morning weight jumps up by 3 pounds?"
    },
    "red_flags": [
      "Waking up gasping for air in the middle of the night (Paroxysmal Nocturnal Dyspnea)",
      "Sudden extreme swelling in the legs, abdomen, and inability to lie flat without coughing"
    ]
  },
  {
    "id": "DOC-CARD-075",
    "condition": "Parkinson's Disease",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "MDS",
    "citation": "Fox SH et al. International Parkinson and Movement Disorder Society Evidence-Based Medicine Review: Update on Treatments for the Motor Symptoms of Parkinson's Disease. Mov Disord. 2018;33(8):1248-1266.",
    "doi_or_source": "10.1002/mds.27372",
    "clinical_evidence": "Levodopa/Carbidopa remains the most effective symptomatic treatment for motor symptoms (bradykinesia, rigidity). To delay levodopa-induced motor complications (dyskinesias, 'wearing-off' periods), dopamine agonists (Pramipexole, Ropinirole) or MAO-B inhibitors (Rasagiline) may be used as initial monotherapy in younger patients, though they carry risks of impulse control disorders and hallucinations.",
    "solution_protocol": {
      "non_pharmacological_targets": "Intensive physical therapy focusing on large amplitude movements (e.g., LSVT BIG therapy); speech therapy; fall prevention evaluation; high-fiber diet to combat severe autonomic constipation.",
      "monitoring_cadence": "Clinical assessment every 3-6 months to adjust timing and dosing of levodopa to minimize 'off' periods.",
      "clinical_thresholds": "Deep Brain Stimulation (DBS) of the subthalamic nucleus is indicated for advanced PD with severe motor fluctuations and disabling dyskinesias not controlled by optimized medical therapy."
    },
    "patient_plain_language": "Parkinson's disease occurs when the brain slowly stops producing dopamine, a chemical essential for smooth, coordinated muscle movements, leading to tremors, stiffness, and slow movement.",
    "doctor_consultation_checklist": {
      "parameter_question": "Should my medication be dosed more frequently throughout the day to prevent 'wearing off' before the next pill?",
      "safety_question": "Could my dopamine medications cause impulsive behaviors like gambling or excessive shopping?",
      "action_threshold_question": "When do motor fluctuations become severe enough that we should consider Deep Brain Stimulation surgery?"
    },
    "red_flags": [
      "Sudden inability to move (freezing of gait) leading to dangerous falls",
      "New onset of visual hallucinations or severe confusion (Possible medication toxicity or Lewy Body progression)"
    ]
  },
  {
    "id": "DOC-CARD-076",
    "condition": "Fibromyalgia",
    "specialty": "Rheumatology",
    "organ_system": "Systemic / Neurological",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACR / EULAR",
    "citation": "Macfarlane GJ et al. EULAR Revised Recommendations for the Management of Fibromyalgia. Ann Rheum Dis. 2017;76(2):318-328.",
    "doi_or_source": "10.1136/annrheumdis-2016-209724",
    "clinical_evidence": "Non-pharmacological therapies (specifically graded aerobic exercise) have the highest evidence level (Grade A) and are the only universally recommended first-line therapy. Pharmacotherapy is tailored to specific symptoms: Duloxetine or Milnacipran (SNRIs) for depression/pain; Pregabalin for sleep/pain. Strong recommendations strictly oppose the use of opioids and strong analgesics, which worsen central sensitization and hyperalgesia.",
    "solution_protocol": {
      "non_pharmacological_targets": "Graded, low-impact aerobic exercise (aquatic therapy, walking, cycling); Cognitive Behavioral Therapy (CBT) to reduce pain catastrophizing; mindfulness and sleep hygiene optimization.",
      "monitoring_cadence": "Reassess functional capacity and symptom severity at 4-6 week intervals using the Fibromyalgia Impact Questionnaire (FIQ).",
      "clinical_thresholds": "Diagnosis relies on the 2016 ACR criteria (Widespread Pain Index and Symptom Severity Scale), without requiring tender point examinations."
    },
    "patient_plain_language": "Fibromyalgia is a central nervous system disorder where the brain's pain-processing center acts like a stereo with the volume turned up too high, causing widespread body pain, fatigue, and brain fog without visible tissue damage.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my lab work definitely rule out inflammatory arthritis or thyroid issues?",
      "safety_question": "Why are opioid pain medications actually harmful for the specific type of nerve pain in Fibromyalgia?",
      "action_threshold_question": "Can I get a referral for a physical therapist trained specifically in graded aquatic exercise?"
    },
    "red_flags": [
      "Sudden localized joint swelling, high fever, or progressive muscle weakness (Signs that the pain is NOT fibromyalgia)"
    ]
  },
  {
    "id": "DOC-CARD-077",
    "condition": "Gallstone Disease (Cholelithiasis & Cholecystitis)",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "EASL",
    "citation": "European Association for the Study of the Liver (EASL). EASL Clinical Practice Guidelines on the Prevention, Diagnosis and Treatment of Gallstones. J Hepatol. 2016;65(1):146-181.",
    "doi_or_source": "10.1016/j.jhep.2016.03.005",
    "clinical_evidence": "Asymptomatic gallstones should generally not be treated or followed (except in specific high-risk populations). For symptomatic biliary colic, laparoscopic cholecystectomy is the definitive treatment. In cases of acute cholecystitis, early laparoscopic cholecystectomy (within 72 hours of admission) is superior to delayed surgery, reducing hospital stay and complications. Ursodeoxycholic acid has limited utility, reserved for non-surgical candidates with small radiolucent stones.",
    "solution_protocol": {
      "non_pharmacological_targets": "For symptomatic patients awaiting surgery: dietary fat restriction to prevent gallbladder contraction; gradual weight loss (rapid weight loss >1.5 kg/week promotes gallstone formation).",
      "monitoring_cadence": "Abdominal ultrasound is the primary diagnostic modality (sensitivity >95% for stones >2mm).",
      "clinical_thresholds": "Common bile duct stones (choledocholithiasis) require ERCP stone extraction prior to or during cholecystectomy."
    },
    "patient_plain_language": "Gallstones are hard, pebble-like deposits of cholesterol or bilirubin that form in the gallbladder. If they block the duct where bile exits, they cause severe cramping pain after eating fatty foods.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my ultrasound show any thickening of the gallbladder wall or stones blocking the main bile duct?",
      "safety_question": "Should I maintain a strictly low-fat diet to prevent pain attacks until my surgery date?",
      "action_threshold_question": "What specific symptoms mean a stone is trapped and I need emergency surgery?"
    },
    "red_flags": [
      "Fever, chills, and severe right upper abdominal pain (Acute Cholecystitis)",
      "Yellowing of the skin/eyes (jaundice), dark urine, and light-colored stools (Bile Duct Obstruction)",
      "Charcot's triad: Fever, right upper quadrant pain, and jaundice (Acute Cholangitis Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-078",
    "condition": "Schizophrenia",
    "specialty": "Psychiatry",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "APA",
    "citation": "Keepers GA et al. The American Psychiatric Association Practice Guideline for the Treatment of Patients With Schizophrenia. Am J Psychiatry. 2020;177(9):868-872.",
    "doi_or_source": "10.1176/appi.ajp.2020.177901",
    "clinical_evidence": "Second-generation antipsychotics (SGAs: e.g., Risperidone, Olanzapine, Aripiprazole) are first-line for acute exacerbations and maintenance. Clozapine is strictly indicated for treatment-resistant schizophrenia (failure of 2 adequate antipsychotic trials) or patients with high suicide risk, due to risk of severe agranulocytosis. Long-acting injectable (LAI) antipsychotics are strongly recommended for patients with history of relapse related to nonadherence.",
    "solution_protocol": {
      "non_pharmacological_targets": "Cognitive Behavioral Therapy for psychosis (CBTp); supported employment programs; family psychoeducation; Assertive Community Treatment (ACT) for patients with frequent hospitalizations.",
      "monitoring_cadence": "Metabolic monitoring (weight, BMI, fasting glucose/HbA1c, fasting lipids) at baseline, 3 months, and annually, as SGAs carry high risks for metabolic syndrome.",
      "clinical_thresholds": "Absolute Neutrophil Count (ANC) must be monitored weekly to monthly (via REMS program) for any patient prescribed Clozapine."
    },
    "patient_plain_language": "Schizophrenia is a severe brain disorder that interferes with a person's ability to think clearly, manage emotions, make decisions, and relate to others, often causing hallucinations (hearing voices) or delusions.",
    "doctor_consultation_checklist": {
      "parameter_question": "Are we tracking my blood sugar and cholesterol, since my medication can affect my metabolism?",
      "safety_question": "If I struggle to remember to take my daily pill, am I a candidate for a once-a-month injectable medication?",
      "action_threshold_question": "How can my family learn to identify the early warning signs (prodrome) of a relapse before I need hospitalization?"
    },
    "red_flags": [
      "Command hallucinations ordering the person to harm themselves or others",
      "Severe muscle rigidity, high fever, and altered mental status (Neuroleptic Malignant Syndrome: Emergency)"
    ]
  },
  {
    "id": "DOC-CARD-079",
    "condition": "Diabetic Peripheral Neuropathy",
    "specialty": "Neurology",
    "organ_system": "Nervous / Endocrine",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ADA",
    "citation": "Pop-Busui R et al. Diabetic Neuropathy: A Position Statement by the American Diabetes Association. Diabetes Care. 2017;40(1):136-154. (Updated in 2024 Standards of Care).",
    "doi_or_source": "10.2337/dc16-2042",
    "clinical_evidence": "Tight glycemic control is the only disease-modifying strategy proven to prevent or delay the progression of diabetic neuropathy. For symptomatic neuropathic pain, Pregabalin, Duloxetine, or Gabapentin are recommended as initial pharmacological treatments (Grade A). Opioids (including Tramadol) are not recommended as first or second-line agents due to high risks of addiction and complications.",
    "solution_protocol": {
      "non_pharmacological_targets": "Daily comprehensive foot inspections using a mirror; proper diabetic footwear to prevent pressure ulcers; avoidance of walking barefoot; smoking cessation (smoking restricts microvascular blood flow to the nerves).",
      "monitoring_cadence": "Annual comprehensive foot exam including 10-g monofilament testing, vibration sense (128-Hz tuning fork), and ankle reflexes.",
      "clinical_thresholds": "Target HbA1c <7.0% to halt progressive microvascular nerve damage."
    },
    "patient_plain_language": "Diabetic neuropathy occurs when chronic high blood sugar damages the tiny blood vessels that feed your nerves, typically starting in the longest nerves (the toes and feet), causing burning pain, tingling, or dangerous numbness.",
    "doctor_consultation_checklist": {
      "parameter_question": "Did my annual exam include the 10-gram monofilament test to check for protective sensation in my feet?",
      "safety_question": "How can I get custom diabetic shoes to prevent unnoticed blisters from turning into infected ulcers?",
      "action_threshold_question": "If nerve pain medications make me dizzy or sleepy, how should we adjust the dose?"
    },
    "red_flags": [
      "A new ulcer, blister, or cut on the foot that is not healing, draining pus, or turning black",
      "A foot that suddenly becomes red, hot, and swollen (Charcot neuroarthropathy or severe infection)"
    ]
  },
  {
    "id": "DOC-CARD-080",
    "condition": "Chronic Venous Insufficiency (CVI) & Varicose Veins",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "SVS / AVF",
    "citation": "Gloviczki P et al. The Care of Patients with Varicose Veins and Associated Chronic Venous Diseases: Clinical Practice Guidelines of the Society for Vascular Surgery and the American Venous Forum. J Vasc Surg. 2011;53(5 Suppl):2S-48S.",
    "doi_or_source": "10.1016/j.jvs.2011.01.079",
    "clinical_evidence": "Compression therapy (20-30 mmHg graduated compression stockings) is the primary conservative treatment to reduce edema and pain, and is mandatory to promote the healing of venous stasis ulcers (Grade 1B). For symptomatic varicose veins with documented axial reflux, endovenous thermal ablation (laser or radiofrequency) is recommended over surgical stripping due to reduced convalescence and lower complication rates (Grade 1B).",
    "solution_protocol": {
      "non_pharmacological_targets": "Leg elevation above heart level for 30 minutes, 3-4 times daily; calf muscle pump exercises (walking, ankle flexes); avoidance of prolonged standing or sitting.",
      "monitoring_cadence": "Venous duplex ultrasound evaluation to map the exact location of valvular reflux prior to any intervention.",
      "clinical_thresholds": "CEAP classification guides management: C2 (varicose veins) to C6 (active venous ulcer). Intervention is highly recommended for C4-C6 disease."
    },
    "patient_plain_language": "Chronic venous insufficiency happens when the one-way valves in your leg veins fail. Instead of pumping blood back up to the heart, gravity pulls the blood back down, causing it to pool and stretch the veins, leading to swelling, aching, and skin damage.",
    "doctor_consultation_checklist": {
      "parameter_question": "Does my leg ultrasound show which specific vein valves are failing to pump blood upward?",
      "safety_question": "What strength of graduated compression stockings (mmHg) do I need, and how do I put them on correctly?",
      "action_threshold_question": "If conservative measures fail, am I a candidate for minimally invasive endovenous laser therapy?"
    },
    "red_flags": [
      "A leg ulcer that begins draining heavy yellow fluid, smells foul, or is surrounded by hot red skin (Infection)",
      "Sudden, painful swelling of just one leg, especially the calf, which feels hard (Possible Deep Vein Thrombosis)"
    ]
  },

  # ── LIST 3 (081 - 100) ────────────────────────────────────────────
  {
    "id": "DOC-CARD-081",
    "condition": "Non-ST-Elevation Acute Coronary Syndrome (NSTEMI / Unstable Angina)",
    "specialty": "Cardiovascular",
    "organ_system": "Circulatory",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AHA / ACC",
    "citation": "Amsterdam EA et al. 2014 AHA/ACC Guideline for the Management of Patients with Non-ST-Elevation Acute Coronary Syndromes. Circulation. 2014;130(25):e344-e426. (Updated 2021).",
    "doi_or_source": "10.1161/CIR.0000000000000134",
    "clinical_evidence": "Unlike STEMI, NSTEMI does not show ST-segment elevation on ECG but is characterized by elevated cardiac troponins. Dual antiplatelet therapy (DAPT: Aspirin + P2Y12 inhibitor like Ticagrelor) and systemic anticoagulation (Heparin/Enoxaparin) are first-line. An early invasive strategy (cardiac catheterization within 24 hours) is indicated for patients with high-risk features (TIMI/GRACE scores) such as refractory ischemia or hemodynamic instability.",
    "solution_protocol": {
      "non_pharmacological_targets": "Bed rest with continuous telemetry monitoring; supplemental oxygen only if SpO2 < 90%; strict cardiac diet upon oral feeding resumption.",
      "monitoring_cadence": "Serial high-sensitivity cardiac troponins (hs-cTn) at 0, 1, and 3 hours to detect delta (change) indicating acute myocardial injury.",
      "clinical_thresholds": "Immediate upgrade to urgent catheterization if patient develops new ST elevations, cardiogenic shock, or sustained ventricular arrhythmias."
    },
    "patient_plain_language": "An NSTEMI is a type of heart attack where a cholesterol plaque ruptures and partially blocks a heart artery, causing heart muscle damage without completely stopping all blood flow.",
    "doctor_consultation_checklist": {
      "parameter_question": "What did my serial troponin blood tests show regarding heart muscle damage?",
      "safety_question": "How long will I need to remain on two different types of blood thinners (DAPT) after discharge?",
      "action_threshold_question": "Based on my risk score, will I need an angiogram to look for blockages that require a stent?"
    },
    "red_flags": [
      "Return of crushing chest pressure at rest while in the hospital",
      "Sudden shortness of breath, dizziness, and cold sweats"
    ]
  },
  {
    "id": "DOC-CARD-082",
    "condition": "Anaphylaxis",
    "specialty": "Infectious Disease",
    "organ_system": "Systemic / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAAAI / ACAAI / WAO",
    "citation": "Shaker MS et al. Anaphylaxis-a 2020 practice parameter update, systematic review, and Grading of Recommendations, Assessment, Development and Evaluation (GRADE) analysis. J Allergy Clin Immunol. 2020;145(4):1082-1123.",
    "doi_or_source": "10.1016/j.jaci.2020.01.017",
    "clinical_evidence": "Epinephrine (intramuscular into the anterolateral thigh) is the only first-line treatment for anaphylaxis. Antihistamines (H1/H2 blockers) and corticosteroids are second-line adjunctive therapies that do not treat the life-threatening respiratory or cardiovascular compromise of anaphylaxis and must never delay epinephrine administration. A second dose of epinephrine may be required in 5-15 minutes if symptoms do not improve.",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate removal of the trigger if possible (e.g., stopping an IV drug infusion, removing a stinger); place patient in a supine position with legs elevated (unless causing respiratory distress) to prevent empty vena cava syndrome.",
      "monitoring_cadence": "Continuous pulse oximetry, blood pressure, and cardiac monitoring; observe for 4-6 hours post-resolution for biphasic reactions.",
      "clinical_thresholds": "Anaphylaxis is diagnosed by acute onset involving skin/mucosal tissue PLUS either respiratory compromise, reduced blood pressure, or severe gastrointestinal symptoms."
    },
    "patient_plain_language": "Anaphylaxis is a severe, whole-body allergic reaction that happens rapidly. It can cause your throat to swell shut and your blood pressure to drop dangerously low. Epinephrine is the only medicine that can reverse it quickly.",
    "doctor_consultation_checklist": {
      "parameter_question": "Can we arrange for allergy testing to definitively identify my severe triggers?",
      "safety_question": "How do I properly carry, store, and use an epinephrine auto-injector?",
      "action_threshold_question": "Should I have a personalized anaphylaxis action plan to give to my child's school?"
    },
    "red_flags": [
      "Feeling of a lump in the throat, wheezing, or difficulty swallowing",
      "Feeling faint, dizzy, or a sense of impending doom (Immediate 911 / Epinephrine required)"
    ]
  },
  {
    "id": "DOC-CARD-083",
    "condition": "Acute Diverticulitis",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AGA",
    "citation": "Peery AF et al. American Gastroenterological Association Institute Guideline on the Management of Acute Diverticulitis. Gastroenterology. 2015;149(7):1944-1949. (Reaffirmed).",
    "doi_or_source": "10.1053/j.gastro.2015.10.003",
    "clinical_evidence": "For acute uncomplicated diverticulitis in immunocompetent patients, routine use of antibiotics is no longer recommended, as RCTs show no improvement in recovery time or prevention of complications (Grade: Conditional). Management relies on clear liquid diet and pain control. Antibiotics (e.g., Ciprofloxacin + Metronidazole) are reserved for complicated cases (abscess, perforation) or high-risk patients.",
    "solution_protocol": {
      "non_pharmacological_targets": "Clear liquid diet for 2-3 days during acute flares, advancing to a low-fiber diet as symptoms resolve; once fully recovered, transition to a high-fiber diet to prevent recurrence.",
      "monitoring_cadence": "Clinical re-evaluation in 2-3 days. A screening colonoscopy is recommended 6-8 weeks after resolution of the first episode to rule out masked colorectal cancer.",
      "clinical_thresholds": "CT scan of the abdomen and pelvis with IV contrast is the imaging modality of choice to distinguish uncomplicated from complicated disease (Hinchey classification)."
    },
    "patient_plain_language": "Diverticulitis happens when small, bulging pouches in the lining of your large intestine become inflamed or infected, usually causing severe pain in the lower left side of the belly.",
    "doctor_consultation_checklist": {
      "parameter_question": "Did my CT scan show uncomplicated inflammation or a complicated infection like an abscess?",
      "safety_question": "Why are antibiotics no longer automatically prescribed for mild cases?",
      "action_threshold_question": "When should I schedule my follow-up colonoscopy to ensure there are no hidden issues?"
    },
    "red_flags": [
      "Rigid, board-like abdomen with severe pain upon releasing pressure (Rebound tenderness / Peritonitis)",
      "High fever, inability to keep fluids down, and lack of bowel movements"
    ]
  },
  {
    "id": "DOC-CARD-084",
    "condition": "Giant Cell Arteritis (Temporal Arteritis)",
    "specialty": "Rheumatology",
    "organ_system": "Vascular / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACR",
    "citation": "Maz M et al. 2021 American College of Rheumatology/Vasculitis Foundation Guideline for the Management of Giant Cell Arteritis and Takayasu Arteritis. Arthritis Rheumatol. 2021;73(8):1349-1365.",
    "doi_or_source": "10.1002/art.41774",
    "clinical_evidence": "GCA is a medical emergency due to the high risk of irreversible blindness. High-dose systemic glucocorticoids (Prednisone 40-60 mg/day; IV Methylprednisolone if visual symptoms are present) must be started immediately upon clinical suspicion, before biopsy confirmation. Tocilizumab (IL-6 receptor antagonist) combined with a steroid taper is strongly recommended over steroids alone to reduce cumulative steroid toxicity and flares.",
    "solution_protocol": {
      "non_pharmacological_targets": "Given high-dose steroid requirements: calcium and vitamin D supplementation; bone density monitoring; blood glucose monitoring.",
      "monitoring_cadence": "ESR and CRP monitoring every 2-4 weeks during the initial steroid taper; Temporal artery biopsy should ideally be performed within 1-2 weeks of starting steroids.",
      "clinical_thresholds": "Diagnosis supported by new-onset localized headache, jaw claudication, visual symptoms, and elevated ESR >50 mm/hr in adults >50 years old."
    },
    "patient_plain_language": "Giant cell arteritis is severe inflammation of the blood vessels in your scalp, neck, and arms. If the inflammation blocks the artery supplying the eye, it can cause sudden, permanent blindness.",
    "doctor_consultation_checklist": {
      "parameter_question": "What are my current ESR and CRP inflammation levels, and are they responding to steroids?",
      "safety_question": "How are we protecting my bones and blood sugar while I am on high doses of steroids?",
      "action_threshold_question": "Can I be referred for a temporal artery biopsy to confirm the diagnosis without delaying my treatment?"
    },
    "red_flags": [
      "Sudden blurriness, double vision, or a dark curtain falling over the vision of one eye",
      "Severe pain in the jaw muscles while chewing (Jaw Claudication)"
    ]
  },
  {
    "id": "DOC-CARD-085",
    "condition": "Primary Open-Angle Glaucoma (POAG)",
    "specialty": "Neurology",
    "organ_system": "Visual",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAO",
    "citation": "American Academy of Ophthalmology Preferred Practice Pattern Glaucoma Panel. Primary Open-Angle Glaucoma Preferred Practice Pattern. Ophthalmology. 2021;128(1):P71-P150.",
    "doi_or_source": "10.1016/j.ophtha.2020.10.022",
    "clinical_evidence": "Lowering intraocular pressure (IOP) is the only proven method to slow visual field loss. Topical prostaglandin analogs (Latanoprost, Bimatoprost) are the preferred first-line medical therapy due to once-daily dosing and high efficacy (lowering IOP by 25-33%). Selective laser trabeculoplasty (SLT) is equally effective as a first-line alternative to eye drops (LiGHT Trial, The Lancet).",
    "solution_protocol": {
      "non_pharmacological_targets": "Proper eye drop administration technique (nasolacrimal occlusion for 1-2 minutes after instillation to minimize systemic absorption and side effects); avoidance of inverted yoga positions which spike IOP.",
      "monitoring_cadence": "Check IOP, optic nerve head status (OCT imaging), and visual fields every 3-12 months depending on disease severity and target IOP achievement.",
      "clinical_thresholds": "Target IOP is typically set 20-30% below the pre-treatment baseline pressure, adjusted dynamically based on visual field progression."
    },
    "patient_plain_language": "Open-angle glaucoma is a slow, painless disease where fluid builds up inside the eye, raising the pressure and gradually damaging the optic nerve, slowly stealing your peripheral (side) vision.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my target eye pressure number, and are my current drops keeping me below it?",
      "safety_question": "Am I demonstrating the correct technique to close my tear duct after putting in drops so the medicine stays in my eye?",
      "action_threshold_question": "Would I be a candidate for laser treatment (SLT) to reduce how many daily drops I need to take?"
    },
    "red_flags": [
      "Noticing you are bumping into doorframes or missing things to your left or right (Peripheral vision loss)",
      "Severe eye pain, redness, and halos around lights (Indicates Angle-Closure Glaucoma, a different, acute emergency)"
    ]
  },
  {
    "id": "DOC-CARD-086",
    "condition": "Age-Related Macular Degeneration (AMD)",
    "specialty": "Neurology",
    "organ_system": "Visual",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline & Landmark RCT",
    "source_body": "AAO & NEJM (AREDS2)",
    "citation": "American Academy of Ophthalmology Retina/Vitreous Panel. Age-Related Macular Degeneration Preferred Practice Pattern. Ophthalmology. 2019;127(1):P1-P65; AREDS2 Research Group. JAMA. 2013;309(19):2005-2015.",
    "doi_or_source": "10.1016/j.ophtha.2019.09.024",
    "clinical_evidence": "For intermediate dry AMD, AREDS2 antioxidant vitamin formulation (Vitamin C, E, Lutein, Zeaxanthin, Zinc, Copper) reduces the 5-year risk of progression to advanced AMD by 25%. For advanced 'wet' (neovascular) AMD, intravitreal anti-VEGF injections (Bevacizumab, Ranibizumab, Aflibercept) are the standard of care, preventing severe vision loss in over 90% of patients and improving vision in 30%.",
    "solution_protocol": {
      "non_pharmacological_targets": "Absolute smoking cessation (smoking doubles AMD risk and accelerates progression); UV protection (sunglasses); diet rich in green leafy vegetables (lutein) and omega-3 fatty acids.",
      "monitoring_cadence": "Daily self-monitoring of central vision using an Amsler Grid; regular dilated retinal exams and Optical Coherence Tomography (OCT) every 4-6 weeks during active wet AMD treatment.",
      "clinical_thresholds": "Conversion from 'dry' to 'wet' AMD is marked by new fluid or hemorrhage under the retina on OCT, requiring immediate anti-VEGF therapy."
    },
    "patient_plain_language": "Macular degeneration damages the macula—the center part of the retina responsible for sharp, straight-ahead vision needed for reading and recognizing faces. It does not cause complete darkness, but rather a blurry or missing spot in the center of your sight.",
    "doctor_consultation_checklist": {
      "parameter_question": "Do I have 'dry' or 'wet' macular degeneration, and what stage is it currently?",
      "safety_question": "Should I be taking the specific AREDS2 eye vitamin formula based on my stage of disease?",
      "action_threshold_question": "How do I use an Amsler Grid at home, and what changes should prompt an immediate clinic visit?"
    },
    "red_flags": [
      "Straight lines suddenly appearing wavy or bent (Metamorphopsia)",
      "A new, rapidly expanding dark or blank spot in the direct center of your vision"
    ]
  },
  {
    "id": "DOC-CARD-087",
    "condition": "Bell's Palsy (Idiopathic Facial Paralysis)",
    "specialty": "Neurology",
    "organ_system": "Nervous",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAN",
    "citation": "Baugh RF et al. Clinical Practice Guideline: Bell's Palsy. Otolaryngol Head Neck Surg. 2013;149(3 Suppl):S1-27. (AAN Endorsed).",
    "doi_or_source": "10.1177/0194599813505967",
    "clinical_evidence": "Oral corticosteroids (e.g., Prednisone 60 mg/day for 5 days, then tapered) initiated within 72 hours of symptom onset significantly increase the probability of complete facial nerve recovery (Grade A). The addition of antiviral therapy (valacyclovir) provides only modest, conditional benefit for severe cases (House-Brackmann grade V-VI) but should not be used as monotherapy.",
    "solution_protocol": {
      "non_pharmacological_targets": "Eye protection is paramount: rigorous use of artificial tears during the day, lubricating ointment at night, and physically taping the affected eyelid shut during sleep to prevent corneal abrasions/ulceration.",
      "monitoring_cadence": "Follow-up at 1 month to assess nerve recovery and ensure no corneal damage has occurred.",
      "clinical_thresholds": "If facial paralysis spares the forehead (i.e., the patient can wrinkle their forehead normally on the paralyzed side), Bell's palsy is excluded, and acute stroke must be evaluated immediately."
    },
    "patient_plain_language": "Bell's palsy is a sudden, temporary weakness or paralysis of the muscles on one side of your face, believed to be caused by a viral infection that swells the facial nerve.",
    "doctor_consultation_checklist": {
      "parameter_question": "Was I started on oral steroids within the critical 72-hour window?",
      "safety_question": "How exactly do I apply eye tape and lubricants at night to protect my eye from drying out?",
      "action_threshold_question": "If I see no improvement after several months, what nerve-testing or physical therapy options exist?"
    },
    "red_flags": [
      "Paralysis of the lower face while the forehead moves normally (Sign of Stroke)",
      "Redness, severe pain, or a scratchy feeling in the eye on the paralyzed side (Corneal ulceration)"
    ]
  },
  {
    "id": "DOC-CARD-088",
    "condition": "Carpal Tunnel Syndrome",
    "specialty": "Neurology",
    "organ_system": "Nervous / Musculoskeletal",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAOS",
    "citation": "American Academy of Orthopaedic Surgeons. Management of Carpal Tunnel Syndrome Evidence-Based Clinical Practice Guideline. 2016.",
    "doi_or_source": "https://www.aaos.org/globalassets/quality-and-practice-resources/carpal-tunnel/cts-cpg.pdf",
    "clinical_evidence": "First-line conservative management includes neutral-angle wrist splinting (worn primarily at night) and local corticosteroid injections, which provide robust short-to-medium term relief (Grade Strong). Oral NSAIDs, diuretics, and gabapentin are not recommended. For patients with severe nerve compression (muscle atrophy) or those failing conservative therapy, surgical carpal tunnel release provides excellent long-term outcomes.",
    "solution_protocol": {
      "non_pharmacological_targets": "Ergonomic workplace modifications (keyboard/mouse alignment); nocturnal volar wrist splinting; nerve gliding exercises.",
      "monitoring_cadence": "Reassess symptoms after 4-6 weeks of splinting. Consider Electromyography (EMG) and Nerve Conduction Studies (NCS) to quantify nerve damage if surgery is considered.",
      "clinical_thresholds": "Thenar atrophy (wasting of the thumb base muscle) or persistent sensory loss mandates urgent surgical evaluation to prevent irreversible nerve death."
    },
    "patient_plain_language": "Carpal tunnel syndrome occurs when the median nerve is squeezed or compressed as it travels through a narrow passageway in your wrist, causing numbness, tingling, and weakness in your hand.",
    "doctor_consultation_checklist": {
      "parameter_question": "Do my symptoms warrant a nerve conduction study (EMG) to measure the exact level of nerve trapping?",
      "safety_question": "Am I wearing my wrist splint in a truly neutral position (not bent backward) during sleep?",
      "action_threshold_question": "At what point of numbness or muscle weakness should we stop injections and consider a simple release surgery?"
    },
    "red_flags": [
      "Visible shrinking or flattening of the muscle at the base of the thumb (Thenar Atrophy)",
      "Dropping objects frequently due to loss of hand strength and grip"
    ]
  },
  {
    "id": "DOC-CARD-089",
    "condition": "Mild Traumatic Brain Injury (Concussion)",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "CDC & AAN",
    "citation": "Lumba-Brown A et al. Centers for Disease Control and Prevention Guideline on the Diagnosis and Management of Mild Traumatic Brain Injury Among Children. JAMA Pediatr. 2018;172(11):e182853.",
    "doi_or_source": "10.1001/jamapediatrics.2018.2853",
    "clinical_evidence": "Routine neuroimaging (CT/MRI) is NOT recommended for mild TBI without red-flag symptoms, to avoid unnecessary radiation exposure (Grade A). Complete physical and cognitive rest beyond 2-3 days is discouraged; early, gradually escalating light aerobic activity speeds recovery compared to strict rest (cocooning).",
    "solution_protocol": {
      "non_pharmacological_targets": "Graduated Return-to-Learn and Return-to-Play protocols; strict avoidance of any activity with a risk of secondary head impact until fully cleared; optimization of sleep; limitation of screen time only if it provokes symptoms.",
      "monitoring_cadence": "Close observation for the first 24 hours; reassess symptom resolution using standardized tools (e.g., SCAT5/SCAT6) prior to advancing activity stages.",
      "clinical_thresholds": "Clearance for contact sports requires the patient to be completely asymptomatic at rest and during maximal physical exertion without the use of pain medications."
    },
    "patient_plain_language": "A concussion is a mild brain injury caused by a jolt to the head that disrupts normal brain function. The brain needs a few days of calm, followed by a gradual return to light activities to heal properly.",
    "doctor_consultation_checklist": {
      "parameter_question": "What standardized symptom checklist should we use at home to track recovery?",
      "safety_question": "Why is it important to avoid complete 'dark room' resting for more than two days?",
      "action_threshold_question": "What are the exact, gradual steps required before returning to sports or gym class?"
    },
    "red_flags": [
      "Worsening severe headache, repeated vomiting, or increasing confusion",
      "One pupil larger than the other, or inability to wake the patient from sleep (Immediate Emergency: possible brain bleed)"
    ]
  },
  {
    "id": "DOC-CARD-090",
    "condition": "Allergic Rhinitis (Hay Fever)",
    "specialty": "Infectious Disease",
    "organ_system": "Respiratory / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAAI / ACAAI",
    "citation": "Dykewicz MS et al. Rhinitis 2020: A practice parameter update. J Allergy Clin Immunol. 2020;146(4):721-767.",
    "doi_or_source": "10.1016/j.jaci.2020.07.007",
    "clinical_evidence": "Intranasal corticosteroids (INCS: Fluticasone, Budesonide) are the most effective monotherapy for all symptoms of allergic rhinitis (sneezing, congestion, itching) and are strongly recommended as first-line treatment for moderate-to-severe disease. Oral second-generation antihistamines (Cetirizine, Loratadine) are effective for mild, episodic symptoms but do not relieve severe nasal congestion. First-generation antihistamines (Diphenhydramine) should be avoided due to sedation and anticholinergic side effects.",
    "solution_protocol": {
      "non_pharmacological_targets": "Allergen avoidance (HEPA air filters, washing bedding in hot water for dust mites, keeping windows closed during high pollen seasons); nasal saline irrigation (Neti pot) with distilled/boiled water.",
      "monitoring_cadence": "Assess symptom relief after 2-4 weeks of continuous INCS use (they require days/weeks to reach peak efficacy).",
      "clinical_thresholds": "Allergen immunotherapy (subcutaneous shots or sublingual tablets) is indicated for patients with severe disease refractory to pharmacotherapy."
    },
    "patient_plain_language": "Allergic rhinitis occurs when your immune system overreacts to harmless particles like pollen or dust, causing inflammation, swelling, and mucus production in your nasal passages.",
    "doctor_consultation_checklist": {
      "parameter_question": "Can allergy testing help identify which exact seasons or animals I need to avoid?",
      "safety_question": "Am I aiming my nasal steroid spray correctly (pointing away from the septum) to avoid nosebleeds?",
      "action_threshold_question": "If nasal sprays and pills fail, am I a candidate for allergy desensitization shots?"
    },
    "red_flags": [
      "Unilateral (one-sided) nasal obstruction with blood-tinged discharge (Requires ENT evaluation to rule out polyps or masses)",
      "Concurrent severe wheezing or chest tightness (Indicates allergic asthma component)"
    ]
  },
  {
    "id": "DOC-CARD-091",
    "condition": "Chronic Spontaneous Urticaria (Hives)",
    "specialty": "Dermatology",
    "organ_system": "Integumentary / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: International Guideline",
    "source_body": "EAACI / WAO",
    "citation": "Zuberbier T et al. The EAACI/GA²LEN/EuroGuiDerm/APAAACI Guideline for the Definition, Classification, Diagnosis and Management of Urticaria. Allergy. 2022;77(3):734-766.",
    "doi_or_source": "10.1111/all.15090",
    "clinical_evidence": "Defined as hives occurring most days for >6 weeks. First-line therapy is regular-dosed modern second-generation H1-antihistamines (Cetirizine, Fexofenadine). If symptoms persist after 2-4 weeks, guidelines strongly recommend increasing the antihistamine dose up to four-fold (Grade A). If refractory to high-dose antihistamines, Omalizumab (anti-IgE biologic) is the recommended add-on therapy.",
    "solution_protocol": {
      "non_pharmacological_targets": "Avoidance of exacerbating factors (NSAIDs, tight clothing, extreme heat or cold, stress); keeping a symptom diary to track flares using the Urticaria Activity Score (UAS7).",
      "monitoring_cadence": "Evaluate UAS7 score every 2-4 weeks during medication dose titration.",
      "clinical_thresholds": "Extensive allergy testing, dietary elimination, and malignancy screening are NOT routinely recommended for chronic spontaneous urticaria unless indicated by patient history."
    },
    "patient_plain_language": "Chronic hives are itchy, raised, red welts on the skin that come and go daily for more than 6 weeks, usually caused by an overactive immune system rather than a specific allergy to a food or chemical.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my Urticaria Activity Score (UAS7) showing improvement on my current medication?",
      "safety_question": "Is it safe to increase the dose of my non-drowsy antihistamine up to four times the package dose under your supervision?",
      "action_threshold_question": "If high-dose antihistamines fail, am I a candidate for an injectable medication like Omalizumab?"
    },
    "red_flags": [
      "Hives accompanied by lip swelling, difficulty breathing, or dizziness (Anaphylaxis)",
      "Individual hives that are painful rather than itchy, leave bruises, and last in the exact same spot for >24 hours (Urticarial Vasculitis)"
    ]
  },
  {
    "id": "DOC-CARD-092",
    "condition": "Acne Vulgaris",
    "specialty": "Dermatology",
    "organ_system": "Integumentary",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAD",
    "citation": "Zaenglein AL et al. Guidelines of Care for the Management of Acne Vulgaris. J Am Acad Dermatol. 2016;74(5):945-973.e33. (Updated 2024).",
    "doi_or_source": "10.1016/jaad.2015.12.037",
    "clinical_evidence": "Topical retinoids (Adapalene, Tretinoin) are the foundation of acne therapy, targeting microcomedone formation. Benzoyl peroxide should always be added when topical or oral antibiotics are used to prevent bacterial resistance. For severe, nodulocystic, or scarring acne, oral Isotretinoin is strongly recommended and highly effective, requiring strict teratogenicity monitoring (e.g., iPLEDGE).",
    "solution_protocol": {
      "non_pharmacological_targets": "Gentle cleansing with non-comedogenic syndet bars or washes; avoidance of abrasive scrubbing or popping lesions (increases scarring and hyperpigmentation); low-glycemic index diet.",
      "monitoring_cadence": "Reassess clinical response at 8-12 weeks (acne medications take time to affect the cell turnover cycle).",
      "clinical_thresholds": "Systemic antibiotics (Doxycycline) should be limited to 3-4 months maximum to minimize antimicrobial resistance, used strictly alongside topical retinoids."
    },
    "patient_plain_language": "Acne is an inflammatory skin condition where dead skin cells and oil plug hair follicles, allowing bacteria to multiply and cause red, swollen bumps or deep cysts.",
    "doctor_consultation_checklist": {
      "parameter_question": "Is my regimen targeting both the clogged pores (retinoid) and the bacteria (benzoyl peroxide)?",
      "safety_question": "How can I manage the expected skin peeling and dryness during the first few weeks of using a retinoid?",
      "action_threshold_question": "At what point of severity or scarring should we consider oral Isotretinoin?"
    },
    "red_flags": [
      "Deep, painful, inflamed cysts that are leaving permanent indented scars on the skin",
      "Sudden onset of severe acne with fever and joint pain (Acne Fulminans)"
    ]
  },
  {
    "id": "DOC-CARD-093",
    "condition": "Polymyalgia Rheumatica (PMR)",
    "specialty": "Rheumatology",
    "organ_system": "Musculoskeletal / Immune",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACR / EULAR",
    "citation": "Dejaco C et al. 2015 Recommendations for the Management of Polymyalgia Rheumatica: A European League Against Rheumatism/American College of Rheumatology Collaborative Initiative. Ann Rheum Dis. 2015;74(10):1799-1807.",
    "doi_or_source": "10.1136/annrheumdis-2015-207492",
    "clinical_evidence": "Low-dose systemic glucocorticoids (Prednisone 12.5-25 mg/day) are the cornerstone of therapy, providing dramatic and rapid symptom relief (often within 48-72 hours). Tapering should be slow and individualized (typically lasting 1-2 years) to prevent relapse. Methotrexate may be considered early in patients at high risk for steroid toxicity or those with relapsing disease.",
    "solution_protocol": {
      "non_pharmacological_targets": "Bone-sparing strategies given long-term steroid use (calcium, vitamin D, weight-bearing exercise); fall prevention assessment.",
      "monitoring_cadence": "Clinical assessment and ESR/CRP measurement every 4-8 weeks during the steroid taper.",
      "clinical_thresholds": "Diagnosis relies on age >50, bilateral shoulder/pelvic girdle aching, morning stiffness >45 mins, and elevated inflammatory markers (ESR/CRP)."
    },
    "patient_plain_language": "Polymyalgia rheumatica is an inflammatory disorder causing widespread muscle aching and severe morning stiffness, primarily affecting the shoulders and hips in older adults. It responds exceptionally well to low-dose steroids.",
    "doctor_consultation_checklist": {
      "parameter_question": "Are my ESR and CRP inflammation blood tests returning to normal on this steroid dose?",
      "safety_question": "Have we optimized my bone protection (like taking a bisphosphonate) while I am on long-term steroids?",
      "action_threshold_question": "If I develop a new, severe headache, could that mean the inflammation is spreading to my blood vessels?"
    },
    "red_flags": [
      "New, severe, localized headache, jaw pain while chewing, or sudden vision changes (Indicates concurrent Giant Cell Arteritis emergency)"
    ]
  },
  {
    "id": "DOC-CARD-094",
    "condition": "Thyroid Nodules",
    "specialty": "Endocrinology",
    "organ_system": "Endocrine",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ATA",
    "citation": "Haugen BR et al. 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer. Thyroid. 2016;26(1):1-133.",
    "doi_or_source": "10.1089/thy.2015.0020",
    "clinical_evidence": "The initial evaluation of a thyroid nodule requires measuring serum TSH. If TSH is subnormal (hyperthyroidism), a radionuclide thyroid scan is required (functioning 'hot' nodules are rarely malignant). If TSH is normal or elevated, a dedicated thyroid ultrasound determines the need for Fine-Needle Aspiration (FNA) biopsy based on sonographic pattern (e.g., solid, hypoechoic, microcalcifications) and size (typically >1 cm for high suspicion).",
    "solution_protocol": {
      "non_pharmacological_targets": "Observation and reassurance for completely benign, asymptomatic nodules.",
      "monitoring_cadence": "For nodules with benign cytology, repeat ultrasound at 1-2 years. For non-diagnostic FNA, repeat biopsy with ultrasound guidance.",
      "clinical_thresholds": "Bethesda System for Reporting Thyroid Cytopathology dictates management: Bethesda II (Benign) -> observe; Bethesda VI (Malignant) -> surgical resection."
    },
    "patient_plain_language": "A thyroid nodule is a solid or fluid-filled lump within the thyroid gland in your neck. The vast majority are benign (non-cancerous), but ultrasound features and a simple needle biopsy are used to be absolutely sure.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my TSH level, and does the ultrasound show high-risk or low-risk features?",
      "safety_question": "Is the nodule large enough or suspicious enough to require a needle biopsy?",
      "action_threshold_question": "Based on my Bethesda biopsy score, do I need surgery or just routine ultrasound monitoring?"
    },
    "red_flags": [
      "Rapid growth of a firm, fixed nodule in the neck",
      "New onset of hoarseness, difficulty swallowing, or enlarged lymph nodes in the neck"
    ]
  },
  {
    "id": "DOC-CARD-095",
    "condition": "Ectopic Pregnancy",
    "specialty": "Women's Health",
    "organ_system": "Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACOG",
    "citation": "ACOG Practice Bulletin No. 193: Tubal Ectopic Pregnancy. Obstet Gynecol. 2018;131(3):e91-e103.",
    "doi_or_source": "10.1097/AOG.0000000000002560",
    "clinical_evidence": "Diagnosis requires transvaginal ultrasound (TVUS) and serial quantitative beta-hCG measurements. If a patient is hemodynamically stable, willing to comply with post-treatment follow-up, and meets criteria (mass <3-4 cm, no fetal cardiac activity), medical management with intramuscular Methotrexate is safe and effective. Hemodynamic instability or evidence of rupture mandates immediate surgical intervention (laparoscopy/salpingectomy).",
    "solution_protocol": {
      "non_pharmacological_targets": "Avoidance of folic acid supplements, NSAIDs, and alcohol during Methotrexate therapy; pelvic rest (no intercourse) until resolution is confirmed.",
      "monitoring_cadence": "Serial quantitative hCG testing on Days 4 and 7 post-Methotrexate. A decrease of ≥15% between Day 4 and Day 7 indicates successful treatment; if <15%, a second dose or surgery is required.",
      "clinical_thresholds": "hCG levels must be monitored weekly until they reach non-pregnant levels (<5 mIU/mL)."
    },
    "patient_plain_language": "An ectopic pregnancy occurs when a fertilized egg implants outside the uterus, most commonly in a fallopian tube. It cannot survive, and as it grows, it poses a life-threatening risk of rupturing the tube and causing severe internal bleeding.",
    "doctor_consultation_checklist": {
      "parameter_question": "What are my current hCG hormone levels, and when exactly do I need to return for my next blood draw?",
      "safety_question": "Do I meet all the safety criteria for medical treatment (Methotrexate) rather than surgery?",
      "action_threshold_question": "What level of abdominal pain requires me to go immediately back to the emergency room for fear of a rupture?"
    },
    "red_flags": [
      "Sudden, severe, sharp stabbing pain in the pelvis or abdomen",
      "Dizziness, fainting, or pain radiating to the shoulder tip (Signs of internal bleeding)"
    ]
  },
  {
    "id": "DOC-CARD-096",
    "condition": "Postmenopausal Bleeding & Endometrial Hyperplasia",
    "specialty": "Women's Health",
    "organ_system": "Reproductive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "ACOG",
    "citation": "ACOG Committee Opinion No. 734: The Role of Transvaginal Ultrasonography in the Evaluation of Postmenopausal Bleeding. Obstet Gynecol. 2018.",
    "doi_or_source": "10.1097/AOG.0000000000002631",
    "clinical_evidence": "Any postmenopausal bleeding requires immediate investigation to rule out endometrial cancer (present in ~10% of cases). Initial evaluation options are transvaginal ultrasound (TVUS) or endometrial biopsy. An endometrial thickness of ≤4 mm on TVUS carries a >99% negative predictive value for endometrial cancer, and observation is reasonable. Thickness >4 mm requires endometrial tissue sampling.",
    "solution_protocol": {
      "non_pharmacological_targets": "Weight management (obesity is a primary risk factor for estrogen-driven endometrial hyperplasia).",
      "monitoring_cadence": "If initial biopsy is benign but bleeding persists or recurs, further evaluation with hysteroscopy and directed biopsy is mandatory.",
      "clinical_thresholds": "Endometrial hyperplasia with atypia carries a high risk of concurrent or future cancer and is typically managed with hysterectomy; hyperplasia without atypia is managed with progestin therapy (e.g., Levonorgestrel IUD)."
    },
    "patient_plain_language": "Any vaginal bleeding that occurs more than 12 months after your last menstrual period is abnormal. While it is often caused by harmless thinning of vaginal tissues, it must always be checked immediately to rule out uterine cancer.",
    "doctor_consultation_checklist": {
      "parameter_question": "Did my ultrasound show that my uterine lining is thicker than the safe 4-millimeter threshold?",
      "safety_question": "Can an endometrial biopsy be performed safely and comfortably in the office today?",
      "action_threshold_question": "If the biopsy shows hyperplasia (thickened cells), what are the options for treating it with hormones vs. surgery?"
    },
    "red_flags": [
      "Any episode of vaginal bleeding, spotting, or brownish discharge occurring after menopause (Mandatory evaluation)"
    ]
  },
  {
    "id": "DOC-CARD-097",
    "condition": "Erectile Dysfunction (ED)",
    "specialty": "Cardiovascular",
    "organ_system": "Genitourinary / Vascular",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AUA",
    "citation": "Burnett AL et al. Erectile Dysfunction: AUA Guideline. J Urol. 2018;200(3):633-641.",
    "doi_or_source": "10.1016/j.juro.2018.05.004",
    "clinical_evidence": "ED is a recognized early clinical marker for underlying Atherosclerotic Cardiovascular Disease (ASCVD); symptoms of ED often precede coronary events by 3-5 years. Phosphodiesterase-5 (PDE5) inhibitors (Sildenafil, Tadalafil) are first-line oral therapy. PDE5 inhibitors are absolutely contraindicated in patients taking nitrates (due to severe refractory hypotension) and must be used with caution with alpha-blockers.",
    "solution_protocol": {
      "non_pharmacological_targets": "Cardiovascular risk reduction: strict smoking cessation, weight loss, Mediterranean diet, and aerobic exercise (proven to improve endothelial function and ED severity); psychological counseling for performance anxiety.",
      "monitoring_cadence": "Comprehensive cardiovascular risk assessment (lipid panel, fasting glucose/HbA1c, blood pressure) in all men presenting with new-onset ED.",
      "clinical_thresholds": "If oral PDE5 inhibitors fail or are contraindicated, intracavernosal injections (Alprostadil), vacuum erection devices, or surgical penile prostheses are indicated."
    },
    "patient_plain_language": "Erectile dysfunction is often a plumbing issue caused by the same plaque buildup that causes heart disease. The tiny blood vessels in the penis become narrowed years before the larger arteries in the heart do.",
    "doctor_consultation_checklist": {
      "parameter_question": "Have we run a full cardiovascular screening (cholesterol and blood sugar) to ensure my heart is healthy?",
      "safety_question": "Are any of my current heart or blood pressure medications (like nitrates) dangerous to mix with ED pills?",
      "action_threshold_question": "How exactly should I time my medication with food and activity for it to work optimally?"
    },
    "red_flags": [
      "An erection lasting longer than 4 hours (Priapism: requires immediate emergency room treatment to prevent permanent tissue damage)"
    ]
  },
  {
    "id": "DOC-CARD-098",
    "condition": "Restless Legs Syndrome (RLS)",
    "specialty": "Neurology",
    "organ_system": "Central Nervous System",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "AAN",
    "citation": "Winkelman JW et al. Practice Guideline Summary: Treatment of Restless Legs Syndrome in Adults. Neurology. 2016;87(24):2585-2593.",
    "doi_or_source": "10.1212/WNL.0000000000003388",
    "clinical_evidence": "First-line evaluation must include checking serum ferritin, as brain iron deficiency is a primary driver of RLS. If ferritin is <75 ng/mL, iron supplementation is the first-line therapy. For pharmacological symptom control, alpha-2-delta ligands (Pregabalin, Gabapentin enacarbil) are preferred. Dopamine agonists (Pramipexole, Ropinirole) are effective but carry a high risk of 'augmentation' (paradoxical worsening of symptoms over time).",
    "solution_protocol": {
      "non_pharmacological_targets": "Avoidance of caffeine, alcohol, and nicotine near bedtime; moderate aerobic exercise; pneumatic compression devices; review of current medications (antidepressants like SSRIs/SNRIs and antihistamines strongly exacerbate RLS).",
      "monitoring_cadence": "Reassess serum ferritin levels 3-4 months after starting oral iron replacement.",
      "clinical_thresholds": "Diagnosis requires URGE criteria: Urge to move legs, Rest worsens symptoms, Getting up/movement relieves symptoms, Evening/nighttime worsening."
    },
    "patient_plain_language": "Restless legs syndrome is a neurological disorder causing an overwhelming, uncomfortable urge to move your legs, usually occurring in the evening or when trying to sleep, severely disrupting rest.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my serum ferritin iron level, and should I start an iron supplement to see if it fixes the issue?",
      "safety_question": "Are my allergy pills or antidepressant medications making my restless legs worse?",
      "action_threshold_question": "If I am on a dopamine medication and my symptoms start happening earlier in the afternoon, how do we treat 'augmentation'?"
    },
    "red_flags": [
      "Severe daytime sleepiness leading to falling asleep while driving"
    ]
  },
  {
    "id": "DOC-CARD-099",
    "condition": "Acute Appendicitis",
    "specialty": "Gastroenterology",
    "organ_system": "Digestive",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "WSES",
    "citation": "Di Saverio S et al. Diagnosis and Treatment of Acute Appendicitis: 2020 Update of the WSES Jerusalem Guidelines. World J Emerg Surg. 2020;15(1):27.",
    "doi_or_source": "10.1186/s13017-020-00306-3",
    "clinical_evidence": "Laparoscopic appendectomy remains the gold standard treatment for acute appendicitis. While non-operative management (antibiotics alone) can be successful in selected patients with uncomplicated appendicitis, there is a recurrence rate of up to 39% at 5 years (CODA trial). Surgery is mandatory for complicated appendicitis (perforation, peritonitis, abscess).",
    "solution_protocol": {
      "non_pharmacological_targets": "Immediate NPO (nothing by mouth) status in the emergency department; IV fluid resuscitation and analgesia.",
      "monitoring_cadence": "Clinical scoring systems (Alvarado score or AIR score) guide risk stratification and need for imaging.",
      "clinical_thresholds": "CT scan of the abdomen/pelvis with IV contrast is the most accurate imaging modality in adults; Ultrasound is preferred in children and pregnant women to avoid radiation."
    },
    "patient_plain_language": "Appendicitis is a sudden infection and inflammation of the appendix, a small pouch attached to the large intestine. It typically requires quick surgical removal before it can burst.",
    "doctor_consultation_checklist": {
      "parameter_question": "Did the CT scan or ultrasound confirm appendicitis, and is it uncomplicated or ruptured?",
      "safety_question": "If we try treating this with antibiotics alone instead of surgery, what are the chances it returns?",
      "action_threshold_question": "What are the surgical risks of a laparoscopic removal versus open surgery?"
    },
    "red_flags": [
      "Pain starting around the belly button that shifts to the lower right abdomen and becomes intense",
      "Sudden relief of severe pain followed by a high fever and a rigid, swollen abdomen (Indicates the appendix has burst/perforated)"
    ]
  },
  {
    "id": "DOC-CARD-100",
    "condition": "Hyperkalemia (Elevated Blood Potassium)",
    "specialty": "Nephrology",
    "organ_system": "Renal / Cardiovascular",
    "cebm_level": 1,
    "evidence_tier": "Level 1: Clinical Practice Guideline",
    "source_body": "KDIGO",
    "citation": "KDIGO Consensus Conference on Potassium Management. Kidney Int. 2020;97(1):42-61.",
    "doi_or_source": "10.1016/j.kint.2019.09.018",
    "clinical_evidence": "Severe hyperkalemia (≥6.5 mEq/L) or any hyperkalemia with ECG changes (peaked T waves, widened QRS) is a life-threatening emergency requiring immediate myocardial stabilization with IV Calcium Gluconate (or Calcium Chloride). This must be followed by intracellular potassium-shifting agents (IV Insulin with Dextrose, Albuterol) and eventually potassium-removing agents (Loop diuretics, GI cation binders like Patiromer, or emergent Hemodialysis).",
    "solution_protocol": {
      "non_pharmacological_targets": "Strict low-potassium diet restriction; immediate cessation of all potassium-sparing medications (ACEi/ARBs, MRAs like Spironolactone, NSAIDs).",
      "monitoring_cadence": "Continuous 12-lead ECG and telemetry monitoring in the acute phase; repeat serum potassium levels 1-2 hours after acute interventions.",
      "clinical_thresholds": "Emergent hemodialysis is indicated for hyperkalemia refractory to medical management or in the setting of severe oliguric renal failure."
    },
    "patient_plain_language": "Hyperkalemia is dangerously high potassium in the blood, usually because the kidneys cannot filter it out. Because potassium controls the heart's electrical rhythm, high levels can cause the heart to suddenly stop.",
    "doctor_consultation_checklist": {
      "parameter_question": "What is my exact potassium blood level, and is my EKG showing any dangerous heart rhythm changes?",
      "safety_question": "Are my blood pressure pills or over-the-counter pain relievers holding onto too much potassium?",
      "action_threshold_question": "Do I need a new prescription for an oral potassium-binder medicine to keep my levels safe at home?"
    },
    "red_flags": [
      "Muscle weakness, numbness, or tingling in the limbs",
      "Heart palpitations, skipped beats, or severe shortness of breath (Medical Emergency)"
    ]
  }
]

from scripts.assemble_dataset import ALL_NEW_DISEASES
ALL_DISEASES.extend(ALL_NEW_DISEASES)

DOMAIN_MAP = {
    "Cardiovascular": "CARDIOVASCULAR",
    "Cardiology & Emergency Medicine": "CARDIOVASCULAR",
    "Vascular & Cardiology": "CARDIOVASCULAR",
    "Vascular & Hematology": "CARDIOVASCULAR",
    "Vascular Surgery": "CARDIOVASCULAR",
    "Urology & Cardiology": "CARDIOVASCULAR",
    "Endocrinology": "ENDOCRINOLOGY_METABOLISM",
    "Endocrinology & Women's Health": "ENDOCRINOLOGY_METABOLISM",
    "Gastroenterology": "GASTROENTEROLOGY",
    "Gastroenterology & General Surgery": "GASTROENTEROLOGY",
    "Gastroenterology & Infectious Disease": "GASTROENTEROLOGY",
    "General Surgery": "GASTROENTEROLOGY",
    "Hepatology": "GASTROENTEROLOGY",
    "Hepatology & Infectious Disease": "GASTROENTEROLOGY",
    "Pulmonology": "PULMONOLOGY",
    "Infectious Disease & Pulmonology": "PULMONOLOGY",
    "Nephrology": "NEPHROLOGY",
    "Nephrology & Emergency Medicine": "NEPHROLOGY",
    "Infectious Disease": "INFECTIOUS_DISEASE",
    "Infectious Disease & Urology": "INFECTIOUS_DISEASE",
    "Infectious Disease & Orthopedics": "INFECTIOUS_DISEASE",
    "Critical Care & Infectious Disease": "INFECTIOUS_DISEASE",
    "Infectious Disease & Neurology": "INFECTIOUS_DISEASE",
    "Allergy & Immunology / Emergency Medicine": "INFECTIOUS_DISEASE",
    "Allergy & Immunology": "INFECTIOUS_DISEASE",
    "Psychiatry": "PSYCHIATRY",
    "Mental Health & Psychiatry": "PSYCHIATRY",
    "Neurology": "NEUROLOGY",
    "Neurology & Emergency Medicine": "NEUROLOGY",
    "Neurology & Endocrinology": "NEUROLOGY",
    "Neurology & Otolaryngology": "NEUROLOGY",
    "Neurology & Sports Medicine": "NEUROLOGY",
    "Neurology & Sleep Medicine": "NEUROLOGY",
    "Neurology & Orthopedics": "NEUROLOGY",
    "Neurology & Pain Medicine": "NEUROLOGY",
    "Orthopedics & Neurology": "NEUROLOGY",
    "Rheumatology": "RHEUMATOLOGY",
    "Rheumatology & Ophthalmology": "RHEUMATOLOGY",
    "Orthopedics & Rheumatology": "RHEUMATOLOGY",
    "Genetics & Rheumatology": "RHEUMATOLOGY",
    "Women's Health": "WOMENS_HEALTH",
    "Women's Health & Infectious Disease": "WOMENS_HEALTH",
    "Obstetrics & Gynecology / Emergency": "WOMENS_HEALTH",
    "Obstetrics & Gynecology": "WOMENS_HEALTH",
    "Pediatrics": "PEDIATRICS",
    "Pediatrics / Neonatology": "PEDIATRICS",
    "Dermatology": "DERMATOLOGY",
    "Dermatology & Oncology": "DERMATOLOGY",
    "Allergy & Dermatology": "DERMATOLOGY",
    "Hematology": "CARDIOVASCULAR",
    "Hematology & Nephrology": "NEPHROLOGY",
    "Hematology & Oncology": "ONCOLOGY",
    "Oncology": "ONCOLOGY",
    "Urology": "NEPHROLOGY",
    "Orthopedics": "RHEUMATOLOGY",
    "Critical Care": "EMERGENCY_MEDICINE",
    "Gynecology": "WOMENS_HEALTH",
    "ENT / Otolaryngology": "GENERAL_MEDICINE",
    "ENT": "GENERAL_MEDICINE",
    "Otolaryngology": "GENERAL_MEDICINE",
    "Ophthalmology": "OPHTHALMOLOGY"
}

CATEGORY_ICONS = {
    "Cardiovascular": "❤️",
    "Cardiology": "❤️",
    "Endocrinology": "🩸",
    "Gastroenterology": "🫕",
    "General Surgery": "🫕",
    "Hepatology": "🫕",
    "Pulmonology": "🫁",
    "Nephrology": "💧",
    "Infectious Disease": "🛡️",
    "Allergy": "🛡️",
    "Psychiatry": "🌱",
    "Neurology": "🧠",
    "Rheumatology": "🤲",
    "Women's Health": "🌸",
    "Obstetrics": "🌸",
    "Pediatrics": "🧸",
    "Dermatology": "🧴",
    "Hematology": "🩸",
    "Oncology": "🎗️",
    "Urology": "💧",
    "Orthopedics": "🦴",
    "Critical Care": "🚨",
    "Gynecology": "🌸",
    "ENT": "👂",
    "Otolaryngology": "👂",
    "Genetics": "🧬",
    "Ophthalmology": "👁️"
}


def transform_to_knowledge_base():
    formatted_docs = []
    suggestions = []

    for item in ALL_DISEASES:
        cebm_enum_val = "Level 1 (Meta-Analysis / Systematic Review)" if item["cebm_level"] == 1 else "Level 2 (Randomized Controlled Trial)"
        
        spec = item.get("specialty", "General Medicine")
        domain = DOMAIN_MAP.get(spec, "GENERAL_MEDICINE")
        
        # Build comprehensive keywords
        cond = item["condition"]
        kw_set = {cond.lower(), spec.lower(), item.get("organ_system", "").lower(), item["source_body"].lower()}
        
        # Add clean words from condition, citation, and evidence
        for word in re.findall(r"[a-zA-Z]{3,}", f"{cond} {item['citation']} {item['clinical_evidence'][:200]} {item.get('patient_plain_language', '')[:100]}"):
            kw_set.add(word.lower())

        # Extract snippet from clinical evidence + protocol
        snippet = f"{item['clinical_evidence']} Guideline Protocol: {item['solution_protocol']['non_pharmacological_targets']} Thresholds: {item['solution_protocol']['clinical_thresholds']}"
        
        doc = {
            "id": item["id"],
            "domain": domain,
            "disease": cond,
            "title": f"{cond}: Evidence & Clinical Guidelines ({item['source_body']})",
            "journal": item["source_body"],
            "year": 2024,
            "doi_or_pmid": item["doi_or_source"],
            "evidence_level": cebm_enum_val,
            "keywords": list(kw_set),
            "snippet": snippet,
            "key_takeaway": item["clinical_evidence"][:220] + "...",
            "patient_plain_language": item.get("patient_plain_language"),
            "doctor_consultation_checklist": item.get("doctor_consultation_checklist"),
            "red_flags": item.get("red_flags", []),
            "solution_protocol": item.get("solution_protocol")
        }
        if "evidence_stack" in item:
            doc["evidence_stack"] = item["evidence_stack"]
        formatted_docs.append(doc)

        # Generate Frontend Suggestion Chip
        first_spec = spec.split(" & ")[0].split(" / ")[0]
        icon = CATEGORY_ICONS.get(first_spec, "🩺")
        cat = first_spec
        suggestions.append({
            "id": f"sug-{item['id'].lower()}",
            "label": cond,
            "category": cat,
            "query": f"What are the verified clinical guidelines and evidence-backed treatments for {cond}?",
            "healthBody": item["source_body"],
            "description": item["patient_plain_language"][:110] + "...",
            "icon": icon
        })

    # Save to backend
    DATA_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(formatted_docs, f, indent=2, ensure_ascii=False)
    print(f"[OK] Successfully written {len(formatted_docs)} disease records to {DATA_JSON_PATH}")

    # Generate web suggestions.ts
    ts_content = f"""export interface SearchSuggestion {{
  id: string;
  label: string;
  category: string;
  query: string;
  healthBody: string;
  description: string;
  icon?: string;
}}

export const HEALTH_SUGGESTIONS: SearchSuggestion[] = {json.dumps(suggestions, indent=2, ensure_ascii=False)};

export function getMatchingSuggestions(input: string, limit: number = 8): SearchSuggestion[] {{
  if (!input || !input.trim()) {{
    return HEALTH_SUGGESTIONS.slice(0, limit);
  }}

  const clean = input.toLowerCase().trim();
  const words = clean.split(/\\s+/).filter(Boolean);

  const scored = HEALTH_SUGGESTIONS.map((item) => {{
    let score = 0;
    const labelLower = item.label.toLowerCase();
    const queryLower = item.query.toLowerCase();
    const descLower = item.description.toLowerCase();
    const catLower = item.category.toLowerCase();
    const bodyLower = item.healthBody.toLowerCase();

    if (labelLower.includes(clean)) score += 60;
    if (queryLower.includes(clean)) score += 35;

    words.forEach((w) => {{
      if (labelLower.includes(w)) score += 25;
      if (queryLower.includes(w)) score += 15;
      if (descLower.includes(w)) score += 8;
      if (catLower.includes(w)) score += 6;
      if (bodyLower.includes(w)) score += 4;
    }});

    return {{ item, score }};
  }});

  return scored
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((s) => s.item)
    .slice(0, limit);
}}
"""
    with open(SUGGESTIONS_TS_PATH, "w", encoding="utf-8") as f:
        f.write(ts_content)
    print(f"[OK] Successfully generated {len(suggestions)} frontend suggestion chips in {SUGGESTIONS_TS_PATH}")

if __name__ == "__main__":
    transform_to_knowledge_base()
