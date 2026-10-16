"""
part1_cardio_pulm.py
"""

PART_1_DISEASES = [
    {
        "id": "DOC-CARD-101",
        "icd10": "I35.0",
        "condition": "Aortic Valve Stenosis",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (PARTNER 3)",
        "citation": "Mack MJ et al. Transcatheter Aortic-Valve Replacement with a Balloon-Expandable Valve in Low-Risk Patients (PARTNER 3). N Engl J Med. 2019;380:1695-1705.",
        "doi_or_source": "10.1056/NEJMoa1814052",
        "clinical_evidence": "In 1,000 low-risk patients with severe symptomatic aortic stenosis, transcatheter aortic-valve replacement (TAVR) with a balloon-expandable valve was superior to surgical replacement with respect to composite death, stroke, or rehospitalization at 1 year (8.5% vs 15.1%; difference -7.1 percentage points; 95% CI -10.8 to -3.5; p<0.001 for noninferiority, p=0.001 for superiority). Standard therapy requires echocardiographic surveillance and valve intervention once AVA <1.0 cm2 or mean gradient >=40 mmHg with symptoms.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoidance of competitive vigorous exertion once severe; structured low-intensity cardiac conditioning; strict systolic blood pressure control without sudden vasodilation.",
            "monitoring_cadence": "Transthoracic echocardiogram (TTE) every 6-12 months for severe asymptomatic AS; annual TTE for moderate AS.",
            "clinical_thresholds": "Aortic valve area (AVA) < 1.0 cm² or mean gradient ≥ 40 mmHg, peak velocity ≥ 4.0 m/s triggers valve team evaluation."
        },
        "patient_plain_language": "Aortic stenosis is like a doorway in your heart's main valve that has become calcified, stiff, and narrow. When the door cannot open fully, your heart has to squeeze much harder to pump blood to the rest of your body.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current aortic valve area and mean pressure gradient on my latest echocardiogram?",
            "safety_question": "Are there blood pressure medications, like high-dose nitrates, that I should avoid to prevent fainting?",
            "action_threshold_question": "What specific symptoms (like sudden shortness of breath, dizziness on standing, or chest pressure) mean I need an immediate valve evaluation?"
        },
        "red_flags": [
            "Sudden syncope (fainting) on minimal exertion, acute angina at rest, or new-onset resting pulmonary edema"
        ]
    },
    {
        "id": "DOC-CARD-102",
        "icd10": "I42.1",
        "condition": "Hypertrophic Cardiomyopathy (HCM)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (EXPLORER-HCM)",
        "citation": "Olivotto I et al. Mavacamten for treatment of symptomatic obstructive hypertrophic cardiomyopathy (EXPLORER-HCM). Lancet. 2020;396(10253):759-769.",
        "doi_or_source": "10.1016/S0140-6736(20)31792-X",
        "clinical_evidence": "In 251 patients with obstructive hypertrophic cardiomyopathy, the cardiac myosin inhibitor mavacamten significantly increased peak oxygen consumption (pVO2) and reduced LVOT gradient by 36 mmHg vs placebo (p<0.0001). 37% of mavacamten-treated patients met the primary composite endpoint vs 17% in placebo. First-line therapy includes non-vasodilating beta-blockers or nondihydropyridine calcium channel blockers.",
        "solution_protocol": {
            "non_pharmacological_targets": "Adequate daily hydration (avoid dehydration/hypovolemia); avoidance of intense competitive athletics or sudden burst training; genetic counseling for first-degree relatives.",
            "monitoring_cadence": "Annual clinical review, 24-48 hour ambulatory ECG Holter for ventricular arrhythmias, and repeat TTE.",
            "clinical_thresholds": "LV wall thickness ≥ 30 mm, unexplained syncope, or family history of sudden death mandates ICD risk score evaluation."
        },
        "patient_plain_language": "Hypertrophic cardiomyopathy is a genetic condition where the heart muscle walls become abnormally thick and bulky, like an over-muscled pump. This extra thickness makes it harder for the heart chamber to relax and can partly block blood leaving the heart.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my left ventricular outflow tract (LVOT) gradient at rest and with exertion?",
            "safety_question": "Should my children or siblings undergo genetic testing and echocardiogram screening for this heart condition?",
            "action_threshold_question": "What is my calculated 5-year risk score for sudden cardiac death and do I qualify for an implantable defibrillator (ICD)?"
        },
        "red_flags": [
            "Unexplained sudden fainting (syncope) during or right after exertion, sustained rapid heart racing, or sudden crushing chest pain"
        ]
    },
    {
        "id": "DOC-CARD-103",
        "icd10": "I33.0",
        "condition": "Infective Endocarditis",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Multi-Society Clinical Practice Guideline",
        "source_body": "Circulation (AHA)",
        "citation": "Baddour LM et al. Infective Endocarditis in Adults: Diagnosis, Antimicrobial Therapy, and Management of Complications. Circulation. 2015;132(15):1435-1486.",
        "doi_or_source": "10.1161/CIR.0000000000000296",
        "clinical_evidence": "AHA/ESC guidelines mandate modified Duke Criteria for diagnostic confirmation (positive blood cultures across multiple bottles and transesophageal echocardiographic demonstration of oscillating vegetation or abscess). Intravenous bactericidal antibiotic therapy tailored to organism (viridans streptococci, S. aureus, Enterococcus) for 4-6 weeks is required. Early surgical valve replacement is indicated for heart failure, fungal/resistant infection, or persistent large mobile vegetations (>10 mm) with recurrent embolization.",
        "solution_protocol": {
            "non_pharmacological_targets": "Meticulous oral dental hygiene; prompt eradication of skin/catheter infection sources; antibiotic prophylaxis before dental procedures only in high-risk cardiac cohorts.",
            "monitoring_cadence": "Daily clinical exam for new murmurs or embolic signs; serial blood cultures until negative; follow-up echocardiogram prior to discharge.",
            "clinical_thresholds": "Vegetation size > 10 mm on valve leaflet or severe acute valvular regurgitation triggers urgent surgical evaluation."
        },
        "patient_plain_language": "Infective endocarditis is a bacterial infection of the heart's inner lining and valves. Bacteria enter the bloodstream from teeth, skin, or medical lines and latch onto heart valves, creating small infected clumps called vegetations.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have my repeat blood cultures turned completely negative after starting IV antibiotics?",
            "safety_question": "Do I need to take preventive antibiotics before visiting the dentist in the future?",
            "action_threshold_question": "What are the warning signs that an infected clot has traveled (like sudden weakness, vision changes, or painful finger spots)?"
        },
        "red_flags": [
            "Sudden numbness or weakness on one side of the body (stroke), acute severe breathlessness, or persistent high spiking fevers on antibiotics"
        ]
    },
    {
        "id": "DOC-CARD-104",
        "icd10": "I30.9",
        "condition": "Acute Pericarditis",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Randomized Controlled Trial",
        "source_body": "NEJM (ICAP)",
        "citation": "Imazio M et al. A Randomized Trial of Colchicine for Acute Pericarditis (ICAP). N Engl J Med. 2013;369:1522-1528.",
        "doi_or_source": "10.1056/NEJMoa1208536",
        "clinical_evidence": "In 240 patients with acute pericarditis, the addition of weight-adjusted colchicine (0.5 mg daily or BID for 3 months) to standard NSAID therapy reduced recurrence rates from 37.5% to 16.7% (relative risk reduction 56%; number needed to treat = 5; p<0.001) and reduced symptom persistence at 72 hours (19.2% vs 40.0%; p=0.001). Diagnostic criteria require at least 2 of 4: pleuritic chest pain improved by leaning forward, pericardial friction rub, PR depression/diffuse ST elevation on ECG, and new/worsening pericardial effusion.",
        "solution_protocol": {
            "non_pharmacological_targets": "Exercise restriction (avoid strenuous activity and competitive sports) until complete resolution of symptoms and normalization of CRP/ESR.",
            "monitoring_cadence": "Serum C-reactive protein (CRP) surveillance every 1-2 weeks to guide tapering of NSAIDs.",
            "clinical_thresholds": "Effusion size > 20 mm on echo, hemodynamic compromise (pulsus paradoxus > 10 mmHg), or tamponade mandates emergent pericardiocentesis."
        },
        "patient_plain_language": "Pericarditis is inflammation of the double-layered protective sac (the pericardium) that wraps around your heart. When inflamed, the two layers rub against each other like sandpaper, causing sharp chest pain that hurts worse when taking a deep breath or lying flat.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current C-reactive protein (CRP) level and is the inflammation decreasing?",
            "safety_question": "How long should I stay on colchicine and how should we gradually taper my ibuprofen or anti-inflammatory medicine?",
            "action_threshold_question": "At what point is it safe for me to resume moderate exercise and gym workouts?"
        },
        "red_flags": [
            "Sudden dizziness, severe breathlessness when sitting upright, swelling in neck veins, or feeling faint (signs of cardiac tamponade)"
        ]
    },
    {
        "id": "DOC-CARD-105",
        "icd10": "I71.4",
        "condition": "Abdominal Aortic Aneurysm (AAA)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Clinical Practice Guideline",
        "source_body": "Eur J Vasc Endovasc Surg (ESVS)",
        "citation": "Wanhainen A et al. European Society for Vascular Surgery (ESVS) 2019 Clinical Practice Guidelines on the Management of Abdominal Aorto-iliac Artery Aneurysms. Eur J Vasc Endovasc Surg. 2019;57(1):8-93.",
        "doi_or_source": "10.1016/j.ejvs.2018.09.020",
        "clinical_evidence": "ESVS and SVS guidelines recommend ultrasound screening for men aged 65-75 with any smoking history. Threshold for elective repair (EVAR or open surgical repair) is an aneurysm diameter >= 5.5 cm in men, >= 5.0 cm in women, or rapid expansion >= 1.0 cm/year. Intensive medical management includes smoking cessation (the strongest modifiable risk factor for expansion and rupture), high-intensity statin therapy, and antiplatelet therapy for systemic atherosclerotic risk reduction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate, complete tobacco cessation; avoidance of extreme isometric heavy weightlifting; moderate systolic BP control (<130/80 mmHg).",
            "monitoring_cadence": "Duplex ultrasound surveillance: every 3 years for 3.0-3.9 cm; annually for 4.0-4.9 cm; every 3-6 months for 5.0-5.4 cm.",
            "clinical_thresholds": "Aortic diameter ≥ 5.5 cm in men or ≥ 5.0 cm in women triggers vascular surgical consultation for repair."
        },
        "patient_plain_language": "An abdominal aortic aneurysm is a bulge or ballooning in the main blood vessel (the aorta) that carries blood through your belly. It happens when the artery wall weakens over time, often due to high blood pressure and smoking, much like a weak spot on a bicycle tire.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact diameter of my aneurysm in centimeters and how fast has it grown since my last scan?",
            "safety_question": "What is my optimal blood pressure target to prevent excess stress on the aorta wall?",
            "action_threshold_question": "At what size measurement will we discuss repair options like a stent graft (EVAR) versus surgery?"
        },
        "red_flags": [
            "Sudden severe, tearing pain in the lower back, abdomen, or flank, accompanied by lightheadedness, cold sweat, or collapse (Aortic Rupture Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-106",
        "icd10": "I95.1",
        "condition": "Neurogenic Orthostatic Hypotension (nOH)",
        "specialty": "Cardiovascular",
        "organ_system": "Nervous & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Consensus Statement & Meta-Analysis",
        "source_body": "Clin Auton Res (AAS/EFNS)",
        "citation": "Freeman R et al. Consensus statement on the definition of orthostatic hypotension, neurally mediated syncope and the postural tachycardia syndrome. Clin Auton Res. 2011;21(2):69-72.",
        "doi_or_source": "10.1007/s10286-011-0119-5",
        "clinical_evidence": "Diagnostic consensus defines orthostatic hypotension as a sustained reduction of systolic blood pressure of at least 20 mmHg or diastolic blood pressure of at least 10 mmHg within 3 minutes of standing or head-up tilt. In neurogenic forms (Parkinson's, MSA, diabetic autonomic neuropathy), blunted reflex tachycardia (ratio of delta HR to delta SBP <0.5 bpm/mmHg) reflects sympathetic failure. Pharmacotherapy includes droxidopa, midodrine, or fludrocortisone titrated against supine hypertension.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bolus water drinking (500 mL water 30 min before rising); dietary sodium expansion (6-10 g salt/day unless contraindicated); thigh-high compression stockings (30-40 mmHg); abdominal binder.",
            "monitoring_cadence": "Seated and 3-minute standing blood pressure measurements at each visit; evening supine BP checks to screen for supine hypertension.",
            "clinical_thresholds": "Standing systolic BP maintained > 90 mmHg without symptoms while keeping supine nocturnal BP < 180/110 mmHg."
        },
        "patient_plain_language": "Orthostatic hypotension means your blood pressure drops sharply when you stand up. Normally, nerve reflexes squeeze your leg blood vessels like elastic bands to keep blood flowing up to your brain; in this condition, those nerve reflexes are sluggish, leaving blood pooled in your legs.",
        "doctor_consultation_checklist": {
            "parameter_question": "What are my exact lying-down versus standing-up blood pressure readings?",
            "safety_question": "Are any of my current blood pressure or prostate medications making my standing dizziness worse?",
            "action_threshold_question": "What physical counter-maneuvers (like leg crossing or calf clenching) can I use immediately when feeling faint?"
        },
        "red_flags": [
            "Loss of consciousness with falls or head trauma, chest pain on standing, or standing systolic blood pressure falling below 70 mmHg"
        ]
    },
    {
        "id": "DOC-CARD-107",
        "icd10": "G90.a",
        "condition": "Postural Orthostatic Tachycardia Syndrome (POTS)",
        "specialty": "Cardiovascular",
        "organ_system": "Nervous & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Heart Rhythm Society Expert Consensus",
        "source_body": "Heart Rhythm (HRS)",
        "citation": "Sheldon RS et al. 2015 Heart Rhythm Society Expert Consensus Statement on the Diagnosis and Treatment of Postural Tachycardia Syndrome, Inappropriate Sinus Tachycardia, and Vasovagal Syncope. Heart Rhythm. 2015;12(6):e41-e63.",
        "doi_or_source": "10.1016/j.hrthm.2015.03.029",
        "clinical_evidence": "HRS consensus criteria require a sustained heart rate increase of >= 30 bpm (or >= 40 bpm in individuals aged 12-19) within 10 minutes of standing or tilt-table testing, in the absence of orthostatic hypotension, accompanied by chronic orthostatic symptoms for >= 3 months. First-line therapy centers on non-pharmacological intravascular volume expansion: 2-3 L oral fluids daily, 8-10 g sodium daily, structured recumbent/rowing exercise training. Pharmacologic adjuncts include fludrocortisone, propranolol/bisoprolol, pyridostigmine, and midodrine.",
        "solution_protocol": {
            "non_pharmacological_targets": "High fluid intake (2.5-3.0 L/day) and high sodium intake (8-10 g/day); waist-high compression garments (20-30 mmHg); Levine semi-recumbent progressive aerobic exercise protocol.",
            "monitoring_cadence": "10-minute active stand test ('NASA lean test') every 3-6 months to assess hemodynamic compensation.",
            "clinical_thresholds": "Postural heart rate increase < 30 bpm during sustained standing indicates therapeutic stabilization."
        },
        "patient_plain_language": "POTS is a condition where your body has trouble balancing blood flow when you are upright. When you stand, blood pools in your legs and belly, and your heart races frantically trying to pump blood back up to your brain, making you feel lightheaded, exhausted, and shaky.",
        "doctor_consultation_checklist": {
            "parameter_question": "How much daily salt and water should I be consuming to maintain my blood volume?",
            "safety_question": "Could a low-dose beta-blocker or midodrine help stabilize my heart rate without dropping my blood pressure too low?",
            "action_threshold_question": "What structured recumbent exercise program (like rowing or recumbent cycling) do you recommend to rebuild my stamina?"
        },
        "red_flags": [
            "Recurrent syncope (blackouts) with head injury, prolonged unresponsiveness, or new chest tightness accompanied by severe shortness of breath"
        ]
    },
    {
        "id": "DOC-CARD-108",
        "icd10": "I73.00",
        "condition": "Raynaud's Phenomenon",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory & Rheumatologic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & Practice Guideline",
        "source_body": "NEJM Review",
        "citation": "Wigley FM, Flavahan NA. Raynaud's Phenomenon. N Engl J Med. 2016;375(6):556-565.",
        "doi_or_source": "10.1056/NEJMcp1507631",
        "clinical_evidence": "Primary Raynaud's (idiopathic vasospasm) is distinguished from secondary Raynaud's (underlying connective tissue disease such as systemic sclerosis, SLE) by normal nailfold capillaroscopy, symmetric attacks, absence of digital ulceration/necrosis, and negative antinuclear antibody (ANA) serology. First-line pharmacotherapy consists of dihydropyridine calcium channel blockers (nifedipine 30-60 mg daily or amlodipine 5-10 mg daily), reducing attack frequency by 33% and severity by 35% in meta-analyses. Phosphodiesterase-5 inhibitors (sildenafil) are effective for refractory symptoms or digital ulcers.",
        "solution_protocol": {
            "non_pharmacological_targets": "Core and extremity cold avoidance (layering, thermal mittens, hand warmers); avoidance of emotional stress triggers; complete avoidance of nicotine/smoking and sympathomimetic decongestants.",
            "monitoring_cadence": "Annual examination of digital pulp for ischemic pits or ulcers; baseline ANA and nailfold capillaroscopy screening.",
            "clinical_thresholds": "Digital tissue loss, persistent cyanosis >2 hours, or nailfold capillary drop-out mandates secondary autoimmune disease workup."
        },
        "patient_plain_language": "Raynaud's phenomenon is an over-reaction of the tiny blood vessels in your fingers and toes to cold temperatures or stress. The vessels spasm shut temporarily, turning your fingers white, then blue, and finally red and throbbing as blood rushes back in.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I have primary Raynaud's or are there signs of a secondary autoimmune condition like scleroderma or lupus?",
            "safety_question": "Are any of my migraine medications or nasal decongestants causing my blood vessels to clamp down?",
            "action_threshold_question": "Would a gentle blood-vessel relaxing medication like nifedipine help during winter months?"
        },
        "red_flags": [
            "Severe persistent finger pain with black discoloration or open sores (digital ulcers / gangrene), or cold fingers that fail to re-warm after 2 hours"
        ]
    },
    {
        "id": "DOC-CARD-109",
        "icd10": "I49.5",
        "condition": "Sick Sinus Syndrome (Bradycardia-Tachycardia)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACC/AHA/HRS Clinical Practice Guideline",
        "source_body": "Circulation (ACC/AHA/HRS)",
        "citation": "Kusumoto FM et al. 2018 ACC/AHA/HRS Guideline on the Evaluation and Management of Patients With Bradycardia and Cardiac Conduction Delay. Circulation. 2019;140(8):e382-e482.",
        "doi_or_source": "10.1161/CIR.0000000000000628",
        "clinical_evidence": "ACC/AHA/HRS guidelines establish that permanent pacemaker implantation (dual-chamber DDDR preferred over single-chamber) is a Class I recommendation for documented symptomatic sinus node dysfunction (sinus pauses >3 seconds, chronotropic incompetence, or symptomatic bradycardia). In tachycardia-bradycardia syndrome, pacing prevents post-conversion pauses, enabling safe use of AV-nodal blocking agents (beta-blockers) and anticoagulation for concurrent atrial fibrillation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Audit and discontinuation of non-essential negative chronotropic medications (beta-blockers, non-DHP CCBs, antiarrhythmics, digoxin); avoidance of vagal triggers.",
            "monitoring_cadence": "14-day continuous ambulatory cardiac patch monitor to correlate dizziness/syncope with documented sinus arrest.",
            "clinical_thresholds": "Symptomatic sinus pause ≥ 3.0 seconds or waking heart rate < 40 bpm with syncope triggers permanent pacing indication."
        },
        "patient_plain_language": "Sick sinus syndrome is a problem with your heart's natural electrical pacemaker (the sinus node). Over time, the pacemaker cells can wear out, causing your heart to beat too slowly, pause for several seconds, or alternate between sluggish beats and sudden racing spells.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my longest pause and lowest heart rate recorded on my cardiac Holter monitor?",
            "safety_question": "Are any of my blood pressure or heart medications contributing to my slow heart rate?",
            "action_threshold_question": "At what point should we schedule a permanent pacemaker to protect against fainting?"
        },
        "red_flags": [
            "Sudden fainting with no warning, heart pausing longer than 3 seconds with dizziness, or crushing chest pain with a heart rate below 35 bpm"
        ]
    },
    {
        "id": "DOC-CARD-110",
        "icd10": "I47.1",
        "condition": "Supraventricular Tachycardia (AVNRT / AVRT)",
        "specialty": "Cardiovascular",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACC/AHA/HRS Practice Guideline",
        "source_body": "Circulation (ACC/AHA/HRS)",
        "citation": "Page RL et al. 2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia. Circulation. 2016;133(14):e506-e574.",
        "doi_or_source": "10.1161/CIR.0000000000000311",
        "clinical_evidence": "Clinical guidelines recommend modified Valsalva maneuver (REVERT protocol: 15-second strain at 40 mmHg followed by immediate supine repositioning and 45-degree passive leg elevation for 15 seconds) as first-line bedside therapy, achieving 43% cardioversion vs 17% standard Valsalva (p<0.0001). Intravenous adenosine (6 mg rapid bolus, then 12 mg if needed) is first-line pharmacologic cardioversion. Catheter ablation is Class I curative therapy with >95% success and <1% major complication rate.",
        "solution_protocol": {
            "non_pharmacological_targets": "Instruction in modified Valsalva maneuver for acute home episodes; limitation of excessive caffeine, energy drinks, alcohol binges, and pseudoephedrine.",
            "monitoring_cadence": "12-lead ECG during acute palpitations; electrophysiology (EP) consultation for recurrent episodes.",
            "clinical_thresholds": "Symptomatic recurrent SVT refractory to or intolerant of medical prophylaxis warrants catheter ablation."
        },
        "patient_plain_language": "Supraventricular tachycardia (SVT) is a condition where an extra electrical wire or short-circuit in your heart causes it to suddenly switch into hyper-drive, racing at 150 to 220 beats per minute, before suddenly clicking back to normal.",
        "doctor_consultation_checklist": {
            "parameter_question": "What exact type of SVT showed up on my ECG (such as AVNRT or WPW syndrome)?",
            "safety_question": "Can you teach me the modified Valsalva leg-raise technique to stop an episode at home safely?",
            "action_threshold_question": "Would a minor catheter ablation procedure cure this permanently so I don't need daily medications?"
        },
        "red_flags": [
            "Racing heart rate > 180 bpm accompanied by chest pressure, fainting, extreme breathlessness, or blue lips"
        ]
    },
    {
        "id": "DOC-CARD-111",
        "icd10": "I27.0",
        "condition": "Pulmonary Arterial Hypertension (PAH)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ESC/ERS Clinical Practice Guideline",
        "source_body": "Eur Heart J (ESC/ERS)",
        "citation": "Humbert M et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. Eur Heart J. 2022;43(38):3618-3731.",
        "doi_or_source": "10.1093/eurheartj/ehac237",
        "clinical_evidence": "Hemodynamic definition updated to mean pulmonary arterial pressure (mPAP) > 20 mmHg with pulmonary capillary wedge pressure <= 15 mmHg and pulmonary vascular resistance (PVR) > 2 Wood units. Initial upfront oral dual combination therapy (ERA + PDE5i: macitentan/tadalafil or ambrisentan/tadalafil) demonstrated significant reduction in clinical failure events (AMBITION trial, HR 0.50, p<0.001). Parenteral prostacyclin analogues (epoprostenol) are mandatory for high-risk patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Supervised pulmonary rehabilitation; sodium restriction (<2,000 mg/day) for right ventricular volume overload; annual influenza/pneumococcal/COVID vaccinations; pregnancy avoidance due to high maternal mortality.",
            "monitoring_cadence": "Comprehensive multiparameter risk stratification (6-minute walk distance, WHO functional class, NT-proBNP, echo) every 3-6 months.",
            "clinical_thresholds": "Right ventricular dysfunction, syncope, or WHO Functional Class IV status designates high-risk category mandating parenteral prostanoid escalation."
        },
        "patient_plain_language": "Pulmonary arterial hypertension means blood pressure inside the arteries of your lungs is dangerously high. It is different from regular arm blood pressure: the small blood vessels in your lungs become stiff and narrow, forcing the right side of your heart to work overtime to push blood through.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my 6-minute walk distance and current NT-proBNP heart strain score?",
            "safety_question": "Am I on upfront combination therapy to target multiple biological pathways in my lung vessels?",
            "action_threshold_question": "What are the earliest signs that the right side of my heart is straining (like swollen ankles or stomach fullness)?"
        },
        "red_flags": [
            "Fainting (syncope) during routine walking, acute severe shortness of breath at rest, coughing up blood, or blue discoloration of lips"
        ]
    },
    {
        "id": "DOC-CARD-112",
        "icd10": "J47.9",
        "condition": "Bronchiectasis (Non-Cystic Fibrosis)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Respiratory Society Clinical Guideline",
        "source_body": "Eur Respir J (ERS)",
        "citation": "Polverino E et al. European Respiratory Society guidelines for the management of adult bronchiectasis. Eur Respir J. 2017;50(3):1700629.",
        "doi_or_source": "10.1183/13993003.00629-2017",
        "clinical_evidence": "Diagnostic confirmation requires high-resolution CT (HRCT) demonstrating bronchoarterial ratio > 1.0 (signet-ring sign) and lack of bronchial tapering. Airway clearance techniques (oscillating PEP devices, active cycle of breathing) twice daily significantly improve sputum clearance and quality of life. For patients with >=3 exacerbations/year or chronic Pseudomonas aeruginosa colonization, long-term macrolide maintenance (azithromycin 250-500 mg 3x/week) reduces exacerbations by over 50% (EMBRACE, BAT trials).",
        "solution_protocol": {
            "non_pharmacological_targets": "Twice-daily airway clearance physiotherapy with oscillating positive expiratory pressure (OPEP); nebulized hypertonic saline (3% or 7%) to hydrate secretions; pulmonary rehabilitation.",
            "monitoring_cadence": "Serial sputum microbiologic cultures at every routine visit and acute exacerbation to detect Pseudomonas aeruginosa early.",
            "clinical_thresholds": "Three or more infectious exacerbations per year triggers indication for long-term macrolide prophylaxis."
        },
        "patient_plain_language": "Bronchiectasis is a condition where the airways in your lungs have become abnormally widened, scarred, and flabby, like stretched-out elastic bands. Because they lose their shape, thick mucus pools inside, making it hard to clear bacteria and leading to repeat lung infections.",
        "doctor_consultation_checklist": {
            "parameter_question": "What bacteria showed up in my latest sputum culture, and does it require targeted inhaled antibiotics?",
            "safety_question": "Have I had an ECG or hearing check before starting long-term azithromycin antibiotic therapy?",
            "action_threshold_question": "How can I tell the difference between my baseline daily cough and a true bacterial lung infection that needs antibiotics?"
        },
        "red_flags": [
            "Coughing up fresh blood (hemoptysis) greater than 50 mL, severe sudden breathlessness, or high fever with confusion"
        ]
    },
    {
        "id": "DOC-CARD-113",
        "icd10": "D86.0",
        "condition": "Pulmonary Sarcoidosis",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Thoracic Society Clinical Guideline",
        "source_body": "Am J Respir Crit Care Med (ATS)",
        "citation": "Crouser ED et al. Diagnosis and Detection of Sarcoidosis. An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;201(8):e26-e51.",
        "doi_or_source": "10.1164/rccm.202002-0251ST",
        "clinical_evidence": "ATS guidelines require consistent clinical and radiographic presentation, noncaseating granulomas on histopathology (bronchoscopy with EBUS-TBNA preferred), and exclusion of alternate causes (fungal/mycobacterial infections, berylliosis). First-line therapy for organ-threatening disease (progressive pulmonary decline, cardiac or neurosarcoidosis, hypercalcemia) is oral prednisone (20-40 mg daily tapered over 6-12 months). Methotrexate (10-20 mg weekly) or azathioprine serves as steroid-sparing maintenance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Baseline and annual screening for cardiac sarcoidosis (ECG, Holter, cardiac MRI if symptomatic) and ocular uveitis (slit-lamp exam); avoidance of supplemental vitamin D if hypercalcemic.",
            "monitoring_cadence": "Pulmonary function tests (FVC, DLCO) and serum calcium/ACE levels every 3-6 months during active therapy.",
            "clinical_thresholds": "Decline in FVC ≥ 10% or DLCO ≥ 15%, or cardiac conduction abnormalities triggers immediate systemic immunosuppression."
        },
        "patient_plain_language": "Sarcoidosis is an immune system condition where your white blood cells cluster together to form microscopic inflammatory lumps called granulomas, most often in the lungs and lymph nodes. Think of your immune system setting off false fire alarms and leaving small clumps of inflammatory tissue behind.",
        "doctor_consultation_checklist": {
            "parameter_question": "How are my lung function numbers (FVC and DLCO oxygen diffusion) trending compared to baseline?",
            "safety_question": "Have we thoroughly checked my heart and eyes to make sure sarcoid granulomas haven't formed there?",
            "action_threshold_question": "What is our plan to taper steroids and transition to a steroid-sparing medicine to protect my bones and blood sugar?"
        },
        "red_flags": [
            "Sudden heart palpitations, unexplained fainting (heart block / ventricular arrhythmia), sudden vision loss, or rapid progressive breathlessness"
        ]
    },
    {
        "id": "DOC-CARD-114",
        "icd10": "J67.9",
        "condition": "Chronic Hypersensitivity Pneumonitis (HP)",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATS/JRS/ALAT Clinical Practice Guideline",
        "source_body": "Am J Respir Crit Care Med (ATS)",
        "citation": "Raghu G et al. Diagnosis of Hypersensitivity Pneumonitis in Adults. An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;202(3):e36-e69.",
        "doi_or_source": "10.1164/rccm.202005-2032ST",
        "clinical_evidence": "ATS/JRS/ALAT guidelines distinguish non-fibrotic vs fibrotic HP using high-resolution CT (three-density pattern / headcheese sign, mosaic attenuation, centrilobular ground glass) and bronchoalveolar lavage (lymphocytosis >20-30%). Identification and complete antigen avoidance (bird feathers/down, household molds, hot tubs, farming antigens) is the cornerstone of management. In progressive fibrotic HP, nintedanib slows FVC decline by 57% (INBUILD trial, p<0.001), while systemic steroids and mycophenolate mofetil target non-fibrotic inflammation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Meticulous remediation or removal of triggering organic antigens (feather duvets, pet birds, indoor mold remediation, occupational respirators).",
            "monitoring_cadence": "PFTs (FVC, DLCO) every 3-6 months; annual HRCT to detect progressive fibrotic changes.",
            "clinical_thresholds": "Progression of lung fibrosis despite complete antigen removal warrants evaluation for antifibrotic therapy (nintedanib)."
        },
        "patient_plain_language": "Hypersensitivity pneumonitis is an allergic reaction deep inside the air sacs of your lungs caused by repeatedly breathing in microscopic organic dust, such as mold spores, bird droppings, or down feathers. Over time, this chronic allergy can cause stiff scar tissue to form in your lungs.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my lung scan show reversible inflammation or permanent scarring (fibrosis)?",
            "safety_question": "What home or workplace antigens (down pillows, moldy AC units, birds) should I thoroughly remove?",
            "action_threshold_question": "Would an antifibrotic medication help protect my lung capacity from declining?"
        },
        "red_flags": [
            "Severe oxygen desaturation below 88% on room air, blue lips or fingers, or severe progressive breathlessness when walking a few steps"
        ]
    },
    {
        "id": "DOC-CARD-115",
        "icd10": "J90",
        "condition": "Pleural Effusion & Empyema",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: British Thoracic Society Clinical Guideline",
        "source_body": "Thorax (BTS)",
        "citation": "Davies HE et al. Management of pleural infection in adults: British Thoracic Society Pleural Disease Guideline 2010. Thorax. 2010;65(Suppl 2):ii41-ii53.",
        "doi_or_source": "10.1136/thx.2010.137000",
        "clinical_evidence": "Diagnostic thoracentesis with Light's criteria differentiates transudate (heart failure, cirrhosis) from exudate (infection, malignancy). Complicated parapneumonic effusion and empyema are defined by pleural fluid pH < 7.20, glucose < 60 mg/dL, elevated LDH (>1,000 U/L), or positive Gram stain/culture. Immediate intercostal chest tube drainage and parenteral broad-spectrum antibiotics covering anaerobes and Gram-negative bacilli are mandatory. Intrapleural tissue plasminogen activator (tPA) plus DNase (MIST-2 trial) significantly improves fluid drainage and reduces surgical referral by 77% (p=0.005).",
        "solution_protocol": {
            "non_pharmacological_targets": "Bedside thoracic ultrasound guidance for all pleural procedures to minimize pneumothorax risk; chest physiotherapy and incentive spirometry.",
            "monitoring_cadence": "Daily clinical and drainage volume assessment; serial chest radiographs or ultrasound until lung re-expansion.",
            "clinical_thresholds": "Pleural fluid pH < 7.20 or frankly purulent fluid triggers immediate mandatory tube thoracostomy drainage."
        },
        "patient_plain_language": "A pleural effusion is an abnormal buildup of fluid in the space between your lung and your chest wall, like water pooling around a sponge. When bacteria infect this fluid, it forms a pocket of pus called an empyema, which compresses the lung and makes breathing painful and difficult.",
        "doctor_consultation_checklist": {
            "parameter_question": "What did the lab tests show on my pleural fluid (is it an infection, heart fluid, or something else)?",
            "safety_question": "Do I need a small drainage tube placed with ultrasound guidance to remove the fluid completely?",
            "action_threshold_question": "How long will I need IV antibiotics to ensure the lung infection is completely cured?"
        },
        "red_flags": [
            "Severe sharp chest pain with high spiking fever, inability to catch breath while sitting still, or coughing up foul-smelling sputum"
        ]
    },
    {
        "id": "DOC-CARD-116",
        "icd10": "J20.9",
        "condition": "Acute Bronchitis",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Meta-Analysis",
        "source_body": "Cochrane Database Syst Rev",
        "citation": "Smith SM et al. Antibiotics for acute bronchitis. Cochrane Database Syst Rev. 2017;6(6):CD000245.",
        "doi_or_source": "10.1002/14651858.CD000245.pub4",
        "clinical_evidence": "Over 90% of acute bronchitis cases in immunocompetent adults are caused by respiratory viruses (rhinovirus, coronavirus, influenza, RSV, parainfluenza). Cochrane meta-analysis of 17 RCTs (n=5,099) established that routine antibiotic therapy provides no clinically meaningful benefit (reducing cough duration by only 0.5 days) while doubling adverse drug events (nausea, diarrhea, rash; OR 1.20) and driving antimicrobial resistance. Routine guidelines (CDC, NICE, ACP) recommend symptomatic therapy alone: honey, guaifenesin, short-acting beta-agonists only if wheezing present, and patient education on natural 2-3 week cough duration.",
        "solution_protocol": {
            "non_pharmacological_targets": "Adequate hydration; warm tea with honey (demonstrated antitussive benefit in clinical trials); cool-mist humidifier; avoidance of tobacco smoke.",
            "monitoring_cadence": "Re-evaluation if fever persists >3 days, dyspnea develops, or cough lasts >3 weeks.",
            "clinical_thresholds": "Vital sign abnormalities (HR > 100, RR > 24, temp > 38°C) or focal lung crackles warrant chest X-ray to rule out pneumonia."
        },
        "patient_plain_language": "Acute bronchitis is a temporary viral infection of the large breathing tubes in your lungs, usually coming after a common cold. Because it is almost always caused by viruses, antibiotics will not cure it, but soothing remedies and rest allow the airway lining to heal over 2 to 3 weeks.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are my oxygen level, heart rate, and temperature normal, confirming this is just bronchitis and not pneumonia?",
            "safety_question": "Why are antibiotics not recommended for viral bronchitis, and what over-the-counter remedies will soothe my cough safely?",
            "action_threshold_question": "What warning signs should prompt me to come back for a chest X-ray?"
        },
        "red_flags": [
            "Fever above 38.5°C (101.3°F) lasting over 3 days, coughing up rust-colored sputum, shortness of breath at rest, or oxygen saturation below 94%"
        ]
    },
    {
        "id": "DOC-CARD-117",
        "icd10": "R05.3",
        "condition": "Chronic Refractory Cough",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Respiratory Society Clinical Practice Guideline",
        "source_body": "Eur Respir J (ERS)",
        "citation": "Morice AH et al. ERS guidelines on the diagnosis and treatment of chronic cough in adults and children. Eur Respir J. 2020;55(1):1901136.",
        "doi_or_source": "10.1183/13993003.01136-2019",
        "clinical_evidence": "Chronic cough is defined as daily cough lasting > 8 weeks. Systematic guideline evaluation rules out the 'triad' of upper airway cough syndrome, cough-variant asthma (bronchoprovocation test), and non-acid reflux before diagnosing cough hypersensitivity syndrome. In unexplained or refractory chronic cough, targeted neuromodulators (low-dose slow-release morphine 5-10 mg BID, gabapentin 300-900 mg daily, speech pathology cough suppression therapy) achieve significant reductions in cough frequency and Leicester Cough Questionnaire improvement.",
        "solution_protocol": {
            "non_pharmacological_targets": "Speech pathology-directed cough suppression therapy (respiratory retraining, hard swallowing, voluntary cough suppression maneuvers); avoidance of thermal and irritant cough triggers.",
            "monitoring_cadence": "Validated cough severity scoring (Leicester Cough Questionnaire or visual analogue scale) every 4-8 weeks.",
            "clinical_thresholds": "Cough lasting >8 weeks with normal chest X-ray and negative methacholine challenge qualifies as chronic cough hypersensitivity."
        },
        "patient_plain_language": "Chronic cough is a cough that lingers for more than 8 weeks after any initial infection has cleared. Often, the nerves in your throat and airways become hyper-sensitive—like a car alarm that goes off when a gentle breeze blows—triggering sudden coughing fits from talking, laughing, or cold air.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have we ruled out hidden asthma, acid reflux, and nasal drip as causes of my chronic cough?",
            "safety_question": "Could specialized cough-suppression speech therapy or a low-dose nerve-calming medication help quiet my cough reflex?",
            "action_threshold_question": "Could any blood pressure medications I take (such as ACE inhibitors like lisinopril) be triggering this cough?"
        },
        "red_flags": [
            "Coughing up blood (hemoptysis), unintentional weight loss, voice hoarseness lasting >3 weeks, or persistent night sweats"
        ]
    },
    {
        "id": "DOC-CARD-118",
        "icd10": "J61",
        "condition": "Asbestosis & Occupational Pneumoconiosis",
        "specialty": "Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Consensus Statement (Helsinki Criteria)",
        "source_body": "Scand J Work Environ Health (Helsinki)",
        "citation": "Wolff H et al. Asbestos, asbestosis, and cancer, the Helsinki criteria for attribution 2014: recommendations. Scand J Work Environ Health. 2015;41(1):5-15.",
        "doi_or_source": "10.5271/sjweh.3462",
        "clinical_evidence": "Diagnostic attribution per Helsinki criteria requires documented occupational latency (typically >15-20 years from first exposure), high-resolution CT demonstration of bilateral basilar interstitial fibrosis, subpleural curvilinear lines, dot-like opacities, and pleural plaques. PFTs demonstrate a classic restrictive ventilatory defect with reduced DLCO. Tobacco smoking acts synergistically, increasing lung cancer risk by up to 50-fold in asbestos-exposed workers. Management focuses on rigorous smoking cessation, prompt treatment of respiratory infections, and screening for pleural mesothelioma and bronchogenic carcinoma.",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive, absolute tobacco cessation; occupational exposure elimination; annual influenza and pneumococcal vaccination series; pulmonary rehabilitation.",
            "monitoring_cadence": "Annual spirometry and DLCO; low-dose CT chest screening every 1-2 years for early lung cancer detection in high-risk cohorts.",
            "clinical_thresholds": "Resting or exertional room-air oxygen saturation ≤ 88% qualifies for supplemental ambulatory oxygen therapy."
        },
        "patient_plain_language": "Asbestosis is scarring of the lung tissue caused by inhaling microscopic asbestos mineral fibers years ago at work. The body cannot dissolve the tiny needle-like fibers, so the lungs form stiff fibrous scar tissue around them, making the lungs less elastic and harder to inflate.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current lung volume (FVC) and oxygen diffusion capacity (DLCO)?",
            "safety_question": "Should I undergo regular low-dose CT lung cancer screening scans because of my past asbestos exposure?",
            "action_threshold_question": "Do I qualify for supplemental oxygen to help me stay active and breathe easier during daily walks?"
        },
        "red_flags": [
            "New or worsening coughing up blood, sudden unilateral chest pain with fluid buildup (pleural effusion), or rapid weight loss"
        ]
    },
    {
        "id": "DOC-CARD-119",
        "icd10": "E10.9",
        "condition": "Type 1 Diabetes Mellitus",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ADA/EASD Consensus Report",
        "source_body": "Diabetes Care (ADA/EASD)",
        "citation": "Holt RIG et al. The Management of Type 1 Diabetes in Adults. A Consensus Report by ADA and EASD. Diabetes Care. 2021;44(11):2589-2625.",
        "doi_or_source": "10.2337/dci21-0043",
        "clinical_evidence": "Autoimmune destruction of pancreatic beta cells results in absolute insulin deficiency, requiring lifelong exogenous insulin replacement. Multiple daily injections (MDI: basal long-acting degludec/glargine + rapid-acting prandial aspart/lispro) or automated insulin delivery (AID / hybrid closed-loop pump systems) are standard of care. Continuous glucose monitoring (CGM) is a Class 1 recommendation, targeting Time in Range (TIR 70-180 mg/dL) > 70% and Time Below Range (<70 mg/dL) < 4%, reducing severe hypoglycemia and microvascular complications (DCCT/EDIC cohorts).",
        "solution_protocol": {
            "non_pharmacological_targets": "Accurate carbohydrate counting (insulin-to-carbohydrate ratios); structured aerobic and resistance exercise planning with pre-workout glucose checks; medical alert identification.",
            "monitoring_cadence": "Continuous glucose monitoring (CGM) sensor wear; HbA1c every 3 months; annual microalbuminuria, lipid panel, dilated eye exam, and comprehensive foot exam.",
            "clinical_thresholds": "Target Time in Range (70-180 mg/dL) > 70% with Time Below Range (<70 mg/dL) < 4%."
        },
        "patient_plain_language": "Type 1 diabetes is an autoimmune condition where your body's immune system mistakenly attacks the insulin-producing factory cells in your pancreas. Because your body makes zero insulin, you must supply it daily through injections or a pump to allow sugar to enter your cells for energy.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Time in Range percentage (70-180 mg/dL) on my continuous glucose monitor?",
            "safety_question": "Do my family members or coworkers know how to use emergency nasal glucagon (Baqsimi) if I have severe low blood sugar?",
            "action_threshold_question": "Would I be a good candidate for a hybrid closed-loop insulin pump to automate my overnight insulin doses?"
        },
        "red_flags": [
            "Blood glucose > 250 mg/dL with positive urine/blood ketones, nausea, vomiting, rapid deep breathing, or fruity breath (Diabetic Ketoacidosis Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-120",
        "icd10": "E11.10",
        "condition": "Diabetic Ketoacidosis (DKA)",
        "specialty": "Endocrinology",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ADA Consensus Clinical Practice Guideline",
        "source_body": "Diabet Med (JBDS/ADA)",
        "citation": "Dhatariya KK et al. Management of hyperosmolar hyperglycaemic state and diabetic ketoacidosis in adults: a consensus guideline. Diabet Med. 2023;40(4):e15005.",
        "doi_or_source": "10.1111/dme.15005",
        "clinical_evidence": "Diagnostic triad: Hyperglycemia (blood glucose > 250 mg/dL), ketosis (beta-hydroxybutyrate > 3.0 mmol/L or moderate/large urine ketones), and metabolic acidosis (arterial/venous pH < 7.30, serum bicarbonate < 18 mEq/L, anion gap > 12). Protocolized management mandates IV fluid resuscitation (0.9% NaCl 1,000 mL/hr initially), fixed-rate continuous IV insulin infusion (0.1 units/kg/hr), and strict potassium replacement (adding 20-30 mEq K+ per liter of IV fluid once K+ < 5.2 mEq/L) to prevent lethal hypokalemic arrhythmias. Insulin is withheld only if serum potassium is < 3.3 mEq/L until repleted.",
        "solution_protocol": {
            "non_pharmacological_targets": "'Sick-day rules' education: never discontinue basal insulin during illness; frequent blood glucose and ketone testing every 2-4 hours; aggressive oral hydration.",
            "monitoring_cadence": "Hourly capillary glucose checks, venous blood gas, electrolytes, and anion gap calculation every 2-4 hours in ICU/step-down unit.",
            "clinical_thresholds": "Resolution criteria: Blood glucose < 200 mg/dL, venous pH > 7.30, bicarbonate ≥ 18 mEq/L, and normalized anion gap (≤12)."
        },
        "patient_plain_language": "Diabetic ketoacidosis (DKA) is a life-threatening medical emergency where the body has so little insulin that it cannot burn sugar for fuel. Instead, it breaks down body fat at an extreme speed, flooding the bloodstream with toxic acids called ketones.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my anion gap and beta-hydroxybutyrate blood ketone level?",
            "safety_question": "Are my potassium levels being closely monitored and replaced before starting or increasing insulin?",
            "action_threshold_question": "What exact 'sick-day rules' should I follow when sick with a stomach flu to prevent DKA from ever happening again?"
        },
        "red_flags": [
            "Persistent vomiting with inability to keep fluids down, confusion, deep rapid gasping breaths (Kussmaul breathing), or blood ketones > 3.0 mmol/L"
        ]
    }
]