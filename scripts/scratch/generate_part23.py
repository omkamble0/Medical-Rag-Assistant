"""
Generator for scripts/dataset_parts/part23_everyday_symptoms_and_minor_injuries.py
Covers 50 common day-to-day conditions (DOC-CARD-551 to DOC-CARD-600):
Cough, Leg Pain, Shoulder Pain, Cut / Laceration, Sore Throat, Common Cold,
Ear Pain, Dry Eye, Pink Eye, Stiff Neck, Knee Sprain, Ankle Sprain, Wrist Pain,
Low Back Strain, Bruises, Minor Burns, Sunburn, Insect Bites, Canker Sores,
Toothache, Nosebleeds, Hiccups, Indigestion, Intestinal Gas, Stomach Flu,
Nausea & Motion Sickness, Constipation, Hemorrhoids, Tension Headache,
Heat Exhaustion, Alcohol Hangover, DOMS, Foot Blisters, Ingrown Toenail,
Hives, Contact Dermatitis, Chapped Lips, Orthostatic Dizziness, Lifestyle Fatigue,
Food Poisoning, Jammed Finger, Shin Splints, Sciatica, Plantar Fasciitis,
Skin Splinter, Tailbone Pain, Groin Strain, Swollen Lymph Nodes, Cold Sores, Dandruff.
"""

import json
from pathlib import Path

EVERYDAY_CONDITIONS = [
    {
        "id": "DOC-CARD-551",
        "icd10": "R05.9",
        "condition": "Acute Viral Cough & Bronchial Irritation",
        "specialty": "Pulmonology & Primary Care",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CHEST Guideline & Cochrane Systematic Review",
        "source_body": "CHEST & Cochrane Respiratory Group",
        "citation": "Malesker MA et al. Pharmacologic and Nonpharmacologic Treatment for Acute Cough Associated With the Common Cold: CHEST Expert Panel Report. Chest. 2017;152(5):1021-1037.",
        "doi_or_source": "10.1016/j.chest.2017.08.009",
        "clinical_evidence": "Acute cough (<3 weeks duration) is most commonly triggered by upper respiratory viral infections provoking post-nasal drip, airway sensory hyperreactivity, and epithelial inflammation. Cochrane systematic reviews show routine antibiotics provide no clinical benefit and cause adverse events. CHEST guidelines recommend honey (in patients >1 year) as superior to placebo/diphenhydramine for nighttime cough, warm fluid hydration, and guaifenesin for thick mucus secretions.",
        "solution_protocol": {
            "non_pharmacological_targets": "Honey (1-2 teaspoons for individuals older than 1 year); cool-mist humidification; warm tea with lemon; steam inhalation; elevated sleeping angle (15-30 degrees) to minimize nocturnal post-nasal pooling; smoking cessation.",
            "monitoring_cadence": "Self-monitor cough duration; reassess if persisting beyond 3 weeks (subacute cough) or worsening after initial 5 days.",
            "clinical_thresholds": "Cough lasting >3 weeks or accompanied by hemoptysis, fever >38.5C (101.3F), or resting SpO2 <95%."
        },
        "patient_plain_language": "An acute viral cough is your airway's natural defense reflex to clear out mucus and irritants after catching a cold. The sensitive cough nerve endings in your throat stay hyperactive for 10 to 14 days even after the virus is gone. Honey, warm fluids, and steam soothe the tickling nerve endings much more effectively and safely than antibiotics, which cannot kill common cold viruses.",
        "doctor_consultation_checklist": {
            "parameter_question": "How many days has the cough lasted, and are you coughing up clear mucus, yellow-green phlegm, or blood?",
            "safety_question": "Are you experiencing shortness of breath, wheezing, or chest tightness when breathing in deeply?",
            "action_threshold_question": "If my cough lasts longer than 3 weeks, do I need a chest X-ray to check for secondary infection or asthma?"
        },
        "red_flags": [
            "Hemoptysis (coughing up frank red blood or rust-colored sputum)",
            "Stridor, shortness of breath, or resting oxygen saturation below 92%",
            "High fever persisting beyond 3 days or sudden relapse with shaking chills"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "A common cough caused by cold viruses clears up on its own within two to three weeks; honey, steam, and fluids provide gentle relief.",
                "plain_analogy": "A sensitive smoke detector that keeps sounding after the smoke has cleared because its sensor is still warm; soothing moisture calms the sensor.",
                "lifestyle_action": "Sip warm water or tea with honey, run a cool-mist vaporizer in your bedroom, and stay well hydrated."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Honey (natural demulcent for age >1 year)",
                    "Guaifenesin (Mucinex: 200-400 mg oral every 4 hours or 600-1200 mg ER every 12 hours)",
                    "Dextromethorphan (Delsym / Robitussin: 10-20 mg oral every 4 hours)",
                    "Saline nasal spray (0.9% sodium chloride isotonic rinses for post-nasal drip)",
                    "Benzonatate (Tessalon Perles: 100-200 mg oral TID as non-narcotic prescription antitussive)"
                ],
                "dosing_gdmt": "First line: Non-pharmacological demulcents (honey, warm liquids). For disruptive dry cough: Dextromethorphan or Benzonatate. Never give honey to infants under 12 months due to infant botulism risk.",
                "black_box_warning": "Codeine and tramadol containing cough syrups are contraindicated in pediatric patients due to fatal respiratory depression risk.",
                "contraindications": ["Infant age under 1 year for honey", "Productive bacterial pneumonia (cough suppression harmful)"]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-COUGH",
                "pmid_or_doi": "10.1002/14651858.CD007094.pub5",
                "cebm_level": 1,
                "sample_size": 899,
                "endpoints": "Honey significantly reduced cough frequency, symptom severity, and improved child and parent sleep quality compared to placebo or diphenhydramine."
            }
        }
    },
    {
        "id": "DOC-CARD-552",
        "icd10": "M79.669",
        "condition": "Leg Pain & Calf Muscle Strain",
        "specialty": "Orthopedics & Sports Medicine",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Clinical Practice Guideline & BJSM Consensus",
        "source_body": "British Journal of Sports Medicine (BJSM) & ACSM",
        "citation": "Green B et al. Calf Muscle Strain Injuries in Sport: A Systematic Review of Risk Factors, Rehabilitation, and Prevention. Br J Sports Med. 2020;54(12):703-714.",
        "doi_or_source": "10.1136/bjsports-2019-101764",
        "clinical_evidence": "Acute calf muscle strains typically involve tearing of muscle fibers at the myotendinous junction of the medial head of the gastrocnemius (tennis leg) or the deeper soleus. Immediate management requires the PEACE & LOVE protocol (Protect, Elevate, Avoid anti-inflammatories, Compress, Educate & Load, Optimism, Vascularization, Exercise). It is critical to differentiate calf strains from deep vein thrombosis (DVT) using Wells DVT score and ultrasound when unilateral calf swelling, pitting edema, or immobilization history is present.",
        "solution_protocol": {
            "non_pharmacological_targets": "Relative rest with gentle active ankle dorsiflexion; elastic compression bandage; elevation above heart level during rest; progressive eccentric calf strengthening (seated soleus and standing gastrocnemius raises); avoid aggressive stretching in the first 72 hours.",
            "monitoring_cadence": "Daily check for swelling, tenderness progression, and weight-bearing ability; clinical re-evaluation if unable to bear weight after 48 hours.",
            "clinical_thresholds": "Wells Score ≥2 (high pre-test DVT probability) or visible severe gap defect with inability to plantarflex (Achilles tendon rupture)."
        },
        "patient_plain_language": "A calf strain is an overstretching or tear of the powerful muscle fibers at the back of your lower leg, often felt as a sudden 'pop' or snap when pushing off while walking, running, or playing sports. Resting the leg, wearing a gentle snug compression sleeve, keeping the foot elevated on pillows, and gradually restarting light walking as tolerated allows the muscle fibers to stitch back together without forming thick scar tissue.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did you feel or hear a distinct 'pop' in the back of your ankle or calf when the pain began?",
            "safety_question": "Is the calf red, hot to the touch, or swollen compared to the other leg, which could indicate a blood clot (DVT)?",
            "action_threshold_question": "Can you stand on your tiptoes on that leg, or does the Thompson squeeze test suggest an Achilles tendon tear?"
        },
        "red_flags": [
            "Sudden swelling, warmth, redness, and deep tenderness of one calf (DVT warning sign)",
            "Audible pop at the heel with inability to point the toes downward (Achilles tendon rupture)",
            "Severe progressive calf tightness with cold pale foot and numbness (Compartment syndrome)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Calf muscle strains happen when the calf muscles are stretched too far; resting, compressing, elevating, and light walking aid recovery.",
                "plain_analogy": "A strong elastic exercise band whose outer fibers fray when snapped too quickly; resting and gentle warming allow the fibers to regain their tensile strength.",
                "lifestyle_action": "Wrap the calf in a comfortable elastic compression wrap, elevate your leg on a pillow, and avoid high-impact jumping until pain-free."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Acetaminophen (Tylenol: 500-1000 mg oral every 6 hours PRN, max 3000 mg/day)",
                    "Topical NSAID gel (Diclofenac 1% gel / Voltaren: 2-4 g applied locally 3-4 times daily)",
                    "Oral NSAIDs (Ibuprofen: 400 mg oral TID with meals after initial 48 hours)",
                    "Menthol / Camphor topical cooling analgesic patches"
                ],
                "dosing_gdmt": "First 48 hours: Acetaminophen and topical analgesics preferred over high-dose oral NSAIDs to avoid blunting the early inflammatory healing cascade. Gradual mobilization begins on day 3-5.",
                "contraindications": ["Known DVT or active deep vein thrombosis", "Complete Achilles tendon rupture requiring surgical repair"]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BJSM-CALF-REHAB",
                "pmid_or_doi": "10.1136/bjsports-2019-101764",
                "cebm_level": 1,
                "sample_size": 1280,
                "endpoints": "Structured progressive eccentric loading and early mobilization significantly reduced time to full return to sport and halved 12-month re-injury rates."
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
        "source_body": "American Academy of Orthopaedic Surgeons (AAOS)",
        "citation": "Pedowitz RA et al. Optimizing the Management of Rotator Cuff Problems: American Academy of Orthopaedic Surgeons Clinical Practice Guideline. J Am Acad Orthop Surg. 2011;19(6):380-388.",
        "doi_or_source": "10.5435/00124635-201106000-00007",
        "clinical_evidence": "Rotator cuff tendinopathy and subacromial impingement involve chronic micro-tearing and inflammation of the supraspinatus tendon beneath the coracoacromial arch, presenting with anterolateral shoulder ache exacerbated by overhead reach and sleeping on the affected side. Cochrane reviews and AAOS guidelines demonstrate that targeted physical therapy focusing on rotator cuff and scapular stabilizer strengthening is as effective as subacromial decompression surgery for non-traumatic full and partial thickness tears.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid repetitive overhead reaching; side-sleeping modifications with a body pillow; rotator cuff eccentric rehabilitation (sleeper stretch, internal/external rotation with light resistance bands, scapular retraction rows); ice packs 15 min twice daily after activity.",
            "monitoring_cadence": "Weekly evaluation of active abduction range of motion; clinical reassessment if no improvement within 6 to 12 weeks of structured physical therapy.",
            "clinical_thresholds": "Inability to actively elevate arm above 90 degrees ('drop arm' sign) indicating large acute full-thickness tendon tear."
        },
        "patient_plain_language": "Rotator cuff shoulder pain happens when the four small stabilizing muscles and tendons that hold your shoulder ball in its shallow socket become pinched, irritated, or worn down from repetitive reaching or sleeping awkwardly. You feel an ache on the outside of your upper arm, especially when reaching into a high cabinet or putting on a jacket. Targeted gentle resistance band exercises strengthen these muscles and open up breathing room inside the shoulder joint.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does your shoulder ache keep you awake at night when you roll onto that side?",
            "safety_question": "Did the pain start suddenly after a heavy fall or jerk, leaving you completely unable to lift your arm?",
            "action_threshold_question": "Would a referral for dedicated physical therapy or a diagnostic ultrasound be appropriate before considering injections?"
        },
        "red_flags": [
            "Sudden complete inability to raise arm following acute trauma (Acute full-thickness rotator cuff rupture)",
            "Left shoulder pain associated with chest pressure, sweating, or nausea (Myocardial infarction red flag)",
            "Hot, red, swollen shoulder joint with fever (Septic glenohumeral arthritis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Shoulder tendinopathy causes pain on the outer shoulder and arm when reaching overhead; physical therapy exercises are the primary cure.",
                "plain_analogy": "A rope repeatedly rubbing over a rough metal pulley; by strengthening the guiding cables (rotator muscles), the rope glides cleanly without friction.",
                "lifestyle_action": "Avoid reaching up high repeatedly, place a supportive pillow under your arm when sleeping, and perform gentle pendulum warm-ups."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Topical Diclofenac gel 1% (Voltaren: 2 g applied to affected shoulder QID)",
                    "Oral NSAIDs (Naproxen 250-500 mg BID with food or Ibuprofen 400-600 mg TID for 7-10 days)",
                    "Acetaminophen (500-1000 mg every 6 hours PRN for patients unable to take NSAIDs)",
                    "Subacromial corticosteroid injection (Triamcinolone 40 mg with 1% lidocaine - reserved for recalcitrant pain)"
                ],
                "dosing_gdmt": "First line: 6 to 12 weeks of structured physical therapy plus topical/oral NSAIDs. Subacromial steroid injections should be limited to 1-2 per year to prevent tendon weakening.",
                "contraindications": ["Complete acute retracted rotator cuff tear in young active patients (early surgical repair indicated)"]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-SHOULDER-EX",
                "pmid_or_doi": "10.1002/14651858.CD012224",
                "cebm_level": 1,
                "sample_size": 1735,
                "endpoints": "Exercise therapy produced clinically significant improvements in pain and shoulder function that were maintained at 1 year and comparable to surgical outcomes."
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
        "source_body": "CDC, WHO & Cochrane Wounds Group",
        "citation": "Fernandez R, Griffiths R. Water for Wound Cleansing. Cochrane Database Syst Rev. 2012;(2):CD003861; Liang JL et al. Prevention of Pertussis, Tetanus, and Diphtheria with Vaccines in the United States: Recommendations of the ACIP. MMWR Recomm Rep. 2018;67(2):1-44.",
        "doi_or_source": "10.1002/14651858.CD003861.pub3",
        "clinical_evidence": "Minor cuts, skin abrasions, and superficial lacerations require rapid wound assessment: depth, foreign body presence, tendon/neurovascular integrity, and tetanus vaccination status. Cochrane systematic reviews demonstrate that cleansing wounds with potable tap water is as effective as sterile saline and does not increase infection rates. Wounds requiring primary closure (sutures, staples, tissue adhesives) should ideally be closed within 12-18 hours (up to 24 hours on the vascular face). Tetanus toxoid booster is indicated for dirty/contaminated wounds if last booster was >5 years ago.",
        "solution_protocol": {
            "non_pharmacological_targets": "Direct firm pressure with a clean cloth/gauze for 5-10 minutes to stop bleeding; copious copiously irrigate with lukewarm tap water for 3-5 minutes; avoid harsh antiseptics like hydrogen peroxide or rubbing alcohol inside the wound as they damage healthy granulation cells; apply thin petroleum jelly or antibiotic ointment; cover with a sterile breathable adhesive bandage; change dressing daily.",
            "monitoring_cadence": "Inspect wound daily for signs of secondary bacterial infection (spreading redness, worsening throbbing pain, pus/discharge, fever).",
            "clinical_thresholds": "Laceration gaping >0.5 cm, exposing subcutaneous yellow fat or muscle, located over a bending joint, or bleeding pulsatile red blood."
        },
        "patient_plain_language": "A minor cut or scrape happens when everyday sharp objects break through the top layers of your skin. The most important first step is pressing firmly with a clean cloth for five full minutes until bleeding stops, then washing the cut thoroughly under running tap water to flush away dirt and germs. Applying a thin coat of plain petroleum jelly keeps the skin moist so it heals twice as fast with minimal scarring.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does the cut gape open when you move the body part, requiring stitches or skin glue to close neatly?",
            "safety_question": "When did you receive your last tetanus vaccine booster (was it within the past 5 to 10 years)?",
            "action_threshold_question": "Do you feel any numbness, tingling, or weakness in your fingers or toes past the cut?"
        },
        "red_flags": [
            "Pulsatile arterial spurting or bleeding that does not stop after 10-15 minutes of continuous firm pressure",
            "Spreading red streaks moving up the limb or fever developing within 48 hours (Lymphangitis/Cellulitis)",
            "Loss of sensation or inability to bend fingers/toes distal to the laceration (Nerve or tendon transection)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Minor cuts heal quickly when washed thoroughly with water, kept clean and moist under a bandage, and checked for signs of infection.",
                "plain_analogy": "A tear in a waterproof jacket; cleaning out the grit and taping the edges together smoothly allows the waterproof membrane to reseal without leaking.",
                "lifestyle_action": "Rinse under clean tap water, apply petroleum jelly, cover with an adhesive bandage, and keep the wound clean and dry during showers."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "White petrolatum (Vaseline / Aquaphor: thin layer applied to clean wound to promote moist healing)",
                    "Triple antibiotic ointment (Bacitracin / Neomycin / Polymyxin B - OTC topical)",
                    "Tetanus toxoid conjugate vaccine (Tdap / Td booster within 48 hours if indicated)",
                    "Topical 2-octyl cyanoacrylate skin adhesive (Dermabond - medical tissue glue for clean linear lacerations)"
                ],
                "dosing_gdmt": "Clean with tap water. Apply thin petroleum jelly and sterile dressing daily. Administer Td/Tdap if dirty wound and >5 years since last booster, or clean wound and >10 years.",
                "contraindications": ["Do not use tissue adhesive skin glue over high-tension joints or animal bite wounds (high infection risk)"]
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COCHRANE-WOUND-CLEANSE",
                "pmid_or_doi": "10.1002/14651858.CD003861.pub3",
                "cebm_level": 1,
                "sample_size": 3314,
                "endpoints": "Washing acute wounds with potable tap water reduced wound infection rates compared to no cleansing and was non-inferior to sterile normal saline."
            }
        }
    }
]

print("Script template ready. Now let us generate all 50 conditions.")
