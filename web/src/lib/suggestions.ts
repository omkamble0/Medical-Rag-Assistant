export interface SearchSuggestion {
  id: string;
  label: string;
  category: string;
  query: string;
  healthBody: string;
  description: string;
  icon?: string;
}

export const HEALTH_SUGGESTIONS: SearchSuggestion[] = [
  // ── 1. CARDIOVASCULAR & HEART ────────────────────────────────
  {
    id: "sug-hyp-1",
    label: "High Blood Pressure (Hypertension)",
    category: "Cardiovascular",
    query: "What are the first-line treatments and DASH diet guidelines for high blood pressure?",
    healthBody: "WHO / AHA / ACC",
    description: "First-line therapies (ACEi, ARBs, CCBs, Thiazides) & DASH sodium reduction",
    icon: "❤️"
  },
  {
    id: "sug-hyp-2",
    label: "Blood Pressure Numbers & Monitoring",
    category: "Cardiovascular",
    query: "What is normal blood pressure and how should I monitor it at home?",
    healthBody: "WHO / AHA Guidelines",
    description: "Systolic/diastolic targets, home cuffs, and lifestyle modifications",
    icon: "🩺"
  },
  {
    id: "sug-chol-1",
    label: "High Cholesterol & Statin Safety",
    category: "Cardiovascular",
    query: "Are statin side effects dangerous and what are the alternatives for high cholesterol?",
    healthBody: "ESC / AHA / NLA",
    description: "LDL reduction, statin safety profile, ezetimibe & PCSK9 inhibitors",
    icon: "💊"
  },
  {
    id: "sug-hf-1",
    label: "Heart Failure & Breathlessness (HFrEF)",
    category: "Cardiovascular",
    query: "What are the newest treatments for heart failure with reduced ejection fraction (HFrEF)?",
    healthBody: "AHA / ACC / ESC",
    description: "Sacubitril/valsartan (Entresto), SGLT2i, and quadruple guideline therapy",
    icon: "🫀"
  },
  {
    id: "sug-afib-1",
    label: "Atrial Fibrillation (AFib) & Stroke Risk",
    category: "Cardiovascular",
    query: "How does blood thinner treatment prevent stroke in atrial fibrillation?",
    healthBody: "AHA / ESC / NICE",
    description: "DOACs (Apixaban, Rivaroxaban) vs Warfarin & CHA2DS2-VASc scoring",
    icon: "⚡"
  },
  {
    id: "sug-stroke-1",
    label: "Stroke Prevention & Post-TIA Care",
    category: "Cardiovascular",
    query: "What is the recommended secondary prevention after a minor stroke or TIA?",
    healthBody: "AHA / ASA / WHO",
    description: "Dual antiplatelet therapy (DAPT), blood pressure control, and statins",
    icon: "🧠"
  },
  {
    id: "sug-cad-1",
    label: "Coronary Artery Disease & Angina",
    category: "Cardiovascular",
    query: "What is the optimal medical therapy vs stenting for stable coronary artery disease?",
    healthBody: "ISCHEMIA Trial / AHA / ESC",
    description: "Anti-anginals, beta-blockers, statins, and revascularization guidelines",
    icon: "🫀"
  },

  // ── 2. DIABETES & METABOLISM ────────────────────────────────
  {
    id: "sug-t2d-1",
    label: "Type 2 Diabetes & Semaglutide (GLP-1)",
    category: "Diabetes & Metabolism",
    query: "Semaglutide cardiovascular outcomes and titration schedule in Type 2 Diabetes",
    healthBody: "ADA / EASD / WHO",
    description: "HbA1c control, weight loss, cardiovascular event risk reduction",
    icon: "🩸"
  },
  {
    id: "sug-t1d-1",
    label: "Type 1 Diabetes & Insulin Management",
    category: "Diabetes & Metabolism",
    query: "What are the latest guidelines for intensive insulin therapy and CGM in Type 1 Diabetes?",
    healthBody: "ADA / ISPAD / WHO",
    description: "Continuous Glucose Monitoring (CGM), basal-bolus insulin & target HbA1c <7%",
    icon: "💉"
  },
  {
    id: "sug-glp1-side",
    label: "GLP-1 Side Effects & Nausea Management",
    category: "Diabetes & Metabolism",
    query: "How to manage nausea and digestive side effects on Ozempic or Wegovy?",
    healthBody: "Lancet / ADA Clinical Update",
    description: "Slow 4-week titration schedules, hydration, and dietary adjustments",
    icon: "🧪"
  },
  {
    id: "sug-obesity-1",
    label: "Obesity & Weight Loss (Tirzepatide / Semaglutide)",
    category: "Diabetes & Metabolism",
    query: "What are the medically proven treatments and medications for obesity management?",
    healthBody: "WHO / Endocrine Society",
    description: "Lifestyle interventions, GLP-1/GIP receptor agonists & metabolic outcomes",
    icon: "⚖️"
  },
  {
    id: "sug-fattyliver-1",
    label: "Fatty Liver Disease (NAFLD / MASLD)",
    category: "Diabetes & Metabolism",
    query: "What are the proven treatments and diet changes for non-alcoholic fatty liver disease?",
    healthBody: "AASLD / EASL / WHO",
    description: "Weight loss, Mediterranean diet, Resmetirom & fibrosis staging",
    icon: "🥗"
  },
  {
    id: "sug-pcos-1",
    label: "PCOS (Polycystic Ovary Syndrome)",
    category: "Endocrine & Women's Health",
    query: "What is the recommended treatment approach for PCOS irregular periods and insulin resistance?",
    healthBody: "ESHRE / ASRM Guidelines",
    description: "Oral contraceptives, Metformin, lifestyle modifications, and Letrozole",
    icon: "🌸"
  },

  // ── 3. RESPIRATORY & PULMONOLOGY ───────────────────────────
  {
    id: "sug-asthma-1",
    label: "Asthma Inhalers & Wheezing (GINA Strategy)",
    category: "Respiratory",
    query: "What is the recommended inhaler approach for mild to moderate asthma?",
    healthBody: "GINA 2024 / WHO",
    description: "As-needed ICS-formoterol vs daily maintenance and SABA relievers",
    icon: "🫁"
  },
  {
    id: "sug-copd-1",
    label: "COPD Management & Inhaler Options",
    category: "Respiratory",
    query: "What are the benefits of single-inhaler triple therapy for COPD exacerbations?",
    healthBody: "GOLD 2024 / WHO",
    description: "LAMA/LABA/ICS combinations, smoking cessation, and pulmonary rehab",
    icon: "💨"
  },
  {
    id: "sug-covid-1",
    label: "COVID-19 Treatment & Paxlovid",
    category: "Infectious Disease",
    query: "Paxlovid antiviral efficacy and timing in high-risk COVID-19 patients",
    healthBody: "WHO / NIH / CDC",
    description: "Oral antiviral within 5 days of symptoms to reduce hospitalization by 89%",
    icon: "🛡️"
  },
  {
    id: "sug-sleep-1",
    label: "Sleep Apnea & CPAP Therapy",
    category: "Respiratory",
    query: "How does CPAP therapy help obstructive sleep apnea and daytime fatigue?",
    healthBody: "AASM / WHO Guidelines",
    description: "Apnea-Hypopnea Index (AHI), CPAP adherence, and cardiovascular health",
    icon: "😴"
  },
  {
    id: "sug-pneum-1",
    label: "Pneumonia & Chest Infections",
    category: "Respiratory",
    query: "What are the first-line antibiotics and recovery guidelines for community-acquired pneumonia?",
    healthBody: "ATS / IDSA Guidelines",
    description: "Amoxicillin, Doxycycline, CURB-65 criteria, and follow-up care",
    icon: "🌡️"
  },

  // ── 4. MENTAL HEALTH & NEUROLOGY ───────────────────────────
  {
    id: "sug-depr-1",
    label: "Depression & Antidepressant Options",
    category: "Mental Health",
    query: "What are the most effective and well-tolerated antidepressants for major depression?",
    healthBody: "WHO / NICE / APA",
    description: "SSRIs (Escitalopram, Sertraline), psychotherapy (CBT), and recovery timelines",
    icon: "🌱"
  },
  {
    id: "sug-anx-1",
    label: "Generalized Anxiety & Panic Attacks",
    category: "Mental Health",
    query: "What are the best evidence-based treatments for chronic anxiety and panic disorders?",
    healthBody: "NICE / WFSBP / WHO",
    description: "First-line SSRIs/SNRIs, cognitive behavioral therapy, and coping strategies",
    icon: "🕊️"
  },
  {
    id: "sug-insom-1",
    label: "Insomnia & CBT-I Sleep Therapy",
    category: "Mental Health",
    query: "What are the core techniques of CBT for Insomnia (CBT-I) without sleeping pills?",
    healthBody: "ACP Clinical Practice Guideline",
    description: "Sleep restriction, stimulus control, sleep hygiene, and circadian alignment",
    icon: "🌙"
  },
  {
    id: "sug-mig-1",
    label: "Migraine & Severe Headaches",
    category: "Neurology",
    query: "What are the newest preventative and acute treatments for chronic migraine?",
    healthBody: "AHS / EHF / WHO",
    description: "CGRP inhibitors (Erenumab), Triptans, and trigger management",
    icon: "💆"
  },
  {
    id: "sug-alz-1",
    label: "Alzheimer's Disease & Memory Loss",
    category: "Neurology",
    query: "What are the latest disease-modifying therapies for early Alzheimer's disease?",
    healthBody: "NIA / WHO / FDA",
    description: "Anti-amyloid monoclonal antibodies (Lecanemab) & cognitive monitoring",
    icon: "🧩"
  },
  {
    id: "sug-pd-1",
    label: "Parkinson's Disease & Tremors",
    category: "Neurology",
    query: "What is the evidence-based medication regimen for Parkinson's motor symptoms?",
    healthBody: "Movement Disorder Society (MDS)",
    description: "Levodopa/Carbidopa, dopamine agonists, and physical therapy",
    icon: "🚶"
  },

  // ── 5. MUSCULOSKELETAL, JOINTS & PAIN ───────────────────────
  {
    id: "sug-back-1",
    label: "Lower Back Pain & Sciatica",
    category: "Musculoskeletal",
    query: "What is the recommended non-surgical care for acute and chronic lower back pain?",
    healthBody: "ACP / NICE / WHO",
    description: "First-line physical therapy, NSAIDs, heat therapy, avoiding routine opioids",
    icon: "🧘"
  },
  {
    id: "sug-ra-1",
    label: "Rheumatoid Arthritis & Joint Pain",
    category: "Musculoskeletal",
    query: "What is the first-line medication protocol for rheumatoid arthritis?",
    healthBody: "ACR / EULAR Guidelines",
    description: "Methotrexate DMARD therapy, biologic TNF inhibitors, and joint protection",
    icon: "🤲"
  },
  {
    id: "sug-osteo-1",
    label: "Osteoporosis & Bone Density",
    category: "Musculoskeletal",
    query: "How do bisphosphonates reduce fracture risk in postmenopausal osteoporosis?",
    healthBody: "NOF / Endocrine Society / WHO",
    description: "Alendronate, Zoledronate, DXA scan T-scores, and Vitamin D3 + Calcium",
    icon: "🦴"
  },
  {
    id: "sug-gout-1",
    label: "Gout Attacks & High Uric Acid",
    category: "Musculoskeletal",
    query: "What is the best long-term strategy to prevent gout flare-ups and lower uric acid?",
    healthBody: "ACR / EULAR Guidelines",
    description: "Allopurinol treat-to-target (<6.0 mg/dL), Colchicine flare prophylaxis",
    icon: "🦶"
  },
  {
    id: "sug-oa-1",
    label: "Knee & Hip Osteoarthritis",
    category: "Musculoskeletal",
    query: "What are the most effective non-surgical treatments for knee osteoarthritis pain?",
    healthBody: "OARSI / ACR Guidelines",
    description: "Topical NSAID gel (Diclofenac), low-impact exercise, and weight management",
    icon: "🦵"
  },

  // ── 6. DIGESTIVE & GASTROENTEROLOGY ─────────────────────────
  {
    id: "sug-gerd-1",
    label: "Acid Reflux & GERD Management",
    category: "Gastrointestinal",
    query: "What are the safest long-term approaches for acid reflux and heartburn?",
    healthBody: "ACG / AGA / WHO",
    description: "PPI tapering, H2 blockers, dietary modifications, and meal timing",
    icon: "🫕"
  },
  {
    id: "sug-hpyl-1",
    label: "Stomach Ulcers & H. Pylori Infection",
    category: "Gastrointestinal",
    query: "What is the recommended 14-day quadruple therapy for H. pylori eradication?",
    healthBody: "ACG / Maastricht VI Consensus",
    description: "Bismuth quadruple therapy, eradication testing, and mucosal healing",
    icon: "🔬"
  },
  {
    id: "sug-ibs-1",
    label: "IBS & Low-FODMAP Diet",
    category: "Gastrointestinal",
    query: "How does a low-FODMAP diet and gut-targeted therapy help IBS symptoms?",
    healthBody: "ACG Clinical Guideline",
    description: "Dietary trigger elimination, soluble fiber, Rifaximin, and Linaclotide",
    icon: "🥑"
  },
  {
    id: "sug-celiac-1",
    label: "Celiac Disease & Gluten Sensitivity",
    category: "Gastrointestinal",
    query: "What are the diagnostic blood tests and dietary guidelines for celiac disease?",
    healthBody: "ACG / WHO Practice Standard",
    description: "tTG-IgA screening, duodenal biopsy, and strict lifelong gluten-free diet",
    icon: "🌾"
  },

  // ── 7. RENAL, ENDOCRINE & DERMATOLOGY ───────────────────────
  {
    id: "sug-ckd-1",
    label: "Chronic Kidney Disease (CKD)",
    category: "Renal & Endocrine",
    query: "What medications slow down kidney function decline in chronic kidney disease?",
    healthBody: "KDIGO 2024 / WHO",
    description: "SGLT2 inhibitors (Dapagliflozin), ACEi/ARBs, and eGFR monitoring",
    icon: "💧"
  },
  {
    id: "sug-thyroid-1",
    label: "Hypothyroidism & Thyroid Health",
    category: "Renal & Endocrine",
    query: "What is the correct dosing and monitoring approach for Levothyroxine in hypothyroidism?",
    healthBody: "ATA / AACE Guidelines",
    description: "TSH target ranges, morning fasting administration, and symptom relief",
    icon: "🦋"
  },
  {
    id: "sug-hyperthyr-1",
    label: "Hyperthyroidism & Graves' Disease",
    category: "Renal & Endocrine",
    query: "What are the first-line antithyroid medications and beta-blockers for Graves' disease?",
    healthBody: "ATA Practice Guidelines",
    description: "Methimazole, symptom control with beta-blockers, and thyroid labs",
    icon: "⚡"
  },
  {
    id: "sug-eczema-1",
    label: "Eczema (Atopic Dermatitis) & Skin Care",
    category: "Dermatology",
    query: "What is the recommended treatment ladder for atopic dermatitis and eczema flares?",
    healthBody: "AAD 2024 / EADV",
    description: "Liberal emollient use, topical corticosteroids, and Dupilumab biologics",
    icon: "🧴"
  },
  {
    id: "sug-psor-1",
    label: "Psoriasis & Plaque Clearance",
    category: "Dermatology",
    query: "What are the most effective biologic and topical therapies for plaque psoriasis?",
    healthBody: "AAD / NPF Guidelines",
    description: "IL-17/IL-23 biologics, topical corticosteroids with vitamin D, and joint checks",
    icon: "✨"
  },
  {
    id: "sug-shingles-1",
    label: "Shingles (Herpes Zoster) & Prevention",
    category: "Infectious & Dermatology",
    query: "What is the treatment window for Valacyclovir and efficacy of the Shingrix vaccine?",
    healthBody: "CDC / ACIP / NEJM",
    description: "72-hour antiviral window for rash, nerve pain relief, and 97% vaccine protection",
    icon: "🛡️"
  },
  {
    id: "sug-uti-1",
    label: "Urinary Tract Infection (UTI) First-Line",
    category: "Infectious Disease",
    query: "What are the recommended first-line antibiotics for acute uncomplicated UTI cystitis?",
    healthBody: "IDSA / ESCMID Guidelines",
    description: "Nitrofurantoin (5 days), Fosfomycin (single dose), and hydration",
    icon: "🚻"
  },
  {
    id: "sug-bph-1",
    label: "Enlarged Prostate (BPH) & Frequent Urination",
    category: "Men's Health",
    query: "What are the first-line medications for benign prostatic hyperplasia (BPH)?",
    healthBody: "AUA / EAU Guidelines",
    description: "Tamsulosin alpha-blockers, Finasteride combination, and symptom relief",
    icon: "🚽"
  },

  // ── 8. PREVENTIVE CANCER SCREENING ──────────────────────────
  {
    id: "sug-crc-1",
    label: "Colorectal Cancer Screening (Age 45)",
    category: "Preventive Health",
    query: "What are the recommended routine screening ages for colon, breast, and cervical cancer?",
    healthBody: "USPSTF / WHO / ACS",
    description: "Colonoscopy starting at age 45, FIT stool testing, and early polyps detection",
    icon: "🎗️"
  },
  {
    id: "sug-bc-1",
    label: "Mammogram & Breast Cancer Screening",
    category: "Preventive Health",
    query: "What are the updated 2024 USPSTF breast cancer screening guidelines for women?",
    healthBody: "USPSTF / WHO 2024",
    description: "Biennial screening mammography beginning at age 40 through 74",
    icon: "🎀"
  },

  // ── 9. EMERGENCY SAFETY INTERCEPT ───────────────────────────
  {
    id: "sug-emer-1",
    label: "Emergency Chest Pain & Warning Signs",
    category: "Emergency Triage",
    query: "I have severe crushing chest pain, cold sweats, and cannot breathe",
    healthBody: "Tier-1 Emergency Intercept",
    description: "Immediate emergency department evaluation and 911 / 112 / 108 hotlines",
    icon: "🚨"
  }
];

export function getMatchingSuggestions(input: string, limit: number = 7): SearchSuggestion[] {
  if (!input || !input.trim()) {
    return HEALTH_SUGGESTIONS.slice(0, limit);
  }

  const clean = input.toLowerCase().trim();
  const words = clean.split(/\s+/).filter(Boolean);

  const scored = HEALTH_SUGGESTIONS.map((item) => {
    let score = 0;
    const labelLower = item.label.toLowerCase();
    const queryLower = item.query.toLowerCase();
    const descLower = item.description.toLowerCase();
    const catLower = item.category.toLowerCase();
    const bodyLower = item.healthBody.toLowerCase();

    if (labelLower.includes(clean)) score += 50;
    if (queryLower.includes(clean)) score += 30;

    words.forEach((w) => {
      if (labelLower.includes(w)) score += 20;
      if (queryLower.includes(w)) score += 12;
      if (descLower.includes(w)) score += 8;
      if (catLower.includes(w)) score += 6;
      if (bodyLower.includes(w)) score += 4;
    });

    return { item, score };
  });

  return scored
    .filter((s) => s.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((s) => s.item)
    .slice(0, limit);
}
