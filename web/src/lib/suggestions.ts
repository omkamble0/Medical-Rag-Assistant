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
  },
  {
    "id": "sug-doc-card-101",
    "label": "Aortic Valve Stenosis",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Aortic Valve Stenosis?",
    "healthBody": "NEJM (PARTNER 3)",
    "description": "Aortic stenosis is like a doorway in your heart's main valve that has become calcified, stiff, and narrow. Whe...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-102",
    "label": "Hypertrophic Cardiomyopathy (HCM)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypertrophic Cardiomyopathy (HCM)?",
    "healthBody": "The Lancet (EXPLORER-HCM)",
    "description": "Hypertrophic cardiomyopathy is a genetic condition where the heart muscle walls become abnormally thick and bu...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-103",
    "label": "Infective Endocarditis",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Infective Endocarditis?",
    "healthBody": "Circulation (AHA)",
    "description": "Infective endocarditis is a bacterial infection of the heart's inner lining and valves. Bacteria enter the blo...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-104",
    "label": "Acute Pericarditis",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Pericarditis?",
    "healthBody": "NEJM (ICAP)",
    "description": "Pericarditis is inflammation of the double-layered protective sac (the pericardium) that wraps around your hea...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-105",
    "label": "Abdominal Aortic Aneurysm (AAA)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Abdominal Aortic Aneurysm (AAA)?",
    "healthBody": "Eur J Vasc Endovasc Surg (ESVS)",
    "description": "An abdominal aortic aneurysm is a bulge or ballooning in the main blood vessel (the aorta) that carries blood ...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-106",
    "label": "Neurogenic Orthostatic Hypotension (nOH)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Neurogenic Orthostatic Hypotension (nOH)?",
    "healthBody": "Clin Auton Res (AAS/EFNS)",
    "description": "Orthostatic hypotension means your blood pressure drops sharply when you stand up. Normally, nerve reflexes sq...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-107",
    "label": "Postural Orthostatic Tachycardia Syndrome (POTS)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Postural Orthostatic Tachycardia Syndrome (POTS)?",
    "healthBody": "Heart Rhythm (HRS)",
    "description": "POTS is a condition where your body has trouble balancing blood flow when you are upright. When you stand, blo...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-108",
    "label": "Raynaud's Phenomenon",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Raynaud's Phenomenon?",
    "healthBody": "NEJM Review",
    "description": "Raynaud's phenomenon is an over-reaction of the tiny blood vessels in your fingers and toes to cold temperatur...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-109",
    "label": "Sick Sinus Syndrome (Bradycardia-Tachycardia)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sick Sinus Syndrome (Bradycardia-Tachycardia)?",
    "healthBody": "Circulation (ACC/AHA/HRS)",
    "description": "Sick sinus syndrome is a problem with your heart's natural electrical pacemaker (the sinus node). Over time, t...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-110",
    "label": "Supraventricular Tachycardia (AVNRT / AVRT)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Supraventricular Tachycardia (AVNRT / AVRT)?",
    "healthBody": "Circulation (ACC/AHA/HRS)",
    "description": "Supraventricular tachycardia (SVT) is a condition where an extra electrical wire or short-circuit in your hear...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-111",
    "label": "Pulmonary Arterial Hypertension (PAH)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pulmonary Arterial Hypertension (PAH)?",
    "healthBody": "Eur Heart J (ESC/ERS)",
    "description": "Pulmonary arterial hypertension means blood pressure inside the arteries of your lungs is dangerously high. It...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-112",
    "label": "Bronchiectasis (Non-Cystic Fibrosis)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bronchiectasis (Non-Cystic Fibrosis)?",
    "healthBody": "Eur Respir J (ERS)",
    "description": "Bronchiectasis is a condition where the airways in your lungs have become abnormally widened, scarred, and fla...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-113",
    "label": "Pulmonary Sarcoidosis",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pulmonary Sarcoidosis?",
    "healthBody": "Am J Respir Crit Care Med (ATS)",
    "description": "Sarcoidosis is an immune system condition where your white blood cells cluster together to form microscopic in...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-114",
    "label": "Chronic Hypersensitivity Pneumonitis (HP)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Hypersensitivity Pneumonitis (HP)?",
    "healthBody": "Am J Respir Crit Care Med (ATS)",
    "description": "Hypersensitivity pneumonitis is an allergic reaction deep inside the air sacs of your lungs caused by repeated...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-115",
    "label": "Pleural Effusion & Empyema",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pleural Effusion & Empyema?",
    "healthBody": "Thorax (BTS)",
    "description": "A pleural effusion is an abnormal buildup of fluid in the space between your lung and your chest wall, like wa...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-116",
    "label": "Acute Bronchitis",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Bronchitis?",
    "healthBody": "Cochrane Database Syst Rev",
    "description": "Acute bronchitis is a temporary viral infection of the large breathing tubes in your lungs, usually coming aft...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-117",
    "label": "Chronic Refractory Cough",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Refractory Cough?",
    "healthBody": "Eur Respir J (ERS)",
    "description": "Chronic cough is a cough that lingers for more than 8 weeks after any initial infection has cleared. Often, th...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-118",
    "label": "Asbestosis & Occupational Pneumoconiosis",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Asbestosis & Occupational Pneumoconiosis?",
    "healthBody": "Scand J Work Environ Health (Helsinki)",
    "description": "Asbestosis is scarring of the lung tissue caused by inhaling microscopic asbestos mineral fibers years ago at ...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-119",
    "label": "Type 1 Diabetes Mellitus",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Type 1 Diabetes Mellitus?",
    "healthBody": "Diabetes Care (ADA/EASD)",
    "description": "Type 1 diabetes is an autoimmune condition where your body's immune system mistakenly attacks the insulin-prod...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-120",
    "label": "Diabetic Ketoacidosis (DKA)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diabetic Ketoacidosis (DKA)?",
    "healthBody": "Diabet Med (JBDS/ADA)",
    "description": "Diabetic ketoacidosis (DKA) is a life-threatening medical emergency where the body has so little insulin that ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-121",
    "label": "Primary Adrenal Insufficiency (Addison's Disease)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Adrenal Insufficiency (Addison's Disease)?",
    "healthBody": "J Clin Endocrinol Metab",
    "description": "Addison's disease is like having an empty battery in your body's stress hormone factory. Your adrenal glands c...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-122",
    "label": "Cushing's Syndrome (Hypercortisolism)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cushing's Syndrome (Hypercortisolism)?",
    "healthBody": "J Clin Endocrinol Metab",
    "description": "Cushing's syndrome is like your body's stress alarm getting permanently stuck in the 'ON' position. An excess ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-123",
    "label": "Primary Hyperparathyroidism",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Hyperparathyroidism?",
    "healthBody": "J Bone Miner Res",
    "description": "Primary hyperparathyroidism occurs when one of the four tiny rice-sized glands behind your thyroid produces to...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-124",
    "label": "Hypoparathyroidism",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypoparathyroidism?",
    "healthBody": "Eur J Endocrinol",
    "description": "Hypoparathyroidism is a shortage of parathyroid hormone, usually after neck or thyroid surgery. Without this h...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-125",
    "label": "Familial Hypercholesterolemia (HeFH)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Familial Hypercholesterolemia (HeFH)?",
    "healthBody": "Eur Heart J",
    "description": "Familial hypercholesterolemia is an inherited gene mutation that prevents your liver from filtering 'bad' LDL ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-126",
    "label": "Male Hypogonadism (Testosterone Deficiency)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Male Hypogonadism (Testosterone Deficiency)?",
    "healthBody": "J Clin Endocrinol Metab",
    "description": "Male hypogonadism happens when a man's testicles or pituitary gland produce abnormally low levels of testoster...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-127",
    "label": "Polycystic Ovary Syndrome (PCOS)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polycystic Ovary Syndrome (PCOS)?",
    "healthBody": "Fertil Steril",
    "description": "PCOS is a hormonal and metabolic imbalance where ovaries make slightly higher levels of androgen hormones and ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-128",
    "label": "Peptic Ulcer Disease (PUD)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Peptic Ulcer Disease (PUD)?",
    "healthBody": "Am J Gastroenterol",
    "description": "A peptic ulcer is an open sore on the lining of your stomach or upper intestine, most often caused by a stomac...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-129",
    "label": "Chronic Hepatitis B Infection",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Hepatitis B Infection?",
    "healthBody": "Hepatology",
    "description": "Chronic hepatitis B is a persistent viral infection in your liver. While many people have zero symptoms for ye...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-130",
    "label": "Gastroparesis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gastroparesis?",
    "healthBody": "Am J Gastroenterol",
    "description": "Gastroparesis, or 'stomach paralysis', means the stomach muscles take far too long to push food into the intes...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-131",
    "label": "Achalasia",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Achalasia?",
    "healthBody": "Am J Gastroenterol",
    "description": "Achalasia is a condition where the muscular valve at the bottom of your swallowing tube (the esophagus) cannot...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-132",
    "label": "Microscopic Colitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Microscopic Colitis?",
    "healthBody": "Gastroenterology",
    "description": "Microscopic colitis is an inflammatory bowel condition where the large intestine looks completely normal to th...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-133",
    "label": "Autoimmune Hepatitis (AIH)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Autoimmune Hepatitis (AIH)?",
    "healthBody": "Hepatology",
    "description": "Autoimmune hepatitis is a condition where your own immune defense system gets confused and attacks your liver ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-134",
    "label": "Primary Biliary Cholangitis (PBC)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Biliary Cholangitis (PBC)?",
    "healthBody": "Hepatology",
    "description": "Primary biliary cholangitis is an autoimmune condition where the immune system attacks and damages the tiny dr...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-135",
    "label": "Acute Pancreatitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Pancreatitis?",
    "healthBody": "Am J Gastroenterol",
    "description": "Acute pancreatitis is sudden, severe inflammation of the pancreas gland behind your stomach. Digestive enzymes...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-136",
    "label": "Hemorrhoidal Disease and Anal Fissure",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hemorrhoidal Disease and Anal Fissure?",
    "healthBody": "Dis Colon Rectum",
    "description": "Hemorrhoids are swollen, inflamed blood vessel cushions in your lower rectum, while an anal fissure is a small...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-137",
    "label": "Acute Diverticulitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Diverticulitis?",
    "healthBody": "Gastroenterology",
    "description": "Diverticulitis occurs when small pouches in your colon wall become inflamed or irritated. This typically cause...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-138",
    "label": "Small Intestinal Bacterial Overgrowth (SIBO)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Small Intestinal Bacterial Overgrowth (SIBO)?",
    "healthBody": "Am J Gastroenterol",
    "description": "SIBO occurs when bacteria that normally belong in the large intestine migrate backwards and colonize the small...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-139",
    "label": "Barrett's Esophagus",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Barrett's Esophagus?",
    "healthBody": "Am J Gastroenterol",
    "description": "Barrett's esophagus happens when years of acid reflux irritate the bottom of your swallowing tube. To protect ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-140",
    "label": "Clostridioides difficile Infection (CDI)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Clostridioides difficile Infection (CDI)?",
    "healthBody": "Clin Infect Dis",
    "description": "C. diff is a stubborn bacterial infection of the colon that takes over when strong antibiotics wipe out your b...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-141",
    "label": "Transient Ischemic Attack (TIA)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Transient Ischemic Attack (TIA)?",
    "healthBody": "Stroke",
    "description": "A TIA (transient ischemic attack), sometimes called a 'warning stroke' or 'mini-stroke', occurs when blood flo...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-142",
    "label": "Myasthenia Gravis",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Myasthenia Gravis?",
    "healthBody": "Neurology",
    "description": "Myasthenia gravis is an autoimmune condition where your body's antibodies block communication between your ner...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-143",
    "label": "Trigeminal Neuralgia",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Trigeminal Neuralgia?",
    "healthBody": "Eur J Neurol",
    "description": "Trigeminal neuralgia, sometimes referred to as 'tic douloureux', is a severe nerve pain disorder caused by an ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-144",
    "label": "Essential Tremor",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Essential Tremor?",
    "healthBody": "Neurology",
    "description": "Essential tremor is a nervous system disorder that causes rhythmic shaking of your hands when you try to use t...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-145",
    "label": "Normal Pressure Hydrocephalus (NPH)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Normal Pressure Hydrocephalus (NPH)?",
    "healthBody": "Neurosurgery",
    "description": "Normal pressure hydrocephalus is a treatable brain condition where excess spinal fluid slowly builds up in the...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-146",
    "label": "Cluster Headache",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cluster Headache?",
    "healthBody": "Headache",
    "description": "Cluster headaches are excruciating, one-sided headaches centered around or behind one eye that strike in clust...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-147",
    "label": "Amyotrophic Lateral Sclerosis (ALS)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Amyotrophic Lateral Sclerosis (ALS)?",
    "healthBody": "Eur J Neurol",
    "description": "Amyotrophic lateral sclerosis (ALS), also known as Lou Gehrig's disease, is a condition where the nerve cells ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-148",
    "label": "Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)?",
    "healthBody": "JAMA",
    "description": "Idiopathic intracranial hypertension, or pseudotumor cerebri, occurs when fluid pressure builds up inside your...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-149",
    "label": "Restless Legs Syndrome (RLS / Willis-Ekbom Disease)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Restless Legs Syndrome (RLS / Willis-Ekbom Disease)?",
    "healthBody": "Neurology",
    "description": "Restless legs syndrome is a neurological sensory condition that causes an overwhelming, creepy-crawly urge to ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-150",
    "label": "Bell's Palsy (Idiopathic Facial Paralysis)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bell's Palsy (Idiopathic Facial Paralysis)?",
    "healthBody": "Otolaryngol Head Neck Surg",
    "description": "Bell's palsy is a sudden, temporary weakness or paralysis of the muscles on one side of your face caused by in...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-151",
    "label": "Nephrolithiasis (Kidney Stones)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Nephrolithiasis (Kidney Stones)?",
    "healthBody": "J Urol",
    "description": "Kidney stones are hard mineral crystal deposits that form inside your kidneys when your urine becomes overly c...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-152",
    "label": "Autosomal Dominant Polycystic Kidney Disease (ADPKD)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Autosomal Dominant Polycystic Kidney Disease (ADPKD)?",
    "healthBody": "N Engl J Med",
    "description": "Autosomal dominant polycystic kidney disease (ADPKD) is a genetic condition where thousands of fluid-filled sa...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-153",
    "label": "Nephrotic Syndrome",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Nephrotic Syndrome?",
    "healthBody": "Kidney Int",
    "description": "Nephrotic syndrome is a kidney condition where the tiny filtering units in your kidneys (glomeruli) become dam...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-154",
    "label": "IgA Nephropathy (Berger's Disease)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for IgA Nephropathy (Berger's Disease)?",
    "healthBody": "The Lancet",
    "description": "IgA nephropathy is an immune disorder where abnormal antibodies called IgA get trapped in the microscopic filt...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-155",
    "label": "Overactive Bladder (OAB)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Overactive Bladder (OAB)?",
    "healthBody": "J Urol",
    "description": "Overactive bladder is a condition where your bladder muscles squeeze and spasm before your bladder is actually...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-156",
    "label": "Stress Urinary Incontinence",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Stress Urinary Incontinence?",
    "healthBody": "Obstet Gynecol",
    "description": "Stress urinary incontinence happens when the muscles and tissues supporting your bladder and urethra weaken. S...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-157",
    "label": "Interstitial Cystitis (Bladder Pain Syndrome)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Interstitial Cystitis (Bladder Pain Syndrome)?",
    "healthBody": "J Urol",
    "description": "Interstitial cystitis, or bladder pain syndrome, is a chronic inflammatory condition where you feel aching, pr...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-158",
    "label": "Chronic Prostatitis / Chronic Pelvic Pain Syndrome (CP/CPPS)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Prostatitis / Chronic Pelvic Pain Syndrome (CP/CPPS)?",
    "healthBody": "Eur Urol",
    "description": "Chronic pelvic pain syndrome in men causes ongoing aching pain, pressure, or discomfort in the pelvic floor, g...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-159",
    "label": "Benign Prostatic Hyperplasia (BPH) with LUTS",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Benign Prostatic Hyperplasia (BPH) with LUTS?",
    "healthBody": "J Urol",
    "description": "Benign prostatic hyperplasia (BPH) is an age-related, non-cancerous enlargement of the prostate gland in men. ...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-160",
    "label": "Acute Kidney Injury (AKI)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Kidney Injury (AKI)?",
    "healthBody": "Kidney Int Suppl",
    "description": "Acute kidney injury is a sudden, sharp decline in kidney function that occurs over hours or days. When the kid...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-161",
    "label": "Ankylosing Spondylitis (Axial Spondyloarthritis)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ankylosing Spondylitis (Axial Spondyloarthritis)?",
    "healthBody": "Ann Rheum Dis",
    "description": "Ankylosing spondylitis is a chronic autoimmune form of arthritis that targets your spine and pelvic joints. Un...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-162",
    "label": "Psoriatic Arthritis (PsA)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Psoriatic Arthritis (PsA)?",
    "healthBody": "Nat Rev Rheumatol",
    "description": "Psoriatic arthritis is an autoimmune condition where your immune system attacks both your skin and your joints...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-163",
    "label": "Systemic Sclerosis (Scleroderma)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Systemic Sclerosis (Scleroderma)?",
    "healthBody": "Ann Rheum Dis",
    "description": "Systemic sclerosis, or scleroderma, is a rare autoimmune disorder where the body produces too much collagen pr...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-164",
    "label": "Sjögren's Syndrome",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sjögren's Syndrome?",
    "healthBody": "Ann Rheum Dis",
    "description": "Sjögren's syndrome is an autoimmune condition where your immune system attacks your body's moisture-producing ...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-165",
    "label": "Polymyalgia Rheumatica (PMR)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polymyalgia Rheumatica (PMR)?",
    "healthBody": "Ann Rheum Dis",
    "description": "Polymyalgia rheumatica (PMR) is an inflammatory condition affecting older adults that causes severe stiffness ...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-166",
    "label": "Dermatomyositis / Polymyositis",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dermatomyositis / Polymyositis?",
    "healthBody": "N Engl J Med",
    "description": "Dermatomyositis is an autoimmune condition where your immune system causes inflammation in both your muscles a...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-167",
    "label": "Rotator Cuff Tendinopathy and Tears",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Rotator Cuff Tendinopathy and Tears?",
    "healthBody": "J Am Acad Orthop Surg",
    "description": "The rotator cuff is a team of four muscles and tendons that keep your shoulder ball centered in its socket. We...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-168",
    "label": "Plantar Fasciitis",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Plantar Fasciitis?",
    "healthBody": "J Orthop Sports Phys Ther",
    "description": "Plantar fasciitis is an irritation and thickening of the strong, shock-absorbing band of tissue that supports ...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-169",
    "label": "Adhesive Capsulitis (Frozen Shoulder)",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Adhesive Capsulitis (Frozen Shoulder)?",
    "healthBody": "J Orthop Sports Phys Ther",
    "description": "Adhesive capsulitis, commonly called 'frozen shoulder', happens when the strong capsule of connective tissue s...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-170",
    "label": "Lumbar Spinal Stenosis",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Lumbar Spinal Stenosis?",
    "healthBody": "Spine J",
    "description": "Lumbar spinal stenosis is an age-related narrowing of the bone canal in your lower back that houses your nerve...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-171",
    "label": "Herpes Zoster (Shingles)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Herpes Zoster (Shingles)?",
    "healthBody": "N Engl J Med",
    "description": "Shingles is a painful blistering rash caused by the chickenpox virus waking up after sleeping quietly in your ...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-172",
    "label": "Infectious Mononucleosis (Epstein-Barr Virus)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Infectious Mononucleosis (Epstein-Barr Virus)?",
    "healthBody": "N Engl J Med",
    "description": "Infectious mononucleosis ('mono') is a viral infection caused by the Epstein-Barr virus, spread through saliva...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-173",
    "label": "Influenza Infection (Flu)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Influenza Infection (Flu)?",
    "healthBody": "Clin Infect Dis",
    "description": "Influenza, or the flu, is a highly contagious viral lung infection that strikes suddenly like a freight train,...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-174",
    "label": "Malaria (Plasmodium falciparum / vivax)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Malaria (Plasmodium falciparum / vivax)?",
    "healthBody": "The Lancet",
    "description": "Malaria is a serious, mosquito-transmitted blood infection caused by microscopic parasites that multiply insid...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-175",
    "label": "Dengue Fever",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dengue Fever?",
    "healthBody": "N Engl J Med",
    "description": "Dengue fever, known as 'breakbone fever' due to the intense pain in your muscles and joints, is a mosquito-spr...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-176",
    "label": "Community-Acquired MRSA Skin Infection",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Community-Acquired MRSA Skin Infection?",
    "healthBody": "N Engl J Med",
    "description": "A MRSA skin abscess is a bacterial infection of the skin that forms a tender, pus-filled boil, often mistaken ...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-177",
    "label": "Giardiasis",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Giardiasis?",
    "healthBody": "Cochrane Database Syst Rev",
    "description": "Giardiasis, sometimes called 'beaver fever', is a microscopic parasite infection in your intestines picked up ...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-178",
    "label": "Streptococcal Pharyngitis (Strep Throat)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Streptococcal Pharyngitis (Strep Throat)?",
    "healthBody": "Clin Infect Dis",
    "description": "Strep throat is a contagious bacterial throat infection caused by Group A Streptococcus bacteria. It typically...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-179",
    "label": "Lyme Disease (Borrelia burgdorferi)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Lyme Disease (Borrelia burgdorferi)?",
    "healthBody": "Clin Infect Dis",
    "description": "Lyme disease is a bacterial infection spread by the bite of an infected blacklegged deer tick. The classic fir...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-180",
    "label": "Sepsis and Septic Shock",
    "category": "Critical Care",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sepsis and Septic Shock?",
    "healthBody": "Crit Care Med",
    "description": "Sepsis is a medical emergency that happens when your body's immune system has an extreme, overwhelming respons...",
    "icon": "🚨"
  },
  {
    "id": "sug-doc-card-181",
    "label": "Iron Deficiency Anemia (IDA)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Iron Deficiency Anemia (IDA)?",
    "healthBody": "Gastroenterology",
    "description": "Iron deficiency anemia occurs when your body does not have enough iron mineral to build hemoglobin, the iron-r...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-182",
    "label": "Vitamin B12 Deficiency (Pernicious / Megaloblastic Anemia)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vitamin B12 Deficiency (Pernicious / Megaloblastic Anemia)?",
    "healthBody": "N Engl J Med",
    "description": "Vitamin B12 deficiency is a shortage of a vital nutrient needed to produce healthy red blood cells and maintai...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-183",
    "label": "Immune Thrombocytopenia (ITP)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Immune Thrombocytopenia (ITP)?",
    "healthBody": "Blood Adv",
    "description": "Immune thrombocytopenia (ITP) is a condition where your immune system mistakenly creates antibodies that tag y...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-184",
    "label": "Multiple Myeloma",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Multiple Myeloma?",
    "healthBody": "The Lancet",
    "description": "Multiple myeloma is a cancer of the plasma cells, which are the white blood cells that make antibodies. When a...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-185",
    "label": "Chronic Lymphocytic Leukemia (CLL)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Lymphocytic Leukemia (CLL)?",
    "healthBody": "The Lancet (ELEVATE-TN)",
    "description": "Chronic lymphocytic leukemia (CLL) is a slow-growing cancer of the blood and bone marrow involving white blood...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-186",
    "label": "Polycythemia Vera (PV)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polycythemia Vera (PV)?",
    "healthBody": "N Engl J Med",
    "description": "Polycythemia vera is a rare chronic bone marrow condition where a gene mutation instructs your marrow factorie...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-187",
    "label": "Rosacea",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Rosacea?",
    "healthBody": "Cochrane Database Syst Rev",
    "description": "Rosacea is a chronic skin condition causing persistent facial redness, flushing, and small acne-like bumps acr...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-188",
    "label": "Alopecia Areata",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Alopecia Areata?",
    "healthBody": "N Engl J Med",
    "description": "Alopecia areata is an autoimmune condition where your body's immune cells mistakenly attack the roots of your ...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-189",
    "label": "Hidradenitis Suppurativa",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hidradenitis Suppurativa?",
    "healthBody": "The Lancet",
    "description": "Hidradenitis suppurativa is a painful, chronic inflammatory skin condition where clogged hair follicles in sen...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-190",
    "label": "Vitiligo",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vitiligo?",
    "healthBody": "N Engl J Med",
    "description": "Vitiligo is an autoimmune condition where your body's immune defense system attacks its own pigment-producing ...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-191",
    "label": "Obsessive-Compulsive Disorder (OCD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Obsessive-Compulsive Disorder (OCD)?",
    "healthBody": "Am J Psychiatry",
    "description": "OCD is a mental health condition where your brain gets stuck on distressing, intrusive thoughts, doubts, or fe...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-192",
    "label": "Panic Disorder",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Panic Disorder?",
    "healthBody": "Cochrane Database Syst Rev",
    "description": "Panic disorder is a condition where your body's 'fight-or-flight' alarm system misfires without any real dange...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-193",
    "label": "Social Anxiety Disorder (Social Phobia)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Social Anxiety Disorder (Social Phobia)?",
    "healthBody": "The Lancet Psychiatry",
    "description": "Social anxiety disorder is far more intense than ordinary shyness. It is an intense, paralyzing fear of being ...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-194",
    "label": "Alcohol Use Disorder (AUD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Alcohol Use Disorder (AUD)?",
    "healthBody": "Am J Psychiatry",
    "description": "Alcohol use disorder is a chronic medical brain disease where changes in brain chemistry make it extremely dif...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-195",
    "label": "Uterine Leiomyomas (Fibroids)",
    "category": "Gynecology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Uterine Leiomyomas (Fibroids)?",
    "healthBody": "Obstet Gynecol",
    "description": "Uterine fibroids are non-cancerous muscular growths that develop in the wall of your uterus. While many cause ...",
    "icon": "🌸"
  },
  {
    "id": "sug-doc-card-196",
    "label": "Postpartum Depression (PPD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Postpartum Depression (PPD)?",
    "healthBody": "Am J Psychiatry",
    "description": "Postpartum depression is a medical complication of childbirth caused by massive hormonal drops and chemical sh...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-197",
    "label": "Croup (Laryngotracheobronchitis)",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Croup (Laryngotracheobronchitis)?",
    "healthBody": "Cochrane Database Syst Rev",
    "description": "Croup is a common childhood viral infection that causes swelling in the voice box and windpipe just below the ...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-198",
    "label": "Pediatric Bronchiolitis (RSV)",
    "category": "Pediatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pediatric Bronchiolitis (RSV)?",
    "healthBody": "Pediatrics",
    "description": "Bronchiolitis is a common winter viral infection (most often caused by RSV) that clogs the tiniest breathing b...",
    "icon": "🧸"
  },
  {
    "id": "sug-doc-card-199",
    "label": "Benign Paroxysmal Positional Vertigo (BPPV)",
    "category": "ENT",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Benign Paroxysmal Positional Vertigo (BPPV)?",
    "healthBody": "Otolaryngol Head Neck Surg",
    "description": "BPPV is a common inner-ear balance disorder where tiny calcium 'ear stones' come loose from their normal spot ...",
    "icon": "👂"
  },
  {
    "id": "sug-doc-card-200",
    "label": "Diabetic Retinopathy",
    "category": "Ophthalmology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diabetic Retinopathy?",
    "healthBody": "Ophthalmology",
    "description": "Diabetic retinopathy is damage to the delicate blood vessels in the light-sensing retina at the back of your e...",
    "icon": "👁️"
  },
  {
    "id": "sug-doc-card-201",
    "label": "Mitral Valve Regurgitation",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Mitral Valve Regurgitation?",
    "healthBody": "NEJM (COAPT Trial) & ACC/AHA",
    "description": "The mitral valve is like a one-way swinging door that lets blood flow forward from your heart's upper chamber ...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-202",
    "label": "Infective Endocarditis",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Infective Endocarditis?",
    "healthBody": "Circulation (AHA Endocarditis Guidelines) & NEJM (POET)",
    "description": "Infective endocarditis is a serious infection of the smooth inner lining and valves of your heart. Bacteria or...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-203",
    "label": "Acute Pericarditis",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Pericarditis?",
    "healthBody": "NEJM (ICAP Trial) & ESC Guidelines",
    "description": "Pericarditis is an inflammation of the pericardium, the protective fluid-filled double-layered sac that surrou...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-204",
    "label": "Cardiac Tamponade",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cardiac Tamponade?",
    "healthBody": "ESC Guidelines on Pericardial Diseases & JAMA Rational Clinical Exam",
    "description": "Cardiac tamponade is a medical emergency where fluid rapidly builds up inside the sac wrapped around your hear...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-205",
    "label": "Ventricular Tachycardia (VT)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ventricular Tachycardia (VT)?",
    "healthBody": "NEJM (VANISH Trial) & AHA/ACC/HRS Guidelines",
    "description": "Ventricular tachycardia (VT) is a dangerously fast heartbeat that starts in the bottom pumping chambers (ventr...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-206",
    "label": "Supraventricular Tachycardia (SVT)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Supraventricular Tachycardia (SVT)?",
    "healthBody": "The Lancet (REVERT Trial) & ACC/AHA/HRS Guidelines",
    "description": "Supraventricular tachycardia (SVT) is a condition where an extra electrical short-circuit in the top chambers ...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-207",
    "label": "Thoracic Aortic Aneurysm",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Thoracic Aortic Aneurysm?",
    "healthBody": "JACC / Circulation (AHA/ACC Aortic Guidelines)",
    "description": "A thoracic aortic aneurysm is a bulge or ballooning in the aorta, the large main highway artery carrying oxyge...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-208",
    "label": "Abdominal Aortic Aneurysm (AAA)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Abdominal Aortic Aneurysm (AAA)?",
    "healthBody": "The Lancet (EVAR trial 1 & 2) & USPSTF",
    "description": "An abdominal aortic aneurysm (AAA) is a balloon-like swelling in the lower part of the aorta, the main blood v...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-209",
    "label": "Raynaud's Phenomenon",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Raynaud's Phenomenon?",
    "healthBody": "Cochrane Database of Systematic Reviews & ACR",
    "description": "Raynaud's phenomenon is an over-reactive response in the small blood vessels of your fingers and toes when exp...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-210",
    "label": "Buerger's Disease (Thromboangiitis Obliterans)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Buerger's Disease (Thromboangiitis Obliterans)?",
    "healthBody": "Circulation (AHA Vascular Guidelines) & European Consensus",
    "description": "Buerger's disease is an inflammatory disease that causes swelling, inflammation, and tiny blood clots in the b...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-211",
    "label": "Cor Pulmonale",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cor Pulmonale?",
    "healthBody": "CHEST & European Respiratory Society (ERS/ESC)",
    "description": "Cor pulmonale is heart enlargement and weakness on the right side of your heart caused by chronic lung disease...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-212",
    "label": "Bronchiectasis (Non-Cystic Fibrosis)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bronchiectasis (Non-Cystic Fibrosis)?",
    "healthBody": "European Respiratory Journal (ERS) & Thorax (BTS)",
    "description": "Bronchiectasis is a chronic lung condition where the airways (bronchial tubes) become abnormally widened, stre...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-213",
    "label": "Spontaneous Pneumothorax",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Spontaneous Pneumothorax?",
    "healthBody": "NEJM (PSP Trial) & British Thoracic Society (BTS)",
    "description": "A spontaneous pneumothorax is a collapsed lung that occurs suddenly without any injury. A tiny air blister (bl...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-214",
    "label": "Pleural Effusion (Exudative vs Transudative)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pleural Effusion (Exudative vs Transudative)?",
    "healthBody": "Thorax (British Thoracic Society) & Light's Criteria Meta-Analysis",
    "description": "A pleural effusion is an abnormal buildup of extra fluid in the space between your lung and the chest wall (th...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-215",
    "label": "Silicosis (Occupational Pneumoconiosis)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Silicosis (Occupational Pneumoconiosis)?",
    "healthBody": "WHO / International Labour Organization (ILO) & ATS",
    "description": "Silicosis is a chronic, permanent lung condition caused by breathing in tiny, invisible specks of mineral dust...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-216",
    "label": "Asbestosis & Pleural Plaques",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Asbestosis & Pleural Plaques?",
    "healthBody": "American Thoracic Society (ATS) & Lancet Oncology",
    "description": "Asbestosis is long-term scarring and inflammation of the lungs caused by breathing in asbestos fibers, a heat-...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-217",
    "label": "Hypersensitivity Pneumonitis",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypersensitivity Pneumonitis?",
    "healthBody": "American Thoracic Society & European Respiratory Society",
    "description": "Hypersensitivity pneumonitis is an allergic reaction deep inside the air sacs of your lungs triggered by breat...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-218",
    "label": "Pulmonary & Systemic Sarcoidosis",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pulmonary & Systemic Sarcoidosis?",
    "healthBody": "ATS / ERS Sarcoidosis Guidelines & NEJM",
    "description": "Sarcoidosis is an inflammatory disease where your immune system clusters together into tiny microscopic clumps...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-219",
    "label": "Cryptogenic Organizing Pneumonia (COP)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cryptogenic Organizing Pneumonia (COP)?",
    "healthBody": "American Thoracic Society & European Respiratory Society",
    "description": "Cryptogenic organizing pneumonia (COP) is a non-infectious inflammatory lung condition where plugs of healing ...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-220",
    "label": "Pulmonary Arteriovenous Malformation (PAVM)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pulmonary Arteriovenous Malformation (PAVM)?",
    "healthBody": "Thorax (British Thoracic Society) & JACC",
    "description": "A pulmonary arteriovenous malformation (PAVM) is an abnormal direct tangle between a blood vessel carrying blo...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-221",
    "label": "Barrett's Esophagus",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Barrett's Esophagus?",
    "healthBody": "NEJM (AIM Dysplasia Trial) & ACG Guidelines",
    "description": "Barrett's esophagus is a condition where chronic acid reflux from the stomach damages the lower lining of your...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-222",
    "label": "Achalasia",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Achalasia?",
    "healthBody": "NEJM (POEM vs LHM) & ACG Guidelines",
    "description": "Achalasia is a rare swallowing disorder where the nerves in your food pipe (esophagus) become damaged and stop...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-223",
    "label": "Eosinophilic Esophagitis (EoE)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Eosinophilic Esophagitis (EoE)?",
    "healthBody": "NEJM (Dupilumab EoE Trial) & ACG/AGA Guidelines",
    "description": "Eosinophilic esophagitis (EoE) is an allergic inflammatory condition of your food pipe (esophagus). Certain fo...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-224",
    "label": "Gastroparesis (Diabetic & Idiopathic)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gastroparesis (Diabetic & Idiopathic)?",
    "healthBody": "American College of Gastroenterology (ACG) Guidelines",
    "description": "Gastroparesis is a condition where the muscles in your stomach work too slowly or stop squeezing altogether, d...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-225",
    "label": "Zollinger-Ellison Syndrome (Gastrinoma)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Zollinger-Ellison Syndrome (Gastrinoma)?",
    "healthBody": "National Comprehensive Cancer Network (NCCN) & Lancet",
    "description": "Zollinger-Ellison syndrome is a rare digestive disorder where tiny tumors called gastrinomas form in your panc...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-226",
    "label": "Microscopic Colitis (Collagenous & Lymphocytic)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Microscopic Colitis (Collagenous & Lymphocytic)?",
    "healthBody": "Cochrane Database of Systematic Reviews & AGA Guidelines",
    "description": "Microscopic colitis is an inflammatory bowel disorder that causes frequent, watery, non-bloody diarrhea, espec...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-227",
    "label": "Short Bowel Syndrome (Intestinal Failure)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Short Bowel Syndrome (Intestinal Failure)?",
    "healthBody": "The Lancet (STEPS Trial) & ASPEN Guidelines",
    "description": "Short bowel syndrome occurs when you are missing a large portion of your small intestine (usually after surger...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-228",
    "label": "Small Intestinal Bacterial Overgrowth (SIBO)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Small Intestinal Bacterial Overgrowth (SIBO)?",
    "healthBody": "NEJM (TARGET 1 & 2) & ACG SIBO Clinical Guideline",
    "description": "Small intestinal bacterial overgrowth (SIBO) occurs when bacteria that normally live harmlessly in your large ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-229",
    "label": "Autoimmune Hepatitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Autoimmune Hepatitis?",
    "healthBody": "AASLD Guidelines & Journal of Hepatology",
    "description": "Autoimmune hepatitis is a chronic disease where your body's immune defense system mistakenly identifies your o...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-230",
    "label": "Primary Biliary Cholangitis (PBC)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Biliary Cholangitis (PBC)?",
    "healthBody": "NEJM (POISE Trial) & AASLD Practice Guidance",
    "description": "Primary biliary cholangitis (PBC) is an autoimmune condition where your immune system slowly attacks and destr...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-231",
    "label": "Primary Sclerosing Cholangitis (PSC)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Sclerosing Cholangitis (PSC)?",
    "healthBody": "AASLD Practice Guidelines & The Lancet",
    "description": "Primary sclerosing cholangitis (PSC) is an inflammatory disease that causes scarring and narrowing in the medi...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-232",
    "label": "Wilson's Disease (Hepatolenticular Degeneration)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Wilson's Disease (Hepatolenticular Degeneration)?",
    "healthBody": "AASLD Practice Guidelines & European Association for the Study of the Liver (EASL)",
    "description": "Wilson's disease is an inherited genetic condition where your body cannot get rid of excess copper from the fo...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-233",
    "label": "Hereditary Hemochromatosis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hereditary Hemochromatosis?",
    "healthBody": "AASLD Guidelines & New England Journal of Medicine",
    "description": "Hereditary hemochromatosis is a genetic 'iron overload' disorder where your digestive system absorbs far more ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-234",
    "label": "Hepatorenal Syndrome (HRS-AKI)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hepatorenal Syndrome (HRS-AKI)?",
    "healthBody": "NEJM (CONFIRM Trial) & AASLD Practice Guidance",
    "description": "Hepatorenal syndrome is a severe medical emergency where the kidneys suddenly stop functioning properly becaus...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-235",
    "label": "Hepatic Encephalopathy",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hepatic Encephalopathy?",
    "healthBody": "NEJM (Rifaximin HE Trial) & AASLD/EASL Guidelines",
    "description": "Hepatic encephalopathy is a decline in brain function that happens when your liver is too damaged to filter ou...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-236",
    "label": "Chronic Pancreatitis",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Pancreatitis?",
    "healthBody": "American College of Gastroenterology (ACG) Guidelines",
    "description": "Chronic pancreatitis is long-term, permanent inflammation and scarring of your pancreas, the organ tucked behi...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-237",
    "label": "Pancreatic Exocrine Insufficiency (PEI)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pancreatic Exocrine Insufficiency (PEI)?",
    "healthBody": "Cochrane Database of Systematic Reviews & United European Gastroenterology (UEG)",
    "description": "Pancreatic exocrine insufficiency (PEI) means your pancreas does not produce enough digestive enzymes to break...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-238",
    "label": "Cushing's Syndrome & Disease",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cushing's Syndrome & Disease?",
    "healthBody": "Endocrine Society & NEJM",
    "description": "Cushing's syndrome is a hormone disorder caused by having too much cortisol (the body's primary stress hormone...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-239",
    "label": "Primary Adrenal Insufficiency (Addison's Disease)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Adrenal Insufficiency (Addison's Disease)?",
    "healthBody": "Endocrine Society & Lancet Diabetes & Endocrinology",
    "description": "Addison's disease is an autoimmune condition where your adrenal glands (tiny hormone factories sitting on top ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-240",
    "label": "Primary Hyperaldosteronism (Conn's Syndrome)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Hyperaldosteronism (Conn's Syndrome)?",
    "healthBody": "Endocrine Society & The Lancet Diabetes & Endocrinology",
    "description": "Primary hyperaldosteronism (Conn's syndrome) is a hormonal cause of severe high blood pressure. Your adrenal g...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-241",
    "label": "Amyotrophic Lateral Sclerosis (ALS)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Amyotrophic Lateral Sclerosis (ALS)?",
    "healthBody": "NEJM & The Lancet Neurology (Edaravone & Riluzole)",
    "description": "Amyotrophic lateral sclerosis (ALS, often called Lou Gehrig's disease) is a progressive nervous system disease...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-242",
    "label": "Huntington's Disease",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Huntington's Disease?",
    "healthBody": "JAMA (First-HD Trial) & NEJM",
    "description": "Huntington's disease is a genetic brain disorder caused by an inherited error in a single gene. Over time, it ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-243",
    "label": "Normal Pressure Hydrocephalus (NPH)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Normal Pressure Hydrocephalus (NPH)?",
    "healthBody": "NEJM & Journal of Neurosurgery (INPH Guidelines)",
    "description": "Normal pressure hydrocephalus (NPH) is a condition where normal fluid (cerebrospinal fluid) builds up inside t...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-244",
    "label": "Guillain-Barré Syndrome (GBS)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Guillain-Barré Syndrome (GBS)?",
    "healthBody": "Cochrane Database of Systematic Reviews & The Lancet Neurology",
    "description": "Guillain-Barré syndrome (GBS) is a rare neurological disorder where your body's immune system, usually trigger...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-245",
    "label": "Myasthenia Gravis",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Myasthenia Gravis?",
    "healthBody": "NEJM (MGTX Trial) & REGAIN Trial",
    "description": "Myasthenia gravis is an autoimmune disorder where your immune system mistakenly blocks or destroys the recepto...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-246",
    "label": "Trigeminal Neuralgia",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Trigeminal Neuralgia?",
    "healthBody": "American Academy of Neurology (AAN) & European Academy of Neurology (EAN)",
    "description": "Trigeminal neuralgia is an intense facial nerve pain condition often described as one of the most painful cond...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-247",
    "label": "Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)?",
    "healthBody": "JAMA (NORDIC Trial) & Cochrane Database",
    "description": "Idiopathic intracranial hypertension (pseudotumor cerebri) is a condition where high pressure builds up inside...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-248",
    "label": "Cluster Headache",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cluster Headache?",
    "healthBody": "JAMA & The Lancet Neurology (High-Flow O2 & Verapamil)",
    "description": "Cluster headaches are excruciatingly painful headaches known as 'suicide headaches' due to their extreme sever...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-249",
    "label": "Transient Ischemic Attack (TIA)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Transient Ischemic Attack (TIA)?",
    "healthBody": "NEJM (CHANCE & POINT Trials) & AHA/ASA Guidelines",
    "description": "A transient ischemic attack (TIA), often called a 'warning stroke' or 'mini-stroke', occurs when blood flow to...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-250",
    "label": "Vascular Dementia",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vascular Dementia?",
    "healthBody": "Stroke (AHA/ASA Scientific Statement) & Cochrane",
    "description": "Vascular dementia is memory and thinking loss caused by reduced blood flow to the brain, often following multi...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-251",
    "label": "Dementia with Lewy Bodies (DLB)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dementia with Lewy Bodies (DLB)?",
    "healthBody": "Neurology (DLB Consortium Guidelines)",
    "description": "Dementia with Lewy bodies (DLB) is a progressive brain condition caused by abnormal microscopic protein deposi...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-252",
    "label": "Frontotemporal Dementia (FTD)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Frontotemporal Dementia (FTD)?",
    "healthBody": "Brain & The Lancet Neurology (FTDC Criteria)",
    "description": "Frontotemporal dementia (FTD) is a group of brain disorders caused by nerve cell damage and shrinking in the f...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-253",
    "label": "Obsessive-Compulsive Disorder (OCD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Obsessive-Compulsive Disorder (OCD)?",
    "healthBody": "Cochrane Database of Systematic Reviews & American Psychiatric Association",
    "description": "Obsessive-compulsive disorder (OCD) is a mental health condition driven by a cycle of obsessions and compulsio...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-254",
    "label": "Panic Disorder & Agoraphobia",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Panic Disorder & Agoraphobia?",
    "healthBody": "Cochrane Database of Systematic Reviews & Lancet Psychiatry",
    "description": "Panic disorder is an anxiety condition where you experience sudden, terrifying surges of overwhelming fear and...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-255",
    "label": "Borderline Personality Disorder (BPD)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Borderline Personality Disorder (BPD)?",
    "healthBody": "Cochrane Database of Systematic Reviews & JAMA Psychiatry",
    "description": "Borderline personality disorder (BPD) is a mental health condition characterized by intense emotional sensitiv...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-256",
    "label": "Meniere's Disease (Endolymphatic Hydrops)",
    "category": "Otolaryngology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Meniere's Disease (Endolymphatic Hydrops)?",
    "healthBody": "Otolaryngology-Head and Neck Surgery (AAO-HNS Guidelines)",
    "description": "Meniere's disease is an inner ear disorder caused by excess fluid pressure building up inside the hearing and ...",
    "icon": "👂"
  },
  {
    "id": "sug-doc-card-257",
    "label": "Sudden Sensorineural Hearing Loss (SSNHL)",
    "category": "Otolaryngology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sudden Sensorineural Hearing Loss (SSNHL)?",
    "healthBody": "Otolaryngology-Head and Neck Surgery & JAMA Otolaryngology",
    "description": "Sudden sensorineural hearing loss (often called sudden deafness) is an ear emergency where you suddenly wake u...",
    "icon": "👂"
  },
  {
    "id": "sug-doc-card-258",
    "label": "Anterior Ischemic Optic Neuropathy (AION)",
    "category": "Ophthalmology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Anterior Ischemic Optic Neuropathy (AION)?",
    "healthBody": "American Academy of Ophthalmology (AAO) & Ophthalmology",
    "description": "Anterior ischemic optic neuropathy (AION) is often described as a 'stroke of the optic nerve'. The small blood...",
    "icon": "👁️"
  },
  {
    "id": "sug-doc-card-259",
    "label": "Central Retinal Artery Occlusion (CRAO)",
    "category": "Ophthalmology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Central Retinal Artery Occlusion (CRAO)?",
    "healthBody": "Stroke (AHA Scientific Statement on CRAO) & Ophthalmology",
    "description": "Central retinal artery occlusion (CRAO) is an eye stroke. Just like an ischemic stroke in the brain, a small t...",
    "icon": "👁️"
  },
  {
    "id": "sug-doc-card-260",
    "label": "Rhegmatogenous Retinal Detachment",
    "category": "Ophthalmology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Rhegmatogenous Retinal Detachment?",
    "healthBody": "Ophthalmology (AAO Preferred Practice Pattern) & Cochrane",
    "description": "A retinal detachment occurs when the thin, light-sensitive tissue at the back of your eye (the retina) peels a...",
    "icon": "👁️"
  },
  {
    "id": "sug-doc-card-261",
    "label": "IgA Nephropathy (Berger's Disease)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for IgA Nephropathy (Berger's Disease)?",
    "healthBody": "The Lancet (TESTING Trial) & NEJM (NefIgArd)",
    "description": "IgA nephropathy (Berger's disease) is an autoimmune kidney disease where an abnormal form of an antibody calle...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-262",
    "label": "Membranous Nephropathy",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Membranous Nephropathy?",
    "healthBody": "NEJM (MENTOR Trial) & KDIGO Guidelines",
    "description": "Membranous nephropathy is an autoimmune kidney disease where your body produces antibodies (most commonly anti...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-263",
    "label": "Minimal Change Disease",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Minimal Change Disease?",
    "healthBody": "Kidney International (KDIGO Glomerular Diseases)",
    "description": "Minimal change disease is a kidney condition that causes your kidneys to suddenly leak massive amounts of prot...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-264",
    "label": "Focal Segmental Glomerulosclerosis (FSGS)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Focal Segmental Glomerulosclerosis (FSGS)?",
    "healthBody": "The Lancet (DUET & DUPLEX Trials) & KDIGO",
    "description": "Focal segmental glomerulosclerosis (FSGS) is a kidney disease that causes scarring in the microscopic filters ...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-265",
    "label": "Autosomal Dominant Polycystic Kidney Disease (ADPKD)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Autosomal Dominant Polycystic Kidney Disease (ADPKD)?",
    "healthBody": "NEJM (TEMPO 3:4 & REPRISE Trials) & KDIGO",
    "description": "Autosomal dominant polycystic kidney disease (ADPKD) is an inherited genetic condition that causes hundreds of...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-266",
    "label": "Lupus Nephritis",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Lupus Nephritis?",
    "healthBody": "NEJM (BLISS-LN Trial) & The Lancet (AURORA Trial)",
    "description": "Lupus nephritis is kidney inflammation caused by systemic lupus erythematosus (SLE), an autoimmune disease. In...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-267",
    "label": "ANCA-Associated Vasculitis (Granulomatosis with Polyangiitis)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for ANCA-Associated Vasculitis (Granulomatosis with Polyangiitis)?",
    "healthBody": "NEJM (ADVOCATE Trial & RAVE Trial) & ACR Guidelines",
    "description": "ANCA-associated vasculitis (such as Granulomatosis with Polyangiitis) is an autoimmune disorder where your imm...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-268",
    "label": "Ankylosing Spondylitis (Axial Spondyloarthritis)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ankylosing Spondylitis (Axial Spondyloarthritis)?",
    "healthBody": "NEJM (MEASURE 1 & 2 Trials) & ACR/SAA Guidelines",
    "description": "Ankylosing spondylitis is an inflammatory arthritis that primarily attacks the joints of your spine and pelvis...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-269",
    "label": "Psoriatic Arthritis",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Psoriatic Arthritis?",
    "healthBody": "The Lancet (DISCOVER-1 & 2 Trials) & ACR/NPF Guidelines",
    "description": "Psoriatic arthritis is an autoimmune condition that causes joint pain, swelling, and stiffness in people who h...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-270",
    "label": "Systemic Sclerosis (Scleroderma)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Systemic Sclerosis (Scleroderma)?",
    "healthBody": "NEJM (SENSCIS Trial) & ACR/EULAR Recommendations",
    "description": "Systemic sclerosis (scleroderma) is an autoimmune disorder that causes your body to produce far too much colla...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-271",
    "label": "Sjögren's Syndrome",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sjögren's Syndrome?",
    "healthBody": "Annals of the Rheumatic Diseases & Arthritis & Rheumatology",
    "description": "Sjögren's syndrome is an autoimmune disease where your body's immune system attacks its own moisture-producing...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-272",
    "label": "Dermatomyositis & Polymyositis",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dermatomyositis & Polymyositis?",
    "healthBody": "NEJM (ProDERM Trial) & EULAR/ACR Guidelines",
    "description": "Dermatomyositis is a rare inflammatory disease marked by muscle weakness and distinctive skin rashes. Your imm...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-273",
    "label": "Behçet's Disease",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Behçet's Disease?",
    "healthBody": "NEJM (RELIEF Trial) & EULAR Recommendations",
    "description": "Behçet's disease is a rare autoimmune disorder that causes inflammation in blood vessels throughout your body....",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-274",
    "label": "Polyarteritis Nodosa (PAN)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polyarteritis Nodosa (PAN)?",
    "healthBody": "Arthritis & Rheumatology (ACR Guideline) & Medicine",
    "description": "Polyarteritis nodosa (PAN) is a serious autoimmune condition where your immune system attacks and inflames med...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-275",
    "label": "Henoch-Schönlein Purpura (IgA Vasculitis)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Henoch-Schönlein Purpura (IgA Vasculitis)?",
    "healthBody": "Annals of the Rheumatic Diseases & Cochrane Review",
    "description": "Henoch-Schönlein purpura (IgA vasculitis) is an illness that causes tiny blood vessels in the skin, joints, in...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-276",
    "label": "Ehlers-Danlos Syndrome (Hypermobile & Vascular)",
    "category": "Genetics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ehlers-Danlos Syndrome (Hypermobile & Vascular)?",
    "healthBody": "The Lancet (BBEST Trial) & International EDS Consortium",
    "description": "Ehlers-Danlos syndrome (EDS) is a group of inherited genetic conditions that affect collagen, the fibrous 'glu...",
    "icon": "🧬"
  },
  {
    "id": "sug-doc-card-277",
    "label": "Complex Regional Pain Syndrome (CRPS)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Complex Regional Pain Syndrome (CRPS)?",
    "healthBody": "Pain (IASP Budapest Criteria) & Cochrane Reviews",
    "description": "Complex regional pain syndrome (CRPS) is a severe, chronic nerve pain condition that usually develops in an ar...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-278",
    "label": "Cervical Radiculopathy (Cervical Spondylosis)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cervical Radiculopathy (Cervical Spondylosis)?",
    "healthBody": "Spine Journal (NASS Guidelines) & Cochrane Database",
    "description": "Cervical radiculopathy, commonly called a 'pinched nerve in the neck', occurs when a nerve root leaving your s...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-279",
    "label": "Adhesive Capsulitis (Frozen Shoulder)",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Adhesive Capsulitis (Frozen Shoulder)?",
    "healthBody": "Cochrane Database of Systematic Reviews & BMJ",
    "description": "Adhesive capsulitis, commonly known as 'frozen shoulder', is a condition where the strong connective tissue ca...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-280",
    "label": "Greater Trochanteric Pain Syndrome (Trochanteric Bursitis)",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Greater Trochanteric Pain Syndrome (Trochanteric Bursitis)?",
    "healthBody": "British Journal of Sports Medicine (BJSM) & Cochrane",
    "description": "Greater trochanteric pain syndrome (often called trochanteric bursitis) is a condition that causes sharp or ac...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-281",
    "label": "Immune Thrombocytopenia (ITP)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Immune Thrombocytopenia (ITP)?",
    "healthBody": "The Lancet (RAISE Trial) & ASH Guidelines",
    "description": "Immune thrombocytopenia (ITP) is an autoimmune blood condition where your immune system mistakenly destroys yo...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-282",
    "label": "Thrombotic Thrombocytopenic Purpura (TTP)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Thrombotic Thrombocytopenic Purpura (TTP)?",
    "healthBody": "NEJM (HERCULES Trial) & ISTH Guidelines",
    "description": "Thrombotic thrombocytopenic purpura (TTP) is a critical, life-threatening blood emergency where your immune sy...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-283",
    "label": "Atypical Hemolytic Uremic Syndrome (aHUS)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Atypical Hemolytic Uremic Syndrome (aHUS)?",
    "healthBody": "NEJM (Eculizumab in aHUS) & KDIGO Guidelines",
    "description": "Atypical hemolytic uremic syndrome (aHUS) is a rare, severe blood and kidney disorder caused by a genetic malf...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-284",
    "label": "Polycythemia Vera",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polycythemia Vera?",
    "healthBody": "NEJM (CYTO-PV Trial & RESPONSE Trial) & WHO/NCCN",
    "description": "Polycythemia vera is a rare, slow-growing blood cancer where your bone marrow produces far too many red blood ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-285",
    "label": "Essential Thrombocythemia (ET)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Essential Thrombocythemia (ET)?",
    "healthBody": "NEJM (PT1 Trial) & WHO/NCCN Guidelines",
    "description": "Essential thrombocythemia (ET) is a rare blood disorder where your bone marrow produces too many platelets. Pl...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-286",
    "label": "Myelodysplastic Syndromes (MDS)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Myelodysplastic Syndromes (MDS)?",
    "healthBody": "NEJM & The Lancet (COMMANDS Trial & AZA-001)",
    "description": "Myelodysplastic syndromes (MDS) are a group of bone marrow disorders sometimes described as 'bone marrow failu...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-287",
    "label": "Chronic Lymphocytic Leukemia (CLL)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Lymphocytic Leukemia (CLL)?",
    "healthBody": "NEJM (ELEVATE-TN & CLL14 Trials) & NCCN Guidelines",
    "description": "Chronic lymphocytic leukemia (CLL) is a slow-growing cancer of the white blood cells (lymphocytes). The bone m...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-288",
    "label": "Multiple Myeloma",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Multiple Myeloma?",
    "healthBody": "NEJM (GRIFFIN & MAIA Trials) & IMWG Guidelines",
    "description": "Multiple myeloma is a type of blood cancer that develops in plasma cells, a type of white blood cell in your b...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-289",
    "label": "Hodgkin Lymphoma",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hodgkin Lymphoma?",
    "healthBody": "NEJM (ECHELON-1 Trial) & NCCN Guidelines",
    "description": "Hodgkin lymphoma is a cancer of the lymphatic system, which is part of your body's germ-fighting immune networ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-290",
    "label": "Diffuse Large B-Cell Lymphoma (DLBCL)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diffuse Large B-Cell Lymphoma (DLBCL)?",
    "healthBody": "NEJM (POLARIX Trial & ZUMA-7) & NCCN Guidelines",
    "description": "Diffuse large B-cell lymphoma (DLBCL) is a fast-growing, aggressive cancer of the lymphatic system. B-cells, a...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-291",
    "label": "Malignant Cutaneous Melanoma",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Malignant Cutaneous Melanoma?",
    "healthBody": "NEJM (CheckMate 067 & KEYNOTE-006) & NCCN Guidelines",
    "description": "Malignant melanoma is the most serious and dangerous type of skin cancer. It develops in the melanocyte cells ...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-292",
    "label": "Basal Cell & Cutaneous Squamous Cell Carcinoma",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Basal Cell & Cutaneous Squamous Cell Carcinoma?",
    "healthBody": "NEJM (Cemiplimab Trial & Vismodegib) & NCCN Guidelines",
    "description": "Basal cell carcinoma and squamous cell carcinoma are the two most common types of skin cancer. They develop on...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-293",
    "label": "Hidradenitis Suppurativa",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hidradenitis Suppurativa?",
    "healthBody": "NEJM (PIONEER Trials) & The Lancet (SUNSHINE & SUNSPOT)",
    "description": "Hidradenitis suppurativa (HS) is a chronic, painful, inflammatory skin condition that causes deep, swollen, te...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-294",
    "label": "Bullous Pemphigoid",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bullous Pemphigoid?",
    "healthBody": "NEJM (Topical Clobetasol Trial) & The Lancet (Ritux 3)",
    "description": "Bullous pemphigoid is an autoimmune skin condition that primarily affects older adults. Your body's immune sys...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-295",
    "label": "Vitiligo",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vitiligo?",
    "healthBody": "NEJM (TRuE-V1 & TRuE-V2 Trials) & Vitiligo Guidelines",
    "description": "Vitiligo is an autoimmune skin condition where your immune system mistakenly attacks and destroys your body's ...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-296",
    "label": "Alopecia Areata",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Alopecia Areata?",
    "healthBody": "NEJM (BRAVE-AA1 & BRAVE-AA2) & Lancet (ALLEGRO)",
    "description": "Alopecia areata is an autoimmune condition where your immune system mistakenly targets and attacks your hair f...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-297",
    "label": "Herpes Zoster (Shingles) & Postherpetic Neuralgia",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Herpes Zoster (Shingles) & Postherpetic Neuralgia?",
    "healthBody": "NEJM (ZOE-50 & ZOE-70 Trials) & CDC/ACIP Guidelines",
    "description": "Herpes zoster (commonly called shingles) is a painful blistering rash caused by the chickenpox virus (varicell...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-298",
    "label": "Infectious Mononucleosis (Epstein-Barr Virus)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Infectious Mononucleosis (Epstein-Barr Virus)?",
    "healthBody": "CDC Infectious Disease Guidance & JAMA Rational Clinical Exam",
    "description": "Infectious mononucleosis (often called 'mono' or the 'kissing disease') is a common viral infection caused by ...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-299",
    "label": "Acute & Chronic Osteomyelitis",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute & Chronic Osteomyelitis?",
    "healthBody": "NEJM (OVIVA Trial) & IDSA Practice Guidelines",
    "description": "Osteomyelitis is a severe bacterial infection deep inside a bone. Bacteria can reach the bone through the bloo...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-300",
    "label": "Recurrent Clostridioides difficile Infection",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Recurrent Clostridioides difficile Infection?",
    "healthBody": "NEJM (PUNCH CD3 Trial & MODIFY I/II) & IDSA/SHEA Guidelines",
    "description": "Recurrent Clostridioides difficile (C. diff) infection is a bacterial bowel infection that causes severe, wate...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-301",
    "label": "Orthostatic Hypotension (Low Blood Pressure)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Orthostatic Hypotension (Low Blood Pressure)?",
    "healthBody": "AHA/ACC & Neurological Sciences",
    "description": "Low blood pressure when standing is like low water pressure in a garden hose. When you stand up, gravity pulls...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-302",
    "label": "Hypoglycemia (Low Blood Sugar)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypoglycemia (Low Blood Sugar)?",
    "healthBody": "American Diabetes Association (ADA)",
    "description": "Low blood sugar is like a car engine running out of gasoline. Your brain and nerves rely entirely on sugar (gl...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-303",
    "label": "Sinus Bradycardia & Conduction Disease",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sinus Bradycardia & Conduction Disease?",
    "healthBody": "Circulation & Heart Rhythm Society",
    "description": "The heart has its own natural battery and electrical spark plug called the sinus node. Bradycardia means this ...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-304",
    "label": "Complete Atrioventricular Heart Block (Third-Degree AV Block)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Complete Atrioventricular Heart Block (Third-Degree AV Block)?",
    "healthBody": "JACC & Circulation",
    "description": "The heart has upper chambers (atria) that collect blood and lower pumping chambers (ventricles) that send it t...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-305",
    "label": "Vasovagal Syncope (Neurocardiogenic Syncope)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vasovagal Syncope (Neurocardiogenic Syncope)?",
    "healthBody": "JAMA & Circulation (POST II)",
    "description": "Vasovagal syncope is a temporary reflex reaction where your nervous system overreacts to a trigger like prolon...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-306",
    "label": "Cardiogenic Shock & Acute Low Cardiac Output",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cardiogenic Shock & Acute Low Cardiac Output?",
    "healthBody": "NEJM (SHOCK Trial) & ACC/AHA",
    "description": "Cardiogenic shock is a critical emergency where the heart muscle is so severely damaged (usually from a massiv...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-307",
    "label": "Diabetic Ketoacidosis (DKA)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diabetic Ketoacidosis (DKA)?",
    "healthBody": "ADA & Endocrine Society",
    "description": "Diabetic ketoacidosis happens when the body does not have enough insulin to move sugar into cells for energy. ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-308",
    "label": "Hyperosmolar Hyperglycemic State (HHS)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hyperosmolar Hyperglycemic State (HHS)?",
    "healthBody": "ADA & Lancet Diabetes & Endocrinology",
    "description": "Hyperosmolar Hyperglycemic State is an extreme emergency seen in type 2 diabetes where blood sugar climbs sky-...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-309",
    "label": "Acute Productive (Wet) Cough",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Productive (Wet) Cough?",
    "healthBody": "CHEST & Cochrane Database",
    "description": "A wet or productive cough is your lungs' natural cleaning reflex. When bacteria, viruses, or irritants cause i...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-310",
    "label": "Subacute & Chronic Dry (Non-Productive) Cough",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Subacute & Chronic Dry (Non-Productive) Cough?",
    "healthBody": "CHEST & British Thoracic Society (BTS)",
    "description": "A dry cough produces no mucus or phlegm. It feels like an annoying, relentless tickle in your throat. It is of...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-311",
    "label": "Cardiogenic Pulmonary Edema (Cardiac Asthma)",
    "category": "Cardiovascular",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cardiogenic Pulmonary Edema (Cardiac Asthma)?",
    "healthBody": "Lancet & European Heart Journal (3CPO Trial)",
    "description": "Cardiogenic pulmonary edema (often called 'cardiac asthma') happens when the heart's left pump fails to pump b...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-312",
    "label": "Bronchial Asthma (Airway Hyperresponsiveness)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bronchial Asthma (Airway Hyperresponsiveness)?",
    "healthBody": "Global Initiative for Asthma (GINA) & NEJM (SYGMA 1 & 2)",
    "description": "Bronchial asthma is chronic inflammation in the air tubes of your lungs. When exposed to a trigger (like cold ...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-313",
    "label": "Benign Paroxysmal Positional Vertigo (BPPV)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Benign Paroxysmal Positional Vertigo (BPPV)?",
    "healthBody": "Otolaryngology-Head and Neck Surgery & Cochrane",
    "description": "BPPV is a mechanical problem in your inner ear balance system. Your inner ear contains microscopic calcium cry...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-314",
    "label": "Meniere's Disease (Endolymphatic Hydrops)",
    "category": "Otolaryngology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Meniere's Disease (Endolymphatic Hydrops)?",
    "healthBody": "Otolaryngology-Head and Neck Surgery & Cochrane",
    "description": "Meniere's disease is caused by excess fluid pressure building up inside the hearing and balance chambers of yo...",
    "icon": "👂"
  },
  {
    "id": "sug-doc-card-315",
    "label": "Vestibular Neuritis (Acute Peripheral Vestibulopathy)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vestibular Neuritis (Acute Peripheral Vestibulopathy)?",
    "healthBody": "NEJM & Neurology",
    "description": "Vestibular neuritis is sudden inflammation and swelling of the vestibular nerve—the primary cable that sends b...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-316",
    "label": "Hypokalemia (Low Potassium)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypokalemia (Low Potassium)?",
    "healthBody": "Kidney International & Circulation",
    "description": "Potassium is an essential mineral and electrolyte that acts like electrical power for your muscles, especially...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-317",
    "label": "Hyponatremia & Syndrome of Inappropriate Antidiuretic Hormone (SIADH)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hyponatremia & Syndrome of Inappropriate Antidiuretic Hormone (SIADH)?",
    "healthBody": "European Journal of Endocrinology & Nephrology Dialysis Transplantation",
    "description": "Hyponatremia means your blood sodium is diluted too thin by excess water. Sodium is the main salt that keeps w...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-318",
    "label": "Hypocalcemia & Tetany",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypocalcemia & Tetany?",
    "healthBody": "Journal of Clinical Endocrinology & Metabolism (JCEM)",
    "description": "Calcium is not just for strong bones—it acts as an electrical stabilizer for all your nerves and muscles. In h...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-319",
    "label": "Hypomagnesemia",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypomagnesemia?",
    "healthBody": "Circulation & American Journal of Kidney Diseases",
    "description": "Magnesium is a vital mineral that acts like a cellular calm-down switch and spark plug helper. It works behind...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-320",
    "label": "Bipolar Depression (Bipolar I & II Depressive Episode)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bipolar Depression (Bipolar I & II Depressive Episode)?",
    "healthBody": "Lancet Psychiatry & American Journal of Psychiatry",
    "description": "Bipolar depression is the low, exhausted phase of bipolar disorder. While it feels just like ordinary depressi...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-321",
    "label": "Hashimoto's Thyroiditis (Autoimmune Hypothyroidism)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hashimoto's Thyroiditis (Autoimmune Hypothyroidism)?",
    "healthBody": "Thyroid & Endocrine Practice",
    "description": "The thyroid gland acts as your body's furnace. In Hashimoto's, the furnace fuel valve is turned down too low, ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-322",
    "label": "Central Diabetes Insipidus (Arginine Vasopressin Deficiency)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Central Diabetes Insipidus (Arginine Vasopressin Deficiency)?",
    "healthBody": "Lancet Diabetes & Endocrinology",
    "description": "A water-loss problem where the brain does not make enough anti-urination hormone, leaving the floodgates open ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-323",
    "label": "Nephrogenic Diabetes Insipidus (Renal AVP Resistance)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Nephrogenic Diabetes Insipidus (Renal AVP Resistance)?",
    "healthBody": "Nature Reviews Nephrology",
    "description": "Your kidneys have broken antennas that cannot hear the brain's hormone telling them to hold onto water, forcin...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-324",
    "label": "Primary Adrenal Insufficiency (Addison's Disease)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Adrenal Insufficiency (Addison's Disease)?",
    "healthBody": "Journal of Clinical Endocrinology & Metabolism",
    "description": "Your adrenal glands cannot produce cortisol (the stress hormone) or aldosterone. Your blood pressure crashes, ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-325",
    "label": "Cushing's Syndrome (Endogenous Hypercortisolemia)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cushing's Syndrome (Endogenous Hypercortisolemia)?",
    "healthBody": "Journal of Clinical Endocrinology & Metabolism",
    "description": "Your body is flooded with way too much cortisol stress hormone, causing rapid weight gain around the face and ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-326",
    "label": "Primary Hypoparathyroidism (Hypocalcemia)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Hypoparathyroidism (Hypocalcemia)?",
    "healthBody": "European Journal of Endocrinology",
    "description": "Tiny parathyroid glands in your neck fail to make hormone, causing blood calcium to drop. You feel tingling ar...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-327",
    "label": "Primary Hyperparathyroidism (Hypercalcemia)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Hyperparathyroidism (Hypercalcemia)?",
    "healthBody": "Journal of Bone and Mineral Research",
    "description": "One overactive parathyroid gland constantly steals calcium from your bones and dumps it into your blood, causi...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-328",
    "label": "Secondary Hyperparathyroidism of CKD",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Secondary Hyperparathyroidism of CKD?",
    "healthBody": "Kidney International",
    "description": "Failing kidneys cannot clear phosphorus. High phosphorus traps calcium, forcing parathyroid glands into hyperd...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-329",
    "label": "Hypopituitarism & Panhypopituitarism",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypopituitarism & Panhypopituitarism?",
    "healthBody": "Journal of Clinical Endocrinology & Metabolism",
    "description": "The pituitary master conductor in your brain goes silent, shutting down thyroid, adrenal, and sex hormone fact...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-330",
    "label": "Acromegaly (Growth Hormone Excess)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acromegaly (Growth Hormone Excess)?",
    "healthBody": "Journal of Clinical Endocrinology & Metabolism",
    "description": "A benign pituitary tumor pumps out excess growth hormone in adulthood. Your shoe and ring sizes steadily grow,...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-331",
    "label": "Severe Accidental Hypothermia (Core Temp <32 C)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Severe Accidental Hypothermia (Core Temp <32 C)?",
    "healthBody": "Resuscitation & Circulation",
    "description": "Your body temperature drops dangerously low from freezing exposure. Heart rate and breathing slow to a crawl, ...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-332",
    "label": "Exertional Heatstroke & Severe Hyperthermia (Core Temp >40 C)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Exertional Heatstroke & Severe Hyperthermia (Core Temp >40 C)?",
    "healthBody": "Wilderness & Environmental Medicine",
    "description": "Your body's cooling system fails completely during extreme heat or exertion. Body temperature spikes over 104 ...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-333",
    "label": "Malignant Hyperthermia (Ryanodine Receptor Toxicity)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Malignant Hyperthermia (Ryanodine Receptor Toxicity)?",
    "healthBody": "Anesthesiology",
    "description": "A rare inherited reaction to anesthesia gases where muscle cell calcium gates stick wide open, causing muscles...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-334",
    "label": "Neuroleptic Malignant Syndrome (NMS)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Neuroleptic Malignant Syndrome (NMS)?",
    "healthBody": "Critical Care Medicine",
    "description": "A severe reaction to psychiatric antipsychotic medications that blocks dopamine receptors. Muscles become stif...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-335",
    "label": "Serotonin Syndrome (Serotonin Toxicity)",
    "category": "Psychiatry",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Serotonin Syndrome (Serotonin Toxicity)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Your brain and nerves get poisoned by way too much serotonin (often from combining two antidepressant or migra...",
    "icon": "🌱"
  },
  {
    "id": "sug-doc-card-336",
    "label": "Tension Pneumothorax (Obstructive Shock Emergency)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Tension Pneumothorax (Obstructive Shock Emergency)?",
    "healthBody": "Journal of Trauma and Acute Care Surgery",
    "description": "A one-way hole in your lung lets air leak out into your chest cavity with every breath, but none can escape. T...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-337",
    "label": "Primary Spontaneous Pneumothorax (PSP)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Spontaneous Pneumothorax (PSP)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A small air bubble (bleb) on the outer tip of your lung pops like a thin balloon, letting air leak into your c...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-338",
    "label": "Acute Massive Pulmonary Embolism with Hemodynamic Collapse",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Massive Pulmonary Embolism with Hemodynamic Collapse?",
    "healthBody": "European Heart Journal & NEJM",
    "description": "A massive blood clot travels from the leg veins and wedges tightly in the main blood pipe leading from your he...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-339",
    "label": "Cardiac Tamponade (Pericardial Fluid Compression)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cardiac Tamponade (Pericardial Fluid Compression)?",
    "healthBody": "European Heart Journal",
    "description": "Fluid, blood, or pus builds up rapidly inside the tough sac surrounding your heart. The fluid squeezes the hea...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-340",
    "label": "Massive Hemoptysis (Bronchial Artery Hemorrhage)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Massive Hemoptysis (Bronchial Artery Hemorrhage)?",
    "healthBody": "Cardiovascular and Interventional Radiology",
    "description": "Coughing up large amounts of pure blood from high-pressure arteries in your lungs (often from bronchiectasis, ...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-341",
    "label": "Acute Ischemic Stroke (LVO / Thrombolytic Candidate)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Ischemic Stroke (LVO / Thrombolytic Candidate)?",
    "healthBody": "Stroke & NEJM",
    "description": "A blood clot clogs an artery supplying blood to your brain, causing sudden facial drooping, arm weakness, and ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-342",
    "label": "Acute Spontaneous Intracerebral Hemorrhage (ICH)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Spontaneous Intracerebral Hemorrhage (ICH)?",
    "healthBody": "Stroke & Lancet",
    "description": "A blood vessel inside your brain bursts open under high pressure, bleeding directly into brain tissue. It crea...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-343",
    "label": "Aneurysmal Subarachnoid Hemorrhage (aSAH)",
    "category": "Neurosurgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Aneurysmal Subarachnoid Hemorrhage (aSAH)?",
    "healthBody": "Stroke & NEJM",
    "description": "A blister-like balloon (aneurysm) on a brain artery bursts, spraying blood into the fluid spaces around your b...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-344",
    "label": "Central Sleep Apnea (Cheyne-Stokes Breathing)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Central Sleep Apnea (Cheyne-Stokes Breathing)?",
    "healthBody": "Journal of Clinical Sleep Medicine",
    "description": "Unlike typical sleep apnea where your throat physically closes off, central sleep apnea happens when your brai...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-345",
    "label": "Acute Angle-Closure Glaucoma",
    "category": "Ophthalmology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Angle-Closure Glaucoma?",
    "healthBody": "Ophthalmology",
    "description": "A sudden plumbing blockage in your eye. The colored iris bulges forward, clamping shut the microscopic drain p...",
    "icon": "👁️"
  },
  {
    "id": "sug-doc-card-346",
    "label": "Transient Ischemic Attack (High ABCD2 Score)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Transient Ischemic Attack (High ABCD2 Score)?",
    "healthBody": "Stroke & NEJM",
    "description": "A transient ischemic attack (often called a 'mini-stroke') is a temporary blockage of a brain artery that clea...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-347",
    "label": "Pseudogout / Calcium Pyrophosphate Deposition (CPPD)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pseudogout / Calcium Pyrophosphate Deposition (CPPD)?",
    "healthBody": "Annals of the Rheumatic Diseases",
    "description": "Pseudogout feels almost identical to regular gout—a swollen, red, hot, excruciatingly painful joint (most comm...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-348",
    "label": "Essential Tremor (Action & Kinetic Tremor)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Essential Tremor (Action & Kinetic Tremor)?",
    "healthBody": "Neurology",
    "description": "Essential tremor is the most common movement disorder. It causes your hands to shake when you try to use them—...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-349",
    "label": "Vascular Dementia (Subcortical Ischemic Stepwise Decline)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vascular Dementia (Subcortical Ischemic Stepwise Decline)?",
    "healthBody": "Stroke & Lancet Neurology",
    "description": "Vascular dementia happens when microscopic silent strokes or clogged small blood vessels starve brain tissue o...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-350",
    "label": "Frontotemporal Dementia (Behavioral Variant FTD / Pick's Disease)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Frontotemporal Dementia (Behavioral Variant FTD / Pick's Disease)?",
    "healthBody": "Brain & Lancet Neurology",
    "description": "Frontotemporal dementia attacks the frontal lobes of the brain—the centers responsible for manners, empathy, j...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-351",
    "label": "Normal Pressure Hydrocephalus (NPH)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Normal Pressure Hydrocephalus (NPH)?",
    "healthBody": "Neurosurgery & Lancet Neurology",
    "description": "Normal pressure hydrocephalus happens when excess spinal fluid slowly builds up in the deep cavities of your b...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-352",
    "label": "Wernicke Encephalopathy (Acute Thiamine Deficiency)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Wernicke Encephalopathy (Acute Thiamine Deficiency)?",
    "healthBody": "European Journal of Neurology",
    "description": "A severe brain emergency caused by total exhaustion of Vitamin B1 (thiamine)—often in people with chronic alco...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-353",
    "label": "Hepatic Encephalopathy (Hyperammonemia & Asterixis)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hepatic Encephalopathy (Hyperammonemia & Asterixis)?",
    "healthBody": "Hepatology",
    "description": "When the liver is severely scarred (cirrhosis), it cannot filter out normal toxins like ammonia produced by in...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-354",
    "label": "Delirium (Acute Brain Failure / Toxic-Metabolic Encephalopathy)",
    "category": "Geriatrics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Delirium (Acute Brain Failure / Toxic-Metabolic Encephalopathy)?",
    "healthBody": "Journal of the American Geriatrics Society",
    "description": "Delirium is sudden, temporary brain confusion caused by an underlying medical sickness (like a urinary infecti...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-355",
    "label": "Central Pontine Myelinolysis (Osmotic Demyelination Syndrome)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Central Pontine Myelinolysis (Osmotic Demyelination Syndrome)?",
    "healthBody": "Lancet Neurology",
    "description": "A severe, preventable brainstem injury that happens when doctors or nurses raise very low blood sodium levels ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-356",
    "label": "Multiple System Atrophy (MSA / Shy-Drager Syndrome)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Multiple System Atrophy (MSA / Shy-Drager Syndrome)?",
    "healthBody": "Movement Disorders",
    "description": "Multiple system atrophy is a rare, aggressive nerve disorder that attacks both your movement controls and your...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-357",
    "label": "Progressive Supranuclear Palsy (Steele-Richardson-Olszewski)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Progressive Supranuclear Palsy (Steele-Richardson-Olszewski)?",
    "healthBody": "Movement Disorders",
    "description": "Progressive supranuclear palsy is an aggressive Parkinson's-like condition. The hallmark signs are an inabilit...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-358",
    "label": "Dementia with Lewy Bodies (DLB)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dementia with Lewy Bodies (DLB)?",
    "healthBody": "Neurology",
    "description": "Lewy body dementia is the second most common form of progressive dementia. It combines memory changes with viv...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-359",
    "label": "Temporal Lobe Epilepsy (Focal Impaired Awareness Seizures)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Temporal Lobe Epilepsy (Focal Impaired Awareness Seizures)?",
    "healthBody": "Epilepsia & Lancet",
    "description": "Temporal lobe epilepsy causes focal seizures that start in your brain's memory and emotion center. They often ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-360",
    "label": "Convulsive Status Epilepticus (Prolonged Seizure Emergency)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Convulsive Status Epilepticus (Prolonged Seizure Emergency)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Status epilepticus is a life-threatening medical emergency where a continuous convulsive seizure lasts for mor...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-361",
    "label": "Acute Colonic Diverticulitis (LLQ Peritonitis)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Colonic Diverticulitis (LLQ Peritonitis)?",
    "healthBody": "Gastroenterology",
    "description": "Small outward pouches in your lower left bowel wall (diverticula) become inflamed or micro-perforated. Unlike ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-362",
    "label": "Acute Appendicitis (McBurney's Point Peritonitis)",
    "category": "General Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Appendicitis (McBurney's Point Peritonitis)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Your appendix—a small finger-shaped pouch hanging from the beginning of your colon on the lower RIGHT side—get...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-363",
    "label": "Crohn's Disease (Transmural Granulomatous Ileocolitis)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Crohn's Disease (Transmural Granulomatous Ileocolitis)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Crohn's disease is chronic inflammation that can strike anywhere along your digestive tract from mouth to colo...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-364",
    "label": "Severe Iron Deficiency Anemia (Microcytic Hypochromic)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Severe Iron Deficiency Anemia (Microcytic Hypochromic)?",
    "healthBody": "Gut",
    "description": "Iron is the primary building brick for hemoglobin, the protein sponge inside red blood cells that carries oxyg...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-365",
    "label": "Polycythemia Vera (JAK2 V617F Erythrocytosis)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polycythemia Vera (JAK2 V617F Erythrocytosis)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Polycythemia vera is the exact opposite of anemia. A genetic switch (JAK2 mutation) inside your bone marrow ge...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-366",
    "label": "Immune Thrombocytopenia (ITP / Autoimmune Purpura)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Immune Thrombocytopenia (ITP / Autoimmune Purpura)?",
    "healthBody": "Blood Advances",
    "description": "Immune thrombocytopenia is a disorder where your immune system mistakenly attacks and destroys your blood-clot...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-367",
    "label": "Essential Thrombocythemia (High Platelets / Clotting Risk)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Essential Thrombocythemia (High Platelets / Clotting Risk)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Essential thrombocythemia is the exact opposite of immune thrombocytopenia. A genetic switch inside your bone ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-368",
    "label": "Thrombotic Thrombocytopenic Purpura (TTP / ADAMTS13 Deficiency)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Thrombotic Thrombocytopenic Purpura (TTP / ADAMTS13 Deficiency)?",
    "healthBody": "New England Journal of Medicine",
    "description": "TTP is a critical medical emergency. An enzyme (ADAMTS13) that normally snips giant sticky clotting proteins g...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-369",
    "label": "Hemolytic Uremic Syndrome (STEC-HUS / Shiga Toxin)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hemolytic Uremic Syndrome (STEC-HUS / Shiga Toxin)?",
    "healthBody": "Pediatric Nephrology & Lancet",
    "description": "Hemolytic uremic syndrome happens after a severe foodborne stomach bug (usually from undercooked ground beef o...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-370",
    "label": "Disseminated Intravascular Coagulation (DIC)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Disseminated Intravascular Coagulation (DIC)?",
    "healthBody": "Journal of Thrombosis and Haemostasis",
    "description": "DIC is a severe, paradoxical clotting and bleeding storm triggered by a catastrophic illness (like severe seps...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-371",
    "label": "Celiac Disease (Gluten Enteropathy & Villous Atrophy)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Celiac Disease (Gluten Enteropathy & Villous Atrophy)?",
    "healthBody": "American Journal of Gastroenterology",
    "description": "Celiac disease is an autoimmune condition where eating gluten (a protein found in wheat, barley, and rye) trig...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-372",
    "label": "Mallory-Weiss Syndrome (Gastroesophageal Mucosal Laceration)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Mallory-Weiss Syndrome (Gastroesophageal Mucosal Laceration)?",
    "healthBody": "Gastrointestinal Endoscopy",
    "description": "A Mallory-Weiss tear is a superficial tear in the inner lining of your esophagus where it connects to your sto...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-373",
    "label": "Boerhaave Syndrome (Transmural Esophageal Rupture)",
    "category": "Thoracic Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Boerhaave Syndrome (Transmural Esophageal Rupture)?",
    "healthBody": "World Journal of Emergency Surgery",
    "description": "Boerhaave syndrome is a catastrophic, full-thickness burst of your food pipe (esophagus) caused by violent vom...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-374",
    "label": "Bleeding Esophageal Varices (Portal Hypertension)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bleeding Esophageal Varices (Portal Hypertension)?",
    "healthBody": "Journal of Hepatology",
    "description": "When your liver is heavily scarred from cirrhosis, blood backs up like traffic on a blocked highway. Blood get...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-375",
    "label": "Peptic Ulcer Disease Bleeding (Forrest Class I/IIa)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Peptic Ulcer Disease Bleeding (Forrest Class I/IIa)?",
    "healthBody": "American Journal of Gastroenterology",
    "description": "A deep sore in the lining of your stomach or upper small intestine erodes into a blood vessel. It is most ofte...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-376",
    "label": "Acute Mesenteric Ischemia (Arterial Embolism / Thrombosis)",
    "category": "Vascular Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Mesenteric Ischemia (Arterial Embolism / Thrombosis)?",
    "healthBody": "World Journal of Emergency Surgery",
    "description": "A blood clot suddenly lodges in the main artery supplying blood to your intestines (like a stroke of the bowel...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-377",
    "label": "Small Bowel Obstruction (SBO - Adhesive Mechanical)",
    "category": "General Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Small Bowel Obstruction (SBO - Adhesive Mechanical)?",
    "healthBody": "World Journal of Emergency Surgery",
    "description": "Fibrous scar bands (adhesions) from a previous belly surgery act like tight rubber bands wrapped around your s...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-378",
    "label": "Paralytic Postoperative Ileus (Neurogenic Hypomotility)",
    "category": "General Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Paralytic Postoperative Ileus (Neurogenic Hypomotility)?",
    "healthBody": "World Journal of Surgery",
    "description": "Unlike a physical kink from a scar band, paralytic ileus is a temporary 'sleep' of your bowel muscles after su...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-379",
    "label": "Clostridioides difficile Colitis (Pseudomembranous Colitis)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Clostridioides difficile Colitis (Pseudomembranous Colitis)?",
    "healthBody": "Clinical Infectious Diseases",
    "description": "A severe bacterial infection of your colon that happens after taking antibiotics. The antibiotics wipe out you...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-380",
    "label": "Toxic Megacolon (Acute Colonic Dilation Emergency)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Toxic Megacolon (Acute Colonic Dilation Emergency)?",
    "healthBody": "American Journal of Gastroenterology",
    "description": "A life-threatening complication of severe colitis (from C. diff or ulcerative colitis) where the colon wall be...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-381",
    "label": "Aseptic Viral Meningitis (Enteroviral / HSV-2)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Aseptic Viral Meningitis (Enteroviral / HSV-2)?",
    "healthBody": "Clinical Infectious Diseases",
    "description": "A viral infection causes inflammation of the protective layers covering your brain and spinal cord. Unlike dan...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-382",
    "label": "Acute Bacterial Meningitis (Streptococcus pneumoniae)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Bacterial Meningitis (Streptococcus pneumoniae)?",
    "healthBody": "Clinical Infectious Diseases & Lancet",
    "description": "A life-threatening medical emergency where bacteria directly invade the fluid and lining around your brain. It...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-383",
    "label": "Acute Septic Arthritis (Synovial Fluid >50,000 WBCs)",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Septic Arthritis (Synovial Fluid >50,000 WBCs)?",
    "healthBody": "Rheumatology",
    "description": "A joint infection is a true orthopedic emergency. Bacteria (most often Staph) enter a joint (most commonly the...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-384",
    "label": "Anaphylactic Shock (IgE-Mediated Hypersensitivity)",
    "category": "Allergy",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Anaphylactic Shock (IgE-Mediated Hypersensitivity)?",
    "healthBody": "World Allergy Organization Journal",
    "description": "Anaphylaxis is an immediate, full-body allergic explosion (to foods, medications, or bee stings). Your immune ...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-385",
    "label": "Septic Shock (Sepsis-3 Refractory Vasoplegia)",
    "category": "Critical Care",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Septic Shock (Sepsis-3 Refractory Vasoplegia)?",
    "healthBody": "Critical Care Medicine & Intensive Care Medicine",
    "description": "Septic shock happens when a severe infection triggers an overwhelming body-wide inflammatory storm. Your blood...",
    "icon": "🚨"
  },
  {
    "id": "sug-doc-card-386",
    "label": "Acute Cellulitis & Erysipelas (Group A Streptococcus)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Cellulitis & Erysipelas (Group A Streptococcus)?",
    "healthBody": "Clinical Infectious Diseases",
    "description": "Cellulitis is a bacterial infection of the deep layers of your skin, most commonly on the lower leg. Bacteria ...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-387",
    "label": "Stasis Dermatitis (Venous Incompetence & Hemosiderin)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Stasis Dermatitis (Venous Incompetence & Hemosiderin)?",
    "healthBody": "Journal of Vascular Surgery",
    "description": "Stasis dermatitis is a common condition that is frequently mistaken for an infection (cellulitis). Weak valves...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-388",
    "label": "Necrotizing Fasciitis (Flesh-Eating Surgical Emergency)",
    "category": "General Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Necrotizing Fasciitis (Flesh-Eating Surgical Emergency)?",
    "healthBody": "World Journal of Emergency Surgery",
    "description": "Necrotizing fasciitis (flesh-eating infection) is a catastrophic surgical emergency. Fast-moving bacteria trav...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-389",
    "label": "Staphylococcal Toxic Shock Syndrome (TSS Toxin-1)",
    "category": "Infectious Disease",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Staphylococcal Toxic Shock Syndrome (TSS Toxin-1)?",
    "healthBody": "Clinical Infectious Diseases",
    "description": "Toxic shock syndrome is an overwhelming immune reaction to a toxin produced by common Staph bacteria (often as...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-390",
    "label": "Stevens-Johnson Syndrome & Toxic Epidermal Necrolysis (SJS/TEN)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Stevens-Johnson Syndrome & Toxic Epidermal Necrolysis (SJS/TEN)?",
    "healthBody": "British Journal of Dermatology",
    "description": "SJS and TEN are life-threatening allergic reactions to medications where your body attacks its own skin and mu...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-391",
    "label": "DRESS Syndrome (Drug Reaction with Eosinophilia and Systemic Symptoms)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for DRESS Syndrome (Drug Reaction with Eosinophilia and Systemic Symptoms)?",
    "healthBody": "British Journal of Dermatology",
    "description": "DRESS syndrome is a delayed, severe allergy to a medication that strikes 2 to 8 weeks after starting the pill....",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-392",
    "label": "Acute Compartment Syndrome (Traumatic Limb Ischemia)",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Compartment Syndrome (Traumatic Limb Ischemia)?",
    "healthBody": "Journal of the American Academy of Orthopaedic Surgeons",
    "description": "Compartment syndrome is a surgical emergency that happens after a broken bone or crushing injury. Muscles are ...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-393",
    "label": "Deep Vein Thrombosis of Lower Extremity (DVT)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Deep Vein Thrombosis of Lower Extremity (DVT)?",
    "healthBody": "Chest",
    "description": "A blood clot forms inside the deep veins of your calf or thigh. It blocks blood from flowing smoothly back to ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-394",
    "label": "Ruptured Baker's Popliteal Cyst (Pseudothrombophlebitis)",
    "category": "Orthopedics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ruptured Baker's Popliteal Cyst (Pseudothrombophlebitis)?",
    "healthBody": "Arthritis Care & Research",
    "description": "A Baker's cyst is a fluid-filled sac behind your knee caused by arthritis or cartilage tears. If the sac pops,...",
    "icon": "🦴"
  },
  {
    "id": "sug-doc-card-395",
    "label": "Acute Pancreatitis (Atlanta Criteria / Lipase >3x ULN)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Pancreatitis (Atlanta Criteria / Lipase >3x ULN)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Acute pancreatitis is sudden inflammation of your pancreas (most commonly caused by gallstones or heavy alcoho...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-396",
    "label": "Perforated Viscus & Pneumoperitoneum (Rigid Abdomen)",
    "category": "General Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Perforated Viscus & Pneumoperitoneum (Rigid Abdomen)?",
    "healthBody": "World Journal of Emergency Surgery",
    "description": "A hole has burst completely open in the wall of your stomach or intestines (often from a deep bleeding ulcer, ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-397",
    "label": "Acute Ascending Cholangitis (Charcot's Triad & Sepsis)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Ascending Cholangitis (Charcot's Triad & Sepsis)?",
    "healthBody": "Journal of Hepato-Biliary-Pancreatic Sciences",
    "description": "Acute cholangitis is a severe, life-threatening infection of the bile duct pipes draining your liver. A gallst...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-398",
    "label": "Acute Cholecystitis (Murphy's Sign & Gallbladder Empyema)",
    "category": "General Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Cholecystitis (Murphy's Sign & Gallbladder Empyema)?",
    "healthBody": "World Journal of Emergency Surgery",
    "description": "Acute cholecystitis happens when a gallstone gets stuck in the exit neck of your gallbladder. Bile is trapped ...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-399",
    "label": "Carbon Monoxide Poisoning (Carboxyhemoglobinemia)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Carbon Monoxide Poisoning (Carboxyhemoglobinemia)?",
    "healthBody": "Annals of Emergency Medicine",
    "description": "Carbon monoxide is an invisible, odorless, tasteless toxic gas produced by faulty furnaces, generators, or car...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-400",
    "label": "Cyanide Poisoning (Cytochrome Oxidase Inhibition)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cyanide Poisoning (Cytochrome Oxidase Inhibition)?",
    "healthBody": "Annals of Emergency Medicine",
    "description": "Cyanide is a rapidly fatal chemical poison (commonly inhaled during house fires from burning plastics, foams, ...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-401",
    "label": "Hypertrophic Obstructive Cardiomyopathy (HOCM)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hypertrophic Obstructive Cardiomyopathy (HOCM)?",
    "healthBody": "Lancet",
    "description": "The muscular wall separating the left and right pumping chambers of your heart becomes excessively thick and o...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-402",
    "label": "Dilated Cardiomyopathy (Non-Ischemic Systolic Dysfunction)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dilated Cardiomyopathy (Non-Ischemic Systolic Dysfunction)?",
    "healthBody": "Circulation",
    "description": "Unlike HOCM where the heart muscle is overly thick, dilated cardiomyopathy causes the heart's main pumping cha...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-403",
    "label": "Chronic Constrictive Pericarditis (Rigid Pericardial Shell)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Constrictive Pericarditis (Rigid Pericardial Shell)?",
    "healthBody": "European Heart Journal",
    "description": "The sac surrounding your heart (pericardium) becomes stiff, thickened, and heavily calcified like an armor she...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-404",
    "label": "Cardiac Amyloidosis (ATTR Transthyretin Cardiomyopathy)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cardiac Amyloidosis (ATTR Transthyretin Cardiomyopathy)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Misfolded proteins (amyloid fibrils) gradually deposit in between your heart muscle cells like cement or harde...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-405",
    "label": "Acute Aortic Dissection - Stanford Type A (Ascending Aorta)",
    "category": "Cardiothoracic Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Aortic Dissection - Stanford Type A (Ascending Aorta)?",
    "healthBody": "Annals of Thoracic Surgery",
    "description": "A catastrophic surgical emergency where the inner layer of the main artery leaving your heart (ascending aorta...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-406",
    "label": "Acute Aortic Dissection - Stanford Type B (Descending Aorta)",
    "category": "Vascular Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Aortic Dissection - Stanford Type B (Descending Aorta)?",
    "healthBody": "Journal of Vascular Surgery",
    "description": "The main aorta tears downstream from the heart (after the left arm artery branch in your chest or abdomen). Un...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-407",
    "label": "Ventricular Tachycardia (Monomorphic Sustained VT)",
    "category": "Cardiac Electrophysiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ventricular Tachycardia (Monomorphic Sustained VT)?",
    "healthBody": "Circulation",
    "description": "An abnormally rapid, dangerous electrical short-circuit originates deep inside your heart's main pumping chamb...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-408",
    "label": "Paroxysmal Supraventricular Tachycardia (AVNRT / AVRT)",
    "category": "Cardiac Electrophysiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Paroxysmal Supraventricular Tachycardia (AVNRT / AVRT)?",
    "healthBody": "Circulation",
    "description": "A benign electrical short-circuit or looping pathway inside the heart's upper junction box (AV node) triggers ...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-409",
    "label": "Wolff-Parkinson-White Syndrome (Pre-Excited Atrial Fibrillation)",
    "category": "Cardiac Electrophysiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Wolff-Parkinson-White Syndrome (Pre-Excited Atrial Fibrillation)?",
    "healthBody": "Circulation",
    "description": "You were born with an extra microscopic electrical wire (accessory pathway) connecting the upper and lower hea...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-410",
    "label": "Brugada Syndrome (Type 1 Coved ST Elevation Channelopathy)",
    "category": "Cardiac Electrophysiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Brugada Syndrome (Type 1 Coved ST Elevation Channelopathy)?",
    "healthBody": "Heart Rhythm",
    "description": "A genetic condition affecting the microscopic sodium gates in your heart cells. It causes a distinctive wave o...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-411",
    "label": "Congenital Long QT Syndrome (LQTS - Torsades de Pointes)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Congenital Long QT Syndrome (LQTS - Torsades de Pointes)?",
    "healthBody": "Circulation",
    "description": "The electrical recharging phase of your heart muscle cells takes longer than normal. On an ECG, this appears a...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-412",
    "label": "Sick Sinus Syndrome (Tachycardia-Bradycardia Syndrome)",
    "category": "Cardiac Electrophysiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sick Sinus Syndrome (Tachycardia-Bradycardia Syndrome)?",
    "healthBody": "Circulation",
    "description": "Your heart's natural spark plug (the sinus node) has worn out with age or fibrous scarring. It fires too slowl...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-413",
    "label": "Acute Fulminant Myocarditis (Inflammatory Cardiomyopathy)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Fulminant Myocarditis (Inflammatory Cardiomyopathy)?",
    "healthBody": "Circulation",
    "description": "An aggressive viral infection (or immunotherapy drug reaction) triggers your immune system to attack and infla...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-414",
    "label": "Takotsubo Cardiomyopathy (Stress-Induced Apical Ballooning)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Takotsubo Cardiomyopathy (Stress-Induced Apical Ballooning)?",
    "healthBody": "European Heart Journal",
    "description": "Also known as 'Broken Heart Syndrome', this condition happens when an overwhelming emotional shock or severe p...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-415",
    "label": "Atherosclerotic Renovascular Hypertension (Renal Artery Stenosis)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Atherosclerotic Renovascular Hypertension (Renal Artery Stenosis)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Cholesterol plaques narrow the main pipe supplying blood to one or both of your kidneys. The starved kidney mi...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-416",
    "label": "Fibromuscular Dysplasia (Renal 'String-of-Beads' FMD)",
    "category": "Vascular Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Fibromuscular Dysplasia (Renal 'String-of-Beads' FMD)?",
    "healthBody": "Vascular Medicine & European Heart Journal",
    "description": "A non-clotting disorder of blood vessel walls that most commonly affects young to middle-aged women. The muscu...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-417",
    "label": "Primary Hyperaldosteronism (Conn's Syndrome / Aldosteronoma)",
    "category": "Endocrinology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Hyperaldosteronism (Conn's Syndrome / Aldosteronoma)?",
    "healthBody": "Journal of Clinical Endocrinology & Metabolism",
    "description": "One or both of your adrenal glands (small caps on top of your kidneys) produce too much aldosterone hormone. T...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-418",
    "label": "Acute Aortic Regurgitation (Flail Valve Leaflet / Endocarditis)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Aortic Regurgitation (Flail Valve Leaflet / Endocarditis)?",
    "healthBody": "Circulation",
    "description": "The one-way exit valve of your heart (aortic valve) suddenly blows open or gets destroyed by a severe bacteria...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-419",
    "label": "Severe Calcific Aortic Stenosis (Low-Flow Low-Gradient vs High Gradient)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Severe Calcific Aortic Stenosis (Low-Flow Low-Gradient vs High Gradient)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Over decades, calcium and bone-like crusts build up on your heart's main exit doorway (aortic valve), making i...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-420",
    "label": "Severe Mitral Regurgitation (Acute Papillary Rupture vs Chronic Degenerative)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Severe Mitral Regurgitation (Acute Papillary Rupture vs Chronic Degenerative)?",
    "healthBody": "New England Journal of Medicine",
    "description": "The two-door flap valve (mitral valve) that prevents blood from leaking backward into your lungs fails to seal...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-421",
    "label": "Acute Respiratory Distress Syndrome (ARDS - Berlin Definition)",
    "category": "Critical Care",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Respiratory Distress Syndrome (ARDS - Berlin Definition)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A severe, life-threatening lung inflammation that develops rapidly after pneumonia, sepsis, or severe trauma. ...",
    "icon": "🚨"
  },
  {
    "id": "sug-doc-card-422",
    "label": "Non-Cystic Fibrosis Bronchiectasis (Chronic Airway Dilation)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Non-Cystic Fibrosis Bronchiectasis (Chronic Airway Dilation)?",
    "healthBody": "Thorax & Lancet Respiratory Medicine",
    "description": "Your breathing tubes (bronchi) have become permanently stretched out, widened, and scarred from recurrent infe...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-423",
    "label": "Cystic Fibrosis (CFTR Modulator Triplet Therapy)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cystic Fibrosis (CFTR Modulator Triplet Therapy)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A genetic condition affecting a microscopic salt channel (CFTR). Because salt cannot move normally, mucus ever...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-424",
    "label": "Pulmonary Sarcoidosis (Non-Caseating Granulomatous Disease)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pulmonary Sarcoidosis (Non-Caseating Granulomatous Disease)?",
    "healthBody": "American Journal of Respiratory and Critical Care Medicine",
    "description": "Your immune cells cluster together to form microscopic clumps of inflammation called granulomas, most often in...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-425",
    "label": "Chronic Hypersensitivity Pneumonitis (Bird Fancier / Farmer's Lung)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Hypersensitivity Pneumonitis (Bird Fancier / Farmer's Lung)?",
    "healthBody": "American Journal of Respiratory and Critical Care Medicine",
    "description": "An allergic inflammation deep inside your lungs triggered by repeatedly breathing in organic dusts—such as pro...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-426",
    "label": "Silicosis (Eggshell Calcification Pneumoconiosis)",
    "category": "Occupational Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Silicosis (Eggshell Calcification Pneumoconiosis)?",
    "healthBody": "American Journal of Respiratory and Critical Care Medicine",
    "description": "An occupational lung disease caused by inhaling fine silica dust from stone cutting, sandblasting, or manufact...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-427",
    "label": "Coal Workers' Pneumoconiosis (Black Lung & Caplan Syndrome)",
    "category": "Occupational Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Coal Workers' Pneumoconiosis (Black Lung & Caplan Syndrome)?",
    "healthBody": "Lancet",
    "description": "A chronic occupational lung scarring disease caused by decades of inhaling coal dust underground ('Black Lung'...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-428",
    "label": "Asbestosis & Pleural Plaques (Amphibole / Chrysotile Fibrosis)",
    "category": "Occupational Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Asbestosis & Pleural Plaques (Amphibole / Chrysotile Fibrosis)?",
    "healthBody": "American Journal of Respiratory and Critical Care Medicine",
    "description": "Breathing in microscopic mineral fibers (asbestos) from old shipyards, brake linings, pipes, or insulation dec...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-429",
    "label": "Pleural Empyema (Complicated Parapneumonic Infection)",
    "category": "Thoracic Surgery",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pleural Empyema (Complicated Parapneumonic Infection)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A severe complication of pneumonia where the infection spills into the water space surrounding your lung (pleu...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-430",
    "label": "Malignant Pleural Effusion (Metastatic Pleural Carcinomatosis)",
    "category": "Interventional Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Malignant Pleural Effusion (Metastatic Pleural Carcinomatosis)?",
    "healthBody": "JAMA & Lancet Oncology",
    "description": "Cancer cells from the lung, breast, or other organs spread to the lining of your chest, causing fluid to conti...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-431",
    "label": "Chronic Thromboembolic Pulmonary Hypertension (CTEPH)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Thromboembolic Pulmonary Hypertension (CTEPH)?",
    "healthBody": "New England Journal of Medicine",
    "description": "After a pulmonary embolism, old blood clots do not dissolve normally. Instead, they transform into tough, fibr...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-432",
    "label": "Pulmonary Arterial Hypertension (Group 1 WHO PAH)",
    "category": "Cardiology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pulmonary Arterial Hypertension (Group 1 WHO PAH)?",
    "healthBody": "New England Journal of Medicine",
    "description": "The microscopic blood vessels inside your lungs become pathologically thick, narrow, and stiff. Your heart's r...",
    "icon": "❤️"
  },
  {
    "id": "sug-doc-card-433",
    "label": "Bronchial Carcinoid Tumor (Neuroendocrine Bronchospasm)",
    "category": "Thoracic Oncology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bronchial Carcinoid Tumor (Neuroendocrine Bronchospasm)?",
    "healthBody": "Neuroendocrinology",
    "description": "A slow-growing neuroendocrine tumor growing inside a lung breathing tube. Because it partly blocks airflow and...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-434",
    "label": "Idiopathic Pulmonary Fibrosis (UIP Pattern - Antifibrotic GDMT)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Idiopathic Pulmonary Fibrosis (UIP Pattern - Antifibrotic GDMT)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A progressive scarring disease where the elastic, sponge-like walls of your lungs slowly turn into thick, stif...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-435",
    "label": "Cryptogenic Organizing Pneumonia (COP - Steroid-Responsive)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Cryptogenic Organizing Pneumonia (COP - Steroid-Responsive)?",
    "healthBody": "European Respiratory Journal",
    "description": "Inflammatory plugs of connective tissue fill your microscopic air sacs, often appearing on X-rays like patches...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-436",
    "label": "Eosinophilic Granulomatosis with Polyangiitis (EGPA / Churg-Strauss)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Eosinophilic Granulomatosis with Polyangiitis (EGPA / Churg-Strauss)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A rare autoimmune condition combining severe asthma, nasal polyps, and very high levels of allergy cells (eosi...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-437",
    "label": "Allergic Bronchopulmonary Aspergillosis (ABPA)",
    "category": "Pulmonology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Allergic Bronchopulmonary Aspergillosis (ABPA)?",
    "healthBody": "Journal of Allergy and Clinical Immunology",
    "description": "An intense allergic overreaction in your lungs caused by mold spores (Aspergillus) that live in soil and mulch...",
    "icon": "🫁"
  },
  {
    "id": "sug-doc-card-438",
    "label": "Obesity Hypoventilation Syndrome (Pickwickian Sleep Hypoventilation)",
    "category": "Sleep Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Obesity Hypoventilation Syndrome (Pickwickian Sleep Hypoventilation)?",
    "healthBody": "American Journal of Respiratory and Critical Care Medicine",
    "description": "Severe excess body weight presses down on your chest wall and diaphragm like heavy sandbags. Your breathing mu...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-439",
    "label": "Vocal Cord Dysfunction / Inducible Laryngeal Obstruction (ILO)",
    "category": "Otolaryngology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Vocal Cord Dysfunction / Inducible Laryngeal Obstruction (ILO)?",
    "healthBody": "European Respiratory Journal",
    "description": "Your vocal cords (voice box) snap tightly shut when you breathe IN, instead of opening wide to let air enter. ...",
    "icon": "👂"
  },
  {
    "id": "sug-doc-card-440",
    "label": "Aspirin-Exacerbated Respiratory Disease (AERD / Samter Triad)",
    "category": "Allergy",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Aspirin-Exacerbated Respiratory Disease (AERD / Samter Triad)?",
    "healthBody": "Journal of Allergy and Clinical Immunology",
    "description": "A distinctive condition combining severe asthma, aggressive nasal polyps that block your sense of smell, and a...",
    "icon": "🛡️"
  },
  {
    "id": "sug-doc-card-441",
    "label": "Primary Biliary Cholangitis (PBC - Anti-Mitochondrial Antibodies)",
    "category": "Hepatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Biliary Cholangitis (PBC - Anti-Mitochondrial Antibodies)?",
    "healthBody": "Hepatology",
    "description": "An autoimmune condition where your body's immune system slowly attacks and destroys the microscopic bile ducts...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-442",
    "label": "Primary Sclerosing Cholangitis (PSC - Large Duct Beaded Strictures)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Sclerosing Cholangitis (PSC - Large Duct Beaded Strictures)?",
    "healthBody": "Hepatology",
    "description": "A chronic disease that causes inflammation, scarring, and tightening of the medium and large bile pipes inside...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-443",
    "label": "Autoimmune Hepatitis (Type 1 Anti-SMA & Hypergammaglobulinemia)",
    "category": "Hepatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Autoimmune Hepatitis (Type 1 Anti-SMA & Hypergammaglobulinemia)?",
    "healthBody": "Hepatology",
    "description": "Your own immune system mistakes your liver cells for foreign invaders and attacks them, driving up liver enzym...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-444",
    "label": "Wilson's Disease (Hepatolenticular Degeneration - Copper Overload)",
    "category": "Medical Genetics",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Wilson's Disease (Hepatolenticular Degeneration - Copper Overload)?",
    "healthBody": "Journal of Hepatology",
    "description": "A genetic condition where your liver cannot pump extra dietary copper into bile. Over years, toxic copper pile...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-445",
    "label": "Hereditary Hemochromatosis (C282Y HFE Iron Overload)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hereditary Hemochromatosis (C282Y HFE Iron Overload)?",
    "healthBody": "Hepatology",
    "description": "Your body absorbs far too much iron from ordinary food because of a genetic mutation in the HFE gene. The exce...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-446",
    "label": "Gastroparesis (Delayed Gastric Emptying / Diabetic Gastroparesis)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gastroparesis (Delayed Gastric Emptying / Diabetic Gastroparesis)?",
    "healthBody": "American Journal of Gastroenterology",
    "description": "The muscular pump of your stomach becomes sluggish and partly paralyzed (often caused by diabetes or nerve inj...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-447",
    "label": "Esophageal Achalasia (Aperistalsis & Non-Relaxing LES)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Esophageal Achalasia (Aperistalsis & Non-Relaxing LES)?",
    "healthBody": "American Journal of Gastroenterology & NEJM",
    "description": "The muscular ring at the bottom of your swallowing tube (lower esophageal sphincter) stays clamped shut like a...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-448",
    "label": "Zenker's Diverticulum (Killian Triangle Pharyngeal Pouch)",
    "category": "Otolaryngology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Zenker's Diverticulum (Killian Triangle Pharyngeal Pouch)?",
    "healthBody": "Gastrointestinal Endoscopy",
    "description": "A small outpouching or pocket forms at the back of your throat, right above your swallowing tube. Food gets tr...",
    "icon": "👂"
  },
  {
    "id": "sug-doc-card-449",
    "label": "Microscopic Colitis: Collagenous Colitis (Subepithelial Band)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Microscopic Colitis: Collagenous Colitis (Subepithelial Band)?",
    "healthBody": "Gastroenterology",
    "description": "A condition causing chronic, watery diarrhea (often 5 to 10 watery stools a day) where your colon appears 100%...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-450",
    "label": "Microscopic Colitis: Lymphocytic Colitis (Intraepithelial Lymphocytes)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Microscopic Colitis: Lymphocytic Colitis (Intraepithelial Lymphocytes)?",
    "healthBody": "United European Gastroenterology Journal",
    "description": "Similar to collagenous colitis, lymphocytic colitis causes persistent, watery diarrhea with completely normal-...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-451",
    "label": "Exocrine Pancreatic Insufficiency (EPI - Severe Steatorrhea)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Exocrine Pancreatic Insufficiency (EPI - Severe Steatorrhea)?",
    "healthBody": "American Journal of Gastroenterology",
    "description": "Your pancreas has lost its ability to manufacture digestive enzymes (lipase, protease, amylase). Because dieta...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-452",
    "label": "Chronic Calcific Pancreatitis (Intractable Pain & Duct Stones)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Calcific Pancreatitis (Intractable Pain & Duct Stones)?",
    "healthBody": "United European Gastroenterology Journal",
    "description": "Permanent, irreversible scarring and calcium stones form inside the drainage ducts of your pancreas (most ofte...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-453",
    "label": "Budd-Chiari Syndrome (Hepatic Venous Outflow Obstruction)",
    "category": "Hepatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Budd-Chiari Syndrome (Hepatic Venous Outflow Obstruction)?",
    "healthBody": "Journal of Hepatology",
    "description": "A rare and dangerous blood clot forms in the main drainage veins leaving your liver (hepatic veins). Because b...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-454",
    "label": "Spontaneous Bacterial Peritonitis (SBP - Ascitic PMN >=250/mcL)",
    "category": "Hepatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Spontaneous Bacterial Peritonitis (SBP - Ascitic PMN >=250/mcL)?",
    "healthBody": "Hepatology",
    "description": "A severe, life-threatening bacterial infection that develops spontaneously inside the fluid pool in your belly...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-455",
    "label": "Hepatorenal Syndrome (HRS-AKI - Refractory Vasoplegia)",
    "category": "Hepatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hepatorenal Syndrome (HRS-AKI - Refractory Vasoplegia)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A severe complication of advanced liver disease where your kidneys shut down, not because the kidneys themselv...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-456",
    "label": "Hepatic Encephalopathy (West Haven Neuropsychiatric Staging)",
    "category": "Hepatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hepatic Encephalopathy (West Haven Neuropsychiatric Staging)?",
    "healthBody": "Hepatology",
    "description": "When the liver is severely scarred or bypassed by shunts, it cannot filter ammonia and digestive toxins produc...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-457",
    "label": "Eosinophilic Esophagitis (EoE - Trachealization & Food Impaction)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Eosinophilic Esophagitis (EoE - Trachealization & Food Impaction)?",
    "healthBody": "New England Journal of Medicine",
    "description": "An allergic inflammation inside your swallowing tube (esophagus) triggered by common foods (most often cow's m...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-458",
    "label": "Severe Erosive Reflux Esophagitis (Los Angeles Grade C/D)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Severe Erosive Reflux Esophagitis (Los Angeles Grade C/D)?",
    "healthBody": "American Journal of Gastroenterology",
    "description": "Stomach acid and bile splash backward into your lower esophagus with such harsh intensity that they burn deep,...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-459",
    "label": "Gastric Antral Vascular Ectasia (GAVE - 'Watermelon Stomach')",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Gastric Antral Vascular Ectasia (GAVE - 'Watermelon Stomach')?",
    "healthBody": "Gastrointestinal Endoscopy",
    "description": "The tiny microscopic blood vessels inside the lower part of your stomach (antrum) become enlarged, fragile, an...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-460",
    "label": "Dieulafoy's Lesion (Submucosal Caliber-Persistent Arterial Bleed)",
    "category": "Gastroenterology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dieulafoy's Lesion (Submucosal Caliber-Persistent Arterial Bleed)?",
    "healthBody": "Gastrointestinal Endoscopy",
    "description": "A surprisingly dangerous, abnormally thick artery running just beneath the surface of your stomach wall. Becau...",
    "icon": "🫕"
  },
  {
    "id": "sug-doc-card-461",
    "label": "Minimal Change Disease (Nephrotic Foot Process Effacement)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Minimal Change Disease (Nephrotic Foot Process Effacement)?",
    "healthBody": "Kidney International",
    "description": "The tiny microscopic filters in your kidneys (glomeruli) look completely normal under a standard light microsc...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-462",
    "label": "Primary Membranous Nephropathy (Anti-PLA2R Antibodies)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Primary Membranous Nephropathy (Anti-PLA2R Antibodies)?",
    "healthBody": "New England Journal of Medicine",
    "description": "An autoimmune condition where your immune system makes specific antibodies (Anti-PLA2R) that attack the outer ...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-463",
    "label": "Focal Segmental Glomerulosclerosis (FSGS - APOL1 Podocytopathy)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Focal Segmental Glomerulosclerosis (FSGS - APOL1 Podocytopathy)?",
    "healthBody": "Kidney International",
    "description": "Scar tissue forms in scattered patches (focal) and in small segments of your kidney filters. Because the damag...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-464",
    "label": "IgA Nephropathy (Berger's Disease - Synpharyngitic Hematuria)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for IgA Nephropathy (Berger's Disease - Synpharyngitic Hematuria)?",
    "healthBody": "JAMA & Lancet",
    "description": "The most common kidney filter disease in the world. Your body makes an unusual form of an antibody called IgA ...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-465",
    "label": "Post-Streptococcal Glomerulonephritis (PSGN - Latent Subepithelial Humps)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Post-Streptococcal Glomerulonephritis (PSGN - Latent Subepithelial Humps)?",
    "healthBody": "Pediatric Nephrology",
    "description": "An immune reaction in your kidneys that strikes 1 to 3 weeks AFTER a strep throat infection (or 3 to 6 weeks a...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-466",
    "label": "Lupus Nephritis (ISN/RPS Class IV Diffuse Proliferative)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Lupus Nephritis (ISN/RPS Class IV Diffuse Proliferative)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Lupus (SLE) causes your immune system to attack and severely inflame your kidney filters, causing protein and ...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-467",
    "label": "Autosomal Dominant Polycystic Kidney Disease (ADPKD - Tolvaptan GDMT)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Autosomal Dominant Polycystic Kidney Disease (ADPKD - Tolvaptan GDMT)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A genetic condition where thousands of fluid-filled blisters (cysts) slowly grow inside both of your kidneys o...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-468",
    "label": "Distal Renal Tubular Acidosis (Type 1 dRTA - Alkaline Urine pH >5.5)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Distal Renal Tubular Acidosis (Type 1 dRTA - Alkaline Urine pH >5.5)?",
    "healthBody": "Kidney International & CJASN",
    "description": "The tiny microscopic pumps in the collecting tubes of your kidneys cannot pump acid out into your urine. Becau...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-469",
    "label": "Proximal Renal Tubular Acidosis (Type 2 pRTA - Fanconi Syndrome)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Proximal Renal Tubular Acidosis (Type 2 pRTA - Fanconi Syndrome)?",
    "healthBody": "Kidney International",
    "description": "The front filtering tubes of your kidneys (proximal tubules) fail to reabsorb bicarbonate, spilling it into yo...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-470",
    "label": "Hyperkalemic Renal Tubular Acidosis (Type 4 RTA - Hypoaldosteronism)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Hyperkalemic Renal Tubular Acidosis (Type 4 RTA - Hypoaldosteronism)?",
    "healthBody": "American Journal of Kidney Diseases",
    "description": "The most common kidney tubular acid condition, frequently occurring in individuals with diabetes or mild kidne...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-471",
    "label": "Calcium Oxalate Nephrolithiasis (Hypercalciuria & Hypocitraturia)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Calcium Oxalate Nephrolithiasis (Hypercalciuria & Hypocitraturia)?",
    "healthBody": "Journal of Urology",
    "description": "The most common type of kidney stone (accounting for 80% of stones). Calcium binds with oxalate in your urine,...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-472",
    "label": "Uric Acid Nephrolithiasis (Radiolucent Stones & Alkalinization)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Uric Acid Nephrolithiasis (Radiolucent Stones & Alkalinization)?",
    "healthBody": "European Urology",
    "description": "Kidney stones made of crystallized uric acid. Unlike calcium stones, uric acid stones are completely invisible...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-473",
    "label": "Struvite Infection Stones (Triple Phosphate Staghorn Calculi)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Struvite Infection Stones (Triple Phosphate Staghorn Calculi)?",
    "healthBody": "Journal of Urology",
    "description": "Dangerous 'infection stones' that grow rapidly into giant branching antlers (staghorn stones) that fill your e...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-474",
    "label": "Interstitial Cystitis / Bladder Pain Syndrome (Hunner Lesions)",
    "category": "Urology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Interstitial Cystitis / Bladder Pain Syndrome (Hunner Lesions)?",
    "healthBody": "Journal of Urology",
    "description": "A chronic, agonizing bladder condition causing burning pelvic pain, pressure, and needing to urinate 20 to 40 ...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-475",
    "label": "Anti-Glomerular Basement Membrane Disease (Goodpasture Syndrome)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Anti-Glomerular Basement Membrane Disease (Goodpasture Syndrome)?",
    "healthBody": "Kidney International",
    "description": "A rare, aggressive medical emergency where your body manufactures antibodies that attack the collagen foundati...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-476",
    "label": "Granulomatosis with Polyangiitis (GPA / Wegener's PR3-ANCA)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Granulomatosis with Polyangiitis (GPA / Wegener's PR3-ANCA)?",
    "healthBody": "New England Journal of Medicine",
    "description": "An autoimmune condition where antibodies (PR3-ANCA) inflame and destroy small blood vessels, particularly in y...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-477",
    "label": "Microscopic Polyangiitis (MPA - MPO-ANCA / p-ANCA)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Microscopic Polyangiitis (MPA - MPO-ANCA / p-ANCA)?",
    "healthBody": "New England Journal of Medicine",
    "description": "An autoimmune small blood vessel inflammation that specifically attacks your kidney filters and the blood vess...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-478",
    "label": "Rhabdomyolysis (Crush Injury & Myoglobinuric AKI)",
    "category": "Emergency Medicine",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Rhabdomyolysis (Crush Injury & Myoglobinuric AKI)?",
    "healthBody": "New England Journal of Medicine",
    "description": "Severe muscle breakdown triggered by a crush injury, intense unaccustomed exercise, prolonged immobility on a ...",
    "icon": "🩺"
  },
  {
    "id": "sug-doc-card-479",
    "label": "Contrast-Associated Acute Kidney Injury (CA-AKI / CIN)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Contrast-Associated Acute Kidney Injury (CA-AKI / CIN)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A temporary decline in kidney function that can happen after receiving concentrated iodine contrast dye for a ...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-480",
    "label": "Acute Interstitial Nephritis (Drug-Induced AIN - Triad Fever/Rash/Eosinophilia)",
    "category": "Nephrology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Interstitial Nephritis (Drug-Induced AIN - Triad Fever/Rash/Eosinophilia)?",
    "healthBody": "Kidney International",
    "description": "An allergic reaction deep inside the sponge tissue surrounding your kidney tubes (interstitium) caused by a me...",
    "icon": "💧"
  },
  {
    "id": "sug-doc-card-481",
    "label": "Myasthenia Gravis (AChR-Ab Post-Synaptic Junction Failure)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Myasthenia Gravis (AChR-Ab Post-Synaptic Junction Failure)?",
    "healthBody": "Lancet Neurology",
    "description": "An autoimmune condition where your immune system attacks the docking docks (acetylcholine receptors) on your m...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-482",
    "label": "Lambert-Eaton Myasthenic Syndrome (LEMS - Pre-Synaptic P/Q-Type VGCC)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Lambert-Eaton Myasthenic Syndrome (LEMS - Pre-Synaptic P/Q-Type VGCC)?",
    "healthBody": "Cochrane Database of Systematic Reviews & Lancet Neurology",
    "description": "A rare condition where antibodies block the microscopic calcium gates at the very tips of your nerves, prevent...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-483",
    "label": "Amyotrophic Lateral Sclerosis (ALS - Mixed Upper & Lower Motor Neuron)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Amyotrophic Lateral Sclerosis (ALS - Mixed Upper & Lower Motor Neuron)?",
    "healthBody": "Neurology & Lancet Neurology",
    "description": "A motor neuron disease (often known as Lou Gehrig's disease) where the nerve cells that control your voluntary...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-484",
    "label": "Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyneuropathy)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyneuropathy)?",
    "healthBody": "Cochrane Database of Systematic Reviews & Lancet Neurology",
    "description": "A rapid, temporary immune reaction (often triggered by a stomach bug or cold 1 to 3 weeks earlier) where your ...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-485",
    "label": "Chronic Inflammatory Demyelinating Polyneuropathy (CIDP)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Inflammatory Demyelinating Polyneuropathy (CIDP)?",
    "healthBody": "Lancet Neurology",
    "description": "A chronic, ongoing autoimmune condition where your immune system continuously damages the insulation around yo...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-486",
    "label": "Trigeminal Neuralgia (Tic Douloureux - Neurovascular Compression)",
    "category": "Neurology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Trigeminal Neuralgia (Tic Douloureux - Neurovascular Compression)?",
    "healthBody": "Neurology",
    "description": "Known as one of the most agonizing pains in human medicine ('Tic Douloureux'). An artery at the base of your b...",
    "icon": "🧠"
  },
  {
    "id": "sug-doc-card-487",
    "label": "Sjögren's Disease (Anti-SSA/Ro Autoimmune Exocrinopathy)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Sjögren's Disease (Anti-SSA/Ro Autoimmune Exocrinopathy)?",
    "healthBody": "Annals of the Rheumatic Diseases",
    "description": "An autoimmune condition where your immune cells attack and dry out the moisture-producing glands in your body,...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-488",
    "label": "Diffuse Cutaneous Systemic Sclerosis (Anti-Scl-70 / Scleroderma Renal Crisis)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diffuse Cutaneous Systemic Sclerosis (Anti-Scl-70 / Scleroderma Renal Crisis)?",
    "healthBody": "Annals of the Rheumatic Diseases",
    "description": "A serious autoimmune condition where your body overproduces collagen scar tissue throughout your skin and inte...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-489",
    "label": "Limited Cutaneous Systemic Sclerosis (CREST Syndrome / Anti-Centromere)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Limited Cutaneous Systemic Sclerosis (CREST Syndrome / Anti-Centromere)?",
    "healthBody": "Annals of the Rheumatic Diseases",
    "description": "A milder, slower-moving form of scleroderma often called CREST syndrome. Skin thickening is limited to your fi...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-490",
    "label": "Ankylosing Spondylitis (Axial Spondyloarthritis - HLA-B27 Bamboo Spine)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Ankylosing Spondylitis (Axial Spondyloarthritis - HLA-B27 Bamboo Spine)?",
    "healthBody": "Lancet & New England Journal of Medicine",
    "description": "An autoimmune arthritis that attacks your lower back and pelvic joints (sacroiliac joints), strongly linked to...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-491",
    "label": "Polymyalgia Rheumatica (PMR - Rapid Low-Dose Corticosteroid Response)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Polymyalgia Rheumatica (PMR - Rapid Low-Dose Corticosteroid Response)?",
    "healthBody": "Annals of the Rheumatic Diseases & NEJM",
    "description": "An inflammatory condition that strikes adults over age 50, causing severe stiffness and aching in both shoulde...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-492",
    "label": "Dermatomyositis (Gottron's Papules & Paraneoplastic Myopathy)",
    "category": "Rheumatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Dermatomyositis (Gottron's Papules & Paraneoplastic Myopathy)?",
    "healthBody": "New England Journal of Medicine",
    "description": "An autoimmune condition where your immune system attacks your small blood vessels, causing inflammation in you...",
    "icon": "🤲"
  },
  {
    "id": "sug-doc-card-493",
    "label": "Bullous Pemphigoid (BP180/BP230 Subepidermal Tense Blisters)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Bullous Pemphigoid (BP180/BP230 Subepidermal Tense Blisters)?",
    "healthBody": "British Journal of Dermatology & Cochrane Reviews",
    "description": "An autoimmune blistering disease of older adults where antibodies attack the microscopic velcro anchors (hemid...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-494",
    "label": "Pemphigus Vulgaris (Desmoglein 3/1 Intraepidermal Flaccid Blisters)",
    "category": "Dermatology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Pemphigus Vulgaris (Desmoglein 3/1 Intraepidermal Flaccid Blisters)?",
    "healthBody": "Lancet",
    "description": "A rare, serious autoimmune skin disease where your antibodies attack the glue (desmoglein) that binds skin cel...",
    "icon": "🧴"
  },
  {
    "id": "sug-doc-card-495",
    "label": "Multiple Myeloma (CRAB Criteria & Quadruplet Induction GDMT)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Multiple Myeloma (CRAB Criteria & Quadruplet Induction GDMT)?",
    "healthBody": "Blood & Lancet",
    "description": "A blood cancer where abnormal plasma cells (which normally make infection-fighting antibodies) multiply uncont...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-496",
    "label": "Monoclonal Gammopathy of Undetermined Significance (MGUS - Premalignant)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Monoclonal Gammopathy of Undetermined Significance (MGUS - Premalignant)?",
    "healthBody": "Lancet Oncology & Blood",
    "description": "A common, silent blood finding where a small cluster of plasma cells produces a small amount of extra antibody...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-497",
    "label": "Chronic Lymphocytic Leukemia (CLL - Del(17p)/TP53 & BTK Inhibitors)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Chronic Lymphocytic Leukemia (CLL - Del(17p)/TP53 & BTK Inhibitors)?",
    "healthBody": "New England Journal of Medicine",
    "description": "The most common leukemia in adults. Your bone marrow produces too many mature-looking white blood cells (lymph...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-498",
    "label": "Acute Myeloid Leukemia (AML - Auer Rods & Targeted 7+3 Induction)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Acute Myeloid Leukemia (AML - Auer Rods & Targeted 7+3 Induction)?",
    "healthBody": "New England Journal of Medicine",
    "description": "An aggressive, fast-moving cancer of the blood where your bone marrow fills with immature, non-working white b...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-499",
    "label": "Classical Hodgkin Lymphoma (Reed-Sternberg Cells & Nivolumab-AVD)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Classical Hodgkin Lymphoma (Reed-Sternberg Cells & Nivolumab-AVD)?",
    "healthBody": "New England Journal of Medicine",
    "description": "A highly curable cancer of the lymphatic system that most often affects teenagers and young adults. It begins ...",
    "icon": "🩸"
  },
  {
    "id": "sug-doc-card-500",
    "label": "Diffuse Large B-Cell Lymphoma (DLBCL - Pola-R-CHP & CAR-T Therapy)",
    "category": "Hematology",
    "query": "What are the verified clinical guidelines and evidence-backed treatments for Diffuse Large B-Cell Lymphoma (DLBCL - Pola-R-CHP & CAR-T Therapy)?",
    "healthBody": "New England Journal of Medicine",
    "description": "The most common aggressive lymphoma in adults. Cancerous B-cells multiply rapidly in your lymph nodes, forming...",
    "icon": "🩸"
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
