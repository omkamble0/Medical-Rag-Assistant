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
  {
    "id": "sug-doc-card-001",
    "label": "Essential Hypertension",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Essential Hypertension?",
    "healthBody": "ACC/AHA & JAMA",
    "description": "Blood pressure is the force of blood pushing against the walls of your arteries. When it stays high, it slowly...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-002",
    "label": "Heart Failure with Reduced Ejection Fraction (HFrEF)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Heart Failure with Reduced Ejection Fraction (HFrEF)?",
    "healthBody": "NEJM (PARADIGM-HF)",
    "description": "Heart failure means your heart muscle is pumping less efficiently than normal, making it harder to supply oxyg...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-003",
    "label": "Atrial Fibrillation & Stroke Prophylaxis",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Atrial Fibrillation & Stroke Prophylaxis?",
    "healthBody": "NEJM (ARISTOTLE)",
    "description": "Atrial fibrillation is an irregular, quivering heartbeat in the top chambers of your heart. Because blood does...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-004",
    "label": "Hypercholesterolemia & Atherosclerotic Cardiovascular Disease (ASCVD)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypercholesterolemia & Atherosclerotic Cardiovascular Disease (ASCVD)?",
    "healthBody": "AHA/ACC/Multisociety",
    "description": "Cholesterol is a fatty substance your body needs, but too much 'bad' LDL cholesterol builds up inside your art...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-005",
    "label": "Deep Vein Thrombosis (DVT) & Pulmonary Embolism (PE)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Deep Vein Thrombosis (DVT) & Pulmonary Embolism (PE)?",
    "healthBody": "CHEST",
    "description": "A DVT is a blood clot that forms in the deep veins of your leg. If part of the clot breaks free and travels to...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-006",
    "label": "Stable Ischemic Heart Disease & Angina",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Stable Ischemic Heart Disease & Angina?",
    "healthBody": "NEJM (ISCHEMIA)",
    "description": "Stable angina is chest tightness or discomfort that occurs predictably during physical effort or stress, cause...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-007",
    "label": "Type 2 Diabetes Mellitus",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Type 2 Diabetes Mellitus?",
    "healthBody": "ADA",
    "description": "In type 2 diabetes, your body’s cells become resistant to insulin—the key that lets sugar enter your cells for...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-008",
    "label": "Obesity & Weight Management",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Obesity & Weight Management?",
    "healthBody": "NEJM (SURMOUNT-1)",
    "description": "Obesity is a complex, chronic biological condition where appetite hormones and metabolism make it difficult to...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-009",
    "label": "Metabolic Dysfunction-Associated Steatohepatitis (MASH / NASH)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Metabolic Dysfunction-Associated Steatohepatitis (MASH / NASH)?",
    "healthBody": "NEJM (MAESTRO-NASH)",
    "description": "MASH is an advanced form of fatty liver where excess fat stored in liver cells causes inflammation and scarrin...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-010",
    "label": "Primary Hypothyroidism",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Hypothyroidism?",
    "healthBody": "ATA / AACE",
    "description": "Your thyroid gland in your neck produces hormones that set your body's metabolic speed. In hypothyroidism, the...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-011",
    "label": "Polycystic Ovary Syndrome (PCOS)",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polycystic Ovary Syndrome (PCOS)?",
    "healthBody": "ESHRE / ASRM / Monash",
    "description": "PCOS is a hormonal imbalance that affects how ovaries develop and release eggs, often linked to insulin resist...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-012",
    "label": "Adult Persistent Asthma",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Adult Persistent Asthma?",
    "healthBody": "GINA",
    "description": "Asthma is chronic inflammation of your airways that makes them swollen, sensitive, and tight when irritated. U...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-013",
    "label": "Chronic Obstructive Pulmonary Disease (COPD)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Obstructive Pulmonary Disease (COPD)?",
    "healthBody": "GOLD & NEJM (ETHOS)",
    "description": "COPD is long-term damage to the lungs and airways that causes them to become less elastic and easily clogged w...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-014",
    "label": "Community-Acquired Pneumonia (CAP)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Community-Acquired Pneumonia (CAP)?",
    "healthBody": "ATS / IDSA",
    "description": "Pneumonia is an infection that inflames the microscopic air sacs in one or both lungs, causing them to fill wi...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-015",
    "label": "Obstructive Sleep Apnea (OSA)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Obstructive Sleep Apnea (OSA)?",
    "healthBody": "AASM",
    "description": "Sleep apnea happens when throat muscles relax during sleep, temporarily closing your airway like a squished st...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-016",
    "label": "Chronic Kidney Disease (CKD)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Kidney Disease (CKD)?",
    "healthBody": "NEJM (DAPA-CKD) & KDIGO",
    "description": "Chronic kidney disease means your kidneys' microscopic filtering units are gradually scarred, reducing their a...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-017",
    "label": "Benign Prostatic Hyperplasia (BPH)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Benign Prostatic Hyperplasia (BPH)?",
    "healthBody": "AUA / EAU",
    "description": "BPH is a non-cancerous enlargement of the prostate gland that surrounds the urethra, squeezing the tube like a...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-018",
    "label": "Uncomplicated Urinary Tract Infection (Cystitis)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Uncomplicated Urinary Tract Infection (Cystitis)?",
    "healthBody": "IDSA / ESCMID",
    "description": "A bladder infection occurs when bacteria from nearby skin enter the urinary tract and multiply, causing inflam...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-019",
    "label": "Gastroesophageal Reflux Disease (GERD)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gastroesophageal Reflux Disease (GERD)?",
    "healthBody": "ACG",
    "description": "Acid reflux occurs when the muscular valve between your food pipe and stomach doesn't close tightly, allowing ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-020",
    "label": "Irritable Bowel Syndrome (IBS)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Irritable Bowel Syndrome (IBS)?",
    "healthBody": "ACG",
    "description": "IBS is a disorder of the gut-brain connection where your intestines have become hypersensitive, causing abdomi...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-021",
    "label": "Helicobacter pylori Infection",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Helicobacter pylori Infection?",
    "healthBody": "ACG & Maastricht VI",
    "description": "H. pylori is a tough spiral-shaped bacteria that burrows into the mucous lining of your stomach, causing ulcer...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-022",
    "label": "Celiac Disease",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Celiac Disease?",
    "healthBody": "ACG",
    "description": "Celiac disease is an autoimmune condition where eating gluten (a protein in wheat, rye, and barley) triggers y...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-023",
    "label": "Major Depressive Disorder (MDD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Major Depressive Disorder (MDD)?",
    "healthBody": "The Lancet",
    "description": "Major depression is a medical illness involving imbalances in brain circuits and neurotransmitters that affect...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-024",
    "label": "Generalized Anxiety Disorder (GAD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Generalized Anxiety Disorder (GAD)?",
    "healthBody": "NICE",
    "description": "Generalized anxiety disorder is when your brain’s alarm system gets stuck in overdrive, causing persistent, un...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-025",
    "label": "Chronic Migraine",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Migraine?",
    "healthBody": "AHS & The Lancet Neurology",
    "description": "Migraine is not just a bad headache; it is a neurological event where waves of nerve sensitivity and swelling ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-026",
    "label": "Chronic Insomnia",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Insomnia?",
    "healthBody": "ACP",
    "description": "Chronic insomnia is when difficulty falling or staying asleep becomes a habitual pattern where your brain asso...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-027",
    "label": "Early Alzheimer's Disease & Mild Cognitive Impairment",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Early Alzheimer's Disease & Mild Cognitive Impairment?",
    "healthBody": "NEJM (Clarity AD)",
    "description": "Alzheimer's disease involves the slow buildup of abnormal protein plaques and tangles in the brain, which grad...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-028",
    "label": "Rheumatoid Arthritis (RA)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Rheumatoid Arthritis (RA)?",
    "healthBody": "ACR / EULAR",
    "description": "Rheumatoid arthritis is an autoimmune condition where your immune system mistakenly attacks the lining of your...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-029",
    "label": "Knee & Hip Osteoarthritis",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Knee & Hip Osteoarthritis?",
    "healthBody": "OARSI & ACR",
    "description": "Osteoarthritis is a mechanical wear-and-repair process where the protective cartilage cushioning the ends of y...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-030",
    "label": "Gout & Hyperuricemia",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gout & Hyperuricemia?",
    "healthBody": "ACR",
    "description": "Gout occurs when high levels of uric acid form sharp needle-like microscopic crystals in your joints (often th...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-031",
    "label": "Chronic Non-Specific Lower Back Pain",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Non-Specific Lower Back Pain?",
    "healthBody": "ACP & The Lancet Series",
    "description": "Most lower back pain is related to muscle strain, ligament tension, and spinal disc irritation. Resting in bed...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-032",
    "label": "Postmenopausal Osteoporosis",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Postmenopausal Osteoporosis?",
    "healthBody": "Endocrine Society",
    "description": "Osteoporosis is a silent thinning of your bones where bone tissue breaks down faster than it rebuilds, making ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-033",
    "label": "Menopausal Vasomotor Symptoms & Hormone Therapy",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Menopausal Vasomotor Symptoms & Hormone Therapy?",
    "healthBody": "The Menopause Society (NAMS) & JAMA",
    "description": "During perimenopause and menopause, your ovaries produce less estrogen, causing your brain's temperature contr...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-034",
    "label": "Endometriosis & Chronic Pelvic Pain",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Endometriosis & Chronic Pelvic Pain?",
    "healthBody": "ESHRE",
    "description": "Endometriosis occurs when tissue similar to the lining inside your uterus grows outside the womb on other pelv...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-035",
    "label": "Preeclampsia Prevention & Management",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Preeclampsia Prevention & Management?",
    "healthBody": "USPSTF & ACOG",
    "description": "Preeclampsia is a pregnancy complication characterized by high blood pressure and signs of strain on other org...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-036",
    "label": "Gestational Diabetes Mellitus (GDM)",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gestational Diabetes Mellitus (GDM)?",
    "healthBody": "ACOG & HAPO Study",
    "description": "Gestational diabetes is temporary high blood sugar that develops during pregnancy because placental hormones i...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-037",
    "label": "Pediatric Acute Otitis Media (AOM)",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pediatric Acute Otitis Media (AOM)?",
    "healthBody": "AAP",
    "description": "An ear infection is inflammation and fluid trapped behind your child's eardrum, usually triggered by swelling ...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-038",
    "label": "Pediatric Asthma & Viral Wheeze",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pediatric Asthma & Viral Wheeze?",
    "healthBody": "GINA",
    "description": "In toddlers and young children, cold viruses can cause the small breathing tubes in their lungs to swell and w...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-039",
    "label": "Simple Febrile Seizures",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Simple Febrile Seizures?",
    "healthBody": "AAP",
    "description": "A simple febrile seizure is a brief, harmless convulsion triggered by a sudden spike in body temperature in yo...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-040",
    "label": "Pediatric Attention-Deficit/Hyperactivity Disorder (ADHD)",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pediatric Attention-Deficit/Hyperactivity Disorder (ADHD)?",
    "healthBody": "AAP & MTA Study",
    "description": "ADHD is a neurodevelopmental condition where brain circuits that regulate attention, impulse control, and dopa...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-041",
    "label": "COVID-19 Acute Outpatient Management",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for COVID-19 Acute Outpatient Management?",
    "healthBody": "NEJM (EPIC-HR) & WHO",
    "description": "COVID-19 is a viral respiratory infection that can cause severe lung inflammation in high-risk individuals. An...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-042",
    "label": "Atopic Dermatitis (Eczema)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Atopic Dermatitis (Eczema)?",
    "healthBody": "AAD",
    "description": "Eczema is a condition where your skin's outer moisture barrier is leaky and easily inflamed, allowing water to...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-043",
    "label": "Plaque Psoriasis",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Plaque Psoriasis?",
    "healthBody": "AAD / NPF",
    "description": "Psoriasis is an autoimmune condition where immune signals cause skin cells to grow way too quickly—in days ins...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-044",
    "label": "Cellulitis & Purulent Skin Infections",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cellulitis & Purulent Skin Infections?",
    "healthBody": "IDSA",
    "description": "Cellulitis is a bacterial infection of the deep skin layers and tissues, causing a localized patch of skin to ...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-045",
    "label": "Clostridioides difficile Infection (CDI)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Clostridioides difficile Infection (CDI)?",
    "healthBody": "IDSA / SHEA",
    "description": "C. diff is a spore-forming bacterial infection of the colon that often takes over after antibiotics wipe out y...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-046",
    "label": "Early Localized Lyme Disease",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Early Localized Lyme Disease?",
    "healthBody": "IDSA / AAN / ACR",
    "description": "Lyme disease is a bacterial infection transmitted by blacklegged deer ticks. In its early stage, it often caus...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-047",
    "label": "Colorectal Cancer Screening",
    "category": "Oncology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Colorectal Cancer Screening?",
    "healthBody": "USPSTF",
    "description": "Colorectal cancer screening checks for precancerous polyps (small growths on the inner colon wall) and removes...",
    "icon": "🎗️"
  },
  {
    "id": "sug-doc-card-048",
    "label": "Breast Cancer Screening",
    "category": "Oncology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Breast Cancer Screening?",
    "healthBody": "USPSTF",
    "description": "A screening mammogram is a low-dose X-ray picture of the breast used to detect tiny changes or early tumors lo...",
    "icon": "🎗️"
  },
  {
    "id": "sug-doc-card-049",
    "label": "Lung Cancer Screening",
    "category": "Oncology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Lung Cancer Screening?",
    "healthBody": "USPSTF & NEJM (NLST)",
    "description": "Low-dose CT lung screening uses a quick, low-radiation scanner to take detailed cross-section images of your l...",
    "icon": "🎗️"
  },
  {
    "id": "sug-doc-card-050",
    "label": "Cervical Cancer Screening & HPV Triage",
    "category": "Oncology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cervical Cancer Screening & HPV Triage?",
    "healthBody": "USPSTF & ASCCP",
    "description": "Cervical cancer screening checks the cells of your cervix for high-risk strains of the Human Papillomavirus (H...",
    "icon": "🎗️"
  },
  {
    "id": "sug-doc-card-051",
    "label": "Crohn's Disease (Inflammatory Bowel Disease)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Crohn's Disease (Inflammatory Bowel Disease)?",
    "healthBody": "ACG",
    "description": "Crohn's disease is an autoimmune condition where your immune system attacks the lining of your digestive tract...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-052",
    "label": "Ulcerative Colitis (Inflammatory Bowel Disease)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ulcerative Colitis (Inflammatory Bowel Disease)?",
    "healthBody": "ACG",
    "description": "Ulcerative colitis is a chronic inflammatory disease that causes continuous superficial sores (ulcers) specifi...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-053",
    "label": "Peripheral Artery Disease (PAD)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Peripheral Artery Disease (PAD)?",
    "healthBody": "AHA / ACC",
    "description": "Peripheral artery disease is caused by cholesterol plaque building up in the arteries of your legs, reducing b...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-054",
    "label": "Systemic Lupus Erythematosus (SLE)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Systemic Lupus Erythematosus (SLE)?",
    "healthBody": "EULAR",
    "description": "Lupus is a chronic autoimmune disease where the immune system loses its ability to tell the difference between...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-055",
    "label": "HIV Pre-Exposure Prophylaxis (PrEP)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for HIV Pre-Exposure Prophylaxis (PrEP)?",
    "healthBody": "CDC",
    "description": "PrEP is a highly effective preventive medication (taken as a daily pill or bi-monthly injection) that builds a...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-056",
    "label": "Chronic Hepatitis C (HCV)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Hepatitis C (HCV)?",
    "healthBody": "AASLD / IDSA",
    "description": "Hepatitis C is a viral infection that slowly damages the liver over decades. Modern antiviral pills can comple...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-057",
    "label": "Sickle Cell Disease",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sickle Cell Disease?",
    "healthBody": "ASH",
    "description": "Sickle cell disease is a genetic condition where red blood cells become hard and crescent-shaped instead of ro...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-058",
    "label": "Multiple Sclerosis (Relapsing-Remitting)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Multiple Sclerosis (Relapsing-Remitting)?",
    "healthBody": "NEJM (OPERA I/II)",
    "description": "Multiple sclerosis is an autoimmune disease where the immune system attacks myelin, the protective insulation ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-059",
    "label": "Pelvic Inflammatory Disease (PID)",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pelvic Inflammatory Disease (PID)?",
    "healthBody": "CDC",
    "description": "Pelvic inflammatory disease is a serious bacterial infection of the female reproductive organs (uterus, fallop...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-060",
    "label": "Neonatal Hyperbilirubinemia (Jaundice)",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Neonatal Hyperbilirubinemia (Jaundice)?",
    "healthBody": "AAP",
    "description": "Jaundice is a common, temporary yellowing of a newborn's skin and eyes caused by a buildup of bilirubin, a yel...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-061",
    "label": "Acute Pancreatitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Pancreatitis?",
    "healthBody": "ACG",
    "description": "Acute pancreatitis is a sudden, severe inflammation where the digestive enzymes made by the pancreas become ac...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-062",
    "label": "Cirrhosis & Portal Hypertension",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cirrhosis & Portal Hypertension?",
    "healthBody": "AASLD",
    "description": "Cirrhosis is severe scarring of the liver that blocks normal blood flow. This causes pressure to back up into ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-063",
    "label": "Acute Ischemic Stroke",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Ischemic Stroke?",
    "healthBody": "AHA / ASA",
    "description": "An ischemic stroke happens when a blood clot blocks a blood vessel in the brain, cutting off oxygen. Brain cel...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-064",
    "label": "Adult Epilepsy & Seizure Disorders",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Adult Epilepsy & Seizure Disorders?",
    "healthBody": "AAN / AES",
    "description": "Epilepsy is a neurological disorder where clusters of nerve cells in the brain sometimes signal abnormally, ca...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-065",
    "label": "Bipolar I Disorder",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bipolar I Disorder?",
    "healthBody": "CANMAT / ISBD",
    "description": "Bipolar disorder is a brain condition that causes extreme, uncontrollable shifts in mood, energy, and activity...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-066",
    "label": "Post-Traumatic Stress Disorder (PTSD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Post-Traumatic Stress Disorder (PTSD)?",
    "healthBody": "APA / VA/DoD",
    "description": "PTSD is a condition where the brain's 'fight or flight' alarm system stays stuck in the ON position long after...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-067",
    "label": "Sepsis & Septic Shock",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sepsis & Septic Shock?",
    "healthBody": "Surviving Sepsis Campaign (SCC)",
    "description": "Sepsis is a life-threatening emergency where the body's immune system overreacts to an infection, causing wide...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-068",
    "label": "Active Tuberculosis (TB)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Active Tuberculosis (TB)?",
    "healthBody": "ATS / CDC / IDSA",
    "description": "Tuberculosis is a serious bacterial infection that usually attacks the lungs. It requires a long, uninterrupte...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-069",
    "label": "Syphilis",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Syphilis?",
    "healthBody": "CDC",
    "description": "Syphilis is a bacterial infection typically spread by sexual contact that progresses in stages. If treated ear...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-070",
    "label": "Bacterial Meningitis",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bacterial Meningitis?",
    "healthBody": "IDSA",
    "description": "Bacterial meningitis is a life-threatening infection of the membranes surrounding the brain and spinal cord, c...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-071",
    "label": "Hyperthyroidism & Graves' Disease",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hyperthyroidism & Graves' Disease?",
    "healthBody": "ATA",
    "description": "Graves' disease is an autoimmune condition where antibodies act like a broken thermostat, telling your thyroid...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-072",
    "label": "Acute Kidney Injury (AKI)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Kidney Injury (AKI)?",
    "healthBody": "KDIGO",
    "description": "Acute kidney injury is a sudden drop in kidney function, often caused by severe dehydration, toxic medications...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-073",
    "label": "Idiopathic Pulmonary Fibrosis (IPF)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Idiopathic Pulmonary Fibrosis (IPF)?",
    "healthBody": "ATS / ERS / JRS / ALAT",
    "description": "Idiopathic pulmonary fibrosis is a progressive disease where the delicate air sacs in the lungs become thick, ...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-074",
    "label": "Heart Failure with Preserved Ejection Fraction (HFpEF)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Heart Failure with Preserved Ejection Fraction (HFpEF)?",
    "healthBody": "NEJM (EMPEROR-Preserved)",
    "description": "In HFpEF (diastolic heart failure), your heart pumps with normal strength, but the heart muscle is too stiff t...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-075",
    "label": "Parkinson's Disease",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Parkinson's Disease?",
    "healthBody": "MDS",
    "description": "Parkinson's disease occurs when the brain slowly stops producing dopamine, a chemical essential for smooth, co...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-076",
    "label": "Fibromyalgia",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Fibromyalgia?",
    "healthBody": "ACR / EULAR",
    "description": "Fibromyalgia is a central nervous system disorder where the brain's pain-processing center acts like a stereo ...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-077",
    "label": "Gallstone Disease (Cholelithiasis & Cholecystitis)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gallstone Disease (Cholelithiasis & Cholecystitis)?",
    "healthBody": "EASL",
    "description": "Gallstones are hard, pebble-like deposits of cholesterol or bilirubin that form in the gallbladder. If they bl...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-078",
    "label": "Schizophrenia",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Schizophrenia?",
    "healthBody": "APA",
    "description": "Schizophrenia is a severe brain disorder that interferes with a person's ability to think clearly, manage emot...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-079",
    "label": "Diabetic Peripheral Neuropathy",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diabetic Peripheral Neuropathy?",
    "healthBody": "ADA",
    "description": "Diabetic neuropathy occurs when chronic high blood sugar damages the tiny blood vessels that feed your nerves,...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-080",
    "label": "Chronic Venous Insufficiency (CVI) & Varicose Veins",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Venous Insufficiency (CVI) & Varicose Veins?",
    "healthBody": "SVS / AVF",
    "description": "Chronic venous insufficiency happens when the one-way valves in your leg veins fail. Instead of pumping blood ...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-081",
    "label": "Non-ST-Elevation Acute Coronary Syndrome (NSTEMI / Unstable Angina)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Non-ST-Elevation Acute Coronary Syndrome (NSTEMI / Unstable Angina)?",
    "healthBody": "AHA / ACC",
    "description": "An NSTEMI is a type of heart attack where a cholesterol plaque ruptures and partially blocks a heart artery, c...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-082",
    "label": "Anaphylaxis",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Anaphylaxis?",
    "healthBody": "AAAAI / ACAAI / WAO",
    "description": "Anaphylaxis is a severe, whole-body allergic reaction that happens rapidly. It can cause your throat to swell ...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-083",
    "label": "Acute Diverticulitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Diverticulitis?",
    "healthBody": "AGA",
    "description": "Diverticulitis happens when small, bulging pouches in the lining of your large intestine become inflamed or in...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-084",
    "label": "Giant Cell Arteritis (Temporal Arteritis)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Giant Cell Arteritis (Temporal Arteritis)?",
    "healthBody": "ACR",
    "description": "Giant cell arteritis is severe inflammation of the blood vessels in your scalp, neck, and arms. If the inflamm...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-085",
    "label": "Primary Open-Angle Glaucoma (POAG)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Open-Angle Glaucoma (POAG)?",
    "healthBody": "AAO",
    "description": "Open-angle glaucoma is a slow, painless disease where fluid builds up inside the eye, raising the pressure and...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-086",
    "label": "Age-Related Macular Degeneration (AMD)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Age-Related Macular Degeneration (AMD)?",
    "healthBody": "AAO & NEJM (AREDS2)",
    "description": "Macular degeneration damages the macula—the center part of the retina responsible for sharp, straight-ahead vi...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-087",
    "label": "Bell's Palsy (Idiopathic Facial Paralysis)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bell's Palsy (Idiopathic Facial Paralysis)?",
    "healthBody": "AAN",
    "description": "Bell's palsy is a sudden, temporary weakness or paralysis of the muscles on one side of your face, believed to...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-088",
    "label": "Carpal Tunnel Syndrome",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Carpal Tunnel Syndrome?",
    "healthBody": "AAOS",
    "description": "Carpal tunnel syndrome occurs when the median nerve is squeezed or compressed as it travels through a narrow p...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-089",
    "label": "Mild Traumatic Brain Injury (Concussion)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Mild Traumatic Brain Injury (Concussion)?",
    "healthBody": "CDC & AAN",
    "description": "A concussion is a mild brain injury caused by a jolt to the head that disrupts normal brain function. The brai...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-090",
    "label": "Allergic Rhinitis (Hay Fever)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Allergic Rhinitis (Hay Fever)?",
    "healthBody": "AAAI / ACAAI",
    "description": "Allergic rhinitis occurs when your immune system overreacts to harmless particles like pollen or dust, causing...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-091",
    "label": "Chronic Spontaneous Urticaria (Hives)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Spontaneous Urticaria (Hives)?",
    "healthBody": "EAACI / WAO",
    "description": "Chronic hives are itchy, raised, red welts on the skin that come and go daily for more than 6 weeks, usually c...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-092",
    "label": "Acne Vulgaris",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acne Vulgaris?",
    "healthBody": "AAD",
    "description": "Acne is an inflammatory skin condition where dead skin cells and oil plug hair follicles, allowing bacteria to...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-093",
    "label": "Polymyalgia Rheumatica (PMR)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polymyalgia Rheumatica (PMR)?",
    "healthBody": "ACR / EULAR",
    "description": "Polymyalgia rheumatica is an inflammatory disorder causing widespread muscle aching and severe morning stiffne...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-094",
    "label": "Thyroid Nodules",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Thyroid Nodules?",
    "healthBody": "ATA",
    "description": "A thyroid nodule is a solid or fluid-filled lump within the thyroid gland in your neck. The vast majority are ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-095",
    "label": "Ectopic Pregnancy",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ectopic Pregnancy?",
    "healthBody": "ACOG",
    "description": "An ectopic pregnancy occurs when a fertilized egg implants outside the uterus, most commonly in a fallopian tu...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-096",
    "label": "Postmenopausal Bleeding & Endometrial Hyperplasia",
    "category": "Women's Health",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Postmenopausal Bleeding & Endometrial Hyperplasia?",
    "healthBody": "ACOG",
    "description": "Any vaginal bleeding that occurs more than 12 months after your last menstrual period is abnormal. While it is...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-097",
    "label": "Erectile Dysfunction (ED)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Erectile Dysfunction (ED)?",
    "healthBody": "AUA",
    "description": "Erectile dysfunction is often a plumbing issue caused by the same plaque buildup that causes heart disease. Th...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-098",
    "label": "Restless Legs Syndrome (RLS)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Restless Legs Syndrome (RLS)?",
    "healthBody": "AAN",
    "description": "Restless legs syndrome is a neurological disorder causing an overwhelming, uncomfortable urge to move your leg...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-099",
    "label": "Acute Appendicitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Appendicitis?",
    "healthBody": "WSES",
    "description": "Appendicitis is a sudden infection and inflammation of the appendix, a small pouch attached to the large intes...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-100",
    "label": "Hyperkalemia (Elevated Blood Potassium)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hyperkalemia (Elevated Blood Potassium)?",
    "healthBody": "KDIGO",
    "description": "Hyperkalemia is dangerously high potassium in the blood, usually because the kidneys cannot filter it out. Bec...",
    "icon": "💧"
  }
];

export function getMatchingSuggestions(input: string, limit: number = 8): SearchSuggestion[] {
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

    if (labelLower.includes(clean)) score += 60;
    if (queryLower.includes(clean)) score += 35;

    words.forEach((w) => {
      if (labelLower.includes(w)) score += 25;
      if (queryLower.includes(w)) score += 15;
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
