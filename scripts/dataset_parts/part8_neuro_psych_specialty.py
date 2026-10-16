"""
part8_neuro_psych_specialty.py
"""

PART_8_DISEASES = [
    {
        "id": "DOC-CARD-241",
        "icd10": "G12.21",
        "condition": "Amyotrophic Lateral Sclerosis (ALS)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM & The Lancet Neurology (Edaravone & Riluzole)",
        "citation": "Writing Group; Edaravone (MCI-186) ALS 19 Study Group. Safety and efficacy of edaravone in well defined patients with amyotrophic lateral sclerosis. Lancet Neurol. 2017;16(7):505-512.",
        "doi_or_source": "10.1016/S1474-4422(17)30115-1",
        "clinical_evidence": "In the landmark double-blind Phase 3 MCI-186 trial (n=137 patients with early definite or probable ALS), intravenous edaravone (a free-radical scavenger, 60 mg daily in 28-day cycles) significantly slowed functional motor decline over 24 weeks compared with placebo, as measured by the Revised ALS Functional Rating Scale (ALSFRS-R mean difference 2.49 points; 95% CI 0.99-3.98; p=0.0013). Riluzole (50 mg BID) prolongs median survival or time to tracheostomy by 2-3 months (hazard ratio 0.65; p=0.002). Multidisciplinary specialized ALS clinic care and early non-invasive ventilation (NIV/BiPAP) when upright FVC <50% or sniff nasal pressure <40 cm H2O prolongs quality survival by >12 months.",
        "solution_protocol": {
            "non_pharmacological_targets": "Early speech-language pathology communication evaluation (eye-gaze communication devices); occupational therapy for adaptive eating utensils; nocturnal non-invasive positive pressure ventilation (BiPAP); timely percutaneous endoscopic gastrostomy (PEG) feeding tube placement prior to FVC dropping <50%.",
            "monitoring_cadence": "Quarterly ALSFRS-R scoring; upright and supine spirometry (FVC and maximum inspiratory pressure [MIP]); liver function tests (AST/ALT/bilirubin) monthly for the first 3 months on riluzole.",
            "clinical_thresholds": "Orthopnea, supine FVC drop >20%, or upright FVC <50% triggers immediate nocturnal BiPAP initiation; involuntary weight loss >10% with dysphagia triggers PEG tube placement."
        },
        "patient_plain_language": "Amyotrophic lateral sclerosis (ALS, often called Lou Gehrig's disease) is a progressive nervous system disease that affects motor nerve cells in your brain and spinal cord. These motor nerves control all your voluntary muscles. As the nerves gradually degenerate, the muscles they signal become weak, twitch (fasciculations), and shrink, making it difficult to walk, talk, swallow, and breathe.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current upright and lying-down forced vital capacity (FVC) percentage, and is it time to begin nocturnal BiPAP breathing support?",
            "safety_question": "Should I be taking both riluzole and edaravone to give myself the best protection against disease progression?",
            "action_threshold_question": "At what point in my swallowing difficulties should we schedule a feeding tube (PEG) placement before my breathing muscles become too weak for the procedure?"
        },
        "red_flags": [
            "Severe shortness of breath when lying flat, morning carbon dioxide headaches with confusion, choking on saliva, or inability to clear chest phlegm"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Amyotrophic lateral sclerosis is a progressive neurodegenerative disease that affects nerve cells in the brain and spinal cord that control muscle movement.",
                "plain_analogy": "The electrical wiring between the brain and muscles slowly fraying, leaving the muscles powerless and inactive.",
                "lifestyle_action": "Maintain high-calorie nutrition. Conserve energy with adaptive devices. Start nocturnal breathing support early."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Riluzole (Rilutek)", "Edaravone (Radicava IV / Oral)", "Tofersen (Qalsody for SOD1)", "Dextromethorphan/Quinidine (Nuedexta)"],
                "dosing_gdmt": "Riluzole 50 mg orally BID taken on an empty stomach PLUS Edaravone 105 mg oral suspension daily in 14-day cycles.",
                "black_box_warning": "Riluzole: Severe hepatotoxicity and neutropenia; monitor transaminases monthly for 3 months, then quarterly.",
                "organ_clearance_cutoffs": "Discontinue riluzole if ALT exceeds 5x ULN; Nuedexta contraindicated in heart block or prolonged QT interval."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MCI-186 Study",
                "pmid_or_doi": "10.1016/S1474-4422(17)30115-1",
                "cebm_level": 2,
                "sample_size": 137,
                "endpoints": "ALSFRS-R decline slowed by 33% with edaravone vs placebo (difference 2.49 points; p=0.0013); riluzole prolongs tracheostomy-free survival."
            }
        }
    },
    {
        "id": "DOC-CARD-242",
        "icd10": "G10",
        "condition": "Huntington's Disease",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "JAMA (First-HD Trial) & NEJM",
        "citation": "Huntington Study Group. Effect of Deutetrabenazine on Chorea Among Patients With Huntington Disease: A Randomized Clinical Trial (First-HD). JAMA. 2016;316(1):40-50.",
        "doi_or_source": "10.1001/jama.2016.8655",
        "clinical_evidence": "Huntington's disease is an autosomal dominant neurodegenerative disorder caused by an expanded CAG trinucleotide repeat (>36 repeats; fully penetrant at >=40 repeats) in the HTT gene on chromosome 4, resulting in toxic huntingtin protein aggregation and profound striatal (caudate and putamen) GABAergic medium spiny neuron loss. The clinical triad comprises motor chorea, cognitive decline, and psychiatric disturbances. In the multicenter double-blind Phase 3 First-HD trial (n=90 patients), deuterated tetrabenazine (deutetrabenazine, a vesicular monoamine transporter 2 [VMAT2] inhibitor) significantly improved the Total Maximal Chorea score from baseline to week 12 compared with placebo (mean difference -2.5 units; 95% CI -3.7 to -1.3; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Physical therapy for gait stability and fall prevention; speech-language swallowing evaluation and modified food textures; genetic counseling protocol (Huntington's Disease Society of America guidelines) prior to predictive testing.",
            "monitoring_cadence": "Unified Huntington's Disease Rating Scale (UHDRS) total motor and functional assessments every 6 months; formal depression and suicidality screening (Columbia-Suicide Severity Rating Scale) at every visit.",
            "clinical_thresholds": "UHDRS chorea score impairment interfering with activities of daily living or causing falls warrants VMAT2 inhibitor therapy (deutetrabenazine 6-48 mg/day or tetrabenazine 12.5-100 mg/day)."
        },
        "patient_plain_language": "Huntington's disease is a genetic brain disorder caused by an inherited error in a single gene. Over time, it damages nerve cells in the central movement-control centers of your brain. It causes involuntary dancing or jerking movements (chorea), changes in personality, irritability, and gradual memory and reasoning challenges. Each child of an affected parent has a 50% chance of inheriting the gene.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Unified Huntington's Disease Rating Scale (UHDRS) motor and chorea score?",
            "safety_question": "What mood, depression, or suicidal thinking symptoms must my family monitor for while taking VMAT2 chorea medications?",
            "action_threshold_question": "What genetic counseling and confidential testing resources are available for my adult children who want to know their carrier status?"
        },
        "red_flags": [
            "Sudden severe depressive mood swings, suicidal thoughts, severe choking spells when eating, or frequent traumatic falls"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Huntington disease is an inherited disorder that causes the progressive breakdown of nerve cells in the brain, causing involuntary movements and cognitive decline.",
                "plain_analogy": "A hereditary spelling error in the brain's genetic blueprint that causes movement-control centers to wear out prematurely.",
                "lifestyle_action": "Eat calorie-dense meals to combat high energy burn from involuntary movements. Remove home tripping hazards."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Deutetrabenazine (Austedo)", "Tetrabenazine (Xenazine)", "Valbenazine (Ingrezza)", "Olanzapine"],
                "dosing_gdmt": "Deutetrabenazine: Start 6 mg daily with food, titrating weekly by 6 mg/day to maximum 48 mg/day (administered BID).",
                "black_box_warning": "VMAT2 Inhibitors: Increased risk of depression and suicidal thoughts and behaviors in patients with Huntington's disease.",
                "organ_clearance_cutoffs": "Contraindicated in patients with active suicidal ideation or untreated depression, and with concurrent MAO inhibitors."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "First-HD",
                "pmid_or_doi": "10.1001/jama.2016.8655",
                "cebm_level": 2,
                "sample_size": 90,
                "endpoints": "Total Maximal Chorea score reduced by 4.4 points with deutetrabenazine vs 1.9 points placebo (p<0.001); patient global impression improved."
            }
        }
    },
    {
        "id": "DOC-CARD-243",
        "icd10": "G91.2",
        "condition": "Normal Pressure Hydrocephalus (NPH)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Multicenter Prospective Clinical Trial & Guideline",
        "source_body": "NEJM & Journal of Neurosurgery (INPH Guidelines)",
        "citation": "Klinge P et al. One-year outcomes of European multicentre study on normal pressure hydrocephalus (INPH). Acta Neurochir (Wien). 2012;154(7):1179-1189.",
        "doi_or_source": "10.1007/s00701-012-1376-7",
        "clinical_evidence": "Normal Pressure Hydrocephalus (NPH) is a reversible cause of dementia characterized by the classic clinical triad of gait disturbance ('magnetic' gait: slow, wide-based, shuffling, glued to the floor), cognitive decline (subcortical psychomotor slowing), and urinary incontinence ('wet, wacky, and wobbly'). MRI demonstrates ventriculomegaly disproportionate to sulcal atrophy (Evans index >0.30) with tight high-convexity sulci and enlarged Sylvian fissures (Disproportionately Enlarged Subarachnoid-space Hydrocephalus [DESH]). Diagnostic CSF tap test (removal of 30-50 mL CSF via lumbar puncture) producing an objective >=20% improvement in 10-meter timed walking speed has >90% positive predictive value for surgical shunt success. Ventriculoperitoneal (VP) shunting with a programmable valve achieves long-term clinical gait improvement in >80% of patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Physical therapy for balance and gait rehabilitation; home fall safety modifications; pelvic floor exercises and scheduled voiding regimens for urinary urgency.",
            "monitoring_cadence": "Formal 10-meter timed walking test and Timed Up and Go (TUG) at baseline and 2-4 hours post-lumbar puncture tap test; neurosurgical programmable valve check at 6 weeks and 6 months post-VP shunt.",
            "clinical_thresholds": "Evans index >0.30 with positive tap test (>=20% improvement in walking speed or >=3 steps fewer on 10m walk) indicates immediate candidacy for surgical ventriculoperitoneal (VP) shunt placement."
        },
        "patient_plain_language": "Normal pressure hydrocephalus (NPH) is a condition where normal fluid (cerebrospinal fluid) builds up inside the open fluid chambers (ventricles) of your brain. As the fluid chambers swell, they stretch the brain tissue that controls your walking, memory, and bladder control. The classic signs are a shuffling 'magnetic' walk (feet feeling glued to the floor), mild forgetfulness, and urgent bladder leaks. It is one of the few forms of dementia that can be reversed with a small drainage tube (shunt).",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my exact timed walking speed before and after the 40-milliliter spinal tap fluid removal test?",
            "safety_question": "Does my brain MRI show the classic DESH pattern (enlarged ventricles with crowded upper brain sulci)?",
            "action_threshold_question": "If I receive a ventriculoperitoneal (VP) shunt, what type of programmable magnetic valve will be used and how is it adjusted?"
        },
        "red_flags": [
            "Severe worsening headache when standing up (suspect subdural hematoma from shunt overdrainage), fever with neck stiffness (shunt infection), or sudden inability to walk"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Normal pressure hydrocephalus is an abnormal buildup of cerebrospinal fluid in the brain's ventricles, causing walking difficulties, memory loss, and bladder control problems.",
                "plain_analogy": "An overflowing fluid reservoir in the center of the brain pressing outward against the brain's walking and memory wiring.",
                "lifestyle_action": "Use a walker to prevent falls. Perform scheduled bathroom breaks every 2 hours. Keep track of walking improvements."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Acetazolamide (Temporary bridge)", "Programmable VP Shunt Systems (Strata/Codman)"],
                "dosing_gdmt": "Definitive: Surgical placement of a ventriculoperitoneal (VP) shunt with adjustable differential pressure valve.",
                "black_box_warning": "Surgical Shunts: Risk of subdural hematoma from overdrainage; adjust valve setting if postural headache occurs.",
                "organ_clearance_cutoffs": "Avoid strong external magnetic fields (e.g. non-MRI conditional wands) near programmable valve mechanism."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "INPH European Study",
                "pmid_or_doi": "10.1007/s00701-012-1376-7",
                "cebm_level": 1,
                "sample_size": 142,
                "endpoints": "VP shunting achieves sustained gait improvement in 84% and cognitive stabilization in 72% at 1 year; tap test positive predictive value >90%."
            }
        }
    },
    {
        "id": "DOC-CARD-244",
        "icd10": "G61.0",
        "condition": "Guillain-Barré Syndrome (GBS)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Lancet Meta-Analysis",
        "source_body": "Cochrane Database of Systematic Reviews & The Lancet Neurology",
        "citation": "Hughes RA et al. Intravenous immunoglobulin for Guillain-Barré syndrome. Cochrane Database Syst Rev. 2014;2014(9):CD002063.",
        "doi_or_source": "10.1002/14651858.CD002063.pub6",
        "clinical_evidence": "Guillain-Barré Syndrome (GBS) is an acute immune-mediated post-infectious polyradiculoneuropathy (most commonly following Campylobacter jejuni, CMV, EBV, or Zika virus infection) characterized by molecular mimicry attacking peripheral nerve myelin (AIDP) or axolemma (AMAN/AMSAN). Clinical hallmark is acute, rapidly progressive, symmetric ascending flaccid paralysis with areflexia. Lumbar puncture demonstrates classic 'albuminocytological dissociation' (elevated CSF protein >0.45 g/L with normal white blood cell count <10 cells/mcL). In a Cochrane systematic review of randomized trials (n=585 patients), intravenous immunoglobulin (IVIG 0.4 g/kg/day for 5 days) was equally effective as plasma exchange (PE 200-250 mL/kg over 5 sessions) in accelerating motor recovery and reducing mechanical ventilation (RR 1.05; 95% CI 0.73-1.53), with fewer adverse events. Corticosteroids alone are ineffective and harmful.",
        "solution_protocol": {
            "non_pharmacological_targets": "Admission to ICU or step-down unit with continuous telemetry (monitoring for life-threatening autonomic instability: labile blood pressure, cardiac arrhythmias); physical and occupational therapy for contracture prevention; venous thromboembolism (VTE) prophylaxis.",
            "monitoring_cadence": "Serial measurement of Forced Vital Capacity (FVC) and Negative Inspiratory Force (NIF) every 2-4 hours ('20/30/40 rule': FVC <20 mL/kg, NIF < -30 cm H2O, or maximum expiratory pressure <40 cm H2O indicates elective intubation); continuous cardiac telemetry.",
            "clinical_thresholds": "Rapidly progressive weakness within 2-4 weeks of onset with inability to walk unassisted (Erasmus GBS Respiratory Insufficiency Score [EGRIS] >3) warrants immediate initiation of IVIG (2 g/kg total dose over 5 days) or plasma exchange."
        },
        "patient_plain_language": "Guillain-Barré syndrome (GBS) is a rare neurological disorder where your body's immune system, usually triggered by a recent stomach bug or respiratory virus, gets confused and mistakenly attacks the protective coating of your peripheral nerves. It causes tingling and numbness that starts in your toes and feet and rapidly spreads upward into your legs, arms, and chest, causing temporary weakness or paralysis.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current forced vital capacity (FVC) and negative inspiratory force (NIF) breathing score?",
            "safety_question": "Are my heart rate and blood pressure being continuously monitored on telemetry for autonomic nerve instability?",
            "action_threshold_question": "Have we started my 5-day course of intravenous immunoglobulin (IVIG) or plasma exchange treatment?"
        },
        "red_flags": [
            "Rapidly ascending paralysis reaching the chest, inability to take a deep breath, difficulty swallowing saliva, choking, or extreme heart rate fluctuations"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Guillain-Barré syndrome is a rare condition in which your immune system attacks your peripheral nerves, leading to muscle weakness and paralysis.",
                "plain_analogy": "An overactive immune security system short-circuiting the electrical cables connecting the spinal cord to your leg and arm muscles.",
                "lifestyle_action": "Requires immediate hospital admission. Rest completely while immune treatments clear the antibodies."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Intravenous Immune Globulin (IVIG)", "Plasma Exchange (Plasmapheresis)", "Subcutaneous Heparin (VTE Prophylaxis)"],
                "dosing_gdmt": "IVIG 0.4 g/kg/day IV for 5 consecutive days (total 2 g/kg). Alternatively, Plasma Exchange 5 sessions over 7-14 days.",
                "black_box_warning": "IVIG: Acute renal failure, aseptic meningitis, thrombosis, and hemolysis; monitor renal function and hydrate adequately.",
                "organ_clearance_cutoffs": "Screen for IgA deficiency prior to IVIG (risk of anaphylaxis); systemic corticosteroids are ineffective and contraindicated alone."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Cochrane GBS Review",
                "pmid_or_doi": "10.1002/14651858.CD002063.pub6",
                "cebm_level": 1,
                "sample_size": 585,
                "endpoints": "IVIG equivalent to plasma exchange for accelerating walking recovery (median time to walk unassisted reduced by 32 days); overall recovery >85%."
            }
        }
    },
    {
        "id": "DOC-CARD-245",
        "icd10": "G70.00",
        "condition": "Myasthenia Gravis",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (MGTX Trial) & REGAIN Trial",
        "citation": "Wolfe GI et al. Randomized Trial of Thymectomy in Myasthenia Gravis (MGTX). N Engl J Med. 2016;375(6):511-522.",
        "doi_or_source": "10.1056/NEJMoa1602489",
        "clinical_evidence": "Myasthenia Gravis (MG) is an autoimmune disorder of neuromuscular junction transmission caused predominantly by pathogenic autoantibodies against the nicotinic acetylcholine receptor (AChR-Ab, present in 85%), muscle-specific kinase (MuSK-Ab, 5-8%), or LRP4. Hallmark is fatigable muscle weakness that worsens with repetitive activity and improves with rest. In the landmark international randomized trial of thymectomy (MGTX, n=126 patients with non-thymomatous generalized AChR-positive MG aged 18-65), extended transsternal thymectomy combined with prednisone significantly improved the Quantitative Myasthenia Gravis (QMG) score over 3 years (mean score 6.15 vs 8.99; p<0.001) and lowered average daily prednisone dose (44 mg vs 60 mg; p<0.001) compared with prednisone alone. In refractory generalized MG, complement C5 inhibition (eculizumab) or neonatal Fc receptor (FcRn) blockers (efgartigimod) produce rapid, robust clinical improvements.",
        "solution_protocol": {
            "non_pharmacological_targets": "Rest periods before meals to preserve chewing/swallowing strength; avoidance of medications that block neuromuscular transmission (fluoroquinolones, macrolides, aminoglycosides, beta-blockers, magnesium, and immune checkpoint inhibitors).",
            "monitoring_cadence": "Quantitative Myasthenia Gravis (QMG) and MG Activities of Daily Living (MG-ADL) score at each visit; single-fiber electromyography (SFEMG, sensitivity >95%) if seronegative; chest CT/MRI to screen for thymoma.",
            "clinical_thresholds": "Myasthenic crisis (acute respiratory failure from diaphragmatic weakness or severe bulbar failure) requires immediate ICU admission, non-invasive ventilation or intubation, and rapid rescue therapy with plasma exchange (5 sessions) or IVIG."
        },
        "patient_plain_language": "Myasthenia gravis is an autoimmune disorder where your immune system mistakenly blocks or destroys the receptors on your muscles that receive signals from your nerves. Without these communication receptors, your muscles get tired and weak very quickly when used. The most common signs are a droopy eyelid (ptosis), double vision, difficulty chewing solid food, slurred speech, and muscle fatigue that improves after a short nap.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Myasthenia Gravis Activities of Daily Living (MG-ADL) score and did my blood tests confirm acetylcholine receptor (AChR) antibodies?",
            "safety_question": "Does my chest CT scan show an enlarged thymus gland or a thymoma that should be surgically removed?",
            "action_threshold_question": "Which common antibiotics (like ciprofloxacin or azithromycin) are strictly forbidden for me because they can trigger a breathing crisis?"
        },
        "red_flags": [
            "Severe shortness of breath, inability to swallow liquids without choking, difficulty holding your head upright, or voice fading to a whisper (Myasthenic Crisis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Myasthenia gravis is a chronic autoimmune neuromuscular disease that causes weakness in the skeletal muscles that worsens after periods of activity.",
                "plain_analogy": "A radio receiver on the muscle that has had its antenna blocked by antibodies, so the muscle misses the nerve's commands.",
                "lifestyle_action": "Schedule important tasks and meals for the morning when strength is highest. Rest frequently. Keep emergency rescue card."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Pyridostigmine (Mestinon)", "Efgartigimod (Vyvgart)", "Eculizumab (Soliris)", "Prednisone", "Azathioprine"],
                "dosing_gdmt": "Pyridostigmine 60 mg orally every 4 hours while awake (titrated to maximum 120 mg q3-4h). Efgartigimod 10 mg/kg IV weekly for 4 weeks.",
                "black_box_warning": "Eculizumab: Life-threatening and fatal meningococcal infections; mandatory meningococcal vaccination (MenACWY and MenB) at least 2 weeks prior.",
                "organ_clearance_cutoffs": "Monitor for cholinergic crisis (excessive tearing, salivation, diarrhea, bradycardia) if high-dose pyridostigmine is used."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MGTX / ADAPT",
                "pmid_or_doi": "10.1056/NEJMoa1602489",
                "cebm_level": 2,
                "sample_size": 126,
                "endpoints": "Thymectomy significantly lowers 3-year QMG score (6.15 vs 8.99; p<0.001) and reduces steroid dependency; Efgartigimod achieves 68% response rate."
            }
        }
    },
    {
        "id": "DOC-CARD-246",
        "icd10": "G50.0",
        "condition": "Trigeminal Neuralgia",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAN/EAN Clinical Practice Guideline",
        "source_body": "American Academy of Neurology (AAN) & European Academy of Neurology (EAN)",
        "citation": "Bendtsen L et al. European Academy of Neurology guideline on trigeminal neuralgia. Eur J Neurol. 2019;26(6):831-845.",
        "doi_or_source": "10.1111/ene.13950",
        "clinical_evidence": "Trigeminal neuralgia (TN, tic douloureux) is characterized by paroxysmal, brief (lasting fractions of a second to 2 minutes), severe, unilateral, electric shock-like, shooting facial pains strictly distributed along one or more divisions of the trigeminal nerve (most commonly V2 maxillary and V3 mandibular). Pain is triggered by innocuous light cutaneous touch (brushing teeth, light breeze, chewing, talking). Classic TN is driven by neurovascular compression of the trigeminal nerve root entry zone by an aberrant arterial loop (most commonly the superior cerebellar artery [SCA]), identifiable on 3D high-resolution T2/constructive interference MRI (3D-CISS/FIESTA). First-line pharmacological therapy with sodium channel blockers (carbamazepine 200-1200 mg/day or oxcarbazepine 600-1800 mg/day) achieves initial pain control in >80% of patients. Microvascular decompression (MVD, Janetta procedure) achieves long-term pain freedom without sensory loss in >70-80% at 5 years.",
        "solution_protocol": {
            "non_pharmacological_targets": "Identification and gentle avoidance of trigger zones (washing face with warm water rather than cold; using a soft-bristled toothbrush; wearing a scarf to block cold wind exposure).",
            "monitoring_cadence": "Serum sodium, CBC, and liver function tests at baseline, 2, 4, and 12 weeks during carbamazepine/oxcarbazepine therapy; HLA-B*1502 genetic screening in patients of Asian ancestry prior to carbamazepine.",
            "clinical_thresholds": "Refractory pain despite therapeutic antiepileptic drug titration or drug intolerance warrants neurosurgical evaluation for microvascular decompression (MVD) or stereotactic Gamma Knife radiosurgery."
        },
        "patient_plain_language": "Trigeminal neuralgia is an intense facial nerve pain condition often described as one of the most painful conditions known. A pulsating blood vessel presses against the trigeminal nerve, the main sensation cable connecting your face to your brain. This wears away the nerve's protective insulation, so even the lightest brush—like a gentle gust of wind, chewing food, or brushing your teeth—triggers blinding, lightning-bolt pain across your cheek, jaw, or mouth.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my high-resolution 3D MRI scan show an artery pressing directly against my trigeminal nerve root?",
            "safety_question": "Was my blood sodium level and HLA-B*1502 genetic test checked before starting carbamazepine to prevent low sodium or severe allergic skin rashes?",
            "action_threshold_question": "Am I a candidate for microvascular decompression (MVD) surgery to place a tiny Teflon cushion between the blood vessel and the nerve?"
        },
        "red_flags": [
            "Severe facial numbness, loss of the eye blink reflex (corneal reflex), bilateral facial shooting pain (suspect Multiple Sclerosis), or acute hearing loss"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Trigeminal neuralgia is a chronic pain condition that affects the trigeminal nerve, which carries sensation from your face to your brain.",
                "plain_analogy": "An exposed electrical wire in your face having its protective insulation rubbed off by a pulsating blood vessel, causing sudden electrical shocks.",
                "lifestyle_action": "Avoid cold drafts on your face. Chew food on the unaffected side. Use gentle warm water when washing."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Carbamazepine (Tegretol)", "Oxcarbazepine (Trileptal)", "Baclofen", "Lamotrigine"],
                "dosing_gdmt": "Carbamazepine 100-200 mg BID initially, titrated by 100-200 mg every few days to pain control (typical dose 400-800 mg daily; max 1200 mg).",
                "black_box_warning": "Carbamazepine: Toxic epidermal necrolysis (TEN) and Stevens-Johnson syndrome (SJS) in HLA-B*1502 carriers; aplastic anemia and agranulocytosis.",
                "organ_clearance_cutoffs": "Monitor for SIADH and hyponatremia (check serum sodium periodically); monitor CBC and LFTs quarterly."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EAN Trigeminal Neuralgia",
                "pmid_or_doi": "10.1111/ene.13950",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "Carbamazepine/oxcarbazepine achieves initial pain relief in >80%; microvascular decompression achieves 5-year pain freedom in 73% without nerve numbness."
            }
        }
    },
    {
        "id": "DOC-CARD-247",
        "icd10": "G93.2",
        "condition": "Idiopathic Intracranial Hypertension (Pseudotumor Cerebri)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "JAMA (NORDIC Trial) & Cochrane Database",
        "citation": "NORDIC Idiopathic Intracranial Hypertension Study Group. Effect of Acetazolamide on Visual Function in Patients with Idiopathic Intracranial Hypertension and Mild Visual Loss: The Idiopathic Intracranial Hypertension Treatment Trial (IIHTT). JAMA. 2014;311(16):1641-1651.",
        "doi_or_source": "10.1001/jama.2014.3312",
        "clinical_evidence": "Idiopathic Intracranial Hypertension (IIH, formerly pseudotumor cerebri) is characterized by elevated intracranial pressure (>250 mm H2O in adults) without hydrocephalus, mass lesion, or abnormal CSF composition, predominantly affecting young obese females of childbearing age. Modified Dandy criteria require papilledema, normal neurological exam (except 6th cranial nerve abducens palsy), and MRI showing neuroimaging signs of raised ICP (empty sella turcica, flattening of posterior sclerae, distension of perioptic subarachnoid space, and bilateral transverse venous sinus stenosis). In the landmark multicenter double-blind IIHTT trial (n=165 patients with mild visual field loss), high-dose acetazolamide (titrated up to 4 g daily) plus a low-sodium weight-reduction diet produced significantly greater improvement in visual field perimetric mean deviation (MD: +1.43 dB; p=0.04) and papilledema grade (mean reduction -0.70 Frisén units; p<0.001) compared with diet alone. Weight reduction of 10-15% cures IIH in >70%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured multidisciplinary weight loss program (GLP-1 receptor agonists or bariatric surgery) targeting 10-15% total body weight reduction; strict dietary sodium restriction (<2,000 mg/day); avoidance of contributing drugs (tetracyclines, excess vitamin A/retinoids, and recombinant growth hormone).",
            "monitoring_cadence": "Formal Humphrey automated visual field testing (24-2 or 30-2) and optical coherence tomography (OCT) of retinal nerve fiber layer (RNFL) thickness every 4 weeks initially, then quarterly until papilledema completely resolves.",
            "clinical_thresholds": "Progressive visual field loss (perimetric mean deviation worsening to <-7 dB) or fulminant IIH with severe vision decline within 4 weeks requires emergent surgical intervention (optic nerve sheath fenestration [ONSF] or transverse sinus stenting)."
        },
        "patient_plain_language": "Idiopathic intracranial hypertension (pseudotumor cerebri) is a condition where high pressure builds up inside your skull, acting just like a brain tumor even though no actual tumor exists. The fluid that cushions your brain (cerebrospinal fluid) cannot drain away quickly enough, putting high pressure on your optic nerves (the cables connecting your eyes to your brain). This causes daily throbbing headaches, whooshing sounds in your ears (pulsatile tinnitus), and brief blackouts in your vision when bending over.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Frisén papilledema grade on eye exam and my Humphrey visual field loss measurement?",
            "safety_question": "What dose of acetazolamide (Diamox) do I need to take, and should I take potassium supplements to avoid tingling in my fingers and toes?",
            "action_threshold_question": "What degree of vision dimming or blurriness signals that I need urgent optic nerve fenestration surgery to protect my sight?"
        },
        "red_flags": [
            "Sudden loss of peripheral vision, persistent graying out of sight when changing positions, severe double vision, or visual acuity dropping rapidly"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Idiopathic intracranial hypertension occurs when high pressure builds up inside the skull, causing headaches and vision problems.",
                "plain_analogy": "A clogged drain in the skull that lets brain fluid build up like high water pressure, squishing the delicate optic nerves from behind.",
                "lifestyle_action": "Target 10-15% weight loss. Restrict sodium. Stop all tetracycline acne medications and vitamin A supplements immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Acetazolamide (Diamox)", "Topiramate", "Furosemide"],
                "dosing_gdmt": "Acetazolamide 500 mg orally BID, titrated by 500 mg every 1-2 weeks up to maximum tolerated dose (typically 1-2 g daily; max 4 g).",
                "black_box_warning": "Acetazolamide: Hypokalemia, metabolic acidosis, and paresthesias; contraindicated in known sulfonamide allergy.",
                "organ_clearance_cutoffs": "Monitor serum electrolytes (bicarbonate, potassium) and renal function at baseline and monthly during titration."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "IIHTT Trial",
                "pmid_or_doi": "10.1001/jama.2014.3312",
                "cebm_level": 2,
                "sample_size": 165,
                "endpoints": "Visual field function and papilledema grade improved significantly with high-dose acetazolamide plus diet vs diet alone (p=0.04); quality of life score boosted."
            }
        }
    },
    {
        "id": "DOC-CARD-248",
        "icd10": "G44.009",
        "condition": "Cluster Headache",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "JAMA & The Lancet Neurology (High-Flow O2 & Verapamil)",
        "citation": "Cohen AS et al. High-flow oxygen for treatment of cluster headache: a randomized, double-blind, placebo-controlled trial. JAMA. 2009;302(22):2451-2457.",
        "doi_or_source": "10.1001/jama.2009.1855",
        "clinical_evidence": "Cluster headache is the most severe primary headache disorder, classified as a trigeminal autonomic cephalalgia (TAC) characterized by strictly unilateral, excruciating, piercing/boring orbital or supraorbital pain lasting 15 to 180 minutes, accompanied by prominent ipsilateral cranial autonomic features (conjunctival injection, lacrimation, nasal congestion, rhinorrhea, forehead sweating, and partial Horner's syndrome [ptosis and miosis]). In the landmark double-blind placebo-controlled crossover trial (n=109 patients with 150 attacks treated), high-flow 100% normobaric oxygen (12 L/min via non-rebreather face mask for 15 minutes) rendered 78% of patients pain-free at 15 minutes compared with only 20% on medical air placebo (p<0.001; NNT = 1.7). Subcutaneous sumatriptan (6 mg) provides rapid abortion in >75% within 15 minutes. First-line preventative therapy is high-dose verapamil (240-960 mg/day).",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute avoidance of all alcohol during active cluster bouts (alcohol triggers an attack within 45 minutes in >90% of active patients); avoidance of volatile chemical fumes, petroleum solvents, and daytime naps.",
            "monitoring_cadence": "Baseline and serial 12-lead ECG monitoring every 2 weeks during verapamil dose titration to detect PR-interval prolongation and heart block; tracking attack diary.",
            "clinical_thresholds": "Occurrence of >=2 cluster attacks per day warrants immediate bridging steroid burst (prednisone 60-80 mg daily tapered over 2-3 weeks) while concurrently titrating verapamil maintenance."
        },
        "patient_plain_language": "Cluster headaches are excruciatingly painful headaches known as 'suicide headaches' due to their extreme severity. The pain attacks strike like an ice-pick stabbing into or around one eye, lasting from 30 minutes to 3 hours, often waking you from sleep at the exact same hour every night. During an attack, the affected eye tears up, the eyelid droops, and your nose becomes stuffed or runny. Sufferers are intensely restless, pacing the room rather than lying still.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I have a home medical prescription for a high-flow 100% oxygen cylinder (with a 12-15 L/min regulator and non-rebreather face mask)?",
            "safety_question": "Has my ECG been checked before increasing my verapamil dose to ensure my heart's electrical timing (PR interval) is safe?",
            "action_threshold_question": "Can I use subcutaneous sumatriptan injections or nasal zolmitriptan sprays alongside my oxygen tank for immediate abortive relief?"
        },
        "red_flags": [
            "Sudden thunderclap onset of maximal pain in <1 minute (rule out subarachnoid hemorrhage), permanent vision changes, or high fever with stiff neck"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cluster headaches are a series of relatively short but extremely painful headaches that occur in cycles or bouts.",
                "plain_analogy": "A red-hot poker being driven directly into one eye socket on a clockwork schedule every night.",
                "lifestyle_action": "Zero alcohol during cluster periods. Keep an oxygen tank beside your bed. Do not lie down during attacks; pacing helps."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Oxygen Therapy 100%", "Sumatriptan Subcutaneous (6 mg)", "Zolmitriptan Nasal Spray", "Verapamil", "Galcanezumab (Emgality)"],
                "dosing_gdmt": "Acute: 100% O2 at 12-15 L/min via non-rebreather mask for 15 min + Sumatriptan 6 mg SC. Prevention: Verapamil 240-480 mg daily.",
                "black_box_warning": "Sumatriptan: Coronary vasospasm, myocardial infarction, and ventricular arrhythmias; contraindicated in ischemic heart disease or uncontrolled hypertension.",
                "organ_clearance_cutoffs": "Monitor baseline and serial ECGs with verapamil; hold if PR interval exceeds 0.20 seconds."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "High-Flow O2 Trial",
                "pmid_or_doi": "10.1001/jama.2009.1855",
                "cebm_level": 2,
                "sample_size": 109,
                "endpoints": "Pain freedom at 15 minutes achieved in 78% with high-flow oxygen vs 20% placebo (p<0.001; NNT=1.7); zero adverse events."
            }
        }
    },
    {
        "id": "DOC-CARD-249",
        "icd10": "G45.9",
        "condition": "Transient Ischemic Attack (TIA)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (CHANCE & POINT Trials) & AHA/ASA Guidelines",
        "citation": "Johnston SC et al. Clopidogrel and Aspirin in Acute Ischemic Stroke and High-Risk TIA (POINT). N Engl J Med. 2018;379(3):215-225.",
        "doi_or_source": "10.1056/NEJMoa1800410",
        "clinical_evidence": "A Transient Ischemic Attack (TIA) is a transient episode of neurological dysfunction caused by focal brain, spinal cord, or retinal ischemia, without acute infarction on diffusion-weighted MRI (DWI). TIA carries an immediate 10-15% risk of disabling ischemic stroke within 90 days, with half occurring within the first 48 hours. In the landmark POINT (n=4881) and CHANCE (n=5170) trials in high-risk TIA (ABCD2 score >=4) or minor stroke, dual antiplatelet therapy (DAPT: Aspirin 81 mg + Clopidogrel 300-600 mg load then 75 mg daily) initiated within 12-24 hours and continued for exactly 21 days significantly reduced subsequent major ischemic stroke by 25-32% compared with aspirin monotherapy (HR 0.68-0.75; p<0.001) without a significant excess in major hemorrhage when capped at 21 days.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate admission to an emergency acute stroke unit or rapid-access TIA clinic; immediate carotid duplex ultrasound (carotid endarterectomy within 7-14 days if symptomatic 70-99% stenosis); Mediterranean diet; smoking cessation.",
            "monitoring_cadence": "ABCD2 risk score calculation at triage; continuous cardiac telemetry for >=24-48 hours (or 30-day mobile cardiac outpatient telemetry) to detect occult atrial fibrillation; brain MRI with diffusion-weighted imaging (DWI); lipid panel.",
            "clinical_thresholds": "ABCD2 score >=4 (Age >=60 [1], BP >=140/90 [1], Clinical unilateral weakness [2] or speech impairment [1], Duration >=60m [2] or 10-59m [1], Diabetes [1]) mandates immediate DAPT and inpatient observation."
        },
        "patient_plain_language": "A transient ischemic attack (TIA), often called a 'warning stroke' or 'mini-stroke', occurs when blood flow to part of your brain is briefly blocked by a small traveling blood clot. The symptoms—such as a droopy face, weak arm, or slurred speech—may disappear completely after a few minutes, but a TIA is an emergency warning that a major, permanent stroke could strike within the next 48 hours.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my ABCD2 stroke risk score, and did my brain MRI show any hidden tiny strokes on diffusion-weighted imaging (DWI)?",
            "safety_question": "Am I on the 21-day dual blood thinner combination (aspirin plus clopidogrel) to protect me from a major stroke during the high-risk window?",
            "action_threshold_question": "Did my ultrasound or CT scan show narrowing in my carotid neck arteries that requires a surgical cleaning procedure (endarterectomy)?"
        },
        "red_flags": [
            "Sudden facial drooping, arm numbness or weakness, speech slurring or confusion, sudden vision loss in one eye, or sudden balance loss (F-A-S-T signs)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A transient ischemic attack is a temporary blockage of blood flow to the brain, serving as a critical warning sign for a major stroke.",
                "plain_analogy": "A temporary power flicker in the brain's grid caused by a passing clot, warning of a total blackout if not treated immediately.",
                "lifestyle_action": "Call 911 immediately even if symptoms completely clear. Take blood thinners as prescribed for the full 21 days."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Aspirin", "Clopidogrel (Plavix)", "Atorvastatin 80 mg", "Ticagrelor (THALES protocol)"],
                "dosing_gdmt": "DAPT for 21 days: Clopidogrel 300 mg load, then 75 mg daily PLUS Aspirin 81 mg daily, transitioning to monotherapy on day 22.",
                "black_box_warning": "Clopidogrel: Diminished antiplatelet effect in patients who are CYP2C19 poor metabolizers; consider alternative (ticagrelor).",
                "organ_clearance_cutoffs": "Initiate high-intensity statin (Atorvastatin 80 mg daily) immediately regardless of baseline LDL-C."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POINT / CHANCE",
                "pmid_or_doi": "10.1056/NEJMoa1800410",
                "cebm_level": 2,
                "sample_size": 4881,
                "endpoints": "Subsequent ischemic stroke reduced by 28% with 21-day DAPT vs aspirin alone (5.0% vs 6.5%; HR 0.72; p=0.001); risk reduction front-loaded."
            }
        }
    },
    {
        "id": "DOC-CARD-250",
        "icd10": "F01.50",
        "condition": "Vascular Dementia",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA/ASA Scientific Statement & Cochrane Review",
        "source_body": "Stroke (AHA/ASA Scientific Statement) & Cochrane",
        "citation": "Gorelick PB et al. Vascular Contributions to Cognitive Impairment and Dementia: A Statement for Healthcare Professionals From the AHA/ASA. Stroke. 2011;42(9):2672-2713.",
        "doi_or_source": "10.1161/STR.0b013e3182299496",
        "clinical_evidence": "Vascular Cognitive Impairment and Dementia (VCID) is the second most common form of dementia, encompassing multi-infarct dementia, strategic single-infarct dementia, and subcortical ischemic vascular dementia (Binswanger's disease driven by arteriolosclerosis). Brain MRI is the diagnostic modality of choice, revealing extensive confluent periventricular white matter hyperintensities (Fazekas Grade 3), multiple lacunar infarcts, and microbleeds on susceptibility-weighted imaging (SWI). Unlike the insidious memory-predominant course of Alzheimer's, vascular dementia classically presents with stepwise cognitive decline, prominent dysexecutive syndrome (impaired planning, sequencing, processing speed), and early psychomotor and gait slowing. Aggressive vascular risk reduction (BP <130/80 mmHg with ACEi/ARBs, statins, and antiplatelet therapy) halts further microvascular accumulation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Mediterranean-DASH Diet Intervention for Neurodegenerative Delay (MIND diet); 150 minutes/week of structured aerobic exercise; cognitive stimulation therapy; fall prevention home modifications.",
            "monitoring_cadence": "Montreal Cognitive Assessment (MoCA, superior to MMSE for executive dysfunction) every 6 months; annual brain MRI tracking progression of white matter hyperintensities; home blood pressure logs.",
            "clinical_thresholds": "MoCA score <26 with executive deficits (Trail Making Test B impairment) and Fazekas Grade 2-3 white matter changes establishes subcortical vascular cognitive impairment."
        },
        "patient_plain_language": "Vascular dementia is memory and thinking loss caused by reduced blood flow to the brain, often following multiple silent 'mini-strokes' or long-term narrowing of tiny blood vessels in the brain. Unlike other dementias that primarily start with memory loss, vascular dementia often starts with slowed thinking, difficulty planning and organizing daily tasks, and a hesitant, unsteady walking gait.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my Montreal Cognitive Assessment (MoCA) score, particularly on the executive planning and clock-drawing sections?",
            "safety_question": "Does my brain MRI show extensive white matter damage or silent lacunar strokes, and is my blood pressure strictly controlled?",
            "action_threshold_question": "Would a cholinesterase inhibitor medication (such as donepezil) be beneficial if there is mixed Alzheimer's and vascular disease?"
        },
        "red_flags": [
            "Sudden stepwise drop in mental clarity, sudden new weakness or numbness on one side of the body, difficulty swallowing, or frequent unexplained falls"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Vascular dementia is a decline in thinking skills caused by conditions that block or reduce blood flow to various regions of the brain.",
                "plain_analogy": "A city grid suffering rolling localized brownouts because the small electrical cables supplying power to neighborhoods are narrowed and failing.",
                "lifestyle_action": "Keep blood pressure strictly under 130/80. Walk 30 minutes every day. Follow the Mediterranean brain-healthy diet."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Aspirin", "Atorvastatin", "Donepezil", "Memantine", "Lisinopril"],
                "dosing_gdmt": "Intensive BP control with ACEi/ARB (target SBP <130 mmHg) + High-intensity statin + Aspirin 81 mg daily for secondary prevention.",
                "black_box_warning": "Antipsychotics in dementia: Increased risk of all-cause mortality and ischemic cerebrovascular adverse events.",
                "organ_clearance_cutoffs": "Cholinesterase inhibitors (donepezil 5-10 mg daily) show modest cognitive benefits in mixed vascular dementia; check for bradycardia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHA/ASA Vascular Dementia",
                "pmid_or_doi": "10.1161/STR.0b013e3182299496",
                "cebm_level": 1,
                "sample_size": 4100,
                "endpoints": "Intensive blood pressure lowering (SBP <120 vs <140 mmHg) in SPRINT-MIND reduced mild cognitive impairment risk by 19% (HR 0.81; p=0.007)."
            }
        }
    },
    {
        "id": "DOC-CARD-251",
        "icd10": "G31.83",
        "condition": "Dementia with Lewy Bodies (DLB)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Fourth Consensus Report of DLB Consortium",
        "source_body": "Neurology (DLB Consortium Guidelines)",
        "citation": "McKeith IG et al. Diagnosis and management of dementia with Lewy bodies: Fourth consensus report of the DLB Consortium. Neurology. 2017;89(1):88-100.",
        "doi_or_source": "10.1212/WNL.0000000000004058",
        "clinical_evidence": "Dementia with Lewy Bodies (DLB) is pathologically characterized by widespread neuronal alpha-synuclein inclusions (Lewy bodies and Lewy neurites) throughout the neocortex, paralimbic, and brainstem structures. Core clinical features require: (1) fluctuating cognition with pronounced variations in attention and alertness; (2) recurrent, complex, well-formed visual hallucinations (present in >80%); (3) REM sleep behavior disorder (RBD: dream enactment, kicking/punching during sleep, preceding dementia by years); and (4) one or more spontaneous cardinal features of parkinsonism (bradykinesia, rigidity, rest tremor). Indicative biomarkers include reduced dopamine transporter (DaT) uptake in basal ganglia on DaTscan SPECT (sensitivity 78%, specificity 90%) and preserved temporal lobe structures on MRI. Patients exhibit severe neuroleptic sensitivity (up to 50% suffer acute severe parkinsonism, neuroleptic malignant syndrome, or death when exposed to typical antipsychotics).",
        "solution_protocol": {
            "non_pharmacological_targets": "Bed safety modifications for REM sleep behavior disorder (placing mattress on floor, removing sharp nightstands); gentle lighting and reassurance for visual hallucinations without challenging reality; physical therapy for parkinsonian gait.",
            "monitoring_cadence": "Quarterly clinical tracking of cognitive fluctuations, Epworth Sleepiness Scale, and UPDRS motor scores; bone mineral density scan (high fall and fracture risk); formal depression screening.",
            "clinical_thresholds": "Severe REM sleep behavior disorder causing traumatic injury warrants low-dose melatonin (3-12 mg) or clonazepam (0.25-0.5 mg); cognitive impairment responds robustly to cholinesterase inhibitors (donepezil/rivastigmine)."
        },
        "patient_plain_language": "Dementia with Lewy bodies (DLB) is a progressive brain condition caused by abnormal microscopic protein deposits called Lewy bodies forming inside your brain cells. It causes memory and thinking problems that fluctuate dramatically from hour to hour, realistic visual hallucinations (often seeing people or animals that are not there), physically acting out dreams while asleep (kicking or shouting), and Parkinson's-like stiffness and shuffling.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my brain DaTscan or FDG-PET scan show the distinctive loss of dopamine transporters in the basal ganglia confirming Lewy body disease?",
            "safety_question": "Is my medical chart clearly flagged with an allergy alert to NEVER give me standard antipsychotic tranquilizers (like haloperidol)?",
            "action_threshold_question": "How will we balance taking carbidopa/levodopa for my motor stiffness without worsening my visual hallucinations?"
        },
        "red_flags": [
            "Acute severe muscle rigidity with high fever and altered consciousness after receiving an anti-nausea or psychiatric pill (Neuroleptic Malignant Syndrome)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dementia with Lewy bodies is a progressive dementia that leads to a decline in thinking, reasoning, and independent function, combined with movement problems.",
                "plain_analogy": "Protein clumps cluttering brain wiring, causing fluctuating mental brownouts, visual hallucinations, and dream-enacting sleep.",
                "lifestyle_action": "Pad bedroom walls and bedside floor. Avoid all older psychiatric sedatives. Maintain steady daily routines."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Donepezil (Aricept)", "Rivastigmine Patch (Exelon)", "Carbidopa/Levodopa", "Melatonin", "Pimavanserin"],
                "dosing_gdmt": "First-line: Donepezil 5-10 mg daily or Rivastigmine patch 4.6-9.5 mg/24h. For motor parkinsonism: Low-dose Carbidopa/Levodopa 25/100 mg TID.",
                "black_box_warning": "Antipsychotics: Severe neuroleptic sensitivity; typical neuroleptics (haloperidol) can trigger irreversible rigidity and fatal cardiovascular collapse.",
                "organ_clearance_cutoffs": "If an antipsychotic is absolutely necessary for distressing psychosis, only Quetiapine (12.5-25 mg) or Pimavanserin is tolerated."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DLB Consortium Consensus",
                "pmid_or_doi": "10.1212/WNL.0000000000004058",
                "cebm_level": 1,
                "sample_size": 2500,
                "endpoints": "Cholinesterase inhibitors improve cognitive fluctuation and attention scores by 30%; DaTscan provides 90% diagnostic specificity vs Alzheimer's."
            }
        }
    },
    {
        "id": "DOC-CARD-252",
        "icd10": "G31.09",
        "condition": "Frontotemporal Dementia (FTD)",
        "specialty": "Neurology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Consensus Criteria & Cohort Review",
        "source_body": "Brain & The Lancet Neurology (FTDC Criteria)",
        "citation": "Rascovsky K et al. Sensitivity of revised diagnostic criteria for the behavioural variant of frontotemporal dementia (bvFTD). Brain. 2011;134(Pt 9):2456-2477.",
        "doi_or_source": "10.1093/brain/awr179",
        "clinical_evidence": "Frontotemporal Dementia (FTD / Frontotemporal Lobar Degeneration [FTLD]) is the most common cause of early-onset dementia in patients <65 years, pathologically driven by tau inclusions (Pick bodies), TDP-43, or FUS aggregates. The behavioral variant (bvFTD) is diagnosed via the international FTDC criteria requiring at least 3 of 6 core features: (1) early behavioral disinhibition (socially inappropriate actions, loss of manners); (2) early apathy or inertia; (3) early loss of empathy or sympathy; (4) early perseverative, stereotyped, or compulsive behavior; (5) hyperorality and dietary changes (gluttony, sweet cravings); and (6) executive cognitive deficits with relative sparing of episodic memory and visuospatial function. Structural MRI shows asymmetric knife-blade atrophy of frontal and anterior temporal lobes. Genetic mutations (C9orf72 hexanucleotide expansion, GRN, MAPT) account for 30-40% of familial cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured environmental routines; secure lockboxes for food and finances (protecting against hyperorality and impulsive financial disinhibition); specialized caregiver support groups and respite care; genetic counseling for first-degree relatives.",
            "monitoring_cadence": "Frontal Behavioral Inventory (FBI) and Clinical Dementia Rating scale modified for FTLD (CDR-FTLD) every 6 months; speech-language evaluation for primary progressive aphasia variants; annual caregiver burden assessments.",
            "clinical_thresholds": "Emergence of motor neuron disease features (fasciculations, muscle wasting, hyperreflexia indicating FTD-ALS overlap) or progressive dysphagia requires immediate multidisciplinary palliative and swallowing evaluation."
        },
        "patient_plain_language": "Frontotemporal dementia (FTD) is a group of brain disorders caused by nerve cell damage and shrinking in the front and side regions of your brain (the frontal and temporal lobes). Because these areas govern your personality, behavior, judgment, empathy, and language, FTD typically starts with major personality shifts—such as socially inappropriate comments, loss of sympathy for family, obsessive rituals, or a craving for sweets—often while memory remains intact.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my brain MRI show frontotemporal lobar atrophy, and should we order a C9orf72 genetic test for familial frontotemporal degeneration?",
            "safety_question": "Why are standard Alzheimer's medications (like donepezil or memantine) not recommended, and could they make my behavioral symptoms worse?",
            "action_threshold_question": "What medications (such as SSRIs like sertraline or trazodone) can help safely tone down compulsive habits and emotional agitation?"
        },
        "red_flags": [
            "Rapid muscle twitching, muscle wasting, and weakness in hands or legs (suspect FTD-ALS overlap), severe choking on food, or dangerous impulsive behaviors"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Frontotemporal dementia is a group of disorders caused by progressive nerve cell loss in the brain's frontal lobes or its temporal lobes, affecting personality and speech.",
                "plain_analogy": "The brain's behavioral filter and social conductor wearing away, so personal judgment and emotional empathy are lost.",
                "lifestyle_action": "Secure bank accounts and credit cards. Lock the pantry if sweet bingeing occurs. Establish peaceful, consistent routines."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Sertraline (Off-label)", "Paroxetine", "Trazodone", "Citalopram"],
                "dosing_gdmt": "SSRIs (Sertraline 50-150 mg daily or Paroxetine 20-40 mg daily) significantly reduce repetitive behaviors, disinhibition, and carbohydrate binging.",
                "black_box_warning": "Cholinesterase inhibitors (Donepezil/Galantamine): May worsen behavioral agitation in FTD; generally avoided.",
                "organ_clearance_cutoffs": "Avoid typical antipsychotics; if low-dose atypical antipsychotics are required, obtain informed family consent."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "FTDC Consensus",
                "pmid_or_doi": "10.1093/brain/awr179",
                "cebm_level": 1,
                "sample_size": 1780,
                "endpoints": "Revised FTDC criteria achieve 95% sensitivity for pathologically confirmed bvFTD; SSRIs significantly reduce Frontal Behavioral Inventory scores."
            }
        }
    },
    {
        "id": "DOC-CARD-253",
        "icd10": "F42.9",
        "condition": "Obsessive-Compulsive Disorder (OCD)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & APA Practice Guideline",
        "source_body": "Cochrane Database of Systematic Reviews & American Psychiatric Association",
        "citation": "Skapinakis P et al. Pharmacological and psychotherapeutic interventions for management of obsessive-compulsive disorder in adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2016;3(8):730-739.",
        "doi_or_source": "10.1016/S2215-0366(16)30069-4",
        "clinical_evidence": "Obsessive-Compulsive Disorder (OCD) is characterized by intrusive, distressing, ego-dystonic thoughts, urges, or images (obsessions) that trigger repetitive mental or physical behaviors (compulsions) performed to neutralize anxiety, consuming >1 hour daily. In a comprehensive network meta-analysis of 54 randomized trials (n=6652 patients), Exposure and Response Prevention (ERP) behavioral therapy combined with high-dose Selective Serotonin Reuptake Inhibitors (SSRIs) was significantly superior to either intervention alone for reduction in Yale-Brown Obsessive Compulsive Scale (Y-BOCS) scores (standardized mean difference -1.18; 95% CI -1.45 to -0.91; p<0.0001). SSRI doses required for OCD are typically substantially higher than for major depression (e.g. Fluoxetine up to 80 mg/day, Sertraline up to 200 mg/day) and require 8-12 weeks to assess clinical response.",
        "solution_protocol": {
            "non_pharmacological_targets": "Exposure and Response Prevention (ERP) psychotherapy: creating a graded hierarchy of feared triggers (in vivo and imaginal exposure) with deliberate, prolonged refusal to engage in neutralizing rituals; mindfulness techniques.",
            "monitoring_cadence": "Yale-Brown Obsessive Compulsive Scale (Y-BOCS) score tracking at baseline and every 4 weeks (clinical response defined as >=25-35% reduction in Y-BOCS); screen for co-occurring major depressive disorder and suicidality.",
            "clinical_thresholds": "Y-BOCS score >=24 indicates severe OCD; failure to respond to two successive trials of high-dose SSRIs for 12 weeks warrants augmentation with an atypical antipsychotic (Aripiprazole 2-10 mg or Risperidone 0.5-2 mg) or deep brain stimulation (DBS)."
        },
        "patient_plain_language": "Obsessive-compulsive disorder (OCD) is a mental health condition driven by a cycle of obsessions and compulsions. Obsessions are unwanted, intrusive, frightening thoughts or doubts (like fears of germs, harm, or symmetry) that get stuck on repeat in your mind, triggering intense anxiety. Compulsions are repetitive mental acts or physical behaviors (like washing hands, checking door locks, or tapping) you feel driven to perform to relieve the anxiety.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current score on the Yale-Brown Obsessive Compulsive Scale (Y-BOCS)?",
            "safety_question": "Is my SSRI medication dose high enough for OCD, and have we allowed a full 8 to 12 weeks to judge whether it is working?",
            "action_threshold_question": "How can I be connected with an OCD-specialist therapist trained in Exposure and Response Prevention (ERP) therapy?"
        },
        "red_flags": [
            "Severe unrelenting obsessions that consume >8 hours daily, skin breakdown and bleeding from compulsive handwashing, severe depression, or suicidal thoughts"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Obsessive-compulsive disorder is a common, chronic disorder in which a person has uncontrollable, recurring thoughts and behaviors that they feel the urge to repeat.",
                "plain_analogy": "A false fire alarm ringing continuously in your brain, convincing you that performing a repetitive ritual is the only way to silence the alarm.",
                "lifestyle_action": "Practice Exposure and Response Prevention daily. Do not ask family members for reassurance rituals. Exercise regularly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Fluoxetine (Prozac)", "Sertraline (Zoloft)", "Fluvoxamine", "Paroxetine", "Clomipramine (Anafranil)"],
                "dosing_gdmt": "Fluoxetine titrated to 60-80 mg daily, or Sertraline 200 mg daily. For treatment-resistant OCD: Clomipramine 100-250 mg daily.",
                "black_box_warning": "Antidepressants: Increased risk of suicidal thoughts and behaviors in children, adolescents, and young adults (under age 25).",
                "organ_clearance_cutoffs": "Monitor for QTc prolongation and anticholinergic side effects with tricyclic Clomipramine; check baseline ECG."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Lancet Psychiatry OCD Meta-Analysis",
                "pmid_or_doi": "10.1016/S2215-0366(16)30069-4",
                "cebm_level": 1,
                "sample_size": 6652,
                "endpoints": "ERP therapy combined with SSRIs achieves significant Y-BOCS reduction (SMD -1.18; p<0.0001); 65% achieve long-term clinical remission."
            }
        }
    },
    {
        "id": "DOC-CARD-254",
        "icd10": "F41.0",
        "condition": "Panic Disorder & Agoraphobia",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & APA Practice Guideline",
        "source_body": "Cochrane Database of Systematic Reviews & Lancet Psychiatry",
        "citation": "Bighelli I et al. Psychotherapeutic and pharmacological interventions for panic disorder in adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2018;5(7):590-600.",
        "doi_or_source": "10.1016/S2215-0366(18)30172-X",
        "clinical_evidence": "Panic disorder is characterized by recurrent unexpected panic attacks (abrupt surges of intense fear or intense discomfort reaching a peak within minutes, with at least 4 of 13 autonomic symptoms: palpitations, sweating, trembling, dyspnea, choking sensation, chest pain, nausea, dizziness, chills/heat, paresthesias, derealization/depersonalization, fear of losing control, and fear of dying) followed by at least 1 month of persistent worry about further attacks or maladaptive avoidance behavior (agoraphobia). In a network meta-analysis of 87 randomized controlled trials (n=12,823 patients), Cognitive Behavioral Therapy (CBT with interoceptive exposure) combined with an SSRI/SNRI achieved superior remission of panic attacks and reduction in agoraphobic avoidance compared with either treatment alone (odds ratio 2.45; 95% CI 1.72-3.48; p<0.0001). Long-term benzodiazepine monotherapy is discouraged due to tolerance and rebound panic.",
        "solution_protocol": {
            "non_pharmacological_targets": "Cognitive Behavioral Therapy (CBT): interoceptive exposure (deliberately inducing physical sensations like hyperventilation, spinning, or breath-holding to extinguish catastrophic misinterpretation of body cues); diaphragmatic breathing; elimination of caffeine and stimulants.",
            "monitoring_cadence": "Panic Disorder Severity Scale (PDSS) score at baseline and every 4 weeks; monitor blood pressure and resting heart rate; screen for co-occurring depression and alcohol use disorder.",
            "clinical_thresholds": "PDSS score reduction >=40% denotes clinical response; absence of panic attacks for 12 consecutive months on maintenance SSRI therapy warrants considering very slow medication taper."
        },
        "patient_plain_language": "Panic disorder is an anxiety condition where you experience sudden, terrifying surges of overwhelming fear and physical sensations called panic attacks. Out of nowhere, your heart pounds rapidly, your chest tightens, you gasp for breath, and you feel like you are having a heart attack, fainting, or dying. Because these attacks strike without warning, many people develop agoraphobia—avoiding crowded places, stores, or driving out of fear of having another attack.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current score on the Panic Disorder Severity Scale (PDSS)?",
            "safety_question": "Has a full medical evaluation (including an ECG and thyroid blood test) confirmed that my heart and thyroid are physically healthy?",
            "action_threshold_question": "How does interoceptive exposure therapy work in CBT to train my brain that racing heart sensations are harmless adrenaline rushes?"
        },
        "red_flags": [
            "Severe agoraphobic housebound isolation, turning to alcohol or sedatives to cope, profound depression, or active suicidal thoughts"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Panic disorder is an anxiety disorder where you have sudden attacks of fear and panic that have no apparent cause.",
                "plain_analogy": "An adrenaline alarm bell in the brain going off at full blast when there is no actual emergency or danger present.",
                "lifestyle_action": "Cut out all caffeine and energy drinks. Practice slow diaphragmatic breathing (4-second inhale, 6-second exhale). Do not flee panic situations."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Sertraline (Zoloft)", "Paroxetine", "Venlafaxine ER", "Clonazepam (Short-term bridge)"],
                "dosing_gdmt": "Start low to avoid transient anxiety: Sertraline 25 mg daily for 1 week, then titrate to 50-150 mg daily. Venlafaxine ER 37.5 mg to 150 mg.",
                "black_box_warning": "Benzodiazepines: Concomitant use with opioids may result in profound sedation, respiratory depression, coma, and death.",
                "organ_clearance_cutoffs": "Avoid benzodiazepines in patients with a history of substance abuse; taper slowly over months to prevent severe rebound panic."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Lancet Panic Network Meta-Analysis",
                "pmid_or_doi": "10.1016/S2215-0366(18)30172-X",
                "cebm_level": 1,
                "sample_size": 12823,
                "endpoints": "Combined CBT and SSRI therapy achieves 74% panic-free remission rate at 6 months (OR 2.45; p<0.0001); relapse rate significantly lower than medication alone."
            }
        }
    },
    {
        "id": "DOC-CARD-255",
        "icd10": "F60.3",
        "condition": "Borderline Personality Disorder (BPD)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & Randomized Trials",
        "source_body": "Cochrane Database of Systematic Reviews & JAMA Psychiatry",
        "citation": "Cristea IA et al. Efficacy of Psychotherapies for Borderline Personality Disorder: A Systematic Review and Meta-analysis. JAMA Psychiatry. 2017;74(4):319-328.",
        "doi_or_source": "10.1001/jamapsychiatry.2016.4290",
        "clinical_evidence": "Borderline Personality Disorder (BPD) is characterized by a pervasive pattern of emotional dysregulation, instability of interpersonal relationships, unstable self-image, marked impulsivity (spending, sex, substance abuse), recurrent suicidal behavior, gestures, or self-harm (NSSI), and chronic feelings of emptiness. In a comprehensive systematic review and meta-analysis of 33 randomized controlled trials (n=2256 patients), specialized psychotherapies—most notably Dialectical Behavior Therapy (DBT, standardized mean difference -0.34; p=0.005) and Mentalization-Based Therapy (MBT)—significantly reduced self-harm, suicidal gestures, emergency department visits, and BPD core symptom severity compared with treatment as usual. Pharmacotherapy has no primary disease-modifying FDA approval; low-dose second-generation antipsychotics or mood stabilizers offer modest adjunctive control for severe affective lability.",
        "solution_protocol": {
            "non_pharmacological_targets": "Comprehensive Dialectical Behavior Therapy (DBT): weekly individual therapy, weekly DBT skills training group (mindfulness, distress tolerance, emotion regulation, interpersonal effectiveness), and between-session phone coaching; written crisis safety plan.",
            "monitoring_cadence": "Zanarini Rating Scale for Borderline Personality Disorder (ZAN-BPD) every 3 months; structured continuous suicide and self-harm risk assessments; regular review of medication polypharmacy.",
            "clinical_thresholds": "Acute life-threatening self-harm or active suicidal crisis requires immediate safety planning and brief crisis stabilization; avoid prolonged psychiatric hospitalizations which cause regression."
        },
        "patient_plain_language": "Borderline personality disorder (BPD) is a mental health condition characterized by intense emotional sensitivity and difficulty regulating emotions. Sufferers experience emotions like emotional third-degree burns—feeling emotional pain far more intensely and for longer than others. This leads to dramatic mood shifts, intense fears of abandonment, rocky relationships, impulsive actions, and self-harm when distress becomes overwhelming.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current score on the Zanarini Rating Scale for Borderline Personality Disorder (ZAN-BPD)?",
            "safety_question": "Do I have an active, written DBT crisis safety plan with emergency contact numbers and specific distress tolerance skills to use during an emotional storm?",
            "action_threshold_question": "How can I join a certified Dialectical Behavior Therapy (DBT) skills training group to learn emotion regulation tools?"
        },
        "red_flags": [
            "Severe escalating self-harm, active suicide preparation or plan, acute intoxication combined with despair, or severe dissociative episodes"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Borderline personality disorder is an illness marked by an ongoing pattern of varying moods, self-image, and behavior.",
                "plain_analogy": "Having an emotional thermostat that is hypersensitive, causing feelings to spike rapidly into intense fires that take hours to cool.",
                "lifestyle_action": "Enroll in DBT skills training. Practice the TIPP distress tolerance skills (temperature ice water, intense exercise, paced breathing). Keep a diary card."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Aripiprazole (Adjunctive)", "Quetiapine", "Lamotrigine", "Fluoxetine"],
                "dosing_gdmt": "No FDA-approved drugs for BPD. Low-dose Aripiprazole 2-10 mg or Quetiapine 50-150 mg daily used adjunctively for severe affective instability.",
                "black_box_warning": "Avoid long-term benzodiazepine prescriptions: High risk of behavioral disinhibition, overdose in impulsivity, and physiological dependence.",
                "organ_clearance_cutoffs": "Regularly audit medications to minimize polypharmacy; psychotherapy is the primary, proven curative treatment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "JAMA BPD Meta-Analysis",
                "pmid_or_doi": "10.1001/jamapsychiatry.2016.4290",
                "cebm_level": 1,
                "sample_size": 2256,
                "endpoints": "DBT reduces self-harm by 50% and psychiatric hospitalizations by 40% vs control (p=0.005); 10-year remission rates exceed 85%."
            }
        }
    },
    {
        "id": "DOC-CARD-256",
        "icd10": "H81.09",
        "condition": "Meniere's Disease (Endolymphatic Hydrops)",
        "specialty": "Otolaryngology",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNS Clinical Practice Guideline & Cochrane Review",
        "source_body": "Otolaryngology-Head and Neck Surgery (AAO-HNS Guidelines)",
        "citation": "Basura GJ et al. Clinical Practice Guideline: Meniere's Disease. Otolaryngol Head Neck Surg. 2020;162(2_suppl):S1-S55.",
        "doi_or_source": "10.1177/0194599820901439",
        "clinical_evidence": "Meniere's disease is an inner ear disorder pathologically characterized by endolymphatic hydrops (fluid distension of the endolymphatic system in the cochlea and vestibular labyrinth). The definitive diagnostic criteria established by AAO-HNS and the Bárány Society require: (1) two or more spontaneous episodes of rotational vertigo lasting between 20 minutes and 12 hours; (2) audiometrically documented low-to-medium frequency sensorineural hearing loss in the affected ear on at least one occasion before, during, or after an episode; and (3) fluctuating aural fullness or tinnitus in the affected ear. First-line conservative management with dietary sodium restriction (<1,500-2,000 mg/day) and oral diuretics (hydrochlorothiazide/triamterene) or betahistine reduces vertigo attack frequency in >70-80% of patients. Intratympanic dexamethasone or gentamicin is effective in refractory cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict daily dietary sodium restriction (<1,500-2,000 mg/day without sudden fluctuations); elimination of caffeine, alcohol, and excessive monosodium glutamate (MSG); vestibular rehabilitation therapy between acute attacks.",
            "monitoring_cadence": "Serial pure-tone audiometry at 3, 6, and 12 months; vestibular function testing (caloric testing and video head impulse test [vHIT]); vertigo attack diary tracking frequency and duration.",
            "clinical_thresholds": "Disabling Tumarkin 'otolithic drop attacks' (sudden falls without loss of consciousness) or intractable vertigo spells despite 3 months of medical therapy warrants intratympanic gentamicin chemical labyrinthectomy or surgical endolymphatic sac decompression."
        },
        "patient_plain_language": "Meniere's disease is an inner ear disorder caused by excess fluid pressure building up inside the hearing and balance chambers of your inner ear. This fluid buildup triggers sudden attacks of violent room-spinning dizziness (vertigo) that last for hours, accompanied by nausea, a roaring sound in your ear (tinnitus), a clogged feeling of pressure in the ear, and temporary loss of low-pitched hearing.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my audiogram hearing test show the classic low-frequency hearing loss that confirms Meniere's disease?",
            "safety_question": "What is my daily sodium limit, and should I take a mild water pill (diuretic) to prevent fluid pressure from building up in my inner ear?",
            "action_threshold_question": "What rescue medication (like meclizine or sublingual ondansetron) should I carry with me at all times for acute vertigo attacks?"
        },
        "red_flags": [
            "Sudden falling to the ground without warning while remaining fully awake (Tumarkin drop attacks), new weakness in your face or arms, or sudden slurred speech"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Meniere's disease is an inner ear disorder that causes episodes in which you feel as if you are spinning (vertigo), and you have fluctuating hearing loss.",
                "plain_analogy": "High water pressure inside the inner ear's delicate canals, disrupting both hearing and balance gyroscopes at the same time.",
                "lifestyle_action": "Limit sodium strictly under 2,000 mg daily. Spread water intake evenly. Keep emergency vertigo pills in your pocket."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Triamterene/HCTZ (Dyazide)", "Meclizine", "Betahistine", "Dexamethasone (Intratympanic)", "Gentamicin (Intratympanic)"],
                "dosing_gdmt": "Prevention: Triamterene 37.5 mg / HCTZ 25 mg daily. Acute attacks: Meclizine 25-50 mg PO + Ondansetron 4-8 mg ODT.",
                "black_box_warning": "Intratympanic Gentamicin: Irreversible sensorineural hearing loss; reserve for severe unilateral vertigo refractory to conservative therapy.",
                "organ_clearance_cutoffs": "Monitor serum electrolytes and renal function periodically on thiazide diuretics."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO-HNS Meniere Guideline",
                "pmid_or_doi": "10.1177/0194599820901439",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Dietary sodium restriction and diuretics control vertigo attack frequency in >75%; intratympanic gentamicin achieves >85% vertigo control."
            }
        }
    },
    {
        "id": "DOC-CARD-257",
        "icd10": "H90.5",
        "condition": "Sudden Sensorineural Hearing Loss (SSNHL)",
        "specialty": "Otolaryngology",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNS Clinical Practice Guideline & Randomized Trials",
        "source_body": "Otolaryngology-Head and Neck Surgery & JAMA Otolaryngology",
        "citation": "Chandrasekhar SS et al. Clinical Practice Guideline: Sudden Hearing Loss (Update). Otolaryngol Head Neck Surg. 2019;161(1_suppl):S1-S45.",
        "doi_or_source": "10.1177/0194599819859885",
        "clinical_evidence": "Sudden Sensorineural Hearing Loss (SSNHL) is an otologic emergency defined as a rapid sensorineural hearing loss of >=30 decibels (dB) across at least 3 contiguous audiometric frequencies occurring within a 72-hour window. Approximately 90% of cases are idiopathic, with vascular ischemia, viral labyrinthitis, or cochlear autoimmune reactions implicated. Immediate initiation of high-dose systemic corticosteroids (prednisone 1 mg/kg/day, maximum 60 mg daily for 7-14 days followed by a taper) or intratympanic corticosteroid injections (dexamethasone 10-24 mg/mL or methylprednisolone) within the first 14 days achieves meaningful hearing recovery in 65-80% of patients. Hyperbaric oxygen therapy (HBOT) within 1 month of onset provides significant additional hearing gain (odds ratio 1.43). Gadolinium-enhanced brain MRI of the internal auditory canal (IAC) is mandatory to rule out vestibular schwannoma (acoustic neuroma, found in 3-5%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency audiology pure-tone audiometry within 24-48 hours; strict avoidance of loud noise exposure; hyperbaric oxygen therapy (HBOT) sessions within 2-4 weeks; contrast-enhanced MRI of internal auditory canals.",
            "monitoring_cadence": "Repeat pure-tone audiometry at 2 weeks, 4 weeks, and 3 months to monitor decibel recovery and word recognition score (WRS); brain MRI with IAC protocol.",
            "clinical_thresholds": "Sensorineural hearing drop >=30 dB across 3 frequencies warrants immediate high-dose oral steroids; incomplete recovery (<10 dB improvement) at 2-3 weeks triggers salvage intratympanic steroid injections."
        },
        "patient_plain_language": "Sudden sensorineural hearing loss (often called sudden deafness) is an ear emergency where you suddenly wake up with one ear completely blocked or hearing muffled, or notice the hearing vanish over a few hours. Many people mistakenly think their ear is just plugged with earwax or water, but it is actually damage to the nerve hair cells in your inner ear. Beginning steroid treatment within the first few days gives you the highest chance of getting your hearing back permanently.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the decibel hearing drop and word recognition percentage score on my emergency pure-tone audiogram?",
            "safety_question": "Have we started high-dose oral prednisone immediately, or should we add direct steroid injections through my eardrum (intratympanic)?",
            "action_threshold_question": "Is an MRI scan of my internal auditory canals scheduled to rule out a benign acoustic neuroma tumor on the hearing nerve?"
        },
        "red_flags": [
            "Sudden loss of hearing in one ear accompanied by facial muscle paralysis, severe continuous spinning dizziness, or difficulty walking"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sudden deafness is an unexplained, rapid loss of hearing that happens all at once or over a few days.",
                "plain_analogy": "A blown fuse in the inner ear's electrical hearing microphone; emergency steroid treatment can reset the fuse if started within days.",
                "lifestyle_action": "Do not wait for it to clear. Go to an ENT specialist or emergency clinic immediately. Protect the ear from loud noises."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Prednisone Oral", "Dexamethasone (Intratympanic Injection)", "Methylprednisolone", "Hyperbaric Oxygen"],
                "dosing_gdmt": "Prednisone 60 mg PO daily for 7-14 days followed by a 5-day taper. Intratympanic Dexamethasone 10-24 mg/mL (0.4-0.8 mL injected weekly for 3-4 doses).",
                "black_box_warning": "Delays beyond 2 to 4 weeks significantly reduce likelihood of hearing recovery, resulting in permanent deafness.",
                "organ_clearance_cutoffs": "Monitor blood glucose in diabetic patients on high-dose steroids; intratympanic injection avoids systemic steroid side effects."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO-HNS SSNHL Guideline",
                "pmid_or_doi": "10.1177/0194599819859885",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "High-dose corticosteroids started within 14 days achieve significant hearing recovery in 75%; salvage intratympanic injections restore hearing in 40% of non-responders."
            }
        }
    },
    {
        "id": "DOC-CARD-258",
        "icd10": "H47.01",
        "condition": "Anterior Ischemic Optic Neuropathy (AION)",
        "specialty": "Ophthalmology",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Cohort Consensus",
        "source_body": "American Academy of Ophthalmology (AAO) & Ophthalmology",
        "citation": "Hayreh SS. Ischemic optic neuropathy. Prog Retin Eye Res. 2009;28(1):34-62.",
        "doi_or_source": "10.1016/j.preteyeres.2008.11.002",
        "clinical_evidence": "Anterior Ischemic Optic Neuropathy (AION) is infarction of the optic nerve head supplied by the short posterior ciliary arteries, presenting as sudden, painless, unilateral vision loss accompanied by optic disc edema. It is critically bifurcated into: (1) Arteritic AION (A-AION, accounting for 10-15%), an ophthalmic emergency caused by Giant Cell Arteritis (GCA) in patients >=50 years, marked by high ESR (>50-100 mm/h) and elevated CRP; and (2) Non-Arteritic AION (NA-AION, 85-90%), driven by nocturnal arterial hypotension and microvascular hypoperfusion in structurally crowded optic discs ('disc-at-risk': small or absent optic cup). Visual field testing classically reveals an inferior altitudinal visual field defect. In A-AION, emergent high-dose IV methylprednisolone (1 g daily for 3 days) is mandatory to prevent fellow eye blindness (which occurs in up to 50% within days if untreated).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate ESR and CRP blood testing in all patients >=50; avoidance of nocturnal blood pressure overtreatment (avoid taking antihypertensives right before bedtime to prevent nocturnal hypotensive optic ischemia); CPAP for sleep apnea.",
            "monitoring_cadence": "Humphrey 24-2 visual field perimetry and optical coherence tomography (OCT) of the retinal nerve fiber layer (RNFL); temporal artery biopsy (minimum 2 cm specimen) within 1-2 weeks if arteritic form suspected.",
            "clinical_thresholds": "Suspected Arteritic AION with scalp tenderness, jaw claudication, or ESR >50 mm/h warrants immediate emergency IV methylprednisolone prior to waiting for temporal artery biopsy results."
        },
        "patient_plain_language": "Anterior ischemic optic neuropathy (AION) is often described as a 'stroke of the optic nerve'. The small blood vessels carrying oxygen to the optic nerve (the main visual cable transmitting images from your eye to your brain) suddenly become blocked. This causes sudden, painless loss of vision in one eye, typically leaving the lower or upper half of your vision completely dark.",
        "doctor_consultation_checklist": {
            "parameter_question": "Were my ESR and CRP inflammation markers checked immediately to rule out Giant Cell Arteritis (temporal arteritis)?",
            "safety_question": "Should I avoid taking my blood pressure medications right at bedtime to prevent my blood pressure from dipping too low while I sleep?",
            "action_threshold_question": "Do I have a 'crowded optic disc' in my other eye, and what steps should I take to protect my remaining good eye?"
        },
        "red_flags": [
            "Severe headache at the temples, pain when chewing food (jaw claudication), scalp tenderness when brushing hair, or sudden vision loss spreading to the other eye"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ischemic optic neuropathy is a loss of vision caused by damage to the optic nerve from poor blood flow.",
                "plain_analogy": "A blood clot or drop in water pressure cutting off blood flow to the optic nerve cable, turning off half the picture.",
                "lifestyle_action": "Emergency eye clinic exam immediately. Never take blood pressure pills right at bedtime. Treat sleep apnea."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Methylprednisolone IV", "Prednisone Oral", "Aspirin", "Tocilizumab (for Giant Cell Arteritis)"],
                "dosing_gdmt": "For Arteritic AION: Methylprednisolone 1g IV daily for 3 days, followed by oral Prednisone 1 mg/kg daily. NA-AION: Aspirin 81 mg daily.",
                "black_box_warning": "High-dose systemic steroids: Monitor for acute psychosis, acute peptic ulceration, and severe hyperglycemia.",
                "organ_clearance_cutoffs": "PDE5 inhibitors (sildenafil, tadalafil) carry an FDA warning for NA-AION; avoid in patients with prior NA-AION in one eye."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Hayreh Ischemic Optic Registry",
                "pmid_or_doi": "10.1016/j.preteyeres.2008.11.002",
                "cebm_level": 1,
                "sample_size": 1900,
                "endpoints": "Immediate IV steroids in Arteritic AION reduces fellow-eye blindness from 50% to <5%; NA-AION fellow eye involvement 15% at 5 years."
            }
        }
    },
    {
        "id": "DOC-CARD-259",
        "icd10": "H34.1",
        "condition": "Central Retinal Artery Occlusion (CRAO)",
        "specialty": "Ophthalmology",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA Scientific Statement & Systematic Review",
        "source_body": "Stroke (AHA Scientific Statement on CRAO) & Ophthalmology",
        "citation": "Biousse V et al. Management of Central Retinal Artery Occlusion: A Scientific Statement From the American Heart Association. Stroke. 2021;52(6):e282-e294.",
        "doi_or_source": "10.1161/STR.0000000000000366",
        "clinical_evidence": "Central Retinal Artery Occlusion (CRAO) is an acute ischemic stroke of the eye, characterized by sudden, painless, profound monocular vision loss (visual acuity counting fingers or worse in >90%). Fundoscopy reveals a pale, edematous retina with the classic 'cherry-red spot' at the fovea (where the thin foveal retina allows the underlying red choroid to shine through). The AHA scientific statement emphasizes that CRAO must be triaged as an acute ischemic stroke code; the retina suffers irreversible ischemic infarction within 240 minutes (4 hours) of complete occlusion. Over 70% of CRAO patients have concurrent high-grade ipsilateral carotid artery stenosis or cardioembolic sources. Emergency intravenous thrombolysis (IV alteplase 0.9 mg/kg) within 4.5 hours of symptom onset produces visual recovery in 37% vs 17% conventional conservative therapy (p=0.002).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency 911 activation and transport to a comprehensive stroke center; conservative bedside maneuvers (ocular massage with Goldman lens, rebreathing into a paper bag to induce hypercapnic vasodilation) while preparing thrombolysis; emergency anterior chamber paracentesis.",
            "monitoring_cadence": "Emergent non-contrast head CT and CT angiography (CTA) of head/neck vessels; continuous telemetry for atrial fibrillation; transthoracic/transesophageal echocardiogram (TTE/TEE); dilated retinal examination at 2-4 weeks to screen for iris neovascularization (neovascular glaucoma).",
            "clinical_thresholds": "Onset of visual loss <4.5 hours without contraindications warrants emergency evaluation for intravenous tissue plasminogen activator (IV alteplase) by the acute stroke neurology team."
        },
        "patient_plain_language": "Central retinal artery occlusion (CRAO) is an eye stroke. Just like an ischemic stroke in the brain, a small traveling blood clot gets stuck in the main artery supplying blood and oxygen to your retina (the visual film lining the back of your eye). This causes sudden, painless blindness in one eye, like a dark window shade pulling shut. It is a critical medical emergency requiring immediate emergency room stroke evaluation.",
        "doctor_consultation_checklist": {
            "parameter_question": "Am I within the 4.5-hour time window to receive emergency clot-busting medication (IV tPA / alteplase)?",
            "safety_question": "Did my emergency neck CT angiogram or carotid ultrasound show a severe blockage in my carotid artery?",
            "action_threshold_question": "What blood thinner and cholesterol medication do I need to start immediately to prevent a major brain stroke?"
        },
        "red_flags": [
            "Sudden painless loss of vision in one eye, sudden facial weakness, arm numbness, speech difficulty, or sudden loss of balance"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Central retinal artery occlusion is a blockage of the blood flow in the central retinal artery that carries oxygen to the retina, causing sudden blindness.",
                "plain_analogy": "A stroke of the eye: a blood clot plugging the main pipe that powers the eye's visual camera screen.",
                "lifestyle_action": "Call 911 immediately. Treat this as an acute stroke. Every minute counts to preserve retinal nerve tissue."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Alteplase IV (tPA)", "Aspirin", "Atorvastatin 80 mg", "Timolol Ophthalmic Drops", "Acetazolamide"],
                "dosing_gdmt": "Within 4.5 hours: IV Alteplase 0.9 mg/kg (max 90 mg; 10% bolus over 1 min, remaining 90% over 60 min). Secondary: High-intensity statin + Aspirin.",
                "black_box_warning": "Alteplase: Intracranial hemorrhage and fatal systemic bleeding; strict adherence to stroke thrombolysis exclusion criteria.",
                "organ_clearance_cutoffs": "Screen for neovascular glaucoma with panretinal photocoagulation (PRP) or anti-VEGF if ocular neovascularization develops."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHA CRAO Statement",
                "pmid_or_doi": "10.1161/STR.0000000000000366",
                "cebm_level": 1,
                "sample_size": 2600,
                "endpoints": "IV thrombolysis within 4.5 hours improves visual recovery rate from 17% to 37% (p=0.002); stroke workup identifies surgical carotid stenosis in >25%."
            }
        }
    },
    {
        "id": "DOC-CARD-260",
        "icd10": "H33.2",
        "condition": "Rhegmatogenous Retinal Detachment",
        "specialty": "Ophthalmology",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO Preferred Practice Pattern & Multicenter Trials",
        "source_body": "Ophthalmology (AAO Preferred Practice Pattern) & Cochrane",
        "citation": "Flaxel CJ et al. Retinal Detachment Preferred Practice Pattern. Ophthalmology. 2020;127(1):P146-P181.",
        "doi_or_source": "10.1016/j.ophtha.2019.09.048",
        "clinical_evidence": "Rhegmatogenous Retinal Detachment (RRD) is an ophthalmic surgical emergency occurring when a full-thickness retinal tear or break (rhegma), most commonly triggered by posterior vitreous detachment (PVD) or lattice degeneration in myopic eyes, allows liquefied vitreous fluid to dissect into the subretinal space, separating the neurosensory retina from the underlying retinal pigment epithelium (RPE). Cardinal premonitory symptoms include sudden photopsia (flashes of light), sudden shower of black floaters, and a progressive dark peripheral curtain/shadow advancing toward the central vision. In the primary repair of uncomplicated RRD, surgical reattachment via pars plana vitrectomy (PPV) or scleral buckle achieves primary anatomic reattachment in >85-90% of cases and final attachment in >95%. Preserving visual acuity depends critically on whether the macula is still attached ('macula-on' status).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency same-day ophthalmologic referral; head positioning (postural positioning to let gravity prevent fluid from peeling the macula); strict avoidance of vigorous head movement, bending over, or heavy lifting.",
            "monitoring_cadence": "Post-operative retinal examination at day 1, week 1, month 1, and month 3; intraocular pressure monitoring; visual field tracking.",
            "clinical_thresholds": "A 'macula-on' retinal detachment is an absolute surgical emergency requiring operative intervention within 24-48 hours to preserve sharp central 20/20 reading vision."
        },
        "patient_plain_language": "A retinal detachment occurs when the thin, light-sensitive tissue at the back of your eye (the retina) peels away from its normal position and blood supply, like wallpaper peeling off a damp wall. It often begins with sudden bursts of flashing lights and a shower of dark floating specks, followed by a dark shadow or curtain spreading across your field of vision. Prompt surgical repair is needed to prevent permanent blindness.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is my macula (the center of reading vision) still attached ('macula-on') or has it detached?",
            "safety_question": "Which surgical repair—a pneumatic gas bubble, a scleral buckle silicone band, or a vitrectomy—is recommended for my specific tear?",
            "action_threshold_question": "What exact head positioning (such as face-down positioning) must I maintain after surgery to keep the gas bubble pressing against the tear?"
        },
        "red_flags": [
            "A dark shadow or black curtain spreading across your peripheral vision toward the center, sudden burst of bright flashes of light, or sudden shower of dozens of dark floaters"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Retinal detachment is a medical emergency where the retina at the back of the eye pulls away from the layer of blood vessels that provides it with oxygen and nourishment.",
                "plain_analogy": "Wallpaper peeling away from the wall; if fluid gets underneath, the entire sheet peels down until re-glued by a surgeon.",
                "lifestyle_action": "Do not rub your eye. Avoid bending over or heavy lifting. See a retinal eye surgeon on the exact same day."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Sulfur Hexafluoride (SF6) Gas", "Perfluoropropane (C3F8) Gas", "Silicone Oil", "Prednisolone Acetate Drops"],
                "dosing_gdmt": "Surgical repair: Pars plana vitrectomy (PPV) with internal fluid-gas exchange (C3F8 or SF6) and laser retinopexy. Post-op Prednisolone drops QID.",
                "black_box_warning": "Intraocular Gas: Absolute contraindication to air travel or nitrous oxide anesthesia while gas bubble is inside the eye (causes explosive IOP increase).",
                "organ_clearance_cutoffs": "Patients with intraocular gas bubbles must wear a warning bracelet until the bubble is fully reabsorbed (2-8 weeks)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO Retinal Detachment PPP",
                "pmid_or_doi": "10.1016/j.ophtha.2019.09.048",
                "cebm_level": 1,
                "sample_size": 5100,
                "endpoints": "Primary anatomic reattachment achieved in >90%; macula-on detachment surgery within 24-48 hours preserves 20/40 or better vision in >85%."
            }
        }
    }
]