"""
part3_neuro_renal.py
"""

PART_3_DISEASES = [
    {
        "id": "DOC-CARD-141",
        "icd10": "G45.9",
        "condition": "Transient Ischemic Attack (TIA)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA Guideline for the Prevention of Stroke",
        "source_body": "Stroke",
        "citation": "Kleindorfer DO et al. 2021 Guideline for the Prevention of Stroke in Patients With Stroke and Transient Ischemic Attack: A Guideline From the AHA/ASA. Stroke. 2021;52(7):e364-e467.",
        "doi_or_source": "10.1161/STR.0000000000000375",
        "clinical_evidence": "A TIA is defined neurobiologically as a transient episode of neurological dysfunction caused by focal brain, spinal cord, or retinal ischemia, without acute tissue infarction on diffusion-weighted MRI (DWI). ABCD2 score (Age ≥60, BP ≥140/90, Clinical features [unilateral weakness, speech impairment], Duration, Diabetes) stratifies 90-day stroke risk. Landmark POINT and CHANCE randomized trials demonstrated that high-risk TIA (ABCD2 ≥ 4) or minor stroke requires dual antiplatelet therapy (DAPT: aspirin 81 mg + clopidogrel 75 mg daily after loading doses) initiated within 24 hours and continued for 21 days (POINT trial: major ischemic events reduced by 25%, HR 0.75, 95% CI 0.59-0.95; CHANCE trial: HR 0.68), followed by single antiplatelet monotherapy long-term to minimize major bleeding risk.",
        "solution_protocol": {
            "non_pharmacological_targets": "Emergent diagnostic evaluation within 24 hours: brain MRI with DWI, vascular imaging (CTA/MRA of head and neck), 12-lead ECG, telemetry/Holter to rule out atrial fibrillation; Mediterranean diet and blood pressure < 130/80 mmHg.",
            "monitoring_cadence": "Extended cardiac rhythm monitoring (at least 2-4 weeks via patch/event monitor) if stroke mechanism is cryptogenic; follow-up neurology consultation at 30 days.",
            "clinical_thresholds": "ABCD2 score ≥ 4 indicates high early stroke recurrence risk, mandating hospitalization and 21-day DAPT."
        },
        "patient_plain_language": "A TIA (transient ischemic attack), sometimes called a 'warning stroke' or 'mini-stroke', occurs when blood flow to a part of your brain is briefly blocked. The symptoms disappear within minutes to hours, but it is a critical warning sign that a major, permanent stroke could happen soon unless treated immediately.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my ABCD2 risk score and did my brain MRI show any signs of permanent stroke tissue damage?",
            "safety_question": "Am I starting dual antiplatelet therapy (aspirin plus clopidogrel) for the first 21 days, and when do I switch back to a single pill?",
            "action_threshold_question": "Did my ultrasound or CT angiogram reveal any significant narrowing in my carotid neck arteries?"
        },
        "red_flags": [
            "Sudden facial droop, arm weakness or numbness on one side, slurred speech, sudden loss of vision in one eye, or inability to walk (BE-FAST Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-142",
        "icd10": "G70.00",
        "condition": "Myasthenia Gravis",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Consensus Guidance for Myasthenia Gravis",
        "source_body": "Neurology",
        "citation": "Narayanaswami P et al. International Consensus Guidance for Management of Myasthenia Gravis: 2020 Update. Neurology. 2021;96(3):114-122.",
        "doi_or_source": "10.1212/WNL.0000000000011124",
        "clinical_evidence": "Myasthenia gravis is an autoimmune neuromuscular junction disorder caused by pathogenic autoantibodies directed against acetylcholine receptors (AChR-Ab, 85%), muscle-specific kinase (MuSK), or LRP4, manifesting as fluctuating, fatigable skeletal muscle weakness with diurnal variation (worse in the evening or after exertion). Ptosis and diplopia occur in >85%; bulbar and respiratory involvement produce dysarthria, dysphagia, and dyspnea. First-line symptomatic treatment is oral pyridostigmine (acetylcholinesterase inhibitor, 30-60 mg every 4-6 hours). Corticosteroids (prednisone) combined with steroid-sparing agents (azathioprine, mycophenolate mofetil) induce immunosuppression. Landmark MGTX trial (NEJM 2016) proved extended transsternal thymectomy provides long-term clinical benefit in non-thymomatous AChR-positive generalized MG under age 65.",
        "solution_protocol": {
            "non_pharmacological_targets": "Rest periods prior to meals to facilitate safe swallowing; avoid extreme heat/hot baths; strictly avoid neuromuscular-blocking medications (fluoroquinolones, macrolides, aminoglycosides, beta-blockers, magnesium).",
            "monitoring_cadence": "Quantitative Myasthenia Gravis (QMG) or MG Activities of Daily Living (MG-ADL) score tracking; pulmonary function testing (forced vital capacity [FVC] and negative inspiratory force [NIF]) during flares; chest CT to screen for thymoma.",
            "clinical_thresholds": "Forced vital capacity (FVC) < 15-20 mL/kg or NIF worse than -20 to -30 cmH2O indicates impending myasthenic crisis requiring ICU transfer."
        },
        "patient_plain_language": "Myasthenia gravis is an autoimmune condition where your body's antibodies block communication between your nerves and muscles. This causes muscles to tire out unusually fast with use, leading to drooping eyelids, double vision, and weakness when chewing or lifting your arms.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my specific antibody subtype (AChR, MuSK, or seronegative) and did my chest CT show a thymoma tumor?",
            "safety_question": "Do I have an up-to-date wallet card listing common prescription antibiotics and drugs that are strictly forbidden in myasthenia?",
            "action_threshold_question": "At what degree of swallowing difficulty or breathing fatigue should I go directly to the emergency department for intravenous IVIG or plasma exchange?"
        },
        "red_flags": [
            "Acute shortness of breath when lying flat (orthopnea), choking on liquids/saliva, or inability to count to 20 on a single breath (Myasthenic Crisis)"
        ]
    },
    {
        "id": "DOC-CARD-143",
        "icd10": "G50.0",
        "condition": "Trigeminal Neuralgia",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN/EAN Practice Guideline",
        "source_body": "Eur J Neurol",
        "citation": "Bendtsen L et al. European Academy of Neurology guideline on trigeminal neuralgia. Eur J Neurol. 2019;26(6):831-845.",
        "doi_or_source": "10.1111/ene.13950",
        "clinical_evidence": "Trigeminal neuralgia is characterized by sudden, unilateral, brief, electric shock-like paroxysmal pain limited to the distribution of one or more branches of the fifth cranial nerve (most frequently V2 maxillary and V3 mandibular), triggered by innocuous sensory tactile stimuli (washing, shaving, talking, brushing teeth, light breeze). Classical trigeminal neuralgia is caused by neurovascular compression of the trigeminal nerve root entry zone (most often by the superior cerebellar artery), detectable on high-resolution 3D constructive interference in steady state (CISS/FIESTA) MRI. Carbamazepine (200-1,200 mg/day; Cochrane review NNT=1.7) and oxcarbazepine (600-1,800 mg/day) are the gold-standard first-line pharmacotherapies. Microvascular decompression (MVD / Janetta procedure) provides long-term pain freedom in >70-80% of refractory classical cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Identify and minimize trigger mechanisms (use soft toothbrushes, protect face from cold wind with scarves, chew on unaffected side); pre-medication HLA-B*1502 genetic screening in patients of Asian descent to avoid Stevens-Johnson syndrome.",
            "monitoring_cadence": "CBC, serum sodium, and liver enzymes at baseline, 2-4 weeks, and every 6 months while on carbamazepine/oxcarbazepine (risk of hyponatremia and aplastic anemia); high-resolution brain MRI.",
            "clinical_thresholds": "Carbamazepine titrated to pain relief while monitoring for serum sodium < 130 mEq/L or elevated transaminases."
        },
        "patient_plain_language": "Trigeminal neuralgia, sometimes referred to as 'tic douloureux', is a severe nerve pain disorder caused by an irritated nerve in your face. Simple daily actions like brushing your teeth, chewing, or feeling a gentle breeze against your cheek can trigger excruciating, lightning-bolt shocks across your jaw or cheek.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my specialized brain MRI show a blood vessel pressing directly against my trigeminal nerve root?",
            "safety_question": "Are my blood counts and sodium levels being checked regularly while taking carbamazepine or oxcarbazepine?",
            "action_threshold_question": "If medications no longer control my pain attacks or cause severe drowsiness, would I be a candidate for surgical microvascular decompression?"
        },
        "red_flags": [
            "Inability to eat or drink due to continuous paroxysmal shocks resulting in acute dehydration, or severe skin rash/peeling after starting carbamazepine"
        ]
    },
    {
        "id": "DOC-CARD-144",
        "icd10": "G25.0",
        "condition": "Essential Tremor",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN Evidence-Based Practice Guideline",
        "source_body": "Neurology",
        "citation": "Zesiewicz TA et al. Evidence-based guideline update: Treatment of essential tremor: Report of the Guideline Development Subcommittee of the AAN. Neurology. 2011;77(19):1752-1760.",
        "doi_or_source": "10.1212/WNL.0b013e318236f0fd",
        "clinical_evidence": "Essential tremor is the most common movement disorder, characterized by an 8-12 Hz bilateral action or kinetic tremor prominently affecting the hands and forearms during voluntary movement (drinking from a cup, handwriting, using utensils), with or without head ('no-no' or 'yes-yes') or voice tremor, in the absence of other neurological signs (rigidity, bradykinesia, resting tremor). Family history is present in >50% (autosomal dominant transmission). Level A first-line therapies include propranolol (60-240 mg/day, reducing tremor amplitude by ~50%) and primidone (50-250 mg/day). Topiramate, gabapentin, and atenolol serve as Level B alternatives. For medically refractory disabling tremor, magnetic resonance-guided focused ultrasound (MRgFUS) thalamotomy or deep brain stimulation (DBS) targeting the ventral intermediate nucleus (VIM) of the thalamus produces >70% long-term tremor reduction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Elimination of tremor-aggravating stimulants (excess caffeine, energy drinks, pseudoephedrine); use of weighted utensils, heavy mugs, and wrist weights; occupational therapy for writing ergonomics.",
            "monitoring_cadence": "Fahn-Tolosa-Marin Tremor Rating Scale assessment annually; heart rate and blood pressure checks before and after propranolol titration.",
            "clinical_thresholds": "Propranolol contraindicated in severe asthma or sinus bradycardia (resting HR < 55 bpm)."
        },
        "patient_plain_language": "Essential tremor is a nervous system disorder that causes rhythmic shaking of your hands when you try to use them for everyday tasks like holding a coffee cup, eating soup, or writing. It is an 'action tremor' (worse when moving) rather than a resting tremor.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my clinical exam rule out Parkinson's disease (confirming this is an action tremor without resting rigidity)?",
            "safety_question": "Does my pulse rate or history of asthma allow me to safely take propranolol for my hand tremors?",
            "action_threshold_question": "If medications don't control the shaking enough to eat or write, am I a candidate for non-invasive focused ultrasound or deep brain stimulation?"
        },
        "red_flags": [
            "Sudden asymmetric onset accompanied by facial droop, limb weakness, or rapid cognitive decline indicating alternative central pathology"
        ]
    },
    {
        "id": "DOC-CARD-145",
        "icd10": "G91.2",
        "condition": "Normal Pressure Hydrocephalus (NPH)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International NPH Guidelines",
        "source_body": "Neurosurgery",
        "citation": "Marmarou A et al. Development of guidelines for idiopathic normal-pressure hydrocephalus: Introduction. Neurosurgery. 2005;57(3 Suppl):S1-S3.",
        "doi_or_source": "10.1227/01.neu.0000168188.25559.0e",
        "clinical_evidence": "Idiopathic normal pressure hydrocephalus is characterized by the classic clinical triad of gait disturbance ('magnetic', shuffling, wide-based, apraxic gait; typically the earliest and most responsive symptom), cognitive decline (subcortical dementia, psychomotor slowing), and urinary urgency/incontinence ('wobbly, wacky, and wet'). Brain MRI demonstrates ventriculomegaly disproportionate to sulcal enlargement (Evans' index > 0.30) with tight high-convexity sulci and enlarged Sylvian fissures (DESH pattern: disproportionately enlarged subarachnoid-space hydrocephalus). Diagnostic confirmation requires a high-volume lumbar puncture tap test (removal of 30-50 mL CSF) showing quantitative improvement in timed 10-meter walk velocity and step count. Ventriculoperitoneal (VP) shunting provides dramatic and sustained functional improvement in >75% of carefully selected patients (SINPHONI trials).",
        "solution_protocol": {
            "non_pharmacological_targets": "Physical therapy for gait training and fall prevention; structured home safety modifications (grab bars, removing throw rugs); scheduled toileting regimens.",
            "monitoring_cadence": "Quantitative timed 10-meter walk test and cognitive testing before and 2-4 hours after lumbar puncture; post-shunt clinical evaluation and non-contrast head CT at 1, 3, and 12 months.",
            "clinical_thresholds": "Evans' index > 0.30 on brain MRI plus ≥20% improvement in timed walk test post-LP confirms shunt-responsive NPH."
        },
        "patient_plain_language": "Normal pressure hydrocephalus is a treatable brain condition where excess spinal fluid slowly builds up in the fluid cavities (ventricles) of your brain. This extra fluid presses on nearby brain circuits, causing a classic trio of symptoms: a shuffling 'feet stuck to the floor' walk, mild memory confusion, and urinary urgency.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Evans' index on brain imaging and did my MRI show the classic enlarged ventricles?",
            "safety_question": "Can we schedule a high-volume lumbar puncture tap test to see if draining temporary spinal fluid improves my walking speed?",
            "action_threshold_question": "If my walking speed improves after the spinal tap, are we ready to consult neurosurgery for a ventriculoperitoneal shunt?"
        },
        "red_flags": [
            "Sudden severe headache, persistent vomiting, fever, or lethargy after shunt surgery indicating shunt malfunction or infection"
        ]
    },
    {
        "id": "DOC-CARD-146",
        "icd10": "G44.009",
        "condition": "Cluster Headache",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Headache Society Guideline",
        "source_body": "Headache",
        "citation": "Robbins MS et al. Treatment of Cluster Headache: The American Headache Society Evidence-Based Guidelines. Headache. 2016;56(7):1093-1106.",
        "doi_or_source": "10.1111/head.12866",
        "clinical_evidence": "Cluster headache is the most severe trigeminal autonomic cephalalgia, characterized by strictly unilateral, excruciating, piercing, or boring retro-orbital/temporal pain lasting 15-180 minutes, occurring from once every other day up to 8 times daily during cluster periods (often lasting 6-12 weeks). Attacks are accompanied by ipsilateral cranial autonomic symptoms (conjunctival injection, lacrimation, nasal congestion, rhinorrhea, eyelid edema, forehead sweating, or miosis/ptosis) and severe motor agitation/restlessness (pacing). First-line acute abortive therapy mandates 100% normobaric oxygen via non-rebreather mask (12-15 L/min for 15-20 min; aborts >75% of attacks within 15 min; Cochrane review) or subcutaneous sumatriptan 6 mg. First-line preventive therapy is oral verapamil (high-dose: 240-960 mg/day), requiring baseline and serial ECG monitoring for PR prolongation and heart block. Galcanezumab (300 mg SQ monthly) is FDA-approved for episodic cluster prevention.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of all alcohol during active cluster bouts (alcohol reliably triggers an attack within 45 minutes); maintain regular sleep-wake rhythms; avoid daytime napping.",
            "monitoring_cadence": "ECG at baseline and after every 80 mg dose increase of verapamil above 240 mg/day (to detect PR interval prolongation and AV block); headache attack log.",
            "clinical_thresholds": "PR interval > 0.20 seconds or heart rate < 50 bpm on verapamil mandates dose reduction or cardiology consultation."
        },
        "patient_plain_language": "Cluster headaches are excruciating, one-sided headaches centered around or behind one eye that strike in clusters lasting weeks to months. Often nicknamed 'suicide headaches' due to their extreme intensity, they cause the eye to water and turn red, with intense restlessness that makes sitting still impossible.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I have a home medical oxygen tank with a high-flow non-rebreather mask (12 to 15 liters per minute) for fast attack relief?",
            "safety_question": "Are we performing serial ECG tracings as we increase my verapamil dose to ensure my heart rate and electrical conduction stay safe?",
            "action_threshold_question": "Would I benefit from a short steroid taper or galcanezumab injections to break my current cluster cycle?"
        },
        "red_flags": [
            "Sudden maximal-intensity headache ('thunderclap' headache reaching peak in <1 minute) requiring urgent exclusion of subarachnoid hemorrhage"
        ]
    },
    {
        "id": "DOC-CARD-147",
        "icd10": "G12.21",
        "condition": "Amyotrophic Lateral Sclerosis (ALS)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EFNS/EAN Guidelines on ALS Management",
        "source_body": "Eur J Neurol",
        "citation": "Andersen PM et al. EFNS guidelines on the Clinical Management of Amyotrophic Lateral Sclerosis (MALS)--revised report of an EFNS task force. Eur J Neurol. 2012;19(3):360-375.",
        "doi_or_source": "10.1111/j.1468-1331.2011.03501.x",
        "clinical_evidence": "ALS is a progressive, fatal neurodegenerative disease characterized by simultaneous degeneration of upper motor neurons (corticospinal: spasticity, hyperreflexia, Babinski sign) and lower motor neurons (anterior horn cells: muscle weakness, atrophy, fasciculations) across bulbar, cervical, thoracic, and lumbosacral regions. Gold standard diagnosis follows the Awaji/Gold Coast criteria supported by electromyography (EMG). Multidisciplinary specialized care extends survival and improves quality of life. Riluzole (50 mg orally twice daily) extends median tracheostomy-free survival by 2-3 months by modulating glutamatergic neurotransmission. Edaravone (IV/oral free radical scavenger) slows functional decline in early disease. Noninvasive positive-pressure ventilation (NIV / BiPAP) significantly prolongs survival and slows respiratory decline when initiated once forced vital capacity (FVC) drops below 80% or sniff nasal inspiratory pressure (SNIP) < 40 cmH2O.",
        "solution_protocol": {
            "non_pharmacological_targets": "Multidisciplinary clinic visits (neurologist, pulmonologist, speech therapist, occupational therapist, registered dietitian); high-calorie, nutrient-dense diet to prevent hypermetabolic weight loss; early discussion of advance care planning.",
            "monitoring_cadence": "ALS Functional Rating Scale-Revised (ALSFRS-R) and upright/supine spirometry (FVC) every 3 months; liver function tests every month for the first 3 months on riluzole.",
            "clinical_thresholds": "FVC < 80% of predicted, orthopnea, or daytime hypercapnia mandates immediate initiation of noninvasive ventilation (BiPAP)."
        },
        "patient_plain_language": "Amyotrophic lateral sclerosis (ALS), also known as Lou Gehrig's disease, is a condition where the nerve cells in your brain and spinal cord that control voluntary muscles slowly break down. Over time, muscles become weak and thin, affecting walking, speaking, swallowing, and breathing.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current forced vital capacity (FVC) sitting and lying down, and what is my ALSFRS-R functional score?",
            "safety_question": "Are my liver enzymes normal on riluzole, and are we monitoring my swallowing safety to prevent aspiration pneumonia?",
            "action_threshold_question": "When should we order a noninvasive breathing machine (BiPAP) to support my lungs and help me sleep comfortably?"
        },
        "red_flags": [
            "Severe respiratory insufficiency with morning headaches (CO2 retention), inability to clear throat secretions, or acute aspiration choking events"
        ]
    },
    {
        "id": "DOC-CARD-148",
        "icd10": "G93.2",
        "condition": "Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Idiopathic Intracranial Hypertension Treatment Trial (IIHTT)",
        "source_body": "JAMA",
        "citation": "NORDIC Idiopathic Intracranial Hypertension Study Group. Effect of acetazolamide on visual function in patients with idiopathic intracranial hypertension and mild visual loss: the IIHTT randomized clinical trial. JAMA. 2014;311(16):1641-1651.",
        "doi_or_source": "10.1001/jama.2014.3312",
        "clinical_evidence": "Idiopathic intracranial hypertension (IIH) predominantly affects women of childbearing age with obesity (BMI > 30), characterized by elevated intracranial pressure (>250 mmH2O on lumbar puncture in adults) in the absence of ventriculomegaly, mass lesion, or cerebral venous sinus thrombosis. Classic symptoms include daily throbbing headaches, transient visual obscurations (dimming of vision lasting seconds with postural changes), pulsatile tinnitus ('whooshing' sound in ears), and horizontal diplopia (cranial nerve VI palsy). The hallmark physical sign is bilateral papilledema, which risks permanent optic atrophy and blindness. The landmark IIHTT trial proved that weight reduction combined with acetazolamide (carbonic anhydrase inhibitor, titrated up to 1-4 g/day) significantly improved Humphrey visual field mean deviation, reduced papilledema grade, and improved quality of life compared to placebo.",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured lifestyle weight management program targeting 5-15% sustained body weight reduction (often induces disease remission); sodium-restricted diet; discontinuation of offending medications (tetracyclines, retinoids/Accutane, excess vitamin A).",
            "monitoring_cadence": "Humphrey automated visual field testing and optical coherence tomography (OCT) of the retinal nerve fiber layer every 1-3 months; comprehensive dilated funduscopic exam.",
            "clinical_thresholds": "CSF opening pressure > 250 mmH2O confirms elevated ICP; worsening visual field loss (mean deviation worsening by >2 dB) warrants surgical intervention (optic nerve sheath fenestration or CSF shunt)."
        },
        "patient_plain_language": "Idiopathic intracranial hypertension, or pseudotumor cerebri, occurs when fluid pressure builds up inside your skull without an actual tumor. This high pressure squeezes your optic nerves, leading to daily headaches, a rhythmic whooshing heartbeat sound in your ears, and brief dimming or blurring of vision.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my cerebrospinal fluid opening pressure on spinal tap, and what is the severity grade of my papilledema?",
            "safety_question": "Are my serum electrolytes and potassium levels being monitored while I am taking acetazolamide (Diamox)?",
            "action_threshold_question": "Are my automated visual field tests showing that my peripheral vision is completely stable, or is there any sign of vision loss?"
        },
        "red_flags": [
            "Rapid progressive constriction of peripheral vision, loss of central visual acuity, or persistent double vision (impending optic nerve compromise)"
        ]
    },
    {
        "id": "DOC-CARD-149",
        "icd10": "G25.81",
        "condition": "Restless Legs Syndrome (RLS / Willis-Ekbom Disease)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN Evidence-Based Practice Guideline",
        "source_body": "Neurology",
        "citation": "Winkelman JW et al. Practice guideline summary: Treatment of restless legs syndrome in adults: Report of the Guideline Development, Dissemination, and Implementation Subcommittee of the AAN. Neurology. 2016;87(24):2585-2593.",
        "doi_or_source": "10.1212/WNL.0000000000003388",
        "clinical_evidence": "Diagnostic criteria (IRLSSG) require: (1) an irresistible urge to move the legs usually accompanied by uncomfortable paresthesias, (2) symptoms begin or worsen during periods of rest or inactivity, (3) symptoms are partially or totally relieved by movement (walking, stretching), and (4) symptoms occur exclusively or predominantly in the evening or night. Central nervous system iron deficiency in the substantia nigra impairs dopamine neurotransmission. Serum ferritin should be evaluated; oral iron supplementation is indicated if ferritin < 75 mcg/L or transferrin saturation < 20%, and IV ferric carboxymaltose is superior for refractory iron deficiency. First-line pharmacotherapy has shifted to alpha-2-delta calcium channel ligands (gabapentin enacarbil, pregabalin) over dopamine agonists (pramipexole, ropinirole) because dopamine agonists cause severe clinical augmentation (earlier symptom onset, increased intensity, spread to arms) in up to 50-70% of long-term users.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoidance of exacerbating triggers: caffeine, alcohol, nicotine, sedating antihistamines (diphenhydramine), dopamine antagonists, and SSRIs/SNRIs; moderate regular exercise; warm evening baths.",
            "monitoring_cadence": "Morning fasting iron panel (ferritin and transferrin saturation) every 6-12 months; International RLS Severity Scale (IRLS) symptom monitoring.",
            "clinical_thresholds": "Serum ferritin < 75 mcg/L or transferrin saturation < 20% mandates therapeutic iron repletion."
        },
        "patient_plain_language": "Restless legs syndrome is a neurological sensory condition that causes an overwhelming, creepy-crawly urge to move your legs when you try to rest, sit still, or fall asleep. Moving or walking provides temporary relief, but the sensations return as soon as you lie down again.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my fasting ferritin and transferrin saturation level to see if low brain iron stores are causing my symptoms?",
            "safety_question": "Why are alpha-2-delta medications like gabapentin generally preferred today over older dopamine drugs that can make symptoms worse over time?",
            "action_threshold_question": "Am I taking any over-the-counter nighttime sleep aids like Benadryl that could actually be making my restless legs flare up?"
        },
        "red_flags": [
            "Sudden severe impulse control disorders (compulsive gambling, binge eating, hypersexuality) if taking dopamine agonist medications"
        ]
    },
    {
        "id": "DOC-CARD-150",
        "icd10": "G51.0",
        "condition": "Bell's Palsy (Idiopathic Facial Paralysis)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNSF Clinical Practice Guideline",
        "source_body": "Otolaryngol Head Neck Surg",
        "citation": "Baugh RF et al. Clinical practice guideline: Bell's palsy. Otolaryngol Head Neck Surg. 2013;149(3 Suppl):S1-S27.",
        "doi_or_source": "10.1177/0194599813505967",
        "clinical_evidence": "Bell's palsy is an acute, unilateral peripheral lower motor neuron facial nerve (CN VII) paresis or paralysis, causing weakness of both upper and lower facial muscles (inability to furrow forehead, close eye, or smile), peaking within 72 hours, thought to result from HSV-1 reactivation causing nerve edema inside the fallopian canal. It is distinguished from central stroke where forehead movement is preserved due to bilateral cortical innervation. Cochrane systematic reviews and landmark RCTs confirm that oral corticosteroids (prednisone 60-80 mg/day for 7-10 days initiated within 72 hours of symptom onset) significantly increase complete recovery rates from ~70% to >85% (RR 1.15, 95% CI 1.05-1.26; NNT=10). Adding antiviral therapy (valacyclovir 1 g TID) provides modest incremental benefit in severe complete paralysis (House-Brackmann grade V-VI). Aggressive corneal protection is paramount to prevent exposure keratitis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive daytime artificial tears every 1-2 hours; lubricating ophthalmic ointment at night; tape the eyelid safely shut at night with moisture chamber to prevent corneal ulceration.",
            "monitoring_cadence": "House-Brackmann facial nerve grading at baseline and follow-up at 1, 3, and 6 months; ophthalmology referral if eye closure is incomplete.",
            "clinical_thresholds": "Initiation of high-dose oral corticosteroids within 72 hours of symptom onset is the critical therapeutic window."
        },
        "patient_plain_language": "Bell's palsy is a sudden, temporary weakness or paralysis of the muscles on one side of your face caused by inflammation of the main facial nerve. Unlike a stroke, Bell's palsy causes your entire half of the face to droop, including your eyebrow and forehead, making it difficult to close your eye or smile.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my physical exam confirm that my forehead is paralyzed, ruling out a central brain stroke?",
            "safety_question": "Have I started oral steroid pills within the critical 72-hour window to give my facial nerve the best chance of 100% recovery?",
            "action_threshold_question": "What exact eye drops, lubricating night ointments, and protective tape should I use to protect my eye from drying out and scratching?"
        },
        "red_flags": [
            "Inability to close the eye leading to severe eye pain, foreign body sensation, redness, or cloudy cornea (impending corneal ulceration)"
        ]
    },
    {
        "id": "DOC-CARD-151",
        "icd10": "N20.0",
        "condition": "Nephrolithiasis (Kidney Stones)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA Clinical Guideline",
        "source_body": "J Urol",
        "citation": "Pearle MS et al. Medical Management of Kidney Stones: AUA Guideline. J Urol. 2014;192(2):316-324.",
        "doi_or_source": "10.1016/j.juro.2014.05.006",
        "clinical_evidence": "Nephrolithiasis affects ~10% of individuals, with calcium oxalate (75-80%) and uric acid (10%) being the most prevalent compositions. Acute presentation involves severe colicky flank pain radiating to the groin with microscopic or gross hematuria. Low-dose non-contrast abdominopelvic CT is the imaging gold standard. Stones < 5 mm have an ~75-80% spontaneous passage rate, while stones ≥ 7-10 mm frequently require urologic intervention (ureteroscopy with laser lithotripsy or shock wave lithotripsy). Prevention requires 24-hour urine collection. High fluid intake to achieve > 2.5 L daily urine output halves recurrence risk (Cochrane RR 0.45). Normal dietary calcium (1,000-1,200 mg/day) reduces stone formation by binding dietary oxalate in the gut, whereas calcium restriction paradoxically increases stones. Thiazide diuretics reduce hypercalciuria; potassium citrate alkalinizes urine to dissolve uric acid stones and bind calcium.",
        "solution_protocol": {
            "non_pharmacological_targets": "Fluid intake to maintain > 2.5 liters urine output/day (urine color clear/pale); dietary sodium restriction (<2,300 mg/day; high sodium increases urinary calcium excretion); limit animal protein; do not restrict dietary calcium.",
            "monitoring_cadence": "24-hour urine metabolic profile (volume, calcium, oxalate, citrate, uric acid, sodium, pH) 6-8 weeks post-resolution; repeat annually; stone composition analysis.",
            "clinical_thresholds": "Stones > 10 mm, persistent pain, severe hydronephrosis, or fever with infected obstructed stone require urgent urologic intervention."
        },
        "patient_plain_language": "Kidney stones are hard mineral crystal deposits that form inside your kidneys when your urine becomes overly concentrated. When a stone moves down the narrow drainage tube toward your bladder, it causes intense, cramping back and flank pain, nausea, and blood in your urine.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured size and exact location of my stone on the CT scan, and was my filtered stone sent for mineral analysis?",
            "safety_question": "Should we complete a 24-hour urine collection to identify the chemical imbalance causing my stones and prevent future ones?",
            "action_threshold_question": "How much water do I need to drink every day to ensure my urine volume is consistently above 2.5 liters?"
        },
        "red_flags": [
            "Fever and shaking chills accompanying flank pain (infected obstructed kidney / urosepsis emergency requiring urgent decompression)"
        ]
    },
    {
        "id": "DOC-CARD-152",
        "icd10": "Q61.2",
        "condition": "Autosomal Dominant Polycystic Kidney Disease (ADPKD)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Controversies Conference / TEMPO 3:4 RCT",
        "source_body": "N Engl J Med",
        "citation": "Torres VE et al. Tolvaptan in patients with autosomal dominant polycystic kidney disease (TEMPO 3:4). N Engl J Med. 2012;367(25):2407-2418.",
        "doi_or_source": "10.1056/NEJMoa1205511",
        "clinical_evidence": "ADPKD is the most common hereditary kidney disorder (1:400 to 1:1,000 live births), caused by germline mutations in PKD1 (80%) or PKD2 (15%), resulting in progressive bilateral fluid-filled renal cyst expansion, destruction of renal parenchyma, and end-stage kidney disease in >50% by age 60. Hypertension develops early and requires aggressive control (target BP < 110/75 mmHg in young patients with preserved eGFR; HALT-PKD trial). Total kidney volume (TKV) measured by MRI and classified via the Mayo Imaging Classification (Classes 1C-1E) stratifies rapid progressors. The selective vasopressin V2 receptor antagonist tolvaptan (TEMPO 3:4 and REPRISE trials) significantly slowed TKV growth and reduced the rate of eGFR decline by ~1.0-1.2 mL/min/1.73m² per year, and is indicated for patients with rapidly progressive disease.",
        "solution_protocol": {
            "non_pharmacological_targets": "High fluid intake (≥ 3 liters/day water to suppress endogenous vasopressin production); strict dietary sodium restriction (<2,000 mg/day); avoid contact sports risking cyst rupture.",
            "monitoring_cadence": "eGFR and urine albumin-to-creatinine ratio every 3-6 months; monthly liver function tests for the first 18 months on tolvaptan (due to idiosyncratic hepatotoxicity risk); baseline brain MRA screening for intracranial berry aneurysms in patients with high-risk family history.",
            "clinical_thresholds": "Mayo Imaging Classification 1C, 1D, or 1E (predicted eGFR loss > 3 mL/min/1.73m²/year) qualifies for tolvaptan therapy."
        },
        "patient_plain_language": "Autosomal dominant polycystic kidney disease (ADPKD) is a genetic condition where thousands of fluid-filled sacs (cysts) slowly grow and multiply inside your kidneys over decades. As the cysts enlarge, your kidneys grow to several times their normal size, crowding out healthy kidney tissue and causing high blood pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my total kidney volume (TKV) and Mayo imaging classification on MRI?",
            "safety_question": "Do I have a family history of brain aneurysms that warrants a screening MRA scan of my brain arteries?",
            "action_threshold_question": "Am I a candidate for tolvaptan (Jynarque) to slow the growth of kidney cysts and preserve my kidney function?"
        },
        "red_flags": [
            "Sudden severe flank pain with gross dark hematuria and fever (infected renal cyst), or sudden explosive 'worst headache of life' (ruptured intracranial aneurysm)"
        ]
    },
    {
        "id": "DOC-CARD-153",
        "icd10": "N04.9",
        "condition": "Nephrotic Syndrome",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Clinical Practice Guideline for Glomerular Diseases",
        "source_body": "Kidney Int",
        "citation": "Rovin BH et al. KDIGO 2021 Clinical Practice Guideline for the Management of Glomerular Diseases. Kidney Int. 2021;100(4S):S1-S276.",
        "doi_or_source": "10.1016/j.kint.2021.05.021",
        "clinical_evidence": "Nephrotic syndrome is characterized by heavy proteinuria (> 3.5 g/24 hr or spot urine protein-to-creatinine ratio [uPCR] > 3.0 g/g), hypoalbuminemia (serum albumin < 3.0 g/dL), generalized peripheral and periorbital edema, and hyperlipidemia. Major primary adult etiologies include membranous nephropathy (anti-PLA2R positive in 70-80%), focal segmental glomerulosclerosis (FSGS), and minimal change disease (MCD). Renal biopsy provides definitive histological confirmation. MCD responds dramatically to high-dose oral prednisone (1 mg/kg/day, achieving remission in >80%). Membranous nephropathy risk stratification dictates therapy: rituximab (CD20-depleting B-cell therapy, MENTOR trial; NEJM 2019) is superior to cyclosporine for inducing sustained complete/partial remission with favorable safety profile. Severe hypoalbuminemia (<2.0-2.5 g/dL) carries high venous thromboembolism risk (DVT/PE/renal vein thrombosis), requiring prophylactic anticoagulation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary sodium restriction (<2,000 mg/day) to control refractory edema; moderate dietary protein intake (0.8 g/kg/day; high-protein diets increase glomerular hyperfiltration and worsen proteinuria); pneumococcal and influenza vaccinations.",
            "monitoring_cadence": "Spot urine protein-to-creatinine ratio (uPCR), serum albumin, creatinine, eGFR, and lipid panel every 1-3 months; anti-PLA2R antibody titers every 3 months for membranous nephropathy.",
            "clinical_thresholds": "Proteinuria > 3.5 g/24 hr with albumin < 3.0 g/dL establishes nephrotic state; serum albumin < 2.0-2.5 g/dL in membranous nephropathy triggers prophylactic anticoagulation evaluation."
        },
        "patient_plain_language": "Nephrotic syndrome is a kidney condition where the tiny filtering units in your kidneys (glomeruli) become damaged and leaky. Instead of keeping essential proteins in your blood, they spill large amounts of protein into your urine, causing your body to retain fluid and swell, particularly around your eyes, ankles, and legs.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current 24-hour urine protein or urine protein-to-creatinine ratio and blood albumin level?",
            "safety_question": "Because my blood albumin is very low, do I need blood thinners to protect me from dangerous blood clots in my legs or lungs?",
            "action_threshold_question": "Will I need a kidney biopsy or an anti-PLA2R antibody blood test to determine the exact type of kidney disease causing my protein leak?"
        },
        "red_flags": [
            "Sudden unilateral calf swelling and tenderness (DVT), sudden shortness of breath and pleuritic chest pain (pulmonary embolism), or flank pain with gross hematuria (renal vein thrombosis)"
        ]
    },
    {
        "id": "DOC-CARD-154",
        "icd10": "N02.8",
        "condition": "IgA Nephropathy (Berger's Disease)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Guideline / NefIgArd Phase 3 RCT",
        "source_body": "The Lancet",
        "citation": "Rovin BH et al. Efficacy and safety of targeted-release budesonide in patients with primary IgA nephropathy (NefIgArd): 2-year results from a randomised, double-blind, placebo-controlled phase 3 trial. Lancet. 2023;402(10405):859-870.",
        "doi_or_source": "10.1016/S0140-6736(23)01554-4",
        "clinical_evidence": "IgA nephropathy is the most common primary glomerulonephritis worldwide, caused by galactose-deficient IgA1 deposition in the glomerular mesangium, inducing mesangial proliferation, matrix expansion, and glomerulosclerosis. Classic presentation is episodic synpharyngitic gross hematuria (coca-cola colored urine 24-48 hours after an upper respiratory infection) or asymptomatic microscopic hematuria with persistent proteinuria. Definitive diagnosis requires kidney biopsy scored via the Oxford Classification (MEST-C score). Foundational supportive therapy for all patients with proteinuria > 0.5 g/day mandates maximally tolerated ACE inhibitors or ARBs, combined with SGLT2 inhibitors (DAPA-CKD trial; 71% reduction in kidney failure composite). For persistent proteinuria ≥ 0.75-1.0 g/day despite supportive therapy, targeted-release enteric budesonide (Nefecon 16 mg daily) provides significant eGFR preservation and proteinuria reduction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict dietary sodium restriction (<2,000 mg/day); smoking cessation; aggressive systolic blood pressure target < 120 mmHg (KDIGO 2021).",
            "monitoring_cadence": "Spot urine protein-to-creatinine ratio (uPCR), microscopic urinalysis, serum creatinine, and eGFR every 3-6 months; annual cardiovascular risk assessment.",
            "clinical_thresholds": "Persistent proteinuria ≥ 0.75-1.0 g/day despite ≥ 3 months of optimized supportive therapy indicates high risk of progressive kidney failure, qualifying for immunosuppressive or targeted therapies."
        },
        "patient_plain_language": "IgA nephropathy is an immune disorder where abnormal antibodies called IgA get trapped in the microscopic filters of your kidneys. This triggers chronic inflammation and scarring, often noticed when your urine turns brown or tea-colored during or right after a throat infection.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current urine protein-to-creatinine ratio and eGFR kidney filtration rate?",
            "safety_question": "Am I on the maximum safe dose of a blood pressure protector (ACE inhibitor or ARB) plus an SGLT2 inhibitor to shield my kidneys?",
            "action_threshold_question": "If my urine protein remains over 1 gram per day, would I benefit from a targeted gut steroid capsule (budesonide/Tarpeyo)?"
        },
        "red_flags": [
            "Rapid deterioration of kidney function (creatinine doubling over weeks), rapid drop in urine output, or severe uncontrolled high blood pressure"
        ]
    },
    {
        "id": "DOC-CARD-155",
        "icd10": "N32.81",
        "condition": "Overactive Bladder (OAB)",
        "specialty": "Urology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA/SUFU Guideline",
        "source_body": "J Urol",
        "citation": "Lightner DJ et al. Diagnosis and Treatment of Non-Neurogenic Overactive Bladder (OAB) in Adults: An AUA/SUFU Guideline Amendment 2019. J Urol. 2019;202(3):558-563.",
        "doi_or_source": "10.1097/JU.0000000000000309",
        "clinical_evidence": "Overactive bladder is a clinical syndrome characterized by urinary urgency (compelling desire to pass urine which is difficult to defer), usually accompanied by frequency (≥8 micturitions/24 hr) and nocturia (≥2 voids/night), with or without urgency urinary incontinence (OAB wet vs OAB dry), in the absence of UTI or other pathology. Initial management focuses on behavioral therapies (bladder training, timed voiding, fluid management, pelvic floor muscle therapy). Second-line therapy consists of oral antimuscarinics (solifenacin, oxybutynin; cautioned in elderly due to anticholinergic cognitive burden and dementia risk) or beta-3 adrenergic agonists (mirabegron 25-50 mg daily, vibegron 75 mg daily; relax detrusor without anticholinergic side effects). Third-line modalities for refractory cases include intradetrusor onabotulinumtoxinA (100 units), sacral neuromodulation (InterStim), or percutaneous tibial nerve stimulation (PTNS).",
        "solution_protocol": {
            "non_pharmacological_targets": "Pelvic floor muscle training (Kegel exercises) with biofeedback; bladder retraining with progressive voiding intervals; fluid intake moderation (avoid excess fluids after 6 PM); eliminate dietary bladder irritants (caffeine, artificial sweeteners, carbonated beverages, spicy foods).",
            "monitoring_cadence": "3-day voiding frequency-volume diary; Post-Void Residual (PVR) measurement via bladder scan prior to starting medications or botulinum toxin.",
            "clinical_thresholds": "Post-void residual (PVR) > 150-200 mL warrants caution when prescribing antimuscarinics to prevent acute urinary retention."
        },
        "patient_plain_language": "Overactive bladder is a condition where your bladder muscles squeeze and spasm before your bladder is actually full, creating a sudden, urgent need to run to the bathroom that can be hard to hold back. It often causes frequent daytime trips and waking up multiple times each night.",
        "doctor_consultation_checklist": {
            "parameter_question": "What did my 3-day bladder diary and post-void residual ultrasound show?",
            "safety_question": "Are beta-3 medications like mirabegron or vibegron safer for my memory and cognitive health than older anticholinergic pills like oxybutynin?",
            "action_threshold_question": "If pills don't adequately stop the bladder spasms, am I a good candidate for bladder botulinum toxin injections or nerve stimulation?"
        },
        "red_flags": [
            "Inability to pass any urine with severe lower belly pressure and pain (acute urinary retention), or visible blood in the urine (gross hematuria)"
        ]
    },
    {
        "id": "DOC-CARD-156",
        "icd10": "N39.3",
        "condition": "Stress Urinary Incontinence",
        "specialty": "Urology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACOG Practice Bulletin / Cochrane Review",
        "source_body": "Obstet Gynecol",
        "citation": "American College of Obstetricians and Gynecologists. Urinary Incontinence in Women: ACOG Practice Bulletin No. 155. Obstet Gynecol. 2015;126(5):e66-e81.",
        "doi_or_source": "10.1097/AOG.0000000000001148",
        "clinical_evidence": "Stress urinary incontinence (SUI) is involuntary leakage of urine upon physical exertion, sneezing, coughing, laughing, or lifting, occurring when intra-abdominal pressure exceeds urethral closure pressure in the setting of pelvic floor muscle laxity or intrinsic sphincter deficiency. First-line therapy is supervised pelvic floor muscle training (PFMT / Kegels; Cochrane systematic review confirms PFMT yields >5-fold higher cure/improvement rates vs control, RR 5.34). Vaginal pessaries or urethral inserts provide non-surgical mechanical urethral support. For patients desiring definitive surgical correction, the synthetic midurethral sling (retropubic or transobturator tape) remains the gold standard procedure with >85-90% subjective cure rates at 5 years. Burch colposuspension or autologous fascial slings serve as non-mesh alternatives.",
        "solution_protocol": {
            "non_pharmacological_targets": "Supervised pelvic floor physical therapy (at least 3 sets of 10-15 contractions held 6-8 seconds daily for at least 12 weeks); weight reduction in overweight/obese women (5-10% weight loss reduces incontinence episodes by 50%); treatment of chronic constipation.",
            "monitoring_cadence": "Validated incontinence symptom questionnaire (e.g., UDI-6, IIQ-7) and 24-hour pad test at 3 months post-physiotherapy; urology/urogynecology review.",
            "clinical_thresholds": "Positive cough stress test during physical exam with bladder comfortably full confirms stress incontinence."
        },
        "patient_plain_language": "Stress urinary incontinence happens when the muscles and tissues supporting your bladder and urethra weaken. Sudden physical pressure on your abdomen—such as coughing, sneezing, laughing, jumping, or exercising—causes accidental urine leakage.",
        "doctor_consultation_checklist": {
            "parameter_question": "Can you refer me to a specialized pelvic floor physical therapist to ensure I am performing pelvic contractions correctly?",
            "safety_question": "Would a removable vaginal pessary provide adequate support during exercise without requiring surgery?",
            "action_threshold_question": "If physical therapy doesn't resolve the leakage, what are the success rates and risks of a midurethral sling procedure?"
        },
        "red_flags": [
            "Complete inability to urinate (urinary retention) following pelvic surgery, severe groin pain, or vaginal mesh erosion symptoms"
        ]
    },
    {
        "id": "DOC-CARD-157",
        "icd10": "N30.10",
        "condition": "Interstitial Cystitis (Bladder Pain Syndrome)",
        "specialty": "Urology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA Clinical Guideline",
        "source_body": "J Urol",
        "citation": "Hanno PM et al. Diagnosis and treatment of interstitial cystitis/bladder pain syndrome: AUA guideline amendment. J Urol. 2015;193(5):1545-1553.",
        "doi_or_source": "10.1016/j.juro.2015.01.086",
        "clinical_evidence": "Interstitial cystitis / bladder pain syndrome (IC/BPS) is defined as an unpleasant sensation (pain, pressure, discomfort) perceived to be related to the urinary bladder, associated with lower urinary tract symptoms of more than 6 weeks duration, in the absence of infection or other identifiable causes. Pain typically intensifies as the bladder fills and temporarily relieves following voiding. Cystoscopy may reveal glomerulations (petechial hemorrhages on hydrodistention) or Hunner lesions (circumscribed reddish mucosal lesions with radiating vessels; present in 10-15%). Stepwise management: Step 1 involves patient education, fluid regulation, and elimination of dietary triggers (caffeine, citrus, alcohol, artificial sweeteners). Step 2 incorporates specialized pelvic floor physical therapy (targeting muscle spasms and trigger points; strictly avoiding strengthening Kegels) and oral medications (amitriptyline 25-75 mg, cimetidine, hydroxyzine, or pentosan polysulfate sodium). Hunner lesions respond to endoscopic fulguration.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary modification using an elimination diet to identify bladder irritants (coffee, tea, tomatoes, spicy foods, acidic fruit); gentle myofascial physical therapy (avoid Kegel exercises which exacerbate hypertonic pelvic floor spasms); application of heat/cold to pelvic area.",
            "monitoring_cadence": "Genitourinary Pain and Frequency (PUF) score or O'Leary-Sant Symptom Index every 3 months; regular retinal screening if taking pentosan polysulfate (due to drug-induced pigmentary maculopathy risk).",
            "clinical_thresholds": "Cystoscopic identification of Hunner lesions dictates direct endoscopic electrocautery or triamcinolone injection."
        },
        "patient_plain_language": "Interstitial cystitis, or bladder pain syndrome, is a chronic inflammatory condition where you feel aching, pressure, or burning pain in your bladder that worsens as your bladder fills with urine. People often feel the urge to urinate dozens of times a day to relieve the aching pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my cystoscopy show Hunner's ulcers or classic signs of bladder lining inflammation?",
            "safety_question": "If I am taking Elmiron (pentosan polysulfate), am I getting baseline and annual eye exams to protect my retinas?",
            "action_threshold_question": "Can I be referred to a physical therapist specialized in pelvic floor muscle release rather than standard Kegel exercises?"
        },
        "red_flags": [
            "Gross visible hematuria (blood in urine) requiring cystoscopy to rule out bladder carcinoma, persistent fever, or progressive severe pelvic pain"
        ]
    },
    {
        "id": "DOC-CARD-158",
        "icd10": "N41.1",
        "condition": "Chronic Prostatitis / Chronic Pelvic Pain Syndrome (CP/CPPS)",
        "specialty": "Urology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EAU Guidelines on Chronic Pelvic Pain",
        "source_body": "Eur Urol",
        "citation": "Engeler D et al. EAU Guidelines on Chronic Pelvic Pain. Eur Urol. 2020;77(5):e104-e106.",
        "doi_or_source": "10.1016/j.eururo.2020.01.005",
        "clinical_evidence": "NIH Category III chronic prostatitis / chronic pelvic pain syndrome (CP/CPPS) is characterized by chronic pelvic, perineal, scrotal, penile, or suprapubic pain persisting for at least 3 months within the previous 6 months, in the absence of uropathogenic bacteria on standard cultures. It is frequently accompanied by painful ejaculation, voiding dysfunction, and severe negative cognitive and emotional impact. Management utilizes the multi-modal UPOINT clinical phenotyping system (Urinary, Psychosocial, Organ-specific, Infection, Neurological/systemic, Tenderness of muscles), directing tailored therapy rather than empiric repeated antibiotic courses: alpha-blockers (tamsulosin 0.4 mg) for urinary obstruction; anti-inflammatory agents (NSAIDs); neuromodulating medications (pregabalin, duloxetine); specialized myofascial pelvic floor physical therapy for pelvic floor hypertonicity; and cognitive-behavioral therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Myofascial pelvic floor trigger-point release physical therapy; avoid prolonged sitting and bicycling (use split saddles); warm sitz baths; stress reduction and mindfulness-based pelvic relaxation.",
            "monitoring_cadence": "NIH-Chronic Prostatitis Symptom Index (NIH-CPSI) questionnaire every 4-8 weeks to measure treatment response; repeat urinalysis and urine culture during acute symptom exacerbations.",
            "clinical_thresholds": "Repeated negative urine cultures establish non-bacterial CP/CPPS (NIH Category III), mandating cessation of repetitive antibiotic therapies."
        },
        "patient_plain_language": "Chronic pelvic pain syndrome in men causes ongoing aching pain, pressure, or discomfort in the pelvic floor, groin, or testicles, often made worse by sitting or after ejaculation. It is usually not an active bacterial infection, but rather a combination of tense pelvic floor muscles and irritated pelvic nerves.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my score on the NIH Chronic Prostatitis Symptom Index (NIH-CPSI)?",
            "safety_question": "Since my urine cultures show no bacteria, can we stop taking repeated courses of antibiotics that aren't helping?",
            "action_threshold_question": "Would a course of alpha-blockers combined with pelvic floor physical therapy help relieve my pelvic muscle tension?"
        },
        "red_flags": [
            "High fever with chills and acute inability to urinate (acute bacterial prostatitis emergency), or gross painless blood in urine"
        ]
    },
    {
        "id": "DOC-CARD-159",
        "icd10": "N40.1",
        "condition": "Benign Prostatic Hyperplasia (BPH) with LUTS",
        "specialty": "Urology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AUA Clinical Guideline",
        "source_body": "J Urol",
        "citation": "Lerner LB et al. Management of Lower Urinary Tract Symptoms Attributed to Benign Prostatic Hyperplasia: AUA Guideline. J Urol. 2021;206(4):806-817.",
        "doi_or_source": "10.1097/JU.0000000000002183",
        "clinical_evidence": "Benign prostatic hyperplasia involves non-malignant adenomatous stromal and epithelial proliferation of the prostate transition zone, causing bladder outlet obstruction and lower urinary tract symptoms (LUTS: weak stream, hesitancy, intermittency, straining, post-void dribbling, frequency, nocturia). Symptom severity is quantified via the International Prostate Symptom Score (IPSS). Medical therapy: Alpha-1 adrenergic antagonists (tamsulosin 0.4 mg, alfuzosin 10 mg) rapidly relax prostate smooth muscle, improving IPSS by 4-6 points within 2-4 days. 5-alpha reductase inhibitors (5-ARIs: finasteride 5 mg, dutasteride 0.5 mg) shrink prostate volume by ~20-25% and reduce the long-term risk of acute urinary retention and BPH-related surgery (MTOPS and CombAT trials), indicated when prostate volume > 30 cc or PSA > 1.5 ng/mL. Tadalafil 5 mg daily is approved for concomitant erectile dysfunction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Limit fluid intake in the 2 hours before bed; reduce caffeine and alcohol consumption; avoid OTC decongestants (pseudoephedrine) and first-generation antihistamines which can trigger urinary retention; practice double-voiding.",
            "monitoring_cadence": "IPSS questionnaire, post-void residual (PVR) ultrasound, and serum PSA every 6-12 months (note: 5-ARIs halve serum PSA; true PSA is 2x measured value).",
            "clinical_thresholds": "PVR > 250-300 mL, recurrent urinary tract infections, bladder calculi, or refractory urinary retention warrants surgical intervention (TURP, HoLEP, water vapor thermal therapy/Rezum, or prostatic urethral lift/UroLift)."
        },
        "patient_plain_language": "Benign prostatic hyperplasia (BPH) is an age-related, non-cancerous enlargement of the prostate gland in men. Because the prostate wraps around the tube that carries urine from your bladder, its growth squeezes the pipe, causing a weak or stopped stream, nighttime bathroom trips, and straining.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my IPSS symptom score, prostate size, and post-void residual urine volume?",
            "safety_question": "If I take finasteride or dutasteride, does my doctor remember to multiply my PSA lab result by two to monitor accurately for prostate health?",
            "action_threshold_question": "Would combination therapy (tamsulosin plus finasteride) or a minimally invasive office procedure best preserve my bladder function?"
        },
        "red_flags": [
            "Sudden complete inability to pass urine with severe lower abdominal distension (acute urinary retention emergency requiring immediate catheterization)"
        ]
    },
    {
        "id": "DOC-CARD-160",
        "icd10": "N17.9",
        "condition": "Acute Kidney Injury (AKI)",
        "specialty": "Nephrology",
        "organ_system": "Urinary & Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO Clinical Practice Guideline for Acute Kidney Injury",
        "source_body": "Kidney Int Suppl",
        "citation": "Kellum JA et al. KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney Int Suppl. 2012;2(1):1-138.",
        "doi_or_source": "10.1038/kisup.2012.1",
        "clinical_evidence": "KDIGO diagnostic criteria define AKI by any of: increase in serum creatinine by ≥ 0.3 mg/dL within 48 hours; increase in serum creatinine to ≥ 1.5 times baseline within 7 days; or urine volume < 0.5 mL/kg/h for 6 hours. Etiologies are categorized into prerenal (hypovolemia, heart failure, sepsis, NSAIDs/ACEi causing decreased renal perfusion; fractional excretion of sodium FeNa < 1%, BUN:creatinine ratio > 20:1); intrinsic renal (acute tubular necrosis [ATN] from ischemia or nephrotoxins, acute interstitial nephritis [AIN], glomerulonephritis; FeNa > 2%, muddy brown granular casts); and postrenal obstructive (nephrolithiasis, BPH, neurogenic bladder; hydronephrosis on renal ultrasound). Core management mandates prompt hemodynamic resuscitation with balanced crystalloids (SMART trial; NEJM 2018), discontinuation of all nephrotoxic agents (NSAIDs, aminoglycosides, IV iodinated contrast), relief of obstruction, and dose-adjustment of all renally cleared drugs.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict fluid balance tracking (intake vs output); avoidance of all nephrotoxic medications (NSAIDs, OTC herbal supplements, contrast dye); protocolized electrolyte dietary restrictions (low potassium, low phosphorus) during oliguric phase.",
            "monitoring_cadence": "Serum creatinine, BUN, electrolytes (potassium, bicarbonate), and urine output every 12-24 hours in hospitalized patients; renal recovery reassessment at 30 and 90 days.",
            "clinical_thresholds": "Absolute indications for urgent renal replacement therapy (dialysis): refractory hyperkalemia (K+ > 6.5 mEq/L with ECG changes), refractory metabolic acidosis (pH < 7.15), refractory pulmonary edema, or uremic complications (pericarditis, encephalopathy)."
        },
        "patient_plain_language": "Acute kidney injury is a sudden, sharp decline in kidney function that occurs over hours or days. When the kidneys suddenly struggle to filter the blood—often due to severe dehydration, an infection, or certain medications—waste products and excess fluids rapidly build up in the body.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current serum creatinine compared to my baseline, and what was the identified trigger for this kidney injury?",
            "safety_question": "Have all potentially harmful medications, like ibuprofen, naproxen, or certain blood pressure pills, been immediately stopped?",
            "action_threshold_question": "Are my blood potassium and acid levels being monitored closely to ensure my heart rhythm remains completely safe?"
        },
        "red_flags": [
            "Sudden severe shortness of breath with fluid in lungs (pulmonary edema), no urine output for >12 hours (anuria), confusion, or cardiac rhythm changes from high potassium"
        ]
    }
]