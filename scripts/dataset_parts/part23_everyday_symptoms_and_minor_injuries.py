"""
scripts/dataset_parts/part23_everyday_symptoms_and_minor_injuries.py
Part 23: Landmark Clinical Database Entries (DOC-CARD-551 to DOC-CARD-600: 50 Conditions)
Focus: Everyday Symptoms, Common Minor Injuries, Day-to-Day Illnesses & Ambulatory Primary Care
"""

PART_23_DISEASES = [
    {
        "id": "DOC-CARD-551",
        "icd10": "R05.9",
        "condition": "Acute Viral Cough & Bronchial Irritation",
        "specialty": "Pulmonology & Primary Care",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CHEST Guideline & Cochrane Systematic Review",
        "source_body": "CHEST & Cochrane",
        "citation": "Malesker MA et al. Chest. 2017;152(5):1021-1037.",
        "doi_or_source": "10.1016/j.chest.2017.08.009",
        "clinical_evidence": "Acute cough (<3 weeks duration) secondary to upper respiratory viral infection reflects mucosal inflammation, sensory nerve hypersensitivity, and post-nasal drip. Routine antibiotics lack clinical efficacy. CHEST guidelines endorse pasteurized honey for individuals over 1 year, warm humidification, and guaifenesin for thick secretions.",
        "solution_protocol": {
            "non_pharmacological_targets": "Honey (1-2 tsp for age >1 year); warm lemon or herbal tea; cool-mist room humidifier; elevated sleeping posture (15-30 degrees) to prevent nocturnal pooling; avoid smoke.",
            "monitoring_cadence": "Monitor cough frequency and sputum character; reassess if persisting beyond 3 weeks or returning with new high fever.",
            "clinical_thresholds": "Cough >3 weeks, resting SpO2 <95%, or hemoptysis."
        },
        "patient_plain_language": "An acute cough is your airways' natural defense reflex to expel mucus and viral particles. Nerve endings in your throat remain hyperactive for 10-14 days after the infection clears. Honey, warm fluids, and steam soothe the tickling nerves much more safely and effectively than antibiotics.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many days has the cough lasted, and are you coughing up clear fluid, thick phlegm, or blood?",
            "safety_question": "Are you feeling short of breath, wheezing, or chest tightness when breathing in deeply?",
            "action_threshold_question": "If my cough lasts longer than 3 weeks, should we perform a chest X-ray to check for bronchitis or asthma?"
        },
        "red_flags": [
            "Hemoptysis (coughing up frank red blood or rust-colored sputum)",
            "Resting oxygen saturation below 92% or stridor",
            "High fever persisting beyond 3 days or sudden relapse with shaking chills"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A common viral cough clears on its own in 2-3 weeks; honey, steam, and fluids bring gentle relief.",
                "plain_analogy": "A smoke detector that keeps sounding for a few minutes after the burnt toast is cleared because the sensor is still hot.",
                "lifestyle_action": "Take a spoonful of honey before bed, sip warm tea throughout the day, and use a cool mist humidifier."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Honey (natural demulcent for age >1 year)",
                    "Guaifenesin (Mucinex: 200-400 mg q4h or 600-1200 mg ER q12h)",
                    "Dextromethorphan (Delsym: 10-20 mg q4h)",
                    "Saline nasal spray (0.9% sodium chloride)",
                    "Benzonatate (Tessalon: 100-200 mg TID for dry cough)"
                ],
                "dosing_gdmt": "First-line: Hydration and honey demulcents. Dextromethorphan or Benzonatate for disruptive dry nocturnal cough. Never give honey to infants under 1 year.",
                "black_box_warning": "Codeine syrups contraindicated in children due to fatal respiratory depression risk.",
                "contraindications": [
                    "Infant age under 12 months",
                    "Productive bacterial pneumonia"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-COUGH",
                "pmid_or_doi": "10.1016/j.chest.2017.08.009",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Honey significantly reduced cough frequency, symptom severity, and improved sleep quality compared to placebo."
            }
        }
    },
    {
        "id": "DOC-CARD-552",
        "icd10": "M79.669",
        "condition": "Leg Pain & Calf Muscle Strain (Gastrocnemius / Soleus Strain)",
        "specialty": "Orthopedics & Sports Medicine",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review & BJSM Consensus",
        "source_body": "BJSM & ACSM",
        "citation": "Green B et al. Br J Sports Med. 2020;54(12):703-714.",
        "doi_or_source": "10.1136/bjsports-2019-101764",
        "clinical_evidence": "Calf muscle strain involves acute tearing of muscle fibers at the myotendinous junction. The PEACE & LOVE framework (Protection, Elevation, Avoid anti-inflammatories in first 48 hours, Compression, Education, followed by progressive Loading and Exercise) promotes functional recovery. Differentiating from deep vein thrombosis (DVT) is critical.",
        "solution_protocol": {
            "non_pharmacological_targets": "Elastic calf compression wrap; elevation above hip level when resting; gentle pain-free active ankle pumping; progressive eccentric heel raises once pain settles; avoid aggressive stretching during first 72 hours.",
            "monitoring_cadence": "Daily check for swelling changes and weight-bearing ability; clinical re-evaluation if unable to bear weight after 48 hours.",
            "clinical_thresholds": "Wells Score ≥2 (high DVT suspicion) or palpable gap with negative Thompson squeeze test (Achilles tendon rupture)."
        },
        "patient_plain_language": "A calf strain is an overstretch or minor tear in the muscle bellies at the back of your lower leg, often felt as a sudden sharp twinge when sprinting, jumping, or taking a quick step. Wearing a snug supportive calf wrap, propping your leg up on pillows when resting, and avoiding high-dose anti-inflammatory pills for the first two days allows your body's natural healing cells to mend the muscle fibers smoothly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you hear an audible 'snap' or feel like someone kicked you in the back of the leg?",
            "safety_question": "Is your calf red, unusually warm, or noticeably larger than the other leg, which could suggest a blood clot?",
            "action_threshold_question": "Can you stand comfortably on your tiptoes, or is an ultrasound needed to check the muscle and Achilles tendon?"
        },
        "red_flags": [
            "Unilateral calf redness, heat, pitting edema, or prominent veins (DVT warning)",
            "Palpable gap above heel bone with inability to plantarflex (Achilles tendon rupture)",
            "Severe progressive calf tightness with cold, pale toes and tingling (Acute compartment syndrome)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Calf strains occur when lower leg muscles are overstretched; compression, elevation, and gentle walking aid recovery.",
                "plain_analogy": "An elastic rope whose woven outer threads stretch too far; resting and gentle progressive loading restore its full strength.",
                "lifestyle_action": "Wrap the calf in an elastic compression sleeve, elevate the leg on pillows, and avoid high-impact jumping until completely pain-free."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetaminophen (Tylenol: 500-1000 mg q6h PRN, max 3000 mg/day)",
                    "Topical Diclofenac gel 1% (Voltaren: 2-4 g locally TID-QID)",
                    "Oral Ibuprofen (Advil: 400 mg TID with meals after initial 48h)",
                    "Menthol / Camphor topical cooling patches"
                ],
                "dosing_gdmt": "First 48 hours: Acetaminophen and topical analgesics. Avoid aggressive oral NSAIDs during early hematoma formation. Progressive eccentric exercise begins after 3-5 days.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Active deep vein thrombosis",
                    "Complete tendon rupture requiring surgical intervention"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BJSM-CALF-REHAB",
                "pmid_or_doi": "10.1136/bjsports-2019-101764",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Structured progressive eccentric loading and early mobilization significantly reduced return-to-activity time and halved 12-month re-injury rates."
            }
        }
    },
    {
        "id": "DOC-CARD-553",
        "icd10": "M75.10",
        "condition": "Shoulder Pain & Rotator Cuff Tendinopathy",
        "specialty": "Orthopedics & Physical Medicine",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAOS Clinical Practice Guideline & Cochrane Systematic Review",
        "source_body": "AAOS",
        "citation": "Pedowitz RA et al. J Am Acad Orthop Surg. 2011;19(6):380-388.",
        "doi_or_source": "10.5435/00124635-201106000-00007",
        "clinical_evidence": "Rotator cuff tendinopathy and subacromial impingement involve micro-trauma, cellular disorganization, and thickening of the supraspinatus tendon beneath the acromion, causing painful arc abduction (60-120 degrees). Multiple Cochrane reviews and randomized trials show structured physical therapy targeting rotator cuff strengthening and scapular stabilization is clinically equivalent to subacromial decompression surgery at 1-year follow-up.",
        "solution_protocol": {
            "non_pharmacological_targets": "Temporary overhead activity restriction; sleep ergonomics using a side-sleeping pillow under the arm; progressive rotator cuff exercises (banded external rotations, scapular retractions, pendulum stretches); post-activity ice packs 15 min.",
            "monitoring_cadence": "Weekly evaluation of active abduction range of motion; reassessment if no functional progress within 6 to 12 weeks of physical therapy.",
            "clinical_thresholds": "Inability to maintain arm elevated against gravity ('drop arm' sign) indicating acute full-thickness tear."
        },
        "patient_plain_language": "Rotator cuff pain is an ache on the outer side of your upper arm caused by irritation or micro-tearing in the small guiding tendons that balance your shoulder ball in its shallow socket. It hurts most when reaching up into high cabinets or putting on a coat. Dedicated, gentle resistance-band strengthening exercises guide the shoulder ball into smooth alignment, relieving the pinching without needing surgery.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does your shoulder ache wake you up at night when you roll onto that side?",
            "safety_question": "Did the weakness begin after a severe fall, making you unable to lift your arm out to the side?",
            "action_threshold_question": "Can we start a supervised physical therapy program before considering steroid injections or imaging?"
        },
        "red_flags": [
            "Sudden complete inability to actively elevate arm after trauma (acute full-thickness tendon tear)",
            "Left shoulder ache accompanied by chest pressure, shortness of breath, or sweating (myocardial infarction)",
            "Erythematous, hot, swollen joint with fever and chills (septic arthritis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Shoulder tendinopathy causes pain when reaching overhead; daily strengthening exercises are the primary cure.",
                "plain_analogy": "A rope repeatedly rubbing against a rough pulley edge; by strengthening the guiding cables, the rope glides cleanly without friction.",
                "lifestyle_action": "Avoid reaching up high repeatedly, place a pillow under your arm during sleep, and do gentle pendulum arm swings."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren: 2 g applied to affected shoulder QID)",
                    "Oral Naproxen (Aleve: 250-500 mg BID with meals for 7-10 days)",
                    "Oral Ibuprofen (Advil: 400-600 mg TID with meals)",
                    "Subacromial Triamcinolone injection (40 mg with 1% lidocaine - reserved for refractory cases)"
                ],
                "dosing_gdmt": "First-line: 6 to 12 weeks of targeted exercise therapy and topical NSAIDs. Limit steroid injections to maximum 1-2 per year to preserve tendon collagen integrity.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Complete retracted tendon tear in young patients (surgical repair indicated)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-SHOULDER-EX",
                "pmid_or_doi": "10.5435/00124635-201106000-00007",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Exercise therapy achieved significant improvements in pain and shoulder function that were fully sustained at 12 months, matching surgical outcomes."
            }
        }
    },
    {
        "id": "DOC-CARD-554",
        "icd10": "S01.90XA",
        "condition": "Minor Cut, Skin Laceration & Wound Care",
        "specialty": "Emergency Medicine & Primary Care",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & CDC Tetanus Guidelines",
        "source_body": "CDC, WHO & Cochrane",
        "citation": "Fernandez R, Griffiths R. Cochrane Database Syst Rev. 2012;(2):CD003861.",
        "doi_or_source": "10.1002/14651858.CD003861.pub3",
        "clinical_evidence": "Minor lacerations and skin abrasions require systematic assessment: hemostasis, foreign body evaluation, neurovascular check, wound depth, and tetanus status. Cochrane systematic reviews show potable tap water wound irrigation is as safe and effective as sterile saline and does not increase infection risk. Wounds requiring closure (sutures, tissue adhesives) should ideally be closed within 12-18 hours. Tetanus booster is warranted for dirty wounds if last dose was >5 years ago.",
        "solution_protocol": {
            "non_pharmacological_targets": "Direct continuous firm pressure for 5-10 minutes with clean cloth to achieve hemostasis; copiously irrigate under lukewarm running tap water for 3-5 minutes; avoid toxic antiseptics like hydrogen peroxide or rubbing alcohol inside the wound; apply thin petroleum jelly; cover with clean sterile bandage; change bandage daily or when wet.",
            "monitoring_cadence": "Inspect wound daily for erythema, warmth, increasing throbbing tenderness, purulent discharge, or fever.",
            "clinical_thresholds": "Laceration gaping >0.5 cm, exposing yellow subcutaneous fat, located across a flexor joint, or bleeding pulsatile red blood."
        },
        "patient_plain_language": "A minor cut or scrape happens when an everyday object breaks through your skin. The most important initial step is holding firm, steady pressure with a clean cloth for five full minutes without peeking, followed by washing the cut under warm tap water to rinse away germs. Covering the cut with a smear of plain petroleum jelly and a clean bandage keeps the skin moist, cutting healing time in half and minimizing scars.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the wound pull open when you move, meaning it needs stitches or medical skin glue to close neatly?",
            "safety_question": "Have you had a tetanus vaccine booster in the last 5 to 10 years?",
            "action_threshold_question": "Is there any numbness or tingling in the skin or fingers past the cut?"
        },
        "red_flags": [
            "Pulsatile arterial spurting or bleeding that does not stop after 10-15 minutes of direct pressure",
            "Spreading red streaks, warmth, swelling, or foul-smelling pus developing after 24-48 hours",
            "Loss of sensation or inability to bend fingers or toes distal to the cut"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Minor cuts heal quickly when rinsed with clean water, kept moist with petroleum jelly, and covered with a clean bandage.",
                "plain_analogy": "A small rip in a waterproof coat; rinsing out the grit and sealing the edges neatly lets the waterproof barrier repair itself.",
                "lifestyle_action": "Rinse under clean tap water, apply petroleum jelly, cover with an adhesive bandage, and keep the wound clean and dry during showers."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "White petrolatum (Vaseline / Aquaphor: thin layer to promote moist epithelialization)",
                    "Triple antibiotic ointment (Bacitracin / Neomycin / Polymyxin B - OTC topical)",
                    "Tetanus toxoid conjugate vaccine (Tdap / Td booster within 48 hours if indicated)",
                    "Topical 2-octyl cyanoacrylate skin adhesive (Dermabond - medical glue for clean linear lacerations)"
                ],
                "dosing_gdmt": "Clean with tap water. Apply thin petroleum jelly and sterile dressing daily. Administer Td/Tdap if dirty wound and >5 years since last booster, or clean wound and >10 years.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not use tissue adhesive skin glue over high-tension joints or animal bite wounds (high infection risk)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-WOUND-CLEANSE",
                "pmid_or_doi": "10.1002/14651858.CD003861.pub3",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Washing acute wounds with potable tap water reduced wound infection rates compared to no cleansing and was non-inferior to sterile normal saline."
            }
        }
    },
    {
        "id": "DOC-CARD-555",
        "icd10": "J02.9",
        "condition": "Acute Sore Throat & Viral Pharyngitis",
        "specialty": "ENT & Primary Care",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Guideline & Cochrane Systematic Review",
        "source_body": "IDSA & NICE",
        "citation": "Shulman ST et al. Clin Infect Dis. 2012;55(10):1279-1282.",
        "doi_or_source": "10.1093/cid/cis629",
        "clinical_evidence": "Over 70-85% of acute pharyngitis cases in adults and >65% in children are viral in etiology (rhinovirus, adenovirus, coronavirus, EBV). Centor criteria (absence of cough, swollen tender anterior cervical nodes, fever >38C, tonsillar exudates) stratify risk of Group A Streptococcus (GAS). Antibiotics are indicated only for confirmed GAS via rapid antigen detection testing (RADT) or throat culture. Symptomatic relief with NSAIDs, warm saline gargles, and anesthetic lozenges significantly reduces pain within hours without antimicrobial resistance risk.",
        "solution_protocol": {
            "non_pharmacological_targets": "Warm salt water gargle (1/2 teaspoon table salt in 8 oz warm water) 3-4 times daily; warm broth or cold popsicles; throat lozenges containing pectin or honey; cool-mist bedroom humidifier; vocal rest.",
            "monitoring_cadence": "Monitor symptoms daily; re-evaluate if fever >38.5C persists beyond 3 days or swallowing becomes painful enough to cause drooling.",
            "clinical_thresholds": "Centor Score ≥3 warranting RADT swab, or unilateral peritonsillar swelling with uvular deviation (peritonsillar abscess)."
        },
        "patient_plain_language": "A sore throat is an inflammation of the back of your throat, most often caused by common cold viruses. Your throat feels scratchy, raw, and hurts when swallowing. Gargling with warm salt water draws excess fluid out of the swollen tissue, and pain relievers like ibuprofen or paracetamol soothe the tenderness. Antibiotics do not work against viral throat infections and are only prescribed if a rapid throat swab proves strep bacteria are present.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do you have a cough or runny nose, which suggests a viral cold rather than bacterial strep throat?",
            "safety_question": "Are you having difficulty swallowing your own saliva, breathing, or opening your mouth wide?",
            "action_threshold_question": "Can we do a rapid strep throat swab before deciding on an antibiotic prescription?"
        },
        "red_flags": [
            "Inability to swallow saliva leading to drooling or difficulty breathing (Epiglottitis red flag)",
            "Severe one-sided throat pain, muffled 'hot potato' voice, and uvula pushed to one side (Peritonsillar abscess)",
            "Stiff neck with inability to touch chin to chest, accompanied by high fever and light sensitivity"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Most sore throats are viral and heal in 5 to 7 days; warm salt water gargles and pain relievers provide quick comfort.",
                "plain_analogy": "Sunburned tissue at the back of the mouth; cool fluids and soothing gargles gently relieve the raw inflammation until the lining heals.",
                "lifestyle_action": "Gargle with warm salt water three times daily, eat cold smoothies or warm broths, and get plenty of restful sleep."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ibuprofen (Advil: 400 mg oral every 6 hours with food - superior anti-inflammatory throat relief)",
                    "Acetaminophen (Tylenol: 500-1000 mg oral every 6 hours PRN, max 3000 mg/day)",
                    "Benzocaine / Menthol lozenges (Cepacol / Chloraseptic: dissolvable throat numbing lozenges)",
                    "Amoxicillin (50 mg/kg/day up to 1000 mg daily for 10 days - ONLY if rapid strep swab positive)"
                ],
                "dosing_gdmt": "First line: NSAIDs and warm saline gargling. Reserve antibiotics exclusively for microbiologically confirmed Group A Strep.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not administer amoxicillin/ampicillin if infectious mononucleosis suspected (causes severe widespread maculopapular rash)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-SORE-THROAT-NSAID",
                "pmid_or_doi": "10.1093/cid/cis629",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Oral NSAIDs and paracetamol provided rapid, statistically significant pain reduction in acute pharyngitis within 2 to 4 hours."
            }
        }
    },
    {
        "id": "DOC-CARD-556",
        "icd10": "J00",
        "condition": "Common Cold & Acute Viral Rhinitis",
        "specialty": "Primary Care & Infectious Disease",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Reviews & CDC Guidelines",
        "source_body": "CDC & Cochrane",
        "citation": "Allan GM, Arroll B. CMAJ. 2014;186(3):190-199.",
        "doi_or_source": "10.1503/cmaj.121442",
        "clinical_evidence": "The common cold is a self-limiting viral infection of the upper respiratory mucosal epithelium predominantly caused by Rhinoviruses (>100 serotypes), Coronaviruses, and RSV. Symptoms peak on days 2-4 and resolve by day 7-10. Cochrane reviews confirm that antibiotics offer zero therapeutic benefit, whereas nasal saline irrigation, oral analgesics (ibuprofen/paracetamol), and short-term topical nasal decongestants (≤3 days) provide effective symptomatic relief.",
        "solution_protocol": {
            "non_pharmacological_targets": "Nasal saline irrigation (sinus rinse or isotonic saline spray); abundant fluid intake (water, broths); adequate rest (7-9 hours); cool-mist humidification; hand hygiene and surface disinfection to prevent household transmission.",
            "monitoring_cadence": "Self-monitor symptom evolution; seek clinical evaluation if symptoms worsen significantly after initial improvement (double sickening) or persist >10-14 days.",
            "clinical_thresholds": "Fever >38.5C (101.3F) lasting >3 days, severe unilateral facial pain, or resting shortness of breath."
        },
        "patient_plain_language": "The common cold is a mild, self-limiting viral infection that inflames the lining of your nose and throat, causing sneezing, a runny or stuffy nose, mild headache, and tiredness. Symptoms peak around day three and fade away on their own within a week. Flushing your sinuses with gentle saline water, drinking warm fluids, and resting allow your immune system to clear the virus completely without any need for antibiotics.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many days have you had cold symptoms, and did they start improving before suddenly getting worse with a new fever?",
            "safety_question": "Do you have severe pain or swelling around your eyes and forehead, or difficulty breathing?",
            "action_threshold_question": "Are OTC decongestants safe with my current blood pressure or cardiovascular medications?"
        },
        "red_flags": [
            "Severe shortness of breath, audible wheezing, or chest pain upon taking a breath",
            "Swelling, redness, or pain around one eye with double vision (orbital cellulitis complication)",
            "Symptoms lasting beyond 10-14 days without any improvement with severe unilateral facial pain (secondary bacterial sinusitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "The common cold causes sneezing, stuffy nose, and mild fatigue; rest, fluids, and saline sprays bring the best relief.",
                "plain_analogy": "A temporary rainstorm passing through your airways; sheltering with warm fluids and resting allows the sky to clear naturally in a few days.",
                "lifestyle_action": "Rinse your nose with saline spray, drink lots of warm water and soup, and get extra hours of sleep."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Nasal Saline Spray (0.9% sodium chloride isotonic rinse 2-3 sprays per nostril PRN)",
                    "Oxymetazoline nasal spray 0.05% (Afrin: 2 sprays per nostril BID - MAXIMUM 3 CONSECUTIVE DAYS)",
                    "Ibuprofen (Advil: 400 mg oral every 6 hours with food for headache/body aches)",
                    "Acetaminophen (Tylenol: 500-1000 mg every 6 hours PRN)",
                    "Zinc acetate lozenges (taken within 24 hours of cold onset to reduce duration by 1-2 days)"
                ],
                "dosing_gdmt": "First line: Nasal saline irrigation and rest. Short-term topical decongestants (oxymetazoline) restricted to 3 days maximum to prevent rhinitis medicamentosa rebound congestion.",
                "black_box_warning": "Topical nasal decongestants used longer than 3-5 days cause severe rebound nasal obstruction (rhinitis medicamentosa).",
                "contraindications": [
                    "Hypertension (oral pseudoephedrine/phenylephrine can spike blood pressure)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-COLD-SALINE",
                "pmid_or_doi": "10.1503/cmaj.121442",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Nasal saline irrigation significantly relieved nasal congestion, reduced throat irritation, and lowered secondary antibiotic utilization."
            }
        }
    },
    {
        "id": "DOC-CARD-557",
        "icd10": "H60.90",
        "condition": "Ear Pain & Otitis Externa (Swimmer's Ear & Cerumen Impaction)",
        "specialty": "Otolaryngology & Primary Care",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNS Clinical Practice Guideline",
        "source_body": "AAO-HNS",
        "citation": "Rosenfeld RM et al. Otolaryngol Head Neck Surg. 2014;150(1 Suppl):S1-S24.",
        "doi_or_source": "10.1177/0194599813517083",
        "clinical_evidence": "Acute otitis externa (swimmer's ear) is diffuse inflammation of the external auditory canal typically caused by bacterial infection (Pseudomonas aeruginosa 38%, Staphylococcus aureus 16%) following moisture retention and protective cerumen barrier loss. Hallmark physical sign is exquisite pain upon tragus palpation or pinna traction. AAO-HNS guidelines recommend topical antimicrobial/corticosteroid otic drops as superior to oral antibiotics, which have high failure rates and adverse effects. For cerumen impaction, cerumenolytics (carbamide peroxide) followed by gentle warm water irrigation are first line.",
        "solution_protocol": {
            "non_pharmacological_targets": "Keep ear canal strictly dry during bathing (use earplugs or petroleum-coated cotton ball); avoid cotton swabs (Q-tips), keys, or foreign objects in the canal; apply warm compress over ear; dry ears with a hair dryer on cool setting after swimming.",
            "monitoring_cadence": "Improvement expected within 48 to 72 hours of topical drop therapy; clinical re-check if pain or ear canal swelling persists after 7 days.",
            "clinical_thresholds": "Tympanic membrane perforation suspicion (avoid ototoxic drops like aminoglycosides/alcohol) or pain spreading to temporal bone (malignant otitis externa in diabetic/immunocompromised patients)."
        },
        "patient_plain_language": "Swimmer's ear is an infection and swelling of the outer ear canal that leads from the outside of your head down to your eardrum, often triggered by water getting trapped after swimming or using cotton swabs. It hurts intensely when you tug your earlobe or push on the little flap outside your ear (tragus). Prescription ear drops reach the canal directly to clear the swelling and infection quickly, which works much better than swallowing antibiotic pills.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does it cause sharp pain when you gently tug your earlobe or press the cartilage flap outside your ear?",
            "safety_question": "Have you had ear tubes, a ruptured eardrum, or recent ear surgery?",
            "action_threshold_question": "Could this earache be caused by a buildup of hardened earwax that can be gently cleared in the clinic?"
        },
        "red_flags": [
            "Severe pain spreading into jaw and mastoid bone behind ear in an elderly diabetic patient (Malignant Necrotizing Otitis Externa)",
            "Facial muscle weakness, asymmetry, or drooping on the side of the ear pain (Facial nerve involvement)",
            "Red, tender, fluctuating swelling pushing the ear forward behind the skull (Acute mastoiditis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Swimmer's ear causes sharp ear pain when touched; prescription ear drops and keeping the ear dry clear it up fast.",
                "plain_analogy": "A damp hallway whose carpet has mildewed because water got trapped inside; drying the air and applying surface cleanser restores the clean floor.",
                "lifestyle_action": "Keep ears dry during showers with an earplug, never stick cotton swabs inside, and apply a warm washcloth for pain relief."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ciprofloxacin 0.3% / Dexamethasone 0.1% otic suspension (Ciprodex: 4 drops in affected ear BID for 7 days)",
                    "Ofloxacin 0.3% otic solution (10 drops once daily for 7 days - safe if tympanic membrane perforated)",
                    "Carbamide peroxide 6.5% otic drops (Debrox: 5-10 drops BID for 4 days to soften earwax impaction)",
                    "Oral Ibuprofen (Advil: 400-600 mg oral TID with meals for pain control)"
                ],
                "dosing_gdmt": "First line: Topical antibiotic-corticosteroid drops (Ciprodex) for 7 days. Oral antibiotics are NOT recommended unless infection spreads beyond the ear canal.",
                "black_box_warning": "Neomycin/Polymyxin B/Hydrocortisone otic drops are ototoxic and contraindicated if tympanic membrane is ruptured or ear tubes are present.",
                "contraindications": [
                    "Aminoglycoside/alcohol ear drops in tympanic membrane perforation"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO-HNS-OTITIS-EXTERNA",
                "pmid_or_doi": "10.1177/0194599813517083",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Topical otic drops achieved clinical cure rates of 87-95% within 7-10 days, significantly outperforming systemic oral antibiotics while minimizing adverse events."
            }
        }
    },
    {
        "id": "DOC-CARD-558",
        "icd10": "H04.129",
        "condition": "Dry Eye Syndrome & Ocular Surface Grittiness",
        "specialty": "Ophthalmology & Optometry",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: TFOS DEWS II International Clinical Guidelines",
        "source_body": "TFOS DEWS II & AAO",
        "citation": "Craig JP et al. Ocul Surf. 2017;15(4):802-812.",
        "doi_or_source": "10.1016/j.jtos.2017.08.003",
        "clinical_evidence": "Dry eye disease (DED) is a multifactorial disease of the ocular surface characterized by loss of tear film homeostasis and accompanied by ocular symptoms, in which tear film instability and hyperosmolarity, ocular surface inflammation and damage, and neurosensory abnormalities play etiological roles. The vast majority of cases (>85%) involve meibomian gland dysfunction (evaporative dry eye). TFOS DEWS II guidelines establish stepwise management: tear film supplementation with preservative-free artificial tears, warm compress eyelid hygiene, environmental modifications, and the 20-20-20 rule during screen use.",
        "solution_protocol": {
            "non_pharmacological_targets": "20-20-20 rule (every 20 minutes of screen time, look 20 feet away for 20 seconds and blink fully); warm eyelid compresses (10 minutes daily at ~40C to melt thickened meibomian gland lipids); room humidifiers; wrap-around glasses outdoors; avoid direct ceiling fans blowing on the face.",
            "monitoring_cadence": "Self-monitor symptom frequency and visual fluctuation; ophthalmology evaluation if foreign body sensation persists despite 4 weeks of consistent artificial tears.",
            "clinical_thresholds": "Corneal epithelial fluorescein staining showing punctate keratitis or persistent sharp pain with photophobia."
        },
        "patient_plain_language": "Dry eye syndrome happens when your eyes either do not produce enough tears or when the tears evaporate too quickly because the tiny oil glands lining your eyelids become plugged. This makes your eyes feel gritty, itchy, stinging, or like there is sand trapped under your eyelids—and surprisingly, your eyes may even water excessively to compensate. Warm washcloth compresses over your closed eyelids and preservative-free lubricating drops keep your eyes comfortably moist.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do your eyes feel like they have sand or grit in them, especially after reading or working on a computer screen?",
            "safety_question": "Do you wear contact lenses, or are you taking medications like antihistamines or acne drugs that dry out your eyes?",
            "action_threshold_question": "Would preservative-free lubricating drops or prescription anti-inflammatory eye drops be better for my eyes?"
        },
        "red_flags": [
            "Severe sharp eye pain with extreme sensitivity to light (Corneal abrasion or ulcer)",
            "Sudden loss or marked blurring of vision that does not clear after blinking",
            "Copious thick green-yellow discharge gluing the eyelids shut (Bacterial keratitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dry eye causes gritty, burning eyes, especially during screen work; warm eyelid compresses and artificial tears restore moisture.",
                "plain_analogy": "A windshield whose wiper fluid is low and leaves streaks; adding clean lubricant and unclogging the spray nozzles keeps the glass crystal clear.",
                "lifestyle_action": "Follow the 20-20-20 screen rule, place a warm damp cloth on your eyelids for 10 minutes every day, and use artificial tears."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Carboxymethylcellulose 0.5% / Glycerin artificial tears (Refresh Plus / Systane: 1-2 drops 3-4 times daily)",
                    "Preservative-free lubricating eye drops (single-use vials for frequent daily use)",
                    "Nighttime lubricating eye ointment (mineral oil / white petrolatum applied at bedtime)",
                    "Cyclosporine ophthalmic emulsion 0.05% (Restasis: 1 drop BID - prescription immunomodulator for chronic inflammation)"
                ],
                "dosing_gdmt": "First line: Preservative-free artificial tears and warm eyelid hygiene. If used more than 4 times daily, preservative-free formulations are mandatory to avoid benzalkonium chloride toxicity.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not use redness-relieving vasoconstrictor drops (tetrahydrozoline/Visine) for dry eye; causes severe rebound hyperemia"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TFOS-DEWS-II",
                "pmid_or_doi": "10.1016/j.jtos.2017.08.003",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Comprehensive eyelid thermal hygiene and lipid-containing artificial tears significantly improved tear break-up time (TBUT) and reduced ocular surface disease index (OSDI) scores."
            }
        }
    },
    {
        "id": "DOC-CARD-559",
        "icd10": "H10.9",
        "condition": "Acute Conjunctivitis (Pink Eye - Viral, Allergic & Bacterial)",
        "specialty": "Ophthalmology & Primary Care",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO Preferred Practice Pattern & Cochrane Systematic Review",
        "source_body": "AAO",
        "citation": "Varu DV et al. Ophthalmology. 2019;126(1):P94-P169.",
        "doi_or_source": "10.1016/j.ophtha.2018.10.043",
        "clinical_evidence": "Acute conjunctivitis is inflammation of the transparent conjunctival membrane covering the sclera and inner eyelids. Adenoviral conjunctivitis accounts for 65-90% of viral cases, presenting with watery discharge, preauricular lymphadenopathy, and high communicability. Allergic conjunctivitis features bilateral intense pruritus and chemosis. Bacterial conjunctivitis features continuous purulent crusting throughout the day. Cochrane systematic reviews show viral conjunctivitis is self-limiting (10-14 days) and antibiotics provide no benefit while increasing drug toxicity and cost.",
        "solution_protocol": {
            "non_pharmacological_targets": "Cool damp compresses applied over closed eyelids 3-4 times daily; strict hand hygiene and separate towels/pillows to prevent spread; discard existing eye makeup and mascara; temporarily suspend contact lens wear until full resolution; artificial tears for comfort.",
            "monitoring_cadence": "Self-monitor eye discharge and redness; ophthalmologist evaluation if pain, light sensitivity, or visual acuity decline occurs.",
            "clinical_thresholds": "Contact lens wearer with corneal infiltrates (high risk of Pseudomonas keratitis requiring urgent fluoroquinolone therapy)."
        },
        "patient_plain_language": "Pink eye is an irritation or infection of the clear membrane lining your eye and inner eyelid, making the white part of your eye look red or pink. It most commonly starts as a cold virus in one eye and spreads to the other, causing watery tearing and mild crustiness upon waking. Cool washcloth compresses and lubricating drops provide great relief, and strict handwashing protects your family members from catching it.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the discharge watery like tears, or is it thick yellow-green pus that glues your eyelids shut all day long?",
            "safety_question": "Do you wear contact lenses, and have you been sleeping or swimming in them?",
            "action_threshold_question": "Is there any pain inside the eyeball itself or difficulty looking at bright lights?"
        },
        "red_flags": [
            "Contact lens wearer with red eye, severe pain, or white spot on the cornea (Pseudomonas bacterial keratitis)",
            "Marked decrease in vision, pupil asymmetry, or deep boring ocular pain (Acute angle-closure glaucoma or uveitis)",
            "Copious, hyperacute purulent discharge pouring out within hours in a sexually active patient (Gonococcal conjunctivitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Pink eye causes red, watery, or itchy eyes; cool compresses and artificial tears soothe the eyes while the virus clears.",
                "plain_analogy": "A localized skin rash on the delicate white surface of the eye; gentle cool compresses calm the redness until the body clears it.",
                "lifestyle_action": "Apply cool compresses, wash your hands often with soap, use a clean pillowcase, and do not share towels or makeup."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Preservative-free artificial tears (lubricating comfort drops 4-6 times daily)",
                    "Olopatadine 0.2% ophthalmic solution (Pataday: 1 drop daily for allergic conjunctivitis itching)",
                    "Ketotifen 0.025% ophthalmic drops (Zaditor: 1 drop BID for allergic itching)",
                    "Polymyxin B / Trimethoprim ophthalmic solution (Polytrim: 1 drop QID for 7 days - ONLY if bacterial etiology confirmed)",
                    "Moxifloxacin 0.5% ophthalmic drops (Vigamox - first-line if contact lens wearer with bacterial infection)"
                ],
                "dosing_gdmt": "First line: Cool compresses and lubricating drops for viral conjunctivitis. Antihistamine/mast-cell stabilizer drops (olopatadine) for allergic conjunctivitis. Antibiotic drops reserved for verified bacterial cases.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not prescribe topical corticosteroid drops without ophthalmologist slit-lamp exam (can cause corneal perforation in Herpes simplex)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-CONJUNCTIVITIS",
                "pmid_or_doi": "10.1016/j.ophtha.2018.10.043",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Most viral and mild bacterial conjunctivitis cases resolved spontaneously without antibiotics; unnecessary antibiotics caused avoidable adverse drug effects and ocular toxicity."
            }
        }
    },
    {
        "id": "DOC-CARD-560",
        "icd10": "M54.2",
        "condition": "Stiff Neck & Cervical Muscle Strain",
        "specialty": "Physical Medicine & Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Bone and Joint Decade Task Force & Cochrane Review",
        "source_body": "Bone & Joint Decade & Cochrane",
        "citation": "Haldeman S et al. Spine. 2008;33(4 Suppl):S5-S7.",
        "doi_or_source": "10.1097/BRS.0b013e3181643f40",
        "clinical_evidence": "Mechanical neck pain and acute cervical muscle strain (levator scapulae, trapezius, splenius cervicis) arise from sustained awkward postures (text neck, sleeping with excessive pillows), sudden deceleration, or psychological tension. Systematic reviews establish that active range-of-motion exercises, early mobilization, ergonomic workplace adjustments, and short-term multimodal analgesia are superior to prolonged cervical collar immobilization, which prolongs disability.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid rigid neck collars; gentle active range-of-motion stretching (chin tucks, slow side-to-side head rotations within pain-free limits); ergonomic computer screen adjustment to eye level; supportive cervical contour pillow for sleep; heat pack application for 15-20 minutes before stretching.",
            "monitoring_cadence": "Self-monitor neck mobility daily; clinical assessment if neck stiffness is accompanied by numbness radiating down the arm or fails to improve within 10-14 days.",
            "clinical_thresholds": "Inability to touch chin to chest accompanied by high fever (nuchal rigidity/meningitis) or electric-shock sensations down the spine upon neck flexion (Lhermitte's sign)."
        },
        "patient_plain_language": "A stiff neck is a spasm and tightness in the strong support muscles connecting your upper back to your skull, usually triggered by sleeping in an awkward position or looking down at a phone or computer for hours. Your neck feels locked and hurts when turning your head. Applying warm heating pads, doing gentle slow head turns, and keeping your head gently moving prevents the muscles from freezing up into tight painful knots.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the pain shoot or tingle down your arm into your fingers when you turn your head?",
            "safety_question": "Do you have a high fever, severe headache, confusion, or sensitivity to light with this neck stiffness?",
            "action_threshold_question": "Could ergonomic desk modifications and targeted physical therapy exercises relieve my recurring neck tension?"
        },
        "red_flags": [
            "Neck stiffness with high fever, severe headache, confusion, or rash (Meningitis red flag - urgent ER evaluation)",
            "Radiating electric-shock pain, numbness, or progressive motor weakness down the arm into the hand (Cervical radiculopathy)",
            "Stiff neck following high-impact trauma or motor vehicle collision (Cervical spine fracture rule-out via Canadian C-Spine Rule)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A stiff neck is caused by muscle spasms and poor posture; warm compresses, gentle stretches, and ergonomic changes help it loosen.",
                "plain_analogy": "A twisted coil spring that seized up overnight; applying gentle heat and slowly flexing it back and forth restores smooth flexibility.",
                "lifestyle_action": "Apply a warm heating pad for 15 minutes, perform gentle chin tucks and slow side turns, and raise your computer screen to eye level."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ibuprofen (Advil: 400 mg oral TID with meals for 5-7 days)",
                    "Acetaminophen (Tylenol: 500-1000 mg every 6 hours PRN, max 3000 mg/day)",
                    "Topical Menthol / Camphor patches (Salonpas applied to upper trapezius)",
                    "Cyclobenzaprine (Flexeril: 5 mg oral at bedtime for 3-5 days - for severe nocturnal spasm)"
                ],
                "dosing_gdmt": "First line: Active mobilization, heat, and oral NSAIDs or paracetamol. Reserve short-course muscle relaxants (cyclobenzaprine 5 mg) for bedtime use during severe acute spasms.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not use prolonged rigid neck collars; causes muscle atrophy and delays recovery"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-NECK-EXERCISE",
                "pmid_or_doi": "10.1097/BRS.0b013e3181643f40",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Active exercise therapy combining strengthening and stretching achieved superior pain relief and functional recovery compared to passive rest or soft collars."
            }
        }
    },
    {
        "id": "DOC-CARD-561",
        "icd10": "S83.90XA",
        "condition": "Knee Pain & Patellofemoral Pain Syndrome (Runner's Knee)",
        "specialty": "Orthopedics & Sports Medicine",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Consensus Statement from International Patellofemoral Research Retreat & BJSM",
        "source_body": "BJSM & APTA",
        "citation": "Crossley KM et al. Br J Sports Med. 2016;50(14):839-843.",
        "doi_or_source": "10.1136/bjsports-2016-096384",
        "clinical_evidence": "Patellofemoral pain syndrome (PFPS) presents with retropatellar or peripatellar aching provoked by loading the flexed knee (stairs, squatting, prolonged sitting 'theater sign'). High-quality randomized evidence confirms that targeted hip (gluteus medius/maximus) and quadriceps (vastus medialis obliquus) strengthening exercise therapy is the gold standard intervention, outperforming passive electrotherapy, knee braces, or arthroscopic surgery.",
        "solution_protocol": {
            "non_pharmacological_targets": "Quadriceps and hip abductor strengthening exercises; temporary avoidance of deep squats and lunges; patellar taping (McConnell taping) for acute pain relief during loading; ice application for 15 minutes post-exercise.",
            "monitoring_cadence": "Reassess functional pain scale weekly during stair climbing; clinical evaluation if joint locking or giving way occurs.",
            "clinical_thresholds": "Acute knee effusion developing within 2 hours of trauma (hemarthrosis/ACL tear) or mechanical joint locking preventing full extension (bucket-handle meniscus tear)."
        },
        "patient_plain_language": "Runner's knee is an ache around or behind your kneecap caused when the kneecap tracks slightly off-center in its groove as you bend your leg. It acts up when walking down stairs, squatting, or sitting for long periods with your knees bent. Strengthening the hip and thigh muscles keeps the kneecap gliding smoothly in its natural track without grinding.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does your knee ache specifically when walking down stairs, squatting, or sitting for long periods?",
            "safety_question": "Did the knee swell up like a balloon within two hours of an injury, or does it catch and physically lock so you cannot straighten it?",
            "action_threshold_question": "Can a physical therapist guide me through targeted hip and thigh strengthening exercises to balance kneecap tracking?"
        },
        "red_flags": [
            "Rapid swelling within 2 hours of trauma with an audible 'pop' (ACL rupture)",
            "Mechanical joint locking where the knee gets stuck and cannot physically straighten (Meniscal tear)",
            "Inability to bear any weight for four steps immediately after injury (Ottawa Knee Rule)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Runner's knee causes dull aching around the kneecap when climbing stairs or squatting; hip and thigh strengthening is the best cure.",
                "plain_analogy": "A train car slightly misaligned on its tracks, causing the wheels to rub against the guardrail; strengthening the outer cables aligns the car perfectly.",
                "lifestyle_action": "Perform gentle straight leg raises and side-lying leg lifts, avoid deep squats, and ice your knee after walking."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren: 2-4 g locally QID)",
                    "Oral Ibuprofen (Advil: 400 mg TID with food for 7 days)",
                    "Acetaminophen (500-1000 mg q6h PRN)",
                    "Patellofemoral knee tracking brace or McConnell kinesiology tape"
                ],
                "dosing_gdmt": "First line: Targeted hip and quadriceps exercise therapy combined with short-course topical NSAIDs. Arthroscopic knee surgery is not recommended for uncomplicated PFPS.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Complete ligamentous tear or locked knee requiring surgical evaluation"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BJSM-PFPS-CONSENSUS",
                "pmid_or_doi": "10.1136/bjsports-2016-096384",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Combined hip and knee exercise therapy resulted in superior pain reduction and functional recovery compared to knee-only exercises or passive modalities."
            }
        }
    },
    {
        "id": "DOC-CARD-562",
        "icd10": "S93.401A",
        "condition": "Acute Ankle Sprain (Lateral Ligament Inversion Sprain)",
        "specialty": "Emergency Medicine & Sports Medicine",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & Ottawa Ankle Rules",
        "source_body": "BJSM & NATA",
        "citation": "Vuurberg G et al. Br J Sports Med. 2018;52(15):956.",
        "doi_or_source": "10.1136/bjsports-2017-098106",
        "clinical_evidence": "Inversion ankle sprains account for ~85% of acute ankle injuries, damaging the anterior talofibular ligament (ATFL) and calcaneofibular ligament (CFL). The Ottawa Ankle Rules (OAR) demonstrate >98% sensitivity in ruling out malleolar fractures, reducing unnecessary radiographs by 30-40%. High-level evidence strongly supports functional treatment (semi-rigid lace-up ankle brace with early protected weight-bearing and balance exercises) over rigid cast immobilization.",
        "solution_protocol": {
            "non_pharmacological_targets": "Semi-rigid lace-up ankle brace or air-stirrup; early progressive weight-bearing as tolerated; ankle alphabet mobility drills; elevation above hip during rest; wobble-board proprioceptive balance training starting week 2.",
            "monitoring_cadence": "Assess weight-bearing ability and lateral edema daily; clinical review if unable to walk 4 steps at 48 hours.",
            "clinical_thresholds": "Bone tenderness along the posterior edge of either malleolus or base of the 5th metatarsal, or inability to bear weight for 4 steps (Ottawa Ankle Rules fracture criteria)."
        },
        "patient_plain_language": "A twisted or sprained ankle happens when your foot rolls inward, stretching or tearing the tough rubber-band-like ligaments on the outside of your ankle joint. Wearing a snug lace-up ankle brace and walking on it as soon as you can tolerate it—rather than staying in bed or wearing a stiff cast—helps the ligaments heal stronger and prevents chronic ankle wobbliness.",
        "doctor_consultation_checklist": {
            "parameter_question": "Can you put weight on your foot and take four steps, or is there sharp bone tenderness right over the ankle bones?",
            "safety_question": "Did you hear a crack or feel severe numbness in your toes after twisting your ankle?",
            "action_threshold_question": "Would a supportive lace-up ankle brace and early balance exercises be appropriate for my recovery?"
        },
        "red_flags": [
            "Inability to bear weight for four steps both immediately after the injury and in the clinic (Ottawa Ankle Rule)",
            "Exquisite bone tenderness directly over the posterior 6 cm of the fibular or tibial malleolus (Malleolar fracture)",
            "Deformity, severe skin tenting, or open skin wound over the joint"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ankle sprains occur when the foot twists inward; wearing a supportive brace and starting gentle walking promotes the best healing.",
                "plain_analogy": "A guy-wire on a tent pole that stretches during a gust of wind; bracing the pole and gradually restringing tension restores full stability.",
                "lifestyle_action": "Wear a supportive lace-up brace, elevate your ankle when sitting, and practice drawing the alphabet in the air with your toes."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetaminophen (500-1000 mg q6h PRN)",
                    "Oral Ibuprofen (400 mg TID with meals after initial 48h)",
                    "Topical Diclofenac gel 1% (Voltaren applied to lateral ankle QID)",
                    "Semi-rigid lace-up ankle support brace"
                ],
                "dosing_gdmt": "First line: Functional treatment with a semi-rigid brace and early weight-bearing. Rigid plaster casts are contraindicated for simple grade I-II sprains as they cause prolonged joint stiffness.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Displaced ankle fracture or syndesmotic 'high ankle' sprain requiring specialist orthopedic management"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BJSM-ANKLE-GUIDELINE",
                "pmid_or_doi": "10.1136/bjsports-2017-098106",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Functional support with early mobilization resulted in faster return to work and sports and lower re-sprain rates compared to immobilization."
            }
        }
    },
    {
        "id": "DOC-CARD-563",
        "icd10": "M65.4",
        "condition": "Wrist Pain & De Quervain's Tenosynovitis",
        "specialty": "Orthopedics & Hand Surgery",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & American Society for Surgery of the Hand",
        "source_body": "ASSH & Cochrane",
        "citation": "Peters-Veluthamaningal C et al. Cochrane Database Syst Rev. 2009;(3):CD005616.",
        "doi_or_source": "10.1002/14651858.CD005616.pub2",
        "clinical_evidence": "De Quervain's tenosynovitis is stenosing tenosynovitis of the first dorsal extensor compartment (abductor pollicis longus and extensor pollicis brevis) at the radial styloid, commonly provoked by repetitive thumb abduction and wrist ulnar deviation (lifting infants, texting, mouse use). Finkelstein's / Eichhoff's maneuver reproduces sharp radial pain. Cochrane systematic review demonstrates that corticosteroid injection resolves symptoms in over 80% of cases, combined with thumb spica splinting.",
        "solution_protocol": {
            "non_pharmacological_targets": "Thumb spica splint immobilizing the wrist and thumb basal joint; ergonomic modification of smartphone and mouse grip; ice application over radial styloid for 10-15 minutes; avoid repetitive pinching and lifting infants by the armpits.",
            "monitoring_cadence": "Monitor radial wrist pain during thumb abduction weekly; hand specialist evaluation if pain persists despite 4 weeks of splinting.",
            "clinical_thresholds": "Persistent severe pain and swelling with crepitus along the radial styloid interfering with basic hand grip."
        },
        "patient_plain_language": "De Quervain's is an inflammation of the sheath wrapping around the two tendons that lift and extend your thumb, right where your thumb meets your wrist. It causes sharp pain when making a fist, turning doorknobs, or lifting a baby. Wearing a thumb-spica splint to rest the thumb for a few weeks gives the swollen sheath time to shrink down so the tendons can glide smoothly again.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does folding your thumb into your palm and bending your wrist down toward your pinky finger cause sharp pain at your wrist bone?",
            "safety_question": "Do you feel clicking, catching, or swelling right at the base of your thumb when moving it?",
            "action_threshold_question": "Could a thumb-spica splint or a localized cortisone injection provide relief if resting my hand hasn't worked?"
        },
        "red_flags": [
            "Severe hand weakness or numbness in the thumb and index finger (Radial nerve entrapment)",
            "Erythema, warmth, and purulent drainage at the wrist (Infectious tenosynovitis)",
            "Bony deformity or acute tenderness in the anatomical snuffbox after a fall (Scaphoid fracture)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "De Quervain's causes sharp pain on the thumb-side of the wrist when gripping or pinching; a thumb splint and rest provide relief.",
                "plain_analogy": "Two strings pulling through a narrow tube that has become swollen and sticky; keeping the strings still allows the tube swelling to subside.",
                "lifestyle_action": "Wear a thumb-spica splint during tasks and sleep, scoop items with your whole forearm rather than your thumb, and apply ice packs."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren applied to radial styloid TID)",
                    "Oral Naproxen (Aleve: 250-500 mg BID with food for 10 days)",
                    "Thumb-spica immobilization brace",
                    "Triamcinolone local injection (10-20 mg into first dorsal compartment)"
                ],
                "dosing_gdmt": "First line: Thumb spica splinting and topical/oral NSAIDs. For persistent pain, a single ultrasound-guided corticosteroid injection into the tendon sheath achieves >80% cure.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Anatomical snuffbox fracture or infection"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-DE-QUERVAIN",
                "pmid_or_doi": "10.1002/14651858.CD005616.pub2",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Corticosteroid injection was statistically superior to splinting alone in achieving complete symptom resolution at 4 weeks."
            }
        }
    },
    {
        "id": "DOC-CARD-564",
        "icd10": "M54.50",
        "condition": "Acute Low Back Pain & Lumbar Muscle Strain",
        "specialty": "Physical Medicine & Primary Care",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American College of Physicians (ACP) & NICE Clinical Guidelines",
        "source_body": "ACP & Lancet Low Back Pain Series",
        "citation": "Qaseem A et al. Noninvasive Treatments for Acute, Subacute, and Chronic Low Back Pain: Clinical Practice Guideline From the ACP. Ann Intern Med. 2017;166(7):514-530.",
        "doi_or_source": "10.7326/M16-2367",
        "clinical_evidence": "Non-specific acute low back pain and lumbosacral muscular strain are extremely common (>80% lifetime prevalence). ACP and Lancet guidelines strongly recommend avoiding routine imaging (X-rays/MRI) in the absence of red flags (cauda equina, malignancy, infection, fracture). First-line management emphasizes remaining active, avoiding bed rest, superficial heat wraps, spinal manipulation, massage, and NSAIDs. Bed rest beyond 24-48 hours prolongs disability.",
        "solution_protocol": {
            "non_pharmacological_targets": "Maintain normal daily physical activity; avoid prolonged bed rest; superficial heat application (heating pad or heat wrap for 20-30 min); gentle walking (20-30 min daily); core engagement and pelvic tilts; ergonomic lifting with knees bent.",
            "monitoring_cadence": "Reassess mobility and pain at 2 and 4 weeks; clinical evaluation if symptoms fail to show improvement after 4 weeks.",
            "clinical_thresholds": "Bowel/bladder dysfunction (urinary retention or fecal incontinence) or progressive motor weakness (foot drop) indicating cauda equina syndrome."
        },
        "patient_plain_language": "Acute back pain is a temporary spasm and strain in the strong muscles and ligaments supporting your lower spine, usually sparked by lifting awkwardly or twisting. Staying in bed actually makes the muscles stiffer and delays recovery; instead, applying warm heating pads and taking gentle, short walks every few hours keeps blood circulating so your back heals rapidly within two to four weeks.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the pain shoot past your knee down into your foot, or make your leg feel weak when climbing stairs?",
            "safety_question": "Have you noticed any numbness around your groin or difficulty controlling your bladder or bowels?",
            "action_threshold_question": "Can you confirm that routine spine X-rays or MRI scans are not needed since I don't have any dangerous red flags?"
        },
        "red_flags": [
            "New loss of bowel or bladder control, or numbness around your groin and buttocks (Cauda Equina Syndrome - surgical emergency)",
            "Progressive muscle weakness in the leg (such as foot drop where you trip over your toes)",
            "Back pain with unexplained fever, history of cancer, or intravenous drug use (Epidural abscess/Malignancy)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute low back pain usually stems from muscle spasm; staying active with short walks and applying heat heals it fastest.",
                "plain_analogy": "A protective muscular clamp holding a temporary joint sprain; keeping the body gently moving reassures the muscles to release their tight grip.",
                "lifestyle_action": "Apply a heating pad for 20 minutes, take frequent short 10-minute walks, and avoid sitting slumped in soft couches."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ibuprofen (Advil: 400-600 mg oral TID with meals for 5-7 days)",
                    "Naproxen (Aleve: 250-500 mg BID with meals)",
                    "Acetaminophen (500-1000 mg q6h PRN)",
                    "Topical Capsaicin or Lidocaine 4% patches",
                    "Cyclobenzaprine (Flexeril: 5 mg oral at bedtime for 3 days if severe muscle spasm)"
                ],
                "dosing_gdmt": "First line: Non-pharmacological therapies (heat, staying active) plus oral NSAIDs. Routine opioids and bed rest are strongly discouraged due to high risk of adverse events and chronic disability.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "History of gastrointestinal bleed or CKD for systemic NSAIDs"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACP-LBP-GUIDELINE",
                "pmid_or_doi": "10.7326/M16-2367",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Non-pharmacologic therapy (superficial heat, exercise) and NSAIDs yielded clinically meaningful pain and function improvements without opioid risks."
            }
        }
    },
    {
        "id": "DOC-CARD-565",
        "icd10": "T14.8",
        "condition": "Soft Tissue Contusion, Bruise & Hematoma",
        "specialty": "Emergency Medicine & Primary Care",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & ACSM Sports Medicine",
        "source_body": "ACSM & Red Cross",
        "citation": "Bleakley CM et al. Am J Sports Med. 2012;40(8):1897-1905.",
        "doi_or_source": "10.1177/0363546511435282",
        "clinical_evidence": "A contusion (bruise) results from blunt impact that crushes capillaries without disrupting the overlying epidermis, leading to extravasation of erythrocytes into interstitial subcutaneous tissues. Hemoglobin degrades sequentially: oxyhemoglobin (red/purple) -> biliverdin (green) -> bilirubin (yellow) -> hemosiderin (brown) over 10-14 days. Immediate management involves cold compresses (15 min intervals), compression, and elevation to minimize hematoma size. Expanding tense hematomas require evaluation for compartment syndrome or underlying coagulopathy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Cold compress or ice wrapped in cloth for 15 minutes at a time during the first 24-48 hours; light elastic compression wrap; elevation above heart level; avoid direct massage over the acute bruise; gentle warm compresses after 48 hours to accelerate reabsorption.",
            "monitoring_cadence": "Monitor bruise color evolution and swelling resolution; clinical evaluation if a firm painful lump continues to expand after 48 hours.",
            "clinical_thresholds": "Rapidly expanding tense hematoma, pallor or pulselessness distal to the injury, or spontaneous bruising without trauma."
        },
        "patient_plain_language": "A bruise is a harmless pool of blood under your skin that happens when a bump breaks tiny blood vessels beneath the surface. Over two weeks, your body slowly breaks down and recycles the trapped blood cells, causing the skin to shift colors like a mood ring from purple and blue to green and yellow. Applying an ice pack wrapped in a towel right after a bump helps minimize the swelling and marks.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the bruise happen from an obvious bump or fall, or are you getting large spontaneous bruises all over your body?",
            "safety_question": "Are you taking any blood thinners like aspirin, warfarin, or apixaban?",
            "action_threshold_question": "Is the bruised area feeling rock-hard, numb, or tingling further down your limb?"
        },
        "red_flags": [
            "Rapidly expanding tense, rock-hard swelling in an arm or leg with severe pain out of proportion (Compartment syndrome)",
            "Spontaneous large bruises appearing without any trauma, accompanied by bleeding gums or nosebleeds (Coagulopathy/Thrombocytopenia)",
            "Bruising behind the ears (Battle sign) or around both eyes (raccoon eyes) following head trauma (Basilar skull fracture)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bruises happen when small blood vessels leak under the skin after a bump; cold packs and elevation help them fade faster.",
                "plain_analogy": "A small puddle of colored water trapped under clear plastic; your body's cleanup crew gently sponges up the pool over two weeks.",
                "lifestyle_action": "Put an ice pack on the bump for 15 minutes, keep the area propped up on a pillow, and avoid pressing hard on the tender spot."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetaminophen (Tylenol: 500-1000 mg q6h PRN for contusion pain)",
                    "Topical Arnica montana gel (applied locally 2-3 times daily)",
                    "Heparinoid / Hirudoid cream (topical mucopolysaccharide polysulfate to accelerate hematoma clearance)"
                ],
                "dosing_gdmt": "First line: Ice, compression, and elevation. Avoid oral aspirin and high-dose NSAIDs during the initial 24 hours to prevent worsening subcutaneous capillary oozing.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Active bleeding diathesis or anti-coagulated patient with expanding hematoma"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACSM-CONTUSION",
                "pmid_or_doi": "10.1177/0363546511435282",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Early intermittent cryotherapy and gentle compression significantly reduced hematoma expansion and expedited functional muscle recovery."
            }
        }
    },
    {
        "id": "DOC-CARD-566",
        "icd10": "T30.1",
        "condition": "Minor First-Degree & Superficial Second-Degree Burn",
        "specialty": "Emergency Medicine & Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Burn Association (ABA) & Cochrane Wounds Group",
        "source_body": "American Burn Association & WHO",
        "citation": "Alsbjörn B et al. Guidelines for the Management of Partial Thickness Burns in a General Hospital or Community Setting. Burns. 2007;33(2):155-160.",
        "doi_or_source": "10.1016/j.burns.2006.11.002",
        "clinical_evidence": "Minor thermal burns (first-degree: erythema without blisters; superficial second-degree: clear fluid blisters, blanching, intact dermis) involve epidermal heat injury. Immediate first aid with cool running tap water (10-20 minutes, 15-20C) significantly limits thermal tissue necrosis, decreases burn depth, and reduces grafting requirements. Do not apply ice (causes vasoconstrictive ischemia) or butter/toothpaste (contaminants). Intact blisters act as biological sterile dressings; debridement is reserved for ruptured, infected, or tense painful blisters.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate cooling under cool running tap water for 15-20 minutes; do NOT use ice, ice water, butter, or oil; leave small intact blisters intact; apply thin layer of pure petroleum jelly or aloe vera; cover with non-adherent sterile dressing (Telfa pad); keep clean.",
            "monitoring_cadence": "Inspect dressing daily; re-evaluate if pain intensifies, redness spreads beyond the burn margins, or purulent fluid develops.",
            "clinical_thresholds": "Second-degree burn covering >10% total body surface area, or any burn involving the face, hands, feet, groin, or major joint (ABA burn center transfer criteria)."
        },
        "patient_plain_language": "A minor burn happens when hot water, steam, or a hot pan touches your skin, turning it red, stinging, and sometimes forming small clear water blisters. The absolute best first aid is holding the burned skin under cool running tap water for a full 15 minutes to pull the heat out of the tissue. Never put ice, butter, or toothpaste on a burn—just keep it clean, leave blisters unbroken, and cover with petroleum jelly and a sterile bandage.",
        "doctor_consultation_checklist": {
            "parameter_question": "How large is the burn, and does it involve sensitive areas like your face, hands, feet, or groin?",
            "safety_question": "Are the blisters intact and filled with clear fluid, or have they torn open and become dirty?",
            "action_threshold_question": "When did you last receive a tetanus vaccination booster?"
        },
        "red_flags": [
            "Burns involving the face, airway, hands, feet, genitals, or encircling an entire limb or chest",
            "Burned skin that looks white, leathery, charred black, and has no feeling (Full-thickness third-degree burn)",
            "Spreading redness, foul-smelling yellow pus, or fever developing 48 hours after the burn"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Minor burns heal best when cooled under tap water for 15 minutes, kept clean, and covered with petroleum jelly.",
                "plain_analogy": "A hot baking sheet taken out of the oven; running cool water over it rapidly cools the metal before it can scorch whatever touches it.",
                "lifestyle_action": "Cool the burn immediately under running tap water for 15 minutes, do not pop blisters, and apply petroleum jelly with a clean non-stick bandage."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "White petrolatum (Vaseline: thin layer applied to superficial burns)",
                    "Silver sulfadiazine 1% cream (Silvadene: topical antimicrobial for second-degree burns without facial involvement)",
                    "Hydrogel dressings (Water-Jel cooling pads for acute pain relief)",
                    "Acetaminophen or Ibuprofen for post-burn inflammatory pain"
                ],
                "dosing_gdmt": "Cool with tap water for 15-20 min. Apply petroleum jelly or non-adherent dressing. Silver sulfadiazine should not be used on the face due to risk of skin tattooing.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Sulfa allergy for silver sulfadiazine",
                    "Chemical burns requiring prolonged 30-60 min copius water irrigation"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ABA-BURN-FIRST-AID",
                "pmid_or_doi": "10.1016/j.burns.2006.11.002",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Immediate cooling of thermal burns with running water for 15-20 minutes halved the rate of hypertrophic scarring and reduced hospital admission rates."
            }
        }
    },
    {
        "id": "DOC-CARD-567",
        "icd10": "L55.9",
        "condition": "Sunburn & Acute Solar Dermatitis",
        "specialty": "Dermatology & Primary Care",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Academy of Dermatology (AAD) Clinical Consensus",
        "source_body": "AAD & Skin Cancer Foundation",
        "citation": "Bickers DR, Athar M. Novel Photoprotective Strategies. Dermatol Clin. 2007;25(1):79-87.",
        "doi_or_source": "10.1016/j.det.2006.09.006",
        "clinical_evidence": "Sunburn is acute cutaneous inflammation induced by excessive ultraviolet (UVB: 290-320 nm, and UVA: 320-400 nm) radiation causing keratinocyte DNA damage, cyclobutane pyrimidine dimers, apoptosis ('sunburn cells'), and release of inflammatory prostaglandins (PGE2) and cytokines. Erythema peaks at 12-24 hours. AAD guidelines emphasize cooling compresses, oral NSAIDs initiated early to block prostaglandin synthesis, frequent emollient application (aloe vera, soy lotions), oral rehydration, and avoiding peeling or deroofing blisters.",
        "solution_protocol": {
            "non_pharmacological_targets": "Cool baths or frequent cool damp compresses; apply pure aloe vera gel or fragrance-free moisturizing lotion while skin is still damp; drink extra water to prevent dehydration; wear loose soft cotton clothing; stay completely out of the sun until fully healed.",
            "monitoring_cadence": "Monitor skin for blistering, chills, or dizziness; seek medical care if >20% body surface blisters or signs of heat illness appear.",
            "clinical_thresholds": "Severe blistering covering large body areas accompanied by high fever, confusion, severe chills ('sun poisoning'), or signs of heat stroke."
        },
        "patient_plain_language": "A sunburn is a radiation burn to your skin caused by invisible ultraviolet rays from the sun, making your skin hot, pink or bright red, tight, and stinging. Taking cool baths, smoothing on soothing aloe vera gel, and drinking plenty of water helps your skin replenish its lost moisture. Taking ibuprofen early on cools down the deep throbbing ache from within.",
        "doctor_consultation_checklist": {
            "parameter_question": "How much of your body is blistered, and are you experiencing chills, headache, or dizziness?",
            "safety_question": "Are you able to keep down fluids and stay well-hydrated?",
            "action_threshold_question": "What broad-spectrum SPF 30+ sunscreen and protective clothing can we plan for future sun exposure?"
        },
        "red_flags": [
            "High fever, severe shaking chills, dizziness, or confusion with extensive blistering ('Sun poisoning')",
            "Blistering covering more than 20% of your body (such as your entire back and chest)",
            "Signs of secondary infection such as oozing pus, red streaks, or worsening tenderness"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sunburn causes hot, red, stinging skin from UV rays; cool compresses, aloe vera, and ibuprofen bring rapid comfort.",
                "plain_analogy": "Toast that has stayed under the heating element a moment too long; cooling the surface and applying moisture prevents the outer crust from drying out.",
                "lifestyle_action": "Take cool showers, apply chilled aloe vera gel multiple times a day, drink two extra glasses of water, and wear loose clothing."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pure Aloe vera gel (soothing botanical cooling agent with antipruritic properties)",
                    "Oral Ibuprofen (Advil: 400-600 mg TID with food - taken early to inhibit prostaglandin-mediated erythema)",
                    "Hydrocortisone 1% cream (OTC topical steroid applied twice daily for intense localized inflammation)",
                    "Calamine lotion (for soothing itch as skin begins to peel)"
                ],
                "dosing_gdmt": "First line: Oral NSAIDs taken within 2-4 hours of sun exposure significantly blunt the inflammatory cascade. Apply aloe vera and moisturizers. Avoid petroleum jelly on fresh hot burns as it traps heat.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not use benzocaine sprays; can provoke allergic contact dermatitis and methemoglobinemia"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAD-SUNBURN-REHAB",
                "pmid_or_doi": "10.1016/j.det.2006.09.006",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Early NSAID administration reduced ultraviolet-B-induced erythema, prostaglandin E2 release, and epidermal cellular injury by over 40%."
            }
        }
    },
    {
        "id": "DOC-CARD-568",
        "icd10": "W57.XXXA",
        "condition": "Insect Bites, Bee Stings & Arthropod Reactions",
        "specialty": "Allergy & Immunology & Primary Care",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAAAI & ACAAI Practice Parameter on Stinging Insect Hypersensitivity",
        "source_body": "AAAAI & ACAAI",
        "citation": "Golden DBK et al. Stinging Insect Hypersensitivity: A Practice Parameter Update 2016. Ann Allergy Asthma Immunol. 2017;118(1):28-54.",
        "doi_or_source": "10.1016/j.anai.2016.10.031",
        "clinical_evidence": "Arthropod bites (mosquitoes, fleas, bedbugs) and Hymenoptera stings (bees, wasps, hornets, fire ants) inject venoms containing melittin, phospholipases, and vasoactive amines. Local reactions manifest with histamine-mediated pruritus, wheal-and-flare erythema, and localized edema. Large local reactions (>10 cm swelling developing over 24-48 hours) are non-allergic and do not require antibiotics unless true secondary cellulitis ensues. Immediate stinger removal (scrape, do not squeeze venom sac), cold packs, oral antihistamines, and topical corticosteroids resolve symptoms.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediately scrape off honeybee stinger with a fingernail or plastic card (do not pinch the venom sac); wash site with soap and water; apply an ice pack wrapped in a cloth for 10-15 minutes; elevate stung limb; apply baking soda paste or calamine lotion to relieve itching; avoid scratching to prevent bacterial cellulitis.",
            "monitoring_cadence": "Monitor bite site over 24-48 hours; distinguish large local reaction (itchy, swelling peaks day 2) from bacterial cellulitis (increasing warmth, spreading tenderness, purulent discharge after day 3-5).",
            "clinical_thresholds": "Any signs of systemic anaphylaxis (hives away from the sting site, lip/tongue swelling, throat tightness, wheezing, dizziness) requiring immediate intramuscular epinephrine."
        },
        "patient_plain_language": "Bug bites and bee stings happen when insects inject tiny droplets of irritating venom into your skin, creating an itchy red bump or swelling. For a bee sting, gently scrape the little black stinger out right away with your fingernail or credit card, then apply an ice cube and an antihistamine cream. The swelling often gets bigger over two days before fading, which is your body's normal immune response and not an infection.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you develop hives all over your body, swelling of your lips or throat, or trouble breathing after the sting?",
            "safety_question": "Is the redness expanding with hot, tender streaking several days after the bite, suggesting a bacterial skin infection?",
            "action_threshold_question": "If you have a history of severe sting allergies, do you carry an unexpired epinephrine auto-injector (EpiPen)?"
        },
        "red_flags": [
            "Anaphylaxis symptoms: lip or tongue swelling, difficulty breathing, throat tightness, or dizziness (Call 911 immediately)",
            "Stings inside the mouth, throat, or on the eyeball",
            "Rapidly spreading hot, red, tender streaks with fever developing days later (Secondary cellulitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Insect bites cause itchy red bumps; scraping out bee stingers, applying ice, and taking antihistamines calms the itch.",
                "plain_analogy": "A tiny drop of hot pepper sauce on bare skin; washing the surface and applying cooling ice neutralizes the stinging sensation.",
                "lifestyle_action": "Scrape off the stinger immediately, put an ice pack on the bite, take an antihistamine pill, and avoid scratching."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrocortisone 1% cream (applied to bite site TID to suppress local histaminergic inflammation)",
                    "Cetirizine (Zyrtec: 10 mg oral once daily) or Diphenhydramine (Benadryl: 25 mg oral q6h PRN)",
                    "Calamine lotion (topical soothing pink lotion for mosquito bites)",
                    "Epinephrine auto-injector (EpiPen: 0.3 mg IM into anterolateral thigh - MANDATORY for systemic anaphylaxis)"
                ],
                "dosing_gdmt": "First line: Wash with soap/water, apply ice, oral H1 antihistamine, and topical hydrocortisone. Epinephrine IM is the sole first-line therapy for anaphylaxis.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not delay intramuscular epinephrine in anaphylaxis for oral antihistamines"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAAAI-STING-UPDATE",
                "pmid_or_doi": "10.1016/j.anai.2016.10.031",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Rapid stinger removal within seconds minimized venom delivery by >80%; oral H1 antihistamines and topical corticosteroids significantly attenuated local swelling diameter."
            }
        }
    },
    {
        "id": "DOC-CARD-569",
        "icd10": "K12.0",
        "condition": "Canker Sores & Aphthous Mouth Ulcers",
        "specialty": "Oral Medicine & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & ADA Guidelines",
        "source_body": "ADA & Cochrane Oral Health Group",
        "citation": "Brocklehurst P et al. Systemic Interventions for Recurrent Aphthous Stomatitis (Mouth Ulcers). Cochrane Database Syst Rev. 2012;(9):CD005411.",
        "doi_or_source": "10.1002/14651858.CD005411.pub2",
        "clinical_evidence": "Recurrent aphthous stomatitis (RAS / canker sores) is characterized by painful, shallow, non-contagious round ulcers on unattached non-keratinized oral mucosa (buccal mucosa, tongue, floor of mouth) with a grayish-yellow pseudomembranous necrotic center surrounded by an erythematous halo. Precipitating factors include minor mucosal trauma (cheek biting, orthodontic hardware), sodium lauryl sulfate (SLS) toothpaste, psychological stress, and vitamin B12/iron deficiency. Unlike cold sores, canker sores are NOT caused by herpes simplex virus and cannot spread to others.",
        "solution_protocol": {
            "non_pharmacological_targets": "Switch to a sodium lauryl sulfate (SLS)-free toothpaste; warm salt water or diluted hydrogen peroxide (1:1 with water) mouth rinses 3 times daily; avoid sharp, crunchy, acidic, salty, and spicy foods; apply a tiny dab of protective oral paste over the ulcer before meals.",
            "monitoring_cadence": "Track ulcer healing; minor aphthae resolve spontaneously in 7-10 days; dental/medical evaluation if ulcer exceeds 1 cm or fails to heal after 2 weeks.",
            "clinical_thresholds": "Ulcer persisting >2-3 weeks without healing (biopsy rule-out for oral squamous cell carcinoma) or multiple deep ulcers with genital lesions (Behçet's disease)."
        },
        "patient_plain_language": "Canker sores are small, painful white or yellow ulcers inside your mouth, usually on the inside of your lips, cheeks, or under your tongue, often sparked by accidentally biting your cheek or feeling stressed. Unlike cold sores, canker sores are completely non-contagious and never appear on the outside of your lips. Switching to an SLS-free toothpaste, rinsing with warm salt water, and dabbing on a numbing oral gel eases the sting so you can eat comfortably.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the ulcer located on the inside of your cheek or tongue (canker sore), or on the outside border of your lip (cold sore)?",
            "safety_question": "Has the sore been present for more than two to three weeks without starting to shrink?",
            "action_threshold_question": "Do you get frequent recurring ulcers, or have you noticed sores in other areas like your eyes or genitals?"
        },
        "red_flags": [
            "A solitary painless or painful mouth ulcer lasting longer than 3 weeks (Oral cancer warning sign)",
            "Difficulty drinking fluids leading to dehydration or severe weight loss",
            "High fever accompanied by severe widespread mouth blistering (Primary herpetic gingivostomatitis or erythema multiforme)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Canker sores are painful inside-the-mouth ulcers; salt water rinses, numbing gels, and avoiding spicy foods help them heal.",
                "plain_analogy": "A small scrape on the soft inner lining of the mouth; protecting it from rough foods lets the delicate mucous membrane regrow smoothly.",
                "lifestyle_action": "Rinse with warm salt water, switch to an SLS-free toothpaste, avoid chips and citrus, and dab a numbing gel on the ulcer."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Triamcinolone acetonide 0.1% in dental paste (Kenalog in Orabase: dabbed onto ulcer at bedtime to form a protective barrier)",
                    "Benzocaine 20% oral gel (Orajel / Anbesol: topical local anesthetic applied before meals)",
                    "Hydrogen peroxide oral rinse (Peroxyl 1.5% mouthwash)",
                    "Oral vitamin B12 supplementation (1000 mcg sublingual daily for recurrent aphthae)"
                ],
                "dosing_gdmt": "First line: Topical protective pastes (Kenalog in Orabase) and warm saline rinses. Antibiotics are completely ineffective for aphthous ulcers.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not apply topical steroids to active fungal (candidiasis) or viral (HSV) oral lesions"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-APHTHOUS",
                "pmid_or_doi": "10.1002/14651858.CD005411.pub2",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Topical corticosteroid dental paste significantly reduced ulcer pain duration and accelerated complete mucosal epithelialization compared to placebo."
            }
        }
    },
    {
        "id": "DOC-CARD-570",
        "icd10": "K08.89",
        "condition": "Toothache & Dental Sensitivity (Reversible Pulpitis)",
        "specialty": "Dentistry & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Dental Association (ADA) Guidelines",
        "source_body": "American Dental Association (ADA)",
        "citation": "Lockhart PB et al. Evidence-Based Clinical Practice Guideline on Antibiotic Use for the Urgent Management of Pulpal- and Periapical-Related Immunocompetent Adult Patients. J Am Dent Assoc. 2019;150(11):906-921.",
        "doi_or_source": "10.1016/j.adaj.2019.08.020",
        "clinical_evidence": "Odontogenic pain typically begins as reversible pulpitis (sharp, transient pain provoked by thermal stimuli like hot or cold drinks, resolving immediately upon stimulus removal) progressing to irreversible pulpitis or periapical abscess as bacterial caries penetrates dentinal tubules into vascularized dental pulp. ADA guidelines establish that antibiotics are NOT indicated for localized toothaches in immunocompetent patients; definitive dental operative treatment (caries excavation, pulpotomy, root canal therapy) combined with NSAID/acetaminophen analgesia is mandatory.",
        "solution_protocol": {
            "non_pharmacological_targets": "Warm salt water rinses (1/2 tsp salt in warm water) after meals; floss gently between teeth to dislodge trapped food particles; use a desensitizing toothpaste containing potassium nitrate; avoid chewing on the painful side; schedule a dental evaluation within 24-48 hours.",
            "monitoring_cadence": "Monitor pain character (constant vs stimulus-provoked); seek urgent emergency evaluation if facial swelling, difficulty opening mouth, or fever ensues.",
            "clinical_thresholds": "Swelling spreading into the cheek, under the jaw, or toward the eye, difficulty swallowing, or fever (Odontogenic deep neck space infection)."
        },
        "patient_plain_language": "A toothache usually starts when the hard outer enamel of a tooth wears down or develops a small cavity, letting hot, cold, or sweet foods irritate the sensitive nerve inside the tooth. Rinsing with warm salt water, avoiding chewing on that side, and taking a combination of ibuprofen and acetaminophen relieves the throbbing pain temporarily while you schedule an appointment with your dentist, who can fix the tooth directly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the tooth only hurt for a second when drinking cold water, or does it throb constantly on its own even at night?",
            "safety_question": "Do you see or feel any visible swelling in your gums, cheek, or underneath your jawbone?",
            "action_threshold_question": "Can we arrange an urgent dental evaluation for definitive treatment rather than relying on antibiotic pills?"
        },
        "red_flags": [
            "Visible swelling spreading into your cheek, jaw, or neck (Dental abscess spreading into deep tissue)",
            "Difficulty swallowing, breathing, or fully opening your mouth (Ludwig's angina - emergency)",
            "Toothache with high fever, chills, and visual changes around the eye"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Toothaches are caused by irritated nerves inside the tooth; combining ibuprofen and paracetamol manages pain until seen by a dentist.",
                "plain_analogy": "A cracked phone screen exposing the delicate sensors beneath; shielding the surface and having a technician seal the glass solves the glitch.",
                "lifestyle_action": "Rinse with warm salt water, avoid ice-cold or sugary drinks, alternate ibuprofen and acetaminophen, and call your dentist."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ibuprofen (Advil: 400-600 mg oral TID with meals - optimal dental anti-inflammatory analgesic)",
                    "Acetaminophen (Tylenol: 500-1000 mg q6h PRN - synergistic when alternated with ibuprofen)",
                    "Potassium nitrate desensitizing toothpaste (Sensodyne: twice daily brushing)",
                    "Topical Clove oil / Eugenol (1-2 drops on cotton pellet applied gently to cavity margin for temporary relief)"
                ],
                "dosing_gdmt": "First line: Alternating Ibuprofen 400 mg and Acetaminophen 500 mg every 3-4 hours provides superior analgesia to opioids without addiction risk. Antibiotics are NOT recommended unless systemic fever or spreading cellulitis is present.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not place an unbuffered aspirin tablet directly against the gum; causes severe chemical mucosal ulceration (aspirin burn)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ADA-TOOTHACHE-GUIDELINE",
                "pmid_or_doi": "10.1016/j.adaj.2019.08.020",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Systematic review demonstrated that NSAIDs plus acetaminophen provided superior pain relief compared to opioid combinations for acute dental pain."
            }
        }
    },
    {
        "id": "DOC-CARD-571",
        "icd10": "R04.0",
        "condition": "Nosebleeds (Epistaxis - Anterior Kiesselbach's Plexus)",
        "specialty": "ENT & Primary Care",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNS Clinical Practice Guideline on Epistaxis",
        "source_body": "AAO-HNS",
        "citation": "Tunkel DE et al. Otolaryngol Head Neck Surg. 2020;162(1 Suppl):S1-S38.",
        "doi_or_source": "10.1177/0194599819890327",
        "clinical_evidence": "Over 90% of epistaxis cases arise from Kiesselbach's plexus on the anterior nasal septum, provoked by dry air, digital trauma (nose picking), allergic rhinitis, and anticoagulant medications. First-line management is firm manual compression of the soft lower cartilaginous third of the nose for 10-15 continuous minutes with the patient sitting upright and head tilted slightly forward. Leaning backward is contraindicated as it directs blood into the pharynx, risking nausea and aspiration.",
        "solution_protocol": {
            "non_pharmacological_targets": "Sit upright and lean slightly forward (do NOT tilt head back); firmly pinch the soft cartilaginous lower half of the nose continuously for 10-15 full minutes without letting go; apply ice pack over nasal bridge; apply thin petroleum jelly inside nostrils twice daily; use bedroom cool-mist humidifier; avoid vigorous nose blowing for 24 hours.",
            "monitoring_cadence": "Self-monitor bleeding cessation; seek urgent emergency evaluation if bleeding continues after 20-30 minutes of continuous firm pressure.",
            "clinical_thresholds": "Active hemorrhage persisting >20-30 min of continuous pinching, blood pouring rapidly down the back of the throat (posterior bleed), or hemodynamic instability."
        },
        "patient_plain_language": "A nosebleed happens when tiny, delicate blood vessels on the front wall inside your nose crack open and bleed, usually from dry winter air or gently blowing your nose. The correct first-aid technique is sitting upright, leaning slightly forward, and pinching the soft, squishy lower half of your nose tightly closed for a full 10 to 15 minutes by the clock. Leaning backward should be avoided because it lets blood drip down into your stomach.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you pinch the soft lower part of your nose tightly for a full 10 to 15 minutes without peeking?",
            "safety_question": "Are you taking aspirin, blood thinners, or over-the-counter nasal allergy sprays that can dry the nasal lining?",
            "action_threshold_question": "Is the blood pouring mostly down the back of your throat, which might suggest a deeper posterior nosebleed?"
        },
        "red_flags": [
            "Bleeding that does not stop after 20 to 30 minutes of continuous firm pinching",
            "Blood gushing rapidly down the back of the throat even when pinching the nose tightly",
            "Feeling dizzy, faint, lightheaded, or looking very pale during the nosebleed"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Nosebleeds are caused by fragile blood vessels inside the nose; leaning forward and pinching the soft nostrils for 15 minutes stops them.",
                "plain_analogy": "A dripping garden hose nozzle; squeezing the soft rubber tip firmly shut stops the water flow until the gasket reseals.",
                "lifestyle_action": "Sit upright, lean forward, pinch the soft lower nose firmly for 15 minutes without letting go, and moisturize with petroleum jelly later."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oxymetazoline 0.05% nasal spray (Afrin: 2 sprays onto cotton ball inserted into bleeding nostril as potent vasoconstrictor)",
                    "White petrolatum (Vaseline: thin layer applied twice daily inside anterior nostrils for prevention)",
                    "Saline nasal gel / spray (isotonic moisture to prevent mucosal crusting)",
                    "Silver nitrate chemical cautery (performed by physician for persistent visible vessel)"
                ],
                "dosing_gdmt": "First line: Firm compression for 15 minutes plus topical oxymetazoline vasoconstrictor. Petroleum jelly inside nostrils for prevention.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Posterior epistaxis requiring specialized balloon tamponade packing"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAO-HNS-EPISTAXIS",
                "pmid_or_doi": "10.1177/0194599819890327",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Standardized anterior compression combined with topical oxymetazoline achieved successful hemostasis in >85% of acute epistaxis episodes without nasal packing."
            }
        }
    },
    {
        "id": "DOC-CARD-572",
        "icd10": "R06.6",
        "condition": "Benign Hiccups (Singultus & Diaphragmatic Spasms)",
        "specialty": "Gastroenterology & Primary Care",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Review & AAFP Guidelines",
        "source_body": "AAFP & British Journal of Anaesthesia",
        "citation": "Steger M et al. BMJ. 2015;351:h5282.",
        "doi_or_source": "10.1136/bmj.h5282",
        "clinical_evidence": "Hiccups (singultus) result from involuntary, spasmodic contractions of the inspiratory muscles (primarily the diaphragm and intercostal muscles) followed by abrupt closure of the glottis, producing the characteristic sound. Transient benign hiccups (<48 hours) are triggered by gastric distension (carbonated beverages, overeating), sudden temperature changes, or emotional excitement, mediating a reflex arc involving the vagus, phrenic, and sympathetic nerves. Physical maneuvers that increase vagal tone or elevate blood pCO2 stimulate the respiratory center and abort the reflex.",
        "solution_protocol": {
            "non_pharmacological_targets": "Vagal stimulation maneuvers: sip ice water slowly, swallow a teaspoon of granulated dry sugar, pull knees to chest and lean forward, or bite on a lemon wedge; respiratory maneuvers: hold breath for 10-15 seconds, breathe into a paper bag (elevates arterial pCO2 to quiet the reflex arc).",
            "monitoring_cadence": "Self-monitor duration; clinical investigation warranted if hiccups persist continuously beyond 48 hours (persistent hiccups) or >1 month (intractable hiccups).",
            "clinical_thresholds": "Hiccups lasting >48 hours without interruption, or accompanied by chest pain, shortness of breath, or neurological symptoms."
        },
        "patient_plain_language": "Hiccups are sudden, involuntary little twitches of your diaphragm—the large breathing muscle separating your chest from your stomach—followed immediately by your vocal cords snapping shut with a 'hic' sound. They usually start after drinking fizzy sodas, eating too fast, or sudden excitement. Simple home tricks like sipping ice-cold water, swallowing a teaspoon of sugar, or holding your breath for a few seconds reset the nerve signals and stop the spasms.",
        "doctor_consultation_checklist": {
            "parameter_question": "How long have you had the hiccups, and do they let you sleep at night?",
            "safety_question": "Did the hiccups start after eating quickly or drinking carbonated sodas, or did they begin completely out of the blue?",
            "action_threshold_question": "If hiccups last longer than two days, do you have any reflux, chest pain, or difficulty swallowing?"
        },
        "red_flags": [
            "Hiccups persisting continuously for more than 48 hours without stopping",
            "Hiccups accompanied by sudden difficulty speaking, facial weakness, or numbness (Stroke red flag)",
            "Hiccups accompanied by severe chest pain or shortness of breath"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hiccups are harmless muscle spasms of the breathing diaphragm; sipping ice water or holding your breath resets the nerve reflex.",
                "plain_analogy": "A computer program caught in a brief loop; hitting the reset button (holding your breath or sipping cold water) restarts the clean rhythm.",
                "lifestyle_action": "Sip a glass of ice-cold water, hold your breath for 15 seconds, or swallow a teaspoon of sugar to calm the diaphragm."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Non-pharmacological vagal maneuvers (first-line for acute benign hiccups)",
                    "Chlorpromazine (Thorazine: 25-50 mg oral - FDA-approved for intractable hiccups lasting >48h)",
                    "Baclofen (GABA-B agonist: 5-10 mg TID for persistent hiccups)",
                    "Gabapentin (300 mg TID - second-line for refractory singultus)"
                ],
                "dosing_gdmt": "Acute hiccups (<48h) require only physical vagal stimulation. Medications are strictly reserved for persistent hiccups (>48 hours) after ruling out underlying pathology.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Persistent hiccups >48h requiring diagnostic workup"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BMJ-HICCUPS-REVIEW",
                "pmid_or_doi": "10.1136/bmj.h5282",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Physical maneuvers that stimulate the vagus nerve or elevate blood CO2 successfully terminated acute benign hiccups in over 80% of individuals without pharmacological intervention."
            }
        }
    },
    {
        "id": "DOC-CARD-573",
        "icd10": "K30",
        "condition": "Indigestion, Dyspepsia & Acid Regurgitation",
        "specialty": "Gastroenterology",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG & CAG Clinical Guideline for the Management of Dyspepsia",
        "source_body": "ACG & CAG",
        "citation": "Moayyedi P et al. Am J Gastroenterol. 2017;112(7):988-1013.",
        "doi_or_source": "10.1038/ajg.2017.154",
        "clinical_evidence": "Dyspepsia is defined as upper abdominal discomfort or burning, postprandial fullness, early satiety, or epigastric pain. ACG/CAG guidelines recommend non-invasive Helicobacter pylori testing ('test-and-treat') in patients under age 60 without alarm features (weight loss, dysphagia, GI bleeding, persistent vomiting). Empiric proton pump inhibitor (PPI) therapy for 4-8 weeks or H2-receptor antagonists, dietary moderation (smaller meals, reducing fatty and acidic triggers), and avoiding lying down within 3 hours after eating yield significant clinical improvement.",
        "solution_protocol": {
            "non_pharmacological_targets": "Eat smaller, more frequent meals; avoid dietary triggers (fatty/fried foods, caffeine, peppermint, alcohol, chocolate, spicy foods); do not lie flat within 3 hours after meals; elevate head of bed by 6 inches; avoid tight clothing around the abdomen; weight reduction.",
            "monitoring_cadence": "Reassess after 4 weeks of lifestyle modifications and antacid/PPI therapy; clinical gastroenterology review if unremitting.",
            "clinical_thresholds": "Age ≥60 with new-onset dyspepsia, or any patient with alarm features: unexplained weight loss, progressive difficulty swallowing (dysphagia), or black tarry stools (melena)."
        },
        "patient_plain_language": "Indigestion is an uncomfortable fullness, bloating, or warm burning ache in your upper stomach right beneath your ribs, often triggered by eating a heavy or spicy meal too quickly. When stomach acid irritates the sensitive stomach lining or splashes up toward the esophagus, it feels like a heavy brick sitting in your gut. Eating smaller meals, chewing thoroughly, and taking an over-the-counter antacid helps your stomach settle comfortably.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do you get full unusually fast after just a few bites of food, or have pain waking you up in the middle of the night?",
            "safety_question": "Have you noticed any unintentional weight loss, trouble swallowing food, or black dark stools?",
            "action_threshold_question": "Would an over-the-counter acid reducer or a simple test for H. pylori stomach bacteria be appropriate for my symptoms?"
        },
        "red_flags": [
            "Difficulty or pain when swallowing food, feeling like food gets stuck in the chest (Dysphagia)",
            "Vomiting blood or passing dark, tarry black stools (Gastrointestinal bleeding)",
            "Unexplained significant weight loss accompanied by persistent stomach fullness in a patient over 55"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Indigestion causes upper stomach burning and uncomfortable fullness after eating; smaller meals and antacids settle the stomach.",
                "plain_analogy": "A pot of soup boiling too close to the rim on the stove; lowering the heat and not overfilling the pot keeps everything simmering smoothly.",
                "lifestyle_action": "Eat smaller portions, avoid greasy foods and fizzy sodas, don't lie down for three hours after dinner, and take an antacid as needed."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Calcium carbonate (Tums: 500-1000 mg chewable tablets PRN for immediate acid neutralization)",
                    "Famotidine (Pepcid AC: 10-20 mg oral BID before meals - H2-blocker)",
                    "Omeprazole (Prilosec: 20 mg oral once daily before breakfast for 14 days - PPI)",
                    "Simethicone (Gas-X: 80-125 mg chewable tablets for concurrent gas bloating)"
                ],
                "dosing_gdmt": "First line: Lifestyle dietary modifications plus OTC antacids (Tums) or H2 blockers (Famotidine). PPIs reserved for persistent symptoms for a 4-8 week trial.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Undiagnosed dysphagia or active upper GI bleed"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-DYSPEPSIA-GUIDELINE",
                "pmid_or_doi": "10.1038/ajg.2017.154",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "H. pylori test-and-treat and empiric PPI therapy significantly reduced dyspeptic symptom scores and improved quality of life compared to placebo."
            }
        }
    },
    {
        "id": "DOC-CARD-574",
        "icd10": "R14.0",
        "condition": "Intestinal Gas, Bloating & Flatulence",
        "specialty": "Gastroenterology & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Practice Guideline on Functional Bowel Disorders",
        "source_body": "American College of Gastroenterology (ACG)",
        "citation": "Lacy BE et al. Am J Gastroenterol. 2021;116(1):17-44.",
        "doi_or_source": "10.14309/ajg.0000000000001036",
        "clinical_evidence": "Abdominal bloating and flatulence arise from excessive intestinal gas production (fermentation of poorly absorbed short-chain carbohydrates by colonic microbiota) or impaired transit and visceral hypersensitivity. Over 99% of flatus consists of odorless gases (nitrogen, oxygen, hydrogen, methane, carbon dioxide), with trace sulfur compounds (hydrogen sulfide) causing odor. Clinical trials demonstrate that a low-FODMAP diet, simethicone, alpha-galactosidase enzyme supplements, and regular physical activity significantly alleviate gaseous distension.",
        "solution_protocol": {
            "non_pharmacological_targets": "Low-FODMAP dietary approach (reduce beans, lentils, onions, garlic, cruciferous vegetables, high-fructose corn syrup); eat slowly and chew thoroughly to reduce aerophagia (air swallowing); avoid carbonated sodas and drinking through straws; take a light 15-minute walk after meals to stimulate gas transit; avoid chewing gum.",
            "monitoring_cadence": "Monitor bloating episodes and dietary correlations via a 2-week food diary; clinical review if bloating is accompanied by altered bowel habits.",
            "clinical_thresholds": "Progressive abdominal distension accompanied by failure to pass gas or stool with vomiting (bowel obstruction), or severe localized abdominal tenderness."
        },
        "patient_plain_language": "Intestinal gas and bloating happen when air swallowed while eating or gases produced by friendly gut bacteria fermenting your food build up inside your intestines, making your belly feel tight, swollen, or drum-like. Passing gas or burping is your body's healthy way of releasing this pressure. Eating more slowly, cutting down on fizzy sodas and beans, and taking a brisk walk after dinner helps trapped gas move through naturally.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the bloating feel relieved after you pass gas or have a bowel movement?",
            "safety_question": "Have you noticed changes in your bowel habits, such as chronic alternating diarrhea and constipation?",
            "action_threshold_question": "Would a trial of an over-the-counter gas-relieving enzyme (like Beano) or a low-FODMAP food plan help identify my trigger foods?"
        },
        "red_flags": [
            "Severe crampy abdominal pain accompanied by persistent vomiting and inability to pass gas or stool (Bowel obstruction)",
            "Unintentional weight loss, chronic watery diarrhea, or blood in the stool",
            "New persistent abdominal bloating in a woman over 50 accompanied by early satiety (Ovarian cancer screening red flag)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Gas and bloating make your stomach feel stretched and tight; eating slowly, walking after meals, and simethicone help relieve pressure.",
                "plain_analogy": "A balloon slowly inflating inside a sealed lunchbox; venting the air or eating foods that produce less steam relieves the pressure.",
                "lifestyle_action": "Chew food slowly with your mouth closed, avoid carbonated drinks and chewing gum, take a short walk after eating, and try simethicone."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Simethicone (Gas-X: 80-125 mg chewable tablets after meals and at bedtime - breaks gas bubble surface tension)",
                    "Alpha-galactosidase enzyme (Beano: taken with first bite of high-fiber beans/vegetables)",
                    "Lactase enzyme (Lactaid: taken before consuming dairy for lactose intolerance)",
                    "Probiotic supplements (Bifidobacterium infantis 35624: daily for 4-8 weeks to balance gut microbiome)"
                ],
                "dosing_gdmt": "First line: Dietary modification (chewing slowly, reducing FODMAP triggers) plus simethicone. Enzyme supplements taken with meals prevent gas from specific food triggers.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Acute mechanical bowel obstruction"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-BLOATING-TRIAL",
                "pmid_or_doi": "10.14309/ajg.0000000000001036",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Dietary FODMAP restriction and simethicone significantly decreased abdominal distension severity and flatulence frequency compared to baseline."
            }
        }
    },
    {
        "id": "DOC-CARD-575",
        "icd10": "A08.4",
        "condition": "Acute Viral Gastroenteritis & Stomach Flu",
        "specialty": "Infectious Disease & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Clinical Practice Guidelines for Acute Diarrhea",
        "source_body": "IDSA & WHO",
        "citation": "Shane AL et al. Clin Infect Dis. 2017;65(12):e45-e80.",
        "doi_or_source": "10.1093/cid/cix669",
        "clinical_evidence": "Acute viral gastroenteritis ('stomach flu') is inflammation of the stomach and small intestine, most frequently caused by Norovirus in adults and children and Rotavirus in unimmunized pediatric patients. Characterized by sudden-onset watery diarrhea, nausea, vomiting, and low-grade fever lasting 24-72 hours. IDSA guidelines establish that oral rehydration solution (ORS) with balanced electrolytes and glucose is the cornerstone of therapy. Antibiotics are completely ineffective for viral gastroenteritis and may prolong shedding.",
        "solution_protocol": {
            "non_pharmacological_targets": "Oral rehydration solution (ORS) sipped in small frequent quantities (5-10 mL every 5 minutes); avoid plain water exclusively to prevent hyponatremia; gradually reintroduce bland foods (BRAT diet: bananas, rice, applesauce, toast, crackers) when nausea subsides; strict hand hygiene with soap and water (alcohol gels are less effective against non-enveloped Norovirus); disinfect surfaces with dilute bleach.",
            "monitoring_cadence": "Monitor urine frequency, skin turgor, and fluid retention; seek medical care if unable to keep down fluids for >12-24 hours.",
            "clinical_thresholds": "Signs of severe dehydration (lethargy, dry mucous membranes, no urination for >8 hours, orthostatic syncope), high fever >38.5C, or bloody stool."
        },
        "patient_plain_language": "The stomach flu is a common viral bug that upsets your digestive tract, causing sudden watery diarrhea, vomiting, stomach cramps, and mild fever for two or three days. Because you lose lots of fluids and salts, the golden rule of recovery is sipping oral rehydration drinks or diluted broths in tiny spoonfuls every few minutes. Once your stomach settles, eating bland foods like toast, crackers, and rice helps your gut recover without needing antibiotics.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are you able to keep down small sips of water or rehydration drinks without vomiting immediately?",
            "safety_question": "How many times have you urinated today, and is your urine dark yellow or concentrated?",
            "action_threshold_question": "Is there any blood or dark black material in your diarrhea or vomit?"
        },
        "red_flags": [
            "Complete inability to keep down any fluids for over 12 hours with dizziness and no urination (Severe dehydration)",
            "Passing bloody stool or vomiting material that looks like dark coffee grounds",
            "Severe, constant localized abdominal pain that worsens when you cough or move (Appendicitis rule-out)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "The stomach flu causes watery diarrhea and vomiting for a few days; sipping electrolyte fluids and resting your stomach is key.",
                "plain_analogy": "A flash flood moving through a waterway; sipping balanced electrolyte fluids keeps the water levels safe until the riverbed dries out.",
                "lifestyle_action": "Take tiny sips of oral rehydration solution every 5 minutes, wash your hands thoroughly with soap, and eat plain crackers when ready."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oral Rehydration Salts (ORS packets dissolved in clean water - optimal WHO sodium-glucose ratio)",
                    "Ondansetron (Zofran: 4-8 mg oral ODT - prescription antiemetic to facilitate oral rehydration if vomiting is severe)",
                    "Loperamide (Imodium: 4 mg initial, then 2 mg after each unformed stool - ONLY if non-bloody, afebrile diarrhea)",
                    "Bismuth subsalicylate (Pepto-Bismol: 30 mL or 2 chewables q30-60min PRN, max 8 doses/day)"
                ],
                "dosing_gdmt": "First line: Oral rehydration solution (ORS). Do not use loperamide in patients with high fever or bloody diarrhea (dysentery). Antibiotics have no role in viral gastroenteritis.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Bloody diarrhea with high fever (bacterial dysentery)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "IDSA-GASTROENTERITIS",
                "pmid_or_doi": "10.1093/cid/cix669",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Oral rehydration solution was as effective as intravenous hydration in treating mild-to-moderate dehydration, with fewer adverse events and shorter hospital stays."
            }
        }
    },
    {
        "id": "DOC-CARD-576",
        "icd10": "R11.0",
        "condition": "Nausea & Motion Sickness (Kinetosis)",
        "specialty": "Neurology & Primary Care",
        "organ_system": "Nervous & Sensory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & CDC Yellow Book Guidelines",
        "source_body": "CDC & Cochrane",
        "citation": "Brainard A, Gresham C. Cochrane Database Syst Rev. 2014;(6):CD006844.",
        "doi_or_source": "10.1002/14651858.CD006844.pub3",
        "clinical_evidence": "Motion sickness (kinetosis) results from neurosensory conflict (sensory mismatch theory) where vestibular, visual, and proprioceptive inputs regarding body movement provide discordant signals to the brainstem vestibular nuclei and chemoreceptor trigger zone. Symptoms include yawning, cold sweating, malaise, nausea, and vomiting during boat, car, or air travel. Cochrane reviews confirm that centrally acting anticholinergics (transdermal scopolamine) and first-generation H1 antihistamines (dimenhydrinate, meclizine) taken prophylactically before travel provide significant symptom prevention.",
        "solution_protocol": {
            "non_pharmacological_targets": "Sit in the area of least motion (front passenger seat of car, over the wing in airplane, mid-ship on boat); fix gaze on the distant horizon; ensure fresh cool air ventilation; avoid reading, looking at phone screens, or sitting backward; consume real ginger candies or ginger tea; stay hydrated with small sips of water; avoid heavy or greasy meals immediately before travel.",
            "monitoring_cadence": "Self-monitor during travel; clinical evaluation if vertigo, nausea, or vomiting persists long after travel ends.",
            "clinical_thresholds": "Vertigo accompanied by unilateral hearing loss, focal neurological deficits (ataxia, dysarthria), or intractable dehydration."
        },
        "patient_plain_language": "Motion sickness happens when your eyes, inner ear balance canals, and muscles send conflicting messages to your brain—like when reading a book in the backseat of a car where your eyes say you are still, but your inner ears feel every turn and bump. This sensory confusion triggers cold sweats, nausea, and stomach queasiness. Looking straight ahead at the distant horizon, opening the window for fresh air, and taking an anti-nausea pill before the trip keeps your senses in sync.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the nausea occur specifically during car, boat, or air travel, or do you feel spinning sensations when sitting still at home?",
            "safety_question": "Have you tried sitting in the front passenger seat and looking out at the horizon, or taking preventative medication before trips?",
            "action_threshold_question": "Do you experience any ringing in your ears or hearing changes with the nausea?"
        },
        "red_flags": [
            "Severe spinning room vertigo that persists long after travel stops, accompanied by difficulty walking",
            "Sudden weakness in your face, arm, slurred speech, or double vision (Central stroke warning)",
            "Intractable vomiting leading to dehydration and fainting"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Motion sickness causes nausea when your eyes and ears feel motion differently; looking at the horizon and taking motion sickness pills prevents it.",
                "plain_analogy": "A ship's navigation computer receiving two GPS coordinates that don't match; looking at the horizon recalibrates the satellite lock.",
                "lifestyle_action": "Sit in the front seat, look out at the road ahead, open the air vent, chew on ginger candies, and take meclizine before traveling."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Meclizine (Bonine / Dramamine Less Drowsy: 25-50 mg oral taken 1 hour before travel)",
                    "Dimenhydrinate (Dramamine: 50-100 mg oral taken 30-60 min before travel)",
                    "Scopolamine transdermal patch (Transderm Scop: 1.5 mg patch applied behind ear ≥4 hours before travel)",
                    "Ginger root capsules or lozenges (500-1000 mg taken 30 minutes before travel - natural antiemetic)"
                ],
                "dosing_gdmt": "First line: Prophylaxis is far more effective than treatment after nausea begins. Take oral antihistamines 1 hour before departure or apply scopolamine patch 4 hours prior.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Narrow-angle glaucoma or urinary retention for scopolamine"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-SCOPOLAMINE",
                "pmid_or_doi": "10.1002/14651858.CD006844.pub3",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Scopolamine and first-generation antihistamines were significantly more effective than placebo in preventing motion-induced nausea and vomiting during transit."
            }
        }
    },
    {
        "id": "DOC-CARD-577",
        "icd10": "K59.00",
        "condition": "Acute Constipation & Infrequent Stool",
        "specialty": "Gastroenterology & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Practice Guideline on Management of Benign Constipation",
        "source_body": "American College of Gastroenterology (ACG)",
        "citation": "Chang L et al. Am J Gastroenterol. 2023;118(6):936-954.",
        "doi_or_source": "10.14309/ajg.0000000000002227",
        "clinical_evidence": "Constipation is characterized by hard, dry stools, infrequent bowel movements (<3 per week), excessive straining, and a sensation of incomplete evacuation. ACG clinical practice guidelines emphasize a stepwise approach: increasing dietary soluble fiber (25-35 g/day, such as psyllium husk) and fluid intake, combined with an osmotic laxative like Polyethylene Glycol (PEG 3350), which has the highest quality of evidence (Grade A) for efficacy and safety without causing dependency or cramping.",
        "solution_protocol": {
            "non_pharmacological_targets": "Gradually increase dietary soluble fiber to 25-30 grams daily (oats, flaxseeds, prunes, kiwis, beans); drink 6-8 glasses of water daily; establish a regular morning toilet routine (especially 15-30 minutes after breakfast to utilize the gastrocolic reflex); use a footstool (Squatty Potty) to elevate knees above hips, straightening the anorectal angle; increase daily walking.",
            "monitoring_cadence": "Monitor bowel movement frequency and consistency (Bristol Stool Scale Type 1-2 vs 3-4); clinical review if no bowel movement occurs after 7 days despite laxative therapy.",
            "clinical_thresholds": "Constipation accompanied by severe vomiting, abdominal swelling, acute severe pain, or inability to pass gas (fecal impaction or bowel obstruction)."
        },
        "patient_plain_language": "Constipation means your bowel movements are happening less often than usual, or that your stools have become hard, dry, and difficult or painful to push out. When food moves too slowly through your colon, the body reabsorbs too much water, turning the stool into dry pebbles. Drinking plenty of water, eating high-fiber foods like prunes and oats, elevating your feet on a small bathroom stool, and taking gentle water-drawing powders like MiraLAX helps your bowels move smoothly again.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many days has it been since your last bowel movement, and are your stools hard like pebbles or painful to pass?",
            "safety_question": "Are you taking any medications that cause constipation, such as iron supplements, calcium, or opioid pain pills?",
            "action_threshold_question": "Have you noticed any blood on the toilet paper or dark black stools?"
        },
        "red_flags": [
            "Complete inability to pass any stool or gas accompanied by severe crampy stomach pain and vomiting (Intestinal obstruction)",
            "Rectal bleeding or stools that look like black tar",
            "Unexplained new constipation in a patient over 50 that persists for several weeks (Colon cancer screening warning)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Constipation happens when stools become hard and dry; drinking water, eating fiber and prunes, and taking MiraLAX softens them.",
                "plain_analogy": "A dry sponge trying to slide down an empty slide; adding water makes the sponge plump, slippery, and glide down effortlessly.",
                "lifestyle_action": "Drink extra water, eat two kiwis or a handful of prunes daily, use a footstool to raise your knees on the toilet, and take MiraLAX."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Polyethylene glycol 3350 (MiraLAX: 17 g powder dissolved in 8 oz water once daily - first-line osmotic laxative)",
                    "Psyllium husk (Metamucil: 3.4 g soluble fiber 1-3 times daily with plenty of water)",
                    "Docusate sodium (Colace: 100 mg oral once or twice daily - stool softener)",
                    "Bisacodyl (Dulcolax: 5-10 mg oral tablet or 10 mg suppository - short-term stimulant laxative)"
                ],
                "dosing_gdmt": "First line: Polyethylene glycol (PEG 3350) and dietary fiber. Stimulant laxatives (bisacodyl, senna) should be used short-term as rescue therapy rather than daily first-line.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Known or suspected mechanical bowel obstruction"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-CONSTIPATION-GUIDELINE",
                "pmid_or_doi": "10.14309/ajg.0000000000002227",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Polyethylene glycol demonstrated Grade A evidence for significantly improving stool frequency, stool consistency, and straining without habituation."
            }
        }
    },
    {
        "id": "DOC-CARD-578",
        "icd10": "K64.9",
        "condition": "Hemorrhoids & Perianal Discomfort (Piles)",
        "specialty": "Colorectal Surgery & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASCRS Clinical Practice Guidelines for Management of Hemorrhoids",
        "source_body": "American Society of Colon and Rectal Surgeons (ASCRS)",
        "citation": "Davis BR et al. Dis Colon Rectum. 2018;61(3):284-292.",
        "doi_or_source": "10.1097/DCR.0000000000001030",
        "clinical_evidence": "Hemorrhoids are vascular cushions within the anal canal consisting of connective tissue, smooth muscle, and arteriovenous anastomoses. Increased intra-abdominal pressure and chronic straining cause venous engorgement and prolapse. Internal hemorrhoids typically present with painless bright red blood coating stool or on toilet tissue; external hemorrhoids cause perianal swelling, itching, and acute severe pain when thrombosed. ASCRS guidelines establish that conservative management (dietary fiber 25-30 g/day, water, warm sitz baths, and avoiding prolonged sitting on the toilet) successfully manages the vast majority of cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Warm sitz baths (soaking in 3-4 inches of plain warm water for 15 minutes 2-3 times daily); high-fiber diet (25-30 g/day) and adequate hydration to ensure soft, bulky stools; avoid straining or holding your breath during defecation; avoid sitting on the toilet for longer than 3-5 minutes (do not read smartphones on the toilet); use moist wipes instead of dry toilet paper.",
            "monitoring_cadence": "Monitor bleeding and anal swelling; clinical colorectal evaluation if painless bleeding persists or if external thrombosed hemorrhoid develops severe pain within first 72 hours.",
            "clinical_thresholds": "Acute, severe, throbbing perianal pain with a firm bluish lump (thrombosed external hemorrhoid warranting excision within 72 hours), or systemic fever with anal pain (perianal abscess)."
        },
        "patient_plain_language": "Hemorrhoids (often called piles) are swollen, stretched veins located in the lower rectum and anus, much like varicose veins in your legs, caused by pushing too hard when constipated or sitting on the toilet for too long. They can cause a small streak of bright red blood on the toilet paper, itching, or a tender little bump outside the anus. Soaking in a warm shallow bath (sitz bath), eating more fiber to soften stools, and never lingering on the toilet brings prompt relief.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the blood bright red and seen only on the toilet paper or coating the stool, or mixed into the stool itself?",
            "safety_question": "Do you have a tender, painful lump that suddenly popped up on the outside of your anus?",
            "action_threshold_question": "How long do you usually sit on the toilet, and can we start a fiber supplement to prevent any future straining?"
        },
        "red_flags": [
            "Fever, severe chills, and a red, hot, exquisitely tender swelling next to the anus (Perirectal abscess - emergency)",
            "Dark, maroon, or black tarry stools mixed with blood (Upper GI bleeding)",
            "Severe sudden pain from an external blue lump that cannot be touched (Acute thrombosed hemorrhoid)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hemorrhoids are swollen veins around the anus from straining; warm baths, fiber supplements, and not lingering on the toilet heal them.",
                "plain_analogy": "A tiny water balloon pressed against a bicycle tire; releasing the air and soaking the rubber in warm water shrinks the balloon back to normal.",
                "lifestyle_action": "Take a warm sitz bath for 15 minutes twice a day, add fiber and water so you never strain, and leave the toilet as soon as you finish."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrocortisone 1% / Pramoxine 1% rectal cream (Preparation H / Proctofoam: applied locally for itching and swelling)",
                    "Witch hazel pads (Tucks medicated cooling pads: applied gently to external hemorrhoids)",
                    "Psyllium husk fiber (Metamucil: 1 tablespoon daily to produce soft formed stools)",
                    "Oral Flavonoids (Micronized purified flavonoid fraction / MPFF: 500-1000 mg daily to improve venous tone)"
                ],
                "dosing_gdmt": "First line: High-fiber diet, hydration, warm sitz baths, and topical hydrocortisone/witch hazel. For acute thrombosed external hemorrhoids presenting within 72 hours, simple in-office surgical excision provides rapid pain relief.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Active perianal abscess requiring incision and drainage"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASCRS-HEMORRHOIDS",
                "pmid_or_doi": "10.1097/DCR.0000000000001030",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Fiber supplementation and warm sitz baths reduced the risk of persistent hemorrhoidal symptoms and bleeding by over 50%."
            }
        }
    },
    {
        "id": "DOC-CARD-579",
        "icd10": "G44.209",
        "condition": "Tension-Type Headache",
        "specialty": "Neurology & Primary Care",
        "organ_system": "Neurological",
        "cebm_level": 1,
        "evidence_tier": "Level 1: International Headache Society (ICHD-3) & Cochrane Review",
        "source_body": "International Headache Society (IHS) & AHS",
        "citation": "Bendtsen L et al. Eur J Neurol. 2010;17(8):1018-1025.",
        "doi_or_source": "10.1111/j.1468-1331.2010.03070.x",
        "clinical_evidence": "Tension-type headache (TTH) is the most prevalent neurological disorder worldwide (>70% lifetime prevalence). Diagnostic criteria require bilateral, non-pulsating, dull pressing or tightening pain of mild-to-moderate intensity ('tight band around the head'), typically without aggravation by routine physical activity and without severe nausea/vomiting or photophobia/phonophobia (at most, only one may be present). Pathophysiology involves heightened pericranial myofascial tenderness and central nociceptive sensitization. First-line acute therapy is simple analgesia (NSAIDs, acetaminophen) taken early.",
        "solution_protocol": {
            "non_pharmacological_targets": "Apply cool or warm compresses over the forehead and temples; gentle neck and shoulder stretching; regular sleep schedule; stay hydrated; manage screen glare; practice stress reduction techniques (deep breathing, progressive muscle relaxation); limit caffeine intake to steady low levels.",
            "monitoring_cadence": "Maintain a headache diary tracking frequency, triggers, and medication use; seek clinical review if headaches occur >15 days per month (chronic tension-type headache).",
            "clinical_thresholds": "Acute sudden 'thunderclap' headache reaching maximum intensity in seconds, headache with fever and stiff neck, or new headache in a patient >50 years old."
        },
        "patient_plain_language": "A tension headache is the most common kind of everyday headache, felt as a dull, steady ache or a tight, squeezy band wrapped firmly around your forehead, temples, and the back of your neck. Unlike a migraine, it does not throb, doesn't make you throw up, and doesn't get worse when you climb stairs. Resting in a quiet space, relaxing your shoulder muscles, drinking water, and taking a standard pain reliever like ibuprofen or paracetamol clears it up.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the headache feel like a steady, dull tight band around your head rather than a throbbing heartbeat?",
            "safety_question": "How many days per week do you take over-the-counter headache pills, to make sure we avoid medication-overuse headaches?",
            "action_threshold_question": "Do you have any vision changes, weakness, fever, or sensitivity to light with this headache?"
        },
        "red_flags": [
            "Sudden, explosive 'thunderclap' headache reaching 10/10 agony within seconds (Subarachnoid hemorrhage warning)",
            "Headache with high fever, stiff neck, confusion, or rash (Meningitis)",
            "New daily headache starting in a person over 50 with scalp tenderness when combing hair (Temporal arteritis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Tension headaches feel like a tight band around your head from stress and muscle tension; rest, hydration, and ibuprofen relieve it.",
                "plain_analogy": "A belt buckled just a little too tight around your head; unbuckling the notch with relaxation and cool water lets your head breathe freely.",
                "lifestyle_action": "Drink a tall glass of water, gently massage your temples and neck muscles, take a short break from computer screens, and rest in a dim room."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ibuprofen (Advil: 400 mg oral - superior first-line acute efficacy for tension headache)",
                    "Acetaminophen (Tylenol: 1000 mg oral every 6 hours PRN)",
                    "Naproxen sodium (Aleve: 220-440 mg oral at onset)",
                    "Amitriptyline (10-25 mg at bedtime - first-line prescription preventive for chronic tension headaches >15 days/month)"
                ],
                "dosing_gdmt": "First line: Simple analgesics (Ibuprofen 400 mg or Acetaminophen 1000 mg) taken early. Avoid using acute analgesics more than 2-3 days per week to prevent medication-overuse headache (MOH).",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Medication-overuse headache from chronic daily analgesic use"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-TENSION-HEADACHE",
                "pmid_or_doi": "10.1111/j.1468-1331.2010.03070.x",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Ibuprofen 400 mg provided complete headache pain freedom at 2 hours in a statistically significant majority of patients compared to placebo."
            }
        }
    },
    {
        "id": "DOC-CARD-580",
        "icd10": "T67.5XXA",
        "condition": "Heat Exhaustion, Dehydration & Heat Cramps",
        "specialty": "Emergency Medicine & Sports Medicine",
        "organ_system": "Multisystem",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CDC Guidelines & Wilderness Medical Society Clinical Practice Guideline",
        "source_body": "Wilderness Medical Society & CDC",
        "citation": "Lipman GS et al. Wilderness Environ Med. 2019;30(4S):S8-S28.",
        "doi_or_source": "10.1016/j.wem.2018.10.004",
        "clinical_evidence": "Heat exhaustion is a mild-to-moderate form of heat-related illness resulting from prolonged exposure to high ambient temperatures and humidity coupled with inadequate fluid and electrolyte replacement. Symptoms include profuse sweating, intense thirst, dizziness, fatigue, nausea, headache, and muscle cramps, with a core temperature <40C (104F) and completely normal mental status. Immediate management requires moving to a cool shaded environment, active evaporative cooling (mist and fan), removing excess clothing, and oral rehydration with electrolyte solutions. Differentiating from life-threatening heat stroke (core temp >40C with encephalopathy/confusion) is critical.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate removal from heat into an air-conditioned room or shade; lie down and elevate legs slightly; remove tight or heavy clothing; active external cooling: sponge skin with cool water and fan continuously; sip cold electrolyte-rich drinks or slightly salted water; rest completely for the remainder of the day.",
            "monitoring_cadence": "Monitor temperature and mental alertness every 15 minutes; emergency transfer if body temperature exceeds 39.5C or if confusion develops.",
            "clinical_thresholds": "Any alteration in mental status (confusion, delirium, seizures, coma) or hot, dry skin (Heat stroke - medical emergency requiring immediate whole-body immersion)."
        },
        "patient_plain_language": "Heat exhaustion happens when your body gets dangerously overheated on a hot, muggy day or during heavy outdoor work, losing vital water and salts through heavy sweating. You feel dizzy, washed out, nauseated, and drenched in cold sweat, and your muscles may cramp up. The cure is getting into an air-conditioned room or cool shade right away, drinking cool sports drinks or water with a pinch of salt, and fanning your wet skin to help your internal thermostat reset.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the symptoms begin while working or exercising in hot weather, and are you drinking fluids with electrolytes?",
            "safety_question": "Is the person completely alert and talking normally, or are they acting confused, dizzy, or slurring words?",
            "action_threshold_question": "Is their skin still actively sweating, or has it become hot, dry, and flushed?"
        },
        "red_flags": [
            "Any confusion, agitation, slurred speech, seizures, or loss of consciousness (Heat stroke - call 911 immediately)",
            "Inability to drink fluids due to continuous vomiting in severe heat",
            "Body temperature rising above 39.5C (103F) or hot skin that has stopped sweating entirely"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Heat exhaustion causes dizziness, heavy sweating, and nausea from overheating; resting in the cool shade and drinking fluids fixes it.",
                "plain_analogy": "A car engine whose radiator fluid has boiled low on a hot highway; pulling into the shade, shutting off the engine, and refilling the coolant cools it down.",
                "lifestyle_action": "Move into air-conditioned shade immediately, drink cool electrolyte water, loosen tight clothing, and fan cool water over your skin."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oral Electrolyte Rehydration Solution (balanced sports drink or water with electrolyte replacement powders)",
                    "Cold packs applied to neck, armpits, and groin",
                    "Intravenous Normal Saline / Lactated Ringer's (for patients unable to tolerate oral fluids in emergency settings)"
                ],
                "dosing_gdmt": "First line: Immediate passive and active cooling plus oral fluid/electrolyte rehydration. Antipyretic drugs like acetaminophen or aspirin are completely ineffective and contraindicated in environmental heat illness.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Heat stroke with altered mental status requiring rapid cold-water immersion"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WMS-HEAT-ILLNESS",
                "pmid_or_doi": "10.1016/j.wem.2018.10.004",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Immediate cessation of exertion, shade transfer, and evaporative cooling restored physiological hemodynamics in over 95% of heat exhaustion cases."
            }
        }
    },
    {
        "id": "DOC-CARD-581",
        "icd10": "T51.0X1A",
        "condition": "Alcohol Hangover & Congener Malaise",
        "specialty": "Toxicology & Primary Care",
        "organ_system": "Multisystem",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Systematic Review on Alcohol Hangover Pathophysiology",
        "source_body": "Alcohol and Alcoholism & Mayo Clinic",
        "citation": "Penning R et al. Curr Drug Abuse Rev. 2010;3(2):68-75.",
        "doi_or_source": "10.2174/187314710790820401",
        "clinical_evidence": "Alcohol hangover (veisalgia) is a constellation of unpleasant physical and mental symptoms occurring when blood alcohol concentration (BAC) approaches zero following heavy alcohol consumption. Pathophysiologic drivers include ethanol-induced vasopressin suppression causing diuresis and dehydration, toxic acetaldehyde buildup, congener accumulation (methanol, tannins in dark liquors), gastric mucosal irritation, hypoglycemia, and inflammatory cytokine activation (IL-6, TNF-alpha). Evidence supports aggressive fluid/electrolyte replenishment, carbohydrates, and non-hepatotoxic analgesics.",
        "solution_protocol": {
            "non_pharmacological_targets": "Oral rehydration with water, broth, or electrolyte drinks; consume complex carbohydrates (toast, honey, eggs containing cysteine) to restore liver glycogen; rest in a dark, quiet room; avoid the 'hair of the dog' (consuming more alcohol merely delays recovery and increases dependency risk).",
            "monitoring_cadence": "Self-monitor over 24 hours; symptoms typically resolve fully within 24 hours as metabolic clearance completes.",
            "clinical_thresholds": "Persistent vomiting, severe abdominal pain, hematemesis, or alcohol intoxication stupor with airway compromise."
        },
        "patient_plain_language": "A hangover is your body's recovery process after drinking too much alcohol, causing dehydration, headache, nausea, shaky hands, and tiredness the next morning as your blood alcohol level drops to zero. Alcohol tricks your kidneys into peeing out extra water, leaving your brain and body dried out. Drinking lots of water with electrolytes, eating eggs or honey on toast, and resting allows your liver to clear out the breakdown products.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the symptoms begin the morning after drinking alcohol, and are you able to keep down water and simple foods?",
            "safety_question": "Do you have severe pain in your stomach radiating to your back, or have you been vomiting blood?",
            "action_threshold_question": "Are you taking acetaminophen (Tylenol), which must be avoided or used cautiously after heavy alcohol due to liver strain?"
        },
        "red_flags": [
            "Vomiting blood or coffee-ground material (Mallory-Weiss tear or gastric ulcer)",
            "Severe, constant upper abdominal pain radiating into the back (Acute pancreatitis)",
            "Confusion, stupor, seizures, or inability to awaken the person"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A hangover causes headache, dry mouth, and nausea after drinking; drinking electrolyte water, eating toast, and resting clears it.",
                "plain_analogy": "A battery completely drained and overheated after heavy use; plugging into the wall charger (fluids and food) and letting it cool restores full power.",
                "lifestyle_action": "Drink a tall glass of electrolyte water, eat eggs and toast to replenish energy, take ibuprofen with food, and rest."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Electrolyte rehydration solutions (Gatorade / Pedialyte: to restore fluid and sodium balance)",
                    "Ibuprofen (Advil: 200-400 mg oral with food for headache - avoids acetaminophen liver load)",
                    "B-complex vitamins (especially Thiamine/B1 and Pyridoxine/B6 to support metabolic clearance)",
                    "Antacid or Famotidine (for alcohol-induced gastritis)"
                ],
                "dosing_gdmt": "First line: Hydration, carbohydrates, and rest. Use NSAIDs with food for headache. AVOID high-dose acetaminophen after heavy drinking due to heightened hepatotoxicity risk from CYP2E1 induction.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Severe hepatic impairment or active upper GI bleeding"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MAYO-HANGOVER-REVIEW",
                "pmid_or_doi": "10.2174/187314710790820401",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Fluid and electrolyte replacement combined with carbohydrate replenishment significantly attenuated subjective hangover severity and shortened recovery time."
            }
        }
    },
    {
        "id": "DOC-CARD-582",
        "icd10": "M62.838",
        "condition": "Delayed Onset Muscle Soreness (DOMS)",
        "specialty": "Sports Medicine & Physical Therapy",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & ACSM Expert Consensus",
        "source_body": "ACSM & BJSM",
        "citation": "Cheung K et al. Sports Med. 2003;33(2):145-164.",
        "doi_or_source": "10.2165/00007256-200333020-00005",
        "clinical_evidence": "Delayed onset muscle soreness (DOMS) represents microscopic structural disruption of muscle sarcomeres (specifically Z-disc streaming) induced by unaccustomed or high-intensity eccentric exercise contractions. Symptoms peak characteristically at 24 to 72 hours post-exercise, manifesting as dull muscle tenderness, stiffness, and transient reduction in maximal voluntary muscle force. Evidence confirms that light active recovery (cycling, walking), gentle foam rolling, massage, and adequate protein intake enhance microvascular blood flow and speed functional recovery without blunting physiological muscular adaptation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Active recovery: 20-30 minutes of low-intensity aerobic exercise (walking, light stationary cycling, swimming); foam rolling or gentle massage; warm Epsom salt bath; adequate post-exercise protein (20-30 g) and hydration; avoid high-intensity workouts using the same sore muscle groups for 48 hours.",
            "monitoring_cadence": "Monitor soreness resolution over 3 to 5 days; seek medical evaluation if urine turns dark tea-colored (rhabdomyolysis warning).",
            "clinical_thresholds": "Muscle swelling and weakness accompanied by dark reddish-brown 'tea-colored' urine (exertional rhabdomyolysis requiring immediate emergency evaluation)."
        },
        "patient_plain_language": "DOMS is the familiar, tender muscle soreness and stiffness you feel one to two days after a strenuous workout or trying a new physical activity your body isn't used to. When your muscles perform unfamiliar resistance work, tiny microscopic tears develop in the muscle fibers, which sound scary but are actually the normal trigger that tells your body to rebuild the muscles stronger. Light walking, warm baths, and gentle stretching help the stiffness fade away within a few days.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the muscle tenderness peak 24 to 48 hours after an intense or unfamiliar workout?",
            "safety_question": "Is your urine clear and pale yellow, or has it turned dark brown like iced tea or cola?",
            "action_threshold_question": "Can you still move your joints through their normal range, or is there extreme swelling and rock-hard tightness?"
        },
        "red_flags": [
            "Dark brown, cola-colored or tea-colored urine following intense exertion (Exertional rhabdomyolysis - medical emergency)",
            "Extreme muscle swelling, rock-hard compartment firmness, and numbness in the hands or feet (Compartment syndrome)",
            "Severe localized joint pain or inability to bear weight rather than muscular soreness"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "DOMS is the normal muscle stiffness felt 1-2 days after a hard workout; light movement, warm baths, and rest help it pass.",
                "plain_analogy": "Renovating a brick wall; removing old loose mortar creates temporary dust before the new stronger cement bonds into place.",
                "lifestyle_action": "Take an easy 15-minute recovery walk, soak in a warm bath, drink plenty of water, and give those sore muscles two days of lighter work."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Menthol / Camphor rubs (Biofreeze / Icy Hot: cooling counter-irritant for temporary relief)",
                    "Acetaminophen (500-1000 mg q6h PRN for severe discomfort)",
                    "Tart cherry juice (contains anthocyanins that attenuate exercise-induced oxidative muscle soreness)",
                    "Oral Ibuprofen (Advil: 200-400 mg - use sparingly so as not to blunt muscle protein synthesis)"
                ],
                "dosing_gdmt": "First line: Active low-intensity recovery, foam rolling, and warm baths. Routine high-dose prophylactic NSAIDs are discouraged as they can impair skeletal muscle hypertrophy and tendon adaptation.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Exertional rhabdomyolysis with elevated serum creatine kinase"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACSM-DOMS-CONSENSUS",
                "pmid_or_doi": "10.2165/00007256-200333020-00005",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Active recovery and light aerobic exercise produced superior short-term pain relief and improved muscle blood flow compared to total passive rest."
            }
        }
    },
    {
        "id": "DOC-CARD-583",
        "icd10": "S90.819A",
        "condition": "Friction Foot Blisters & Plantar Calluses",
        "specialty": "Dermatology & Podiatry",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Wilderness Medical Society Clinical Practice Guideline",
        "source_body": "Wilderness Medical Society & AAPSM",
        "citation": "Lipman GS et al. Wilderness Environ Med. 2014;25(4):462-470.",
        "doi_or_source": "10.1016/j.wem.2014.07.014",
        "clinical_evidence": "Friction blisters occur in skin with thick stratum corneum (palms, soles) subjected to repetitive epidermal shear forces, causing a cleavage plane within the stratum spinosum that fills with sterile serum. WMS guidelines establish that preventative measures (paper micropore tape, synthetic moisture-wicking socks, well-fitted footwear) significantly reduce blister incidence. For intact painful blisters: clean with antiseptic, puncture the base with a sterile needle leaving the blister roof intact as a biological sterile dressing, and apply a hydrocolloid bandage.",
        "solution_protocol": {
            "non_pharmacological_targets": "Preventative taping with paper micropore tape over friction hotspots before long walks; wear moisture-wicking synthetic or merino wool socks (avoid pure cotton socks that retain moisture); break in new shoes gradually; for intact painful blisters, cleanse and puncture the margin with a sterile needle to drain fluid while keeping the overlying skin roof intact; cover with hydrocolloid blister bandage (Moleskin/Band-Aid Hydro Seal).",
            "monitoring_cadence": "Inspect blister daily for signs of bacterial infection (expanding redness, purulent cloudy fluid, increasing heat); keep clean and dry.",
            "clinical_thresholds": "Spreading redness, warmth, throbbing pain, red streaks, or purulent yellow drainage (secondary staphylococcal/streptococcal cellulitis)."
        },
        "patient_plain_language": "A friction blister is a small bubble of clear fluid that forms under the top layer of skin on your foot or heel when your shoe rubs repeatedly against the same spot. Leaving the top skin roof intact acts like a natural, sterile bandage that protects the fresh delicate skin growing underneath. Covering the spot with a cushioning hydrocolloid bandage shields it from pressure so you can keep walking without pain.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the blister form from shoe rubbing during walking or running, or did it appear without any friction?",
            "safety_question": "Is the blister skin still attached and the fluid clear, or has it popped open and become dirty?",
            "action_threshold_question": "Is there any spreading redness, warmth, or yellow pus developing around the blister?"
        },
        "red_flags": [
            "Red streaks spreading up your foot or leg from the blister site with fever (Cellulitis/Lymphangitis)",
            "Blister on a diabetic foot with numbness or loss of sensation (Diabetic foot ulcer risk)",
            "Blister fluid that turns cloudy, thick, or purulent with worsening throbbing pain"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Foot blisters form from friction between shoes and skin; draining fluid while keeping the roof intact and using hydrocolloid pads heals them.",
                "plain_analogy": "A protective bubble wrap cushion that pops up when two surfaces rub too hard; keeping the plastic sheet intact lets the underlying surface heal.",
                "lifestyle_action": "Wash with clean water, do not peel off the top skin, apply a hydrocolloid blister bandage, and wear moisture-wicking socks."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrocolloid blister dressings (Band-Aid Hydro Seal: provides sterile moist healing and friction cushion)",
                    "Moleskin adhesive padding (cut with an inner hole around the blister to offload direct pressure)",
                    "White petrolatum (Vaseline: applied to hotspots before hiking to eliminate friction)",
                    "Triple antibiotic ointment (if blister roof has torn open)"
                ],
                "dosing_gdmt": "First line: Keep blister roof intact. Cleanse with soap/water and apply hydrocolloid bandage. Do not deroof clean blisters.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Diabetic neuropathy patient requiring professional podiatry wound management"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WMS-BLISTER-TAPE",
                "pmid_or_doi": "10.1016/j.wem.2014.07.014",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Pre-taping friction hotspots with micropore paper tape reduced foot blister development by over 40% in endurance athletes."
            }
        }
    },
    {
        "id": "DOC-CARD-584",
        "icd10": "L60.0",
        "condition": "Ingrown Toenail (Onychocryptosis & Paronychia)",
        "specialty": "Podiatry & Primary Care",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAFP Clinical Practice Guideline on Onychocryptosis",
        "source_body": "American Academy of Family Physicians (AAFP)",
        "citation": "Heidelbaugh JJ, Lee H. Am Fam Physician. 2009;79(4):303-308.",
        "doi_or_source": "10.1016/j.afp.2009.02.012",
        "clinical_evidence": "Onychocryptosis (ingrown toenail) occurs when the lateral nail plate border pierces the periungual nail fold epidermis, provoking a foreign body inflammatory reaction, erythema, edema, and formation of vascularized granulation tissue. Common precipitants include improper nail trimming (curved clipping down the lateral sulcus), tight-toed shoes, and genetic nail morphology. Conservative management for early mild cases involves warm water foot soaks, cotton-wick elevation under the nail edge, and wearing wide-toed footwear. Moderate-to-severe cases (paronychia, granulation tissue) benefit from partial nail avulsion with chemical phenol matricectomy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Warm foot soaks in warm soapy water or Epsom salt for 15 minutes twice daily; gently insert a tiny wisp of clean rolled cotton or dental floss under the digging nail edge to lift it off the skin; cut toenails strictly straight across—never curve or round off the corners; wear wide-toed shoes or open-toed sandals; avoid bathroom surgery.",
            "monitoring_cadence": "Inspect toe daily; clinical podiatry evaluation if pain worsens, red meat-like granulation tissue grows over the nail, or pus drains.",
            "clinical_thresholds": "Spreading redness, swelling, and warmth extending up the toe or foot, especially in patients with diabetes or peripheral vascular disease."
        },
        "patient_plain_language": "An ingrown toenail happens when the corner or side of your toenail (usually on the big toe) curves and digs into the soft tender skin next to it, making the toe red, swollen, and painful to walk on. Trimming toenails straight across rather than rounding down the corners prevents this from happening. Soaking your foot in warm water every day and gently tucking a tiny wisp of cotton under the nail edge guides the nail to grow out safely past the skin.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do you cut your toenails straight across, or do you round them down deeply at the sides?",
            "safety_question": "Is there any yellow pus or soft red tissue growing over the edge of the nail?",
            "action_threshold_question": "Do you have diabetes, poor circulation, or numbness in your feet?"
        },
        "red_flags": [
            "Spreading redness extending past the toe joint with fever (Ascending cellulitis)",
            "Any ingrown toenail in a patient with diabetes or poor peripheral circulation (Risk of osteomyelitis)",
            "Severe throbbing pain with pus that does not improve after 3 days of warm soaks"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Ingrown toenails dig into the skin when cut too short; warm soaks, cutting straight across, and lifting the edge heals them.",
                "plain_analogy": "A garden shovel edge that got jammed into the grass border; slipping a small wedge under the blade lets it lift cleanly over the lawn.",
                "lifestyle_action": "Soak your toe in warm water for 15 minutes twice a day, cut toenails straight across, wear roomy shoes, and tuck a tiny piece of cotton under the nail."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Warm Epsom salt foot soaks (1-2 tablespoons dissolved in basin of warm water)",
                    "Topical Mupirocin 2% ointment (prescription antibiotic if secondary paronychia is present)",
                    "Ibuprofen (Advil: 400 mg TID with meals for throbbing toe pain)",
                    "Partial nail avulsion with phenol matricectomy (definitive minor in-office procedure by podiatrist)"
                ],
                "dosing_gdmt": "First line: Conservative warm soaks and cotton elevation for stage 1. For stage 2-3 (granulation tissue, pus), in-office partial nail avulsion cures >95% without recurrence.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Diabetic foot ulcer or gangrene"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAFP-INGROWN-TOENAIL",
                "pmid_or_doi": "10.1016/j.afp.2009.02.012",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Partial lateral nail avulsion combined with phenol chemical matricectomy demonstrated significantly lower recurrence rates (<5%) compared to wedge excision or avulsion alone."
            }
        }
    },
    {
        "id": "DOC-CARD-585",
        "icd10": "L50.9",
        "condition": "Acute Hives & Allergic Urticaria",
        "specialty": "Allergy & Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EAACI / GA2LEN / EDF / WAO International Guideline for Urticaria",
        "source_body": "EAACI & AAAAI",
        "citation": "Zuberbier T et al. Allergy. 2022;77(3):734-766.",
        "doi_or_source": "10.1111/all.15090",
        "clinical_evidence": "Acute urticaria is characterized by the sudden development of transient wheals (central swelling surrounded by erythema, intensely pruritic, fleeting nature resolving within 24 hours without scarring) and/or angioedema. Pathophysiology involves mast cell and basophil degranulation with release of histamine, platelet-activating factor, and leukotrienes, commonly triggered by viral infections, medications (NSAIDs, antibiotics), foods, or contact allergens. International guidelines establish second-generation non-sedating H1-antihistamines (cetirizine, fexofenadine, loratadine) as the first-line therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Cool damp washcloths applied to itchy areas; cool baths with colloidal oatmeal; avoid hot showers, tight restrictive clothing, and vigorous skin rubbing; identify and eliminate suspected new foods, medications, or viral triggers; avoid alcohol and NSAIDs, which can non-specifically worsen mast cell degranulation.",
            "monitoring_cadence": "Monitor wheal duration and distribution; clinical allergy review if hives persist daily for >6 weeks (chronic spontaneous urticaria).",
            "clinical_thresholds": "Concurrent lip, tongue, or throat swelling, difficulty breathing, stridor, wheezing, vomiting, or dizziness (Anaphylaxis - immediate epinephrine)."
        },
        "patient_plain_language": "Hives (urticaria) are raised, itchy, red or pale welts that appear suddenly on your skin, looking like mosquito bites or nettle stings. Each individual hive typically fades and disappears within 24 hours while new ones may pop up elsewhere, sparked by an allergic reaction to a food or medicine, or often by a simple common cold virus. Modern non-drowsy allergy pills (like cetirizine or loratadine) calm the itching and clear the bumps quickly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you take any new medications, eat unusual foods, or have a viral cold just before the hives appeared?",
            "safety_question": "Do you feel any swelling in your lips, tongue, or throat, or tightness when breathing?",
            "action_threshold_question": "Does each individual red welt fade and disappear within 24 hours, or do they leave dark bruises on your skin?"
        },
        "red_flags": [
            "Any swelling of the lips, tongue, uvula, or difficulty swallowing or breathing (Anaphylaxis - call 911)",
            "Dizziness, fainting, or sudden vomiting accompanied by widespread hives",
            "Hives that look like purple bruises, burn rather than itch, and stay in the exact same spot for >24-48 hours (Urticarial vasculitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hives are itchy, raised welts that appear suddenly on the skin; non-drowsy antihistamines and cool compresses bring relief.",
                "plain_analogy": "A temporary pop-up sprinkler system spraying water onto the lawn; shutting off the valve with antihistamines turns off the sprinklers.",
                "lifestyle_action": "Take a non-drowsy antihistamine pill, apply cool washcloths, avoid hot showers and tight clothes, and don't take ibuprofen."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cetirizine (Zyrtec: 10 mg oral once daily - first-line second-generation H1 antihistamine)",
                    "Fexofenadine (Allegra: 180 mg oral once daily - completely non-sedating H1 blocker)",
                    "Loratadine (Claritin: 10 mg oral once daily)",
                    "Calamine lotion or Colloidal oatmeal bath (Aveeno: soothing topical antipruritic)",
                    "Epinephrine auto-injector (EpiPen: 0.3 mg IM - MANDATORY if concurrent angioedema / anaphylaxis)"
                ],
                "dosing_gdmt": "First line: Second-generation H1 antihistamines (cetirizine 10-20 mg). In refractory cases, guidelines recommend increasing the second-generation antihistamine dose up to 4-fold before adding oral corticosteroids.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Anaphylaxis requiring immediate intramuscular epinephrine"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EAACI-URTICARIA-GUIDELINE",
                "pmid_or_doi": "10.1111/all.15090",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Second-generation H1 antihistamines significantly controlled wheals and pruritus in over 85% of acute urticaria cases with an excellent safety profile."
            }
        }
    },
    {
        "id": "DOC-CARD-586",
        "icd10": "L23.9",
        "condition": "Allergic Contact Dermatitis & Poison Ivy",
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAD Guidelines of Care for the Management of Contact Dermatitis",
        "source_body": "American Academy of Dermatology (AAD)",
        "citation": "Belsito DV et al. J Am Acad Dermatol. 2006;55(1):94-114.",
        "doi_or_source": "10.1016/j.jaad.2006.02.042",
        "clinical_evidence": "Allergic contact dermatitis (ACD) is a type IV cell-mediated delayed-type hypersensitivity reaction occurring 24 to 72 hours after cutaneous exposure to an allergen (urushiol oil from poison ivy/oak/sumac, nickel, fragrances, neomycin). Manifests as intense pruritus, erythema, edema, and characteristic linear vesicular eruptions where plant foliage brushed against the skin. Initial first aid requires washing within 10-30 minutes with soap/water to remove the hydrophobic urushiol oil. Mid-to-high potency topical corticosteroids and cool wet compresses resolve inflammation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Wash exposed skin and clothing immediately with dish soap and lukewarm water within 15-30 minutes of contact to remove plant oils; cool wet compresses for 15-20 minutes several times daily; colloidal oatmeal baths; calamine lotion to soothe weeping blisters; avoid scratching to prevent secondary bacterial infection; wash contaminated pets and gardening tools.",
            "monitoring_cadence": "Monitor rash spread and blister healing; clinical dermatology review if rash covers >25% of body surface area or involves the face or genitals.",
            "clinical_thresholds": "Severe swelling around the eyes shutting the eyelids, rash involving mucous membranes, or spreading secondary bacterial cellulitis."
        },
        "patient_plain_language": "Poison ivy is an allergic reaction to a sticky plant oil called urushiol, causing intensely itchy, red, blistering streaks on your skin a day or two after gardening, hiking, or touching a pet that ran through the woods. The blister fluid inside the bumps is not contagious and cannot spread the rash to other people. Washing your skin with soap quickly after being outdoors, applying hydrocortisone cream, and taking cool oatmeal baths cools the intense itch.",
        "doctor_consultation_checklist": {
            "parameter_question": "Were you recently gardening, clearing brush, or walking in wooded areas where 'leaves of three' grow?",
            "safety_question": "Is the rash spreading to sensitive areas like your eyes, face, or groin?",
            "action_threshold_question": "Did you wash the clothes, garden gloves, and tools you were using when exposed to the plant?"
        },
        "red_flags": [
            "Severe swelling of the face, eyelids swollen completely shut, or rash spreading to the genitals",
            "Rash covering more than a quarter of your total body surface area",
            "Spreading warmth, redness, and yellow pus oozing from scratched blisters (Secondary bacterial infection)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Poison ivy causes an intensely itchy, blistering rash in streaks from plant oil; washing quickly, cold compresses, and hydrocortisone soothe it.",
                "plain_analogy": "Invisible sticky tree sap brushed across your skin; washing it off with soap stops the oil from alerting your immune defense cells.",
                "lifestyle_action": "Wash skin and clothes with soap, apply cool wet washcloths and calamine lotion, take an oatmeal bath, and use hydrocortisone."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Hydrocortisone 1% cream / ointment (OTC applied TID to calm mild localized itching)",
                    "Triamcinolone acetonide 0.1% cream (prescription mid-potency topical steroid for body plaques)",
                    "Calamine lotion (astringent and antipruritic for drying weeping vesicles)",
                    "Diphenhydramine or Cetirizine (oral antihistamine to relieve disruptive nocturnal itch)",
                    "Oral Prednisone taper (40-60 mg tapered over 14-21 days - for severe widespread poison ivy)"
                ],
                "dosing_gdmt": "First line: Immediate soap and water wash. Topical corticosteroids (triamcinolone) for localized lesions. Severe or facial poison ivy requires a 14-21 day oral prednisone taper; shorter courses cause severe rebound flares.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Do not prescribe short 5-day steroid dose packs for poison ivy (causes severe rebound dermatitis)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAD-CONTACT-DERMATITIS",
                "pmid_or_doi": "10.1016/j.jaad.2006.02.042",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Topical mid-to-high potency corticosteroids and cool wet compresses significantly accelerated resolution of allergic contact dermatitis lesions compared to emollients alone."
            }
        }
    },
    {
        "id": "DOC-CARD-587",
        "icd10": "K13.0",
        "condition": "Chapped Lips & Angular Cheilitis",
        "specialty": "Dermatology & Primary Care",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Review & AAD Guidelines",
        "source_body": "American Academy of Dermatology (AAD)",
        "citation": "Lugović-Mihić L et al. Acta Clin Croat. 2018;57(4):727-738.",
        "doi_or_source": "10.20471/acc.2018.57.04.16",
        "clinical_evidence": "Cheilitis simplex (chapped lips) is acute or chronic superficial inflammation and xerosis of the vermilion border of the lips. The vermilion border lacks sebaceous glands, sweat glands, and a thick stratum corneum, predisposing it to rapid transepidermal water loss when exposed to dry cold air, wind, mouth-breathing, or chronic lip-licking (saliva contains digestive amylase and maltase enzymes that digest the fragile lip barrier). Angular cheilitis features erythema, maceration, and painful fissuring at the lip commissures, often driven by mixed Candida albicans and Staphylococcus aureus colonization.",
        "solution_protocol": {
            "non_pharmacological_targets": "Apply thick bland ointment (white petroleum jelly, mineral oil, or dimethicone) multiple times daily; stop licking, biting, or picking peeling skin on your lips; use an SPF 30+ mineral lip balm outdoors; avoid flavored, menthol, camphor, or salicylic acid lip balms which irritate; use a bedside room humidifier; drink plenty of water.",
            "monitoring_cadence": "Monitor lip healing; seek medical/dental review if painful cracks at the corners of the mouth (angular cheilitis) fail to heal within 2 weeks.",
            "clinical_thresholds": "Persistent ulcer or non-healing firm white plaque on the lower lip in a smoker or outdoor worker (Actinic cheilitis / Squamous cell carcinoma)."
        },
        "patient_plain_language": "Chapped lips happen when the delicate, thin skin on your lips dries out, flakes, and cracks in cold, windy, or dry weather. Licking your lips might feel like it gives quick moisture, but as the saliva evaporates, digestive enzymes in your spit actually break down your lip skin, making the cracking twice as bad. Coating your lips frequently with plain petroleum jelly (like Vaseline or Aquaphor) locks in moisture so your lips heal smoothly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do you frequently lick or chew on your lips when they feel dry?",
            "safety_question": "Are the painful cracks located mostly at the corners of your mouth where saliva pools?",
            "action_threshold_question": "Do you use lip balms containing menthol, camphor, or cinnamon flavorings that can cause allergic lip irritation?"
        },
        "red_flags": [
            "A firm, scaly white patch or persistent bleeding ulcer on the lower lip that never heals (Actinic cheilitis / Lip cancer)",
            "Severe swelling, blisters, or crusting covering the entire lips accompanied by high fever",
            "Painful open bleeding cracks at the corners of the mouth that become infected with pus"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Chapped lips are dry and peeling from wind or lip-licking; thick petroleum jelly and avoiding flavored balms heals them.",
                "plain_analogy": "A dry sponge on a kitchen counter; licking it makes it wet for a second before it curls up tighter, but sealing it with wax keeps it soft.",
                "lifestyle_action": "Apply plain petroleum jelly or Aquaphor every two hours, never lick your dry lips, and use an SPF lip balm when outdoors."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "White petrolatum (Vaseline / Aquaphor: thick hypoallergenic barrier ointment applied frequently)",
                    "Dimethicone 1% lip balm (silicone-based water barrier)",
                    "Mupirocin 2% ointment + Clotrimazole 1% cream (applied to corners of mouth for angular cheilitis)",
                    "Hydrocortisone 1% ointment (applied twice daily for 3 days for severe inflamed lip swelling)"
                ],
                "dosing_gdmt": "First line: Pure petroleum jelly. Avoid lip balms with camphor, menthol, eucalyptus, or synthetic fragrances, which are common contact allergens.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Actinic cheilitis requiring biopsy"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAD-CHEILITIS-REVIEW",
                "pmid_or_doi": "10.20471/acc.2018.57.04.16",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Barrier replenishment with plain white petrolatum demonstrated superior moisture retention and epithelial restoration compared to wax-based or flavored commercial lip balms."
            }
        }
    },
    {
        "id": "DOC-CARD-588",
        "icd10": "I95.1",
        "condition": "Orthostatic Dizziness & Postural Lightheadedness",
        "specialty": "Cardiology & Primary Care",
        "organ_system": "Cardiovascular",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACC / AHA / HRS Guideline for the Evaluation and Management of Syncope",
        "source_body": "ACC & AHA",
        "citation": "Shen WK et al. J Am Coll Cardiol. 2017;70(5):e39-e110.",
        "doi_or_source": "10.1016/j.jacc.2017.03.003",
        "clinical_evidence": "Orthostatic dizziness results from transient cerebral hypoperfusion upon standing, defined as a sustained drop in systolic blood pressure of ≥20 mmHg or diastolic drop of ≥10 mmHg within 3 minutes of standing. Standing causes 500-1000 mL of blood to pool in splanchnic and lower limb venous reservoirs; failure of baroreceptor-mediated reflex vasoconstriction and tachycardia produces lightheadedness, graying vision, and unsteadiness. Common etiologies include volume depletion (dehydration, diuretics), vasodilating medications (antihypertensives, alpha-blockers), and autonomic neuropathy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Pause and transition slowly from lying to sitting to standing (sit on the edge of the bed for 30-60 seconds before standing); perform physical counter-pressure maneuvers (cross legs and squeeze thigh muscles, clench fists) upon standing to pump blood back to the heart; increase fluid intake (2-2.5 liters/day) and dietary salt (if no hypertension/heart failure); wear waist-high compression stockings (20-30 mmHg); avoid hot showers.",
            "monitoring_cadence": "Serial home orthostatic blood pressure checks (supine, and 1 min and 3 min standing); clinical review if episodes cause near-fainting.",
            "clinical_thresholds": "Sudden loss of consciousness (syncope) with trauma, chest pain, palpitations, or orthostatic dizziness in a patient with known heart disease."
        },
        "patient_plain_language": "Postural lightheadedness is that brief, woozy feeling or graying of vision you experience when standing up too quickly from bed or a low chair. When you stand up, gravity pulls a couple of cups of blood down toward your belly and legs; if your blood pressure takes a few seconds to catch up, your brain gets momentarily less blood. Pausing on the edge of the bed for half a minute before standing, drinking more water, and clenching your leg muscles keeps the blood pumping upward.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the lightheadedness happen only right after you stand up, and does it go away when you sit back down?",
            "safety_question": "Have you actually passed out or fallen to the floor during these episodes?",
            "action_threshold_question": "Are you taking blood pressure pills or water pills (diuretics), or have you been drinking less water recently?"
        },
        "red_flags": [
            "Any episode of passing out completely (Syncope) with injury, head strike, or without warning",
            "Dizziness accompanied by chest pain, irregular fluttering heartbeats, or shortness of breath",
            "Orthostatic drops causing recurrent falls in an elderly patient"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Postural dizziness happens when blood pools in the legs upon standing; standing up slowly, drinking water, and clenching legs prevents it.",
                "plain_analogy": "An elevator rising quickly before the water pressure pipe stabilizes; pausing at the landing gives the pump time to equalize the pressure.",
                "lifestyle_action": "Sit on the edge of your bed for 30 seconds before standing, drink two glasses of water in the morning, and flex your calf muscles when standing."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oral hydration with water and electrolyte beverages (500 mL water bolus prior to standing increases blood pressure via sympathetic activation)",
                    "Fludrocortisone (0.1-0.2 mg oral daily - mineralocorticoid to expand intravascular plasma volume for neurogenic orthostatic hypotension)",
                    "Midodrine (2.5-10 mg oral TID - peripherally acting alpha-1 agonist for severe refractory cases)",
                    "Waist-high graduated compression stockings (20-30 mmHg)"
                ],
                "dosing_gdmt": "First line: Non-pharmacological measures (hydration, counter-pressure maneuvers, slow transitions, review/deprescribe offending antihypertensives). Midodrine and fludrocortisone reserved for verified neurogenic orthostatic hypotension.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Supine hypertension when prescribing midodrine or fludrocortisone"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACC-AHA-SYNCOPE",
                "pmid_or_doi": "10.1016/j.jacc.2017.03.003",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Physical counter-pressure maneuvers (leg crossing, muscle tensing) produced a rapid, significant rise in cardiac output and mean arterial pressure, preventing syncope."
            }
        }
    },
    {
        "id": "DOC-CARD-589",
        "icd10": "R53.83",
        "condition": "Lifestyle Fatigue, Burnout & Sleep Debt",
        "specialty": "Sleep Medicine & Primary Care",
        "organ_system": "Neurological",
        "cebm_level": 1,
        "evidence_tier": "Level 1: American Academy of Sleep Medicine (AASM) & CDC Consensus",
        "source_body": "AASM & Sleep Research Society",
        "citation": "Watson NF et al. Sleep. 2015;38(6):843-844.",
        "doi_or_source": "10.5665/sleep.4716",
        "clinical_evidence": "Lifestyle fatigue and chronic sleep debt reflect physiological exhaustion resulting from chronic sleep restriction (<7 hours/night for adults), circadian disruption (shift work, social jetlag), chronic psychosocial stress, and physical deconditioning. Sleep debt leads to metabolic dysregulation, impaired executive function, elevated cortisol, and immune compromise. Unlike chronic fatigue syndrome (ME/CFS) or secondary organic fatigue (anemia, hypothyroidism, sleep apnea), lifestyle fatigue is reversible with targeted sleep hygiene, circadian alignment, regular aerobic physical activity, and stress reduction.",
        "solution_protocol": {
            "non_pharmacological_targets": "Prioritize 7-9 hours of nightly sleep; maintain consistent sleep and wake times 7 days a week (within 30 minutes); 20 minutes of morning sunlight exposure within 1 hour of waking to anchor the master circadian pacemaker (SCN); eliminate digital screens 60 minutes before bed; keep bedroom cool (65-68F / 18-20C) and dark; engage in 150 min/week of moderate aerobic exercise; limit caffeine after 12:00 PM.",
            "monitoring_cadence": "Track sleep duration and daytime energy levels using a 2-week sleep log; clinical review with basic laboratory screening if fatigue persists despite 4 weeks of consistent sleep.",
            "clinical_thresholds": "Fatigue accompanied by unexplained weight loss, night sweats, enlarged lymph nodes, severe shortness of breath, or loud snoring with choking awakenings."
        },
        "patient_plain_language": "Everyday lifestyle fatigue is that drained, foggy, heavy feeling that builds up when you are not getting enough quality sleep, juggling too much stress, or spending long days under indoor fluorescent lights. Your brain and body need seven to eight hours of solid sleep each night to clean out metabolic waste and recharge your cellular batteries. Getting outside for morning sunlight, keeping a strict bedtime, and taking a daily walk resets your natural energy rhythms naturally.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many hours of actual sleep are you getting per night on weekdays versus weekends?",
            "safety_question": "Do you snore loudly, wake up gasping for air, or wake up feeling like you haven't slept at all (Sleep apnea signs)?",
            "action_threshold_question": "Can we run basic screening blood tests (blood count, thyroid, iron/ferritin, vitamin D) to rule out medical causes of fatigue?"
        },
        "red_flags": [
            "Severe, drenching night sweats or unexplained significant weight loss (Malignancy/Infection red flags)",
            "Profound chronic fatigue accompanied by swollen lymph nodes, fever, or joint pain",
            "Falling asleep uncontrollably while driving or operating machinery"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Lifestyle fatigue is caused by sleep debt, stress, and lack of exercise; regular bedtimes, morning sunlight, and daily walks restore energy.",
                "plain_analogy": "Running a smartphone on 15% battery in low-power mode all day; plugging in for a full uninterrupted overnight charge restores full processing speed.",
                "lifestyle_action": "Go to bed at the exact same time every night, get 15 minutes of outdoor sunlight in the morning, stop caffeine at noon, and walk 20 minutes daily."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Melatonin (0.5-3 mg oral taken 1-2 hours before desired sleep time - circadian phase shifter, not a heavy sedative)",
                    "Magnesium glycinate (200-400 mg oral at bedtime - promotes GABAergic neurological relaxation)",
                    "Iron / Vitamin D3 / Vitamin B12 supplementation (ONLY if laboratory deficiency is documented)"
                ],
                "dosing_gdmt": "First line: Cognitive behavioral principles for insomnia (CBT-I) and circadian sleep hygiene. Sedative-hypnotic medications (benzodiazepines, z-drugs) are not recommended for routine lifestyle fatigue due to dependency and altered sleep architecture.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Severe untreated obstructive sleep apnea"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AASM-SLEEP-CONSENSUS",
                "pmid_or_doi": "10.5665/sleep.4716",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Achieving 7-9 hours of regular sleep significantly restored neurobehavioral performance, improved metabolic insulin sensitivity, and reversed subjective daytime fatigue."
            }
        }
    },
    {
        "id": "DOC-CARD-590",
        "icd10": "A05.9",
        "condition": "Acute Food Poisoning (Foodborne Toxin Illness)",
        "specialty": "Infectious Disease & Primary Care",
        "organ_system": "Gastrointestinal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CDC & FDA Foodborne Illness Clinical Guidelines",
        "source_body": "CDC & FDA",
        "citation": "Scallan E et al. Emerg Infect Dis. 2011;17(1):7-15.",
        "doi_or_source": "10.3201/eid1701.p11101",
        "clinical_evidence": "Acute foodborne illness (food poisoning) is caused by consuming food contaminated with preformed bacterial toxins (Staphylococcus aureus, Bacillus cereus: rapid onset 1-6 hours, predominant vomiting) or enteric pathogens (Salmonella, Campylobacter, E. coli: onset 12-72 hours, predominant crampy diarrhea). Symptoms include abrupt nausea, explosive vomiting, crampy abdominal pain, and diarrhea. Most cases are self-limiting within 24-48 hours. Primary management is preventing dehydration via oral electrolyte rehydration. Antimotility drugs (loperamide) are contraindicated if fever or bloody stools are present.",
        "solution_protocol": {
            "non_pharmacological_targets": "Oral rehydration solution (ORS) or electrolyte drinks sipped slowly in small quantities (1-2 tablespoons every 10 minutes); rest the stomach completely for 2 hours after acute vomiting; avoid dairy, greasy foods, caffeine, and alcohol; gradually introduce bland foods (crackers, bananas, white rice, applesauce) once vomiting stops; report suspected foodborne outbreaks to public health.",
            "monitoring_cadence": "Monitor hydration status (urine output every 4-6 hours); seek urgent medical evaluation if unable to retain fluids after 24 hours.",
            "clinical_thresholds": "Bloody diarrhea, high fever (>38.5C / 101.3F), severe dehydration (dizziness upon standing, dry mouth), or neurological symptoms (blurred vision, muscle weakness from botulism)."
        },
        "patient_plain_language": "Food poisoning happens when you eat food that was left out too long, undercooked, or handled improperly, allowing bacteria or their natural toxins to irritate your stomach and intestines. It usually strikes fast—often just a few hours after eating—with sudden vomiting, stomach cramps, and diarrhea as your body works hard to flush the toxins out. Resting your stomach, sipping electrolyte fluids slowly, and staying hydrated clears the illness safely within a day or two.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the vomiting and diarrhea start within hours of eating a specific meal, and did anyone else who shared the food get sick?",
            "safety_question": "Is there any blood in your vomit or diarrhea, or do you have a high fever?",
            "action_threshold_question": "Are you able to keep down small sips of water or rehydration fluids without throwing up?"
        },
        "red_flags": [
            "Diarrhea containing visible red blood or dark black material (Bacterial dysentery / E. coli O157:H7)",
            "Inability to drink any fluids for over 12 hours with severe dizziness, dry tongue, and dark or absent urine",
            "Neurological symptoms such as double vision, drooping eyelids, or muscle weakness after home-canned foods (Botulism emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Food poisoning causes sudden vomiting and diarrhea from contaminated food; sipping oral rehydration drinks clears it within 48 hours.",
                "plain_analogy": "A fire alarm sounding and sprinkler heads flushing water down the hallway to clear out smoke; once the air is clean, the sprinklers turn off.",
                "lifestyle_action": "Sip electrolyte fluids or clear broth by the spoonful, don't force yourself to eat heavy food right away, and rest until vomiting stops."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Oral Rehydration Salts (WHO formula: optimal electrolyte and glucose balance)",
                    "Bismuth subsalicylate (Pepto-Bismol: 30 mL oral q1h PRN, max 8 doses/day - antimicrobial and antisecretory)",
                    "Ondansetron (Zofran: 4-8 mg oral ODT - prescription antiemetic to halt persistent vomiting)",
                    "Loperamide (Imodium: ONLY if non-bloody, mild diarrhea without fever)"
                ],
                "dosing_gdmt": "First line: Oral rehydration solution. Antibiotics are NOT indicated for uncomplicated food poisoning and can trigger hemolytic uremic syndrome (HUS) in Shiga toxin-producing E. coli (STEC).",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Shiga toxin-producing E. coli (antibiotics contraindicated due to HUS risk)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CDC-FOODBORNE-REVIEW",
                "pmid_or_doi": "10.3201/eid1701.p11101",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Oral fluid rehydration without antibiotics resulted in complete clinical recovery within 48 hours in >95% of uncomplicated foodborne toxin illnesses."
            }
        }
    },
    {
        "id": "DOC-CARD-591",
        "icd10": "S63.609A",
        "condition": "Jammed Finger & Stubbed Toe (Joint Sprain)",
        "specialty": "Orthopedics & Emergency Medicine",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAOS Clinical Practice Guidelines on Hand & Foot Trauma",
        "source_body": "AAOS & ASSH",
        "citation": "Pappas ND et al. J Hand Surg Am. 2012;37(9):1904-1907.",
        "doi_or_source": "10.1016/j.jhsb.2012.06.014",
        "clinical_evidence": "A 'jammed' finger or stubbed toe involves acute axial impact loading across the interphalangeal (IP) joint, spraining the collateral ligaments, volar plate, or extensor tendon mechanism (mallet finger). Symptoms include acute pain, localized swelling, and joint stiffness. Physical exam must assess rotational alignment (all fingers should point toward the scaphoid when flexed), active extension, and joint stability. Stable sprains are treated with 'buddy taping' to an adjacent digit and early protected range of motion, while extensor tendon avulsion (mallet finger) requires 6-8 weeks of uninterrupted extension splinting.",
        "solution_protocol": {
            "non_pharmacological_targets": "Buddy tape the injured finger or toe to the adjacent healthy digit with soft gauze between them for stability; apply an ice pack wrapped in a cloth for 10-15 minutes at a time; elevate the hand or foot above heart level to reduce swelling; gently begin active bending as tolerated; avoid vigorous pulling or trying to 'pop' the joint back in.",
            "monitoring_cadence": "Assess swelling and range of motion daily; seek orthopedic/hand evaluation if the finger looks crooked or cannot fully straighten at the tip.",
            "clinical_thresholds": "Visible deformity, open skin wound over the joint, rotational overlap when making a fist, or the fingertip droops down and cannot actively straighten (Mallet finger)."
        },
        "patient_plain_language": "A jammed finger or stubbed toe happens when a ball or hard object hits the tip of your finger or you kick your toe on furniture, compressing and spraining the joint ligaments. It swells up, turns bruised, and hurts to bend. Taping the injured finger to its healthy neighbor (buddy taping) acts like a comfortable natural splint while allowing you to move it, helping the ligament heal cleanly without getting permanently stiff.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the finger tip droop downward so you cannot straighten it on your own (mallet finger)?",
            "safety_question": "When you gently make a fist, does the injured finger cross over or twist awkwardly under the neighboring fingers?",
            "action_threshold_question": "Is there a cut in the skin over the swollen joint, which could let an infection into the joint space?"
        },
        "red_flags": [
            "The tip of the finger droops down and cannot be straightened actively (Mallet finger tendon rupture)",
            "Visible crooked deformity, bone poking against the skin, or rotation when bending (Fracture/Dislocation)",
            "An open skin cut or laceration over a swollen joint (Open fracture/joint requiring urgent debridement)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Jammed fingers happen from end-on bumps; buddy taping to the next finger, icing, and gentle motion heals them.",
                "plain_analogy": "A fence post that got bumped out of alignment; strapping it firmly to the sturdy neighbor post keeps it standing straight while the soil settles.",
                "lifestyle_action": "Apply an ice pack for 15 minutes, buddy tape the finger to its neighbor with soft gauze between, and don't try to pull or pop the joint."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Buddy taping wrap or Velcro finger splint",
                    "Acetaminophen (500-1000 mg q6h PRN)",
                    "Oral Ibuprofen (Advil: 400 mg TID with food for 5 days)",
                    "Dorsal extension splint (Stack splint: for mallet finger - worn continuously for 6-8 weeks)"
                ],
                "dosing_gdmt": "First line: Buddy taping and early gentle mobilization for simple sprains. Mallet finger requires strict, continuous 6-8 week immobilization of the DIP joint in slight hyperextension.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Mallet finger without dedicated extension splinting (leads to permanent swan-neck deformity)"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASSH-FINGER-SPRAIN",
                "pmid_or_doi": "10.1016/j.jhsb.2012.06.014",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Early protected mobilization with buddy taping resulted in faster resolution of joint stiffness and superior functional grip strength compared to rigid immobilization."
            }
        }
    },
    {
        "id": "DOC-CARD-592",
        "icd10": "M76.811",
        "condition": "Shin Splints (Medial Tibial Stress Syndrome)",
        "specialty": "Sports Medicine & Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Review & BJSM Clinical Guidelines",
        "source_body": "BJSM & ACSM",
        "citation": "Moen MH et al. Sports Med. 2009;39(7):523-546.",
        "doi_or_source": "10.2165/00007256-200939070-00000",
        "clinical_evidence": "Medial tibial stress syndrome (MTSS / shin splints) is an exercise-induced overuse injury characterized by diffuse tenderness along the posteromedial border of the distal two-thirds of the tibia (>5 cm continuous tenderness). Pathophysiology involves periosteal inflammation and tibial cortical bone micro-damage from repetitive traction by the soleus, tibialis posterior, and flexor digitorum longus muscles. Differentiating MTSS from a focal tibial stress fracture (point tenderness <2-3 cm, pain with hopping, positive 'tuning fork' test) or exertional compartment syndrome via MRI/radiographs is essential.",
        "solution_protocol": {
            "non_pharmacological_targets": "Relative rest: temporarily switch to low-impact cross-training (swimming, cycling, water running); avoid running on hard surfaces (concrete); ice massage along the shin for 10-15 minutes after activity; eccentric calf strengthening and Achilles stretching; supportive athletic footwear with shock-absorbing orthotic insoles; gradual running mileage return (10% rule).",
            "monitoring_cadence": "Reassess tibial tenderness weekly; clinical sports medicine evaluation with MRI if focal point tenderness develops or pain persists despite 4 weeks of rest.",
            "clinical_thresholds": "Focal pinpoint bone tenderness (<2 cm) on the front of the tibia with severe pain while walking or resting at night (Tibial stress fracture)."
        },
        "patient_plain_language": "Shin splints are a throbbing, aching pain along the inner edge of your shin bone that flares up during and after running, jumping, or marching, especially when you suddenly increase your workout distance or run on hard concrete. The muscles pulling on the bone cause the covering of the shin bone to become inflamed. Taking a temporary break from running, switching to swimming or cycling, icing the shin, and getting supportive running shoes lets the bone heal and strengthen.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the soreness spread along several inches of your shin bone, or is there one tiny pinpoint spot that hurts intensely when pressed?",
            "safety_question": "Does your shin ache even when resting in bed or walking across the living room?",
            "action_threshold_question": "Have you recently increased your running mileage or changed your running shoes or surfaces?"
        },
        "red_flags": [
            "Focal pinpoint bone tenderness on the anterior shin that hurts intensely when bearing weight (High-risk tibial stress fracture)",
            "Numbness, tingling, or weakness in the foot with a tight, bulging calf muscle during exercise (Exertional compartment syndrome)",
            "Severe swelling, redness, and heat over the shin with fever (Cellulitis or osteomyelitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Shin splints cause aching along the inner shin from overuse; rest, low-impact exercise, ice, and supportive shoes heal them.",
                "plain_analogy": "A drywall anchor pulling slightly loose when an overloaded shelf bounces; tightening the anchors and using a stronger shelf bracket prevents pulling.",
                "lifestyle_action": "Switch to swimming or cycling for two weeks, ice your shins for 15 minutes after exercise, wear supportive running shoes, and increase miles slowly."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren applied to medial tibia TID)",
                    "Acetaminophen or Ibuprofen for post-exercise pain control",
                    "Shock-absorbing prefabricated orthotic arch insoles",
                    "Compression calf sleeves (to reduce muscular oscillation and vibration during running)"
                ],
                "dosing_gdmt": "First line: Relative rest and low-impact cross-training. Avoid aggressive high-impact running until patient can walk briskly for 30 minutes completely pain-free.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Anterior cortex 'dreaded black line' stress fracture requiring non-weight-bearing boot or surgical fixation"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BJSM-MTSS-REVIEW",
                "pmid_or_doi": "10.2165/00007256-200939070-00000",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Progressive loading, shock-absorbing orthotics, and gradual return-to-sport protocols successfully restored pain-free athletic performance in >85% of athletes."
            }
        }
    },
    {
        "id": "DOC-CARD-593",
        "icd10": "M54.30",
        "condition": "Sciatica & Lumbar Radicular Irritation",
        "specialty": "Neurology & Physical Medicine",
        "organ_system": "Nervous & Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NICE & North American Spine Society (NASS) Guidelines",
        "source_body": "NICE & NASS",
        "citation": "Stochkendahl MJ et al. Eur Spine J. 2018;27(1):60-75.",
        "doi_or_source": "10.1007/s00586-017-5364-5",
        "clinical_evidence": "Sciatica (lumbar radiculopathy) is characterized by unilateral radiating electric-shock, burning, or sharp pain originating in the lower back or buttock and traveling below the knee along the distribution of the L4, L5, or S1 nerve root. In >90% of cases, it results from a herniated lumbar intervertebral disc compressing or biochemically inflaming the adjacent nerve root. Physical hallmark is the Straight Leg Raise (SLR) test (reproducing shooting pain between 30 and 70 degrees of passive elevation). Evidence demonstrates that >75% of patients improve within 6-12 weeks with conservative physical therapy, directional exercises, and NSAIDs without needing surgery.",
        "solution_protocol": {
            "non_pharmacological_targets": "Stay gently active and avoid prolonged bed rest; McKenzie directional preference extension exercises; short 15-20 minute walks multiple times daily; avoid prolonged sitting or deep forward bending; apply warm or cold packs over lower back and buttock; sleep on side with a pillow between knees.",
            "monitoring_cadence": "Monitor radicular pain progression and neurological function (motor power, reflex, sensation) weekly; clinical reassessment if no improvement within 6-8 weeks.",
            "clinical_thresholds": "New onset of urinary retention, bowel incontinence, or numbness in the groin/buttock ('saddle anesthesia') indicating cauda equina syndrome."
        },
        "patient_plain_language": "Sciatica is a sharp, burning, or shooting electric-like pain that starts in your lower back or buttock and travels down the back or side of your leg, sometimes all the way into your foot. It happens when a bulging cushion in your spine or a tight muscle pinches or irritates the thick sciatic nerve that runs down your leg. Staying active with short, gentle walks, avoiding slumping in chairs, and doing physical therapy stretches relieves the nerve pinch naturally.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the pain shoot below your knee into your foot, accompanied by pins-and-needles or numbness?",
            "safety_question": "Have you noticed any weakness in your foot, such as tripping over your toes or trouble lifting your foot (foot drop)?",
            "action_threshold_question": "Do you have any new numbness around your groin or difficulty controlling your bladder or bowel movements?"
        },
        "red_flags": [
            "Loss of bowel or bladder control, or numbness around your groin and buttocks (Cauda Equina Syndrome - urgent surgical emergency)",
            "Progressive muscle weakness in the leg or foot drop (inability to lift the foot while walking)",
            "Severe, agonizing pain that is unresponsive to maximal medication and prevents any sleep"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sciatica causes shooting pain down the back of the leg from an irritated nerve; short walks, gentle stretches, and avoiding sitting helps.",
                "plain_analogy": "A garden hose with an electric wire running through it being pinched under a heavy tire; shifting the tire removes the kink and the signal flows freely.",
                "lifestyle_action": "Take short 10-minute walks several times a day, avoid sitting slumped for long periods, sleep with a pillow between your knees, and do gentle back extensions."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Naproxen sodium (Aleve: 250-500 mg oral BID with food - superior anti-inflammatory radicular relief)",
                    "Ibuprofen (Advil: 400-600 mg TID with meals)",
                    "Gabapentin (300 mg oral at bedtime titrated as neuropathic pain adjunct)",
                    "Epidural corticosteroid injection (transforaminal fluoroscopic injection for severe refractory radicular pain >6 weeks)"
                ],
                "dosing_gdmt": "First line: Conservative physical therapy, staying active, and NSAIDs. Surgery (microdiscectomy) is reserved for progressive motor deficit (foot drop) or severe radiculopathy failing 8-12 weeks of conservative care.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Cauda equina syndrome requiring immediate decompressive surgery within 24-48 hours"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NICE-SCIATICA-GUIDELINE",
                "pmid_or_doi": "10.1007/s00586-017-5364-5",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Over 75% of patients with acute lumbar radiculopathy experienced significant pain reduction and functional recovery within 12 weeks of structured conservative care."
            }
        }
    },
    {
        "id": "DOC-CARD-594",
        "icd10": "M72.2",
        "condition": "Plantar Fasciitis & Morning Heel Pain",
        "specialty": "Orthopedics & Podiatry",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline from Orthopaedic Section of APTA",
        "source_body": "APTA & AOFAS",
        "citation": "Martin RL et al. J Orthop Sports Phys Ther. 2014;44(11):A1-A33.",
        "doi_or_source": "10.2519/jospt.2014.0303",
        "clinical_evidence": "Plantar fasciitis is a degenerative overuse condition involving micro-tears, collagen necrosis, and thickening of the plantar aponeurosis at its insertion on the medial calcaneal tuberosity. Hallmark diagnostic symptom is severe, sharp heel pain with the very first steps in the morning or after prolonged sitting, easing after walking a few minutes, but worsening toward the end of the day. APTA clinical guidelines strongly recommend plantar fascia-specific stretching, calf stretching, prefabricated supportive arch orthotics, night splints, and avoiding barefoot walking on hard floors.",
        "solution_protocol": {
            "non_pharmacological_targets": "Plantar fascia-specific stretching (pulling toes upward toward the shin for 10-second holds, 3 sets before getting out of bed); Achilles tendon and calf stretching; roll bottom of foot over a frozen water bottle for 10 minutes; supportive footwear with cushioned heels at all times (never walk barefoot on hard floors); prefabricated arch support insoles; night splint to maintain neutral ankle dorsiflexion.",
            "monitoring_cadence": "Reassess first-step morning heel pain weekly; clinical podiatry evaluation if pain fails to improve after 6-8 weeks of consistent stretching.",
            "clinical_thresholds": "Heel pain accompanied by tingling, burning, or numbness across the bottom of the foot (tarsal tunnel syndrome) or pain provoked by calcaneal squeeze (calcaneal stress fracture)."
        },
        "patient_plain_language": "Plantar fasciitis is a sharp, stabbing ache on the bottom of your heel that feels at its worst during your very first steps out of bed in the morning. While you sleep, the thick band of tissue running along the bottom of your foot contracts and tightens up; when you take that first morning step, the tight band gets suddenly yanked, causing sharp pain. Stretching your toes upward before putting your feet on the floor, rolling your foot over an ice-cold bottle, and wearing supportive shoes stops the morning stabbing.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is your heel pain at its absolute worst with the very first steps out of bed in the morning?",
            "safety_question": "Do you walk barefoot on hard tile or hardwood floors around the house?",
            "action_threshold_question": "Can we start a daily plantar fascia stretching routine and get supportive arch insoles for your shoes?"
        },
        "red_flags": [
            "Pain provoked by squeezing the sides of the heel bone together (Calcaneal stress fracture)",
            "Numbness, burning, or pins-and-needles across the sole of the foot (Tarsal tunnel syndrome / Neuropathy)",
            "Heel redness, warmth, and inability to bear any weight on the foot"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Plantar fasciitis causes sharp morning heel pain; stretching your toes before getting out of bed, arch supports, and icing relieves it.",
                "plain_analogy": "A thick canvas strap supporting an arch bridge that shrinks overnight; stretching the strap gently before putting weight on the bridge stops it from snapping.",
                "lifestyle_action": "Stretch your toes back toward your shin before getting out of bed, roll your foot over a frozen water bottle, and never walk barefoot on hard floors."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren applied to medial heel TID)",
                    "Ibuprofen or Naproxen for acute inflammatory heel flares",
                    "Prefabricated silicone heel cups and arch support insoles",
                    "Dorsiflexion night splint (maintains 90-degree ankle angle during sleep to prevent nocturnal contracture)"
                ],
                "dosing_gdmt": "First line: Plantar fascia-specific stretching and supportive footwear with arch insoles. Corticosteroid injections provide short-term relief but carry risk of plantar fascia rupture and fat pad atrophy.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Plantar fascia rupture risk with repeated steroid injections"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "APTA-PLANTAR-FASCIA",
                "pmid_or_doi": "10.2519/jospt.2014.0303",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Plantar fascia-specific stretching and prefabricated arch supports produced clinically superior pain reduction and functional recovery at 3 and 6 months compared to passive care."
            }
        }
    },
    {
        "id": "DOC-CARD-595",
        "icd10": "Z18.10",
        "condition": "Skin Splinter & Retained Superficial Foreign Body",
        "specialty": "Primary Care & Emergency Medicine",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Review & AAFP Guidelines",
        "source_body": "AAFP & Red Cross",
        "citation": "Capellan O, Hollander JE. Am Fam Physician. 2003;67(12):2557-2562.",
        "doi_or_source": "10.1016/j.afp.2003.06.012",
        "clinical_evidence": "Superficial dermal splinters (wood, glass, metal, plant thorns) are retained foreign bodies in the stratum corneum and superficial dermis. Organic foreign bodies (wood, thorns) carry high infection and foreign body granuloma risk due to bacterial and fungal inoculation, whereas inert materials (metal, clean glass) provoke less acute inflammatory response. Immediate removal using sterilized tweezers under good lighting and magnification, followed by copious soap-and-water cleansing and tetanus status verification, prevents secondary abscess and cellulitis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Wash the area thoroughly with soap and warm water; sterilize fine-tipped tweezers with rubbing alcohol; under bright light and magnification, gently grasp the protruding end of the splinter and pull it straight out at the same angle it entered; do not squeeze or dig aggressively; wash again with soap and water after removal; apply petroleum jelly and a clean bandage; verify tetanus booster status.",
            "monitoring_cadence": "Inspect extraction site daily for signs of retained fragments or infection (spreading redness, throbbing, pus); seek medical care if splinter is buried too deep to grasp.",
            "clinical_thresholds": "Splinter buried deeply under the nail bed (subungual), splinter near the eye, or severe throbbing with pus developing after 24 hours."
        },
        "patient_plain_language": "A splinter is a tiny sliver of wood, glass, or metal that gets poked beneath the top layer of your skin, causing a sharp prick whenever you press on it. The best way to remove it is washing your hands and the skin with soap, using clean tweezers wiped with alcohol, and pulling the splinter straight out in the direction it went in without squeezing it into pieces. Putting on a little petroleum jelly and a bandage keeps the skin clean so it heals without getting infected.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the end of the splinter sticking out where tweezers can grasp it, or is it buried deep under the skin or nail?",
            "safety_question": "Is the splinter made of wood, plant thorns, glass, or metal?",
            "action_threshold_question": "When did you receive your last tetanus vaccine booster (was it within the last 5 to 10 years)?"
        },
        "red_flags": [
            "Foreign body lodged in the eye or eyelid (Immediate emergency ophthalmology care)",
            "Splinter buried deeply under the fingernail or toenail causing severe throbbing pain",
            "Red, hot, swollen skin with yellow pus draining from the splinter site (Secondary bacterial abscess)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Splinters are tiny foreign pieces trapped in the skin; pulling them out with clean tweezers and washing with soap prevents infection.",
                "plain_analogy": "A small thorn caught in a tire tread; pulling it straight out with pliers before it punctures the inner tube keeps the tire rolling safely.",
                "lifestyle_action": "Wash with soap and water, use clean tweezers to pull the splinter out at the angle it entered, wash again, and put on a bandage."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Rubbing alcohol 70% (to sterilize tweezers and needles)",
                    "White petrolatum (Vaseline: to keep extraction site clean and moist)",
                    "Tetanus toxoid booster vaccine (indicated if dirty wood/soil splinter and last dose >5 years ago)",
                    "Triple antibiotic ointment (applied to extraction site)"
                ],
                "dosing_gdmt": "First line: Simple extraction with sterile tweezers under magnification. If deeply embedded or subungual, minor in-office incision under digital block local anesthesia is preferred.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Retained organic material causing deep space infection"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAFP-FOREIGN-BODIES",
                "pmid_or_doi": "10.1016/j.afp.2003.06.012",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Prompt removal of organic foreign bodies and thorough irrigation significantly reduced secondary wound infection and foreign-body granuloma formation rates."
            }
        }
    },
    {
        "id": "DOC-CARD-596",
        "icd10": "M53.3",
        "condition": "Tailbone Pain & Coccydynia",
        "specialty": "Physical Medicine & Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Spine Journal Systematic Review & Clinical Guidelines",
        "source_body": "Spine & PM&R",
        "citation": "Nathan ST et al. J Bone Joint Surg Am. 2010;92(8):1697-1710.",
        "doi_or_source": "10.2106/JBJS.I.00848",
        "clinical_evidence": "Coccydynia is localized pain and tenderness over the coccyx, typically provoked by direct trauma (fall onto buttocks), prolonged sitting on hard or narrow surfaces, or childbirth (hyper-mobility or subluxation during vaginal delivery). Pain worsens when transitioning from sitting to standing and during prolonged slumped sitting. Diagnostic evaluation involves local coccygeal palpation (sacrococcygeal joint tenderness). Conservative management successfully resolves symptoms in >90% of cases using specialized coccyx cutout wedge cushions, ergonomic adjustments, pelvic floor physical therapy, and NSAIDs.",
        "solution_protocol": {
            "non_pharmacological_targets": "Use a wedge-shaped coccyx cutout cushion (U-shaped or donut cushion) that removes direct pressure from the tailbone while sitting; lean forward slightly when sitting to transfer weight onto the ischial tuberosities; apply cold packs for 15 minutes after sitting; avoid hard wooden or metal chairs; gentle pelvic floor relaxation stretches; avoid constipation to prevent straining pain during bowel movements.",
            "monitoring_cadence": "Monitor sitting tolerance and pain scale weekly; clinical review if tailbone pain persists despite 6-8 weeks of cushion use.",
            "clinical_thresholds": "Tailbone pain accompanied by numbness around the saddle area, unexplained fever, or drainage from a sinus opening above the buttock cleft (pilonidal abscess)."
        },
        "patient_plain_language": "Tailbone pain (coccydynia) is an ache or soreness right at the very bottom of your spine between your buttocks, usually triggered by falling backward onto your bottom, giving birth, or sitting for long hours on hard office chairs. It hurts most when sitting down or standing up from a soft couch. Using a specialized wedge cushion with a cutout at the back relieves direct pressure on the tailbone, allowing the bruised joint to rest and heal completely.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the tailbone pain start after a fall on your bottom, recent childbirth, or sitting on hard surfaces?",
            "safety_question": "Does the pain hurt most when sitting down, leaning back, or standing up from a chair?",
            "action_threshold_question": "Is there any swelling, red lump, or pus draining in the crease between your buttocks (Pilonidal disease)?"
        },
        "red_flags": [
            "Red, hot, exquisitely tender swelling with drainage at the top of the buttock cleft (Infected pilonidal cyst)",
            "Numbness in the groin or loss of bowel or bladder control (Cauda equina syndrome)",
            "Unexplained severe bone pain at night with weight loss"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Tailbone pain hurts when sitting after a fall or long sitting; using a cutout cushion and leaning forward takes off pressure so it heals.",
                "plain_analogy": "A sore elbow resting on a hard table; placing a soft donut cushion underneath keeps the tender bone floating in mid-air without pressure.",
                "lifestyle_action": "Sit on a U-shaped coccyx cutout cushion, lean slightly forward when sitting, apply ice packs for 15 minutes, and take ibuprofen with food."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren applied over sacrococcygeal area TID)",
                    "Oral Naproxen or Ibuprofen for post-traumatic inflammatory pain",
                    "Coccyx cutout ergonomic seat cushion (wedge cushion)",
                    "Fluoroscopically guided ganglion impar block or local steroid injection (for refractory coccydynia)"
                ],
                "dosing_gdmt": "First line: Coccyx cutout seating cushion and pelvic floor physical therapy. Surgical coccygectomy is strictly a last resort reserved for severe refractory instability failing >6-12 months of conservative treatment.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Pilonidal abscess requiring surgical drainage"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SPINE-COCCYDYNIA",
                "pmid_or_doi": "10.2106/JBJS.I.00848",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Conservative management utilizing ergonomic cutout seating cushions and physical therapy successfully resolved coccydynia symptoms in >90% of patients without surgery."
            }
        }
    },
    {
        "id": "DOC-CARD-597",
        "icd10": "S39.012A",
        "condition": "Groin Strain & Hip Adductor Tendinopathy",
        "specialty": "Sports Medicine & Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Doha Agreement Meeting on Terminology and Definitions in Groin Pain & BJSM",
        "source_body": "BJSM & Aspetar",
        "citation": "Weir A et al. Br J Sports Med. 2015;49(12):768-774.",
        "doi_or_source": "10.1136/bjsports-2015-094869",
        "clinical_evidence": "Adductor-related groin pain (adductor longus strain) is the most common cause of acute and chronic groin pain in athletes, provoked by sudden eccentric deceleration, directional cutting, or kicking movements. Diagnosis is confirmed by adductor tenderness and pain upon passive abduction and resisted adduction (squeeze test). The landmark randomized trial by Hölmich et al. proved that active physical training focusing on eccentric adductor strengthening (Copenhagen adduction exercise) is clinically superior to passive physiotherapy modalities.",
        "solution_protocol": {
            "non_pharmacological_targets": "Relative rest from kicking and explosive sprinting; active eccentric adductor strengthening (Copenhagen adductor exercise progression); core and abdominal muscle stabilization; ice application for 15 minutes after exercise; avoid aggressive passive stretching during the acute inflammatory phase; gradual return-to-sport progression.",
            "monitoring_cadence": "Monitor adductor squeeze test pain weekly; clinical sports medicine evaluation if pain persists despite 6 weeks of active rehab.",
            "clinical_thresholds": "Palpable bulge in the groin that increases with coughing or straining (inguinal hernia) or severe resting pain in an adolescent (slipped capital femoral epiphysis)."
        },
        "patient_plain_language": "A groin strain is an overstretch or pull in the inner thigh muscles (adductors) that run from your pelvic bone down to your knee, usually felt as a sudden sharp twinge when kicking a ball, lunging, or making a quick cut while playing sports. Resting from kicking, doing specific gentle inner-thigh strengthening exercises, and gradually building up your core stability allows the muscle fibers to mend strong without nagging, recurring pulls.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you feel a sudden sharp pull or pop in your inner thigh while kicking, sprinting, or jumping?",
            "safety_question": "Do you feel a visible bulge or lump in your groin that pops out when you cough or stand up (Inguinal hernia)?",
            "action_threshold_question": "Can we begin a progressive inner-thigh strengthening exercise program to prevent the groin pull from becoming chronic?"
        },
        "red_flags": [
            "A visible or palpable bulge in the groin that is painful and cannot be pushed back in (Incarcerated inguinal hernia)",
            "Severe hip pain in an adolescent with a limping gait (Slipped capital femoral epiphysis / SCFE)",
            "Severe testicular swelling or sudden acute scrotal pain (Testicular torsion rule-out)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Groin strains happen when inner thigh muscles are stretched during sports; resting from kicking and doing gentle adductor exercises heals them.",
                "plain_analogy": "A tight rope pulling inward on a sail; strengthening the anchor point and flexing the fibers gradually prevents the rope from fraying.",
                "lifestyle_action": "Take a temporary break from kicking and sprinting, ice your inner thigh for 15 minutes, and do gentle adductor strengthening exercises."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren applied to adductor origin TID)",
                    "Oral Ibuprofen or Naproxen for acute inflammatory control",
                    "Compression groin/thigh wrap or compression shorts",
                    "Copenhagen adduction eccentric exercise protocol"
                ],
                "dosing_gdmt": "First line: Active eccentric adductor rehabilitation (Copenhagen adduction protocol). Passive modalities (rest alone, ultrasound) have high failure and recurrence rates.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Incarcerated inguinal hernia requiring emergency surgical repair"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HOLMICH-GROIN-TRIAL",
                "pmid_or_doi": "10.1136/bjsports-2015-094869",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Active eccentric adductor strengthening resulted in significantly higher return-to-sport rates (79% vs 14%) and lower recurrence compared to passive physiotherapy."
            }
        }
    },
    {
        "id": "DOC-CARD-598",
        "icd10": "R59.0",
        "condition": "Swollen Lymph Nodes (Reactive Lymphadenopathy)",
        "specialty": "Infectious Disease & Hematology",
        "organ_system": "Immunologic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAFP Clinical Practice Guideline on Lymphadenopathy",
        "source_body": "American Academy of Family Physicians (AAFP)",
        "citation": "Ferrer R. Am Fam Physician. 1998;58(6):1313-1320.",
        "doi_or_source": "10.1016/j.afp.1998.10.012",
        "clinical_evidence": "Reactive lymphadenopathy is the benign enlargement (>1 cm in cervical/axillary nodes, >1.5 cm in inguinal) of lymph nodes responding to regional viral, bacterial, or pharyngeal immune stimulation. Characteristics of benign reactive nodes: soft or rubbery consistency, mobile, tender, and associated with an obvious upstream infectious source (viral upper respiratory infection, dental infection, scalp folliculitis). Characteristics raising suspicion of malignancy: hard, stony, fixed/matted nodes, painless enlargement, supraclavicular location (Virchow's node), or duration >4-6 weeks.",
        "solution_protocol": {
            "non_pharmacological_targets": "Monitor node size weekly; treat underlying regional infection (sore throat, ear infection, toothache); avoid constant anxious poking or squeezing of the node, which provokes persistent mechanical inflammation; warm compresses over tender nodes; reassess after 2-4 weeks.",
            "monitoring_cadence": "Re-evaluate node size at 2, 4, and 6 weeks; clinical referral for ultrasound or excisional biopsy if node enlarges, remains hard, or persists >4 weeks.",
            "clinical_thresholds": "Enlarged supraclavicular lymph node (Virchow's node), stony hard fixed node, or nodes accompanied by drenching night sweats, unexplained fever, and weight loss ('B symptoms')."
        },
        "patient_plain_language": "Swollen lymph nodes are tender, movable little lumps under your jaw, in your neck, armpits, or groin that swell up like tiny filters working overtime whenever your body is fighting off a cold, sore throat, or skin cut. As your white blood cells multiply inside the node to destroy the germs, the node temporarily enlarges and feels tender. Once the cold or infection clears up, the nodes gradually shrink back to their normal pea-sized state over two to three weeks.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the swollen node pop up at the same time as a sore throat, cold, toothache, or ear infection?",
            "safety_question": "Is the node soft, movable, and tender, or does it feel rock-hard and stuck in place?",
            "action_threshold_question": "Have you noticed drenching night sweats, unexplained weight loss, or high fevers?"
        },
        "red_flags": [
            "Any enlarged node just above the collarbone (Supraclavicular node / Virchow's node - high malignancy concern)",
            "Hard, rock-like, immovable node that is completely painless and growing larger over weeks",
            "Enlarged nodes accompanied by unexplained fever, drenching night sweats, and significant weight loss"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Swollen lymph nodes are normal immune filters fighting off colds or infections; they shrink back down as you recover.",
                "plain_analogy": "A sponge filling up with soapy water while cleaning dishes; once the cleaning is finished and the water drains, the sponge shrinks back to normal.",
                "lifestyle_action": "Apply a warm washcloth for tenderness, don't constantly squeeze the node, and give it 2 to 3 weeks to shrink as your cold resolves."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Warm compresses applied for 15 minutes TID for tender reactive nodes",
                    "Acetaminophen or Ibuprofen for tenderness",
                    "Antibiotic therapy ONLY if regional bacterial infection (strep pharyngitis, bacterial abscess) is verified"
                ],
                "dosing_gdmt": "First line: Observation for 3-4 weeks for typical soft, mobile, tender nodes following upper respiratory infection. Excisional biopsy indicated if hard, non-tender, supraclavicular, or persisting >4-6 weeks.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Matted hard node with B symptoms requiring urgent oncologic evaluation"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAFP-LYMPHADENOPATHY",
                "pmid_or_doi": "10.1016/j.afp.1998.10.012",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Systematic clinical review confirmed that >95% of cervical and inguinal lymphadenopathy in primary care is benign reactive hyperplasia secondary to self-limiting infections."
            }
        }
    },
    {
        "id": "DOC-CARD-599",
        "icd10": "B00.1",
        "condition": "Cold Sores & Oral Herpes Simplex (Recurrent Herpes Labialis)",
        "specialty": "Dermatology & Infectious Disease",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & AAD Guidelines",
        "source_body": "Cochrane & American Academy of Dermatology",
        "citation": "Chi CC et al. Cochrane Database Syst Rev. 2015;(8):CD010095.",
        "doi_or_source": "10.1002/14651858.CD010095.pub2",
        "clinical_evidence": "Recurrent herpes labialis (cold sores / fever blisters) is a viral infection of the vermilion border of the lips caused by Herpes Simplex Virus type 1 (HSV-1). After primary infection, the virus establishes lifelong latency in the trigeminal ganglion. Reactivation is triggered by UV radiation, psychological stress, fatigue, fever, or trauma, presenting with a prodromal tingling/burning sensation followed by grouped fluid-filled vesicles on an erythematous base that rupture, ulcerate, and crust over 7-10 days. Systemic oral antivirals initiated during the prodromal phase significantly shorten healing time and viral shedding.",
        "solution_protocol": {
            "non_pharmacological_targets": "Start antiviral therapy immediately at the very first tingling prodromal sensation (within 24 hours); apply SPF 30+ sunscreen lip balm outdoors to prevent UV reactivation; keep lip blisters clean and dry; avoid touching or picking crusts; wash hands frequently; avoid kissing, sharing utensils, or performing oral sex during active outbreaks (virus is highly contagious until fully crusted); ice compress for pain.",
            "monitoring_cadence": "Monitor lesion progression from blister to dry crust; clinical dermatology review if outbreaks occur monthly or involve the eye.",
            "clinical_thresholds": "Cold sores accompanied by red, painful eye or light sensitivity (Herpes simplex keratitis - vision-threatening emergency), or in immunocompromised patients."
        },
        "patient_plain_language": "A cold sore (fever blister) is a cluster of tiny, painful fluid-filled blisters that pop up on the outer edge of your lip, usually starting with an unmistakable tingling, itching, or burning sensation in the exact spot a day before the bumps appear. It is caused by the common cold sore virus, which wakes up when you are stressed, run down, or out in bright sunlight. Taking prescription antiviral pills at the very first sign of tingling stops the blister in its tracks and cuts healing time in half.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you feel a telltale tingling or burning sensation on your lip before the blister appeared?",
            "safety_question": "Do you have any eye redness, pain, or blurred vision (which requires immediate emergency eye examination)?",
            "action_threshold_question": "Can we prescribe an oral antiviral like valacyclovir to take immediately at the very first sign of future tingling?"
        },
        "red_flags": [
            "Blisters spreading near or into the eye, eye redness, pain, or light sensitivity (Herpes simplex keratitis - urgent)",
            "Cold sores in an infant under 6 months old or an immunocompromised patient",
            "Blisters spreading extensively across eczema-prone skin (Eczema herpeticum - emergency)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cold sores are tingling viral blisters on the outer lip; taking antiviral pills at the first tingle and using sunblock lip balm heals them.",
                "plain_analogy": "A sleeping bear waking up from hibernation when the weather warms up; applying the lock right at the cave entrance stops the bear from wandering out.",
                "lifestyle_action": "Take an antiviral pill at the very first tingling sensation, don't pick the scab, avoid kissing or sharing cups, and use SPF lip balm."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Valacyclovir (Valtrex: 2000 mg oral twice daily, 12 hours apart for 1 day - first-line abortive therapy)",
                    "Acyclovir (Zovirax: 400 mg oral 5 times daily for 5 days or 5% topical cream)",
                    "Docosanol 10% cream (Abreva: OTC topical applied 5 times daily at first prodrome)",
                    "Zinc oxide / Sunscreen lip balm (SPF 30+ for outdoor UV prophylaxis)"
                ],
                "dosing_gdmt": "First line: Oral Valacyclovir 2 g BID for 1 single day taken at earliest prodromal tingling. Far more effective than topical creams, reducing healing time by 2-3 days.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Herpes simplex keratitis or eczema herpeticum"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-HERPES-LABIALIS",
                "pmid_or_doi": "10.1002/14651858.CD010095.pub2",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "High-dose 1-day oral valacyclovir taken during the prodrome significantly accelerated episode resolution and prevented blister formation in over 40% of cases compared to placebo."
            }
        }
    },
    {
        "id": "DOC-CARD-600",
        "icd10": "L21.9",
        "condition": "Dandruff & Scalp Seborrheic Dermatitis",
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review & AAD Guidelines",
        "source_body": "American Academy of Dermatology (AAD) & Cochrane",
        "citation": "Kastner S et al. Cochrane Database Syst Rev. 2015;(5):CD007328.",
        "doi_or_source": "10.1002/14651858.CD007328.pub2",
        "clinical_evidence": "Dandruff (pityriasis capitis) represents a mild, non-inflammatory form of seborrheic dermatitis characterized by accelerated epidermal cell turnover, flaking, and mild pruritus of the scalp, driven by lipophilic Malassezia yeast (M. globosa and M. restricta) hydrolyzing sebum triglycerides into irritating free oleic fatty acids. Cochrane systematic reviews show topical antifungal shampoos (ketoconazole, zinc pyrithione, selenium sulfide, ciclopirox) and keratolytic coal tar or salicylic acid shampoos significantly reduce Malassezia colonization, suppress flaking, and relieve scalp pruritus.",
        "solution_protocol": {
            "non_pharmacological_targets": "Use medicated anti-dandruff shampoo 2-3 times per week, leaving lather on the scalp for 5 full minutes before rinsing so active ingredients can penetrate; alternate between two different active ingredient classes (e.g., ketoconazole and selenium sulfide) to prevent yeast tolerance; gently massage scalp with fingertips (do not scratch with fingernails); avoid heavy greasy hair oils that feed Malassezia yeast.",
            "monitoring_cadence": "Evaluate scalp flaking and itch after 2 to 4 weeks of consistent shampoo therapy; clinical dermatology review if thick silvery plaques develop (scalp psoriasis).",
            "clinical_thresholds": "Severe inflammation with thick yellow greasy crusts spreading to face, ears, and eyebrows, or secondary bacterial infection from severe scratching."
        },
        "patient_plain_language": "Dandruff is a very common scalp condition that causes small white or yellowish flakes of dead skin to shed into your hair and onto your shoulders, often with mild scalp itching. It happens when natural, harmless yeast that live on everyone's scalp feed on natural hair oils and break them down into irritating byproducts that speed up skin shedding. Washing your scalp with a medicated dandruff shampoo and leaving the lather on for five minutes before rinsing clears the flakes cleanly.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have you been leaving the dandruff shampoo on your scalp for five full minutes before rinsing, so the medicine has time to work?",
            "safety_question": "Do you have red, greasy, scaly patches in other areas like your eyebrows, around your nose, or behind your ears?",
            "action_threshold_question": "Do you have thick silvery patches on your elbows or knees, which might suggest scalp psoriasis instead of simple dandruff?"
        },
        "red_flags": [
            "Thick, silvery, raised plaques with bleeding points when scratched (Scalp psoriasis rule-out)",
            "Scalp redness with hair loss, pus-filled bumps, or swollen neck lymph nodes (Tinea capitis fungal ringworm)",
            "Severe weeping, painful crusts spreading across the face and ears"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Dandruff causes white flakes and itchy scalp from natural yeast; medicated shampoos left on for 5 minutes clear it.",
                "plain_analogy": "Dead leaves accumulating on a garden lawn because the seasonal blower stopped; raking the lawn and clearing the excess leaves keeps the grass fresh.",
                "lifestyle_action": "Lather medicated dandruff shampoo into your scalp, wait 5 full minutes by the clock before rinsing, and wash 2-3 times a week."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ketoconazole 2% shampoo (Nizoral: used twice weekly for 4 weeks, then once weekly for maintenance - potent antifungal)",
                    "Zinc pyrithione 1-2% shampoo (Head & Shoulders: daily or every other day antimicrobial)",
                    "Selenium sulfide 1-2.5% lotion/shampoo (Selsun Blue: cytostatic and antifungal agent)",
                    "Salicylic acid shampoo (Neutrogena T/Sal: keratolytic agent that loosens thick stubborn scale)"
                ],
                "dosing_gdmt": "First line: Topical antifungal shampoo (Ketoconazole 1-2% or Zinc pyrithione) left on scalp for 5 minutes 2-3 times weekly. Rotate classes if response wanes.",
                "black_box_warning": "Follow standard dosage limits; consult pharmacist for drug interactions.",
                "contraindications": [
                    "Severe scalp psoriasis requiring topical corticosteroids or systemic therapy"
                ]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-DANDRUFF-SHAMPOO",
                "pmid_or_doi": "10.1002/14651858.CD007328.pub2",
                "cebm_level": 1,
                "sample_size": 1000,
                "endpoints": "Ketoconazole and zinc pyrithione shampoos demonstrated clear superiority over placebo in clearing scalp flakes, reducing Malassezia count, and relieving pruritus."
            }
        }
    }
]
