"""
part20_adv_oncheme_twins.py
"""

PART_20_DISEASES = [
    {
        "id": "DOC-CARD-481",
        "icd10": "G70.00",
        "condition": "Myasthenia Gravis (AChR-Ab Post-Synaptic Junction Failure)",
        "specialty": "Neurology & Neuromuscular",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ADAPT Landmark Trial & International MG Guidelines",
        "source_body": "Lancet Neurology",
        "citation": "Howard JF Jr et al. Safety, Efficacy, and Tolerability of Efgartigimod in Patients with Generalized Myasthenia Gravis (ADAPT). Lancet Neurol. 2021;20(7):526-536.",
        "doi_or_source": "10.1016/S1474-4422(21)00159-9",
        "clinical_evidence": "Myasthenia Gravis involves pathogenic autoantibodies (anti-AChR in 85%, anti-MuSK, anti-LRP4) blocking and destroying post-synaptic nicotinic acetylcholine receptors, producing hallmark FATIGABLE muscle weakness (worsens with repetitive use, improves with rest). The phase 3 ADAPT trial (n=167) proved that neonatal Fc receptor (FcRn) blocker EFGARTIGIMOD produced rapid, significant clinical improvement (68% responders vs 30% placebo; p<0.0001). Pyridostigmine provides symptomatic acetylcholinesterase inhibition; thymectomy is class I recommendation in non-thymomatous generalized AChR+ MG.",
        "solution_protocol": {
            "non_pharmacological_targets": "Thymectomy evaluation (MGTX trial proved thymectomy improves clinical scores and reduces prednisone requirements for 5 years in AChR+ patients age 18-65); avoid medications that worsen MG (aminoglycosides, fluoroquinolones, macrolides, beta-blockers, magnesium IV, iodinated contrast); energy conservation techniques.",
            "monitoring_cadence": "MG Activities of Daily Living (MG-ADL) and Quantitative MG (QMG) scores every 3 months; Negative Inspiratory Force (NIF) and Forced Vital Capacity (FVC) monitoring during worsening; chest CT/MRI for thymoma.",
            "clinical_thresholds": "Serum Anti-AChR binding antibody positive, or repetitive nerve stimulation showing decremental compound muscle action potential (>10% decrement at 3 Hz)."
        },
        "patient_plain_language": "An autoimmune condition where your immune system attacks the docking docks (acetylcholine receptors) on your muscle cells. Nerves can send signals, but the muscles cannot catch them. This causes hallmark 'fatigue weakness': your eyelids droop (ptosis), your vision goes double, and chewing or walking gets progressively weaker as the day goes on, but temporarily improves after a rest nap.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my blood tests show positive acetylcholine receptor (AChR) or MuSK antibodies?",
            "safety_question": "Have I had a chest CT scan to check for a thymoma tumor, and would surgical removal of the thymus gland help cure my weakness?",
            "action_threshold_question": "Am I a candidate for newer targeted FcRn blocker infusions (Efgartigimod) to rapidly wash away the disease antibodies?"
        },
        "red_flags": [
            "Severe difficulty swallowing saliva, choking, or shortness of breath (Myasthenic Crisis - Emergency ICU Airway)",
            "Drop in breathing capacity (FVC <15-20 mL/kg or NIF worse than -20 cmH2O) requiring urgent plasma exchange"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Myasthenia gravis is an autoimmune muscle disorder causing weakness that worsens with activity and improves with rest.",
                "plain_analogy": "A busy electrical plug outlet whose sockets are jammed with plastic safety caps, preventing plugs from connecting.",
                "lifestyle_action": "Schedule difficult physical tasks early in the day, take your Pyridostigmine before meals, and rest frequently."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pyridostigmine oral (Mestinon - Acetylcholinesterase Inhibitor)",
                    "Efgartigimod alfa-fcab (Vyvgart - FcRn Blocker)",
                    "Prednisone oral",
                    "Plasma Exchange / IVIG (for acute crisis)",
                    "Thymectomy (Surgical)"
                ],
                "dosing_gdmt": "Pyridostigmine 60 mg orally every 4-6 hours (max 120 mg q3-4h); Efgartigimod 10 mg/kg IV weekly x 4 cycles.",
                "black_box_warning": "Avoid Fluoroquinolones, Aminoglycosides, and IV Magnesium (precipitates sudden fatal myasthenic respiratory arrest).",
                "organ_clearance_cutoffs": "Pyridostigmine cholinergic excess causes cramping, diarrhea, and bradycardia; treat with glycopyrrolate."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ADAPT-TRIAL",
                "pmid_or_doi": "10.1016/S1474-4422(21)00159-9",
                "cebm_level": 2,
                "sample_size": 167,
                "endpoints": "Efgartigimod achieves rapid, sustained MG-ADL score reduction in 68% of generalized myasthenia patients (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-482",
        "icd10": "G73.1",
        "condition": "Lambert-Eaton Myasthenic Syndrome (LEMS - Pre-Synaptic P/Q-Type VGCC)",
        "specialty": "Neurology & Oncology",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & EFNS Guidelines on LEMS",
        "source_body": "Cochrane Database of Systematic Reviews & Lancet Neurology",
        "citation": "Keogh M et al. Treatment for Lambert-Eaton Myasthenic Syndrome. Cochrane Database Syst Rev. 2011;(2):CD003279.",
        "doi_or_source": "10.1002/14651858.CD003279.pub3",
        "clinical_evidence": "Unlike Myasthenia Gravis, LEMS involves autoantibodies directed against PRE-SYNAPTIC P/Q-type Voltage-Gated Calcium Channels (VGCC), blocking calcium influx and preventing acetylcholine vesicle release. OVER 50-60% OF PATIENTS HAVE SMALL CELL LUNG CANCER (SCLC - Paraneoplastic LEMS). Clinical hallmark: PROXIMAL MUSCLE STRENGTH AND DEEP TENDON REFLEXES TEMPORARILY IMPROVE FOLLOWING BRIEF MAXIMUM EXERCISE (POST-EXERCISE FACILITATION). AMIFAMPRIDINE (3,4-diaminopyridine / 3,4-DAP) blocks potassium channels, prolonging nerve depolarization and restoring muscle strength (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "MANDATORY ONCOLOGICAL SCREENING FOR UNDERLYING SMALL CELL LUNG CANCER (CT chest/abdomen/pelvis and 18F-FDG PET/CT; repeat screening every 3-6 months for at least 2 years if initially negative); physical therapy; fall prevention.",
            "monitoring_cadence": "Repetitive nerve stimulation (low frequency 3 Hz shows decremental response; high frequency 20-50 Hz or 10-second voluntary exercise shows pathognomonic INCREMENTAL RESPONSE >100%); VGCC antibody titers; autonomic testing.",
            "clinical_thresholds": "Positive P/Q-type VGCC antibodies, proximal limb weakness, autonomic dysfunction (dry mouth, erectile dysfunction, sluggish pupils), and hyporeflexia with post-exercise reflex return."
        },
        "patient_plain_language": "A rare condition where antibodies block the microscopic calcium gates at the very tips of your nerves, preventing them from releasing the chemical that tells muscles to contract. Over half of patients have a hidden small cell lung tumor producing these antibodies. Unlike myasthenia gravis, your muscle strength actually feels STRONGER for a few seconds right after a short burst of exercise (post-exercise facilitation). A targeted pill (Amifampridine) restores nerve firing.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did a full-body PET/CT scan look for an underlying small cell lung cancer (SCLC), and will we repeat scans every 6 months?",
            "safety_question": "Did nerve testing show post-exercise facilitation (muscle signals doubling after 10 seconds of exercise)?",
            "action_threshold_question": "Am I taking Amifampridine (3,4-DAP) to keep the nerve channels open and restore my leg strength?"
        },
        "red_flags": [
            "Sudden appearance of a lung mass, cough with blood, or rapid unprovoked weight loss (SCLC malignancy)",
            "Autonomic failure causing severe orthostatic blackouts and urinary retention"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "LEMS is a nerve-muscle disorder where nerves fail to release acetylcholine, often linked to an underlying lung tumor.",
                "plain_analogy": "A garden hose nozzle valve that gets stuck shut, but opens when you repeatedly pump the lever.",
                "lifestyle_action": "Perform regular cancer screening scans, take Amifampridine as directed, and avoid extreme heat."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Amifampridine oral (Firdapse / 3,4-DAP - Class I First Line)",
                    "Pyridostigmine oral (adjunctive)",
                    "IVIG / Plasma Exchange",
                    "Treatment of Underlying SCLC (Chemo/Radiation)"
                ],
                "dosing_gdmt": "Amifampridine 15-30 mg daily in divided doses (3-4 times daily), titrated to max 80 mg daily.",
                "black_box_warning": "Amifampridine carries a risk of epileptic seizures at high doses (>80-100 mg/day); contraindicated in seizure disorders.",
                "organ_clearance_cutoffs": "Dose reduction in renal or hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-LEMS",
                "pmid_or_doi": "10.1002/14651858.CD003279.pub3",
                "cebm_level": 1,
                "sample_size": 980,
                "endpoints": "Amifampridine significantly improves muscle strength scores and compound muscle action potential amplitude (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-483",
        "icd10": "G12.21",
        "condition": "Amyotrophic Lateral Sclerosis (ALS - Mixed Upper & Lower Motor Neuron)",
        "specialty": "Neurology & Neuromuscular",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN Practice Parameter on ALS & Edaravone Trials",
        "source_body": "Neurology & Lancet Neurology",
        "citation": "Writing Group on behalf of the Edaravone (MCI-186) ALS 19 Study Group. Safety and Efficacy of Edaravone in Well-Defined ALS: A Phase 3 Trial. Lancet Neurol. 2017;16(7):505-512.",
        "doi_or_source": "10.1016/S1474-4422(17)30115-1",
        "clinical_evidence": "ALS is a fatal neurodegenerative disorder causing relentless loss of both Upper Motor Neurons (hyperreflexia, spasticity, positive Babinski sign) and Lower Motor Neurons (fasciculations, muscle atrophy, flaccid weakness). RILUZOLE (50 mg BID oral glutamatergic inhibitor) extends tracheostomy-free survival by 2-3 months. IV/oral EDARAVONE (Radicava; free radical scavenger) slows functional decline by 33% on the ALSFRS-R scale in early definite ALS (p=0.001). EARLY NON-INVASIVE VENTILATION (NIV/BiPAP for FVC <50-80%) extends survival by 7-12 months and preserves quality of life.",
        "solution_protocol": {
            "non_pharmacological_targets": "Early multidisciplinary ALS clinic enrollment (significantly prolongs survival); timely non-invasive ventilation (NIV/BiPAP for FVC <50-80% or orthopnea); early percutaneous endoscopic gastrostomy (PEG) feeding tube placement before FVC <50% to maintain nutrition; speech-generating assistive devices.",
            "monitoring_cadence": "ALS Functional Rating Scale-Revised (ALSFRS-R) monthly; upright and supine spirometry (FVC and MIP/MEP every 3 months; >20% supine FVC drop indicates diaphragmatic weakness); liver enzymes on riluzole.",
            "clinical_thresholds": "El Escorial and Gold Coast Diagnostic Criteria: Simultaneous upper and lower motor neuron signs across >=2 body regions (bulbar, cervical, thoracic, lumbosacral) with documented progression."
        },
        "patient_plain_language": "A motor neuron disease (often known as Lou Gehrig's disease) where the nerve cells that control your voluntary muscles gradually waste away. Because both upper nerves in the brain and lower nerves in the spinal cord are affected, it causes a combination of muscle twitching (fasciculations), shrinking (atrophy), and muscle stiffness. Multidisciplinary ALS clinic care, early nighttime breathing support (BiPAP), and protective medicines (Riluzole and Radicava) prolong survival and comfort.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Forced Vital Capacity (FVC) sitting and lying down, and is it time to begin non-invasive nighttime BiPAP?",
            "safety_question": "Am I taking Riluzole twice daily, and are my liver function enzymes being monitored every month?",
            "action_threshold_question": "Have we discussed early placement of a PEG feeding tube while my lung breathing function is still strong enough for the procedure?"
        },
        "red_flags": [
            "Severe orthopnea (inability to breathe while lying flat on the back, indicating bilateral diaphragm paralysis)",
            "Choking on thin liquids and rapid weight loss from progressive bulbar swallowing failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "ALS is a motor nerve disease causing gradual weakness of voluntary muscles throughout the body.",
                "plain_analogy": "Telephone transmission poles and household wiring slowly breaking down, cutting off power to household appliances.",
                "lifestyle_action": "Attend an ALS specialty clinic, start nighttime breathing support (BiPAP) early, and use assistive technology."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Riluzole oral (Rilutek 50 mg BID - Extends Survival)",
                    "Edaravone IV/oral (Radicava - Free Radical Scavenger)",
                    "Sodium Phenylbutyrate/Taurursodiol (Relyvrio)",
                    "Non-Invasive Ventilation (BiPAP - Class I)"
                ],
                "dosing_gdmt": "Riluzole 50 mg orally every 12 hours on an empty stomach; Edaravone 60 mg IV daily x 14 days in first 28-day cycle, then 10 of 14 days.",
                "black_box_warning": "Riluzole causes asymptomatic liver transaminase elevations; check LFTs monthly x 3 months, then quarterly.",
                "organ_clearance_cutoffs": "Edaravone contains sodium bisulfite; contraindicated in severe sulfite allergy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EDARAVONE-ALS-19",
                "pmid_or_doi": "10.1016/S1474-4422(17)30115-1",
                "cebm_level": 2,
                "sample_size": 137,
                "endpoints": "Edaravone slows ALS functional rating scale decline by 33% compared to placebo over 24 weeks (p=0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-484",
        "icd10": "G61.0",
        "condition": "Guillain-Barré Syndrome (Acute Inflammatory Demyelinating Polyneuropathy)",
        "specialty": "Neurology & Critical Care",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & International GBS Guidelines",
        "source_body": "Cochrane Database of Systematic Reviews & Lancet Neurology",
        "citation": "van Doorn PA et al. Clinical Features, Pathogenesis, and Treatment of Guillain-Barré Syndrome. Lancet Neurol. 2008;7(10):939-950.",
        "doi_or_source": "10.1016/S1474-4422(08)70215-1",
        "clinical_evidence": "GBS is an acute autoimmune post-infectious demyelinating polyneuropathy (commonly following Campylobacter jejuni, CMV, or respiratory illness) presenting with RAPIDLY ASCENDING SYMMETRICAL FLACCID PARALYSIS, AREFLEXIA, and autonomic instability. CORTICOSTEROIDS ARE COMPLETELY INEFFECTIVE AND HARMFUL. INTRAVENOUS IMMUNOGLOBULIN (IVIG 0.4 g/kg/day x 5 days) OR THERAPEUTIC PLASMA EXCHANGE (PE 4-5 sessions) initiated within 2 weeks halts progression and significantly accelerates motor recovery.",
        "solution_protocol": {
            "non_pharmacological_targets": "Admit to ICU/stepdown for close respiratory mechanics monitoring (the '20/30/40 rule': FVC <20 mL/kg, MIP <-30 cmH2O, MEP <40 cmH2O indicates elective intubation); deep vein thrombosis prophylaxis; aggressive neuropathic pain management (gabapentin); physical therapy.",
            "monitoring_cadence": "Serial bedside Forced Vital Capacity (FVC) and Negative Inspiratory Force (NIF) every 2-4 hours; continuous cardiac telemetry (fatal dysautonomia occurs in 20%); Erasmus GBS Outcome Score (EGOS).",
            "clinical_thresholds": "CSF examination demonstrating ALBUMINOCYTOLOGIC DISSOCIATION (elevated protein >45-100 mg/dL with normal WBC count <5-10 cells/mcL); nerve conduction showing demyelinating features."
        },
        "patient_plain_language": "A rapid, temporary immune reaction (often triggered by a stomach bug or cold 1 to 3 weeks earlier) where your immune system attacks the insulation (myelin) covering your peripheral nerves. Weakness starts in your toes and legs and climbs upward toward your chest, along with numbness and loss of reflexes. Corticosteroids do NOT work; emergency hospital care with IV antibody infusions (IVIG) or plasma filtering clears the attack while nerves heal.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are my breathing parameters (Forced Vital Capacity and NIF) being measured every 2 to 4 hours to protect my lungs?",
            "safety_question": "Did my spinal tap show 'albuminocytologic dissociation' (high protein with zero infection cells)?",
            "action_threshold_question": "Why are steroid medications strictly avoided, and have we started IVIG antibody infusions right away?"
        },
        "red_flags": [
            "Rapidly ascending paralysis reaching the chest with inability to count to 20 in a single breath (Emergency Intubation)",
            "Severe blood pressure swings (from 200/110 to 70/40 mmHg) and heart rate drops (Dysautonomia Emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Guillain-Barré syndrome is rapid autoimmune nerve inflammation causing ascending leg and body paralysis.",
                "plain_analogy": "A lightning storm stripping the protective rubber coating off electrical power lines, cutting power to distant switches.",
                "lifestyle_action": "Seek emergency hospital ICU care immediately; early IVIG infusions stop nerve damage, and breathing must be monitored."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intravenous Immunoglobulin (IVIG 0.4 g/kg/day x 5 days - Class I)",
                    "Therapeutic Plasma Exchange (5 sessions over 10-14 days)",
                    "Gabapentin / Pregabalin (for neuropathic pain)",
                    "Enoxaparin SubQ (DVT Prophylaxis)"
                ],
                "dosing_gdmt": "IVIG 2 g/kg total dose divided over 5 consecutive days (0.4 g/kg/day); or Plasma Exchange 200-250 mL/kg over 5 sessions.",
                "black_box_warning": "STRICT CONTRAINDICATION: Systemic Corticosteroids (Prednisone) DELAY recovery in GBS and are proven ineffective.",
                "organ_clearance_cutoffs": "IVIG requires screening for IgA deficiency (anaphylaxis risk) and monitoring of renal function and aseptic meningitis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-GBS-IVIG",
                "pmid_or_doi": "10.1002/14651858.CD002063.pub6",
                "cebm_level": 1,
                "sample_size": 1500,
                "endpoints": "IVIG and plasma exchange produce equivalent superior recovery, halving time on mechanical ventilation compared to supportive care."
            }
        }
    },
    {
        "id": "DOC-CARD-485",
        "icd10": "G61.81",
        "condition": "Chronic Inflammatory Demyelinating Polyneuropathy (CIDP)",
        "specialty": "Neurology & Neuromuscular",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: PATH Landmark Trial & EAN/PNS Guidelines",
        "source_body": "Lancet Neurology",
        "citation": "van Schaik IN et al. Subcutaneous Immunoglobulin for Maintenance Treatment in CIDP (PATH): A Randomised, Double-Blind, Placebo-Controlled, Phase 3 Trial. Lancet Neurol. 2018;17(1):35-46.",
        "doi_or_source": "10.1016/S1474-4422(17)30378-2",
        "clinical_evidence": "CIDP is a chronic, progressive or relapsing-remitting symmetric sensorimotor polyradiculoneuropathy progressing for >8 WEEKS (differentiating it from acute GBS). Unlike GBS, CIDP RESPONDS WELL TO CORTICOSTEROIDS. The phase 3 PATH trial (n=245) proved that weekly SUB-CUTANEOUS IMMUNOGLOBULIN (SCIG 0.2 g/kg or 0.4 g/kg) achieved 67-78% relapse-free survival compared to 37% placebo (p=0.0007), providing convenient at-home maintenance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Adherence to maintenance immunoglobulin or steroid-sparing therapy; supervised physical and occupational therapy; orthotic devices (ankle-foot orthoses / AFOs for bilateral foot drop); fall prevention.",
            "monitoring_cadence": "Inflammatory Neuropathy Cause and Treatment (INCAT) disability score and Medical Research Council (MRC) sum score every 3-6 months; annual electrodiagnostic testing.",
            "clinical_thresholds": "Electrodiagnostic evidence of primary demyelinating neuropathy (conduction velocity slowing, conduction block, prolonged distal latencies) in >=2 nerves, progressing for >=8 weeks."
        },
        "patient_plain_language": "A chronic, ongoing autoimmune condition where your immune system continuously damages the insulation around your nerves over months or years. Unlike GBS which strikes suddenly and heals, CIDP slowly causes weakness and numbness in both legs and arms that lasts longer than 2 months. Fortunately, CIDP responds very well to regular antibody infusions (IVIG or easy at-home under-the-skin SCIG) or steroid pills.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did nerve conduction tests prove chronic demyelination across multiple nerves lasting longer than 8 weeks?",
            "safety_question": "Am I a candidate for at-home subcutaneous immunoglobulin (SCIG) self-injections instead of hospital IV infusions?",
            "action_threshold_question": "What is my current INCAT disability score, and are my ankle-foot braces helping me walk safely?"
        },
        "red_flags": [
            "Rapid loss of hand grip strength making it impossible to hold utensils or turn doorknobs",
            "Severe progressive sensory ataxia causing frequent falls in the dark"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "CIDP is chronic, long-term autoimmune nerve inflammation causing progressive arm and leg weakness.",
                "plain_analogy": "A slow, continuous chemical drip that constantly dissolves the rubber insulation off home electrical wiring.",
                "lifestyle_action": "Take your maintenance immunoglobulin infusions faithfully, use ankle braces to prevent tripping, and do physical therapy."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intravenous Immunoglobulin (IVIG 2 g/kg loading)",
                    "Subcutaneous Immunoglobulin (SCIG - PATH Trial Maintenance)",
                    "Oral Prednisone / Pulse IV Dexamethasone",
                    "Plasma Exchange"
                ],
                "dosing_gdmt": "IVIG 2 g/kg divided over 2-5 days loading; followed by SCIG 0.2-0.4 g/kg once weekly at home.",
                "black_box_warning": "Monitor for systemic steroid complications if corticosteroids are chosen as first line (osteoporosis, hyperglycemia).",
                "organ_clearance_cutoffs": "SCIG requires monitoring for local infusion-site swelling and erythema."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PATH-TRIAL",
                "pmid_or_doi": "10.1016/S1474-4422(17)30378-2",
                "cebm_level": 2,
                "sample_size": 245,
                "endpoints": "Subcutaneous immunoglobulin maintenance therapy prevents CIDP relapse in >78% of patients (p=0.0007)."
            }
        }
    },
    {
        "id": "DOC-CARD-486",
        "icd10": "G50.0",
        "condition": "Trigeminal Neuralgia (Tic Douloureux - Neurovascular Compression)",
        "specialty": "Neurology & Neurosurgery",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN/EFNS Guidelines on Trigeminal Neuralgia",
        "source_body": "Neurology",
        "citation": "Gronseth G et al. Practice Parameter: The Diagnostic Evaluation and Treatment of Trigeminal Neuralgia (An Evidence-Based Review). Neurology. 2008;71(15):1183-1190.",
        "doi_or_source": "10.1212/01.wnl.0000326598.83183.04",
        "clinical_evidence": "Classic TN involves paroxysmal, excruciating, electric shock-like lancinating unilateral facial pain in V2/V3 distributions, triggered by innocuous tactile stimuli (touching face, brushing teeth, chewing, breeze). Caused by neurovascular compression of the trigeminal root entry zone (most commonly superior cerebellar artery). CARBAMAZEPINE (200-1200 mg/day) or OXCARBAZEPINE is first-line medical therapy, achieving initial pain relief in >80%. MICROVASCULAR DECOMPRESSION (MVD / Jannetta procedure) provides definitive cure (>70-80% pain-free at 10 years).",
        "solution_protocol": {
            "non_pharmacological_targets": "Screening for HLA-B*1502 allele prior to carbamazepine in patients of Asian descent (prevents fatal SJS/TEN); avoid known tactile facial triggers; soft room-temperature diet during flares; neurosurgical consultation for MVD if refractory or drug-intolerant.",
            "monitoring_cadence": "High-resolution 3D T2-weighted MRI brain (CISS / FIESTA sequence) demonstrating neurovascular contact with the trigeminal nerve root; complete blood count, sodium, and liver function on carbamazepine.",
            "clinical_thresholds": "Brief, unilateral, electric-shock-like pains, abrupt in onset and termination, strictly limited to the distribution of one or more divisions of the trigeminal nerve."
        },
        "patient_plain_language": "Known as one of the most agonizing pains in human medicine ('Tic Douloureux'). An artery at the base of your brain pulses against your trigeminal facial nerve like a hammer on an exposed electrical wire. The slightest light touch—a cool breeze, brushing your teeth, or chewing—triggers lightning bolts of excruciating electrical pain shooting across your cheek or jaw. A specific nerve pill (Carbamazepine) or a keyhole brain surgery to pad the nerve (MVD) stops the pain completely.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did a high-resolution 3D MRI (FIESTA sequence) reveal an artery compressing my trigeminal nerve root?",
            "safety_question": "Was my genetic test (HLA-B*1502) checked before starting Carbamazepine to prevent severe skin allergic reactions?",
            "action_threshold_question": "Am I a candidate for Microvascular Decompression (MVD) surgery to place a tiny Teflon pad between the artery and nerve?"
        },
        "red_flags": [
            "Severe pain preventing eating and drinking, causing acute dehydration and rapid weight loss",
            "Sudden spreading skin rash with fever or severe mouth ulcers on Carbamazepine (SJS/TEN Emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Trigeminal neuralgia is excruciating, electric-shock facial pain triggered by light touches on the cheek or jaw.",
                "plain_analogy": "An exposed high-voltage spark plug wire vibrating against a metal pipe, firing wild electrical shocks with every pulse.",
                "lifestyle_action": "Take your nerve pain medication faithfully, eat soft foods during pain flares, and consult neurosurgery for nerve padding."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Carbamazepine oral (Tegretol - Class I First Line)",
                    "Oxcarbazepine oral (Trileptal)",
                    "Microvascular Decompression (MVD - Curative Neurosurgery)",
                    "Stereotactic Radiosurgery (Gamma Knife)"
                ],
                "dosing_gdmt": "Carbamazepine 100-200 mg BID, titrated by 100-200 mg every 2-3 days to 400-1,200 mg/day in divided doses.",
                "black_box_warning": "BLACK BOX WARNING: Fatal dermatological reactions (SJS/TEN) and aplastic anemia/agranulocytosis; screen HLA-B*1502.",
                "organ_clearance_cutoffs": "Carbamazepine frequently induces hyponatremia (SIADH) and CYP3A4 auto-induction; check serum sodium and CBC."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAN-EFNS-TN",
                "pmid_or_doi": "10.1212/01.wnl.0000326598.83183.04",
                "cebm_level": 1,
                "sample_size": 1850,
                "endpoints": "Carbamazepine achieves complete initial pain relief in >80% of TN; MVD provides durable 10-year cure in >75%."
            }
        }
    },
    {
        "id": "DOC-CARD-487",
        "icd10": "M35.00",
        "condition": "Sjögren's Disease (Anti-SSA/Ro Autoimmune Exocrinopathy)",
        "specialty": "Rheumatology & Ophthalmology",
        "organ_system": "Immune & Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACR-EULAR Classification Criteria & EULAR Recommendations",
        "source_body": "Annals of the Rheumatic Diseases",
        "citation": "Ramos-Casals M et al. EULAR Recommendations for the Management of Sjögren's Syndrome with Topical and Systemic Therapies. Ann Rheum Dis. 2020;79(1):3-18.",
        "doi_or_source": "10.1136/annrheumdis-2019-216114",
        "clinical_evidence": "Sjögren's is a systemic autoimmune exocrinopathy characterized by lymphocytic infiltration of salivary and lacrimal glands, producing Keratoconjunctivitis Sicca (severe dry eyes) and Xerostomia (severe dry mouth). Autoantibodies (Anti-SSA/Ro in 70-80%, Anti-SSB/La) are diagnostic. SJÖGREN'S CARRIES A 15-TO-40-FOLD ELEVATED RISK OF NON-HODGKIN B-CELL LYMPHOMA (MALT lymphoma of the parotid). Muscarinic agonists (Pilocarpine, Cevimeline) stimulate secretion; Hydroxychloroquine treats systemic arthralgias.",
        "solution_protocol": {
            "non_pharmacological_targets": "Preservative-free artificial tears and lubricating ophthalmic ointments; frequent sips of water, sugar-free gum/lozenges containing xylitol; intensive preventive dental hygiene every 3-4 months (loss of saliva accelerates rampant dental caries); avoid anticholinergic medications.",
            "monitoring_cadence": "Ocular Staining Score (OSS) with lissamine green / fluorescein; Schirmer test (<=5 mm wetting at 5 min is abnormal); unstimulated whole salivary flow rate (<=0.1 mL/min); annual palpation of parotid glands and serum protein electrophoresis for M-spike (lymphoma surveillance).",
            "clinical_thresholds": "ACR-EULAR score >=4 points (Anti-SSA positive = 3 points; labial salivary gland biopsy with focus score >=1 focus/4 mm2 = 3 points)."
        },
        "patient_plain_language": "An autoimmune condition where your immune cells attack and dry out the moisture-producing glands in your body, particularly your tear glands and salivary glands. Your eyes feel like they are full of sandpaper or grit, and your mouth becomes so dry you cannot swallow dry crackers without water. Because saliva protects your teeth, aggressive dental care is critical, and doctors must monitor for swollen parotid glands to screen for lymphoma.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my blood tests show positive Anti-SSA (Ro) antibodies or did a lip biopsy show lymphocytic focus score >=1?",
            "safety_question": "Have I been prescribed Pilocarpine or Cevimeline pills to stimulate natural saliva and tear production?",
            "action_threshold_question": "Am I using preservative-free lubricating eye drops and seeing my dentist every 3 to 4 months for fluoride treatments?"
        },
        "red_flags": [
            "Rapid, firm, persistent enlargement of one parotid salivary gland in the cheek (B-Cell MALT Lymphoma)",
            "Persistent dry eyes developing corneal ulceration or severe visual blurring"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sjögren's disease is an autoimmune condition causing severe dry eyes and dry mouth by attacking moisture glands.",
                "plain_analogy": "An automated lawn sprinkler line whose water supply valves have rusted shut, drying out the grass and plants.",
                "lifestyle_action": "Use preservative-free eye drops hourly, chew xylitol gum, brush and floss diligently, and report cheek swellings."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pilocarpine oral (Salagen 5 mg TID-QID)",
                    "Cevimeline oral (Evoxac 30 mg TID)",
                    "Cyclosporine Ophthalmic Emulsion (Restasis / Cequa)",
                    "Hydroxychloroquine (Plaquenil for systemic arthralgias)"
                ],
                "dosing_gdmt": "Pilocarpine 5 mg orally 3-4 times daily with meals; Cevimeline 30 mg TID; Hydroxychloroquine 5 mg/kg/day.",
                "black_box_warning": "Pilocarpine can cause profuse diaphoresis, urinary urgency, and bronchospasm (avoid in severe asthma).",
                "organ_clearance_cutoffs": "Lifelong ophthalmology screening for hydroxychloroquine retinal toxicity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EULAR-SJOGREN",
                "pmid_or_doi": "10.1136/annrheumdis-2019-216114",
                "cebm_level": 1,
                "sample_size": 2300,
                "endpoints": "Muscarinic agonists combined with topical cyclosporine significantly improve tear film stability and salivary flow."
            }
        }
    },
    {
        "id": "DOC-CARD-488",
        "icd10": "M34.0",
        "condition": "Diffuse Cutaneous Systemic Sclerosis (Anti-Scl-70 / Scleroderma Renal Crisis)",
        "specialty": "Rheumatology & Nephrology",
        "organ_system": "Connective & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR/EUSTAR Recommendations on Systemic Sclerosis",
        "source_body": "Annals of the Rheumatic Diseases",
        "citation": "Kowal-Bielecka O et al. Update of EULAR Recommendations for the Treatment of Systemic Sclerosis. Ann Rheum Dis. 2017;76(8):1327-1339.",
        "doi_or_source": "10.1136/annrheumdis-2016-209909",
        "clinical_evidence": "Diffuse systemic sclerosis causes widespread skin fibrosis proximal to elbows/knees, driven by vasculopathy and autoantibodies (Anti-Scl-70 / Topoisomerase I in 30%, Anti-RNA Polymerase III). Anti-RNA Polymerase III carries high risk for SCLERODERMA RENAL CRISIS (SRC: acute malignant hypertension, microangiopathic hemolytic anemia, and oliguric AKI). ACE INHIBITORS (CAPTOPRIL TITRATED AGGRESSIVELY) ARE LIFE-SAVING FOR SRC. CORTICOSTEROIDS (PREDNISONE >15 MG/DAY) DIRECTLY PRECIPITATE RENAL CRISIS AND ARE STRICTLY CONTRAINDICATED.",
        "solution_protocol": {
            "non_pharmacological_targets": "MANDATORY HOME BLOOD PRESSURE MONITORING DAILY (any systolic BP rise >20-30 mmHg requires immediate emergency contact); cold protection for severe Raynaud's; early esophageal reflux management with high-dose PPI; lung screening.",
            "monitoring_cadence": "Annual High-Resolution Chest CT (HRCT) and PFTs (FVC and DLCO) for Interstitial Lung Disease; annual echocardiogram and NT-proBNP for Pulmonary Arterial Hypertension; daily home BP log.",
            "clinical_thresholds": "Skin thickening proximal to elbows and knees, Raynaud phenomenon with abnormal nailfold capillaroscopy, and positive Anti-Scl-70 or Anti-RNA Polymerase III antibodies."
        },
        "patient_plain_language": "A serious autoimmune condition where your body overproduces collagen scar tissue throughout your skin and internal organs. The skin on your fingers, arms, chest, and face becomes tight, shiny, and hard like leather. It can cause blood vessel spasms (Raynaud's), heartburn, lung scarring, and sudden kidney crises. Steroids are dangerous poisons in this condition because they trigger kidney failure, but blood pressure pills (Captopril) protect your kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I carry the Anti-RNA Polymerase III antibody that puts me at high risk for Scleroderma Renal Crisis?",
            "safety_question": "Why is taking high-dose Prednisone steroid pills strictly forbidden for my diffuse scleroderma?",
            "action_threshold_question": "Why is taking my blood pressure at home every single morning the most important life-saving habit I can have?"
        },
        "red_flags": [
            "Sudden jump in blood pressure (>140/90 mmHg or 20 mmHg increase) with headache and blurry vision (Scleroderma Renal Crisis - EMERGENCY CAPTOPRIL)",
            "Rapidly worsening shortness of breath indicating aggressive Interstitial Lung Disease (ILD)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Diffuse scleroderma is an autoimmune disease causing tightening of the skin and scarring of kidneys and lungs.",
                "plain_analogy": "A flexible leather jacket left outside in a deep freeze that turns stiff, hard, and unbendable.",
                "lifestyle_action": "Check and record your blood pressure every single morning at home, keep your hands warm, and never take high-dose steroids."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Captopril oral (Short-Acting ACEi - LIFE-SAVING FOR RENAL CRISIS)",
                    "Mycophenolate Mofetil (CellCept for progressive skin/lung disease)",
                    "Nintedanib oral (OFEV - for SSc-ILD)",
                    "Tocilizumab (Actemra)"
                ],
                "dosing_gdmt": "Captopril 12.5-25 mg q8h rapidly titrated to max 100 mg TID targeting SBP 110-120 mmHg; Mycophenolate 1-1.5 g BID.",
                "black_box_warning": "STRICT CONTRAINDICATION: Corticosteroids (Prednisone >15 mg/day) directly trigger fatal Scleroderma Renal Crisis.",
                "organ_clearance_cutoffs": "Avoid beta-blockers (exacerbate severe peripheral Raynaud vasospasm and digital ulceration)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EUSTAR-SCLERODERMA",
                "pmid_or_doi": "10.1136/annrheumdis-2016-209909",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Early prompt ACE inhibitor therapy reduces 1-year mortality in Scleroderma Renal Crisis from >85% to <25%."
            }
        }
    },
    {
        "id": "DOC-CARD-489",
        "icd10": "M34.1",
        "condition": "Limited Cutaneous Systemic Sclerosis (CREST Syndrome / Anti-Centromere)",
        "specialty": "Rheumatology & Cardiology",
        "organ_system": "Connective & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR Systemic Sclerosis Guidelines & DETECT Study",
        "source_body": "Annals of the Rheumatic Diseases",
        "citation": "Coghlan JG et al. Evidence-Based Detection of Pulmonary Arterial Hypertension in Systemic Sclerosis (DETECT). Ann Rheum Dis. 2014;73(7):1340-1349.",
        "doi_or_source": "10.1136/annrheumdis-2013-203301",
        "clinical_evidence": "Limited cutaneous SSc is defined by skin thickening restricted to hands, face, and distal extremities, characterized by the classic CREST SYNDROME: Calcinosis cutis, Raynaud phenomenon, Esophageal dysmotility, Sclerodactyly, and Telangiectasia. Strongly associated with ANTI-CENTROMERE ANTIBODIES (ACA in >70-80%). Unlike diffuse SSc, limited SSc has low risk of renal crisis or severe ILD, but carries a high 10-15% cumulative risk of LATE-ONSET PULMONARY ARTERIAL HYPERTENSION (PAH). ANNUAL SCREENING WITH ECHOCARDIOGRAM, DLCO, AND THE DETECT ALGORITHM IS MANDATORY.",
        "solution_protocol": {
            "non_pharmacological_targets": "MANDATORY ANNUAL SCREENING FOR PULMONARY ARTERIAL HYPERTENSION (DETECT algorithm, DLCO, and echo); strict cold avoidance and heated gloves for Raynaud's; prompt treatment of infected digital ulcers; elevate head of bed for reflux.",
            "monitoring_cadence": "Annual echocardiogram (measuring tricuspid regurgitant jet velocity); annual PFTs (disproportionate drop in DLCO with preserved FVC is the earliest red flag for PAH); annual NT-proBNP.",
            "clinical_thresholds": "Anti-Centromere Antibodies (ACA positive) with distal sclerodactyly, Raynaud's, and telangiectasias on face/hands."
        },
        "patient_plain_language": "A milder, slower-moving form of scleroderma often called CREST syndrome. Skin thickening is limited to your fingers and face. The 5 hallmark signs are: calcium lumps under the skin, cold white fingers in the cold (Raynaud's), heartburn difficulty swallowing, claw-like finger tightening (sclerodactyly), and red spider spots on your lips and palms (telangiectasias). The main long-term danger is developing high blood pressure in your lungs (PAH), so a yearly heart ultrasound is essential.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did blood tests confirm Anti-Centromere Antibodies (ACA)?",
            "safety_question": "Is my annual echocardiogram and lung diffusion (DLCO) breathing test scheduled to detect early pulmonary hypertension?",
            "action_threshold_question": "What medications (like calcium channel blockers or sildenafil) will protect my fingers from painful cold-induced sores?"
        },
        "red_flags": [
            "New-onset shortness of breath when walking flat ground, with lightheadedness (Pulmonary Arterial Hypertension)",
            "Painful, black, infected ulcers on the tips of the fingers (Digital Gangrene from severe Raynaud's)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Limited scleroderma (CREST) causes cold-sensitive white fingers, heartburn, tight skin on fingers, and lung pressure risk.",
                "plain_analogy": "Rubber bands wound tightly around the fingers while cold wind causes the small fuel pipes to freeze shut.",
                "lifestyle_action": "Wear heated mittens in cold weather, take your reflux medicine, and get a yearly heart ultrasound to check lung pressure."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Amlodipine / Nifedipine oral (DHP-CCB for Raynaud's)",
                    "Sildenafil oral (Viagra for refractory Raynaud's/digital ulcers)",
                    "Omeprazole / Vonoprazan (High-dose for reflux)",
                    "Bosentan / Ambrisentan (if PAH develops)"
                ],
                "dosing_gdmt": "Nifedipine ER 30-60 mg daily; Sildenafil 20 mg TID for ischemic digital ulcers; high-dose PPI therapy.",
                "black_box_warning": "Avoid beta-blockers and triptan migraine medications (trigger severe peripheral arterial vasospasm).",
                "organ_clearance_cutoffs": "Dose adjustments for hepatic and renal function with PDE5 inhibitors."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DETECT-STUDY",
                "pmid_or_doi": "10.1136/annrheumdis-2013-203301",
                "cebm_level": 1,
                "sample_size": 466,
                "endpoints": "The two-step DETECT algorithm identifies early pulmonary hypertension in systemic sclerosis with 96% sensitivity."
            }
        }
    },
    {
        "id": "DOC-CARD-490",
        "icd10": "M45.9",
        "condition": "Ankylosing Spondylitis (Axial Spondyloarthritis - HLA-B27 Bamboo Spine)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: MEASURE & COAST Landmark Trials & ASAS/EULAR Guidelines",
        "source_body": "Lancet & New England Journal of Medicine",
        "citation": "van der Heijde D et al. 2016 Update of the ASAS/EULAR Management Recommendations for Axial Spondyloarthritis. Ann Rheum Dis. 2017;76(6):978-991.",
        "doi_or_source": "10.1136/annrheumdis-2016-209909",
        "clinical_evidence": "Axial spondyloarthritis is characterized by immune inflammation of the sacroiliac joints (sacroiliitis) and spine, driven by HLA-B27 and the IL-23/IL-17 pathway, causing syndesmophyte formation and spinal fusion ('Bamboo Spine'). Hallmark: INFLAMMATORY BACK PAIN (onset age <40, insidious onset, IMPROVES WITH EXERCISE, WORSENS WITH REST, nocturnal back pain). CONTINUOUS NSAIDs (Celecoxib, Naproxen) are first-line; Biologics (TNF INHIBITORS like Adalimumab/Infliximab or IL-17 INHIBITORS like Secukinumab/Ixekizumab) achieve ASAS40 response in >60% and arrest radiographic spinal progression.",
        "solution_protocol": {
            "non_pharmacological_targets": "Lifelong regular physical exercise and spinal extension physical therapy (preserves chest expansion and spinal mobility; swimming and daily stretching are foundational); complete smoking cessation (smoking accelerates spinal fusion and syndesmophyte growth); maintain erect posture.",
            "monitoring_cadence": "BASDAI (Bath Ankylosing Spondylitis Disease Activity Index) and ASDAS (Ankylosing Spondylitis Disease Activity Score); annual assessment of cervical/lumbar mobility (Schober test) and chest expansion; annual screening for anterior uveitis and aortic regurgitation.",
            "clinical_thresholds": "Radiographic sacroiliitis on pelvic X-ray (modified New York criteria) or active sacroiliac bone marrow edema on MRI (ASAS criteria) in a patient with chronic inflammatory back pain."
        },
        "patient_plain_language": "An autoimmune arthritis that attacks your lower back and pelvic joints (sacroiliac joints), strongly linked to the HLA-B27 gene. Unlike common mechanical back pain, this pain is worst in the morning with stiffness lasting over 30 minutes, feels BETTER when you walk or exercise, and wakes you up in the second half of the night. If untreated, bones in the spine fuse together like solid bamboo. Daily stretching, anti-inflammatory pills, and biologic injections keep your spine flexible.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did an MRI or X-ray of my pelvis confirm inflammation or damage in my sacroiliac joints (sacroiliitis)?",
            "safety_question": "Was my blood test positive for the HLA-B27 gene marker?",
            "action_threshold_question": "Am I a candidate for biologic injections (anti-TNF or anti-IL-17) to stop my spine from fusing together?"
        },
        "red_flags": [
            "Sudden red, painful, light-sensitive eye with blurry vision (Acute Anterior Uveitis - Emergency Ophthalmologist)",
            "Severe neck pain after minor trauma (high risk of unstable spinal fracture through fused spine)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ankylosing spondylitis is autoimmune back arthritis that improves with exercise and can fuse the spine.",
                "plain_analogy": "Door hinges that rust and seize up overnight when sitting still, but loosen up after you swing the door back and forth.",
                "lifestyle_action": "Exercise and stretch your back every single day, never smoke, sleep flat without thick pillows, and take your biologics."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Adalimumab / Infliximab (Anti-TNF Biologics - Class I)",
                    "Secukinumab / Ixekizumab (Anti-IL-17A Inhibitors)",
                    "Celecoxib / Naproxen (Continuous First Line NSAIDs)",
                    "Upadacitinib (JAK Inhibitor)"
                ],
                "dosing_gdmt": "Adalimumab 40 mg SC every 2 weeks; or Secukinumab 150 mg SC monthly; Celecoxib 200-400 mg daily.",
                "black_box_warning": "Screen for latent tuberculosis and hepatitis B prior to initiating any anti-TNF or anti-IL-17 biologic.",
                "organ_clearance_cutoffs": "IL-17 inhibitors can exacerbate inflammatory bowel disease; contraindicated in active Crohn's disease."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MEASURE-1-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1404916",
                "cebm_level": 2,
                "sample_size": 371,
                "endpoints": "Secukinumab produces rapid, sustained ASAS40 clinical improvement and suppresses spinal inflammation (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-491",
        "icd10": "M35.3",
        "condition": "Polymyalgia Rheumatica (PMR - Rapid Low-Dose Corticosteroid Response)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACR/EULAR PMR Guidelines & SAPHYR Landmark Trial",
        "source_body": "Annals of the Rheumatic Diseases & NEJM",
        "citation": "Dejaco C et al. 2015 Recommendations for the Management of Polymyalgia Rheumatica: A European League Against Rheumatism/American College of Rheumatology Collaborative Initiative. Ann Rheum Dis. 2015;74(10):1799-1807.",
        "doi_or_source": "10.1136/annrheumdis-2015-207992",
        "clinical_evidence": "PMR occurs almost exclusively in adults aged >50, presenting with sudden-onset bilateral aching and severe morning stiffness (>45 minutes) in the shoulder and pelvic girdles, accompanied by marked elevation in ESR (>40-50 mm/h) and CRP. Hallmark: DRAMATIC CLINICAL RESPONSE WITHIN 48-72 HOURS TO LOW-DOSE ORAL PREDNISONE (12.5-20 mg/day; failure to improve within 72 hours strongly suggests an alternative diagnosis). PMR is tightly linked with GIANT CELL ARTERITIS (GCA; co-occurs in 15-20%; temporal artery evaluation mandatory).",
        "solution_protocol": {
            "non_pharmacological_targets": "Gradual slow corticosteroid taper over 12-24 months (rapid tapering triggers relapse in >50%); osteoporosis prophylaxis (calcium, vitamin D, and bisphosphonate); regular low-impact exercise.",
            "monitoring_cadence": "ESR and CRP monitoring prior to every dose reduction; screen at EVERY visit for GCA symptoms (headache, scalp tenderness, jaw claudication, visual loss); blood pressure and blood glucose checks.",
            "clinical_thresholds": "Age >=50, bilateral shoulder and hip girdle aching with morning stiffness >45 minutes, elevated ESR/CRP, and dramatic >70% symptom relief within 72 hours of low-dose prednisone."
        },
        "patient_plain_language": "An inflammatory condition that strikes adults over age 50, causing severe stiffness and aching in both shoulders, neck, and hips. In the morning, you may feel so stiff you cannot raise your arms to brush your hair or put on a coat, or get out of a low chair. It is famous for how quickly it responds: taking a modest dose of Prednisone steroid pills melts the pain away within 48 to 72 hours like magic.",
        "doctor_consultation_checklist": {
            "parameter_question": "Why must my steroid medicine (Prednisone) be tapered down very slowly over 1 to 2 years to prevent a flare?",
            "safety_question": "Have I been screened for Giant Cell Arteritis (GCA) signs, such as temple headaches, jaw pain when chewing, or vision changes?",
            "action_threshold_question": "Am I taking calcium, Vitamin D, and bone-strengthening medicine to protect my bones while on steroids?"
        },
        "red_flags": [
            "Sudden severe headache in the temples, scalp pain when brushing hair, or jaw fatigue while chewing (Giant Cell Arteritis)",
            "Sudden, painless temporary darkness or loss of vision in one eye (Amaurosis Fugax - Emergency High-Dose IV Steroids)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "PMR is inflammatory stiffness in the shoulders and hips in older adults that rapidly vanishes with low-dose steroids.",
                "plain_analogy": "A bicycle chain whose links are seized with morning frost, instantly rolling smoothly once sprayed with warm oil.",
                "lifestyle_action": "Take your Prednisone every morning with breakfast, taper only as instructed by your doctor, and report temple pain immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral (12.5-20 mg/day - Dramatic Diagnostic Response)",
                    "Sarilumab SubQ (Kevzara - Anti-IL-6 approved for PMR)",
                    "Methotrexate oral (Steroid-sparing)",
                    "Calcium + Vitamin D3 + Alendronate"
                ],
                "dosing_gdmt": "Prednisone 15 mg once daily x 3-4 weeks, then slow taper by 1 mg/month; Sarilumab 200 mg SC every 2 weeks.",
                "black_box_warning": "Failure to achieve >70% symptom relief within 72 hours of starting 15-20 mg prednisone MANDATES rethinking the diagnosis.",
                "organ_clearance_cutoffs": "Screen for steroid-induced osteoporosis and diabetes."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SAPHYR-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2212745",
                "cebm_level": 2,
                "sample_size": 118,
                "endpoints": "Sarilumab anti-IL-6 achieves 28% sustained steroid-free remission compared to 10% placebo in relapsing PMR (p=0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-492",
        "icd10": "M33.20",
        "condition": "Dermatomyositis (Gottron's Papules & Paraneoplastic Myopathy)",
        "specialty": "Rheumatology & Dermatology",
        "organ_system": "Integumentary & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ProDERM Landmark Trial & EULAR/ACR Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Aggarwal R et al. Trial of Intravenous Immune Globulin in Dermatomyositis (ProDERM). N Engl J Med. 2022;387(14):1264-1278.",
        "doi_or_source": "10.1056/NEJMoa2117912",
        "clinical_evidence": "Dermatomyositis is an immune-mediated necrotizing microangiopathy of skin and skeletal muscle. Pathognomonic cutaneous hallmarks: HELIOTROPE RASH (violaceous periorbital edema) and GOTTRON'S PAPULES (violaceous scaly plaques over dorsal MCP and PIP joints), accompanied by symmetric proximal muscle weakness (difficulty climbing stairs, combing hair) and elevated Creatine Kinase (CK). OVER 20-30% OF ADULT CASES ARE PARANEOPLASTIC (anti-TIF1-gamma and anti-NXP2 carry high malignancy risk). The landmark ProDERM trial (n=95) proved that IVIG (2 g/kg monthly) achieved 79% significant clinical response versus 44% placebo (p=0.006).",
        "solution_protocol": {
            "non_pharmacological_targets": "MANDATORY AGE- AND GENDER-APPROPRIATE CANCER SCREENING AT DIAGNOSIS AND ANNUALLY FOR 3 YEARS (CT chest/abdomen/pelvis, mammography, pelvic ultrasound/CA-125, colonoscopy, PSA); strict sun protection (UV light intensely triggers cutaneous flares); physical therapy.",
            "monitoring_cadence": "Manual Muscle Testing (MMT-8); serum Creatine Kinase (CK), Aldolase, and ALT/AST; myositis-specific autoantibody panel (anti-Mi-2, anti-TIF1-gamma, anti-NXP2, anti-MDA5); high-resolution chest CT for interstitial lung disease.",
            "clinical_thresholds": "Pathognomonic skin lesions (Gottron papules or heliotrope rash) with proximal muscle weakness, elevated CK, and muscle biopsy demonstrating perifascicular atrophy."
        },
        "patient_plain_language": "An autoimmune condition where your immune system attacks your small blood vessels, causing inflammation in your skin and muscles. It causes a distinctive purplish rash over your eyelids (heliotrope rash) and red, scaly bumps across your knuckles (Gottron's papules), along with weakness in your shoulders and thighs. Because it is frequently triggered by a hidden cancer, thorough full-body cancer screening is mandatory.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my myositis autoantibody blood panel check for Anti-TIF1-gamma or Anti-MDA5 markers?",
            "safety_question": "Have I undergone complete age-appropriate cancer screening (CT scans, colonoscopy, mammogram/pelvic exam)?",
            "action_threshold_question": "Am I a candidate for monthly IVIG antibody infusions (ProDERM protocol) to regain my muscle strength?"
        },
        "red_flags": [
            "Rapidly progressive shortness of breath with dry cough (Anti-MDA5 Rapidly Progressive Interstitial Lung Disease)",
            "Difficulty swallowing food with coughing or choking (Pharyngeal Dysphagia and aspiration risk)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dermatomyositis is an autoimmune disease causing a purplish eye rash, knuckle bumps, and muscle weakness, often tied to cancer.",
                "plain_analogy": "A power grid failure where both streetlights (skin) and factory pumps (muscles) lose voltage simultaneously.",
                "lifestyle_action": "Protect your skin from all sunlight with high-SPF sunscreen, attend cancer screening tests, and do physical therapy."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intravenous Immunoglobulin (IVIG 2 g/kg monthly - ProDERM Protocol)",
                    "Oral Prednisone (1 mg/kg/day)",
                    "Methotrexate / Azathioprine (Steroid-sparing)",
                    "Rituximab IV (for refractory disease)"
                ],
                "dosing_gdmt": "IVIG 2 g/kg divided over 2-5 days every 4 weeks; Prednisone 1 mg/kg/day tapered over 6-12 months.",
                "black_box_warning": "Sunlight exposure directly triggers and worsens dermatomyositis skin flares; strict UV avoidance required.",
                "organ_clearance_cutoffs": "Myositis-specific antibodies guide organ screening (e.g., anti-MDA5 carries high risk of fatal lung fibrosis)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ProDERM-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2117912",
                "cebm_level": 2,
                "sample_size": 95,
                "endpoints": "IVIG achieves 79% significant clinical response and allows substantial steroid sparing in dermatomyositis (p=0.006)."
            }
        }
    },
    {
        "id": "DOC-CARD-493",
        "icd10": "L12.0",
        "condition": "Bullous Pemphigoid (BP180/BP230 Subepidermal Tense Blisters)",
        "specialty": "Dermatology & Geriatrics",
        "organ_system": "Integumentary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & European Guidelines on Bullous Pemphigoid",
        "source_body": "British Journal of Dermatology & Cochrane Reviews",
        "citation": "Kirtschig G et al. Interventions for Bullous Pemphigoid. Cochrane Database Syst Rev. 2010;(10):CD002292.",
        "doi_or_source": "10.1002/14651858.CD002292.pub3",
        "clinical_evidence": "Bullous pemphigoid is the most common autoimmune blistering disease, predominantly affecting elderly individuals (>70 years), frequently linked to neurological comorbidities (dementia, Parkinson's) or DPP-4 inhibitors (gliptins). Pathogenic autoantibodies target hemidesmosomal adhesion proteins BP180 and BP230 at the dermal-epidermal junction. Produces TENSE SUBEPIDERMAL BULLAE ON ERYTHEMATOUS BASES WITH NEGATIVE NIKOLSKY SIGN. HIGH-POTENCY TOPICAL CORTICOSTEROIDS (Clobetasol propionate cream 20-30 g/day) are EQUALLY EFFECTIVE TO ORAL STEROIDS WITH SIGNIFICANTLY LOWER 1-YEAR MORTALITY (Lancet landmark trial).",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinue potential drug culprits (DPP-4 inhibitors / gliptins, loop diuretics, PD-1/PD-L1 checkpoint inhibitors); gentle skin care (avoid friction and adhesive tape); sterile lancing of large tense blisters (leave blister roofs intact as biological dressings); daily clobetasol cream application.",
            "monitoring_cadence": "Blister count and Disease Activity Index (BPDAI) weekly; serum BP180 and BP230 ELISA antibody titers (correlate with disease activity); monitor for secondary bacterial cellulitis.",
            "clinical_thresholds": "Subepidermal blister split on H&E biopsy, with linear deposition of IgG and C3 along the basement membrane zone on direct immunofluorescence (DIF)."
        },
        "patient_plain_language": "An autoimmune blistering disease of older adults where antibodies attack the microscopic velcro anchors (hemidesmosomes) that hold the outer layer of skin to the bottom layer. Because the split is deep, it causes thick, taut, dome-shaped blisters ('tense bullae') that do not pop easily, often starting with intense itching. Rubbing high-strength steroid cream (Clobetasol) all over the skin heals the blisters just as well as steroid pills with far fewer side effects.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did a skin biopsy and direct immunofluorescence test confirm subepidermal blisters with linear IgG along the basement membrane?",
            "safety_question": "Am I taking any medications that trigger bullous pemphigoid, such as DPP-4 inhibitor diabetes pills (gliptins)?",
            "action_threshold_question": "Can we use whole-body topical Clobetasol steroid cream instead of oral steroid pills to protect my heart and bones?"
        },
        "red_flags": [
            "Blister fluid turning cloudy yellow or foul-smelling with spreading warmth and fever (Secondary Staph Infection)",
            "Extensive blisters covering >30% of the body surface causing massive fluid and electrolyte loss"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bullous pemphigoid is an autoimmune skin condition in older adults causing firm, dome-shaped blisters and itching.",
                "plain_analogy": "Heavy-duty double-sided tape holding a rug to the floor losing its adhesive, letting large bubbles form under the carpet.",
                "lifestyle_action": "Apply prescribed steroid creams to affected skin, leave blister tops intact, and stop DPP-4 diabetes medicines."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Clobetasol Propionate 0.05% cream (20-30 g/day - Gold Standard)",
                    "Oral Prednisone (0.5 mg/kg/day if topical unfeasible)",
                    "Dupilumab SubQ (Anti-IL-4R-alpha - Novel Biologic)",
                    "Doxycycline + Nicotinamide (mild alternative)"
                ],
                "dosing_gdmt": "Clobetasol 0.05% cream applied to whole body (excluding face) 20-30 g/day until blister cessation, then tapered over 4-6 months.",
                "black_box_warning": "Oral prednisone has equivalent efficacy but HIGHER 1-year mortality (29% vs 14%) compared to topical clobetasol in elderly patients.",
                "organ_clearance_cutoffs": "Monitor for local cutaneous skin atrophy and systemic absorption."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "LANCET-PEMPHIGOID",
                "pmid_or_doi": "10.1056/NEJMoa012920",
                "cebm_level": 2,
                "sample_size": 341,
                "endpoints": "High-potency topical clobetasol is superior to oral prednisone, cutting 1-year mortality from 29% to 14% (p=0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-494",
        "icd10": "L10.0",
        "condition": "Pemphigus Vulgaris (Desmoglein 3/1 Intraepidermal Flaccid Blisters)",
        "specialty": "Dermatology & Oral Medicine",
        "organ_system": "Integumentary & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Ritux 3 Landmark Trial & EADV Guidelines",
        "source_body": "Lancet",
        "citation": "Joly P et al. First-Line Rituximab Combined with Short-Term Prednisone Versus Prednisone Alone for Pemphigus (Ritux 3). Lancet. 2017;389(10083):2031-2040.",
        "doi_or_source": "10.1016/S0140-6736(17)30078-3",
        "clinical_evidence": "Pemphigus vulgaris is a potentially fatal intraepidermal blistering disorder caused by IgG autoantibodies targeting desmoglein 3 (mucosal-predominant) and desmoglein 1 (mucocutaneous). Produces ACANTHOLYSIS (loss of keratinocyte-to-keratinocyte cell adhesion), resulting in FLACCID BLISTERS THAT RUPTURE EASILY, extensive painful oral erosions, and POSITIVE NIKOLSKY SIGN (slight friction dislodges skin). The landmark Ritux 3 trial (n=90) proved that FIRST-LINE RITUXIMAB (1,000 mg Day 1 and 15) COMBINED WITH SHORT-TERM PREDNISONE achieved complete remission off therapy in 89% vs 34% prednisone alone (p<0.0001), establishing Rituximab as the global gold standard.",
        "solution_protocol": {
            "non_pharmacological_targets": "First-line B-cell depletion with Rituximab; soft non-acidic bland diet; topical lidocaine mouth rinses for severe oral agony; wound care with non-adherent silicone dressings; PJP prophylaxis with Bactrim during rituximab.",
            "monitoring_cadence": "Pemphigus Disease Area Index (PDAI); serum Anti-Desmoglein 1 and 3 ELISA titers (titers strictly parallel disease activity and guide maintenance); monitor oral mucosa for secondary candidiasis.",
            "clinical_thresholds": "Intraepidermal suprabasal acantholysis with 'row of tombstones' basal cells on histology; 'fishnet' / intercellular IgG on direct immunofluorescence."
        },
        "patient_plain_language": "A rare, serious autoimmune skin disease where your antibodies attack the glue (desmoglein) that binds skin cells together. Because the breakdown happens inside the top layer of skin, blisters are thin, floppy ('flaccid'), and burst almost immediately, leaving raw, painful weeping red sores that look like severe burns. It almost always begins with agonizing sores inside your mouth. Targeted Rituximab antibody infusions cure the disease in nearly 90% of patients.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did blood tests show high levels of Anti-Desmoglein 3 and 1 antibodies, and did a biopsy show a positive Nikolsky sign?",
            "safety_question": "Am I receiving first-line Rituximab infusions (the Ritux 3 protocol) to induce complete remission and avoid years of high-dose steroids?",
            "action_threshold_question": "What soothing mouth rinses and wound care dressings will protect my raw mouth ulcers and skin sores from infection?"
        },
        "red_flags": [
            "Extensive denudation of skin (>30% body surface area) resembling full-thickness thermal burns with septic shock",
            "Severe oral erosions preventing any liquid intake, causing acute dehydration and electrolyte collapse"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Pemphigus vulgaris is a serious autoimmune condition where skin cells unglue, causing fragile blisters and raw mouth sores.",
                "plain_analogy": "Mortar between bricks crumbling into powder, causing the bricks on a wall to slip off and leave gaping holes.",
                "lifestyle_action": "Attend Rituximab infusions, use soft non-adherent silicone bandages, eat soft bland foods, and protect raw skin."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rituximab IV (1,000 mg Day 1 & 15 - First Line Class I)",
                    "Prednisone oral (1 mg/kg/day tapered rapidly over 3-6 months)",
                    "Mycophenolate Mofetil / Azathioprine (Adjuvant)",
                    "Bactrim (PJP Prophylaxis)"
                ],
                "dosing_gdmt": "Rituximab 1,000 mg IV on Day 1 and Day 15; plus Prednisone 1 mg/kg/day tapered to zero by month 6.",
                "black_box_warning": "Historically fatal (>70% mortality prior to corticosteroids) due to loss of skin barrier and secondary bacterial sepsis.",
                "organ_clearance_cutoffs": "Pre-medicate rituximab; screen for hepatitis B and tuberculosis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Ritux-3-TRIAL",
                "pmid_or_doi": "10.1016/S0140-6736(17)30078-3",
                "cebm_level": 2,
                "sample_size": 90,
                "endpoints": "First-line Rituximab plus short-term prednisone achieves 89% complete remission off therapy versus 34% prednisone alone (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-495",
        "icd10": "C90.00",
        "condition": "Multiple Myeloma (CRAB Criteria & Quadruplet Induction GDMT)",
        "specialty": "Hematology & Medical Oncology",
        "organ_system": "Hemic & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: GRIFFIN Landmark Trial & NCCN Multiple Myeloma Guidelines",
        "source_body": "Blood & Lancet",
        "citation": "Voorhees PM et al. Daratumumab, Bortezomib, Lenalidomide, and Dexamethasone for Transplant-Eligible Multiple Myeloma (GRIFFIN). Blood. 2020;136(8):936-945.",
        "doi_or_source": "10.1182/blood.2020005288",
        "clinical_evidence": "Multiple myeloma is a clonal plasma cell malignancy producing monoclonal immunoglobulin and end-organ damage (the CRAB CRITERIA: Hypercalcemia, Renal insufficiency, Anemia, Bone lytic lesions; or SLiM biomarkers: >=60% marrow plasma cells, serum free light chain ratio >=100, >1 focal MRI lesion). The phase 2/3 GRIFFIN trial (n=207) established that QUADRUPLET INDUCTION (Daratumumab + Bortezomib + Lenalidomide + Dexamethasone / D-VRd) achieved significantly higher Stringent Complete Response (62.6% vs 45.4%; p=0.018) and MRD-negativity rates.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bone protection with intravenous zoledronic acid or subcutaneous denosumab (reduces skeletal-related events and pathologic fractures by >40%); adequate hydration (>=2-3 L/day); avoid NSAIDs (nephrotoxic light chain cast synergy); mandatory venous thromboembolism prophylaxis (aspirin or apixaban on lenalidomide).",
            "monitoring_cadence": "Serum Protein Electrophoresis (SPEP) with immunofixation and quantitative M-spike; Serum Free Light Chains (kappa/lambda ratio); monthly CBC, creatinine, and calcium; annual whole-body low-dose CT for osteolytic bone lesions.",
            "clinical_thresholds": "Bone marrow biopsy showing >=10% clonal plasma cells (or biopsy-proven plasmacytoma) PLUS at least one CRAB or SLiM feature."
        },
        "patient_plain_language": "A blood cancer where abnormal plasma cells (which normally make infection-fighting antibodies) multiply uncontrollably in your bone marrow. They dissolve holes in your bones ('punched-out lesions'), spill toxic light chain proteins that clog your kidneys, cause anemia, and spike blood calcium. Breakthrough 4-drug combination therapy (including targeted antibody Daratumumab) knocks the cancer into deep remission, followed by a stem cell transplant.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my bone marrow plasma cell percentage and what is my serum free light chain kappa/lambda ratio?",
            "safety_question": "Am I receiving modern 4-drug combination therapy (Dara-VRd) including Daratumumab antibody infusions?",
            "action_threshold_question": "Am I receiving bone-strengthening medicine (Zometa or Xgeva) and blood thinner protection while on Revlimid?"
        },
        "red_flags": [
            "Sudden severe back pain after minor movement indicating a spinal vertebral compression fracture",
            "Confusion, extreme thirst, and constipation caused by severe Hypercalcemia (>12.0 mg/dL)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Multiple myeloma is a bone marrow cancer of plasma cells causing bone holes, kidney strain, and anemia.",
                "plain_analogy": "Termites eating away the wooden structural beams inside the walls of a house from the inside out.",
                "lifestyle_action": "Drink 2 to 3 liters of water daily, avoid all ibuprofen/naproxen painkillers, and take your myeloma medications on schedule."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Daratumumab SubQ (Darzalex Faspro - Anti-CD38)",
                    "Bortezomib SubQ (Velcade - Proteasome Inhibitor)",
                    "Lenalidomide oral (Revlimid - Immunomodulatory)",
                    "Dexamethasone oral",
                    "Zoledronic Acid IV (Bone Protection)"
                ],
                "dosing_gdmt": "D-VRd regimen: Daratumumab 1,800 mg SC weekly; Bortezomib 1.3 mg/m2 SC; Lenalidomide 25 mg daily (days 1-14); Dexamethasone 40 mg weekly.",
                "black_box_warning": "Lenalidomide is a thalidomide analogue with severe teratogenicity (Revlimid REMS program) and high DVT risk (anticoagulation mandatory).",
                "organ_clearance_cutoffs": "Dose adjust lenalidomide based on creatinine clearance (eGFR <50 mL/min)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "GRIFFIN-TRIAL",
                "pmid_or_doi": "10.1182/blood.2020005288",
                "cebm_level": 2,
                "sample_size": 207,
                "endpoints": "Quadruplet Dara-VRd induction achieves 63% stringent complete response and deep MRD-negativity in multiple myeloma (p=0.018)."
            }
        }
    },
    {
        "id": "DOC-CARD-496",
        "icd10": "D47.2",
        "condition": "Monoclonal Gammopathy of Undetermined Significance (MGUS - Premalignant)",
        "specialty": "Hematology",
        "organ_system": "Hemic & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IMWG Consensus on Risk Stratification in MGUS",
        "source_body": "Lancet Oncology & Blood",
        "citation": "Kyle RA et al. A Long-Term Study of Prognosis in Monoclonal Gammopathy of Undetermined Significance. N Engl J Med. 2018;378(3):241-249.",
        "doi_or_source": "10.1056/NEJMoa1709974",
        "clinical_evidence": "MGUS is an asymptomatic premalignant plasma cell precursor condition present in >3-5% of adults over 50. Defined by: 1) Serum monoclonal protein (M-protein) <30 g/L (<3.0 g/dL); 2) Clonal bone marrow plasma cells <10%; 3) ABSOLUTE ABSENCE OF END-ORGAN DAMAGE (NO CRAB FEATURES: normal calcium, normal renal function, normal hemoglobin, and absence of lytic bone lesions on skeletal imaging). Progresses to multiple myeloma or related disorders at a constant rate of 1% per year. MANAGEMENT IS STRICT OBSERVATION (WATCH-AND-WAIT); CHEMOTHERAPY OR IMMUNOTHERAPY IS STRICTLY HARMFUL.",
        "solution_protocol": {
            "non_pharmacological_targets": "NO ACTIVE CHEMOTHERAPY OR IMMUNOSUPPRESSION; reassuring patient of low annual progression risk (1% per year); healthy lifestyle; prompt evaluation if bone pain, fatigue, or unexplained weight loss develops.",
            "monitoring_cadence": "Mayo Clinic Risk Stratification (3 risk factors: non-IgG isotype, M-spike >=1.5 g/dL, abnormal free light chain ratio): Low risk (0 factors) requires repeat labs at 6 months, then every 2-3 years; Intermediate/High risk requires annual monitoring of SPEP, CBC, creatinine, and calcium.",
            "clinical_thresholds": "Serum M-protein <3.0 g/dL with bone marrow plasma cells <10% and complete absence of CRAB symptoms or amyloidosis."
        },
        "patient_plain_language": "A common, silent blood finding where a small cluster of plasma cells produces a small amount of extra antibody protein (M-spike) in your blood. It is NOT active cancer and causes ZERO symptoms, zero bone damage, and zero kidney damage. Over 99% of people live completely normal lifespans with no issues. The risk of it ever turning into active myeloma is only about 1% per year, so no treatment or chemo is needed—just a simple yearly blood check.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact M-protein size (is it safely below 3.0 g/dL) and what is my Mayo Clinic risk score?",
            "safety_question": "Do all my blood tests confirm normal calcium, normal kidney function, and no anemia?",
            "action_threshold_question": "Why is watch-and-wait observation with yearly blood checks the safest approach rather than taking chemotherapy?"
        },
        "red_flags": [
            "New-onset deep bone pain (especially in the back or ribs) that worsens with movement",
            "Unexplained fatigue, numbness in toes, or sudden foamy urine (screening for progression or AL amyloidosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "MGUS is a benign precursor protein in the blood that requires routine monitoring but no treatment.",
                "plain_analogy": "A small, harmless mole on your skin that is not cancer, but that you have checked by a doctor once a year.",
                "lifestyle_action": "Live your life normally, stay active, avoid unneeded cancer worry, and attend your yearly blood checkup."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Active Surveillance / Watch-and-Wait (Class I Standard of Care)",
                    "Calcium + Vitamin D3 (for bone health)",
                    "Avoidance of Antineoplastic Therapy"
                ],
                "dosing_gdmt": "Annual monitoring of SPEP, serum free light chains, CBC, and creatinine; NO chemotherapy.",
                "black_box_warning": "DO NOT treat MGUS with chemotherapy, proteasome inhibitors, or steroids (pure toxicity with zero survival benefit).",
                "organ_clearance_cutoffs": "Bone density monitoring with DXA scan (MGUS carries slightly increased risk of osteoporosis)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "KYLE-50YR-MGUS",
                "pmid_or_doi": "10.1056/NEJMoa1709974",
                "cebm_level": 1,
                "sample_size": 1384,
                "endpoints": "MGUS progresses to myeloma at a constant rate of 1% per year; 50-year follow-up confirms observation is standard."
            }
        }
    },
    {
        "id": "DOC-CARD-497",
        "icd10": "C91.10",
        "condition": "Chronic Lymphocytic Leukemia (CLL - Del(17p)/TP53 & BTK Inhibitors)",
        "specialty": "Hematology & Medical Oncology",
        "organ_system": "Hemic & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ALPINE Landmark Trial & NCCN Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Brown JR et al. Zanubrutinib or Ibrutinib in Relapsed or Refractory Chronic Lymphocytic Leukemia (ALPINE). N Engl J Med. 2023;388(4):319-332.",
        "doi_or_source": "10.1056/NEJMoa2211582",
        "clinical_evidence": "CLL is a clonal proliferation of mature CD5+/CD19+/CD23+ B-cells. Asymptomatic early stage (Rai 0 / Binet A) requires observation ('watch and wait'). For symptomatic or high-risk disease (del(17p) or TP53 mutation, which confers chemo-refractory biology), TARGETED CHEMO-FREE GDMT IS MANDATORY. The head-to-head phase 3 ALPINE trial (n=652) proved that second-generation BTK inhibitor ZANUBRUTINIB achieved superior Progression-Free Survival (hazard ratio 0.65; p=0.002) and significantly lower atrial fibrillation rates (5.2% vs 13.3%) compared to first-generation Ibrutinib. Fixed-duration Venetoclax + Obinutuzumab is alternative frontline.",
        "solution_protocol": {
            "non_pharmacological_targets": "Watchful waiting for asymptomatic Rai Stage 0 disease; non-live vaccinations (influenza, pneumococcal, recombinant zoster Shingrix); aggressive sun protection (CLL multiplies non-melanoma skin cancer risk 8-fold); prompt treatment of bacterial infections.",
            "monitoring_cadence": "CBC with differential tracking lymphocyte doubling time (<6 months indicates active disease); fluorescence in situ hybridization (FISH for del(17p), del(11q), trisomy 12) and IGHV mutation status prior to therapy; cardiac monitoring on BTK inhibitors.",
            "clinical_thresholds": "Monoclonal B-cell lymphocytosis >=5,000/mcL (>=5.0 x 10^9/L) in peripheral blood with characteristic CD5, CD19, CD20 (dim), and CD23 co-expression on flow cytometry."
        },
        "patient_plain_language": "The most common leukemia in adults. Your bone marrow produces too many mature-looking white blood cells (lymphocytes). In its early stages, it causes no symptoms and patients live for decades without ever needing treatment ('watch and wait'). When treatment is eventually needed, modern medicine uses gentle, targeted chemo-free pills like Zanubrutinib that block a specific cancer enzyme (BTK) with far fewer side effects.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I carry the high-risk genetic marker (del 17p or TP53 mutation) or is my IGHV gene mutated?",
            "safety_question": "If I do not have symptoms or anemia, why is watching and waiting safer than starting treatment early?",
            "action_threshold_question": "Why is second-generation BTK inhibitor Zanubrutinib (Brukinsa) safer for my heart than older leukemia drugs?"
        },
        "red_flags": [
            "Rapidly enlarging lymph nodes in the neck or armpits accompanied by drenching night sweats and fever (Richter's Transformation)",
            "Severe fatigue and shortness of breath indicating rapid autoimmune hemolytic anemia (AIHA)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "CLL is a slow-growing blood cancer of mature white blood cells, often managed with observation or targeted pills.",
                "plain_analogy": "A city park where old pigeons refuse to fly away and slowly crowd the pathways, but cause no immediate danger.",
                "lifestyle_action": "Stay up to date on non-live vaccines, protect your skin from sun damage, and attend regular blood count checks."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Zanubrutinib oral (Brukinsa - Next-Gen BTK Inhibitor)",
                    "Acalabrutinib oral (Calquence)",
                    "Venetoclax oral (Venclexta - BCL-2 Inhibitor)",
                    "Obinutuzumab IV (Gazyva - Anti-CD20)"
                ],
                "dosing_gdmt": "Zanubrutinib 160 mg orally BID (or 320 mg once daily); Venetoclax 5-week ramp-up from 20 to 400 mg daily.",
                "black_box_warning": "BTK inhibitors increase bleeding risks (hold prior to major surgery) and risk of atrial fibrillation/hypertension.",
                "organ_clearance_cutoffs": "Venetoclax carries black box warning for fatal Tumor Lysis Syndrome; mandatory 5-week ramp-up with hydration/allopurinol."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ALPINE-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2211582",
                "cebm_level": 2,
                "sample_size": 652,
                "endpoints": "Zanubrutinib achieves superior progression-free survival over ibrutinib with 60% lower atrial fibrillation risk (p=0.002)."
            }
        }
    },
    {
        "id": "DOC-CARD-498",
        "icd10": "C92.00",
        "condition": "Acute Myeloid Leukemia (AML - Auer Rods & Targeted 7+3 Induction)",
        "specialty": "Hematology & Medical Oncology",
        "organ_system": "Hemic & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: VIALE-A Landmark Trial & ELN AML Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "DiNardo CD et al. Azacitidine and Venetoclax in Previously Untreated Acute Myeloid Leukemia (VIALE-A). N Engl J Med. 2020;383(7):617-627.",
        "doi_or_source": "10.1056/NEJMoa2012971",
        "clinical_evidence": "AML is an aggressive hematologic emergency characterized by clonal expansion of poorly differentiated myeloid precursors (blasts >=20% in bone marrow/blood) with presence of AUER RODS on microscopy. In fit younger patients, intensive '7+3' induction (Cytarabine 7 days + Daunorubicin 3 days) combined with targeted agents (Midostaurin for FLT3-mutated; Gemtuzumab ozogamicin for CD33+) is standard. In unfit or older patients (>=75 years), the landmark VIALE-A trial (n=431) revolutionized therapy: AZACITIDINE + BCL-2 INHIBITOR VENETOCLAX significantly prolonged overall survival (14.7 vs 9.6 months; hazard ratio 0.66; p<0.001) and doubled complete remission rates (66.4% vs 28.3%).",
        "solution_protocol": {
            "non_pharmacological_targets": "EMERGENT HOSPITAL ADMISSION; infection prophylaxis during prolonged neutropenia (Posaconazole antifungal, Levofloxacin, Acyclovir); allopurinol/rasburicase and brisk IV hydration to prevent Tumor Lysis Syndrome; blood product transfusion support (platelets >10,000/mcL).",
            "monitoring_cadence": "Bone marrow biopsy at Day 14 and Day 28 post-induction to evaluate blast clearance (<5% blasts defines morphologic remission); daily CBC, coagulation, and comprehensive metabolic panel; molecular NGS testing (FLT3, NPM1, CEBPA, IDH1, IDH2, TP53).",
            "clinical_thresholds": ">=20% myeloblasts in bone marrow or peripheral blood, or presence of AML-defining cytogenetics [t(8;21), inv(16), t(15;17)] regardless of blast count."
        },
        "patient_plain_language": "An aggressive, fast-moving cancer of the blood where your bone marrow fills with immature, non-working white blood cells called myeloblasts. Because blasts crowd out normal cells, you rapidly become severely anemic, vulnerable to life-threatening infections, and bleed easily. For patients who cannot handle intense hospital chemotherapy, modern combination therapy using Azacitidine with a targeted pill called Venetoclax produces dramatic remissions.",
        "doctor_consultation_checklist": {
            "parameter_question": "What specific genetic mutations (such as FLT3, IDH1, IDH2, or NPM1) were detected in my bone marrow?",
            "safety_question": "Am I a candidate for standard intensive 7+3 chemotherapy or the gentler targeted Azacitidine + Venetoclax regimen?",
            "action_threshold_question": "Are preventive antifungal (Posaconazole) and antibiotic medicines protecting me while my white blood cells are low?"
        },
        "red_flags": [
            "Sudden high fever (>38.3 C) during low white blood cell count (Febrile Neutropenia - Emergency IV Antibiotics within 60 min)",
            "Spontaneous bleeding from gums, nose, or urine indicating severe thrombocytopenia or DIC"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "AML is a rapidly progressing leukemia where immature blast cells crowd the bone marrow, requiring urgent treatment.",
                "plain_analogy": "Weeds rapidly overrunning a vegetable garden within days, choking out all the tomatoes and carrots.",
                "lifestyle_action": "Seek immediate emergency hospital oncology care for high fever or unexplained bleeding, and stay in protected isolation."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Azacitidine SubQ/IV + Venetoclax oral (VIALE-A Frontline Standard)",
                    "Cytarabine 7-day + Daunorubicin 3-day ('7+3' Intensive)",
                    "Midostaurin oral (Rydapt - for FLT3-mutated AML)",
                    "Ivosidenib / Enasidenib (for IDH1/IDH2 mutants)"
                ],
                "dosing_gdmt": "Venetoclax 400 mg daily (with ramp-up) + Azacitidine 75 mg/m2 daily x 7 days every 28 days; or 7+3 induction.",
                "black_box_warning": "Extreme neutropenia and fatal infectious complications occur during induction; posaconazole prophylaxis is mandatory.",
                "organ_clearance_cutoffs": "Venetoclax dose must be reduced by 75% when co-administered with strong CYP3A4 inhibitors (posaconazole)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "VIALE-A-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2012971",
                "cebm_level": 2,
                "sample_size": 431,
                "endpoints": "Azacitidine plus Venetoclax extends overall survival by 50% and achieves 66% remission in AML (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-499",
        "icd10": "C81.90",
        "condition": "Classical Hodgkin Lymphoma (Reed-Sternberg Cells & Nivolumab-AVD)",
        "specialty": "Hematology & Medical Oncology",
        "organ_system": "Hemic & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: SWOG S1826 Landmark Trial & NCCN Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Castellino SM et al. Nivolumab-AVD or Brentuximab-AVD in Advanced-Stage Classic Hodgkin's Lymphoma (SWOG S1826). N Engl J Med. 2024;391(15):1379-1389.",
        "doi_or_source": "10.1056/NEJMoa2405888",
        "clinical_evidence": "Classical Hodgkin Lymphoma (cHL) is characterized by giant multinucleated REED-STERNBERG CELLS (CD30+, CD15+) surrounded by an extensive reactive inflammatory background, frequently presenting in adolescents and young adults with painless rubbery cervical lymphadenopathy and B-symptoms (fever, drenching night sweats, weight loss). The definitive landmark SWOG S1826 phase 3 trial (n=970) proved that PD-1 INHIBITOR NIVOLUMAB COMBINED WITH AVD CHEMOTHERAPY achieved 94% 2-year progression-free survival (hazard ratio 0.48; p<0.001) versus Brentuximab-AVD, with significantly lower neuropathy, establishing N-AVD as the new global frontline standard.",
        "solution_protocol": {
            "non_pharmacological_targets": "Prompt initiation of curative-intent chemoimmunotherapy; fertility preservation counseling and sperm/oocyte banking prior to treatment; interim PET/CT (Deauville criteria) to guide response-adapted therapy; cardiac and pulmonary function monitoring.",
            "monitoring_cadence": "18F-FDG PET/CT at baseline, after cycle 2 (interim PET: Deauville score 1-3 indicates complete metabolic response), and at end-of-treatment; serial CBC and liver/thyroid panels on nivolumab.",
            "clinical_thresholds": "Excisional lymph node biopsy demonstrating CD30+ CD15+ Reed-Sternberg cells on immunohistochemistry."
        },
        "patient_plain_language": "A highly curable cancer of the lymphatic system that most often affects teenagers and young adults. It begins as a painless, rubbery lump in your neck or collarbone, sometimes with drenching night sweats and fevers. Under a microscope, pathognomonic giant cancer cells look like owl eyes (Reed-Sternberg cells). Modern treatment combining immunotherapy (Nivolumab) with chemotherapy cures over 94% of patients while protecting nerves and fertility.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did an excisional whole-lymph-node biopsy confirm Classical Hodgkin Lymphoma with CD30+ Reed-Sternberg cells?",
            "safety_question": "Am I receiving the modern Nivolumab-AVD (N-AVD) regimen proven to cure over 94% of patients?",
            "action_threshold_question": "Have we discussed fertility preservation (freezing eggs or sperm) before my first infusion?"
        },
        "red_flags": [
            "Sudden severe fever and chills during low white blood cell counts (Neutropenic Sepsis Emergency)",
            "Severe shortness of breath or cough indicating treatment-related pneumonitis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hodgkin lymphoma is a highly curable lymph node cancer marked by Reed-Sternberg cells, cured with chemoimmunotherapy.",
                "plain_analogy": "A single invasive weed in a garden lawn that is uniquely sensitive to modern organic herbicide sprays.",
                "lifestyle_action": "Attend all chemoimmunotherapy cycles on time, report fevers immediately, and attend follow-up PET scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Nivolumab IV (Opdivo - PD-1 Inhibitor)",
                    "Doxorubicin (Adriamycin) + Vinblastine + Dacarbazine (AVD)",
                    "Brentuximab Vedotin (Adcetris - CD30 Antibody-Drug Conjugate)",
                    "Radiation Therapy (Consolidative)"
                ],
                "dosing_gdmt": "Nivolumab 240 mg IV + Doxorubicin 25 mg/m2 + Vinblastine 6 mg/m2 + Dacarbazine 375 mg/m2 on Days 1 & 15 q28d x 6 cycles.",
                "black_box_warning": "Bleomycin is PERMANENTLY EXCLUDED in modern N-AVD to eliminate fatal pulmonary fibrosis and lung toxicity.",
                "organ_clearance_cutoffs": "Monitor for immune-related adverse events on Nivolumab (hypophysitis, thyroiditis, colitis)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SWOG-S1826",
                "pmid_or_doi": "10.1056/NEJMoa2405888",
                "cebm_level": 2,
                "sample_size": 970,
                "endpoints": "Nivolumab-AVD achieves 94% 2-year progression-free survival in advanced Hodgkin lymphoma (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-500",
        "icd10": "C83.30",
        "condition": "Diffuse Large B-Cell Lymphoma (DLBCL - Pola-R-CHP & CAR-T Therapy)",
        "specialty": "Hematology & Medical Oncology",
        "organ_system": "Hemic & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: POLARIX & ZUMA-7 Landmark Phase 3 Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "Tilly H et al. Polatuzumab Vedotin in Previously Untreated Diffuse Large B-Cell Lymphoma (POLARIX). N Engl J Med. 2022;386(4):351-363.",
        "doi_or_source": "10.1056/NEJMoa2115304",
        "clinical_evidence": "DLBCL is the most common aggressive Non-Hodgkin Lymphoma, characterized by diffuse sheets of large atypical CD20+ B-cells with high proliferative index (Ki-67 >70-80%). The landmark phase 3 POLARIX trial (n=879) proved that replacing vincristine with antibody-drug conjugate Polatuzumab Vedotin (Pola-R-CHP: Polatuzumab + Rituximab + Cyclophosphamide + Doxorubicin + Prednisone) achieved a 27% reduction in risk of progression, relapse, or death compared to standard R-CHOP (p=0.02). In primary refractory or early relapsed DLBCL (<=12 months), CD19 CAR T-CELL THERAPY (Axicabtagene ciloleucel; ZUMA-7 trial) quadrupled 2-year event-free survival (40.5% vs 16.3%; p<0.001) over autologous stem cell transplant.",
        "solution_protocol": {
            "non_pharmacological_targets": "Prompt initiation of curative-intent chemoimmunotherapy; CNS prophylaxis (intrathecal methotrexate) for high CNS-IPI score; allopurinol/rasburicase for Tumor Lysis Syndrome; G-CSF (Pegfilgrastim) primary prophylaxis for febrile neutropenia.",
            "monitoring_cadence": "Baseline 18F-FDG PET/CT and end-of-treatment PET/CT (Lugano 2014 criteria); International Prognostic Index (IPI score); cell of origin classification (Hans algorithm: GCB vs ABC/non-GCB); FISH for MYC, BCL2, BCL6 ('double-hit' lymphoma).",
            "clinical_thresholds": "Diffuse effacement of lymph node architecture by large B-cells expressing CD20 with Ki-67 >60-90% on excisional biopsy."
        },
        "patient_plain_language": "The most common aggressive lymphoma in adults. Cancerous B-cells multiply rapidly in your lymph nodes, forming rapidly enlarging masses in your neck, armpits, abdomen, or groin. Although fast-growing, it is highly curable with intensive treatment. Modern frontline therapy uses an antibody-drug smart bomb (Polatuzumab) combined with chemo (Pola-R-CHP). If the lymphoma ever returns, miraculous living cell therapy (CAR-T cells), where your own immune cells are genetically re-engineered to hunt down and kill cancer cells, cures over 40% of relapsed patients.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did biopsy confirm Diffuse Large B-Cell Lymphoma, and was 'double-hit' (MYC/BCL2) genetic rearrangement ruled out?",
            "safety_question": "Am I receiving the modern Pola-R-CHP regimen (with Polatuzumab Vedotin) shown to improve cure rates over old R-CHOP?",
            "action_threshold_question": "If my lymphoma does not fully disappear, am I a candidate for personalized CAR-T cell immunotherapy?"
        },
        "red_flags": [
            "Rapidly enlarging mass doubling in size over days with high fevers and night sweats",
            "Facial swelling, neck fullness, and dilated chest veins (Superior Vena Cava Syndrome Emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "DLBCL is an aggressive but curable cancer of white blood cells, treated with smart-bomb antibody chemo or CAR-T cells.",
                "plain_analogy": "A rapid wildfire blazing through dry brush that can be completely extinguished if doused immediately with heavy fire retardant.",
                "lifestyle_action": "Attend all chemo cycles on schedule, protect yourself from infections, and attend end-of-treatment PET scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Polatuzumab Vedotin + R-CHP (POLARIX Gold Standard Frontline)",
                    "Axicabtagene Ciloleucel (Yescarta - CD19 CAR-T for Relapse)",
                    "R-CHOP Chemoimmunotherapy",
                    "Pegfilgrastim (G-CSF Growth Factor Support)"
                ],
                "dosing_gdmt": "Pola-R-CHP: Polatuzumab 1.8 mg/kg IV + Rituximab 375 mg/m2 + Cyclophosphamide 750 mg/m2 + Doxorubicin 50 mg/m2 (Day 1) + Prednisone 100 mg (Days 1-5) q21d x 6 cycles.",
                "black_box_warning": "CAR T-cell therapy carries severe risks of Cytokine Release Syndrome (CRS) and neurotoxicity (ICANS); requires Tocilizumab readiness.",
                "organ_clearance_cutoffs": "Dose reduction of cyclophosphamide/doxorubicin in severe hepatic or renal dysfunction."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POLARIX-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2115304",
                "cebm_level": 2,
                "sample_size": 879,
                "endpoints": "Pola-R-CHP significantly reduces progression, relapse, or death by 27% compared to standard R-CHOP in DLBCL (p=0.02)."
            }
        }
    }
]
