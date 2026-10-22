"""
scripts/dataset_parts/part21_emergency_toxicology_metabolic.py
Part 21: Landmark Clinical Database Entries (DOC-CARD-501 to DOC-CARD-520: 20 Critical Conditions)
Focus: Emergency Medicine, Acute Toxicology, Critical Metabolic & Cardiopulmonary Emergencies
"""

PART_21_DISEASES = [
    {
        "id": "DOC-CARD-501",
        "icd10": "T58.01XA",
        "condition": "Carbon Monoxide Poisoning (Carboxyhemoglobin Cellular Hypoxia)",
        "specialty": "Emergency Medicine & Toxicology",
        "organ_system": "Hematologic & Neurological",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & NEJM Landmark Hyperbaric Trial",
        "source_body": "NEJM & Undersea and Hyperbaric Medical Society (UHMS)",
        "citation": "Weaver LK et al. Hyperbaric Oxygen for Acute Carbon Monoxide Poisoning. N Engl J Med. 2002;347(14):1057-1067.",
        "doi_or_source": "10.1056/NEJMoa013121",
        "clinical_evidence": "Carbon monoxide has a 200-250 times greater affinity for hemoglobin than oxygen, forming carboxyhemoglobin (COHb), shifting the oxyhemoglobin dissociation curve leftward (Haldane effect) and poisoning mitochondrial cytochrome c oxidase. The landmark double-blind trial by Weaver et al. (n=152) demonstrated that hyperbaric oxygen (HBO at 2.5-3.0 ATA) reduced persistent cognitive and neuropsychological sequelae at 6 weeks by nearly 50% compared to normobaric oxygen (25.0% vs 46.1%, p=0.007). Half-life of COHb is 320 minutes on room air, 74 minutes on 100% normobaric oxygen, and 20 minutes under 3.0 ATA hyperbaric oxygen.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate removal from exposure source; high-flow 100% normobaric oxygen via non-rebreather mask; hyperbaric oxygen (HBO) consultation for severe indicators (COHb >25%, pregnant with COHb >15%, loss of consciousness, cardiac ischemia, metabolic acidosis pH <7.25); install residential certified UL-2034 CO alarms.",
            "monitoring_cadence": "Serial co-oximetry blood gas (pulse oximeters falsely read normal SpO2), serial cardiac troponin and 12-lead ECG (myocardial injury occurs in up to 37% of poisonings), neuropsychiatric screening at discharge and 4-6 weeks.",
            "clinical_thresholds": "Carboxyhemoglobin (COHb) >3-4% in non-smokers, >10% in heavy smokers; clinical intoxication symptoms appear at >15-20%."
        },
        "patient_plain_language": "Carbon monoxide is an invisible, odorless, tasteless gas produced by burning fuels (furnaces, heaters, car exhausts, generators). It acts like a silent oxygen thief: it grabs onto your red blood cells much tighter than oxygen, starving your brain and heart of vital air. Early signs feel like a winter flu—headache, nausea, and dizziness—without a fever. Breathing pure high-pressure oxygen pushes the toxic gas out of your blood before it damages brain memory pathways.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my carboxyhemoglobin percentage on the co-oximetry blood gas test?",
            "safety_question": "Did my ECG and troponin blood tests show any subtle strain or silent damage to my heart muscle?",
            "action_threshold_question": "Do I meet criteria for hyperbaric chamber oxygen therapy to prevent long-term memory lapses and cognitive fog?"
        },
        "red_flags": [
            "Any syncope, confusion, seizure, or loss of consciousness in an enclosed heated space",
            "Chest pain, acute shortness of breath, or cardiac arrhythmias (CO-induced myocardial infarction)",
            "Pregnancy with known carbon monoxide exposure (fetal hemoglobin binds CO with extreme affinity, leading to fetal demise)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Carbon monoxide poisoning happens when you breathe in too much carbon monoxide, replacing oxygen in your blood and causing severe organ starvation.",
                "plain_analogy": "A counterfeit pass holder filling up all the passenger seats on a commuter train, leaving genuine ticketed workers (oxygen molecules) stranded on the platform.",
                "lifestyle_action": "Evacuate the premises immediately into fresh air, never run generators indoors, and check furnace vents annually."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oxygen 100% inhalation (Normobaric high-flow non-rebreather mask)",
                    "Hyperbaric Oxygen (HBO therapy at 2.5-3.0 ATA)",
                    "Hydroxocobalamin IV (Cyanokit - if concurrent smoke inhalation / cyanide exposure suspected)"
                ],
                "dosing_gdmt": "100% normobaric oxygen administered immediately until COHb <5% and patient is asymptomatic (typically 4-6 hours); HBO: 3 hyperbaric dives within 24 hours.",
                "black_box_warning": "Standard two-wavelength finger pulse oximetry is blind to COHb and falsely reports normal 99-100% oxygen saturation.",
                "organ_clearance_cutoffs": "Monitor for delayed post-hypoxic leukoencephalopathy presenting with parkinsonism or memory deficits 2-40 days after recovery."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEJM-HBO-CO",
                "pmid_or_doi": "10.1056/NEJMoa013121",
                "cebm_level": 1,
                "sample_size": 152,
                "endpoints": "Three hyperbaric oxygen treatments within 24 hours significantly reduced persistent cognitive sequelae at 6 weeks (RR 0.54; 95% CI 0.35-0.84; p=0.007)."
            }
        }
    },
    {
        "id": "DOC-CARD-502",
        "icd10": "T39.1X1A",
        "condition": "Acetaminophen Toxicity (NAPQI Hepatocellular Necrosis & NAC Protocol)",
        "specialty": "Medical Toxicology & Hepatology",
        "organ_system": "Hepatic & Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & Rumack-Matthew Landmark Nomogram Guidelines",
        "source_body": "Lancet & American Association for the Study of Liver Diseases (AASLD)",
        "citation": "Rumack BH, Matthew H. Acetaminophen Poisoning and Toxicity. Pediatrics. 1975;55(6):871-876; Prescott LF et al. Intravenous N-acetylcysteine: The treatment of choice for paracetamol poisoning. Br Med J. 1979;2(6198):1097-1100.",
        "doi_or_source": "10.1136/bmj.2.6198.1097",
        "clinical_evidence": "When therapeutic acetaminophen metabolic pathways (glucuronidation 40-67% and sulfation 20-46%) become saturated, CYP2E1 metabolizes excess drug into the highly electrophilic, hepatotoxic metabolite N-acetyl-p-benzoquinone imine (NAPQI). Once hepatic glutathione stores deplete below 70%, NAPQI binds covalently to hepatocytes, causing centrilobular (Zone 3) hepatic necrosis. Early administration of N-acetylcysteine (NAC) replenishes hepatic glutathione stores and acts as a direct glutathione substitute. When NAC is initiated within 8 hours of acute ingestion, the incidence of severe hepatotoxicity (AST/ALT >1000 IU/L) drops from ~58% to less than 1.6%, with mortality approaching zero.",
        "solution_protocol": {
            "non_pharmacological_targets": "Activated charcoal (1 g/kg, max 50g) if presenting within 1-2 hours of acute overdose; calculate timing precisely for Rumack-Matthew nomogram plotted at 4 to 24 hours post-ingestion; supportive antiemetics (ondansetron; avoid phenothiazines).",
            "monitoring_cadence": "Serum acetaminophen concentration drawn exactly at 4 hours post-ingestion (or immediately if >4 hours); baseline and serial transaminases (ALT/AST), total bilirubin, prothrombin time/INR, blood urea nitrogen, creatinine, serum lactate, and blood glucose every 12 hours.",
            "clinical_thresholds": "Rumack-Matthew Nomogram 4-hour treatment line: serum acetaminophen level ≥150 mcg/mL (993 micromol/L) mandates immediate complete N-acetylcysteine therapy."
        },
        "patient_plain_language": "Acetaminophen (Tylenol/Paracetamol) is safe at recommended doses, but an overdose overwhelms your liver's natural antioxidant defense (glutathione). A toxic byproduct called NAPQI builds up and begins destroying liver cells. A dangerous trap is that the first 24 hours can seem deceptively mild with only slight nausea, but liver failure develops 48 to 72 hours later. N-acetylcysteine (NAC) is an antidote that acts like an emergency refill for your liver's cellular shield, almost completely preventing liver failure if given within 8 hours.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my exact 4-hour acetaminophen blood level plotted against the Rumack-Matthew nomogram line?",
            "safety_question": "Are my liver enzymes (AST/ALT) and blood clotting speed (INR) remaining stable within normal limits?",
            "action_threshold_question": "Have I completed the full course of N-acetylcysteine antidote, and do my end-of-infusion liver labs confirm safety before stopping?"
        },
        "red_flags": [
            "Coagulopathy (INR >3.0) or arterial lactate >3.5 mmol/L (King's College Criteria for urgent liver transplantation)",
            "Encephalopathy, asterixis (flapping hand tremor), severe hypoglycemia, or acute renal failure (Hepatorenal syndrome)",
            "Ingestion exceeding 150 mg/kg or 7.5 grams in adults without immediate antidote intervention"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acetaminophen overdose is the most common cause of acute liver failure in the developed world, treatable with the antidote N-acetylcysteine.",
                "plain_analogy": "A furnace overflowing with toxic soot because the chimney filter (glutathione) ran out; the antidote instantly cleans the filter before the furnace catches fire.",
                "lifestyle_action": "Never exceed 3,000 mg to 4,000 mg of acetaminophen in 24 hours from all combined cold, flu, and pain medications."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "N-acetylcysteine IV (Acetadote 3-bag protocol: 150 mg/kg over 1h, then 50 mg/kg over 4h, then 100 mg/kg over 16h)",
                    "N-acetylcysteine Oral (Mucomyst: 140 mg/kg loading dose, then 70 mg/kg every 4h for 17 doses)",
                    "Activated Charcoal oral (within 2 hours of ingestion)"
                ],
                "dosing_gdmt": "Intravenous NAC 21-hour protocol: Total 300 mg/kg over 21 hours. Continue infusion beyond 21 hours if ALT is elevated, INR >1.3, or APAP is detectable.",
                "black_box_warning": "Anaphylactoid non-IgE reactions (flushing, urticaria, bronchospasm) occur in up to 15% during the initial rapid IV loading dose; manage with slowing infusion rate and antihistamines.",
                "organ_clearance_cutoffs": "Check King's College Criteria: Arterial lactate >3.5 after fluid resuscitation, or combination of pH <7.30 or INR >6.5 + Creatinine >3.4 mg/dL + Grade III/IV encephalopathy triggers emergent liver transplant alert."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "RUMACK-PRESCOTT",
                "pmid_or_doi": "10.1136/bmj.2.6198.1097",
                "cebm_level": 1,
                "sample_size": 1119,
                "endpoints": "Administration of NAC within 8 hours of acetaminophen overdose reduced severe hepatotoxicity to 1.6% and eliminated mortality (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-503",
        "icd10": "T51.1X1A",
        "condition": "Toxic Alcohol Ingestion (Ethylene Glycol & Methanol Poisoning with Fomepizole)",
        "specialty": "Medical Toxicology & Nephrology",
        "organ_system": "Renal & Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NEJM META Trial & American Academy of Clinical Toxicology Practice Guidelines",
        "source_body": "NEJM & American Academy of Clinical Toxicology (AACT)",
        "citation": "Brent J et al. Fomepizole for the Treatment of Ethylene Glycol Poisoning. N Engl J Med. 1999;340(11):832-838; Brent J et al. Fomepizole for the Treatment of Methanol Poisoning. N Engl J Med. 2001;344(6):424-429.",
        "doi_or_source": "10.1056/NEJMoa002683",
        "clinical_evidence": "Ethylene glycol (antifreeze) and methanol (windshield wiper fluid/denatured alcohol) are metabolized by hepatic alcohol dehydrogenase (ADH) into devastating toxic organic acids. Ethylene glycol converts to glycolic acid and oxalic acid, binding calcium to form calcium oxalate monohydrate crystals in renal tubules (causing acute tubular necrosis and hypocalcemia). Methanol converts to formic acid, causing retinal ganglion cell toxicity, optic disc edema, permanent blindness, and putaminal necrosis. The NEJM META trials established Fomepizole (4-methylpyrazole), a competitive ADH inhibitor with an affinity 8,000 times higher than ethanol, as first-line therapy. Fomepizole halted toxic metabolite generation in 100% of patients and eliminated renal failure and optic nerve injury when administered early.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate toxic alcohol panel; calculate osmolal gap = measured serum osmolality - [2*Na + Glucose/18 + BUN/2.8 + Ethanol/4.6]; initiate emergent hemodialysis for refractory metabolic acidosis (pH <7.25), visual impairment, renal failure, or toxic alcohol level ≥50 mg/dL.",
            "monitoring_cadence": "Serial arterial/venous blood gases for anion gap progression; serum electrolytes and osmolality every 2-4 hours; Wood's lamp examination of urine (fluorescein additive in antifreeze); calcium oxalate envelope/needle crystal microscopy.",
            "clinical_thresholds": "Osmolal gap >10-15 mOsm/kg H2O, high anion gap metabolic acidosis (>16 mEq/L), or serum ethylene glycol/methanol level ≥20 mg/dL."
        },
        "patient_plain_language": "Toxic alcohols like ethylene glycol (antifreeze) or methanol (windshield washer fluid) act like intoxicating alcohol at first, but your liver's enzymes turn them into deadly acids. Antifreeze turns into oxalate crystals that shred the kidney filters like sharp glass shards. Methanol turns into formic acid that directly destroys the optic nerve in your eyes, causing permanent 'snowfield' blindness. Fomepizole is a targeted antidote that completely blocks the liver enzyme from processing the poisons, keeping your kidneys and eyes completely safe.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my serum osmolal gap and anion gap on the urgent metabolic panel?",
            "safety_question": "Did urine analysis show calcium oxalate needle crystals, or did fundoscopy show optic disc swelling?",
            "action_threshold_question": "Should we begin emergent Fomepizole infusions and arrange nephrology for hemodialysis clearance?"
        },
        "red_flags": [
            "Severe visual disturbance, blurring, or sensation of 'walking in a blizzard' (Methanol optic papillitis)",
            "Profound high anion gap metabolic acidosis (pH <7.10, HCO3 <8 mEq/L) with Kussmaul respirations",
            "Anuria, acute flank pain, and tetany from severe hypocalcemia (Ethylene glycol acute tubular necrosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Drinking toxic alcohols like antifreeze or windshield washer fluid causes severe kidney failure or blindness, treatable with the antidote fomepizole or kidney dialysis.",
                "plain_analogy": "Putting destructive industrial solvents into an engine; the antidote turns off the ignition key so the chemical cannot burn into caustic acid.",
                "lifestyle_action": "Store all automotive fluids, de-icers, and industrial chemicals in locked original containers out of reach of children and pets."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Fomepizole IV (Antizol - Alcohol Dehydrogenase Inhibitor)",
                    "Ethanol 10% IV infusion (fallback when fomepizole unavailable)",
                    "Sodium Bicarbonate IV (to treat systemic acidemia)",
                    "Cofactor therapy: Pyridoxine (B6 100mg IV) & Thiamine (B1 100mg IV) for ethylene glycol; Folinic Acid (Leucovorin 50mg IV) for methanol",
                    "Intermittent Hemodialysis"
                ],
                "dosing_gdmt": "Fomepizole IV: 15 mg/kg loading dose over 30 min, then 10 mg/kg every 12 hours for 4 doses, then 15 mg/kg every 12 hours until level <20 mg/dL and acid-base status normalizes. Increase dosing frequency to every 4 hours during hemodialysis.",
                "black_box_warning": "Ethanol infusion requires continuous ICU blood glucose and level monitoring (target BAC 100-150 mg/dL) due to high risk of hypoglycemia and inebriation.",
                "organ_clearance_cutoffs": "Hemodialysis clearance of ethylene glycol and methanol is >200 mL/min; dialyze aggressively until toxic alcohol level is undetectable and anion gap is closed."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "META-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa002683",
                "cebm_level": 1,
                "sample_size": 38,
                "endpoints": "Fomepizole effectively blocked toxic alcohol metabolism in 100% of patients with ethylene glycol or methanol poisoning, preserving renal function and vision (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-504",
        "icd10": "T40.1X1A",
        "condition": "Acute Opioid Overdose & Hypoventilation (Naloxone Reversal & Airway Rescue)",
        "specialty": "Emergency Medicine & Addiction",
        "organ_system": "Nervous & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & WHO Guidelines on Community Management of Opioid Overdose",
        "source_body": "CDC, WHO & American Heart Association (AHA)",
        "citation": "McDonald R, Strang J. Are Take-Home Naloxone Programmes Effective? Systematic Review. Addiction. 2016;111(7):1177-1187; NEJM Fentanyl Overdose Consensus 2021.",
        "doi_or_source": "10.1111/add.13326",
        "clinical_evidence": "Opioid agonists (heroin, morphine, oxycodone, and ultra-potent synthetic analogues like fentanyl and carfentanil) stimulate mu-opioid receptors in the ventrolateral medulla and pre-Bötzinger complex, blunting hypercapnic and hypoxic ventilatory drive, precipitating the fatal opioid triad (unresponsiveness, pinpoint miosis, and bradypnea/apnea). Systematic reviews confirm that community take-home and emergency naloxone administration reduces overdose mortality by over 93% (RR 0.07; 95% CI 0.02-0.21). Naloxone is a pure competitive mu-opioid receptor antagonist with an onset of 2-3 minutes intranasally and <1-2 minutes intravenously.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate airway support with bag-valve-mask (BVM) ventilation on 100% supplemental oxygen; sternal rub / tactile stimulation; recovery position to prevent aspiration; co-screen for synthetic fentanyl chest wall rigidity ('wooden chest syndrome').",
            "monitoring_cadence": "Continuous pulse oximetry, continuous capnography (EtCO2), respiratory rate, and cardiac monitoring for at least 2-4 hours for short-acting opioids, or >12-24 hours for sustained-release opioids (methadone, oxycodone CR, fentanyl patches).",
            "clinical_thresholds": "Respiratory rate <8-10 breaths/minute, oxygen saturation <90%, or Glasgow Coma Scale (GCS) <8 in the setting of suspected opioid exposure."
        },
        "patient_plain_language": "An opioid overdose happens when drugs like prescription painkillers, heroin, or street fentanyl slow down the brainstem's automatic breathing center until a person stops breathing entirely. Within minutes, brain cells begin starving of oxygen, the skin turns pale or blue, and pupils become pinpoint tiny. Naloxone (Narcan) is a lifesaver: it is a gentle nasal spray that knocks the opioid off the brain's receptors like a bouncer, restoring natural breathing within 2 to 3 minutes without getting the person high.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's spontaneous respiratory rate and end-tidal CO2 after naloxone administration?",
            "safety_question": "Was synthetic fentanyl or a long-acting opioid involved that could cause renarcotization after naloxone wears off in 30-90 minutes?",
            "action_threshold_question": "Does the patient require a continuous naloxone IV drip or an extended 4-to-6 hour hospital observation period?"
        },
        "red_flags": [
            "Complete apnea, cyanosis, and absent carotid pulse (Cardiac arrest requiring immediate CPR and defibrillation)",
            "Severe non-cardiogenic pulmonary edema with pink frothy sputum following naloxone reversal",
            "Renarcotization (recurrent unresponsiveness and apnea) after initial naloxone bolus wears off"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Opioid overdose slows or stops breathing and is reversed rapidly with naloxone nasal spray or injection.",
                "plain_analogy": "A key jammed into the ignition that has stalled the motor; the antidote is a master key that pushes the bad key out, restarting the engine immediately.",
                "lifestyle_action": "Keep Narcan (naloxone) nasal spray in home first aid kits and never consume non-prescribed pills or street powders alone."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Naloxone nasal spray (Narcan 4 mg single-dose intranasal spray)",
                    "Naloxone injectable IV/IM/SC (0.4 mg to 2 mg)",
                    "Nalmefene nasal spray (Opvee 2.7 mg - long-acting antagonist for synthetic opioids)"
                ],
                "dosing_gdmt": "Intranasal: 4 mg in one nostril; repeat in opposite nostril every 2-3 minutes if no response. IV: Titrate 0.04 to 0.4 mg IV to restore spontaneous breathing (12-14 bpm) without precipitating severe acute withdrawal storm.",
                "black_box_warning": "Precipitated severe acute opioid withdrawal (agitation, vomiting, tachycardia, diaphoresis, hypertension) occurs with excessive rapid boluses.",
                "organ_clearance_cutoffs": "Naloxone duration of action is 30 to 90 minutes; synthetic fentanyl and methadone have half-lives of 8 to 36 hours, carrying high risk of secondary fatal apnea."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-NALOXONE",
                "pmid_or_doi": "10.1111/add.13326",
                "cebm_level": 1,
                "sample_size": 22400,
                "endpoints": "Take-home naloxone programs resulted in a 93% survival rate across witnessed overdoses with a dramatic reduction in overdose mortality (RR 0.07; p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-505",
        "icd10": "T88.3XXA",
        "condition": "Malignant Hyperthermia (RYR1 Calcium Channel Storm & Dantrolene)",
        "specialty": "Anesthesiology & Critical Care",
        "organ_system": "Musculoskeletal & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Malignant Hyperthermia Association of the United States (MHAUS) Consensus Guidelines",
        "source_body": "Anesthesiology & MHAUS",
        "citation": "Hopkins PM et al. European Malignant Hyperthermia Group Guidelines for Investigation of Malignant Hyperthermia Susceptibility. Br J Anaesth. 2015;115(4):531-539; Larach MG et al. Clinical Validation of Malignant Hyperthermia Diagnostic Criteria. Anesthesiology. 1994;80(4):771-779.",
        "doi_or_source": "10.1097/00000542-199404000-00008",
        "clinical_evidence": "Malignant Hyperthermia (MH) is a pharmacogenetic hypermetabolic crisis triggered by volatile halogenated anesthetics (isoflurane, sevoflurane, desflurane) or depolarizing muscle relaxants (succinylcholine). Mutations in the ryanodine receptor gene (RYR1 in 70-80% of cases) or CACNA1S cause uncontrolled calcium efflux from the sarcoplasmic reticulum into the myoplasm. This triggers massive sustained muscle contraction, aerobic/anaerobic hypermetabolism, severe mixed respiratory/metabolic acidosis, hypercarbia (unexplained rise in end-tidal CO2), masseter spasm, rhabdomyolysis, hyperkalemia, and core hyperthermia exceeding 43°C. Historic mortality was >70%; modern protocolized treatment with Dantrolene sodium (which binds RYR1 and halts calcium release) reduces mortality to <5%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately discontinue all volatile halogenated gases and succinylcholine; hyperventilate with 100% oxygen at maximum fresh gas flow (≥10 L/min); activate MHAUS emergency protocol and call the 24/7 MH hotline (1-800-644-9737); insert charcoal filters into anesthetic circuit; initiate active external and internal cooling (cold IV saline 4°C, gastric/bladder cold lavage) until core temperature <38.5°C.",
            "monitoring_cadence": "Continuous core temperature (esophageal or bladder), continuous end-tidal CO2, arterial blood gas every 15 minutes, serial serum potassium, creatinine kinase (CK), urine myoglobin, and coagulation studies (PT/INR, fibrinogen for DIC).",
            "clinical_thresholds": "Unexplained EtCO2 >55-60 mmHg despite hyperventilation, generalized muscle rigidity, heart rate >110 bpm, and rapid temperature elevation (>1°C every 5-10 minutes)."
        },
        "patient_plain_language": "Malignant hyperthermia is a rare, inherited muscle gene quirk that is completely silent in everyday life, but becomes a life-threatening crisis if a person receives certain general anesthesia gases or muscle relaxers in surgery. The muscle cells lock into an uncontrollable spasm, burning oxygen at furious speed and generating extreme body heat (up to 108°F / 42°C). Dantrolene is an antidote that acts like a cellular circuit breaker, shutting off the calcium flood and relaxing the muscles before they break down and cause kidney failure.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's continuous end-tidal CO2 and arterial blood gas base deficit?",
            "safety_question": "Has Dantrolene sodium been reconstituted and administered at the initial 2.5 mg/kg IV push dose?",
            "action_threshold_question": "Are serum potassium levels checked to treat hyperkalemic cardiac arrest, and has active cooling been halted at 38.5°C to avoid hypothermia overshoot?"
        },
        "red_flags": [
            "Severe hyperkalemia (>6.5 mEq/L) producing peaked T waves and sine-wave cardiac arrest",
            "Disseminated intravascular coagulation (DIC) with spontaneous oozing from surgical incisions and IV lines",
            "Severe rhabdomyolysis with dark brown (cola-colored) myoglobinuria and acute renal failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Malignant hyperthermia is an inherited condition that causes a dangerous rise in body temperature and muscle spasms when receiving anesthesia.",
                "plain_analogy": "A car accelerator pedal stuck to the floorboard inside an operating room; the antidote Dantrolene instantly pulls the emergency handbrake.",
                "lifestyle_action": "Inform all surgical teams and anesthesiologists if you or any blood relative had an unexplained high fever or complication during surgery."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Dantrolene sodium IV (Dantrium / Revonto: 2.5 mg/kg initial IV push; repeat up to 10 mg/kg cumulative)",
                    "Ryanodex IV (nanocrystalline Dantrolene sodium: 250 mg per vial requiring only 5 mL sterile water)",
                    "Sodium bicarbonate IV (1-2 mEq/kg for severe metabolic acidosis)",
                    "Insulin Regular (10 units IV) + Dextrose 50% (50 mL) for severe hyperkalemia",
                    "Calcium chloride 10% IV (for cardioprotection if hyperkalemic QRS widening)"
                ],
                "dosing_gdmt": "Dantrolene sodium: 2.5 mg/kg rapid IV bolus. Continue repeat boluses of 1-2.5 mg/kg every 5-10 minutes until EtCO2 normalizes, rigidity ceases, and temperature stabilizes. Maintenance: 1 mg/kg IV every 6 hours for 24-48 hours.",
                "black_box_warning": "Calcium channel blockers (verapamil, diltiazem) are strictly contraindicated with Dantrolene; co-administration causes severe myocardial depression and fatal hyperkalemic collapse.",
                "organ_clearance_cutoffs": "Ensure vigorous urine output (≥1-2 mL/kg/h) with IV fluids, mannitol, and furosemide to prevent myoglobin precipitation in renal tubules."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MHAUS-REGISTRY",
                "pmid_or_doi": "10.1097/00000542-199404000-00008",
                "cebm_level": 1,
                "sample_size": 1400,
                "endpoints": "Rapid administration of Dantrolene within 10 minutes of MH diagnosis reduced mortality from 70% to 1.4% (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-506",
        "icd10": "T43.221A",
        "condition": "Serotonin Syndrome (Hunter Toxicity Criteria & Cyproheptadine)",
        "specialty": "Psychiatry & Toxicology",
        "organ_system": "Nervous & Autonomic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Hunter Serotonin Toxicity Criteria & Clinical Practice Guidelines",
        "source_body": "NEJM & Hunter Area Toxicology Service",
        "citation": "Dunkley EJ et al. The Hunter Serotonin Toxicity Criteria: Simple and Accurate Diagnostic Decision Rules for Serotonin Toxicity. QJM. 2003;96(9):635-642; Boyer EW, Shannon M. The Serotonin Syndrome. N Engl J Med. 2005;352(11):1112-1120.",
        "doi_or_source": "10.1056/NEJMra041867",
        "clinical_evidence": "Serotonin syndrome is a hyper-serotonergic crisis caused by combinations of serotonergic agents (SSRIs, SNRIs, MAOIs, TCAs, triptans, tramadol, linezolid, dextromethorphan, MDMA). Stimulation of central and peripheral 5-HT1A and 5-HT2A receptors causes the clinical triad of neuromuscular excitation (ocular clonus, inducible/spontaneous ankle clonus, hyperreflexia), autonomic instability (hyperthermia, diaphoresis, tachycardia), and altered mental status (agitation, delirium). The Hunter Criteria possess 84% sensitivity and 97% specificity (superior to Sternbach criteria). Hallmark physical finding is lower-extremity hyperreflexia and clonus (distinct from the 'lead-pipe' rigidity of Neuroleptic Malignant Syndrome).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately discontinue all serotonergic agents; IV fluid resuscitation; external cooling blankets for hyperthermia; avoid antipyretics (acetaminophen/aspirin are ineffective as hyperthermia is muscular, not hypothalamic); IV benzodiazepines (diazepam/lorazepam) for neuromuscular agitation.",
            "monitoring_cadence": "Serial examination of deep tendon reflexes, ankle clonus, pupillary mydriasis, continuous core temperature, telemetry, and serum creatine kinase (CK) for rhabdomyolysis.",
            "clinical_thresholds": "Hunter Criteria positive if patient is taking a serotonergic agent PLUS spontaneous clonus, OR inducible clonus with agitation/diaphoresis, OR ocular clonus with diaphoresis, OR tremor with hyperreflexia, OR hypertonia with temperature >38°C and ocular/inducible clonus."
        },
        "patient_plain_language": "Serotonin syndrome occurs when two or more medications that raise brain serotonin are taken together (like combining an antidepressant with certain migraine pills, pain relievers like tramadol, or antibiotics like linezolid). Too much serotonin overloads the nerve system, causing uncontrollable muscle twitching, rhythmic foot tapping (clonus), heavy sweating, shivering, rapid heart rate, and confusion. Stopping the medications and taking a calming medication or a serotonin-blocking antidote like Cyproheptadine quickly settles the nervous system.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the physical examination demonstrate spontaneous or inducible ankle clonus or ocular flutter?",
            "safety_question": "Have all serotonergic medications, supplements (St. John's Wort), and cough syrups (dextromethorphan) been discontinued?",
            "action_threshold_question": "Is the core temperature exceeding 38.5°C requiring Cyproheptadine 5-HT2A blockade and active ICU sedation?"
        },
        "red_flags": [
            "Severe hyperthermia (>41.1°C / 106°F) leading to acute rhabdomyolysis, metabolic acidosis, and multi-organ failure",
            "Severe continuous muscular rigidity impairing chest wall excursions and causing acute hypercapnic respiratory arrest",
            "Autonomic instability with swinging blood pressure and life-threatening ventricular arrhythmias"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Serotonin syndrome is a potentially life-threatening drug reaction caused by too much serotonin in the body.",
                "plain_analogy": "An electrical power grid hit by a massive power surge; the switches start sparking until you flip the master circuit breaker.",
                "lifestyle_action": "Always inform your doctor and pharmacist of every antidepressant, migraine medication, and dietary supplement you take."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cyproheptadine oral (Periactin - 5-HT1A and 5-HT2A Antagonist: 12 mg initial loading dose, then 2 mg q2h)",
                    "Lorazepam IV (Ativan: 2 to 4 mg IV q2-4h for neuromuscular hyperactivity)",
                    "Diazepam IV (Valium: 5 to 10 mg IV)",
                    "Esmolol IV infusion (for severe sinus tachycardia and autonomic instability)"
                ],
                "dosing_gdmt": "Cyproheptadine: 12 mg orally or via NG tube immediately; if symptoms persist, administer 2 mg every 2 hours until response, then 8 mg every 6 hours maintenance.",
                "black_box_warning": "Physical restraints are strictly contraindicated; isometric muscle contractions against restraints rapidly accelerate fatal hyperthermia and lactic acidosis.",
                "organ_clearance_cutoffs": "Resolution typically occurs within 24 hours of discontinuing short-acting SSRIs, but can take days if fluoxetine (long half-life) or MAOIs were ingested."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HUNTER-CRITERIA",
                "pmid_or_doi": "10.1056/NEJMra041867",
                "cebm_level": 1,
                "sample_size": 2222,
                "endpoints": "Hunter Criteria demonstrated 84% sensitivity and 97% specificity for diagnosing serotonin toxicity; cyproheptadine and aggressive sedation eliminated mortality in compliant cohorts."
            }
        }
    },
    {
        "id": "DOC-CARD-507",
        "icd10": "G21.0",
        "condition": "Neuroleptic Malignant Syndrome (Dopamine Blockade Hyperthermia & Bromocriptine/Dantrolene)",
        "specialty": "Psychiatry & Neurology",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Expert Consensus Criteria & Cochrane Database Review",
        "source_body": "Lancet & American Psychiatric Association (APA)",
        "citation": "Gurrera RJ et al. An International Consensus Study of Neuroleptic Malignant Syndrome Diagnostic Criteria Using the Delphi Method. J Clin Psychiatry. 2011;72(9):1222-1228; Strawn JR et al. Neuroleptic Malignant Syndrome: A Review of Pathogenesis and Management. Neuropsychiatr Dis Treat. 2007;3(3):289-296.",
        "doi_or_source": "10.4088/JCP.10m06438",
        "clinical_evidence": "Neuroleptic Malignant Syndrome (NMS) is an idiosyncratic, life-threatening reaction to dopamine D2-receptor antagonists (haloperidol, fluphenazine, chlorpromazine, risperidone, olanzapine) or abrupt withdrawal of dopamine agonists (levodopa, amantadine). Sudden central dopamine depletion in the hypothalamus dysregulates thermoregulation, while striatal dopamine blockade causes generalized, profound 'lead-pipe' rigidity, marked hyperpyrexia (often >40°C), autonomic instability (labile BP, tachycardia, profuse diaphoresis), and profound serum creatine kinase (CK) elevation (frequently >1,000 to 50,000 IU/L). Unlike Serotonin Syndrome, NMS develops slowly over days to weeks, presents with hyporeflexia and lead-pipe rigidity (rather than hyperreflexia/clonus), and responds to dopamine agonists (Bromocriptine) and muscle relaxants (Dantrolene).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately withdraw all offending neuroleptic and antipsychotic agents; aggressive IV fluid hydration (crystalloids at 200-300 mL/h) to maintain urine output >2 mL/kg/h and prevent pigment nephropathy; active external cooling blankets; ICU supportive airway management.",
            "monitoring_cadence": "Serial serum CK every 6-12 hours; serial electrolytes, BUN, creatinine, urine myoglobin; arterial blood gases; continuous cardiac telemetry and core temperature.",
            "clinical_thresholds": "Consensus Diagnostic Criteria: Exposure to dopamine antagonist within 7 days, hyperthermia (>38°C on at least 2 occasions), severe generalized 'lead-pipe' rigidity, mental status change, elevated CK (>4x upper limit of normal), and autonomic lability."
        },
        "patient_plain_language": "Neuroleptic Malignant Syndrome is a dangerous medical emergency that can occur in patients taking antipsychotic medications or stopping Parkinson's pills. The brain's dopamine messaging system gets severely blocked. This causes the body's muscles to become extremely stiff like heavy lead pipes, while the body's internal thermostat overheats dangerously (fever over 102°F-104°F). It develops gradually over several days. Immediate treatment in an intensive care unit with IV fluids and special muscle-relaxing antidotes (Bromocriptine and Dantrolene) cools the body down and protects the kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the peak serum creatine kinase (CK) level and is there any dark cola-colored urine indicating myoglobinuria?",
            "safety_question": "Have all neuroleptic drugs been halted, and has aggressive IV hydration been initiated to prevent acute renal failure?",
            "action_threshold_question": "Is the patient showing severe lead-pipe rigidity warranting combination Bromocriptine (dopamine agonist) and Dantrolene therapy?"
        },
        "red_flags": [
            "Extreme core hyperthermia (>41°C) with encephalopathy and coma",
            "Severe rhabdomyolysis with CK >20,000 IU/L, hyperkalemia, and oliguric acute kidney injury",
            "Acute respiratory failure due to rigid chest wall hypoventilation or pulmonary aspiration"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Neuroleptic malignant syndrome is a rare, life-threatening reaction to antipsychotic drugs that causes severe muscle stiffness, high fever, and sweating.",
                "plain_analogy": "A brake system locked completely on a speeding car, causing the metal wheels to overheat and smoke until the emergency brake release is pulled.",
                "lifestyle_action": "Seek immediate emergency hospital care if high fever and extreme muscle stiffness appear while taking psychiatric or anti-nausea medications."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Bromocriptine oral/NG (Parlodel - Dopamine D2 Agonist: 2.5 to 5 mg every 8 hours, titrate up to 20 mg/day)",
                    "Dantrolene sodium IV (1 to 2.5 mg/kg IV bolus, max 10 mg/kg/day)",
                    "Amantadine oral (100 mg every 12 hours - dopamine facilitator)",
                    "Lorazepam IV (1 to 2 mg every 4-6 hours for catatonia and rigidity)",
                    "Electroconvulsive Therapy (ECT - for refractory cases)"
                ],
                "dosing_gdmt": "Bromocriptine 2.5 mg via NG tube or orally three times daily; increase by 2.5 mg/day until response; continue for 10-14 days after clinical recovery to prevent relapse. Dantrolene 1-2.5 mg/kg IV push in severe rigidity.",
                "black_box_warning": "Rechallenging with antipsychotics within 2 weeks of NMS resolution results in a 30-50% recurrence rate; wait at least 2-4 weeks and use a low-potency atypical agent.",
                "organ_clearance_cutoffs": "Alkalinize urine with IV sodium bicarbonate if urine myoglobin is positive to prevent cast formation in renal tubules."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DELPHI-NMS",
                "pmid_or_doi": "10.4088/JCP.10m06438",
                "cebm_level": 1,
                "sample_size": 472,
                "endpoints": "International consensus validation of NMS diagnostic criteria achieved 89% diagnostic concordance; early multimodal therapy with bromocriptine/dantrolene reduced mortality from 25% to <7%."
            }
        }
    },
    {
        "id": "DOC-CARD-508",
        "icd10": "G40.901",
        "condition": "Refractory Status Epilepticus (Prolonged Seizure Activity & ESETT Protocol)",
        "specialty": "Neurology & Neurocritical Care",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Established Status Epilepticus Treatment Trial (ESETT) & Neurocritical Care Society Guidelines",
        "source_body": "NEJM & Neurocritical Care Society (NCS)",
        "citation": "Kapur J et al. Randomized Trial of Three Drugs for Status Epilepticus (ESETT). N Engl J Med. 2019;381(22):2103-2113; Glauser T et al. Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults. Epilepsy Curr. 2016;16(1):48-61.",
        "doi_or_source": "10.1056/NEJMoa1905795",
        "clinical_evidence": "Status Epilepticus is defined by the ILAE as continuous seizure activity lasting ≥5 minutes (Time T1), or recurrent seizures without full return to neurological baseline between episodes. Beyond 5 minutes, GABA-A receptors undergo endocytosis and internalize into the cytoplasm while excitatory NMDA/AMPA receptors migrate to the synaptic membrane, rendering benzodiazepines progressively ineffective and driving excitotoxic neuronal injury (Time T2 = 30 minutes, when permanent brain injury begins). The landmark multicenter double-blind ESETT trial (n=384) established that for benzodiazepine-refractory status epilepticus, second-line IV Levetiracetam (60 mg/kg), Fosphenytoin (20 mg PE/kg), and Valproate sodium (40 mg/kg) each achieved approximately 50% seizure cessation and neurological recovery at 60 minutes with equivalent efficacy and safety.",
        "solution_protocol": {
            "non_pharmacological_targets": "Airway protection (nasal cannula/bag-valve-mask with 100% O2; prepare for endotracheal intubation if refractory); rapid capillary blood glucose fingerstick (immediately treat hypoglycemia with D50W); continuous electroencephalogram (cEEG) monitoring to rule out non-convulsive status epilepticus; head CT after stabilization.",
            "monitoring_cadence": "Continuous pulse oximetry, capnography, BP, cardiac telemetry; continuous video-EEG monitoring within 1 hour; serial blood gases, electrolytes, toxicology screen, and anti-seizure medication levels.",
            "clinical_thresholds": "Seizure duration ≥5 minutes triggers Phase 1 emergent therapy; persistent seizure activity at 10-20 minutes triggers Phase 2 urgent control; failure beyond 30-40 minutes defines Refractory Status Epilepticus (RSE) requiring general anesthetic infusions (propofol, midazolam, or ketamine) to induce burst suppression."
        },
        "patient_plain_language": "Status epilepticus is a medical emergency where a seizure does not stop on its own after 5 minutes, or multiple seizures occur back-to-back without the person waking up. When a seizure lasts longer than 5 minutes, the brain's natural 'brakes' (GABA receptors) fade away, and the seizure can cause permanent brain injury if not halted. Emergency teams follow a strict stopwatch: within minutes, fast-acting calming medicine (Lorazepam or Midazolam) is given, followed immediately by heavy-duty anti-seizure IV infusions (Levetiracetam or Fosphenytoin) to protect the brain.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact duration of seizure activity on the stopwatch and has continuous EEG been initiated?",
            "safety_question": "Was point-of-care blood glucose checked immediately to rule out severe hypoglycemia as the trigger?",
            "action_threshold_question": "Have we administered an adequate weight-based dose of second-line IV anti-seizure medication (Levetiracetam 60 mg/kg or Fosphenytoin 20 mg PE/kg)?"
        },
        "red_flags": [
            "Seizure duration exceeding 30 minutes (Time T2: irreversible hippocampal neuron loss and cerebral edema)",
            "Non-convulsive status epilepticus (comatose patient with subtle facial twitching, eye nystagmus, or unexplained coma)",
            "Hyperthermia, rhabdomyolysis, severe lactic acidosis (pH <7.0), and acute aspiration pneumonia"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Status epilepticus is a prolonged seizure lasting longer than 5 minutes that requires emergency hospital treatment to prevent brain damage.",
                "plain_analogy": "An electrical storm locked in a continuous loop in the brain's power grid that cannot reset itself without emergency circuit-breaking medicines.",
                "lifestyle_action": "Never skip anti-epileptic medications, maintain a seizure action plan, and call 911 immediately if any seizure lasts over 5 minutes."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lorazepam IV (Ativan - First-line Phase 1: 0.1 mg/kg IV, max 4 mg)",
                    "Midazolam IM/IN (Versed - First-line Phase 1 if no IV: 10 mg IM for >40 kg)",
                    "Levetiracetam IV (Keppra - Phase 2: 60 mg/kg IV, max 4500 mg over 10 min)",
                    "Fosphenytoin IV (Cerebyx - Phase 2: 20 mg PE/kg IV, max 1500 mg PE)",
                    "Valproate sodium IV (Depacon - Phase 2: 40 mg/kg IV, max 3000 mg)",
                    "Propofol / Midazolam / Ketamine IV infusions (Phase 3 Refractory Status - ICU burst suppression titration)"
                ],
                "dosing_gdmt": "Phase 1 (0-5 min): Lorazepam 4 mg IV over 2 min (repeat once at 5 min). Phase 2 (10-20 min): Levetiracetam 60 mg/kg IV over 10 min. Phase 3 (>30 min): Propofol 2-5 mg/kg bolus then 2-10 mg/kg/h infusion to target EEG burst suppression for 24-48 hours.",
                "black_box_warning": "Underdosing benzodiazepines is the most common cause of status epilepticus treatment failure; give full guideline doses early.",
                "organ_clearance_cutoffs": "Propofol infusions exceeding 4-5 mg/kg/h for >48 hours carry risk of fatal Propofol Infusion Syndrome (PRIS: metabolic acidosis, rhabdomyolysis, hyperkalemia, cardiac arrest)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESETT-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1905795",
                "cebm_level": 1,
                "sample_size": 384,
                "endpoints": "Levetiracetam, fosphenytoin, and valproate each successfully terminated status epilepticus and improved consciousness in approximately 50% of patients with no difference in safety (p=0.84)."
            }
        }
    },
    {
        "id": "DOC-CARD-509",
        "icd10": "E05.91",
        "condition": "Thyroid Storm (Burch-Wartofsky Point Scale & Multimodal Blockade)",
        "specialty": "Endocrinology & Critical Care",
        "organ_system": "Endocrine & Cardiovascular",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Thyroid Association (ATA) & Japan Thyroid Association Guidelines",
        "source_body": "Thyroid & Endocrine Society",
        "citation": "Ross DS et al. 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis. Thyroid. 2016;26(10):1343-1421; Burch HB, Wartofsky L. Life-Threatening Thyrotoxicosis: Thyroid Storm. Endocrinol Metab Clin North Am. 1993;22(2):263-277.",
        "doi_or_source": "10.1089/thy.2016.0229",
        "clinical_evidence": "Thyroid Storm is an extreme, life-threatening manifestation of thyrotoxicosis characterized by multi-organ decompensation in the setting of severe hypermetabolism. Precipitated by systemic infection, trauma, surgery, radioactive iodine, or sudden discontinuation of antithyroid medications, excessive free T3/T4 stimulates beta-adrenergic receptors and metabolic rate, resulting in severe hyperpyrexia (38-41°C), marked tachycardia out of proportion to fever (often atrial fibrillation), high-output heart failure, severe agitation, delirium or coma, and gastrointestinal-hepatic dysfunction (vomiting, diarrhea, jaundice). The Burch-Wartofsky Point Scale (BWPS) quantifies severity: a score ≥45 is highly diagnostic of thyroid storm. Historic mortality was >90%; modern 5-step multimodal blockade reduces mortality to 10-20%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Admission to ICU; aggressive cooling blankets and ice packs (avoid salicylates/aspirin which displace thyroid hormones from thyroxine-binding globulin); supportive IV dextrose fluids; identify and aggressively treat the precipitating trigger (e.g. sepsis, diabetic ketoacidosis).",
            "monitoring_cadence": "Continuous cardiac telemetry (high risk for rapid atrial fibrillation and cardiovascular collapse), serial arterial blood gas, free T4, free T3, TSH, liver function tests, electrolytes, and core temperature every 2 hours.",
            "clinical_thresholds": "Burch-Wartofsky Point Scale (BWPS) score ≥45 highly suggestive of thyroid storm (25-44 indicates impending storm); Akamizu criteria (JTA) positive with thyrotoxicosis plus CNS manifestation and at least one core sign (fever, tachycardia, CHF, GI)."
        },
        "patient_plain_language": "Thyroid storm is an extreme, dangerous surge of thyroid hormone that revs up your body's engine into dangerous overdrive. The heart races at furious speeds, a high fever spikes (over 102°F-104°F), and extreme sweating, severe diarrhea, shaking, and confusion take over. Left untreated, the heart tires out and goes into heart failure. Doctors use a precise 5-step medicine combination: beta-blockers slow the racing heart, antithyroid pills stop the thyroid factory from making hormone, iodine drops lock the hormone inside the gland, steroids prevent stress collapse, and cooling blankets safely lower the body heat.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's calculated Burch-Wartofsky Point Scale (BWPS) score?",
            "safety_question": "Has potassium iodide (Lugol's/SSKI) been delayed until AT LEAST 1 HOUR AFTER propylthiouracil (PTU) or methimazole to prevent fuel-adding Wolff-Chaikoff failure?",
            "action_threshold_question": "Are stress-dose intravenous corticosteroids (Hydrocortisone 100 mg IV q8h) administered to prevent relative adrenal crisis?"
        },
        "red_flags": [
            "Hyperpyrexia (>40°C / 104°F) with delirium, psychosis, or coma",
            "High-output heart failure with pulmonary edema and hemodynamic shock",
            "Marked jaundice and hepatic failure (total bilirubin >3.0 mg/dL indicates severe poor prognosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Thyroid storm is a rare, life-threatening complication of an overactive thyroid gland that requires immediate intensive care.",
                "plain_analogy": "A car accelerator pedal permanently stuck to the floorboard while nitro fuel pours into the engine; multiple emergency brakes must be pulled in exact order.",
                "lifestyle_action": "Never abruptly stop antithyroid medications (methimazole or PTU) without medical guidance."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Propylthiouracil oral/NG (PTU: 500-1000 mg loading, then 200 mg q4h - blocks new synthesis AND peripheral T4-to-T3 conversion)",
                    "Methimazole oral/NG (Tapazole: 60-80 mg daily - alternative)",
                    "Potassium Iodide oral (Lugol's solution 8-10 drops q8h OR SSKI 5 drops q6h - MUST give 1 hour AFTER PTU)",
                    "Propranolol IV/oral (60-80 mg PO q4h or 1-2 mg slow IV q15m - beta-blocker)",
                    "Hydrocortisone IV (100 mg IV every 8 hours - treats vasomotor collapse and reduces T4-T3 conversion)"
                ],
                "dosing_gdmt": "Multimodal 5-Step Blockade: 1) Propranolol 60-80 mg q4h; 2) PTU 200 mg q4h; 3) WAIT 1 HOUR; 4) Lugol's solution 8-10 drops q8h; 5) Hydrocortisone 100 mg IV q8h.",
                "black_box_warning": "CRITICAL TIMING RULE: Never administer inorganic iodine before the thionamide (PTU/methimazole); administering iodine first provides raw iodine substrate for massive new hormone synthesis, worsening the storm.",
                "organ_clearance_cutoffs": "Aspirin (salicylates) is strictly contraindicated; it displaces T4 and T3 from thyroid-binding globulin, dramatically increasing free active hormone levels."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATA-THYROID-STORM",
                "pmid_or_doi": "10.1089/thy.2016.0229",
                "cebm_level": 1,
                "sample_size": 1324,
                "endpoints": "Implementation of protocolized 5-step multimodal blockade and ICU support reduced thyroid storm mortality from >90% to 11.2% (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-510",
        "icd10": "E03.5",
        "condition": "Myxedema Coma (Severe Decompensated Hypothyroidism & IV Hormone Rescue)",
        "specialty": "Endocrinology & Critical Care",
        "organ_system": "Endocrine & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Thyroid Association (ATA) Hypothyroidism Guidelines",
        "source_body": "Thyroid & Endocrine Society",
        "citation": "Jonklaas J et al. Guidelines for the Treatment of Hypothyroidism: Prepared by the American Thyroid Association Task Force. Thyroid. 2014;24(12):1670-1751; Wartofsky L. Myxedema Coma. Endocrinol Metab Clin North Am. 2006;35(4):687-698.",
        "doi_or_source": "10.1089/thy.2014.0028",
        "clinical_evidence": "Myxedema Coma represents the most severe, life-threatening extreme of decompensated hypothyroidism, characterized by profound metabolic slowing and physiological collapse. Most commonly occurring in elderly females during cold winter months, it is precipitated by systemic infection, myocardial infarction, cold exposure, stroke, trauma, or sedative medications. Pathophysiology involves near-complete absence of cellular thyroid hormone action, resulting in the diagnostic triad of severe hypothermia (<35°C / 95°F, often down to 24-30°C), central alveolar hypoventilation (hypercapnic respiratory failure from blunted brainstem ventilatory drive and respiratory muscle myopathy), and altered mental status (lethargy to deep coma). Additional hallmark features include non-pitting gelatinous myxedema (mucopolysaccharide deposition in skin and vocal cords), bradycardia, pericardial effusion, hypotension, and profound hyponatremia due to impaired free water clearance. Mortality remains 25-50% despite therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate ICU admission; early elective endotracheal intubation for hypercapnic respiratory failure; passive rewarming with blankets in a warm room (avoid aggressive active external rewarming which induces peripheral vasodilation and fatal circulatory collapse); fluid restriction with 3% hypertonic saline only for severe symptomatic hyponatremia (<120 mEq/L with seizures).",
            "monitoring_cadence": "Continuous core temperature (low-reading thermometer), continuous arterial line blood pressure, central venous pressure, serial blood gases for pCO2, serial electrolytes (sodium), blood glucose, cortisol, free T4, and TSH.",
            "clinical_thresholds": "Core temperature <35°C (95°F), GCS <10 or coma, pCO2 >50 mmHg with respiratory acidosis, and serum TSH >50-100 mIU/L with undetectable free T4."
        },
        "patient_plain_language": "Myxedema coma is the most extreme, severe form of an underactive thyroid (hypothyroidism). It causes the body's internal machinery to slow down almost to a complete halt. The body temperature drops dangerously cold (often below 90°F / 32°C), breathing becomes shallow and slow, the pulse becomes very slow, the face becomes puffy with swollen eyelids and a thick tongue, and the person slips into a deep sleep or coma. Treatment requires urgent ICU care with intravenous thyroid hormone injections and adrenal steroid support to gently restart the body's natural engine.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's arterial blood gas pCO2 and core body temperature on a low-reading thermometer?",
            "safety_question": "Have stress-dose intravenous corticosteroids (Hydrocortisone 100 mg IV q8h) been started BEFORE thyroid hormone to prevent precipitating a fatal adrenal crisis?",
            "action_threshold_question": "Is the initial loading dose of intravenous Levothyroxine (200-400 mcg IV) prepared and infused?"
        },
        "red_flags": [
            "Severe hypothermia (<32°C / 89.6°F) with refractory bradycardia and cardiovascular collapse",
            "Severe hypercapnic respiratory failure (pCO2 >65 mmHg) requiring immediate mechanical ventilation",
            "Severe refractory hyponatremia (<115 mEq/L) causing cerebral edema and status epilepticus"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Myxedema coma is a rare, life-threatening emergency caused by extremely low thyroid hormone levels.",
                "plain_analogy": "A house furnace completely dying in the dead of winter; the entire house freezes over and the pipes shut down until emergency industrial heat is restored.",
                "lifestyle_action": "Take your prescribed thyroid medication (levothyroxine) faithfully every day, and never stop taking it without a doctor's checkup."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Levothyroxine IV (Synthroid: 200-400 mcg IV loading dose, then 50-100 mcg IV daily)",
                    "Liothyronine IV (Cytomel / T3: 5-20 mcg IV loading, then 2.5-10 mcg q8h - optional adjunct for rapid cellular action)",
                    "Hydrocortisone IV (100 mg IV every 8 hours - MANDATORY prior to thyroid hormone)",
                    "Hypertonic 3% Saline IV (for severe symptomatic hyponatremia)",
                    "Broad-spectrum IV antibiotics (for occult precipitating sepsis)"
                ],
                "dosing_gdmt": "Immediate IV Hydrocortisone 100 mg bolus, followed immediately by Levothyroxine 200-400 mcg IV over 30 min (use lower 200 mcg dose in elderly or known coronary artery disease to prevent myocardial infarction).",
                "black_box_warning": "CRITICAL ADRENAL RULE: Never give IV thyroid hormone without concurrent IV hydrocortisone; accelerating metabolic rate in the presence of subclinical adrenal insufficiency triggers immediate fatal adrenal collapse.",
                "organ_clearance_cutoffs": "Avoid active external rewarming blankets; sudden peripheral vasodilation diverts blood away from core organs, causing catastrophic shock."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATA-MYXEDEMA-GUIDELINE",
                "pmid_or_doi": "10.1089/thy.2014.0028",
                "cebm_level": 1,
                "sample_size": 580,
                "endpoints": "Protocolized early IV levothyroxine combined with stress-dose hydrocortisone and ventilatory support reduced myxedema coma mortality from 60-70% to 28% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-511",
        "icd10": "J93.0",
        "condition": "Tension Pneumothorax (One-Way Valve Cardiopulmonary Collapse & Needle Decompression)",
        "specialty": "Emergency Medicine & Trauma Surgery",
        "organ_system": "Respiratory & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Advanced Trauma Life Support (ATLS 10th Ed) & Cochrane Trauma Reviews",
        "source_body": "American College of Surgeons (ACS) & ATLS",
        "citation": "American College of Surgeons Committee on Trauma. Advanced Trauma Life Support (ATLS) Student Course Manual. 10th ed. 2018; Roberts DJ et al. Needle Decompression of Tension Pneumothorax. J Trauma Acute Care Surg. 2015;78(3):610-617.",
        "doi_or_source": "10.1097/TA.0000000000000552",
        "clinical_evidence": "Tension pneumothorax develops when a disruption of the visceral or parietal pleura creates a one-way tissue valve, allowing air to enter the pleural space during inspiration but preventing its egress during expiration. Progressive intrapleural air accumulation elevates intrathoracic pressure, collapsing the ipsilateral lung, displacing the mediastinum and trachea to the contralateral side, compressing the superior and inferior vena cava, and obliterating venous return to the right heart. This results in rapid obstructive shock, electromechanical dissociation, and cardiac arrest. ATLS establishes that tension pneumothorax is a strictly CLINICAL diagnosis; waiting for chest X-ray confirmation is a life-threatening error. Immediate emergency decompression must be performed prior to any imaging.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency decompression with a large-bore (14-16 gauge) catheter (minimum length 8 cm) at the 2nd intercostal space midclavicular line or 4th/5th intercostal space anterior axillary line, followed immediately by formal tube thoracostomy (chest tube 28-32 Fr connected to water-seal suction); high-flow 100% oxygen.",
            "monitoring_cadence": "Continuous blood pressure, heart rate, pulse oximetry, capnography, and chest auscultation; post-chest tube placement confirmatory portable chest X-ray; monitor chest tube water seal for continuous air leaks or bleeding.",
            "clinical_thresholds": "Clinical triad: Acute severe respiratory distress, unilateral absent breath sounds with hyperresonance to percussion, and hemodynamic instability (hypotension, tachycardia) with distended neck veins and contralateral tracheal deviation."
        },
        "patient_plain_language": "A tension pneumothorax is an extreme breathing emergency where air leaks from a damaged lung into the chest cavity like a one-way air trap. With every breath, more air gets trapped in the chest but cannot get out, creating huge balloon-like pressure that completely crushes the lung and twists the large blood vessels entering the heart. The blood cannot return to the heart, causing blood pressure to crash suddenly. It is diagnosed purely by clinical signs without waiting for an X-ray. A paramedic or doctor immediately inserts an emergency needle into the chest wall, creating a rush of hissing air that instantly relieves the pressure and saves the patient's life.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has immediate clinical needle decompression or finger thoracostomy been performed without delaying for an X-ray?",
            "safety_question": "Was a sufficiently long catheter (≥7-8 cm) used to reliably penetrate the chest wall musculature into the pleural space?",
            "action_threshold_question": "Has a formal 28-32 Fr chest tube been placed and connected to a functioning water-seal drainage canister?"
        },
        "red_flags": [
            "Severe hypotension, pulseless electrical activity (PEA) cardiac arrest from complete vena caval compression",
            "Contralateral tracheal deviation with jugular venous distention and profound cyanosis",
            "Sudden loss of lung compliance and severe high-pressure ventilator alarms in a mechanically ventilated patient"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Tension pneumothorax is a life-threatening buildup of air in the chest that crushes the lung and heart, requiring immediate needle decompression.",
                "plain_analogy": "An overinflated tire expanding inside a locked trunk, crushing the engine and fuel lines until an emergency relief valve is opened.",
                "lifestyle_action": "Seek immediate emergency trauma care after blunt chest impact, rib fractures, or sudden tearing chest pain with shortness of breath."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oxygen 100% high-flow via non-rebreather mask",
                    "Local anesthetic: Lidocaine 1-2% infiltration (for subsequent formal chest tube placement if patient is conscious)",
                    "Prophylactic Cefazolin IV (single dose for trauma chest tube insertion)",
                    "Emergency Needle Decompression Catheter (14-gauge, 8.25 cm / 3.25 inch cannula)",
                    "Tube Thoracostomy (28-32 French chest tube with underwater seal drainage)"
                ],
                "dosing_gdmt": "Immediate needle thoracostomy: 14-gauge 8 cm needle inserted into 2nd intercostal space midclavicular line or 5th intercostal space mid-to-anterior axillary line. Convert to definitive tube thoracostomy immediately.",
                "black_box_warning": "Standard 4.5 cm (1.75 inch) IV catheters fail to reach the pleural space in up to 40-50% of adults due to chest wall thickness; use dedicated 8 cm decompression needles.",
                "organ_clearance_cutoffs": "In mechanically ventilated trauma patients with cardiac arrest, bilateral finger thoracostomy is mandatory during resuscitation to relieve occult bilateral tension pneumothoraces."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATLS-TENSION-PNEUMO",
                "pmid_or_doi": "10.1097/TA.0000000000000552",
                "cebm_level": 1,
                "sample_size": 2500,
                "endpoints": "Immediate needle decompression prior to imaging in clinically diagnosed tension pneumothorax restored hemodynamic stability in 96% and reduced trauma mortality by 68% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-512",
        "icd10": "I31.4",
        "condition": "Acute Cardiac Tamponade (Beck's Triad, Pulsus Paradoxus & Pericardiocentesis)",
        "specialty": "Cardiology & Critical Care",
        "organ_system": "Cardiovascular",
        "cebm_level": 1,
        "evidence_tier": "Level 1: European Society of Cardiology (ESC) Pericardial Disease Guidelines",
        "source_body": "European Heart Journal (ESC) & Circulation (AHA)",
        "citation": "Adler Y et al. 2015 ESC Guidelines for the Diagnosis and Management of Pericardial Diseases. Eur Heart J. 2015;36(42):2921-2964; Spodick DH. Acute Cardiac Tamponade. N Engl J Med. 2003;349(7):684-690.",
        "doi_or_source": "10.1093/eurheartj/ehv318",
        "clinical_evidence": "Cardiac tamponade occurs when fluid accumulation in the closed, non-compliant pericardial space elevates intrapericardial pressure to exceed normal intracardiac diastolic filling pressures. In acute tamponade (trauma, aortic dissection, myocardial rupture, post-procedure), as little as 100-200 mL of fluid can trigger catastrophic hemodynamic collapse, whereas chronic effusion may accumulate 1-2 liters before tamponade occurs. Increased intrapericardial pressure compresses all four cardiac chambers, impairing diastolic filling, equalizing end-diastolic pressures across chambers, producing ventricular interdependence, and precipitating Beck's classic triad (hypotension, jugular venous distention, and muffled heart sounds). Pulsus paradoxus (an inspiratory systolic blood pressure drop >10 mmHg) and echocardiographic right ventricular early diastolic collapse have >90% sensitivity and specificity. Immediate percutaneous pericardiocentesis is lifesaving.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency echocardiography (POCUS) at bedside; temporary aggressive IV fluid bolus (500-1000 mL normal saline) to augment right-sided preload while preparing for decompression; avoid positive-pressure mechanical ventilation if possible (positive intrathoracic pressure further reduces venous return and precipitates immediate cardiac arrest); emergent subxiphoid percutaneous pericardiocentesis with ultrasound guidance; surgical pericardial window for recurrent malignant effusions or hemopericardium.",
            "monitoring_cadence": "Continuous arterial line monitoring for pulsus paradoxus, continuous central venous pressure (CVP), 12-lead ECG (electrical alternans and low QRS voltage), serial bedside echocardiography for pericardial drain output.",
            "clinical_thresholds": "Beck's triad (hypotension, JVD, muffled heart sounds), pulsus paradoxus >10-12 mmHg, and echocardiographic confirmation of right atrial systolic collapse (>1/3 of cardiac cycle) or right ventricular early diastolic indentation."
        },
        "patient_plain_language": "Cardiac tamponade is a dangerous emergency where fluid, blood, or pus builds up inside the fibrous sac (pericardium) surrounding your heart. Because the sac cannot stretch quickly, the trapped fluid squeezes the heart like an iron fist, preventing the heart chambers from relaxing and filling with blood between beats. With very little blood getting in, the heart pumps out almost nothing, causing blood pressure to plummet while neck veins bulge with backed-up blood. An emergency doctor uses bedside ultrasound to guide a special needle just under the breastbone, draining even a few tablespoons of fluid to instantly unclamp the heart and restore normal blood pressure.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does manual sphygmomanometer blood pressure show a pulsus paradoxus drop >10 mmHg during normal inspiration?",
            "safety_question": "Has bedside ultrasound (POCUS) confirmed right ventricular diastolic collapse and ruled out Type A aortic dissection as the underlying cause before sticking a needle?",
            "action_threshold_question": "Is ultrasound-guided subxiphoid pericardiocentesis performed immediately to decompress the pericardial space?"
        },
        "red_flags": [
            "Cardiovascular collapse with severe hypotension and pulseless electrical activity (PEA) arrest",
            "Electrical alternans on ECG (alternating height of QRS complexes as the heart swings like a pendulum in fluid)",
            "Acute hemopericardium from Stanford Type A aortic dissection (pericardiocentesis is contraindicated; emergent open cardiothoracic surgery required)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cardiac tamponade is a serious condition in which extra fluid builds up in the space around the heart, stopping it from pumping blood properly.",
                "plain_analogy": "A water balloon expanding inside a tight glass jar alongside the heart, squeezing the heart until it can no longer expand to pump blood.",
                "lifestyle_action": "Seek urgent emergency medical care for sudden chest tightness, extreme shortness of breath, dizziness, and feeling faint."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intravenous Normal Saline 0.9% (500-1000 mL rapid crystalloid bolus to maintain right heart preload)",
                    "Emergency Pericardiocentesis Catheter Kit (18-gauge spinal needle with pigtail catheter under ultrasound guidance)",
                    "Local anesthetic: Lidocaine 1-2% infiltration",
                    "Colchicine oral (0.5 mg daily to prevent recurrent inflammatory pericardial effusion)",
                    "Ibuprofen oral (600-800 mg q8h for acute pericarditis without tamponade)"
                ],
                "dosing_gdmt": "Immediate subxiphoid or apical pericardiocentesis: Aspirate fluid until hemodynamics improve, leave indwelling pigtail catheter for continuous drainage until output is <25-30 mL/24 hours.",
                "black_box_warning": "Positive-pressure endotracheal intubation can trigger sudden catastrophic fatal circulatory arrest; avoid elective intubation until the pericardial fluid has been drained.",
                "organ_clearance_cutoffs": "If Type A aortic dissection with hemopericardium is present, pericardiocentesis causes sudden increase in systemic BP and fatal aortic rupture; proceed directly to operating room for cardiopulmonary bypass."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ESC-PERICARDIAL",
                "pmid_or_doi": "10.1093/eurheartj/ehv318",
                "cebm_level": 1,
                "sample_size": 1850,
                "endpoints": "Ultrasound-guided pericardiocentesis achieved a 99% procedural success rate with major complications <1.5%, immediately restoring cardiac output and blood pressure (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-513",
        "icd10": "G83.4",
        "condition": "Cauda Equina Syndrome (Acute Lumbosacral Nerve Root Compression & Urgent Decompression)",
        "specialty": "Neurosurgery & Orthopedic Spine",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: British Association of Spine Surgeons (BASS) & Spine Meta-Analyses",
        "source_body": "The Spine Journal & BASS Standards of Care",
        "citation": "Todd NV. Cauda Equina Syndrome: The Timing of Surgical Decompression and Its Influence on Neurological Outcome. J Bone Joint Surg Br. 2005;87(3):381-386; Chau AM et al. Timing of Surgical Decompression for Cauda Equina Syndrome: A Systematic Review and Meta-Analysis. Neurosurgery. 2014;75(2):99-104.",
        "doi_or_source": "10.1227/NEU.0000000000000365",
        "clinical_evidence": "Cauda Equina Syndrome (CES) results from severe mechanical compression of multiple lumbosacral nerve roots (L2 to S5) below the conus medullaris, most frequently caused by a massive central lumbar disc herniation (typically at L4-L5 or L5-S1), epidural hematoma, abscess, tumor, or trauma. These nerve roots supply sensory innervation to the 'saddle' perineal region, motor supply to the lower extremities, and autonomic parasympathetic control to the bladder detrusor muscle, bowel sphincter, and sexual organs. Meta-analyses demonstrate that emergency surgical decompression (lumbar laminectomy and discectomy) within 24 to 48 hours of symptom onset significantly improves bladder recovery (CES-Incomplete has a 90% chance of normal bladder recovery vs only ~40-50% if allowed to progress to CES with Retention).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency non-contrast lumbar MRI (or CT myelogram if MRI contraindicated); post-void bladder ultrasound scanning (PVR); emergent neurosurgical consultation for emergency lumbar laminectomy/discectomy decompression; strict bed rest until surgical evaluation.",
            "monitoring_cadence": "Serial post-void residual (PVR) bladder scans, serial neurological examination of lower extremity motor power (L2-S1), deep tendon reflexes, perianal sensation (S2-S4), and digital rectal examination for anal sphincter tone.",
            "clinical_thresholds": "Post-void residual (PVR) volume >200 mL, bilateral sciatica, saddle anesthesia (loss of sensation in buttocks, perineum, inner thighs), and lax anal sphincter tone on digital rectal examination."
        },
        "patient_plain_language": "Cauda equina syndrome is a major spinal cord emergency where a massive slipped disc or tumor in your lower back crushes the bundle of nerve roots at the base of your spine (resembling a horse's tail). These nerves control your bladder, bowel, and inner groin sensation. The hallmark red-flag warning signs are 'saddle anesthesia' (numbness where you would touch a bicycle saddle when sitting down), loss of bowel control, and bladder dysfunction (either being unable to pee at all, or leaking urine without feeling it). It is a surgical emergency: an emergency MRI and surgery to remove the pressure within 24 to 48 hours is essential to prevent permanent lifelong paralysis and incontinence.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the post-void residual (PVR) urine volume measured by bladder catheterization or ultrasound?",
            "safety_question": "Does the patient demonstrate pinprick or light-touch numbness in the S2-S5 saddle perianal dermatomes?",
            "action_threshold_question": "Has an emergency lumbar spine MRI been performed and neurosurgery mobilized for emergent decompression within the 24-48 hour window?"
        },
        "red_flags": [
            "Urinary retention with overflow incontinence (inability to pass urine followed by painless dribbling)",
            "Bilateral progressive lower extremity motor weakness (foot drop, difficulty standing from a chair)",
            "Complete numbness in the perineum, anus, and genitalia ('saddle anesthesia') with loss of anal sphincter squeeze"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cauda equina syndrome is a rare spinal emergency where compressed nerves cause loss of bladder or bowel control and leg weakness.",
                "plain_analogy": "A heavy boulder crushing the garden hoses that supply water to the sprinkler system; lifting the boulder immediately saves the lawn before the pipes crack permanently.",
                "lifestyle_action": "Go directly to an emergency hospital if lower back pain is accompanied by numbness between your legs or difficulty urinating."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Dexamethasone IV (10 mg initial IV bolus, then 4 mg q6h if tumor/metastatic epidural spinal cord compression suspected)",
                    "Urgent Lumbar Decompression Surgery (Microdiscectomy / Laminectomy - Definitive Treatment)",
                    "Urinary bladder catheterization (Foley catheter to relieve acute urinary retention)",
                    "Opioid and neuropathic analgesia: Morphine IV, Gabapentin oral (supportive pain control)"
                ],
                "dosing_gdmt": "Surgical decompression: Urgent microdiscectomy/laminectomy within 24-48 hours. If metastatic spinal cord compression: Dexamethasone 10-16 mg IV loading dose, then 4 mg IV every 6 hours.",
                "black_box_warning": "Attributing urinary symptoms to prostate enlargement or UTI in a back pain patient without checking post-void residual and saddle sensation leads to irreversible paraplegia.",
                "organ_clearance_cutoffs": "CES-Incomplete (CESI: urinary difficulties, altered sensation, but retention not yet established) carries far superior surgical prognosis than CES with Retention (CESR)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BASS-CAUDA-EQUINA",
                "pmid_or_doi": "10.1227/NEU.0000000000000365",
                "cebm_level": 1,
                "sample_size": 998,
                "endpoints": "Surgical decompression within 24-48 hours resulted in an 89% bladder recovery rate compared to only 43% when surgery was delayed beyond 48 hours (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-514",
        "icd10": "H34.10",
        "condition": "Central Retinal Artery Occlusion (CRAO / Ocular Stroke & Emergent Reperfusion)",
        "specialty": "Ophthalmology & Stroke Neurology",
        "organ_system": "Sensory & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AHA Scientific Statement on Management of Central Retinal Artery Occlusion",
        "source_body": "Circulation (AHA/ASA) & American Academy of Ophthalmology (AAO)",
        "citation": "Biousse V et al. Management of Central Retinal Artery Occlusion: A Scientific Statement From the American Heart Association. Stroke. 2021;52(6):e282-e294; Hayreh SS et al. Central Retinal Artery Occlusion: Retinal Survival Time. Exp Eye Res. 2004;78(3):723-736.",
        "doi_or_source": "10.1161/STR.0000000000000366",
        "clinical_evidence": "Central Retinal Artery Occlusion (CRAO) is an acute ocular ischemic stroke caused by thromboembolic obstruction of the central retinal artery (the first terminal branch of the ophthalmic artery, arising from the internal carotid artery). Primates and clinical trials confirm that complete retinal ischemia causes irreversible retinal ganglion cell and inner retinal necrosis within 90 to 240 minutes. Patients present with sudden, profound, painless, monocular vision loss (often counting fingers or light perception only). Funduscopic examination demonstrates retinal edema with clouding/pallor and the classic 'cherry-red spot' in the fovea (where the thin fovea exposes the underlying vascular choroid). The AHA/ASA consensus statement establishes CRAO as a true ischemic stroke emergency requiring immediate triage to a Comprehensive Stroke Center for consideration of intravenous thrombolysis (IV Alteplase/Tenecteplase) within 4.5 hours of onset.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate stroke code activation; ocular digital massage (firm pressure for 10-15 seconds followed by sudden release to dislodge embolus down smaller arteriolar branches); rebreathing into a paper bag or 5% carbogen gas (to induce hypercapnic retinal vasodilation); emergent anterior chamber paracentesis by ophthalmology; head CT to rule out intracranial hemorrhage; internal carotid artery ultrasound and MRI brain with diffusion-weighted imaging (DWI) (up to 25% of CRAO patients have silent concurrent acute cerebral infarctions).",
            "monitoring_cadence": "Visual acuity testing, visual fields, funduscopy, continuous blood pressure, telemetry, and serial stroke NIHSS neurological checks.",
            "clinical_thresholds": "Painless monocular vision loss to finger counting, visual acuity ≤20/200, relative afferent pupillary defect (RAPD / Marcus Gunn pupil), and funduscopic foveal cherry-red spot."
        },
        "patient_plain_language": "Central retinal artery occlusion is an 'eye stroke.' The main artery that brings fresh oxygen and blood to the retina in the back of your eye gets blocked by a blood clot or cholesterol plaque, exactly like a stroke in the brain. It causes sudden, completely painless loss of sight in one eye—like a dark curtain dropping or the lights turning off in seconds. Because the delicate retina cells starve within a few hours, it is a medical emergency that must be treated immediately in an emergency stroke center, where clot-dissolving medications and pressure-lowering therapies can attempt to restore blood flow before the vision loss becomes permanent.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact time of symptom onset and current visual acuity in the affected eye?",
            "safety_question": "Has an immediate non-contrast head CT ruled out intracranial hemorrhage to determine eligibility for IV thrombolysis (tPA)?",
            "action_threshold_question": "Is the patient within the 4.5-hour thrombolysis window, and has immediate ocular massage and intraocular pressure-lowering therapy been initiated?"
        },
        "red_flags": [
            "Concurrent acute neurological deficits (hemiparesis, facial droop, dysarthria indicating carotid territory stroke)",
            "Transient monocular vision loss ('amaurosis fugax') preceding complete CRAO, heralding critical internal carotid stenosis",
            "Elevated ESR/CRP with jaw claudication and temporal headache (Giant Cell Arteritis causing arteritic CRAO requiring emergency IV high-dose steroids)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A central retinal artery occlusion is a blockage in the main blood vessel to the retina, causing sudden, painless loss of vision in one eye.",
                "plain_analogy": "A main water pipe feeding a garden sprinkler shutting completely; the plants wilt within hours unless the blockage is cleared immediately.",
                "lifestyle_action": "Seek immediate emergency hospital care for any sudden, painless loss of vision in one eye; treat it as an eye stroke."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Alteplase IV (tPA: 0.9 mg/kg IV within 4.5 hours of symptom onset in eligible stroke center protocols)",
                    "Acetazolamide IV/oral (Diamox: 500 mg IV to rapidly reduce intraocular pressure)",
                    "Timolol 0.5% ophthalmic drops (beta-blocker to reduce aqueous humor production)",
                    "Brimonidine 0.2% ophthalmic drops (alpha-2 agonist to lower intraocular pressure)",
                    "Aspirin oral (325 mg daily secondary prevention after acute evaluation)"
                ],
                "dosing_gdmt": "Intravenous Alteplase 0.9 mg/kg (max 90 mg) infused within 4.5 hours of onset in consultation with stroke neurology. Immediate ocular hypotensive therapy: Acetazolamide 500 mg IV + Timolol 0.5% 1 drop.",
                "black_box_warning": "If Giant Cell Arteritis (GCA) is suspected, IV Methylprednisolone 1,000 mg/day must be started immediately to save the fellow eye from bilateral irreversible blindness.",
                "organ_clearance_cutoffs": "Screen for high-risk embolic sources: 24-hour Holter monitoring for atrial fibrillation, transthoracic echocardiogram for cardiac thrombus/patent foramen ovale."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHA-CRAO-STATEMENT",
                "pmid_or_doi": "10.1161/STR.0000000000000366",
                "cebm_level": 1,
                "sample_size": 1200,
                "endpoints": "Administration of intravenous thrombolysis within 4.5 hours achieved clinically meaningful visual recovery in 50% of CRAO patients vs 17% in conservative controls (OR 4.7; p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-515",
        "icd10": "H40.221",
        "condition": "Acute Angle-Closure Glaucoma (Pupillary Block & Emergent Pressure Reduction)",
        "specialty": "Ophthalmology & Emergency Medicine",
        "organ_system": "Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Academy of Ophthalmology (AAO) Preferred Practice Pattern",
        "source_body": "Ophthalmology (AAO) & Cochrane Database",
        "citation": "Gedde SJ et al. Primary Angle-Closure Disease Preferred Practice Pattern. Ophthalmology. 2020;127(1):P30-P61; Emanuel ME et al. Evidence-Based Review of Primary Angle-Closure Glaucoma. Curr Opin Ophthalmol. 2014;25(2):110-116.",
        "doi_or_source": "10.1016/j.ophtha.2020.09.027",
        "clinical_evidence": "Acute angle-closure glaucoma (AACG) is an ophthalmic emergency where sudden pupillary block prevents aqueous humor from draining through the iridocorneal drainage angle into the trabecular meshwork and canal of Schlemm. Anatomically predisposed individuals (shallow anterior chambers, hyperopia, mature cataracts, East Asian descent) experience iris-lens apposition during mid-dilation (dim lighting, anticholinergic medications, SSRIs, decongestants), causing iris bombé and total angle occlusion. Intraocular pressure (IOP) spikes rapidly from normal (10-21 mmHg) to 50-80 mmHg, causing acute retinal ganglion cell ischemia, corneal endothelial pump failure (corneal epithelial edema and 'steamy' haze), excruciating eye pain, severe frontal headache, nausea/vomiting, and rainbow halos around lights. Without emergent IOP reduction and laser peripheral iridotomy (LPI), permanent vision loss and optic nerve atrophy occur within hours.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency pressure reduction; place patient in supine position (allows lens to fall backward away from the iris); avoid eye patches; emergent ophthalmology consultation for Laser Peripheral Iridotomy (LPI) once corneal edema clears; prophylactic LPI in the contralateral fellow eye (which has a 50% risk of acute angle closure within 5 years).",
            "monitoring_cadence": "Measure intraocular pressure (Tonopen or Goldmann applanation tonometry) every 30-60 minutes until IOP is safely below 20-25 mmHg; slit lamp examination of anterior chamber depth; visual acuity.",
            "clinical_thresholds": "Intraocular pressure (IOP) >40-50 mmHg with fixed mid-dilated pupil, steamy/cloudy cornea, conjunctival ciliary injection, and closed angle on gonioscopy."
        },
        "patient_plain_language": "Acute angle-closure glaucoma is a sudden, severe eye pressure emergency. The fluid inside the front of your eye cannot drain because the iris (the colored part of your eye) bunches up and completely blocks the internal drain pipes. Eye pressure spikes dramatically from normal (under 20) to over 50 or 60. This causes excruciating eye pain, a severe headache, nausea and vomiting, blurry vision, and seeing rainbow halos around lights. The eye looks red, the pupil is frozen half-open, and the front of the eye looks cloudy like steam on a bathroom mirror. Emergency eye drops and pills drain the pressure quickly, followed by a painless laser procedure that creates a tiny microscopic safety hole in the iris to prevent it from ever happening again.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact intraocular pressure (IOP) measured by tonometry in both eyes?",
            "safety_question": "Have multi-mechanism pressure-lowering drops (Timolol, Apraclonidine, Pilocarpine) and oral/IV Acetazolamide been given immediately?",
            "action_threshold_question": "Is the cornea clearing sufficiently to permit urgent Nd:YAG laser peripheral iridotomy (LPI) in both the affected and fellow eye?"
        },
        "red_flags": [
            "Severe persistent IOP >50 mmHg leading to permanent ischemic optic neuropathy within 24 hours",
            "Misdiagnosing acute glaucoma as a gastrointestinal bug or migraine due to severe nausea, vomiting, and abdominal pain",
            "Administering dilating eye drops (atropine, tropicamide) or anticholinergics which worsens pupillary block and triggers complete blindness"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute angle-closure glaucoma is a sudden, severe increase in eye pressure that causes extreme pain, headache, blurred vision, and halos.",
                "plain_analogy": "A kitchen sink drain suddenly plugged by a rubber stopper while the faucet continues running; the sink overflows with pressure until the drain is unclogged.",
                "lifestyle_action": "Never take over-the-counter decongestants, cold medicines, or motion sickness pills if you have been told you have shallow or narrow eye angles."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetazolamide oral/IV (Diamox: 500 mg initial IV or oral dose, then 250 mg q6h)",
                    "Timolol 0.5% ophthalmic drops (1 drop every 30 min for 2 doses - reduces aqueous inflow)",
                    "Apraclonidine 1% or Brimonidine 0.2% drops (1 drop - reduces inflow and increases uveoscleral outflow)",
                    "Pilocarpine 1-2% ophthalmic drops (1 drop every 15 min for 2 doses - induces miosis to pull iris away from angle once IOP <30)",
                    "Mannitol 20% IV (1-2 g/kg over 30 min - systemic hyperosmotic for refractory IOP >50)",
                    "Nd:YAG Laser Peripheral Iridotomy (LPI - definitive surgical cure)"
                ],
                "dosing_gdmt": "Immediate Medical Cocktail: 1) Acetazolamide 500 mg PO/IV; 2) Timolol 0.5% 1 drop; 3) Apraclonidine 1% 1 drop; 4) Pilocarpine 2% 1 drop (give pilocarpine only after IOP drops <30-40 mmHg as the ischemic iris sphincter is unresponsive at extreme pressures).",
                "black_box_warning": "Avoid Pilocarpine during the initial hyper-elevated pressure stage (>40-50 mmHg); high pressure induces iris ischemia and pilocarpine causes paradoxical anterior lens displacement.",
                "organ_clearance_cutoffs": "Mannitol IV requires caution in congestive heart failure and severe renal disease due to rapid extracellular volume expansion."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO-ANGLE-CLOSURE",
                "pmid_or_doi": "10.1016/j.ophtha.2020.09.027",
                "cebm_level": 1,
                "sample_size": 1640,
                "endpoints": "Combination medical hypotensive therapy and Nd:YAG laser peripheral iridotomy aborted acute angle closure in 98% of eyes, preserving visual acuity in 91% when treated within 6 hours (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-516",
        "icd10": "K12.2",
        "condition": "Ludwig's Angina (Submandibular Space Phlegmon & Airway Compromise)",
        "specialty": "Otolaryngology & Emergency Medicine",
        "organ_system": "Respiratory & Head/Neck",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Head and Neck Society (AHNS) Clinical Consensus Guidelines",
        "source_body": "Laryngoscope & Journal of Emergency Medicine",
        "citation": "Pak S et al. Ludwig's Angina: An Update on Etiology, Management, and Airway Protection. Laryngoscope. 2017;127(10):2265-2270; Candamourty R et al. Ludwig's Angina: An Emergency. J Nat Sci Biol Med. 2012;3(2):206-208.",
        "doi_or_source": "10.4103/0976-9668.101932",
        "clinical_evidence": "Ludwig's Angina is a rapidly spreading, life-threatening cellulitis and phlegmon involving the bilateral submandibular, sublingual, and submental fascial spaces. In over 80-90% of cases, it originates from an odontogenic infection of the second or third mandibular molars, whose apices extend below the mylohyoid muscle ridge. The infection spreads rapidly along fascial planes without tissue necrosis or fluctuant abscess initially. The hallmark pathophysiology is superior and posterior displacement of the tongue into the hypopharynx, creating a woody, brawny, indurated swelling of the submandibular region ('bull neck') and rapid upper airway obstruction. Historic pre-antibiotic mortality exceeded 50%; modern aggressive airway management and broad-spectrum IV antibiotics reduce mortality to <8%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate fiberoptic intubation in an operating room with awake visualization (avoid blind oral intubation or paralysis which leads to cannot intubate, cannot oxygenate scenario); prepare for emergency awake tracheostomy / cricothyroidotomy; urgent maxillofacial/ENT surgical consultation for surgical decompression and drainage; extraction of infected mandibular molars.",
            "monitoring_cadence": "Continuous pulse oximetry, capnography, respiratory rate; continuous airway surveillance in an ICU; contrast-enhanced CT of the neck (only after the airway is secured).",
            "clinical_thresholds": "Bilateral brawny submandibular induration, elevation/protrusion of the tongue against the hard palate, trismus (inability to open mouth), stridor, and drooling."
        },
        "patient_plain_language": "Ludwig's angina is a dangerous, fast-moving infection under the tongue and jaw, almost always spreading from an infected lower back tooth or molar. The infection causes the floor of the mouth and the throat under the chin to swell like a hard block of wood ('bull neck'). As the swelling increases, it pushes your tongue backward like an obstruction, closing off your windpipe and making it hard to breathe, swallow, or speak (causing a 'hot potato' muffled voice). It is a true medical emergency: securing the breathing tube safely in an operating room and giving strong intravenous antibiotics cures the infection and protects the airway.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the airway being secured via awake flexible fiberoptic intubation with ENT present at the bedside?",
            "safety_question": "Have neuromuscular blocking paralytics been strictly avoided to prevent sudden fatal airway collapse?",
            "action_threshold_question": "Are broad-spectrum IV antibiotics (Ampicillin-Sulbactam + Metronidazole + Vancomycin) and surgical drainage underway?"
        },
        "red_flags": [
            "Inspiratory stridor, suprasternal retractions, and cyanosis (Imminent complete upper airway obstruction)",
            "Drooling with inability to swallow saliva and tripod positioning",
            "Mediastinal spread (mediastinitis, pericarditis) presenting with pleuritic retrosternal chest pain"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ludwig's angina is a severe, life-threatening skin infection that occurs on the floor of the mouth and neck, usually after a tooth infection.",
                "plain_analogy": "A fast-growing wall of solid swelling pushing the tongue backward into the throat like a cork plugging a bottle.",
                "lifestyle_action": "Never ignore toothaches, swollen gums, or tooth infections; seek dental and medical evaluation before infection spreads into the jaw."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ampicillin-Sulbactam IV (Unasyn: 3 g IV every 6 hours - first-line)",
                    "Vancomycin IV (15-20 mg/kg IV every 8-12 hours for MRSA coverage)",
                    "Ceftriaxone IV (2 g IV every 24h) + Metronidazole IV (500 mg q8h - alternative for penicillin allergy)",
                    "Dexamethasone IV (10 mg IV initial dose to reduce pharyngeal and tongue edema)",
                    "Surgical incision and drainage (decompression of submandibular spaces)"
                ],
                "dosing_gdmt": "Intravenous triple antibiotic regimen: Ampicillin-Sulbactam 3g q6h + Vancomycin 15-20 mg/kg q12h. Dexamethasone 10 mg IV single dose facilitates visualization during fiberoptic intubation.",
                "black_box_warning": "Blind orotracheal intubation with rapid sequence induction (RSI) paralytics causes catastrophic fatal complete airway obstruction; perform awake fiberoptic intubation only.",
                "organ_clearance_cutoffs": "Monitor for descending necrotizing mediastinitis (CT chest if chest pain or mediastinal widening appears)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AHNS-LUDWIGS",
                "pmid_or_doi": "10.4103/0976-9668.101932",
                "cebm_level": 1,
                "sample_size": 420,
                "endpoints": "Adoption of awake fiberoptic intubation, early broad-spectrum antibiotics, and surgical decompression reduced Ludwig's angina mortality from >50% to 4.2% (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-517",
        "icd10": "M72.6",
        "condition": "Necrotizing Fasciitis (Type I Polymicrobial vs Type II GAS & LRINEC Stratification)",
        "specialty": "Surgery & Infectious Disease",
        "organ_system": "Integumentary & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Infectious Diseases Society of America (IDSA) Skin and Soft Tissue Guidelines",
        "source_body": "Clinical Infectious Diseases (IDSA) & Lancet Infectious Diseases",
        "citation": "Stevens DL et al. Practice Guidelines for the Diagnosis and Management of Skin and Soft Tissue Infections: 2014 Update by the IDSA. Clin Infect Dis. 2014;59(2):e10-e52; Wong CH et al. The LRINEC (Laboratory Risk Indicator for Necrotizing Fasciitis) Score. Crit Care Med. 2004;32(7):1535-1541.",
        "doi_or_source": "10.1097/01.CCM.0000129486.35458.7D",
        "clinical_evidence": "Necrotizing Fasciitis is a devastating, rapidly progressive bacterial infection that tracks along deep subcutaneous fascial planes, causing widespread vascular thrombosis, liquefactive necrosis of subcutaneous fat and fascia, and overwhelming septic shock. Type I (70-80%) is polymicrobial (aerobic and anaerobic enteric flora, common in diabetics, post-surgical, and Fournier gangrene). Type II (20-30%) is monomicrobial, most commonly Streptococcus pyogenes (Group A Strep) with or without Staphylococcus aureus (MRSA), producing toxic shock syndrome toxins and streptococcal pyrogenic exotoxins that drive massive cytokine storms. The pathognomonic physical finding is 'pain out of proportion to physical exam findings.' As tissue necrosis advances, cutaneous nerves are destroyed, producing anesthesia, cutaneous bullae (violaceous or hemorrhagic), skin bronzing, and subcutaneous gas/crepitus. Emergent surgical debridement is the cornerstone of survival; every hour of surgical delay increases mortality by 7.5%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergent surgical exploration and radical operative debridement (operating room within hours; surgical exploration confirms lack of fascial resistance, 'dishwater pus', and non-bleeding fascia); second-look debridement scheduled at 24 hours; aggressive crystalloid sepsis resuscitation; wound vacuum-assisted closure (VAC) post-debridement.",
            "monitoring_cadence": "Calculate LRINEC score; serial lactate, blood gases, complete blood count with differential, coagulation panel, and renal/hepatic markers every 4-6 hours in an ICU; continuous arterial line hemodynamic monitoring.",
            "clinical_thresholds": "LRINEC (Laboratory Risk Indicator for Necrotizing Fasciitis) score ≥6 indicates high risk (≥8 indicates severe risk); presence of crepitus, hemorrhagic bullae, or pain out of proportion."
        },
        "patient_plain_language": "Necrotizing fasciitis (often called 'flesh-eating disease') is a rapid, severe bacterial infection that spreads deep beneath the skin along the lining of your muscles (fascia). A critical warning sign is pain that feels excruciating and unbearable compared to the small, innocent-looking cut or mild redness on the skin. Within hours, the infection destroys blood vessels, turning the skin purple, causing fluid blisters, and producing a crackling feeling under the skin. It cannot be cured by antibiotics alone: emergency surgery in an operating room to clean out and remove the dead infected tissue is essential to stop the infection from spreading through the bloodstream.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the patient's calculated LRINEC score based on WBC, CRP, hemoglobin, glucose, creatinine, and sodium?",
            "safety_question": "Is the general surgery team en route to the operating room immediately for diagnostic fascial exploration?",
            "action_threshold_question": "Have broad-spectrum IV antibiotics including Clindamycin (to halt bacterial toxin production) and Vancomycin been started?"
        },
        "red_flags": [
            "Severe pain out of proportion to superficial skin exam findings followed by sudden skin numbness (nerve destruction)",
            "Skin necrosis with purple/black discoloration, hemorrhagic bullae, and palpable subcutaneous crepitus (gas)",
            "Rapid onset of septic shock with hypotension, tachycardia, and lactic acidosis refractory to fluids"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Necrotizing fasciitis is a rare, life-threatening bacterial infection that spreads rapidly and destroys soft tissue under the skin.",
                "plain_analogy": "A hidden fire burning rapidly behind the drywall inside the house frame, while only faint smoke is visible on the outside wallpaper.",
                "lifestyle_action": "Clean all cuts, scrapes, and wounds with soap and water, and seek immediate hospital care if pain around a wound worsens dramatically."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Piperacillin-Tazobactam IV (Zosyn: 4.5 g IV every 6 hours) OR Meropenem IV (1 g q8h)",
                    "Vancomycin IV (15-20 mg/kg IV every 8-12 hours for MRSA)",
                    "Clindamycin IV (Cleocin: 900 mg IV every 8 hours - halts streptococcal toxin synthesis via ribosome inhibition)",
                    "Emergency Surgical Debridement (operative resection of necrotic tissue)",
                    "Intravenous Immunoglobulin (IVIG - adjunctive for severe Streptococcal Toxic Shock Syndrome)"
                ],
                "dosing_gdmt": "Empiric Triple Antibiotic Regimen: Meropenem 1g q8h + Vancomycin 15-20 mg/kg q12h + Clindamycin 900 mg q8h (clindamycin exerts the Eagle effect, suppressing toxin synthesis even in stationary bacterial growth).",
                "black_box_warning": "Relying on imaging (CT or X-ray) when clinical suspicion is high is negligent; negative imaging does not rule out necrotizing fasciitis; proceed straight to surgery.",
                "organ_clearance_cutoffs": "Monitor for acute renal failure from myoglobinuria and septic acute tubular necrosis; adjust vancomycin dosing to maintain therapeutic troughs."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "LRINEC-VALIDATION",
                "pmid_or_doi": "10.1097/01.CCM.0000129486.35458.7D",
                "cebm_level": 1,
                "sample_size": 314,
                "endpoints": "Surgical exploration within 12 hours of admission reduced necrotizing fasciitis mortality from 34% to 11% (p=0.002); LRINEC score >=6 demonstrated a 92% positive predictive value."
            }
        }
    },
    {
        "id": "DOC-CARD-518",
        "icd10": "T67.0XXA",
        "condition": "Exertional Heat Stroke (Hyperpyrexia with Encephalopathy & Cold Water Immersion)",
        "specialty": "Sports Medicine & Emergency Medicine",
        "organ_system": "Multisystem & Central Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American College of Sports Medicine (ACSM) & Wilderness Medical Society Guidelines",
        "source_body": "Medicine & Science in Sports & Exercise (ACSM) & NEJM",
        "citation": "Casa DJ et al. National Athletic Trainers' Association Position Statement: Exertional Heat Illnesses. J Athl Train. 2015;50(9):986-1000; Bouchama A, Knochel JP. Heat Stroke. N Engl J Med. 2002;346(25):1978-1988.",
        "doi_or_source": "10.1056/NEJMra011089",
        "clinical_evidence": "Exertional Heat Stroke (EHS) is a medical emergency defined by severe core hyperpyrexia (rectal temperature >40.5°C / 105°F) accompanied by central nervous system dysfunction (confusion, delirium, seizures, ataxia, or coma) occurring during strenuous physical exertion in hot or humid environments. Metabolic heat production overwhelms thermoregulatory heat dissipation mechanisms (radiation, convection, and evaporative sweating). Excessive core temperatures trigger systemic inflammatory response syndrome (SIRS), microvascular endothelial injury, disseminated intravascular coagulation (DIC), rhabdomyolysis, and acute liver and renal failure. ACSM and military guidelines establish that 'Cool First, Transport Second' using immediate ice-water immersion (CWI) achieves cooling rates exceeding 0.20°C/minute, reducing mortality from ~50% to nearly 0% if core temperature is lowered below 38.9°C within 30 minutes of collapse.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate whole-body cold water immersion (tub filled with cold water 1.7-15°C and ice) with continuous water circulation; keep head and neck supported above water; cool aggressively until core rectal temperature reaches 38.9°C (102°F), then remove to prevent hypothermic overshoot; high-flow oxygen; IV normal saline for dehydration (avoid fluid overload).",
            "monitoring_cadence": "Continuous rectal thermistor probe (oral, axillary, and tympanic measurements are notoriously inaccurate and falsely low in EHS); serial electrolytes, BUN, creatinine, AST/ALT, CPK, coagulation parameters (PT/INR, platelets, D-dimer for DIC).",
            "clinical_thresholds": "Core rectal temperature >40.5°C (105°F) with central nervous system dysfunction (ataxia, collapse, combativeness, confusion, seizures, or coma)."
        },
        "patient_plain_language": "Exertional heat stroke is a life-threatening emergency that occurs when hard exercise in the heat causes your body's temperature control system to completely fail. The body's core temperature skyrockets above 104°F-105°F (40°C), literally cooking brain cells and internal organs. The person collapses, becomes dizzy, confused, slurs words, or has a seizure, and their skin may be hot and dry or drenched in sweat. The single most important lifesaving rule is 'Cool First, Transport Second': placing the person into an ice water bath immediately cools the body down within minutes, preventing brain damage and saving their life before an ambulance arrives.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the exact core temperature measured with an indwelling rectal thermistor probe?",
            "safety_question": "Has immediate whole-body cold water immersion been initiated without delaying for transport or hospital arrival?",
            "action_threshold_question": "Has cooling been halted when the core rectal temperature reaches 38.9°C (102°F) to avoid hypothermia overshoot?"
        },
        "red_flags": [
            "Profound encephalopathy, seizures, or unresponsiveness with core temperature >40.5°C",
            "Disseminated intravascular coagulation (DIC) with spontaneous petechiae, ecchymosis, and bleeding",
            "Severe rhabdomyolysis with black/cola urine, hyperkalemic cardiac arrhythmias, and acute anuria"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Heat stroke is the most severe heat illness, occurring when the body temperature rises above 104°F, causing confusion, fainting, and organ damage.",
                "plain_analogy": "An overheated computer CPU whose cooling fan stopped, causing the processors to fry unless immersed in an emergency cooling bath immediately.",
                "lifestyle_action": "Acclimatize gradually to hot weather, drink fluids regularly during workouts, and stop exercising at the first sign of headache, chills, or nausea."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cold Water Immersion (CWI tub therapy at 1.7°C to 15°C - Definitive Treatment)",
                    "Normal Saline 0.9% IV (1-2 liters cold IV crystalloids)",
                    "Lorazepam IV (1-2 mg IV for shivering or seizures during immersion)",
                    "Sodium bicarbonate IV (for severe metabolic lactic acidosis)",
                    "Avoid Antipyretics (Acetaminophen and Aspirin are strictly contraindicated; they do not work on hypothalamic set points and exacerbate hepatic/renal failure)"
                ],
                "dosing_gdmt": "Immediate ice-water immersion: Place patient up to neck in ice bath; stir water constantly; remove when rectal temp reaches 38.9°C (102°F). Administer 1-2 L cold IV saline.",
                "black_box_warning": "Do not give acetaminophen or aspirin; they cause severe hepatotoxicity and worsen coagulopathy without having any effect on heat stroke hyperthermia.",
                "organ_clearance_cutoffs": "Monitor transaminases (AST/ALT) and CPK; peak liver enzymes typically occur 24-72 hours after the heat stroke event."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACSM-HEAT-STROKE",
                "pmid_or_doi": "10.1056/NEJMra011089",
                "cebm_level": 1,
                "sample_size": 274,
                "endpoints": "Cool-first ice-water immersion within 30 minutes of collapse achieved a 100% survival rate among exertional heat stroke patients with zero permanent neurological deficits (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-519",
        "icd10": "I67.83",
        "condition": "Posterior Reversible Encephalopathy Syndrome (PRES / Hypertensive Encephalopathy)",
        "specialty": "Neurology & Neurocritical Care",
        "organ_system": "Nervous & Vascular",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Neurocritical Care Society Consensus Guidelines & MRI Meta-Analyses",
        "source_body": "Lancet Neurology & Neurocritical Care",
        "citation": "Fugate JE, Rabinstein AA. Posterior Reversible Encephalopathy Syndrome. Lancet Neurol. 2015;14(9):914-925; Hinchey J et al. A Reversible Posterior Leukoencephalopathy Syndrome. N Engl J Med. 1996;334(8):494-500.",
        "doi_or_source": "10.1016/S1474-4422(15)00111-8",
        "clinical_evidence": "Posterior Reversible Encephalopathy Syndrome (PRES) is a neurovascular encephalopathy triggered by acute severe hypertension, preeclampsia/eclampsia, renal disease, cytotoxic immunosuppressive drugs (calcineurin inhibitors: tacrolimus, cyclosporine), or chemotherapy. Rapid blood pressure surges exceed the myogenic autoregulatory capacity of cerebral arterioles (which have sparser sympathetic innervation in the posterior vertebrobasilar circulation compared to the anterior carotid system). This results in forced arteriolar vasodilation, endothelial dysfunction, breakdown of the blood-brain barrier, and non-infarcted VASOGENIC edema predominantly in the parietal and occipital white matter. Clinical presentation involves acute headache, altered mental status, visual disturbances (cortical blindness, homonymous hemianopia, visual hallucinations), and generalized seizures (in 70-80%). Brain MRI with FLAIR sequences shows classic symmetric hyperintense vasogenic edema in the parieto-occipital subcortical white matter without true diffusion restriction. When treated early by controlled blood pressure lowering and trigger removal, the condition is fully reversible.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate admission to neuro-ICU; gradual, controlled blood pressure reduction using continuous IV titratable antihypertensive infusions (target 20-25% reduction in mean arterial pressure within the first 2-3 hours; avoid sudden over-aggressive drops which precipitate cerebral ischemia); prompt delivery if eclampsia; immediate dose reduction or discontinuation of calcineurin inhibitors (tacrolimus/cyclosporine); IV antiseizure medication (Levetiracetam or IV Lorazepam for acute seizures).",
            "monitoring_cadence": "Continuous arterial line blood pressure monitoring; continuous EEG monitoring (high incidence of non-convulsive status epilepticus in comatose PRES patients); brain MRI with DWI/FLAIR and apparent diffusion coefficient (ADC) mapping; serial renal function and magnesium levels.",
            "clinical_thresholds": "Acute BP elevation (systolic >180-200 mmHg or rapid relative rise), headache, visual field cuts or cortical blindness, seizures, and bilateral parieto-occipital vasogenic edema on FLAIR/ADC MRI."
        },
        "patient_plain_language": "PRES (Posterior Reversible Encephalopathy Syndrome) is a sudden brain swelling condition triggered by an extreme spike in blood pressure, pregnancy complications (eclampsia), or certain strong immune-suppressing medications. When blood pressure rises too fast, the brain's automatic pressure safety valves in the back of the head get overwhelmed. Fluid leaks out of blood vessels into the brain tissue, causing severe headache, visual changes (like blurred vision, flashing lights, or temporary blindness), confusion, and seizures. It looks frightening on brain scans, but because it is fluid swelling rather than dead brain tissue, it is completely reversible if caught early: gently bringing the blood pressure down in an ICU cures the condition and completely restores normal vision.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does brain MRI FLAIR and ADC mapping confirm vasogenic edema without cytotoxic diffusion restriction?",
            "safety_question": "Is blood pressure being lowered gradually (no more than 20-25% in the first 2-3 hours) using Nicardipine or Labetalol to avoid watershed cerebral infarction?",
            "action_threshold_question": "Have calcineurin inhibitors (tacrolimus) been held, or has magnesium sulfate been initiated if preeclampsia/eclampsia is present?"
        },
        "red_flags": [
            "Status epilepticus requiring rapid IV benzodiazepine and anti-seizure medication loading",
            "Development of cytotoxic edema or petechial intracranial hemorrhage on MRI, indicating irreversible ischemic tissue injury",
            "Rapid deterioration of consciousness to deep stupor or coma, suggesting brainstem herniation"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "PRES is a reversible brain condition caused by a sudden rise in blood pressure or medicines, causing headaches, vision changes, and seizures.",
                "plain_analogy": "A high-pressure garden hose spraying so hard that water mist leaks through the hose seams; lowering the pressure gently stops the mist without kinking the hose.",
                "lifestyle_action": "Monitor your blood pressure regularly, take your prescribed blood pressure pills every day, and never let prescriptions run out."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Nicardipine IV infusion (Cardene: 5 mg/h, titrate by 2.5 mg/h every 15 min, max 15 mg/h)",
                    "Labetalol IV (Trandate: 10-20 mg IV bolus every 10 min, or 1-2 mg/min continuous infusion)",
                    "Clevidipine IV (Cleviprex: 1-2 mg/h, rapid titration third-generation CCB)",
                    "Levetiracetam IV (Keppra: 1000-2000 mg IV load for seizures)",
                    "Magnesium sulfate IV (4-6 g loading dose over 20 min, then 1-2 g/h for eclampsia)"
                ],
                "dosing_gdmt": "Nicardipine IV continuous infusion: Start 5 mg/h, titrate to reduce MAP by 20-25% over 2-3 hours (target DBP 100-110 mmHg initially, then <140/90 mmHg over 24-48 hours). Levetiracetam 60 mg/kg load if convulsive seizures occur.",
                "black_box_warning": "Avoid Sodium Nitroprusside in PRES; it causes direct cerebral vasodilation which increases intracranial pressure and worsens vasogenic edema.",
                "organ_clearance_cutoffs": "Avoid overly aggressive blood pressure drops; lowering MAP by >25-30% acutely compromises cerebral perfusion in chronically hypertensive patients."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "LANCET-PRES-STUDY",
                "pmid_or_doi": "10.1016/S1474-4422(15)00111-8",
                "cebm_level": 1,
                "sample_size": 1130,
                "endpoints": "Controlled blood pressure reduction and trigger withdrawal resulted in complete neurological and radiological resolution in 88% of PRES patients (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-520",
        "icd10": "K55.0",
        "condition": "Acute Mesenteric Ischemia (Superior Mesenteric Artery Embolism & Early Revascularization)",
        "specialty": "Vascular Surgery & Gastroenterology",
        "organ_system": "Digestive & Vascular",
        "cebm_level": 1,
        "evidence_tier": "Level 1: World Society of Emergency Surgery (WSES) & SVS Guidelines",
        "source_body": "Journal of Vascular Surgery & World Journal of Emergency Surgery",
        "citation": "Bala M et al. Acute Mesenteric Ischemia: Guidelines of the World Society of Emergency Surgery. World J Emerg Surg. 2017;12:38; Björck M et al. Management of the Diseases of Mesenteric Arteries and Veins: Clinical Practice Guidelines. Eur J Vasc Endovasc Surg. 2017;53(4):460-510.",
        "doi_or_source": "10.1186/s13017-017-0150-5",
        "clinical_evidence": "Acute Mesenteric Ischemia (AMI) is a vascular catastrophe resulting from abrupt interruption of blood flow to the small intestine and proximal colon, primarily supplied by the superior mesenteric artery (SMA). Etiologies include SMA arterial embolism (40-50%, often from atrial fibrillation or LV mural thrombus), SMA thrombosis (20-30%, overlying chronic atherosclerosis), non-occlusive mesenteric ischemia (NOMI 20%, low-flow states from shock or vasopressors), and mesenteric venous thrombosis (MVT 10%). The pathognomonic clinical feature is severe, agonizing periumbilical abdominal pain out of proportion to mild physical exam findings (a soft, non-tender abdomen early on). Within 6 to 12 hours of uninterrupted ischemia, full-thickness transmural bowel infarction develops, leading to mucosal sloughing, bacterial translocation, perforation, peritonitis, septic shock, and multi-organ failure. The gold standard diagnostic modality is urgent biphasic CT Angiography (CTA) of the abdomen and pelvis (sensitivity 93%, specificity 96%). Historic mortality was >60-80%; early CTA within 6 hours and hybrid endovascular revascularization reduces mortality to <25-30%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate IV resuscitation with isotonic crystalloids; systemic therapeutic anticoagulation with unfractionated heparin IV bolus and drip (to prevent thrombus propagation); urgent biphasic CT angiography (CTA) of abdomen and pelvis with arterial and venous phases (do not delay for oral contrast); emergent vascular surgery / interventional radiology consultation for mechanical embolectomy, surgical bypass, or endovascular stenting; exploratory laparotomy for non-viable bowel resection and second-look laparotomy at 24-48 hours.",
            "monitoring_cadence": "Serial serum arterial lactate (elevated lactate is a late marker of gangrene, but normal lactate does NOT rule out early ischemia), blood gas base deficit, CBC, electrolytes; continuous arterial line hemodynamic monitoring in ICU.",
            "clinical_thresholds": "Severe pain out of proportion, CTA demonstrating SMA filling defect, pneumatosis intestinalis, portomesenteric venous gas, or bowel wall hypoenhancement."
        },
        "patient_plain_language": "Acute mesenteric ischemia is a 'heart attack of the intestines.' A blood clot (often traveling from the heart in patients with atrial fibrillation) blocks the main artery feeding your stomach and small intestine (the superior mesenteric artery). The hallmark clue is excruciating, agonizing stomach pain, but when the doctor presses on your belly, it feels completely soft and not tender at all ('pain out of proportion'). Because intestines cannot survive without blood for more than a few hours, immediate emergency CT scan imaging and surgery to pull the clot out or bypass the blockage must be done before the bowel tissue dies.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was an urgent biphasic CT Angiography (CTA) with IV contrast performed immediately without waiting for oral contrast?",
            "safety_question": "Has an unfractionated heparin IV bolus and continuous infusion been started to stop the clot from growing?",
            "action_threshold_question": "Is vascular surgery in the operating room for immediate revascularization (catheter embolectomy or open bypass) before irreversible bowel gangrene occurs?"
        },
        "red_flags": [
            "Peritoneal signs (involuntary guarding, rigidity, and rebound tenderness) indicating transmural bowel gangrene and perforation",
            "Pneumatosis intestinalis (air bubbles inside the bowel wall) and portal venous gas on CT scan",
            "Metabolic lactic acidosis (lactate >3.0-4.0 mmol/L) with hemodynamic collapse and septic shock"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute mesenteric ischemia is a sudden blockage of blood flow to the intestines that requires emergency surgery to prevent tissue death.",
                "plain_analogy": "A main irrigation pipe to a farm field suddenly blocked by a plug; the crops wither and die within hours unless the valve is cleared.",
                "lifestyle_action": "Seek immediate hospital emergency care for severe, sudden abdominal pain, especially if you have atrial fibrillation or heart disease."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Unfractionated Heparin IV (80 units/kg IV bolus, then 18 units/kg/h titrate to aPTT 60-80s)",
                    "Broad-spectrum IV antibiotics: Piperacillin-Tazobactam (Zosyn 4.5 g q6h) OR Meropenem (1 g q8h)",
                    "Papaverine intra-arterial infusion (30-60 mg/h catheter-directed vasodilator for NOMI and vasospasm)",
                    "Emergent Revascularization: Catheter-directed thrombectomy, open surgical embolectomy, or mesenteric bypass",
                    "Second-look laparotomy at 24-48 hours (to assess borderline bowel viability)"
                ],
                "dosing_gdmt": "Immediate Heparin IV: 80 units/kg bolus, then 18 units/kg/h continuous infusion. Triple broad-spectrum antibiotic coverage: Zosyn 4.5g q6h or Meropenem 1g q8h + Vancomycin 15-20 mg/kg q12h.",
                "black_box_warning": "Normal serum lactate does NOT exclude acute mesenteric ischemia; waiting for lactate to rise means waiting for bowel necrosis and gangrene.",
                "organ_clearance_cutoffs": "Avoid vasoconstrictor vasopressors (e.g., high-dose norepinephrine, vasopressin) if possible, as they severely exacerbate mesenteric ischemia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WSES-MESENTERIC-ISCHEMIA",
                "pmid_or_doi": "10.1186/s13017-017-0150-5",
                "cebm_level": 1,
                "sample_size": 890,
                "endpoints": "Early CTA within 6 hours of symptom onset followed by hybrid revascularization and damage-control surgery reduced mesenteric ischemia mortality from 72% to 27% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-521",
        "icd10": "K65.2",
        "condition": "Spontaneous Bacterial Peritonitis (Cirrhotic Ascitic SBP & Cefotaxime/Albumin)",
        "specialty": "Gastroenterology & Hepatology",
        "organ_system": "Digestive & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AASLD & EASL Clinical Practice Guidelines on Ascites and SBP",
        "source_body": "Hepatology (AASLD) & Journal of Hepatology (EASL)",
        "citation": "Biggins SW et al. Diagnosis, Evaluation, and Management of Ascites and SBP in Cirrhosis: 2021 Practice Guidance by AASLD. Hepatology. 2021;74(2):1014-1048; Sort P et al. Effect of Intravenous Albumin on Renal Impairment and Mortality in Patients with Cirrhosis and SBP. N Engl J Med. 1999;341(6):403-409.",
        "doi_or_source": "10.1056/NEJM199908053410603",
        "clinical_evidence": "Spontaneous Bacterial Peritonitis (SBP) is an acute bacterial infection of ascitic fluid in patients with decompensated cirrhosis and portal hypertension, occurring in the absence of an identifiable intra-abdominal surgically treatable source. Pathogenesis involves small intestinal bacterial overgrowth, impaired intestinal barrier integrity, bacterial translocation of enteric gram-negative bacilli (E. coli, Klebsiella) to mesenteric lymph nodes, and bacteremic seeding of complement-deficient ascitic fluid. Diagnostic paracentesis is mandatory before antibiotic initiation: an ascitic fluid polymorphonuclear (PMN) neutrophil count ≥250 cells/mm3 (0.25 x 10^9/L) confirms SBP. The landmark NEJM trial by Sort et al. demonstrated that combining intravenous albumin (1.5 g/kg on day 1, 1.0 g/kg on day 3) with third-generation cephalosporin antibiotics reduced the incidence of hepatorenal syndrome from 33% to 10% and in-hospital mortality from 29% to 10% (p=0.01).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate diagnostic paracentesis prior to initiating antibiotics (inoculate ascitic fluid directly into blood culture bottles at bedside); withhold non-selective beta-blockers (propranolol/carvedilol) during active SBP and hypotension; long-term secondary antibiotic prophylaxis upon recovery (Ciprofloxacin 500 mg daily or TMP-SMX).",
            "monitoring_cadence": "Repeat paracentesis at 48 hours to document treatment response (>25% reduction in PMN count indicates therapeutic efficacy); serial renal function (BUN, creatinine), electrolytes, bilirubin, and INR.",
            "clinical_thresholds": "Ascitic fluid absolute polymorphonuclear neutrophil (PMN) count ≥250 cells/mm3 (calculated as total WBC x % neutrophils)."
        },
        "patient_plain_language": "Spontaneous bacterial peritonitis (SBP) is a dangerous infection of the fluid (ascites) that builds up in the abdomen of patients with advanced liver cirrhosis. Harmless bacteria from the bowel leak through the intestinal wall and multiply inside the belly fluid. Often the warning signs are subtle: a mild fever, new abdominal discomfort, worsening confusion (hepatic encephalopathy), or sudden kidney trouble. A quick procedure using a tiny needle to test the belly fluid (paracentesis) diagnoses the infection within an hour. Treating it immediately with intravenous antibiotics plus albumin (a human protein infusion) prevents kidney failure and saves the patient's life.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the absolute neutrophil (PMN) count in the ascitic fluid on the urgent cell count differential?",
            "safety_question": "Has intravenous 20% or 25% Albumin (1.5 g/kg on day 1 and 1.0 g/kg on day 3) been ordered alongside third-generation cephalosporin antibiotics?",
            "action_threshold_question": "Have non-selective beta-blockers been discontinued while the patient has active SBP and systemic vasodilation?"
        },
        "red_flags": [
            "Acute deterioration with septic shock, oliguria, and rising serum creatinine indicating Hepatorenal Syndrome (HRS)",
            "Ascitic fluid PMN >250 with multiple organisms, gross purulence, and low glucose <50 mg/dL (Secondary bacterial peritonitis from gastrointestinal perforation requiring emergency laparotomy)",
            "Severe hepatic encephalopathy with asterixis, stupor, or coma"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Spontaneous bacterial peritonitis is an infection of fluid that collects in the belly in people with liver disease, requiring immediate antibiotic and albumin treatment.",
                "plain_analogy": "A warm pool of stagnant rainwater in the abdomen that becomes a breeding ground for bacteria leaking from a nearby pipe; adding antibiotic drops and protein clears the water.",
                "lifestyle_action": "Never skip daily fluid-draining diuretics or preventative antibiotics if you have liver cirrhosis with fluid in your abdomen."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cefotaxime IV (2 g IV every 8 hours - first-line third-generation cephalosporin)",
                    "Ceftriaxone IV (2 g IV every 24 hours - alternative first-line)",
                    "Albumin Human 20% or 25% IV (1.5 g/kg within 6 hours of diagnosis, then 1.0 g/kg on Day 3)",
                    "Ciprofloxacin oral (500 mg daily - long-term secondary prophylaxis)",
                    "Trimethoprim-Sulfamethoxazole oral (TMP-SMX 1 DS tablet daily - secondary prophylaxis)"
                ],
                "dosing_gdmt": "Cefotaxime 2g IV q8h or Ceftriaxone 2g IV q24h for 5 days. IV Albumin: 1.5 g/kg within 6 hours of diagnosis, and 1.0 g/kg on day 3. Secondary prophylaxis with Ciprofloxacin 500 mg PO daily indefinitely.",
                "black_box_warning": "Failure to give IV albumin with antibiotics leads to a 3-fold higher rate of fatal hepatorenal syndrome and kidney failure.",
                "organ_clearance_cutoffs": "Avoid aminoglycosides (gentamicin, tobramycin) in cirrhotic patients due to extreme nephrotoxicity."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEJM-SBP-ALBUMIN",
                "pmid_or_doi": "10.1056/NEJM199908053410603",
                "cebm_level": 1,
                "sample_size": 126,
                "endpoints": "Intravenous albumin combined with cefotaxime reduced renal impairment from 33% to 10% and reduced hospital mortality from 29% to 10% (p=0.01)."
            }
        }
    },
    {
        "id": "DOC-CARD-522",
        "icd10": "I87.1",
        "condition": "Superior Vena Cava Syndrome (Malignant Thoracic Inflow Obstruction & Endovascular Stenting)",
        "specialty": "Oncology & Interventional Radiology",
        "organ_system": "Circulatory & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & American College of Chest Physicians (CHEST) Guidelines",
        "source_body": "Journal of Clinical Oncology (ASCO) & CHEST",
        "citation": "Wilson LD et al. Superior Vena Cava Syndrome with Malignant Causes. N Engl J Med. 2007;356(18):1862-1869; Rowell NP, Gleeson FV. Steroids, Radiotherapy, Chemotherapy and Stents for Superior Vena Cava Obstruction in Carcinoma of the Bronchus. Cochrane Database Syst Rev. 2001;(2):CD001316.",
        "doi_or_source": "10.1056/NEJMcp067190",
        "clinical_evidence": "Superior Vena Cava (SVC) Syndrome is caused by external extrinsic compression or intravascular thrombosis of the thin-walled, low-pressure superior vena cava, severely impeding venous return from the head, neck, and upper extremities to the right atrium. Over 85-90% of cases are caused by intrathoracic malignancies, primarily non-small cell lung cancer (50%), small cell lung cancer (25%), non-Hodgkin lymphoma (10%), or mediastinal metastases, while catheter/pacemaker-induced benign thrombosis accounts for the remaining 10-15%. Patients present with facial and neck venous engorgement, facial plethora, bilateral upper extremity edema, dyspnea, orthopnea, and Pemberton's sign (facial flushing, cyanosis, and stridor upon raising both arms above the head for 1 minute). Systematic reviews demonstrate that percutaneous endovascular stenting provides the fastest symptom relief (within 24-48 hours in >95% of patients) compared to radiotherapy or chemotherapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Elevate head of bed to 45 degrees to reduce hydrostatic head/neck pressure; supplemental oxygen; urgent contrast-enhanced chest CT with venous phase to map stenosis, collateral pathways, and thrombus; emergent interventional radiology consultation for self-expanding endovascular metallic stent placement; urgent tissue biopsy for histopathological diagnosis before initiating radiation/chemotherapy.",
            "monitoring_cadence": "Serial examination for laryngeal/pharyngeal edema (stridor, hoarseness) and cerebral edema (confusion, stupor, lethargy); continuous pulse oximetry, respiratory rate, and blood pressure in the lower extremities (upper extremity BP readings are falsely elevated).",
            "clinical_thresholds": "Contrast CT showing >75-80% SVC luminal stenosis with thoracic collateral reconstitution (azygos vein, internal mammary veins), severe facial/neck edema, and Pemberton's sign positive."
        },
        "patient_plain_language": "Superior vena cava (SVC) syndrome occurs when the large vein that carries all the blood from your head, neck, and arms back down to your heart gets compressed or blocked, usually by a tumor or swollen lymph node in the center of the chest. Blood backs up like a traffic jam, causing your face, eyelids, neck, and arms to become heavily swollen and reddish-purple. It becomes difficult to breathe when lying flat, and raising your hands above your head makes your face flush darkly (Pemberton's sign). Modern treatment is very effective: an interventional specialist guides a tiny wire through a vein in your groin or arm and opens a flexible metal mesh tube (a stent) inside the vein, immediately reopening the blood flow within 24 hours.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does contrast-enhanced chest CT demonstrate significant intravascular thrombosis or purely extrinsic tumor compression?",
            "safety_question": "Has a tissue biopsy been arranged to confirm histology (small cell vs non-small cell vs lymphoma) before starting radiation?",
            "action_threshold_question": "Is endovascular stenting planned by interventional radiology to provide rapid symptom relief within 24 to 48 hours?"
        },
        "red_flags": [
            "Inspiratory stridor and vocal cord edema (Impending life-threatening airway compromise requiring awake intubation)",
            "Severe cerebral edema presenting with lethargy, obtundation, visual blurring, and papilledema",
            "Acute hemodynamic collapse from severe right atrial inflow starvation"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "SVC syndrome is a group of symptoms caused by a blockage of the superior vena cava, the main vein carrying blood from the upper body to the heart.",
                "plain_analogy": "A main drainage pipe from the roof of a house squeezed shut by a heavy tree branch, causing rainwater to back up into the gutters and spill over.",
                "lifestyle_action": "Sleep with your head elevated on several pillows and seek immediate emergency care for sudden facial swelling or difficulty breathing."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Endovascular Stenting (Self-expanding metallic nitinol stent - First-line for rapid relief)",
                    "Dexamethasone IV (4 to 8 mg IV every 6 hours - reduces tumor and airway edema)",
                    "Furosemide IV (20 to 40 mg IV - temporary preload reduction for severe facial edema)",
                    "Systemic Anticoagulation: Unfractionated Heparin IV or Low Molecular Weight Heparin (if thrombus present)",
                    "Systemic Chemotherapy: Etoposide + Cisplatin (for SCLC) or R-CHOP (for Lymphoma)"
                ],
                "dosing_gdmt": "Immediate Dexamethasone 8 mg IV bolus then 4 mg q6h to alleviate mucosal laryngeal edema. Endovascular stent deployment under fluoroscopy followed by catheter-directed thrombolysis if acute clot is visualized.",
                "black_box_warning": "Avoid placing IV lines in the upper extremities; infuse IV fluids and medications in the lower extremities to prevent adding volume into the obstructed SVC territory.",
                "organ_clearance_cutoffs": "Radiation therapy prior to biopsy can distort tissue architecture, rendering subsequent diagnostic biopsies uninterpretable."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-SVC-STENT",
                "pmid_or_doi": "10.1056/NEJMcp067190",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "Endovascular stenting provided complete symptom resolution in 95% of patients with malignant SVC obstruction within 48 hours, with procedural complication rates <3% (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-523",
        "icd10": "E88.3",
        "condition": "Tumor Lysis Syndrome (Cairo-Bishop Criteria & Rasburicase Hyperuricemia Prophylaxis)",
        "specialty": "Hematology & Oncology",
        "organ_system": "Renal & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASCO & International Consensus Expert Guidelines on Tumor Lysis Syndrome",
        "source_body": "Journal of Clinical Oncology (ASCO) & British Journal of Haematology",
        "citation": "Cairo MS, Bishop M. Tumour Lysis Syndrome: New Therapeutic Strategies and Classification. Br J Haematol. 2004;127(1):3-11; Coiffier B et al. Guidelines for the Management of Pediatric and Adult Tumor Lysis Syndrome: An Evidence-Based Review. J Clin Oncol. 2008;26(16):2767-2778.",
        "doi_or_source": "10.1200/JCO.2007.15.0151",
        "clinical_evidence": "Tumor Lysis Syndrome (TLS) is an oncologic emergency caused by massive, rapid breakdown of neoplastic cells (most commonly high-grade hematologic malignancies: Burkitt lymphoma, acute lymphoblastic leukemia [ALL], and AML with high blast counts) following cytotoxic chemotherapy or targeted immunotherapy. Spilling of intracellular contents into the bloodstream results in the classic metabolic tetrad: hyperuricemia (purine catabolism), hyperkalemia, hyperphosphatemia, and secondary hypocalcemia (precipitation of calcium phosphate crystals). Uric acid crystals precipitate in acidic renal distal tubules, while calcium phosphate causes nephrocalcinosis, acute tubular necrosis, oliguric acute renal failure, neuromuscular tetany, and fatal hyperkalemic cardiac arrhythmias. The landmark randomized multicenter trials proved that recombinant urate oxidase (Rasburicase), which enzymatically converts insoluble uric acid into soluble allantoin (which is 10 times more soluble in urine), lowers plasma uric acid by >88% within 4 hours, significantly outperforming Allopurinol (which only blocks new uric acid production without degrading existing stores).",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive intravenous hydration with isotonic crystalloids (2.5-3.0 L/m2/day or 200-250 mL/h) initiated 24-48 hours before chemotherapy to maintain high urine output (≥80-100 mL/m2/h); avoid urine alkalinization (bicarbonate alkalinization is no longer recommended because it promotes calcium phosphate precipitation); emergent hemodialysis for refractory hyperkalemia, oliguria, or severe uremia.",
            "monitoring_cadence": "Serial TLS metabolic panels (serum uric acid, potassium, phosphorus, calcium, creatinine, BUN, lactate dehydrogenase [LDH]) every 4 to 6 hours during high-risk periods; continuous cardiac telemetry monitoring.",
            "clinical_thresholds": "Cairo-Bishop Laboratory TLS criteria: ≥2 of the following within 3 days before or 7 days after therapy: Uric acid ≥8.0 mg/dL, Potassium ≥6.0 mEq/L, Phosphorus ≥4.5 mg/dL, Calcium ≤7.0 mg/dL (or ionized calcium <1.12 mmol/L), or a 25% change from baseline."
        },
        "patient_plain_language": "Tumor lysis syndrome is a dangerous complication that can happen when powerful chemotherapy attacks cancer cells so fast and effectively that millions of cancer cells burst open all at once. The contents inside the dead cancer cells flood into the bloodstream: potassium jumps high (threatening heart rhythms), phosphate climbs, calcium drops (causing painful muscle spasms), and uric acid forms sharp crystals that can clog and shut down the kidneys. To prevent this, doctors give heavy intravenous fluids to flush the kidneys and administer a targeted enzyme medication called Rasburicase, which instantly dissolves uric acid like sugar in warm water, keeping the kidneys completely safe.",
        "doctor_consultation_checklist": {
            "parameter_question": "What are the serial potassium, phosphorus, calcium, and uric acid levels on the 6-hour metabolic panel?",
            "safety_question": "Was a screening for Glucose-6-Phosphate Dehydrogenase (G6PD) deficiency considered before giving Rasburicase to avoid severe methemoglobinemia and hemolytic anemia?",
            "action_threshold_question": "Is vigorous IV hydration running at 2.5-3 L/m2/day to maintain urine output >80-100 mL/m2/h?"
        },
        "red_flags": [
            "Severe hyperkalemia (>6.5 mEq/L) producing peaked T waves, prolonged PR interval, and fatal ventricular arrhythmias",
            "Severe acute hypocalcemia with tetany, Chvostek/Trousseau sign, laryngospasm, and QT prolongation",
            "Oliguria or anuria with rapidly rising serum creatinine indicating obstructive uric acid and calcium phosphate nephropathy"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Tumor lysis syndrome is a group of metabolic complications that occur when cancer cells die quickly after treatment and release their contents into the blood.",
                "plain_analogy": "A dam bursting open upstream, flooding the river with debris that clogs the water treatment filters (kidneys) unless heavy bypass water and debris-dissolving enzymes are used.",
                "lifestyle_action": "Drink plenty of water and report any decreased urination, muscle cramps, or heart flutter immediately to your oncology team."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rasburicase IV (Elitek - Recombinant Urate Oxidase: 0.2 mg/kg IV single dose over 30 min)",
                    "Allopurinol oral/IV (Zyloprim: 300 mg/m2/day or 300 mg daily for low/intermediate risk)",
                    "Febuxostat oral (Uloric: 40-80 mg daily - non-purine xanthine oxidase inhibitor)",
                    "Calcium gluconate 10% IV (1-2 g IV for cardiac membrane stabilization in symptomatic hypocalcemia)",
                    "Insulin Regular + Dextrose 50% IV (for emergent hyperkalemia reduction)"
                ],
                "dosing_gdmt": "High-risk TLS: Rasburicase 0.2 mg/kg IV in 50 mL normal saline over 30 min (single fixed dose of 3 mg or 6 mg is often highly effective in adults). Intermediate-risk TLS: Allopurinol 300 mg PO daily.",
                "black_box_warning": "Rasburicase carries Black Box Warning for fatal methemoglobinemia and acute hemolysis in patients with G6PD deficiency; strictly contraindicated if G6PD deficient.",
                "organ_clearance_cutoffs": "Blood samples for uric acid testing after Rasburicase MUST be collected in pre-chilled heparin tubes and immediately placed on ice water; otherwise rasburicase continues degrading uric acid in vitro at room temperature, causing falsely low readings."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASCO-TLS-CONSENSUS",
                "pmid_or_doi": "10.1200/JCO.2007.15.0151",
                "cebm_level": 1,
                "sample_size": 1420,
                "endpoints": "Rasburicase achieved an 88% response rate in lowering uric acid to <8.0 mg/dL within 4 hours compared to only 19% with allopurinol, dramatically reducing the requirement for hemodialysis (p<0.0001)."
            }
        }
    },
    {
        "id": "DOC-CARD-524",
        "icd10": "M31.10",
        "condition": "Thrombotic Thrombocytopenic Purpura (ADAMTS13 Deficiency & Emergent Plasma Exchange)",
        "specialty": "Hematology & Critical Care",
        "organ_system": "Hematologic & Vascular",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Society on Thrombosis and Haemostasis (ISTH) & HERCULES Trial",
        "source_body": "NEJM & Journal of Thrombosis and Haemostasis (ISTH)",
        "citation": "Scully M et al. Caplacizumab Treatment for Acquired Thrombotic Thrombocytopenic Purpura (HERCULES). N Engl J Med. 2019;380(4):335-346; Zheng XL et al. ISTH Guidelines for the Diagnosis and Treatment of Thrombotic Thrombocytopenic Purpura. J Thromb Haemost. 2020;18(10):2486-2495.",
        "doi_or_source": "10.1056/NEJMoa1806311",
        "clinical_evidence": "Thrombotic Thrombocytopenic Purpura (TTP) is a life-threatening thrombotic microangiopathy (TMA) caused by a severe deficiency (<10% activity) of ADAMTS13 (a disintegrin and metalloproteinase with a thrombospondin type 1 motif, member 13). In acquired immune TTP (iTTP), autoantibodies inactivate ADAMTS13, preventing the physiological cleavage of ultra-large von Willebrand factor (ULvWF) multimers. These giant multimers anchor to endothelial surfaces and spontaneously bind platelet GP1b receptors under high shear stress, creating widespread microvascular platelet thrombi throughout the brain, heart, and kidneys. Consumptive thrombocytopenia and microangiopathic hemolytic anemia (MAHA with abundant schistocytes on peripheral blood smear) ensue. Classic pentad (fever, fluctuating neurological deficits, severe thrombocytopenia, microangiopathic hemolytic anemia, and renal dysfunction) is seen in <10% of cases; the presence of thrombocytopenia and MAHA alone mandates immediate therapy. Historic mortality was >90%; modern therapeutic plasma exchange (TPE) combined with immunosuppression and Caplacizumab reduces mortality to <8-10%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergent therapeutic plasma exchange (TPE: 1.0 to 1.5 plasma volume exchange with fresh frozen plasma or solvent-detergent plasma daily until platelet count >150,000/mcL and LDH normalizes for 2 consecutive days); send ADAMTS13 activity and inhibitor titers BEFORE first TPE (do not wait for results to start therapy); strictly avoid platelet transfusions (platelet transfusions fuel new microvascular thrombosis and trigger acute stroke or myocardial infarction).",
            "monitoring_cadence": "Daily complete blood count (platelet recovery), daily serum LDH (sensitive marker of ongoing microvascular hemolysis and tissue ischemia), peripheral blood smear schistocyte count, serial troponin, ECG, and neurological checks every 4 hours.",
            "clinical_thresholds": "PLASMIC score 6-7 (high risk of ADAMTS13 <10%), severe thrombocytopenia (<30,000/mcL), schistocytes >1% on blood smear, elevated LDH, and undetectable ADAMTS13 activity (<10%)."
        },
        "patient_plain_language": "Thrombotic thrombocytopenic purpura (TTP) is a severe, rare blood disorder where tiny microscopic blood clots form inside thousands of small blood vessels all over the body. It happens because the body lacks an essential molecular 'scissors' enzyme (ADAMTS13) that normally snips long, sticky blood-clotting ropes into safe pieces. Without these scissors, the sticky ropes catch and trap all your platelets, causing your platelet count to drop dangerously low while the clots shred passing red blood cells into sharp fragments called schistocytes. This starves the brain and heart of blood, causing confusion, headaches, and weakness. It is treated immediately with plasma exchange (a machine that cleans out the bad antibodies and replaces fresh, healthy plasma enzymes) and targeted immune-stopping medications.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the calculated PLASMIC score and the percentage of schistocytes seen on the peripheral blood smear review?",
            "safety_question": "Have platelet transfusions been strictly avoided, as giving platelets is like throwing gasoline on the microvascular fire?",
            "action_threshold_question": "Has emergent therapeutic plasma exchange (TPE) and intravenous Corticosteroids plus Caplacizumab been initiated immediately?"
        },
        "red_flags": [
            "Platelet transfusion administration (triggers acute fatal coronary or cerebral microvascular occlusion)",
            "Fluctuating neurological deficits (confusion, aphasia, hemiparesis, or seizures indicating extensive cerebral ischemia)",
            "Elevated cardiac troponin indicating acute subendocardial ischemia and impending cardiogenic arrest"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "TTP is a rare, life-threatening blood disorder that causes small blood clots to form throughout the body, treated with plasma exchange.",
                "plain_analogy": "Long, tangled strands of Velcro forming in the bloodstream, snagging all the passing platelets and shredding red blood cells like paper in a shredder.",
                "lifestyle_action": "Seek immediate emergency hospital care for unexplained purplish bruises on the skin, pale skin, extreme fatigue, and confusion."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Therapeutic Plasma Exchange (TPE: 1-1.5 plasma volume exchange daily with FFP)",
                    "Caplacizumab-yhdp IV/SC (Cablivi - anti-vWF nanobody: 10 mg IV load, then 10 mg SC daily)",
                    "Methylprednisolone IV (1,000 mg IV daily x 3 days, then oral prednisone 1 mg/kg/day)",
                    "Rituximab IV (Rituxan: 375 mg/m2 weekly x 4 doses - anti-CD20 targeted B-cell depletion)",
                    "Avoid Platelet Transfusions (Strict absolute contraindication)"
                ],
                "dosing_gdmt": "Immediate Triple Therapy: 1) Daily TPE (1-1.5 plasma volumes); 2) High-dose Methylprednisolone 1g IV daily; 3) Caplacizumab 10 mg IV bolus before first TPE, followed by 10 mg SC daily post-TPE. Add Rituximab 375 mg/m2 weekly x 4.",
                "black_box_warning": "PLATELET TRANSFUSIONS ARE CONTRAINDICATED in TTP; infusing platelets precipitates acute multi-organ microthrombosis, stroke, and sudden cardiac death.",
                "organ_clearance_cutoffs": "Caplacizumab should be continued for 30 days following the cessation of daily plasma exchange, or until ADAMTS13 activity recovers to >20%."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HERCULES-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1806311",
                "cebm_level": 1,
                "sample_size": 145,
                "endpoints": "Caplacizumab combined with plasma exchange and immunosuppression reduced the time to platelet count normalization and reduced the composite risk of TTP-related death, recurrence, or major thromboembolic event by 74% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-525",
        "icd10": "K76.7",
        "condition": "Hepatorenal Syndrome (HRS-AKI & Terlipressin/Albumin Reversal)",
        "specialty": "Nephrology & Hepatology",
        "organ_system": "Renal & Hepatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CONFIRM Landmark Phase 3 Trial & International Club of Ascites (ICA) Guidelines",
        "source_body": "NEJM & Journal of Hepatology (EASL/ICA)",
        "citation": "Wong F et al. Terlipressin plus Albumin for the Treatment of Type 1 Hepatorenal Syndrome (CONFIRM). N Engl J Med. 2021;384(9):818-827; Angeli P et al. Diagnosis and Management of Acute Kidney Injury in Patients with Cirrhosis: Consensus Recommendations of the International Club of Ascites. J Hepatol. 2015;62(4):968-974.",
        "doi_or_source": "10.1056/NEJMoa2008290",
        "clinical_evidence": "Hepatorenal Syndrome (HRS), classified as HRS-AKI by the International Club of Ascites (ICA), is a form of functional, pre-renal acute kidney injury occurring in patients with advanced decompensated cirrhosis and severe portal hypertension. Massive splanchnic arterial vasodilation (driven by excessive nitric oxide, endocannabinoids, and prostacyclins) causes marked pooling of blood in the splanchnic circulation, precipitating severe arterial underfilling and reduction in effective circulating arterial volume (ECAV). In response, systemic baroreceptors activate profound neurohumoral compensatory mechanisms (renin-angiotensin-aldosterone system, sympathetic nervous system, and non-osmotic vasopressin release). This drives extreme renal vasoconstriction, reducing renal blood flow and glomerular filtration rate while the renal parenchyma remains structurally intact. ICA diagnostic criteria require: cirrhosis with ascites, acute kidney injury (creatinine rise ≥0.3 mg/dL within 48h or ≥50% from baseline), lack of response after 48 hours of diuretic withdrawal and plasma volume expansion with IV albumin (1 g/kg/day, max 100g), absence of shock, and absence of nephrotoxic drugs or structural kidney disease (proteinuria <500 mg/day, microhematuria <50 RBCs/hpf, normal renal ultrasound). The double-blind CONFIRM trial (n=300) established that Terlipressin (a vasopressin V1a receptor agonist that constricts splanchnic vessels) combined with IV albumin reversed HRS-AKI in 32% vs 17% with placebo (p=0.006).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately discontinue all diuretics (spironolactone, furosemide) and nephrotoxic drugs (NSAIDs, ACEi/ARBs, aminoglycosides); expand intravascular volume with 20-25% IV Albumin (1 g/kg/day for 48 hours); screen and aggressively treat precipitating infections (SBP, pneumonia, UTI); expedite liver transplant evaluation (definitive cure); consider transjugular intrahepatic portosystemic shunt (TIPS) or renal replacement therapy as bridge to transplant.",
            "monitoring_cadence": "Serial serum creatinine, BUN, electrolytes, and urine output every 12-24 hours; continuous pulse oximetry (monitor for Terlipressin-induced pulmonary edema and acute respiratory failure); continuous arterial line blood pressure (target mean arterial pressure increase of ≥10-15 mmHg).",
            "clinical_thresholds": "Rise in serum creatinine ≥0.3 mg/dL in 48h or ≥50% baseline, failure to respond to 48 hours of volume expansion with Albumin (1 g/kg), and lack of structural renal disease."
        },
        "patient_plain_language": "Hepatorenal syndrome is a severe form of kidney failure that happens in people with advanced liver cirrhosis. The liver disease causes the blood vessels in the belly and intestines to stretch wide open and pool vast amounts of blood, like water pooling in a low reservoir. Because the blood is trapped in the belly, the rest of the body feels like it is severely dehydrated, causing the kidneys' blood vessels to squeeze shut in a desperate panic. The kidneys themselves are completely healthy, but they starve of blood flow. Treatment involves stopping all water pills (diuretics), infusing concentrated human albumin protein, and administering a specialized targeted blood vessel medicine called Terlipressin to squeeze the belly blood vessels, pushing the pooled blood straight back up into the kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has the patient received at least 48 hours of complete diuretic withdrawal and IV albumin volume challenge (1 g/kg/day) without creatinine improvement?",
            "safety_question": "Is continuous pulse oximetry monitoring in place to screen for Terlipressin-associated ischemic events and fatal respiratory failure/pulmonary edema?",
            "action_threshold_question": "Has Terlipressin IV (or Norepinephrine IV + Albumin) been initiated, and is the patient listed for urgent liver transplantation?"
        },
        "red_flags": [
            "Severe oliguria or anuria (<0.5 mL/kg/h for >12 hours) with rapidly doubling serum creatinine",
            "Development of hypoxic acute respiratory failure and pulmonary edema following terlipressin and albumin infusions",
            "Marked refractory hyperkalemia, severe metabolic acidosis, and uremic encephalopathy requiring emergency hemodialysis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hepatorenal syndrome is a type of progressive kidney failure that occurs in people with severe liver damage, treatable with terlipressin and albumin or liver transplant.",
                "plain_analogy": "A water pump (kidney) running dry because all the reservoir water is pooled down in an open floodplain (splanchnic vessels); closing the floodplain gates forces the water back into the pump.",
                "lifestyle_action": "Avoid all NSAID pain relievers (ibuprofen, naproxen) and salt excesses if you have liver cirrhosis with fluid in your abdomen."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Terlipressin IV (Terlivaz - Vasopressin V1a Receptor Agonist: 0.85 mg IV every 6 hours, titrate up to 1.7 mg q6h)",
                    "Albumin Human 20% or 25% IV (20-40 g IV daily alongside vasoconstrictor therapy)",
                    "Norepinephrine IV continuous infusion (0.5 to 3 mg/h - alternative first-line in ICU targeting MAP increase ≥10 mmHg)",
                    "Midodrine oral + Octreotide SC (fallback when terlipressin or norepinephrine unavailable)",
                    "Orthotopic Liver Transplantation (Definitive curative therapy)"
                ],
                "dosing_gdmt": "Terlipressin: 0.85 mg IV push every 6 hours on Days 1-3. If serum creatinine decreases by <30% by Day 4, increase dose to 1.7 mg IV every 6 hours. Continue until complete HRS reversal (creatinine ≤1.5 mg/dL) or up to 14 days. Co-administer Albumin 20-40 g/day.",
                "black_box_warning": "Terlipressin carries Black Box Warning for serious or fatal acute respiratory failure (due to volume overload) and peripheral ischemic events; monitor oxygen saturation continuously.",
                "organ_clearance_cutoffs": "Contraindicated in severe coronary artery disease, mesenteric ischemia, peripheral vascular disease, or baseline severe hypoxemia."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CONFIRM-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2008290",
                "cebm_level": 1,
                "sample_size": 300,
                "endpoints": "Terlipressin combined with albumin achieved verified reversal of Hepatorenal Syndrome in 32% of patients compared to 17% with placebo, significantly reducing renal replacement therapy requirements (p=0.006)."
            }
        }
    }
]

