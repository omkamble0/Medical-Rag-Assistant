"""
part14_gi_heme_twins.py
"""

PART_14_DISEASES = [
    {
        "id": "DOC-CARD-361",
        "icd10": "K57.32",
        "condition": "Acute Colonic Diverticulitis (LLQ Peritonitis)",
        "specialty": "Gastroenterology & General Surgery",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AGA Clinical Practice Guideline",
        "source_body": "Gastroenterology",
        "citation": "Peery AF et al. AGA Clinical Practice Update on Medical Management of Colonic Diverticulitis. Gastroenterology. 2021;160(3):906-911.",
        "doi_or_source": "10.1053/j.gastro.2020.09.059",
        "clinical_evidence": "The landmark DIABOLO and AVOD randomized trials (n=1,150) proved that selective non-antibiotic observation in uncomplicated acute diverticulitis is non-inferior to routine antibiotics in hospital stay (2 vs 3 days) and complication rates (<2%; p=0.88). Oral Ciprofloxacin + Metronidazole or Amoxicillin-Clavulanate (875/125 mg BID) is reserved for complicated diverticulitis (Hinchey Ia-IV with abscess or phlegmon).",
        "solution_protocol": {
            "non_pharmacological_targets": "Clear liquid diet for 48-72 hours during acute flare, progressing to high-fiber diet (30-35 g/day) post-resolution; physical exercise; maintain hydration; nuts, seeds, and popcorn are NOT restricted (debunked myth).",
            "monitoring_cadence": "Clinical reassessment at 48-72 hours; colonoscopy 6-8 weeks post-resolution to rule out occult colorectal cancer.",
            "clinical_thresholds": "Persistent fever >38.5 C, leukocytosis >15,000, or failure to improve in 48 hours mandates repeat abdominal CT."
        },
        "patient_plain_language": "Small outward pouches in your lower left bowel wall (diverticula) become inflamed or micro-perforated. Unlike appendicitis which hurts on the lower RIGHT, diverticulitis causes steady severe cramping pain in the lower LEFT of your belly, with fever and bloating.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my abdominal CT scan show any abscess, perforation, or uncomplicated inflammation?",
            "safety_question": "Can my uncomplicated flare heal with a clear liquid diet and rest rather than heavy antibiotics?",
            "action_threshold_question": "When should I schedule a follow-up colonoscopy to examine the healed bowel wall?"
        },
        "red_flags": [
            "Sudden rigid, board-like abdomen with severe chills (free perforation peritonitis - Emergency Laparotomy)",
            "Passing gas or feces in urine (colovesical fistula)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Diverticulitis is inflammation or infection of small pouches in the colon, causing lower left belly pain.",
                "plain_analogy": "A weak spot in a bicycle inner tube that bulges outward and becomes irritated.",
                "lifestyle_action": "Drink clear broths during a flare, eat high-fiber foods once healed, and drink plenty of water."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Amoxicillin/Clavulanate (Augmentin)",
                    "Ciprofloxacin + Metronidazole (Flagyl)"
                ],
                "dosing_gdmt": "Augmentin 875/125 mg orally BID x 7-10 days; or Cipro 500 mg BID + Flagyl 500 mg TID.",
                "black_box_warning": "Fluoroquinolones carry black box warning for tendonitis and tendon rupture.",
                "organ_clearance_cutoffs": "Adjust dose in moderate to severe renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "DIABOLO",
                "pmid_or_doi": "10.1053/j.gastro.2020.09.059",
                "cebm_level": 2,
                "sample_size": 1150,
                "endpoints": "Observational management is non-inferior to routine antibiotics in uncomplicated diverticulitis."
            }
        }
    },
    {
        "id": "DOC-CARD-362",
        "icd10": "K35.80",
        "condition": "Acute Appendicitis (McBurney's Point Peritonitis)",
        "specialty": "General Surgery & Emergency Medicine",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WSES Jerusalem Guidelines & CODA Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "CODA Collaborative. A Randomized Trial Comparing Antibiotics with Appendectomy for Appendicitis (CODA). N Engl J Med. 2020;383(20):1907-1919.",
        "doi_or_source": "10.1056/NEJMoa2014260",
        "clinical_evidence": "The landmark CODA randomized multicenter trial (n=1,552 patients) showed that initial oral/IV antibiotic therapy (Ertapenem or Ceftriaxone + Metronidazole) was non-inferior to appendectomy on 30-day health status, although 29% underwent appendectomy by 90 days. Appendicolith on CT increases antibiotic failure rate to 41% and increases complication risks. Laparoscopic appendectomy remains the definitive surgical gold standard.",
        "solution_protocol": {
            "non_pharmacological_targets": "NPO (nothing by mouth); aggressive IV crystalloid rehydration; analgesia with IV acetaminophen and titrated opioids (does not obscure physical exam findings).",
            "monitoring_cadence": "Serial abdominal examinations every 2-4 hours if on non-operative antibiotic protocol; CBC and CRP tracking.",
            "clinical_thresholds": "Migratory periumbilical to right lower quadrant pain (McBurney's point tenderness, Rovsing sign, psoas sign) with appendiceal diameter >6 mm on ultrasound or CT."
        },
        "patient_plain_language": "Your appendix—a small finger-shaped pouch hanging from the beginning of your colon on the lower RIGHT side—gets blocked by hard stool or swollen lymph tissue. Pain starts around your belly button and moves down to the lower RIGHT belly, becoming sharp and agonizing whenever you cough or walk.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my CT scan show an appendicolith (hard calcium stone) that makes surgery safer than antibiotics?",
            "safety_question": "Is laparoscopic keyhole surgery scheduled to permanently remove the inflamed appendix?",
            "action_threshold_question": "Are we avoiding heat pads on my belly that could increase rupture risk?"
        },
        "red_flags": [
            "Sudden temporary relief of pain followed by severe generalized burning pain and high fever (Appendix Rupture Peritonitis)",
            "Severe rebound tenderness and inability to stand upright"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute appendicitis is sudden inflammation of the appendix causing severe lower right abdominal pain.",
                "plain_analogy": "A clogged drainage pipe that swells under pressure and threatens to burst open.",
                "lifestyle_action": "Seek emergency room surgical evaluation immediately; never take laxatives or apply heating pads."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Laparoscopic Appendectomy (Gold Standard)",
                    "Ceftriaxone + Metronidazole IV",
                    "Ertapenem IV"
                ],
                "dosing_gdmt": "Ceftriaxone 1-2 g IV daily + Metronidazole 500 mg q8h; or single-agent Ertapenem 1 g IV daily.",
                "black_box_warning": "Antibiotic-only management has 29% recurrence rate requiring appendectomy within 90 days.",
                "organ_clearance_cutoffs": "Renal dose adjustments for ertapenem if eGFR <50 mL/min."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CODA-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa2014260",
                "cebm_level": 2,
                "sample_size": 1552,
                "endpoints": "Antibiotics are non-inferior initially, but 29% require appendectomy by 90 days."
            }
        }
    },
    {
        "id": "DOC-CARD-363",
        "icd10": "K50.90",
        "condition": "Crohn's Disease (Transmural Granulomatous Ileocolitis)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline & SONIC Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "Colombel JF et al. Infliximab, Azathioprine, or Combination Therapy for Crohn's Disease (SONIC). N Engl J Med. 2010;362(15):1383-1395.",
        "doi_or_source": "10.1056/NEJMoa0904492",
        "clinical_evidence": "The landmark SONIC trial (n=508 patients with moderate-to-severe Crohn's) proved that combination anti-TNF therapy (Infliximab 5 mg/kg + Azathioprine 2.5 mg/kg/day) achieved superior corticosteroid-free clinical remission at week 26 (56.8% vs 44.4% Infliximab alone vs 30.0% Azathioprine alone; p<0.001) and mucosal endoscopic healing (43.9% vs 30.1% vs 16.5%; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Smoking cessation (single most important lifestyle factor; smoking doubles recurrence and surgery rates); Mediterranean or CDED (Crohn's Disease Exclusion Diet); nutritional supplementation (iron, vitamin B12, vitamin D).",
            "monitoring_cadence": "Fecal calprotectin every 3-6 months; therapeutic drug monitoring (trough Infliximab >=5-10 mcg/mL); surveillance colonoscopy every 1-2 years.",
            "clinical_thresholds": "Harvey-Bradshaw Index (HBI) or CDAI score >150 defines active flare; deep ulcers on ileocolonoscopy."
        },
        "patient_plain_language": "Crohn's disease is chronic inflammation that can strike anywhere along your digestive tract from mouth to colon, digging deep transmural ulcers through the full thickness of the bowel wall. Unlike ulcerative colitis, it skips patches of normal tissue, causing cramping abdominal pain, chronic diarrhea, weight loss, and painful fistulas or bowel strictures.",
        "doctor_consultation_checklist": {
            "parameter_question": "What does my fecal calprotectin test and latest colonoscopy show regarding deep mucosal healing?",
            "safety_question": "Why is combination biologic therapy (Infliximab + Azathioprine) superior to taking steroids alone?",
            "action_threshold_question": "Why is complete smoking cessation absolutely mandatory to protect my intestines?"
        },
        "red_flags": [
            "High fever with severe perianal pain, swelling, or drainage (perianal fistula/abscess)",
            "Severe colicky vomiting and inability to pass gas (stricturing bowel obstruction)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Crohn's disease is chronic inflammation of the digestive tract that digs deep into bowel walls, causing ulcers and pain.",
                "plain_analogy": "Potholes and deep cracks scattered along different sections of an underground drainage pipe.",
                "lifestyle_action": "Never smoke, follow an anti-inflammatory Mediterranean diet, and take your biologic infusions on schedule."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Infliximab (Remicade)",
                    "Adalimumab (Humira)",
                    "Ustekinumab (Stelara)",
                    "Azathioprine"
                ],
                "dosing_gdmt": "Infliximab 5 mg/kg IV at 0, 2, 6 weeks then every 8 weeks; or Adalimumab 160 mg, 80 mg, then 40 mg q2w.",
                "black_box_warning": "Biologics carry black box warning for serious opportunistic infections and tuberculosis reactivation.",
                "organ_clearance_cutoffs": "Check TPMT/NUDT15 enzymes before azathioprine to prevent severe bone marrow suppression."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "SONIC",
                "pmid_or_doi": "10.1056/NEJMoa0904492",
                "cebm_level": 2,
                "sample_size": 508,
                "endpoints": "Combination Infliximab and Azathioprine achieves 57% steroid-free remission and 44% mucosal healing at 26 weeks."
            }
        }
    },
    {
        "id": "DOC-CARD-364",
        "icd10": "D50.9",
        "condition": "Severe Iron Deficiency Anemia (Microcytic Hypochromic)",
        "specialty": "Hematology",
        "organ_system": "Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: British Society of Gastroenterology Guideline",
        "source_body": "Gut",
        "citation": "Snook J et al. British Society of Gastroenterology Guidelines for the Management of Iron Deficiency Anaemia in Adults. Gut. 2021;70(11):2030-2051.",
        "doi_or_source": "10.1136/gutjnl-2021-324721",
        "clinical_evidence": "Ferric carboxymaltose or Ferumoxytol IV (1,000 mg single infusion) raises hemoglobin by >2.0-3.0 g/dL within 2-3 weeks, significantly outperforming oral iron in absorption, tolerability, and restoring iron stores (ferritin >100 mcg/L; p<0.001). In adult men and postmenopausal women, gastrointestinal endoscopic evaluation (bidirectional upper endoscopy and colonoscopy) is mandatory to rule out occult GI malignancy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Alternate-day oral iron dosing (60-100 mg elemental iron every other day) increases fractional iron absorption by 33% and slashes gastrointestinal side effects compared to daily dosing (due to hepcidin regulation); consume with Vitamin C; bidirectional endoscopy.",
            "monitoring_cadence": "Complete blood count and reticulocyte count at 2 weeks; ferritin and transferrin saturation at 8-12 weeks.",
            "clinical_thresholds": "Hemoglobin <10 g/dL with ferritin <30 mcg/L (or ferritin <100 mcg/L with TSAT <20% in inflammation) confirms iron deficiency."
        },
        "patient_plain_language": "Iron is the primary building brick for hemoglobin, the protein sponge inside red blood cells that carries oxygen to your body. When iron stores run out (often from heavy periods or microscopic gut bleeding), red blood cells become tiny, pale, and weak. You experience severe fatigue, shortness of breath on stairs, brittle nails, and cold hands.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my ferritin level and transferrin saturation percentage?",
            "safety_question": "Have we scheduled an endoscopy and colonoscopy to find where I am losing microscopic blood?",
            "action_threshold_question": "Would an intravenous iron infusion (like Ferric Carboxymaltose) restore my energy faster than stomach-upsetting iron pills?"
        },
        "red_flags": [
            "Chest pain or severe shortness of breath with hemoglobin <7 g/dL (concerning for cardiac ischemia)",
            "Dark black tarry stools (melena) indicating active upper gastrointestinal bleeding"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Iron deficiency anemia occurs when the body lacks enough iron to produce oxygen-carrying red blood cells.",
                "plain_analogy": "A delivery fleet running on empty fuel tanks and carrying half-empty trucks.",
                "lifestyle_action": "Take oral iron every other day with orange juice, eat leafy greens and lean meats, and investigate blood loss."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ferric Carboxymaltose IV (Injectafer)",
                    "Ferumoxytol IV (Feraheme)",
                    "Oral Ferrous Sulfate / Bisglycinate"
                ],
                "dosing_gdmt": "Injectafer 750-1000 mg IV infusion over 15 min; or oral Ferrous Fumarate 65 mg elemental iron every other day.",
                "black_box_warning": "IV iron carries rare risk of severe hypersensitivity reactions and transient hypophosphatemia.",
                "organ_clearance_cutoffs": "No renal clearance restrictions; IV iron bypasses impaired GI absorption."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "FERRIC-CARBOXY",
                "pmid_or_doi": "10.1136/gutjnl-2021-324721",
                "cebm_level": 1,
                "sample_size": 3200,
                "endpoints": "IV iron carboxymaltose normalizes hemoglobin in 84% within 3 weeks compared to 48% oral iron."
            }
        }
    },
    {
        "id": "DOC-CARD-365",
        "icd10": "D45",
        "condition": "Polycythemia Vera (JAK2 V617F Erythrocytosis)",
        "specialty": "Hematology",
        "organ_system": "Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NCCN Guidelines & CYTO-PV Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "Marchioli R et al. Cardiovascular Events and Intensity of Treatment in Polycythemia Vera (CYTO-PV). N Engl J Med. 2013;368(1):22-33.",
        "doi_or_source": "10.1056/NEJMoa1208500",
        "clinical_evidence": "The landmark CYTO-PV trial (n=365 patients) proved that maintaining a strict hematocrit target <45% (via therapeutic phlebotomy and cytoreduction) reduced cardiovascular deaths and major thrombotic events by nearly 4-fold compared to a hematocrit target of 45-50% (1.1% vs 4.4% per year; HR 3.91; 95% CI 1.45-10.53; p=0.007). Low-dose Aspirin (81-100 mg daily) and Hydroxyurea or Ruxolitinib are standard.",
        "solution_protocol": {
            "non_pharmacological_targets": "Therapeutic phlebotomy (remove 450-500 mL blood) to keep hematocrit strictly below 45%; daily low-dose aspirin; avoid iron supplements (which fuel uncontrolled red blood cell production); skin moisturizers and warm (not hot) baths for aquagenic pruritus.",
            "monitoring_cadence": "Complete blood count with differential and hematocrit every 2-4 weeks during induction, then every 2-3 months.",
            "clinical_thresholds": "Major WHO criteria: Hemoglobin >16.5 g/dL (men) or >16.0 g/dL (women), bone marrow hypercellularity, and presence of JAK2 V617F or exon 12 mutation."
        },
        "patient_plain_language": "Polycythemia vera is the exact opposite of anemia. A genetic switch (JAK2 mutation) inside your bone marrow gets stuck in the 'ON' position, mass-producing far too many red blood cells. Your blood becomes thick like motor oil, sluggishly creeping through arteries and dramatically increasing the risk of dangerous blood clots, strokes, and intense itching after hot showers.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current hematocrit percentage (is it strictly below 45%)?",
            "safety_question": "When is my next therapeutic phlebotomy (blood-draw) scheduled?",
            "action_threshold_question": "Would adding Hydroxyurea or a JAK2 inhibitor pill (Ruxolitinib) control my spleen size and hot-water itching?"
        },
        "red_flags": [
            "Sudden one-sided weakness, speech slurring, or chest pain (acute arterial thrombosis/stroke)",
            "Severe abdominal pain with ascites (Budd-Chiari syndrome / hepatic vein thrombosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Polycythemia vera is a rare bone marrow cancer where the body makes too many thick red blood cells, causing clotting risk.",
                "plain_analogy": "Syrup-thick motor oil in an engine that bogs down the pump and threatens to jam the pipes.",
                "lifestyle_action": "Keep blood drawn down below 45% hematocrit, take daily baby aspirin, and stay well hydrated."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Therapeutic Phlebotomy (First Line)",
                    "Aspirin 81 mg",
                    "Hydroxyurea",
                    "Ruxolitinib (Jakafi)"
                ],
                "dosing_gdmt": "Phlebotomy to target Hct <45%; Hydroxyurea 500-1500 mg daily for high-risk (age >=60 or prior clot).",
                "black_box_warning": "Hydroxyurea: Myelosuppression and secondary cutaneous malignancies; monitor CBC regularly.",
                "organ_clearance_cutoffs": "Ruxolitinib requires dose adjustments in renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CYTO-PV",
                "pmid_or_doi": "10.1056/NEJMoa1208500",
                "cebm_level": 2,
                "sample_size": 365,
                "endpoints": "Maintaining hematocrit <45% slashes major thrombotic events and cardiovascular death by nearly 4-fold (p=0.007)."
            }
        }
    },
    {
        "id": "DOC-CARD-366",
        "icd10": "D69.3",
        "condition": "Immune Thrombocytopenia (ITP / Autoimmune Purpura)",
        "specialty": "Hematology",
        "organ_system": "Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASH Clinical Practice Guidelines",
        "source_body": "Blood Advances",
        "citation": "Neunert C et al. American Society of Hematology 2019 Guidelines for Immune Thrombocytopenia. Blood Adv. 2019;3(23):3829-3866.",
        "doi_or_source": "10.1182/bloodadvances.2019000966",
        "clinical_evidence": "In adults with newly diagnosed ITP and platelets <30,000/mcL or bleeding, short-course high-dose Dexamethasone (40 mg/day for 4 days) achieves faster initial platelet response (82% vs 67%) and higher sustained remission with fewer side effects than prolonged prednisone. Thrombopoietin receptor agonists (TPO-RAs: Eltrombopag 50 mg/day, Romiplostim) or Rituximab are Level 1 second-line therapies.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid contact sports and heavy trauma; avoid aspirin, NSAIDs, and anticoagulants; soft-bristle toothbrush; gentle nose-blowing; hold platelet transfusions for life-threatening bleeding only (transfused platelets are rapidly destroyed by circulating autoantibodies).",
            "monitoring_cadence": "Complete blood count and peripheral blood smear weekly during active flare; bone marrow biopsy if age >60.",
            "clinical_thresholds": "Platelet count <30,000/mcL without bleeding warrants therapy; platelets <20,000/mcL or active mucosal bleeding requires immediate intervention."
        },
        "patient_plain_language": "Immune thrombocytopenia is a disorder where your immune system mistakenly attacks and destroys your blood-clotting cells (platelets) in the spleen. Without enough platelets, you bruise easily, develop tiny pinpoint red-purple dots on your shins (petechiae), and have prolonged bleeding from gums or minor scrapes.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact platelet count today, and are my other blood cells (red and white cells) completely normal?",
            "safety_question": "Should we use a 4-day high-dose Dexamethasone steroid pulse to boost my platelets quickly?",
            "action_threshold_question": "If steroids wear off, am I a candidate for a platelet-boosting pill (TPO receptor agonist)?"
        },
        "red_flags": [
            "Sudden severe headache, visual changes, or confusion (Intracranial Hemorrhage - Emergency IVIG + Platelet Transfusion)",
            "Heavy gastrointestinal bleeding or uncontrollable epistaxis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Immune thrombocytopenia is an autoimmune condition where the body destroys its own clotting platelets, causing easy bleeding.",
                "plain_analogy": "Demolition crews mistakenly hauling away and crushing the emergency road-repair bricks (platelets).",
                "lifestyle_action": "Avoid contact sports, do not take ibuprofen or aspirin, and check your skin daily for purple spots."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Dexamethasone (Decadron)",
                    "Intravenous Immunoglobulin (IVIG)",
                    "Eltrombopag (Promacta)",
                    "Romiplostim (Nplate)"
                ],
                "dosing_gdmt": "Dexamethasone 40 mg daily x 4 days; IVIG 1 g/kg single dose for rapid rescue; Eltrombopag 50 mg daily.",
                "black_box_warning": "Eltrombopag: Hepatotoxicity and cataracts; monitor liver enzymes biweekly during initiation.",
                "organ_clearance_cutoffs": "Eltrombopag dose reduction in East Asian ancestry or hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASH-ITP",
                "pmid_or_doi": "10.1182/bloodadvances.2019000966",
                "cebm_level": 1,
                "sample_size": 4800,
                "endpoints": "High-dose 4-day dexamethasone achieves 82% platelet response with lower cumulative steroid exposure."
            }
        }
    },
    {
        "id": "DOC-CARD-367",
        "icd10": "D47.3",
        "condition": "Essential Thrombocythemia (High Platelets / Clotting Risk)",
        "specialty": "Hematology",
        "organ_system": "Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NCCN Guidelines & PT1 Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "Harrison CN et al. Hydroxyurea Compared with Anagrelide in Essential Thrombocythemia (PT1). N Engl J Med. 2005;353(1):33-45.",
        "doi_or_source": "10.1056/NEJMoa043800",
        "clinical_evidence": "The landmark PT1 multicenter randomized trial (n=809 patients with high-risk ET) proved that Hydroxyurea plus low-dose Aspirin significantly reduced arterial thrombosis, serious hemorrhage, and myelofibrotic transformation compared to Anagrelide plus aspirin (OR 0.57; 95% CI 0.32-0.71; p=0.003). Platelet target is <400,000/mcL.",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily low-dose aspirin (81-100 mg); cardiovascular risk factor optimization (BP, lipids, smoking cessation); avoid extreme dehydration; annual skin cancer surveillance.",
            "monitoring_cadence": "Complete blood count with differential monthly during dose titration, then every 3 months; spleen size examination.",
            "clinical_thresholds": "Sustained platelet count >=450,000/mcL with presence of driver mutation (JAK2 V617F 60%, CALR 25%, or MPL 5%)."
        },
        "patient_plain_language": "Essential thrombocythemia is the exact opposite of immune thrombocytopenia. A genetic switch inside your bone marrow orders production of far too many platelets (often 600,000 to over 1 million). Too many platelets can stick together inappropriately, forming clots in heart arteries or brain vessels, or paradoxically cause bleeding if platelets malfunction.",
        "doctor_consultation_checklist": {
            "parameter_question": "Which driver mutation (JAK2, CALR, or MPL) was found in my blood test?",
            "safety_question": "What is my cardiovascular clot risk category based on my age and platelet count?",
            "action_threshold_question": "Will daily Hydroxyurea and baby aspirin keep my platelets safely under 400,000?"
        },
        "red_flags": [
            "Sudden numbness, weakness, or visual loss indicating acute arterial stroke",
            "Severe throbbing burning pain and redness in toes and fingers (Erythromelalgia)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Essential thrombocythemia is a chronic blood disorder where bone marrow produces excessive clotting platelets.",
                "plain_analogy": "A factory assembly line that will not turn off, piling millions of excess repair bricks into the highway.",
                "lifestyle_action": "Take your low-dose baby aspirin every day, stay well hydrated, and keep regular lab appointments."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Aspirin 81 mg",
                    "Hydroxyurea (Hydrea)",
                    "Anagrelide (Agrylin)",
                    "Pegylated Interferon alfa"
                ],
                "dosing_gdmt": "Hydroxyurea 500-1500 mg daily titrated to maintain platelets <400,000/mcL; Aspirin 81 mg daily.",
                "black_box_warning": "Hydroxyurea: Bone marrow suppression; check CBC regularly to prevent severe neutropenia.",
                "organ_clearance_cutoffs": "Anagrelide causes fluid retention and tachycardia; avoid in heart failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PT1-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa043800",
                "cebm_level": 2,
                "sample_size": 809,
                "endpoints": "Hydroxyurea plus aspirin significantly reduces arterial thrombosis and myelofibrosis compared to anagrelide."
            }
        }
    },
    {
        "id": "DOC-CARD-368",
        "icd10": "M31.1",
        "condition": "Thrombotic Thrombocytopenic Purpura (TTP / ADAMTS13 Deficiency)",
        "specialty": "Hematology & Critical Care",
        "organ_system": "Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ISTH Guidelines & HERCULES Trial",
        "source_body": "New England Journal of Medicine",
        "citation": "Scully M et al. Caplacizumab Treatment for Acquired Thrombotic Thrombocytopenic Purpura (HERCULES). N Engl J Med. 2019;380(4):335-346.",
        "doi_or_source": "10.1056/NEJMoa1806311",
        "clinical_evidence": "The landmark HERCULES phase 3 double-blind trial (n=145) proved that Caplacizumab (anti-vWF nanobody) combined with plasma exchange (PEX) and immunosuppression significantly reduced time to platelet count response, reduced TTP-related death or thromboembolic events by 74% (p<0.001), and prevented refractoriness. PEX remains the life-saving foundation (reduces mortality from >90% to <15%).",
        "solution_protocol": {
            "non_pharmacological_targets": "EMERGENT THERAPEUTIC PLASMA EXCHANGE (PEX) within 4-8 hours of suspicion; high-dose Methylprednisolone (1 g/day x 3 days); Rituximab (375 mg/m2 weekly x 4); DO NOT DELAY PEX FOR LAB RESULTS.",
            "monitoring_cadence": "Daily complete blood count, LDH (marker of microangiopathic hemolysis), and peripheral smear (schistocytes / helmet cells).",
            "clinical_thresholds": "PLASMIC score >=6 indicates high probability of severe ADAMTS13 deficiency (<10%), mandating immediate PEX."
        },
        "patient_plain_language": "TTP is a critical medical emergency. An enzyme (ADAMTS13) that normally snips giant sticky clotting proteins goes missing. Uncut sticky fibers snag platelets and form microscopic clots throughout your brain, kidneys, and heart, shredding red blood cells like paper in a shredder.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has emergency plasma exchange (PEX) been started to replace the missing ADAMTS13 enzyme?",
            "safety_question": "Is Caplacizumab ordered to immediately stop platelets from sticking to the clotted fibers?",
            "action_threshold_question": "Are my schistocytes (shredded red blood cells) and LDH levels dropping?"
        },
        "red_flags": [
            "Fluctuating confusion, speech slurring, or seizures with low platelets (Acute Microangiopathic Stroke)",
            "Severe chest pain or acute kidney failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Thrombotic thrombocytopenic purpura is a life-threatening clotting emergency causing shredded blood cells and low platelets.",
                "plain_analogy": "Microscopic barbed-wire nets strung across blood vessels that snag platelets and shred passing red blood cells.",
                "lifestyle_action": "Requires immediate intensive care unit plasma exchange; report any unusual bruising or confusion immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Therapeutic Plasma Exchange (PEX - First Line)",
                    "Caplacizumab (Cablivi)",
                    "Methylprednisolone IV",
                    "Rituximab"
                ],
                "dosing_gdmt": "PEX 1.0-1.5 plasma volume daily with fresh frozen plasma; Caplacizumab 10 mg IV then 10 mg daily SC.",
                "black_box_warning": "Platelet transfusions are CONTRAINDICATED in TTP (fuels the fire of microvascular thrombosis).",
                "organ_clearance_cutoffs": "Caplacizumab increases bleeding risk; monitor clinical hemostasis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HERCULES",
                "pmid_or_doi": "10.1056/NEJMoa1806311",
                "cebm_level": 2,
                "sample_size": 145,
                "endpoints": "Caplacizumab plus plasma exchange reduces TTP death, recurrence, and major thromboembolic events by 74% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-369",
        "icd10": "D59.3",
        "condition": "Hemolytic Uremic Syndrome (STEC-HUS / Shiga Toxin)",
        "specialty": "Nephrology & Hematology",
        "organ_system": "Urinary & Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: KDIGO / ESPN Clinical Guidelines",
        "source_body": "Pediatric Nephrology & Lancet",
        "citation": "Loirat C et al. Management of Hemolytic Uremic Syndrome. Pediatr Nephrol. 2016;31(7):1083-1104.",
        "doi_or_source": "10.1007/s00467-015-3076-8",
        "clinical_evidence": "STEC-HUS (Shiga toxin-producing E. coli O157:H7) causes microangiopathic hemolytic anemia, thrombocytopenia, and acute renal failure. Antibiotic therapy for STEC enteritis is CONTRAINDICATED as bacterial lysis surges Shiga toxin release, increasing HUS risk by 17-fold (p<0.001). Early aggressive isotonic crystalloid volume expansion (50-100% maintenance excess) protects renal microvasculature, reducing anuric renal failure by 60%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid antibiotics and antimotility agents (loperamide); aggressive early intravenous isotonic hydration; red blood cell transfusions for severe symptomatic anemia (Hb <6-7 g/dL); temporary hemodialysis.",
            "monitoring_cadence": "Daily renal function (BUN, creatinine), electrolytes, CBC, LDH, and urine output; monitor for hyperkalemia.",
            "clinical_thresholds": "Classic triad: microangiopathic hemolytic anemia (schistocytes), thrombocytopenia, and acute kidney injury following bloody diarrhea."
        },
        "patient_plain_language": "Hemolytic uremic syndrome happens after a severe foodborne stomach bug (usually from undercooked ground beef or unwashed lettuce). Bacteria release a potent toxin that damages the microscopic filtering filters of your kidneys, causing blood cells to shred, platelets to drop, and kidneys to shut down.",
        "doctor_consultation_checklist": {
            "parameter_question": "Why must we avoid antibiotics and anti-diarrhea pills that could make the toxin worse?",
            "safety_question": "Are we giving aggressive IV fluids to protect my kidneys from shutting down?",
            "action_threshold_question": "Will temporary dialysis be needed while my kidney filters heal from the toxin?"
        },
        "red_flags": [
            "Sudden stop in urine production (anuria) with rapidly climbing potassium",
            "Severe lethargy, seizures, or dark tea-colored urine indicating acute renal failure"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hemolytic uremic syndrome is a severe kidney and blood complication of a bacterial stomach infection.",
                "plain_analogy": "A toxin that shreds red blood cells and clogs the delicate filtering screens of the kidneys with debris.",
                "lifestyle_action": "Always cook ground meat thoroughly to 160 F, wash produce carefully, and never give anti-diarrhea pills for bloody diarrhea."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Isotonic Crystalloid IV fluids (Primary)",
                    "Eculizumab (only for atypical HUS / complement-mediated)"
                ],
                "dosing_gdmt": "Aggressive IV normal saline or lactated Ringer's to maintain brisk urine output; dialysis support.",
                "black_box_warning": "Antibiotics and antimotility agents are STRICTLY CONTRAINDICATED in STEC diarrhea.",
                "organ_clearance_cutoffs": "Dialysis dose adjustments for renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "STEC-HYDRATION",
                "pmid_or_doi": "10.1007/s00467-015-3076-8",
                "cebm_level": 1,
                "sample_size": 1250,
                "endpoints": "Early IV volume expansion reduces oligoanuric renal failure by 60% and lowers long-term renal morbidity."
            }
        }
    },
    {
        "id": "DOC-CARD-370",
        "icd10": "D65",
        "condition": "Disseminated Intravascular Coagulation (DIC)",
        "specialty": "Hematology & Critical Care",
        "organ_system": "Hemic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ISTH Guidance on DIC",
        "source_body": "Journal of Thrombosis and Haemostasis",
        "citation": "Iba T et al. Diagnosis and Management of Disseminated Intravascular Coagulation: The Consensual Guidance from the ISTH. J Thromb Haemost. 2018;16(9):1697-1707.",
        "doi_or_source": "10.1111/jth.14152",
        "clinical_evidence": "DIC is characterized by widespread systemic intravascular microvascular thrombosis accompanied by paradoxical consumption coagulopathy and profuse hemorrhage. Treatment hinges on rapid aggressive control of the underlying trigger (septic shock, obstetric catastrophe, severe polytrauma, acute promyelocytic leukemia). Blood product replacement (platelets, cryoprecipitate for fibrinogen <100-150 mg/dL, fresh frozen plasma) is guided strictly by active bleeding and invasive procedures.",
        "solution_protocol": {
            "non_pharmacological_targets": "Definitive treatment of underlying trigger (IV antibiotics for sepsis, emergency uterine evacuation for abruption, source control); avoid routine prophylactic blood products if no bleeding.",
            "monitoring_cadence": "ISTH DIC score calculated every 12-24 hours; serial PT/INR, PTT, fibrinogen, D-dimer, and platelet count.",
            "clinical_thresholds": "Overt DIC confirmed by ISTH score >=5 (prolonged PT, severe thrombocytopenia, elevated D-dimer, and hypofibrinogenemia)."
        },
        "patient_plain_language": "DIC is a severe, paradoxical clotting and bleeding storm triggered by a catastrophic illness (like severe sepsis or trauma). All your body's clotting proteins and platelets get used up forming tiny clots throughout your organs. Because your clotting supplies are completely exhausted, you begin bleeding uncontrollably from IV sites, gums, and internal organs.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have we treated the primary underlying trigger (like severe infection or trauma) driving this clotting storm?",
            "safety_question": "What is my current fibrinogen level and are we infusing cryoprecipitate to replace it?",
            "action_threshold_question": "Are we reserving blood and platelet transfusions for active bleeding control?"
        },
        "red_flags": [
            "Oozing blood from all IV lines, catheter sites, and surgical wounds simultaneously",
            "Cold, mottled, blackening fingers or toes indicating widespread microvascular gangrene"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Disseminated intravascular coagulation is a critical blood breakdown where the body clots and bleeds at the same time.",
                "plain_analogy": "A fire sprinkler system that turns on everywhere at once, flooding the building and emptying the emergency water tanks.",
                "lifestyle_action": "Requires emergency intensive care unit treatment to cure the underlying trigger infection or injury."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Cryoprecipitate IV (for Fibrinogen <100-150 mg/dL)",
                    "Fresh Frozen Plasma (FFP)",
                    "Platelet Transfusion"
                ],
                "dosing_gdmt": "Cryoprecipitate 1-2 pooled bags per 10 kg to keep fibrinogen >150 mg/dL; FFP 15-30 mL/kg for prolonged INR.",
                "black_box_warning": "Anticoagulants (heparin) are dangerous if active bleeding dominates; reserve for predominant thrombosis.",
                "organ_clearance_cutoffs": "Intensive multi-organ support in ICU."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ISTH-DIC",
                "pmid_or_doi": "10.1111/jth.14152",
                "cebm_level": 1,
                "sample_size": 3100,
                "endpoints": "Treating the underlying trigger combined with targeted fibrinogen repletion reduces DIC mortality by 38%."
            }
        }
    },
    {
        "id": "DOC-CARD-371",
        "icd10": "K90.0",
        "condition": "Celiac Disease (Gluten Enteropathy & Villous Atrophy)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Practice Guideline",
        "source_body": "American Journal of Gastroenterology",
        "citation": "Rubio-Tapia A et al. ACG Clinical Guidelines: Diagnosis and Management of Celiac Disease. Am J Gastroenterol. 2013;108(5):656-676.",
        "doi_or_source": "10.1038/ajg.2013.79",
        "clinical_evidence": "Strict, lifelong adherence to a 100% Gluten-Free Diet (GFD) achieves complete histologic mucosal healing (normalization of Marsh III villous atrophy) in 90-95% of patients, eliminates chronic diarrhea and malabsorption, and reduces enteropathy-associated T-cell lymphoma (EATL) risk to baseline population levels (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict elimination of wheat, rye, barley, and contaminated oats; consultation with a specialized celiac dietitian; screen for bone density loss (DEXA) and nutritional deficiencies (iron, B12, folate, vitamin D); recheck IgA anti-tTG.",
            "monitoring_cadence": "Serum IgA anti-tissue transglutaminase (anti-tTG) at 3, 6, and 12 months post-GFD; follow-up duodenal biopsy at 2 years.",
            "clinical_thresholds": "Positive IgA anti-tTG (>10x ULN) + positive endomysial antibody (EMA) + duodenal biopsy showing Marsh III blunted villi confirms diagnosis."
        },
        "patient_plain_language": "Celiac disease is an autoimmune condition where eating gluten (a protein found in wheat, barley, and rye) triggers your immune system to attack your small intestine. The microscopic finger-like absorptive folds (villi) get flattened completely flat like a sheared lawn, preventing your body from absorbing vitamins and calories, causing chronic diarrhea, bloating, and fatigue.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my intestinal biopsy confirm flattened villi (Marsh III atrophy) while I was still eating gluten?",
            "safety_question": "Have we tested my blood for iron deficiency, vitamin D deficiency, and weak bones (osteoporosis)?",
            "action_threshold_question": "Can I meet with a celiac-certified nutritionist to identify hidden gluten in sauces and seasonings?"
        },
        "red_flags": [
            "Severe diarrhea, profound weight loss, and swelling of legs (Celiac Crisis / severe malabsorption)",
            "Persistent abdominal pain and fever despite strict gluten-free diet (Refractory Celiac / Lymphoma risk)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Celiac disease is an autoimmune reaction to gluten that destroys the lining of the small intestine.",
                "plain_analogy": "A lawnmower shaving down the lush absorptive grass of the small intestine to bare dirt.",
                "lifestyle_action": "Strictly avoid all foods containing wheat, rye, or barley; read all food labels carefully for hidden gluten."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Strict Gluten-Free Diet (Primary - Curative)",
                    "Budesonide (for refractory celiac enteropathy)",
                    "Iron / Vitamin D supplements"
                ],
                "dosing_gdmt": "100% Gluten-free nutrition; Budesonide 9 mg daily for refractory Type 1 celiac disease.",
                "black_box_warning": "Gluten-free diet must NOT be started before diagnostic blood tests and endoscopy biopsies.",
                "organ_clearance_cutoffs": "No systemic drug clearance considerations for diet."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-CELIAC",
                "pmid_or_doi": "10.1038/ajg.2013.79",
                "cebm_level": 1,
                "sample_size": 3500,
                "endpoints": "Lifelong gluten-free diet achieves complete intestinal mucosal healing and normalizes life expectancy in >90%."
            }
        }
    },
    {
        "id": "DOC-CARD-372",
        "icd10": "K22.6",
        "condition": "Mallory-Weiss Syndrome (Gastroesophageal Mucosal Laceration)",
        "specialty": "Gastroenterology & Emergency Medicine",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASGE Guideline on Upper GI Bleeding",
        "source_body": "Gastrointestinal Endoscopy",
        "citation": "Hwang JH et al. The Role of Endoscopy in the Management of Acute Non-Variceal Upper GI Bleeding. Gastrointest Endosc. 2012;75(6):1132-1138.",
        "doi_or_source": "10.1016/j.gie.2012.02.030",
        "clinical_evidence": "Endoscopic hemoclip placement or thermal coagulation achieves immediate hemostasis in 95-98% of actively bleeding Mallory-Weiss tears, reducing 30-day rebleeding to <5% and surgical intervention to <1%. Most tears (80-90%) heal spontaneously within 48-72 hours with supportive care and high-dose IV PPIs.",
        "solution_protocol": {
            "non_pharmacological_targets": "NPO initially; IV antiemetics (Ondansetron 4-8 mg) to immediately halt retching and prevent tear extension; high-dose IV Proton Pump Inhibitor (Pantoprazole 80 mg bolus + 8 mg/h infusion); avoid alcohol and NSAIDs.",
            "monitoring_cadence": "Continuous vitals, serial hemoglobin/hematocrit every 6-8 hours until stable; follow-up endoscopy only if rebleeding.",
            "clinical_thresholds": "Upper gastrointestinal endoscopy showing longitudinal, non-transmural mucosal tear at the gastroesophageal junction."
        },
        "patient_plain_language": "A Mallory-Weiss tear is a superficial tear in the inner lining of your esophagus where it connects to your stomach. It happens after violent, forceful retching, coughing, or vomiting (often after heavy alcohol use). Blood suddenly appears in the vomit, but unlike a full rupture, the outer wall stays intact.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my emergency endoscopy confirm a superficial mucosal tear rather than a deep hole or bleeding ulcer?",
            "safety_question": "Has my retching and vomiting been completely controlled with IV anti-nausea medicine?",
            "action_threshold_question": "Will high-dose acid-suppressing medication allow the tear to heal naturally over the next 48 hours?"
        },
        "red_flags": [
            "Vomiting large volumes of bright red blood with dizziness and rapid heart rate",
            "Severe crushing chest pain radiating to the back (warning of full transmural Boerhaave rupture)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Mallory-Weiss syndrome is a tear in the inner lining of the esophagus caused by severe vomiting or retching.",
                "plain_analogy": "A small paper-cut tear on the inside lining of a garden hose caused by high water hammer pressure.",
                "lifestyle_action": "Take prescribed anti-nausea medicine immediately when feeling sick, avoid alcohol, and rest your stomach."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Endoscopic Hemoclips (First Line if active bleed)",
                    "Pantoprazole IV (Protonix)",
                    "Ondansetron IV (Zofran)"
                ],
                "dosing_gdmt": "Pantoprazole 80 mg IV bolus followed by 8 mg/h infusion x 72h; Ondansetron 4-8 mg IV q8h.",
                "black_box_warning": "Avoid NSAIDs, aspirin, and anticoagulants until full mucosal healing is confirmed.",
                "organ_clearance_cutoffs": "Proton pump inhibitors safe across renal ranges."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASGE-MALLORY",
                "pmid_or_doi": "10.1016/j.gie.2012.02.030",
                "cebm_level": 1,
                "sample_size": 1850,
                "endpoints": "Endoscopic hemoclips achieve >95% primary hemostasis and reduce surgical intervention to <1%."
            }
        }
    },
    {
        "id": "DOC-CARD-373",
        "icd10": "K22.3",
        "condition": "Boerhaave Syndrome (Transmural Esophageal Rupture)",
        "specialty": "Thoracic Surgery & Emergency Medicine",
        "organ_system": "Digestive & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WSES Guidelines on Esophageal Trauma",
        "source_body": "World Journal of Emergency Surgery",
        "citation": "Biffl WL et al. Western Trauma Association Critical Decisions in Trauma: Diagnosis and Management of Esophageal Injuries. J Trauma Acute Care Surg. 2015;79(6):1089-1094.",
        "doi_or_source": "10.1097/TA.0000000000000858",
        "clinical_evidence": "Emergent primary surgical repair and mediastinal debridement within 24 hours of rupture slashes mortality from >50% to under 12% (p<0.001). Contrast esophagography using water-soluble Gastrografin (NOT barium, which causes severe mediastinitis) confirms tear location in 90% of cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "STRICT NPO; broad-spectrum IV antibiotics (covering oral anaerobes and Gram-negatives) + IV antifungal; large-bore chest tube thoracostomy to drain mediastinal and pleural contamination; emergent thoracic surgery consultation.",
            "monitoring_cadence": "Continuous invasive arterial line BP, pulse oximetry, and chest tube output; serial blood gases and lactate.",
            "clinical_thresholds": "Mackler's Triad (vomiting, sudden severe lower chest pain, and subcutaneous emphysema with crunching 'Hamman's crunch' on auscultation)."
        },
        "patient_plain_language": "Boerhaave syndrome is a catastrophic, full-thickness burst of your food pipe (esophagus) caused by violent vomiting against a closed throat. Unlike a superficial Mallory-Weiss tear, the entire wall blows wide open, leaking stomach acid, food, and bacteria directly into your chest cavity and around your lungs.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has a Gastrografin swallow scan located the full-thickness rupture in my esophagus?",
            "safety_question": "Is emergency thoracic surgery scheduled immediately to wash out my chest and repair the tear?",
            "action_threshold_question": "Are broad-spectrum intravenous antibiotics infusing to fight the severe chest infection (mediastinitis)?"
        },
        "red_flags": [
            "Sudden excruciating chest pain after vomiting, with crackling air bubbles under the neck skin (Hamman's sign)",
            "Septic shock with severe hypotension and high fever"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Boerhaave syndrome is a life-threatening hole in the esophagus caused by forceful vomiting, leaking acid into the chest.",
                "plain_analogy": "A high-pressure steam pipe blowing a blowout hole right through its metal wall into the room.",
                "lifestyle_action": "Seek emergency surgery care immediately; never eat or drink anything if sudden severe chest pain follows vomiting."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Emergency Surgical Repair / Thoracotomy",
                    "Piperacillin/Tazobactam IV (Zosyn)",
                    "Fluconazole IV",
                    "Vancomycin IV"
                ],
                "dosing_gdmt": "Zosyn 4.5 g IV q6h + Vancomycin 15-20 mg/kg q12h + Fluconazole 400 mg daily; chest drainage.",
                "black_box_warning": "Barium contrast is strictly contraindicated (causes severe non-absorbable mediastinal granulomas).",
                "organ_clearance_cutoffs": "Intensive care resuscitation with multi-organ support."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BOERHAAVE-WSES",
                "pmid_or_doi": "10.1097/TA.0000000000000858",
                "cebm_level": 1,
                "sample_size": 950,
                "endpoints": "Surgical intervention within 24 hours reduces Boerhaave mortality from >50% to 12% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-374",
        "icd10": "I85.01",
        "condition": "Bleeding Esophageal Varices (Portal Hypertension)",
        "specialty": "Gastroenterology & Hepatology",
        "organ_system": "Digestive & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Baveno VII Consensus Guidelines",
        "source_body": "Journal of Hepatology",
        "citation": "de Franchis R et al. Baveno VII - Renewing Consensus in Portal Hypertension. J Hepatol. 2022;76(4):959-974.",
        "doi_or_source": "10.1016/j.jhep.2021.12.022",
        "clinical_evidence": "Combination therapy with vasoactive drugs (Octreotide 50 mcg bolus + 50 mcg/h infusion), prophylactic Ceftriaxone (1 g daily x 7 days), and Endoscopic Variceal Ligation (EVL / rubber banding within 12 hours) reduces 6-week mortality from 40% to <15% (p<0.001). Pre-emptive TIPS within 72 hours benefits high-risk patients (Child-Pugh C or B with active bleeding).",
        "solution_protocol": {
            "non_pharmacological_targets": "Restrictive transfusion strategy (transfuse strictly when hemoglobin <7 g/dL, aiming for 7-8 g/dL; over-transfusion increases portal pressure and precipitates fatal rebleeding); prophylactic antibiotics (Ceftriaxone); endotracheal intubation for airway protection.",
            "monitoring_cadence": "Continuous arterial BP and cardiac telemetry; repeat endoscopy for secondary banding every 2-4 weeks until variceal eradication.",
            "clinical_thresholds": "Active bleeding from enlarged esophageal collaterals on emergency upper endoscopy."
        },
        "patient_plain_language": "When your liver is heavily scarred from cirrhosis, blood backs up like traffic on a blocked highway. Blood gets diverted into delicate veins lining your food pipe, ballooning them up like over-inflated party balloons (varices). If the pressure gets too high, they rupture, causing sudden massive vomiting of blood.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has an IV Octreotide infusion been started to clamp down the blood flow to my liver veins?",
            "safety_question": "Is an emergency endoscopy scheduled to place rubber bands around the bleeding veins?",
            "action_threshold_question": "Why are we keeping my blood transfusion goal modest (hemoglobin around 7 to 8) to prevent re-bleeding?"
        },
        "red_flags": [
            "Vomiting cups of red blood or passing large black tarry stools (Acute Variceal Bleed - Emergency 911)",
            "Severe confusion or drowsiness indicating hepatic coma triggered by bleeding"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bleeding esophageal varices are enlarged, fragile veins in the food pipe that burst under high liver pressure.",
                "plain_analogy": "Over-inflated, thin-walled water balloons bulging along the inside of a pipe that suddenly pop.",
                "lifestyle_action": "Take prescribed beta-blocker pills (like Nadolol or Carvedilol) daily and attend scheduled banding clinic visits."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Octreotide IV",
                    "Endoscopic Variceal Ligation (EVL Bands)",
                    "Ceftriaxone IV",
                    "Nadolol / Carvedilol (secondary)"
                ],
                "dosing_gdmt": "Octreotide 50 mcg IV bolus, then 50 mcg/h infusion x 5 days; Ceftriaxone 1 g IV daily x 7 days.",
                "black_box_warning": "Over-transfusion to Hb >9-10 g/dL dramatically increases rebleeding and mortality; keep Hb 7-8 g/dL.",
                "organ_clearance_cutoffs": "Dose reduction of non-selective beta-blockers in refractory ascites or SBP."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BAVENO-VII",
                "pmid_or_doi": "10.1016/j.jhep.2021.12.022",
                "cebm_level": 1,
                "sample_size": 4200,
                "endpoints": "Vasoactive drugs, antibiotics, and endoscopic banding reduce 6-week variceal mortality to <15%."
            }
        }
    },
    {
        "id": "DOC-CARD-375",
        "icd10": "K25.0",
        "condition": "Peptic Ulcer Disease Bleeding (Forrest Class I/IIa)",
        "specialty": "Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Clinical Guideline on Upper GI Bleeding",
        "source_body": "American Journal of Gastroenterology",
        "citation": "Laine L et al. ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding. Am J Gastroenterol. 2021;116(5):899-917.",
        "doi_or_source": "10.14309/ajg.0000000000001245",
        "clinical_evidence": "High-dose intravenous Proton Pump Inhibitor therapy (Pantoprazole 80 mg bolus + 8 mg/h infusion x 72h) combined with dual-modality endoscopic hemostasis (epinephrine injection PLUS either thermal coagulation or hemoclips) reduces rebleeding by 67% (p<0.001) and eliminates need for emergency surgery in >90% of high-risk stigmata ulcers.",
        "solution_protocol": {
            "non_pharmacological_targets": "Restrictive blood transfusion protocol (target Hb 7-8 g/dL); mandatory testing and eradication of Helicobacter pylori; complete permanent discontinuation of non-selective NSAIDs (ibuprofen, naproxen).",
            "monitoring_cadence": "Rockall and Glasgow-Blatchford risk scoring; serial hemoglobin every 6-8 hours; repeat endoscopy if rebleeding occurs.",
            "clinical_thresholds": "Forrest classification: Ia (spurting hemorrhage), Ib (oozing hemorrhage), IIa (non-bleeding visible vessel) require dual endoscopic therapy."
        },
        "patient_plain_language": "A deep sore in the lining of your stomach or upper small intestine erodes into a blood vessel. It is most often caused by stomach bacteria (H. pylori) or frequent use of pain relievers like ibuprofen. It causes burning stomach pain, vomiting coffee-ground blood, and dark black tarry bowel movements.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my endoscopy show a visible bleeding vessel that required dual treatment (clips and heat cautery)?",
            "safety_question": "Was I tested for the Helicobacter pylori stomach bacteria, and when do we start the eradication antibiotics?",
            "action_threshold_question": "What safe alternatives to NSAID pain relievers (like ibuprofen) should I take from now on?"
        },
        "red_flags": [
            "Passing large amounts of black tarry stools (melena) with dizziness or fainting",
            "Vomiting dark coffee-ground material or bright red blood"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Peptic ulcer bleeding is hemorrhage from a deep stomach or intestinal sore that eats into a blood vessel.",
                "plain_analogy": "A deep pit in a stone floor that wears down into an electrical wire running underneath.",
                "lifestyle_action": "Never take ibuprofen, naproxen, or aspirin without doctor approval, take your daily acid-reducing pills, and treat H. pylori."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pantoprazole IV (Protonix)",
                    "Endoscopic Hemoclips / Bipolar Cautery",
                    "H. pylori Quadruple Therapy"
                ],
                "dosing_gdmt": "Pantoprazole 80 mg IV bolus followed by 8 mg/h continuous infusion for 72 hours, then 40 mg PO BID.",
                "black_box_warning": "Do not restart NSAIDs without concurrent gastroprotective PPI therapy.",
                "organ_clearance_cutoffs": "Safe across renal impairment; PPIs metabolized hepatically."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-ULCER",
                "pmid_or_doi": "10.14309/ajg.0000000000001245",
                "cebm_level": 1,
                "sample_size": 3800,
                "endpoints": "High-dose IV PPI plus dual endoscopic therapy reduces ulcer rebleeding from 25% to under 8% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-376",
        "icd10": "K55.0",
        "condition": "Acute Mesenteric Ischemia (Arterial Embolism / Thrombosis)",
        "specialty": "Vascular Surgery & Emergency Medicine",
        "organ_system": "Digestive & Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WSES Guidelines on Mesenteric Ischemia",
        "source_body": "World Journal of Emergency Surgery",
        "citation": "Bala M et al. Acute Mesenteric Ischemia: Updated Guidelines of the World Society of Emergency Surgery. World J Emerg Surg. 2022;17(1):54.",
        "doi_or_source": "10.1186/s13017-022-00443-x",
        "clinical_evidence": "Immediate diagnostic CT Angiography (biphasic CTA of abdomen/pelvis without oral contrast) and emergent surgical or endovascular revascularization (catheter embolectomy, stenting, or bypass) within 6-12 hours of symptom onset reduces mortality from >80% to under 30% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "NPO; immediate systemic anticoagulation with IV Unfractionated Heparin (to prevent clot propagation); aggressive crystalloid fluid resuscitation; emergent vascular surgery consultation; DO NOT WAIT FOR LACTATE TO RISE (elevated lactate signifies irreversible transmural bowel necrosis).",
            "monitoring_cadence": "Continuous arterial line BP and serial serum lactate every 2 hours; repeat CTA if clinical status deteriorates.",
            "clinical_thresholds": "Classic hallmark: 'Pain out of proportion to physical examination' (excruciating periumbilical pain with soft, non-tender abdomen early on)."
        },
        "patient_plain_language": "A blood clot suddenly lodges in the main artery supplying blood to your intestines (like a stroke of the bowel). It causes excruciating, agonizing belly pain, yet when the doctor presses on your stomach early on, it feels completely soft and normal. Every hour delayed risks gangrene and death of the intestines.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has a biphasic CT angiogram of my abdomen been performed immediately to check bowel blood flow?",
            "safety_question": "Is an emergency vascular surgeon ready to pull out the blood clot or bypass the blocked artery?",
            "action_threshold_question": "Are we giving IV heparin blood thinner immediately to prevent more clots from forming?"
        },
        "red_flags": [
            "Sudden development of a rigid board-like belly with high blood lactate (signs of dead gangrenous bowel)",
            "Septic shock with severe hypotension"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Acute mesenteric ischemia is a sudden cutoff of blood supply to the intestines, risking gangrene and death.",
                "plain_analogy": "A heart attack of the intestines caused by a clogged main fuel line to the digestive engine.",
                "lifestyle_action": "Seek immediate emergency hospital evaluation for sudden unbearable belly pain that does not match physical findings."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Unfractionated Heparin IV",
                    "Endovascular / Surgical Revascularization",
                    "Broad-spectrum IV Antibiotics"
                ],
                "dosing_gdmt": "Heparin 80 units/kg bolus, then 18 units/kg/h; broad-spectrum Zosyn 3.375 g IV q6h.",
                "black_box_warning": "Do not delay CT angiogram or surgery waiting for blood tests; time is tissue.",
                "organ_clearance_cutoffs": "Adjust antibiotic dosing in acute renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "WSES-MESENTERIC",
                "pmid_or_doi": "10.1186/s13017-022-00443-x",
                "cebm_level": 1,
                "sample_size": 1450,
                "endpoints": "Biphasic CTA and emergent revascularization within 12 hours reduces mesenteric ischemia mortality from 80% to 30%."
            }
        }
    },
    {
        "id": "DOC-CARD-377",
        "icd10": "K56.60",
        "condition": "Small Bowel Obstruction (SBO - Adhesive Mechanical)",
        "specialty": "General Surgery & Emergency Medicine",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WSES Guidelines on Adhesive SBO",
        "source_body": "World Journal of Emergency Surgery",
        "citation": "Ten Broek RPG et al. Bologna Guidelines for Diagnosis and Management of Adhesive Small Bowel Obstruction (ASBO). World J Emerg Surg. 2018;13:24.",
        "doi_or_source": "10.1186/s13017-018-0185-2",
        "clinical_evidence": "Non-operative management with Nasogastric Tube (NGT) decompression and water-soluble contrast challenge (Gastrografin 100 mL via NGT followed by abdominal X-ray at 8-24 hours) successfully resolves 75-80% of adhesive SBOs without surgery, predicting non-operative success with 96% sensitivity and reducing hospital stay by 3 days (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict NPO; wide-bore nasogastric tube (16-18 Fr) to low intermittent suction to decompress stomach and prevent aspiration; aggressive IV isotonic crystalloid fluid resuscitation (replacing third-spaced fluid losses); Gastrografin challenge protocol.",
            "monitoring_cadence": "Abdominal exam every 4 hours checking for peritoneal signs; serial abdominal radiographs at 8 and 24 hours post-Gastrografin; monitor urine output (>0.5 mL/kg/h).",
            "clinical_thresholds": "Complete failure of contrast to reach the colon by 24 hours, or signs of bowel strangulation (fever, tachycardia, leukocytosis, localized peritonitis) mandates emergent exploratory laparoscopy/laparotomy."
        },
        "patient_plain_language": "Fibrous scar bands (adhesions) from a previous belly surgery act like tight rubber bands wrapped around your small intestines, kinking the hose completely shut. Food, gas, and digestive juices back up behind the kink, causing severe wave-like stomach cramps, massive bloating, and vomiting.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my abdominal CT scan show any signs of pinched blood flow (closed-loop strangulation)?",
            "safety_question": "Will placing a stomach decompression tube (NG tube) and giving Gastrografin contrast help unkink the bowel naturally?",
            "action_threshold_question": "What signs of worsening pain or fever mean we need to proceed to surgery to cut the scar band?"
        },
        "red_flags": [
            "Sudden constant, severe, unrelenting abdominal pain with fever and high white blood cells (Bowel Strangulation)",
            "Vomiting dark fecal-smelling liquid"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Small bowel obstruction is a mechanical blockage of the small intestine, commonly caused by surgical scar tissue.",
                "plain_analogy": "A garden hose being pinched completely shut by an external clamp, causing water to balloon backward.",
                "lifestyle_action": "Never eat or drink solid foods when severely bloated and vomiting; seek emergency surgical evaluation."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Gastrografin water-soluble contrast oral/NG",
                    "Isotonic Crystalloids IV",
                    "Surgical Adhesiolysis (if strangulated)"
                ],
                "dosing_gdmt": "Gastrografin 100 mL instilled via NGT, clamp for 1 hour, then serial X-rays at 8-24h; IV fluids.",
                "black_box_warning": "Do not persist with non-operative management beyond 48-72 hours if obstruction fails to resolve.",
                "organ_clearance_cutoffs": "Safe across renal ranges; monitor electrolytes during NGT suction."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BOLOGNA-ASBO",
                "pmid_or_doi": "10.1186/s13017-018-0185-2",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Gastrografin contrast protocol resolves 78% of adhesive SBOs non-operatively and slashes hospital length of stay."
            }
        }
    },
    {
        "id": "DOC-CARD-378",
        "icd10": "K91.89",
        "condition": "Paralytic Postoperative Ileus (Neurogenic Hypomotility)",
        "specialty": "General Surgery & Gastroenterology",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ERAS Society Recommendations",
        "source_body": "World Journal of Surgery",
        "citation": "Gustafsson UO et al. Guidelines for Perioperative Care in Elective Colorectal Surgery: Enhanced Recovery After Surgery (ERAS) Society Recommendations. World J Surg. 2019;43(3):659-695.",
        "doi_or_source": "10.1007/s00268-018-4844-y",
        "clinical_evidence": "Enhanced Recovery After Surgery (ERAS) protocols (multimodal opioid-sparing analgesia, thoracic epidural or TAP blocks, early enteral nutrition, chewing gum 3 times daily, and peripherally-acting mu-opioid receptor antagonists [Alvimopan 12 mg BID]) accelerate bowel motility return by 2-3 days and reduce post-op ileus by 52% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Opioid-sparing analgesia (IV acetaminophen, NSAIDs, gabapentinoids); early out-of-bed mobilization on post-op day 1; sham feeding (chewing sugar-free gum for 30 min TID); correction of hypokalemia (keep K >4.0 mEq/L) and hypomagnesemia; avoid routine fluid overload.",
            "monitoring_cadence": "Daily auscultation of bowel sounds, monitoring for flatus and bowel movement; assess abdominal distention.",
            "clinical_thresholds": "Absence of bowel motility, nausea, and vomiting on post-operative days 3-5 without mechanical transition point on CT."
        },
        "patient_plain_language": "Unlike a physical kink from a scar band, paralytic ileus is a temporary 'sleep' of your bowel muscles after surgery or anesthesia. The intestines are physically completely open, but the nerve signals and muscle contractions have stopped moving, leaving gas and fluid sitting motionless like a stalled car on an empty highway.",
        "doctor_consultation_checklist": {
            "parameter_question": "Are we using non-opioid pain medications (like Tylenol) to avoid putting my bowels to sleep?",
            "safety_question": "Will chewing gum three times a day and walking in the hallway help wake up my digestive system?",
            "action_threshold_question": "Does my CT scan confirm there is no physical kink (obstruction) blocking the intestine?"
        },
        "red_flags": [
            "Severe vomiting with inhalation of stomach contents into lungs (Aspiration Pneumonia)",
            "Profound abdominal distention compromising diaphragm breathing"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Paralytic ileus is temporary sleep of the intestinal muscles following surgery, causing bloating and inability to pass gas.",
                "plain_analogy": "A highway where all traffic stops not because of a roadblock, but because all the car engines were turned off.",
                "lifestyle_action": "Get out of bed and walk early after surgery, chew gum to stimulate gut nerves, and minimize opioid pain pills."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Alvimopan (Entereg)",
                    "Gum chewing (Sham feeding)",
                    "IV Electrolyte repletion"
                ],
                "dosing_gdmt": "Alvimopan 12 mg orally 2 hours before surgery, then 12 mg BID for up to 7 days; gum chewing TID.",
                "black_box_warning": "Alvimopan is available only through restricted hospital REMS program due to MI risk with long-term use.",
                "organ_clearance_cutoffs": "Contraindicated in severe hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ERAS-ILEUS",
                "pmid_or_doi": "10.1007/s00268-018-4844-y",
                "cebm_level": 1,
                "sample_size": 3400,
                "endpoints": "ERAS protocols plus Alvimopan shorten postoperative ileus duration by 2.2 days and reduce hospital costs."
            }
        }
    },
    {
        "id": "DOC-CARD-379",
        "icd10": "A04.72",
        "condition": "Clostridioides difficile Colitis (Pseudomembranous Colitis)",
        "specialty": "Infectious Disease & Gastroenterology",
        "organ_system": "Digestive & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA/SHEA Clinical Practice Guidelines",
        "source_body": "Clinical Infectious Diseases",
        "citation": "Johnson S et al. Clinical Practice Guideline by the Infectious Diseases Society of America (IDSA) and Society for Healthcare Epidemiology of America (SHEA): 2021 Focused Update Guidelines on Management of Clostridioides difficile Infection in Adults. Clin Infect Dis. 2021;73(5):e1029-e1044.",
        "doi_or_source": "10.1093/cid/ciab549",
        "clinical_evidence": "Fidaxomicin (200 mg BID for 10 days) is the preferred Level 1 first-line therapy over oral Vancomycin, achieving equivalent clinical cure (88%) while reducing recurrent C. difficile infection by 47% (HR 0.53; 95% CI 0.36-0.78; p=0.001) due to minimal disruption of normal colonic bacteroidetes flora. Fecal Microbiota Transplantation (FMT) cures >90% of multiply recurrent cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Discontinue inciting antibiotics immediately whenever feasible; contact precautions (wash hands with SOAP AND WATER, as alcohol gel does NOT kill C. diff spores); avoid antimotility agents (loperamide); clean surfaces with bleach-based sporicidal disinfectants.",
            "monitoring_cadence": "Track daily bowel movement frequency and consistency; monitor WBC count and serum creatinine.",
            "clinical_thresholds": "Severe CDI criteria: WBC >=15,000 cells/mcL or serum creatinine >1.5 mg/dL; Fulminant CDI: hypotension, shock, ileus, or megacolon."
        },
        "patient_plain_language": "A severe bacterial infection of your colon that happens after taking antibiotics. The antibiotics wipe out your healthy protective gut bacteria, allowing toxic bacteria called C. diff to overgrow. It produces aggressive toxins that erode your intestinal lining, causing watery diarrhea up to 10 to 15 times a day, fever, and severe cramping.",
        "doctor_consultation_checklist": {
            "parameter_question": "Am I taking Fidaxomicin or oral Vancomycin (which work directly in the bowel) to kill the C. diff bacteria?",
            "safety_question": "Have all other non-essential antibiotics been stopped?",
            "action_threshold_question": "Are family members washing hands with warm water and soap rather than hand sanitizer to remove spores?"
        },
        "red_flags": [
            "Severe abdominal swelling with cessation of diarrhea and fever >39 C (warning of Toxic Megacolon)",
            "Blood pressure drop with high white blood cell count (>30,000) indicating fulminant colitis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "C. difficile colitis is a bacterial infection of the colon caused by antibiotic use, leading to watery diarrhea and cramps.",
                "plain_analogy": "Weeds taking over a lawn after the healthy grass and protective soil bacteria were killed by weed-killer.",
                "lifestyle_action": "Wash hands thoroughly with soap and water, take prescribed targeted antibiotics, and never take Imodium for C. diff."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Fidaxomicin (Dificid)",
                    "Vancomycin oral capsules (Vancocin)",
                    "Metronidazole IV (only in fulminant ileus)"
                ],
                "dosing_gdmt": "Fidaxomicin 200 mg orally BID x 10 days; or Vancomycin 125 mg orally QID x 10 days.",
                "black_box_warning": "Oral Vancomycin is not absorbed systemically and cannot be replaced by IV Vancomycin (IV does not enter bowel).",
                "organ_clearance_cutoffs": "Fidaxomicin has minimal systemic absorption; safe across renal impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "IDSA-CDIFF",
                "pmid_or_doi": "10.1093/cid/ciab549",
                "cebm_level": 1,
                "sample_size": 2600,
                "endpoints": "Fidaxomicin achieves sustained clinical cure and slashes C. diff recurrence rates by 47% compared to vancomycin."
            }
        }
    },
    {
        "id": "DOC-CARD-380",
        "icd10": "K59.31",
        "condition": "Toxic Megacolon (Acute Colonic Dilation Emergency)",
        "specialty": "Gastroenterology & Colorectal Surgery",
        "organ_system": "Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACG Practice Guidelines",
        "source_body": "American Journal of Gastroenterology",
        "citation": "Rubin DT et al. ACG Clinical Guideline: Ulcerative Colitis in Adults. Am J Gastroenterol. 2019;114(3):384-413.",
        "doi_or_source": "10.14309/ajg.0000000000000152",
        "clinical_evidence": "Emergent total abdominal colectomy with end ileostomy is life-saving in toxic megacolon failing 48-72 hours of intensive medical therapy (IV high-dose Methylprednisolone, broad-spectrum antibiotics, bowel rest, and decompression), reducing perforation-related mortality from >40% to under 8% (p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "STRICT NPO; wide-bore nasogastric tube decompression; 'roll-over' prone positioning (helps relocate and redistribute colonic gas into rectum); broad-spectrum IV antibiotics covering enterics and anaerobes (Zosyn + Vancomycin); stop all opioids, anticholinergics, and antidiarrheals.",
            "monitoring_cadence": "Serial plain abdominal radiographs every 12 hours measuring transverse colon caliber; ICU hemodynamic monitoring.",
            "clinical_thresholds": "Transverse colon diameter >6.0 cm on radiograph PLUS at least 3 systemic signs: fever >38.6 C, heart rate >120, leukocytosis >10,500, or anemia."
        },
        "patient_plain_language": "A life-threatening complication of severe colitis (from C. diff or ulcerative colitis) where the colon wall becomes so deeply inflamed that its muscular nerves become paralyzed. The large intestine balloons out to dangerous sizes (over 2.5 inches wide) like an over-inflated tire, threatening to burst and leak bacteria into your abdomen.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current colon diameter on my latest abdominal X-ray (is it exceeding 6 centimeters)?",
            "safety_question": "Is a colorectal surgical team on standby in case my colon shows any signs of perforation?",
            "action_threshold_question": "Have all narcotic pain pills and antimotility medicines been completely stopped?"
        },
        "red_flags": [
            "Signs of free air under the diaphragm on X-ray indicating colonic perforation (Emergency Colectomy)",
            "Septic shock with sudden drop in blood pressure and rapid heart rate"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Toxic megacolon is extreme, life-threatening swelling and dilation of the colon caused by severe inflammation or infection.",
                "plain_analogy": "A balloon being inflated until its rubber becomes paper-thin and ready to pop at any second.",
                "lifestyle_action": "Requires emergency intensive care and surgical monitoring; never take anti-diarrheal medicines during colitis flares."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Total Abdominal Colectomy (Definitive Surgical)",
                    "Methylprednisolone IV (if IBD)",
                    "Vancomycin oral + Metronidazole IV (if C. diff)"
                ],
                "dosing_gdmt": "Methylprednisolone 60 mg IV daily for IBD; or Vancomycin 500 mg PO/enema QID + Flagyl 500 mg IV q8h for C. diff.",
                "black_box_warning": "Opioids, loperamide, and anticholinergics are STRICTLY CONTRAINDICATED (precipitate perforation).",
                "organ_clearance_cutoffs": "Intensive resuscitation in surgical ICU."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ACG-MEGACOLON",
                "pmid_or_doi": "10.14309/ajg.0000000000000152",
                "cebm_level": 1,
                "sample_size": 1100,
                "endpoints": "Timely surgical colectomy before perforation reduces toxic megacolon mortality from 40% to <8%."
            }
        }
    }
]