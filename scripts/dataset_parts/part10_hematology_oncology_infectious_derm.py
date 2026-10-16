"""
part10_hematology_oncology_infectious_derm.py
"""

PART_10_DISEASES = [
    {
        "id": "DOC-CARD-281",
        "icd10": "D69.3",
        "condition": "Immune Thrombocytopenia (ITP)",
        "specialty": "Hematology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "The Lancet (RAISE Trial) & ASH Guidelines",
        "citation": "Cheng G et al. Eltrombopag for management of chronic immune thrombocytopenia (RAISE): a 6-month, randomised, phase 3 study. Lancet. 2011;377(9763):393-402.",
        "doi_or_source": "10.1016/S0140-6736(10)60959-2",
        "clinical_evidence": "Primary Immune Thrombocytopenia (ITP) is an acquired autoimmune disorder characterized by isolated thrombocytopenia (platelet count <100,000/mcL) resulting from antibody-mediated platelet destruction and impaired megakaryocyte thrombopoiesis. In the landmark multicenter double-blind Phase 3 RAISE trial (n=197 patients with chronic refractory ITP), the oral thrombopoietin receptor agonist (TPO-RA) eltrombopag (50-75 mg daily) maintained target platelet counts between 50,000 and 400,000/mcL in 79% of patients vs 28% placebo (odds ratio 8.2; 95% CI 3.6-18.7; p<0.0001). Eltrombopag reduced clinically significant bleeding by 76% (HR 0.24; p=0.0002) and allowed 59% of patients to discontinue or reduce concomitant steroids. ASH guidelines recommend first-line corticosteroids (dexamethasone 40 mg daily for 4 days or prednisone 1 mg/kg/day) or IVIG for platelet counts <20,000-30,000/mcL with bleeding.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoidance of contact sports and high-risk traumatic activities; discontinuation of antiplatelet agents (aspirin, clopidogrel) and NSAIDs; using soft-bristled toothbrushes and electric razors; taking eltrombopag on an empty stomach >=2 hours before or 4 hours after calcium-rich dairy foods.",
            "monitoring_cadence": "Complete blood count with platelet count and peripheral blood smear weekly during dose titration, then monthly; serum ALT, AST, and bilirubin monthly (eltrombopag hepatotoxicity monitoring).",
            "clinical_thresholds": "Platelet count <20,000-30,000/mcL with mucosal bleeding (epistaxis, wet purpura in mouth, hematuria) requires immediate first-line rescue therapy (IVIG 1 g/kg single dose or Dexamethasone 40 mg daily for 4 days)."
        },
        "patient_plain_language": "Immune thrombocytopenia (ITP) is an autoimmune blood condition where your immune system mistakenly destroys your body's platelets (tiny cell fragments that stick together to form blood clots and stop bleeding). Because your platelet count drops far below normal, you bruise easily, develop clusters of tiny red or purple pinpoint spots under your skin (petechiae), and experience frequent nosebleeds or heavy gums.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current platelet count, and has my peripheral blood smear confirmed that the low count is genuine and not platelet clumping?",
            "safety_question": "What are the food timing rules for eltrombopag (avoiding milk, antacids, or iron within 4 hours) so the pill absorbs properly?",
            "action_threshold_question": "At what specific platelet number (such as below 30,000) or bleeding symptom should I go to the emergency room for an IVIG infusion?"
        },
        "red_flags": [
            "Spontaneous bleeding inside your mouth or gums (wet purpura), black tarry bowel movements, severe sudden headache (suspect Intracranial Hemorrhage), or persistent bleeding from cuts"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Immune thrombocytopenia is a disorder that can lead to easy or excessive bruising and bleeding from unusually low levels of platelets.",
                "plain_analogy": "Your body's immune police mistakenly arresting its own blood-clotting repair workers (platelets), leaving punctures unsealed.",
                "lifestyle_action": "Avoid collision sports. Use soft toothbrushes. Never take ibuprofen or aspirin. Take eltrombopag away from dairy."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Eltrombopag (Promacta)", "Romiplostim (Nplate)", "Avatrombopag (Doptelet)", "Dexamethasone", "Intravenous Immune Globulin (IVIG)"],
                "dosing_gdmt": "Eltrombopag 50 mg orally daily on empty stomach (25 mg in East Asian ancestry), titrated to keep platelets >=50,000/mcL. Dexamethasone 40 mg daily x 4 days.",
                "black_box_warning": "Eltrombopag: Severe hepatotoxicity and potential hepatic decompensation in chronic hepatitis C; monitor liver enzymes regularly.",
                "organ_clearance_cutoffs": "Do not adjust dose to normalize platelet counts (>400,000/mcL); aim for safe hemostatic target of 50,000-100,000/mcL to prevent thrombosis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "RAISE Trial",
                "pmid_or_doi": "10.1016/S0140-6736(10)60959-2",
                "cebm_level": 2,
                "sample_size": 197,
                "endpoints": "Target platelet count maintained in 79% with eltrombopag vs 28% placebo (p<0.0001); clinically significant bleeding events reduced by 76%."
            }
        }
    },
    {
        "id": "DOC-CARD-282",
        "icd10": "M31.1",
        "condition": "Thrombotic Thrombocytopenic Purpura (TTP)",
        "specialty": "Hematology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (HERCULES Trial) & ISTH Guidelines",
        "citation": "Scully M et al. Caplacizumab Treatment for Acquired Thrombotic Thrombocytopenic Purpura (HERCULES). N Engl J Med. 2019;380(4):335-346.",
        "doi_or_source": "10.1056/NEJMoa1806311",
        "clinical_evidence": "Immune Thrombotic Thrombocytopenic Purpura (iTTP) is a life-threatening hematologic emergency characterized by microangiopathic hemolytic anemia (MAHA with abundant schistocytes on blood smear) and severe consumptive thrombocytopenia, driven by acquired autoantibodies neutralizing the von Willebrand factor-cleaving protease ADAMTS13 (activity <10%). Ultra-large vWF multimers spontaneously bind platelets, producing widespread microvascular thrombi that cause organ ischemia (brain, heart, kidneys). In the landmark Phase 3 HERCULES trial (n=145 patients), the anti-vWF nanobody caplacizumab (10 mg daily) added to plasma exchange (PEX) and immunosuppression significantly accelerated time to platelet count normalization (rate ratio 1.55; p=0.01) and reduced the composite endpoint of TTP-related death, recurrence, or major thromboembolic event by 74% (12.7% vs 49.3%; p<0.001) while eliminating refractory disease (0% vs 4.2%). Mortality without immediate PEX exceeds 90%, dropping to <10-15% with modern triple therapy (PEX + caplacizumab + rituximab/corticosteroids).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate emergency initiation of therapeutic plasma exchange (PEX 1.0-1.5 plasma volumes daily with fresh frozen plasma replacement); platelet transfusions are strictly contraindicated (feed the microthrombotic fire and precipitate fatal cardiac/cerebral infarction).",
            "monitoring_cadence": "CBC with platelet count, LDH, and peripheral smear for schistocytes twice daily until platelet normalization; ADAMTS13 activity and inhibitor titer at baseline, end of PEX, and quarterly (monitoring for subclinical relapses).",
            "clinical_thresholds": "PLASMIC score >=6 (high probability of severe ADAMTS13 deficiency) or presence of MAHA with thrombocytopenia mandates immediate emergent plasma exchange and caplacizumab without waiting for ADAMTS13 laboratory turnaround."
        },
        "patient_plain_language": "Thrombotic thrombocytopenic purpura (TTP) is a critical, life-threatening blood emergency where your immune system knocks out an enzyme called ADAMTS13. Without this molecular scissor to trim down long sticky protein ropes in your blood, tiny blood clots form in small vessels all throughout your body. These clots block blood flow to your brain and kidneys while chewing up and destroying red blood cells (hemolytic anemia) and using up all your platelets.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my calculated PLASMIC score and my measured ADAMTS13 enzyme activity percentage?",
            "safety_question": "Have we started emergency daily plasma exchange (plasmapheresis) and caplacizumab immediately?",
            "action_threshold_question": "Is my medical chart clearly marked that platelet transfusions are strictly forbidden?"
        },
        "red_flags": [
            "Sudden confusion, speech difficulty, seizures, weakness (cerebral ischemia), dark cola-colored urine, extreme shortness of breath, or bleeding from gums"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Thrombotic thrombocytopenic purpura is a rare blood disorder that causes blood clots to form in small blood vessels throughout the body, leading to low platelets and red cell destruction.",
                "plain_analogy": "Missing molecular scissors that trim blood clotting ropes, so tangled sticky nets trap and shred red blood cells like a blender.",
                "lifestyle_action": "Emergency ICU admission immediately. Platelet transfusions are forbidden. Daily plasma cleaning cleanses the blood."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Caplacizumab-yhdp (Cablivi)", "Therapeutic Plasma Exchange (PEX)", "Rituximab", "Methylprednisolone IV"],
                "dosing_gdmt": "Caplacizumab: 11 mg IV prior to first PEX, then 11 mg SC daily after each PEX and for 30 days post-PEX. Methylprednisolone 1 g IV daily x 3 days + Rituximab 375 mg/m2 weekly x 4.",
                "black_box_warning": "Caplacizumab: Increased risk of bleeding events; withhold if clinically significant active bleeding occurs.",
                "organ_clearance_cutoffs": "Never administer platelet transfusions in TTP unless life-threatening catastrophic hemorrhage is present."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "HERCULES Trial",
                "pmid_or_doi": "10.1056/NEJMoa1806311",
                "cebm_level": 2,
                "sample_size": 145,
                "endpoints": "TTP-related death, recurrence, or major thromboembolic event reduced by 74% with caplacizumab (12.7% vs 49.3%; p<0.001); refractoriness eliminated."
            }
        }
    },
    {
        "id": "DOC-CARD-283",
        "icd10": "D59.3",
        "condition": "Atypical Hemolytic Uremic Syndrome (aHUS)",
        "specialty": "Hematology & Nephrology",
        "organ_system": "Renal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Multicenter Prospective Clinical Trial & Guideline",
        "source_body": "NEJM (Eculizumab in aHUS) & KDIGO Guidelines",
        "citation": "Legendre CM et al. Terminal complement inhibitor eculizumab in atypical hemolytic-uremic syndrome. N Engl J Med. 2013;368(23):2169-2181.",
        "doi_or_source": "10.1056/NEJMoa1208981",
        "clinical_evidence": "Atypical Hemolytic Uremic Syndrome (aHUS) is a genetic, life-threatening thrombotic microangiopathy (TMA) driven by uncontrolled chronic dysregulation of the alternative complement pathway (mutations in CFH, CFI, MCP/CD46, C3, or CFB, or autoantibodies against complement factor H). Unchecked activation of the terminal complement cascade leads to continuous endothelial cell damage, platelet consumption, and microvascular thrombosis, with profound predilection for the renal microvasculature. In prospective multicenter Phase 2/3 trials (n=67 patients), the humanized monoclonal anti-C5 antibody eculizumab produced a rapid, sustained hematologic normalization (platelets and LDH normal in 88%) and achieved a dramatic, durable improvement in renal function (eGFR increased by >=15 mL/min in 80%; 80% of dialysis-dependent patients discontinued dialysis permanently). Long-acting C5 inhibition (ravulizumab every 8 weeks) achieves equivalent complement suppression with reduced infusion frequency.",
        "solution_protocol": {
            "non_pharmacological_targets": "Emergent diagnostic differentiation from TTP (normal ADAMTS13 activity >10%) and STEC-HUS (negative Shiga-toxin PCR and stool culture); mandatory meningococcal vaccination (MenACWY and MenB) plus prophylactic antibiotics (ciprofloxacin/penicillin) for 2 weeks.",
            "monitoring_cadence": "CBC with platelet count, LDH, haptoglobin, and peripheral smear for schistocytes daily until TMA resolution; serum creatinine and eGFR weekly; terminal complement blockade monitoring (CH50 or sC5b-9).",
            "clinical_thresholds": "Microangiopathic hemolytic anemia with acute kidney injury and normal ADAMTS13 (>10%) warrants immediate initiation of terminal complement C5 inhibition (Eculizumab or Ravulizumab) within 24-48 hours to rescue renal parenchyma."
        },
        "patient_plain_language": "Atypical hemolytic uremic syndrome (aHUS) is a rare, severe blood and kidney disorder caused by a genetic malfunction in your immune system's 'complement' defense system. The complement system is like a chemical alarm system that attacks bacteria. In aHUS, the off-switch is broken, so the system stays stuck in the 'attack' mode, destroying healthy blood cells and creating tiny blood clots that rapidly shut down your kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my ADAMTS13 level tested (>10%) to confirm that my condition is aHUS and not TTP, and was stool Shiga-toxin negative?",
            "safety_question": "Have I received both meningococcal vaccines (MenACWY and MenB) and temporary protective antibiotics before starting complement-blocker infusions?",
            "action_threshold_question": "How quickly can we start eculizumab (Soliris) or ravulizumab (Ultomiris) to reverse my kidney damage and get off dialysis?"
        },
        "red_flags": [
            "Sudden severe drop in urine volume, blood pressure spiking dangerously, breathlessness, confusion, or dark brown urine with extreme pale fatigue"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Atypical hemolytic uremic syndrome is an extremely rare, genetic, life-threatening disease that causes abnormal blood clots in small blood vessels throughout the body, especially in the kidneys.",
                "plain_analogy": "An immune alarm system with a broken off-switch that bombards your own kidney blood vessels with chemical attacks.",
                "lifestyle_action": "Emergency hospital admission. Receive meningococcal immunizations. Never miss scheduled complement antibody infusions."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Eculizumab (Soliris)", "Ravulizumab (Ultomiris)", "Pegcetacoplan", "Penicillin VK (Meningococcal Prophylaxis)"],
                "dosing_gdmt": "Eculizumab: 900 mg IV weekly for 4 weeks, then 1,200 mg at week 5, then 1,200 mg every 2 weeks. Or Ravulizumab weight-based IV every 8 weeks.",
                "black_box_warning": "Terminal Complement Inhibitors: Life-threatening and fatal meningococcal infections (up to 2,000-fold risk); mandatory vaccination and alert card.",
                "organ_clearance_cutoffs": "Plasma exchange has poor long-term efficacy (<50%); C5 complement blockade is the primary disease-modifying standard."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "Eculizumab aHUS Trials",
                "pmid_or_doi": "10.1056/NEJMoa1208981",
                "cebm_level": 1,
                "sample_size": 67,
                "endpoints": "Hematologic normalization in 88%; eGFR improved by >=15 mL/min in 80%; 80% of dialysis-dependent patients successfully weaned off dialysis."
            }
        }
    },
    {
        "id": "DOC-CARD-284",
        "icd10": "D45",
        "condition": "Polycythemia Vera",
        "specialty": "Hematology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (CYTO-PV Trial & RESPONSE Trial) & WHO/NCCN",
        "citation": "Marchioli R et al. Cardiovascular events and intensity of treatment in polycythemia vera (CYTO-PV). N Engl J Med. 2013;368(1):22-33.",
        "doi_or_source": "10.1056/NEJMoa1208500",
        "clinical_evidence": "Polycythemia Vera (PV) is a chronic myeloproliferative neoplasm driven in >95-98% by a gain-of-function somatic mutation in JAK2 (V617F in exon 14, or exon 12 mutations), resulting in autonomous trilineage bone marrow proliferation, marked erythrocytosis, and hyperviscosity. The WHO diagnostic criteria require: elevated hemoglobin (>16.5 g/dL in men, >16.0 g/dL in women) or hematocrit (>49% in men, >48% in women); hypercellular bone marrow with trilineage hyperplasia (panmyelosis); and presence of JAK2 mutation. In the landmark multicenter randomized Phase 3 CYTO-PV trial (n=365 patients), maintaining a strict hematocrit target <45% via therapeutic phlebotomy and cytoreduction significantly reduced the primary composite outcome of cardiovascular death or major thrombosis by 73% compared with a hematocrit target of 45-50% (hazard ratio 0.27; 95% CI 0.11-0.66; p=0.007). In hydroxyurea-resistant patients, the JAK1/2 inhibitor ruxolitinib achieved hematocrit control without phlebotomy in 60% vs 20% control (RESPONSE trial, p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Therapeutic phlebotomy (removal of 250-500 mL blood) to maintain hematocrit strictly <45.0% in both men and women; low-dose aspirin (81-100 mg daily) to reduce thrombotic risk; avoiding hot showers to prevent aquagenic pruritus.",
            "monitoring_cadence": "Complete blood count with differential and hematocrit every 2-4 weeks during phlebotomy induction, then monthly once stable; palpation of spleen for splenomegaly; annual bone marrow examination if blast transformation suspected.",
            "clinical_thresholds": "High-risk PV (age >=60 years or history of prior venous/arterial thrombosis) warrants immediate cytoreductive therapy (Hydroxyurea 500-1500 mg daily or pegylated Interferon-alfa)."
        },
        "patient_plain_language": "Polycythemia vera is a rare, slow-growing blood cancer where your bone marrow produces far too many red blood cells. The extra red blood cells thicken your blood like sludge, slowing down circulation and making it much more likely for dangerous blood clots to form in your brain, heart, or legs. Classic symptoms include a reddish or purplish face, burning pain in hands and feet, and intense, stinging skin itching immediately after a warm bath or shower (aquagenic pruritus).",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current hematocrit percentage, and is it strictly below the life-saving target of 45%?",
            "safety_question": "Do I have the JAK2 V617F genetic mutation, and am I taking low-dose daily aspirin to protect against blood clots?",
            "action_threshold_question": "Am I considered high-risk (over age 60 or history of blood clots) requiring daily hydroxyurea or interferon pills?"
        },
        "red_flags": [
            "Sudden severe pain, swelling, and redness in a calf (DVT), sudden shortness of breath, sudden facial droop or arm weakness (stroke), or severe burning pain in fingers/toes"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Polycythemia vera is a slow-growing blood cancer in which your bone marrow makes too many red blood cells, thickening your blood.",
                "plain_analogy": "The bone marrow factory overproducing red blood cells until the blood turns thick like molasses, straining the heart and clogging vessels.",
                "lifestyle_action": "Never let hematocrit rise above 45%. Take lukewarm showers to prevent itching. Walk daily to keep blood circulating."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Hydroxyurea (Hydrea)", "Ruxolitinib (Jakafi)", "Ropeginterferon alfa-2b (Besremi)", "Aspirin 81 mg"],
                "dosing_gdmt": "Hematocrit target <45%. Hydroxyurea 500-1000 mg daily PO. In hydroxyurea-resistant patients: Ruxolitinib 10 mg PO BID.",
                "black_box_warning": "Hydroxyurea: Severe myelosuppression (neutropenia/thrombocytopenia) and secondary leukemia; monitor CBC weekly during titration.",
                "organ_clearance_cutoffs": "Reduce ruxolitinib dose if baseline platelet count is <200,000/mcL or if moderate renal impairment is present."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CYTO-PV Trial",
                "pmid_or_doi": "10.1056/NEJMoa1208500",
                "cebm_level": 2,
                "sample_size": 365,
                "endpoints": "Maintaining hematocrit <45% reduces cardiovascular death and major thrombosis by 73% (HR 0.27; p=0.007); NNT to prevent 1 major thrombotic event = 12."
            }
        }
    },
    {
        "id": "DOC-CARD-285",
        "icd10": "D47.3",
        "condition": "Essential Thrombocythemia (ET)",
        "specialty": "Hematology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (PT1 Trial) & WHO/NCCN Guidelines",
        "citation": "Harrison CN et al. Hydroxyurea compared with anagrelide in high-risk essential thrombocythemia (PT1). N Engl J Med. 2005;353(1):33-45.",
        "doi_or_source": "10.1056/NEJMoa043800",
        "clinical_evidence": "Essential Thrombocythemia (ET) is a chronic myeloproliferative neoplasm characterized by sustained megakaryocytic proliferation, thrombocytosis (platelets >=450,000/mcL), and an elevated risk of arterial/venous thrombosis and hemorrhagic complications (due to acquired von Willebrand syndrome at platelet counts >1,000,000/mcL). Mutational driver landscape comprises JAK2 V617F (55-60%), calreticulin (CALR exon 9 indels, 25-30%, associated with lower thrombosis risk and higher platelet counts), and MPL W515 (3-5%). In the landmark multicenter randomized PT1 trial (n=809 high-risk ET patients), hydroxyurea plus low-dose aspirin was significantly superior to anagrelide plus aspirin in preventing arterial thrombosis (odds ratio 0.43; p=0.004), major hemorrhage (OR 0.39; p=0.003), and myelofibrotic transformation (OR 0.36; p=0.01), establishing hydroxyurea as the first-line cytoreductive standard.",
        "solution_protocol": {
            "non_pharmacological_targets": "Low-dose aspirin (81-100 mg daily) to suppress platelet thromboxane A2; absolute smoking cessation; aggressive cardiovascular risk reduction (BP <130/80 mmHg, LDL-C <70 mg/dL); staying well hydrated.",
            "monitoring_cadence": "Complete blood count with differential and platelet count every 4-8 weeks once stable; screening for microvascular symptoms (erythromelalgia: burning erythema in soles/palms); bone marrow biopsy at diagnosis.",
            "clinical_thresholds": "High-risk ET (age >=60 years or prior thrombotic history) warrants cytoreductive therapy targeting platelets <400,000/mcL; extreme thrombocytosis (>1,000,000-1,500,000/mcL) requires screening for acquired von Willebrand syndrome (hold aspirin if ristocetin cofactor <30% to prevent fatal bleeding)."
        },
        "patient_plain_language": "Essential thrombocythemia (ET) is a rare blood disorder where your bone marrow produces too many platelets. Platelets are the cell fragments responsible for forming blood clots. Having too many platelets can cause them to clump together and block blood vessels, causing blood clots in your brain, heart, or legs. Paradoxically, if platelet counts climb extremely high (over one million), they can consume clotting proteins and cause unusual bleeding.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current platelet count, and which driver mutation (JAK2, CALR, or MPL) was identified on my genetic blood test?",
            "safety_question": "Is my platelet count high enough (over 1 million) that daily aspirin could cause bleeding instead of protecting me?",
            "action_threshold_question": "Am I classified as high-risk (over age 60 or prior clot) requiring daily hydroxyurea to keep my platelets under 400,000?"
        },
        "red_flags": [
            "Painful burning, redness, and throbbing warmth in your palms or soles (erythromelalgia), sudden vision blackouts in one eye (amaurosis fugax), or sudden chest pain"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Essential thrombocythemia is a rare disorder in which your body produces too many blood platelets, which can cause blood clots or bleeding.",
                "plain_analogy": "The bone marrow assembly line running on hyper-speed, churning out mountains of platelets that risk forming highway traffic jams in your arteries.",
                "lifestyle_action": "Take your baby aspirin daily with food. Stay hydrated during air travel. Exercise regularly to keep blood flowing smoothly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Hydroxyurea (Hydrea)", "Anagrelide (Agrylin)", "Pegylated Interferon alfa-2a", "Aspirin 81 mg"],
                "dosing_gdmt": "Hydroxyurea 500-1000 mg orally daily, titrated to keep platelet count between 150,000 and 400,000/mcL PLUS Aspirin 81 mg daily.",
                "black_box_warning": "Hydroxyurea: Severe bone marrow depression; monitor CBC and white blood cell count closely.",
                "organ_clearance_cutoffs": "In women of childbearing potential or pregnancy, pegylated interferon is the non-teratogenic cytoreductive agent of choice."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PT1 Trial",
                "pmid_or_doi": "10.1056/NEJMoa043800",
                "cebm_level": 2,
                "sample_size": 809,
                "endpoints": "Hydroxyurea plus aspirin significantly superior to anagrelide: arterial thrombosis reduced by 57% (p=0.004); major hemorrhage reduced by 61% (p=0.003)."
            }
        }
    },
    {
        "id": "DOC-CARD-286",
        "icd10": "D46.9",
        "condition": "Myelodysplastic Syndromes (MDS)",
        "specialty": "Hematology & Oncology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM & The Lancet (COMMANDS Trial & AZA-001)",
        "citation": "Platzbecker U et al. Luspatercept versus epoetin alfa in erythropoiesis-stimulating agent-naive, transfusion-dependent lower-risk myelodysplastic syndromes (COMMANDS). Lancet. 2023;402(10399):373-385.",
        "doi_or_source": "10.1016/S0140-6736(23)00874-7",
        "clinical_evidence": "Myelodysplastic Syndromes (MDS) are a heterogeneous group of clonal hematopoietic stem cell neoplasms characterized by ineffective hematopoiesis, peripheral blood cytopenias (refractory anemia in >85%), prominent morphological dysplasia in bone marrow lineages, and a propensity for transformation into acute myeloid leukemia (AML). Prognosis is established via the Revised International Prognostic Scoring System (IPSS-R) based on marrow blast percentage, cytogenetics, and cytopenia depth. In the landmark open-label Phase 3 COMMANDS trial (n=356 patients with transfusion-dependent lower-risk MDS), the erythroid maturation agent luspatercept (1.0-1.75 mg/kg subcutaneous every 3 weeks) was significantly superior to epoetin alfa in achieving red blood cell transfusion independence for >=12 weeks with concurrent hemoglobin increase >=1.5 g/dL (58.5% vs 31.2%; p<0.0001). In higher-risk MDS (IPSS-R >3.5), the hypomethylating agent azacitidine (75 mg/m2/day for 7 days every 28 days) prolongs median overall survival compared with conventional care (24.5 vs 15.0 months; hazard ratio 0.58; p=0.0001; AZA-001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Neutropenic infection precautions (rigorous hand hygiene, thorough cooking of meats/vegetables, prompt fever reporting); red blood cell and platelet transfusion support with irradiated, leukoreduced products; iron chelation therapy for secondary hemosiderosis in chronically transfused patients.",
            "monitoring_cadence": "Complete blood count with differential weekly to monthly; bone marrow aspiration and biopsy with cytogenetics/FISH and next-generation sequencing (NGS for SF3B1, TP53, ASXL1 mutations) at baseline and if progressive cytopenias develop.",
            "clinical_thresholds": "MDS with isolated 5q deletion (del[5q]) responds exquisitely to oral lenalidomide (transfusion independence in >65%); higher-risk MDS in medically fit patients aged <=70 warrants immediate allogeneic hematopoietic stem cell transplantation evaluation (the only curative modality)."
        },
        "patient_plain_language": "Myelodysplastic syndromes (MDS) are a group of bone marrow disorders sometimes described as 'bone marrow failure'. Your bone marrow produces defective, immature blood cells that die prematurely inside the marrow instead of maturing into healthy red cells, white cells, and platelets. This causes chronic severe fatigue from anemia, frequent infections due to low white blood cells, and easy bruising. Some forms can progress into acute leukemia.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my revised IPSS-R risk score (Very Low, Low, Intermediate, High, or Very High) and my bone marrow blast percentage?",
            "safety_question": "Do I have the ring sideroblast mutation (SF3B1) or a 5q-deletion that qualifies me for targeted therapies like luspatercept (Reblozyl) or lenalidomide?",
            "action_threshold_question": "Am I a candidate for a curative bone marrow stem cell transplant from an HLA-matched donor?"
        },
        "red_flags": [
            "Fever >38.0°C (100.4°F) while white blood cells are low (Neutropenic Fever emergency), spontaneous heavy bleeding, or profound shortness of breath at rest"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Myelodysplastic syndromes are a group of cancers in which immature blood cells in the bone marrow do not mature or become healthy blood cells.",
                "plain_analogy": "A bone marrow manufacturing plant making defective, flawed blood cells that fail quality inspection and get destroyed before entering circulation.",
                "lifestyle_action": "Avoid raw or undercooked foods. Wash hands constantly. Report any fever immediately to the oncology team."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Luspatercept (Reblozyl)", "Azacitidine (Vidaza)", "Decitabine", "Lenalidomide (Revlimid)", "Epoetin Alfa"],
                "dosing_gdmt": "Lower-risk MDS with anemia: Luspatercept 1.0 mg/kg SC every 3 weeks (titrated to 1.75 mg/kg). Higher-risk: Azacitidine 75 mg/m2/day SC/IV for 7 days q28d.",
                "black_box_warning": "Lenalidomide: Severe embryo-fetal toxicity, deep vein thrombosis, and pulmonary embolism; mandatory Lenalidomide REMS program.",
                "organ_clearance_cutoffs": "Monitor CBC prior to each azacitidine cycle; allogeneic stem cell transplant is the only definitive curative intervention."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "COMMANDS / AZA-001",
                "pmid_or_doi": "10.1016/S0140-6736(23)00874-7",
                "cebm_level": 2,
                "sample_size": 356,
                "endpoints": "Transfusion independence >=12 weeks achieved in 58.5% with luspatercept vs 31.2% epoetin alfa (p<0.0001); Azacitidine extends survival by 9.5 months in higher-risk MDS."
            }
        }
    },
    {
        "id": "DOC-CARD-287",
        "icd10": "C91.10",
        "condition": "Chronic Lymphocytic Leukemia (CLL)",
        "specialty": "Hematology & Oncology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (ELEVATE-TN & CLL14 Trials) & NCCN Guidelines",
        "citation": "Sharman JP et al. Acalabrutinib with or without obinutuzumab versus chlorambucil and obinutuzumab for treatment-naive chronic lymphocytic leukaemia (ELEVATE-TN). Lancet. 2020;395(10232):1278-1291.",
        "doi_or_source": "10.1016/S0140-6736(20)30262-2",
        "clinical_evidence": "Chronic Lymphocytic Leukemia (CLL) and Small Lymphocytic Lymphoma (SLL) are mature B-cell clonal lymphoproliferative neoplasms characterized by absolute monoclonal B-lymphocytosis (>=5,000/mcL for >=3 months) co-expressing CD5, CD19, CD20 (dim), and CD23, with surface immunoglobulin light chain restriction. High-risk genomic markers include TP53 deletion (del[17p]) or mutation, and unmutated IGHV status. In the landmark Phase 3 ELEVATE-TN trial (n=535 treatment-naive CLL patients), continuous monotherapy with the second-generation selective Bruton tyrosine kinase (BTK) inhibitor acalabrutinib (100 mg BID) significantly prolonged progression-free survival (PFS) compared with chemoimmunotherapy (24-month PFS 87% vs 47%; hazard ratio 0.20; 95% CI 0.13-0.30; p<0.0001). Fixed-duration targeted therapy with venetoclax (a BCL-2 inhibitor) plus obinutuzumab for 12 months (CLL14 trial) achieves high rates of undetectable minimal residual disease (uMRD <10^-4 in 76%) and durable 5-year progression-free survival without continuous therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Watchful waiting ('active surveillance') for asymptomatic early-stage disease (Rai 0 / Binet A; early treatment provides zero survival benefit); annual non-live influenza, pneumococcal (PCV20), and recombinant zoster (Shingrix) immunizations (avoid live vaccines); rigorous skin cancer surveillance (CLL carries an 8-fold elevated risk of aggressive cutaneous malignancies).",
            "monitoring_cadence": "Complete blood count with differential and physical examination of lymph nodes, liver, and spleen every 3-6 months; flow cytometry and FISH for del(17p)/TP53 mutation prior to initiating each line of systemic therapy.",
            "clinical_thresholds": "International Workshop on CLL (iwCLL) active disease criteria (progressive marrow failure with worsening anemia/thrombocytopenia, massive progressive splenomegaly, lymphocyte doubling time <6 months, or constitutional B-symptoms) warrants initiating targeted therapy."
        },
        "patient_plain_language": "Chronic lymphocytic leukemia (CLL) is a slow-growing cancer of the white blood cells (lymphocytes). The bone marrow produces abnormal, long-lived B-cells that do not fight infections properly and slowly crowd out normal blood cells. Many people with CLL have zero symptoms for years and do not need immediate treatment—a standard, safe medical approach called 'active surveillance' or watchful waiting.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Rai or Binet clinical stage and what did my genetic FISH test show regarding chromosome 17p deletion or IGHV mutation status?",
            "safety_question": "Am I a candidate for 'watch-and-wait' monitoring, and why does starting chemotherapy too early offer no survival benefit?",
            "action_threshold_question": "If treatment is needed, would a targeted BTK inhibitor pill (like acalabrutinib or zanubrutinib) or a 1-year course of venetoclax be preferred?"
        },
        "red_flags": [
            "Rapid painful enlargement of a single lymph node group with high fevers and weight loss (suspect Richter Transformation into aggressive diffuse large B-cell lymphoma)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Chronic lymphocytic leukemia is a type of cancer of the blood and bone marrow that progresses slowly over many years.",
                "plain_analogy": "Long-lived white blood cells that refuse to die on schedule, slowly piling up in the bloodstream and lymph nodes like cars in a parking lot.",
                "lifestyle_action": "Get non-live vaccines annually. See a dermatologist every year for skin cancer checks. Report rapid lymph node swelling."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Acalabrutinib (Calquence)", "Zanubrutinib (Brukinsa)", "Venetoclax (Venclexta)", "Obinutuzumab (Gazyva)", "Ibrutinib"],
                "dosing_gdmt": "Acalabrutinib 100 mg orally BID continuously. Or Venetoclax 5-week ramp-up (20 to 400 mg daily) + Obinutuzumab for 12 cycles.",
                "black_box_warning": "Venetoclax: Tumor Lysis Syndrome (TLS); requires strict 5-week dose ramp-up, oral hydration, and allopurinol prophylaxis.",
                "organ_clearance_cutoffs": "BTK inhibitors: Monitor for atrial fibrillation, bleeding, and hypertension; hold 3-7 days prior to major surgical procedures."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ELEVATE-TN / CLL14",
                "pmid_or_doi": "10.1016/S0140-6736(20)30262-2",
                "cebm_level": 2,
                "sample_size": 535,
                "endpoints": "Progression-free survival significantly superior with acalabrutinib (HR 0.20; p<0.0001); CLL14 fixed-duration venetoclax achieves 76% undetectable MRD."
            }
        }
    },
    {
        "id": "DOC-CARD-288",
        "icd10": "C90.00",
        "condition": "Multiple Myeloma",
        "specialty": "Hematology & Oncology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (GRIFFIN & MAIA Trials) & IMWG Guidelines",
        "citation": "Facon T et al. Daratumumab plus Lenalidomide and Dexamethasone for Untreated Multiple Myeloma (MAIA). N Engl J Med. 2019;380(21):1989-1999.",
        "doi_or_source": "10.1056/NEJMoa1817249",
        "clinical_evidence": "Multiple Myeloma is a clonal plasma cell malignancy characterized by the neoplastic proliferation of plasma cells in the bone marrow (>10% clonal marrow plasma cells or biopsy-proven plasmacytoma) producing a monoclonal immunoglobulin (M-protein). End-organ damage is defined by the CRAB criteria: Hypercalcemia (serum calcium >11 mg/dL), Renal insufficiency (serum Cr >2 mg/dL or eGFR <40 mL/min), Anemia (hemoglobin <10 g/dL), and Bone lesions (one or more osteolytic lesions on whole-body low-dose CT or PET/CT); or biomarker criteria (SLiM: >=60% clonal bone marrow plasma cells, involved-to-uninvolved serum free light chain [sFLC] ratio >=100, or >1 focal lesion on MRI). In the landmark Phase 3 MAIA trial (n=737 transplant-ineligible newly diagnosed myeloma patients), adding the anti-CD38 monoclonal antibody daratumumab to lenalidomide and dexamethasone (D-Rd) reduced the risk of disease progression or death by 44% (hazard ratio 0.56; 95% CI 0.43-0.73; p<0.001) with 5-year progression-free survival of 52.5% vs 28.7%. In transplant-eligible patients, quadruplet induction (D-RVd) followed by autologous stem cell transplantation achieves deep minimal residual disease negativity.",
        "solution_protocol": {
            "non_pharmacological_targets": "Aggressive oral hydration (>2-3 liters daily to prevent renal cast nephropathy); avoidance of nephrotoxic medications (NSAIDs, IV contrast dyes); prompt treatment of infections; monthly bisphosphonate or RANKL inhibitor (Zoledronic acid 4 mg IV or Denosumab 120 mg SC) to prevent skeletal-related events.",
            "monitoring_cadence": "Serum and 24-hour urine protein electrophoresis with immunofixation (SPEP/UPEP) and serum free light chain (sFLC) assay monthly during induction; complete blood count, serum creatinine, and calcium monthly; annual whole-body low-dose CT or PET/CT.",
            "clinical_thresholds": "Spinal cord compression (back pain with leg weakness or incontinence) is a medical emergency requiring immediate high-dose dexamethasone (40 mg IV), urgent spinal MRI, and emergency radiation therapy or neurosurgical decompression."
        },
        "patient_plain_language": "Multiple myeloma is a type of blood cancer that develops in plasma cells, a type of white blood cell in your bone marrow that normally makes antibodies to fight infections. In myeloma, abnormal plasma cells multiply uncontrollably and produce large amounts of a faulty antibody protein (M-protein). The myeloma cells weaken and eat away at your bones (causing bone pain and fractures), cause high calcium levels, damage your kidneys, and cause severe anemia.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current serum M-protein spike and involved-to-uninvolved serum free light chain (sFLC) ratio?",
            "safety_question": "Are my kidneys fully protected with good hydration, and am I receiving a bone-strengthening medication (like zoledronic acid or denosumab) to prevent bone fractures?",
            "action_threshold_question": "Am I a candidate for an autologous stem cell transplant after completing my initial quadruplet antibody drug therapy?"
        },
        "red_flags": [
            "Sudden severe back pain accompanied by leg weakness, difficulty walking, or loss of bowel/bladder control (Spinal Cord Compression Emergency), or extreme confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Multiple myeloma is a cancer that forms in a type of white blood cell called a plasma cell, crowding out healthy blood cells and damaging bones and kidneys.",
                "plain_analogy": "Abnormal plasma cells overrunning the bone marrow factory and drilling holes in bones while clogging kidney filters with faulty proteins.",
                "lifestyle_action": "Drink 2 to 3 liters of water every day to flush kidneys. Never take ibuprofen or Aleve. Take bone-strengthening infusions."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Daratumumab (Darzalex)", "Bortezomib (Velcade)", "Lenalidomide (Revlimid)", "Carfilzomib", "Zoledronic Acid"],
                "dosing_gdmt": "D-Rd regimen: Daratumumab 1,800 mg SC weekly for 8 weeks, every 2 weeks for 16 weeks, then monthly + Lenalidomide 25 mg daily + Dexamethasone 40 mg weekly.",
                "black_box_warning": "Lenalidomide: Severe birth defects and venous thromboembolism; mandatory aspirin or anticoagulation VTE prophylaxis.",
                "organ_clearance_cutoffs": "Adjust lenalidomide dose according to creatinine clearance; bortezomib does not require dose adjustment for renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MAIA / GRIFFIN",
                "pmid_or_doi": "10.1056/NEJMoa1817249",
                "cebm_level": 2,
                "sample_size": 737,
                "endpoints": "Progression-free survival significantly extended by daratumumab quadruplet/triplet (HR 0.56; p<0.001); 5-year PFS >52% in transplant-ineligible patients."
            }
        }
    },
    {
        "id": "DOC-CARD-289",
        "icd10": "C81.90",
        "condition": "Hodgkin Lymphoma",
        "specialty": "Hematology & Oncology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (ECHELON-1 Trial) & NCCN Guidelines",
        "citation": "Connors JM et al. Brentuximab Vedotin with Chemotherapy for Stage III or IV Hodgkin's Lymphoma (ECHELON-1). N Engl J Med. 2018;378(4):331-344.",
        "doi_or_source": "10.1056/NEJMoa1708984",
        "clinical_evidence": "Classical Hodgkin Lymphoma (cHL) is a B-cell-derived lymphoid malignancy characterized by binucleated or multinucleated giant Reed-Sternberg cells (CD30+, CD15+, CD20-) set within a rich inflammatory background, with a bimodal age distribution (peak in young adults aged 15-35 and >55). In the landmark multicenter randomized Phase 3 ECHELON-1 trial (n=1334 patients with stage III or IV cHL), replacing bleomycin with the antibody-drug conjugate brentuximab vedotin (A+AVD: brentuximab vedotin, doxorubicin, vinblastine, dacarbazine) significantly improved 5-year overall survival compared with standard ABVD (94.9% vs 88.9%; hazard ratio for death 0.59; 95% CI 0.40-0.88; p=0.009), while completely eliminating bleomycin-induced pulmonary toxicity. Interim PET/CT scan (Deauville 5-point score) after 2 cycles allows risk-adapted response-guided therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Primary prophylactic granulocyte colony-stimulating factor (G-CSF / pegfilgrastim) is mandatory with A+AVD to prevent severe neutropenia and febrile neutropenia; fertility preservation counseling (sperm banking or oocyte cryopreservation) prior to chemotherapy initiation; dental clearance.",
            "monitoring_cadence": "Interim 18F-FDG PET/CT scan after 2 cycles of chemotherapy (Deauville 5-point criteria; Deauville 1-3 indicates complete metabolic response); end-of-treatment PET/CT; comprehensive clinical examination every 3 months for 2 years, then every 6 months for 3 years; annual screening mammography starting 8-10 years post-mediastinal radiation.",
            "clinical_thresholds": "Deauville score 4-5 on interim PET/CT (persistent metabolic activity) indicates chemo-refractoriness, mandating biopsy confirmation and escalation to salvage immunochemotherapy (e.g. Pembrolizumab or Nivolumab plus AVD)."
        },
        "patient_plain_language": "Hodgkin lymphoma is a cancer of the lymphatic system, which is part of your body's germ-fighting immune network. Cancerous white blood cells called Reed-Sternberg cells multiply in your lymph nodes. It typically presents as a painless, firm, rubbery lump or swelling in your neck, armpit, or collarbone, accompanied by drenching night sweats, unexplained fevers, and rapid weight loss (known as 'B symptoms'). Hodgkin lymphoma is one of the most curable cancers known, with cure rates over 90%.",
        "doctor_consultation_checklist": {
            "parameter_question": "What clinical stage is my Hodgkin lymphoma (Stage I through IV) based on my initial whole-body PET/CT scan?",
            "safety_question": "Can I receive the bleomycin-free regimen (A+AVD with brentuximab vedotin) to protect my lungs from permanent breathing damage?",
            "action_threshold_question": "What did my interim PET scan (Deauville score) show after cycle 2 regarding whether the cancer has completely melted away?"
        },
        "red_flags": [
            "Fever >38.0°C (100.4°F) while undergoing chemotherapy (emergency febrile neutropenia), severe shortness of breath, or facial and arm swelling (Superior Vena Cava obstruction)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hodgkin lymphoma is a type of cancer that affects the lymphatic system, causing lymph nodes to swell and grow abnormally.",
                "plain_analogy": "A highly curable lymphoid cancer marked by giant 'owl-eyed' cells in swollen neck lymph nodes.",
                "lifestyle_action": "Complete fertility preservation before starting treatment. Report all fevers immediately. Protect skin from sun."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Brentuximab Vedotin (Adcetris)", "Nivolumab (Opdivo)", "Pembrolizumab (Keytruda)", "Doxorubicin", "Vinblastine"],
                "dosing_gdmt": "A+AVD: Brentuximab vedotin 1.2 mg/kg + Doxorubicin 25 mg/m2 + Vinblastine 6 mg/m2 + Dacarbazine 375 mg/m2 on days 1 and 15 of 28-day cycle x 6 cycles.",
                "black_box_warning": "Brentuximab Vedotin: Progressive multifocal leukoencephalopathy (PML) and severe peripheral neuropathy; monitor for numbness/tingling.",
                "organ_clearance_cutoffs": "Mandatory G-CSF support with A+AVD starting on day 2 or 3 of each cycle to prevent severe neutropenic sepsis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ECHELON-1 Trial",
                "pmid_or_doi": "10.1056/NEJMoa1708984",
                "cebm_level": 2,
                "sample_size": 1334,
                "endpoints": "5-year overall survival significantly improved to 94.9% with A+AVD vs 88.9% ABVD (HR 0.59; p=0.009); bleomycin pulmonary toxicity eliminated."
            }
        }
    },
    {
        "id": "DOC-CARD-290",
        "icd10": "C83.30",
        "condition": "Diffuse Large B-Cell Lymphoma (DLBCL)",
        "specialty": "Hematology & Oncology",
        "organ_system": "Hematologic",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (POLARIX Trial & ZUMA-7) & NCCN Guidelines",
        "citation": "Tilly H et al. Polatuzumab Vedotin in Previously Untreated Diffuse Large B-Cell Lymphoma (POLARIX). N Engl J Med. 2022;386(4):351-363.",
        "doi_or_source": "10.1056/NEJMoa2115304",
        "clinical_evidence": "Diffuse Large B-Cell Lymphoma (DLBCL) is the most common aggressive non-Hodgkin lymphoma (accounting for 30-40% of adult NHL), classified by cell of origin into Germinal Center B-cell-like (GCB) and Activated B-cell-like (ABC / non-GCB) subtypes. High-grade double-hit/triple-hit lymphomas carry concurrent MYC and BCL2/BCL6 translocations. In the landmark international Phase 3 POLARIX trial (n=879 patients with previously untreated intermediate-to-high risk DLBCL, IPI 2-5), replacing vincristine with the anti-CD79b antibody-drug conjugate polatuzumab vedotin (Pola-R-CHP: polatuzumab, rituximab, cyclophosphamide, doxorubicin, prednisone) significantly improved 2-year progression-free survival compared with standard R-CHOP (76.7% vs 70.2%; hazard ratio for progression, relapse, or death 0.73; 95% CI 0.57-0.95; p=0.02) and reduced the need for subsequent salvage therapies by 34%. In primary refractory or early relapsing (<12 months) DLBCL, autologous anti-CD19 chimeric antigen receptor (CAR) T-cell therapy (axicabtagene ciloleucel, ZUMA-7 trial) quadrupled event-free survival compared with standard salvage chemotherapy and autologous transplant (HR 0.40; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Tumor lysis syndrome (TLS) prophylaxis with vigorous intravenous hydration (2-3 L/m2/day) and allopurinol or rasburicase prior to cycle 1; fertility preservation consultation; hepatitis B screening and prophylactic entecavir for HBsAg/anti-HBc positive patients.",
            "monitoring_cadence": "Interim and end-of-treatment 18F-FDG PET/CT using the Lugano classification (Deauville 5-point scale); complete blood count with differential weekly; comprehensive cardiac echocardiogram measuring LVEF prior to anthracycline therapy.",
            "clinical_thresholds": "Deauville score 1-3 on end-of-treatment PET/CT defines complete metabolic remission; persistent Deauville 4-5 warrants immediate biopsy confirmation followed by CD19 CAR T-cell therapy evaluation."
        },
        "patient_plain_language": "Diffuse large B-cell lymphoma (DLBCL) is a fast-growing, aggressive cancer of the lymphatic system. B-cells, a type of white blood cell, rapidly multiply and crowd into lymph nodes, causing rapidly enlarging painless swellings in your neck, armpits, abdomen, or groin, accompanied by night sweats, fatigue, and unintended weight loss. Although it is fast-growing, it is very responsive to modern targeted chemo-immunotherapy, and the majority of patients can be permanently cured.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my International Prognostic Index (IPI) score and is my lymphoma classified as GCB or non-GCB on molecular biopsy?",
            "safety_question": "Was my heart pumping function (ejection fraction) checked before starting the red doxorubicin chemotherapy drug?",
            "action_threshold_question": "Am I receiving the modern Pola-R-CHP targeted regimen to give me the highest chance of permanent first-line cure?"
        },
        "red_flags": [
            "Fever over 100.4°F during chemotherapy (emergency febrile neutropenia), rapid swelling of face and neck, severe chest pressure, or difficulty breathing"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Diffuse large B-cell lymphoma is a cancer of the lymphatic system that develops from abnormal B cells and grows rapidly.",
                "plain_analogy": "A fast-multiplying swarm of abnormal B cells that causes lymph nodes to balloon in size, but is highly vulnerable to targeted chemotherapy.",
                "lifestyle_action": "Drink plenty of water to protect kidneys. Report any fever during chemotherapy immediately. Rest during treatment cycles."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Polatuzumab Vedotin (Polivy)", "Rituximab (Rituxan)", "Axicabtagene Ciloleucel (Yescarta)", "Doxorubicin", "Cyclophosphamide"],
                "dosing_gdmt": "Pola-R-CHP: Polatuzumab 1.8 mg/kg + Rituximab 375 mg/m2 + Cyclophosphamide 750 mg/m2 + Doxorubicin 50 mg/m2 IV q21d x 6 cycles + Prednisone 100 mg daily x 5d.",
                "black_box_warning": "CAR T-cell Therapy (Yescarta): Cytokine Release Syndrome (CRS) and immune effector cell-associated neurotoxicity syndrome (ICANS).",
                "organ_clearance_cutoffs": "Monitor for peripheral motor/sensory neuropathy with polatuzumab; reduce doxorubicin dose if bilirubin is elevated."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "POLARIX / ZUMA-7",
                "pmid_or_doi": "10.1056/NEJMoa2115304",
                "cebm_level": 2,
                "sample_size": 879,
                "endpoints": "2-year progression-free survival improved to 76.7% with Pola-R-CHP vs 70.2% R-CHOP (HR 0.73; p=0.02); CAR T-cell therapy quadruples event-free survival in relapse."
            }
        }
    },
    {
        "id": "DOC-CARD-291",
        "icd10": "C43.9",
        "condition": "Malignant Cutaneous Melanoma",
        "specialty": "Dermatology & Oncology",
        "organ_system": "Integumentary",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (CheckMate 067 & KEYNOTE-006) & NCCN Guidelines",
        "citation": "Wolchok JD et al. Overall Survival with Combined Nivolumab and Ipilimumab in Advanced Melanoma (CheckMate 067). N Engl J Med. 2017;377(14):1345-1356.",
        "doi_or_source": "10.1056/NEJMoa1709684",
        "clinical_evidence": "Cutaneous Melanoma is an aggressive malignancy originating from epidermal melanocytes, driven by ultraviolet radiation-induced driver mutations in BRAF (V600E/K in 40-50%), NRAS (15-20%), NF1, or KIT. Primary staging hinges on the AJCC 8th edition tumor thickness (Breslow depth), ulceration, and sentinel lymph node (SLN) status. Complete surgical wide local excision (1 cm margins for Breslow depth <=1.0 mm; 2 cm margins for >2.0 mm) with SLN biopsy is the standard for stage >=pT1b. In the landmark Phase 3 CheckMate 067 trial (n=945 patients with advanced unresectable/metastatic melanoma followed for 6.5 years), dual checkpoint inhibition with nivolumab (anti-PD-1) plus ipilimumab (anti-CTLA-4) achieved a median overall survival of 72.1 months compared with 19.9 months with ipilimumab monotherapy (hazard ratio for death 0.52; p<0.001), with a 6.5-year survival rate of 49% (and 57% in BRAF-mutant melanoma). For BRAF-mutated disease, targeted BRAF/MEK inhibitors (dabrafenib + trametinib) achieve rapid objective response rates >65%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily broad-spectrum SPF 50+ UVA/UVB sunscreen application; avoidance of midday sun (10 AM to 4 PM); UV-protective clothing and wide-brimmed hats; total body skin self-examinations monthly using the ABCDE criteria (Asymmetry, Border irregularity, Color variegation, Diameter >6 mm, Evolving).",
            "monitoring_cadence": "Full-body skin examination by a board-certified dermatologist every 3 months for 2 years, then every 6 months for 3 years; baseline BRAF V600 mutation testing on all resected stage >=IIB melanomas; surveillance whole-body PET/CT or brain MRI for stage III/IV.",
            "clinical_thresholds": "Breslow thickness >0.8 mm (or <0.8 mm with ulceration) indicates mandatory sentinel lymph node biopsy (SLNB) at the time of wide local excision."
        },
        "patient_plain_language": "Malignant melanoma is the most serious and dangerous type of skin cancer. It develops in the melanocyte cells that give your skin its pigment and color, often triggered by intense ultraviolet (UV) sun exposure or tanning beds. It frequently starts as an unusual mole that changes size, shape, or color. While early melanoma is easily cured with a simple surgical removal, it can spread rapidly to lymph nodes and internal organs if ignored.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was the exact Breslow thickness in millimeters on my biopsy report and did my sentinel lymph node show any microscopic cancer cells?",
            "safety_question": "Has my melanoma tumor been tested for the BRAF V600 genetic mutation to guide targeted therapy?",
            "action_threshold_question": "Would I benefit from preventative immunotherapy infusions (such as pembrolizumab or nivolumab) after surgery to stop the cancer from returning?"
        },
        "red_flags": [
            "A mole that changes rapidly in size or color, bleeds, itches, or crusts, or new hard painless lumps feeling like marbles under your armpits or groin"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Melanoma is the most serious type of skin cancer, which develops in the cells that produce melanin — the pigment that gives your skin its color.",
                "plain_analogy": "A pigment cell gone rogue from sun damage, capable of sending microscopic metastatic seeds to internal organs if not cut out early.",
                "lifestyle_action": "Check your moles monthly using ABCDE rules. Wear SPF 50+ daily. Avoid tanning beds permanently. See a dermatologist annually."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Pembrolizumab (Keytruda)", "Nivolumab (Opdivo)", "Ipilimumab (Yervoy)", "Dabrafenib (Tafinlar)", "Trametinib (Mekinist)"],
                "dosing_gdmt": "Adjuvant Stage III/IV: Pembrolizumab 200 mg IV q3w for 1 year. Metastatic: Nivolumab 1 mg/kg + Ipilimumab 3 mg/kg IV q3w for 4 doses, then Nivolumab.",
                "black_box_warning": "Immune Checkpoint Inhibitors: Severe and fatal immune-mediated adverse reactions (colitis, pneumonitis, hepatitis, endocrinopathies).",
                "organ_clearance_cutoffs": "Monitor liver enzymes, thyroid panel, and morning cortisol prior to each immunotherapy cycle; treat colitis with high-dose steroids."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CheckMate 067",
                "pmid_or_doi": "10.1056/NEJMoa1709684",
                "cebm_level": 2,
                "sample_size": 945,
                "endpoints": "6.5-year overall survival reached 49% with nivolumab + ipilimumab (median survival 72.1 months vs 19.9 months; HR 0.52; p<0.001); long-term cures observed."
            }
        }
    },
    {
        "id": "DOC-CARD-292",
        "icd10": "C44.91",
        "condition": "Basal Cell & Cutaneous Squamous Cell Carcinoma",
        "specialty": "Dermatology & Oncology",
        "organ_system": "Integumentary",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial & Guidelines",
        "source_body": "NEJM (Cemiplimab Trial & Vismodegib) & NCCN Guidelines",
        "citation": "Migden MR et al. PD-1 Blockade with Cemiplimab in Advanced Cutaneous Squamous-Cell Carcinoma. N Engl J Med. 2018;379(4):341-351.",
        "doi_or_source": "10.1056/NEJMoa1716971",
        "clinical_evidence": "Non-melanoma skin cancers (NMSC) are the most common human malignancies, comprising Basal Cell Carcinoma (BCC, 80%, driven by Hedgehog pathway mutations [PTCH1/SMO]) and Cutaneous Squamous Cell Carcinoma (cSCC, 20%, driven by TP53 mutations and cumulative UV damage). BCC presents as a pearly pink papule with rolled borders, arborizing telangiectasias, and central ulceration. High-risk NMSC (head/neck 'H-zone', diameter >2 cm, poorly differentiated, or perineural invasion) is treated with Mohs Micrographic Surgery (MMS), achieving the highest 5-year cure rate (>99% for primary BCC; >97% for cSCC) with maximum tissue sparing. In locally advanced or metastatic cSCC, the anti-PD-1 checkpoint inhibitor cemiplimab achieved an objective response rate of 47-50% with durable responses lasting >12 months in the landmark Phase 2/3 trial (NEJM 2018). In advanced/inoperable BCC, the oral Hedgehog pathway inhibitor vismodegib achieves objective responses in 43-60%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily application of broad-spectrum SPF 30-50+ sunscreen; avoidance of sunbeds and direct midday sun; wearing wide-brimmed hats and sun-protective clothing; annual total body skin examinations by a dermatologist.",
            "monitoring_cadence": "Dermatologic follow-up every 6 months for 2 years, then annually (patients with a prior NMSC have a 30-50% risk of developing a subsequent skin cancer within 5 years); lymph node palpation in high-risk cSCC.",
            "clinical_thresholds": "Lesions in cosmetically or functionally critical facial areas (eyelids, nose, lips, ears) or high-risk features mandate Mohs micrographic surgery."
        },
        "patient_plain_language": "Basal cell carcinoma and squamous cell carcinoma are the two most common types of skin cancer. They develop on areas of your body exposed to the sun, such as your face, ears, neck, scalp, and arms. Basal cell cancer often looks like a shiny, pearly pink bump with tiny visible blood vessels, while squamous cell cancer looks like a firm red nodule or a rough, scaly, crusty patch that bleeds easily. When caught early, they are almost 100% curable with a precise in-office surgical procedure called Mohs surgery.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my skin biopsy confirm basal cell carcinoma or squamous cell carcinoma, and were the surgical margins clear?",
            "safety_question": "Is my lesion in a high-risk area (like my nose, eyelid, or ear) that should be removed using Mohs micrographic surgery to save normal skin?",
            "action_threshold_question": "How often should I return for full-body skin checks to catch new skin cancers while they are small?"
        },
        "red_flags": [
            "A sore on your face that bleeds, oozes, crusts, and refuses to heal over 4 weeks, or a rapidly growing firm red bump under the skin near the ear or lip"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Basal cell and squamous cell carcinomas are the most common forms of skin cancer, starting in the top layer of skin and strongly linked to sun exposure.",
                "plain_analogy": "Sun-damaged skin cells growing out of control, easily cut out early but capable of deep local destruction if neglected.",
                "lifestyle_action": "Wear wide-brimmed hats outdoors. Put on sunscreen every morning. Never ignore a bleeding scab that will not heal."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Cemiplimab (Libtayo)", "Vismodegib (Erivedge)", "Fluorouracil Topical (5-FU)", "Imiquimod 5% Cream"],
                "dosing_gdmt": "Standard: Mohs micrographic surgical excision. For advanced cSCC: Cemiplimab 350 mg IV q3w. For superficial BCC: Topical 5-FU BID x 4 weeks.",
                "black_box_warning": "Vismodegib: Severe embryo-fetal death and devastating birth defects; verify pregnancy status prior to initiation.",
                "organ_clearance_cutoffs": "Monitor for immune-mediated colitis, pneumonitis, and endocrinopathies with cemiplimab checkpoint therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEJM Cemiplimab CSCC",
                "pmid_or_doi": "10.1056/NEJMoa1716971",
                "cebm_level": 2,
                "sample_size": 137,
                "endpoints": "Objective response rate 47% with cemiplimab in advanced cSCC; durable disease control rate 65%; Mohs surgery 5-year cure rate exceeds 99%."
            }
        }
    },
    {
        "id": "DOC-CARD-293",
        "icd10": "L73.2",
        "condition": "Hidradenitis Suppurativa",
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (PIONEER Trials) & The Lancet (SUNSHINE & SUNSPOT)",
        "citation": "Kimball AB et al. Two Phase 3 Trials of Adalimumab for Hidradenitis Suppurativa (PIONEER I and II). N Engl J Med. 2016;375(5):422-434.",
        "doi_or_source": "10.1056/NEJMoa1504370",
        "clinical_evidence": "Hidradenitis Suppurativa (HS, acne inversa) is a chronic, painful, debilitating inflammatory follicular occlusion disease affecting apocrine gland-bearing intertriginous skin (axillae, groin, perineal, perianal, and inframammary regions), staged by Hurley stages I (isolated nodules/abscesses), II (recurrent abscesses with sinus tracts and scarring), and III (diffuse confluent interconnected sinus tracts across entire anatomical areas). In the landmark Phase 3 PIONEER I and II trials (n=633 patients with moderate-to-severe HS), adalimumab (160 mg at week 0, 80 mg at week 2, then 40 mg weekly) achieved the Hidradenitis Suppurativa Clinical Response (HiSCR: >=50% reduction in inflammatory nodule and abscess count with zero increase in draining fistulas) in 41.8% to 58.9% of patients compared with 26.0% to 27.6% with placebo (p<0.001). The Phase 3 SUNSHINE and SUNSPOT trials proved that the IL-17A inhibitor secukinumab (300 mg every 2 or 4 weeks) is highly effective and safe for long-term clinical response.",
        "solution_protocol": {
            "non_pharmacological_targets": "Absolute smoking cessation (tobacco smoking is the single strongest disease driver and triggers follicular hyperkeratosis in >85%); structured weight reduction (obesity exacerbates intertriginous skin friction and sweat retention); wearing loose-fitting, breathable cotton clothing; antiseptic washes (chlorhexidine 4% or benzoyl peroxide).",
            "monitoring_cadence": "HiSCR and Hurley staging at 12-week intervals; International Hidradenitis Suppurativa Severity Score (IHS4) at each visit; screening for associated metabolic syndrome and inflammatory bowel disease.",
            "clinical_thresholds": "Hurley stage II or III disease refractory to oral tetracyclines (Doxycycline 100 mg BID for 12 weeks) warrants immediate initiation of biologic therapy (Adalimumab 40 mg weekly or Secukinumab 300 mg q2w) and surgical deroofing/wide excision."
        },
        "patient_plain_language": "Hidradenitis suppurativa (HS) is a chronic, painful, inflammatory skin condition that causes deep, swollen, tender boil-like lumps in areas where skin rubs together, such as your armpits, groin, inner thighs, and under your breasts. The bumps often rupture, draining foul-smelling fluid, and develop interconnected tunnels (sinus tracts) under the skin that heal into thick scar tissue. It is not caused by poor hygiene and is not contagious.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Hurley stage (Stage I, II, or III) and my International HS Severity Score (IHS4)?",
            "safety_question": "Am I a candidate for biologic injections (like adalimumab or secukinumab) to turn off the deep immune inflammation?",
            "action_threshold_question": "Should we schedule surgical 'deroofing' to remove persistent underground drainage tunnels that antibiotics cannot reach?"
        },
        "red_flags": [
            "Severe worsening pain with high fever and chills (secondary cellulitis / bacteremia), rapidly expanding redness, or inability to sit or walk due to groin abscesses"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hidradenitis suppurativa is a chronic skin disease that features small, painful lumps under the skin that typically develop in armpits and the groin.",
                "plain_analogy": "Hair follicles in skin folds getting plugged and exploding inward, creating underground drainage tunnels under the skin.",
                "lifestyle_action": "Quit smoking immediately. Wear loose cotton underwear. Use antibacterial body washes. Avoid tight-fitting clothes."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Adalimumab (Humira)", "Secukinumab (Cosentyx)", "Doxycycline", "Clindamycin + Rifampin"],
                "dosing_gdmt": "Adalimumab: Day 1 (160 mg), Day 15 (80 mg), Day 29 and weekly thereafter (40 mg SC). Or Secukinumab 300 mg every 2-4 weeks.",
                "black_box_warning": "Biologics: Increased risk of serious fungal, bacterial, and mycobacterial (TB) infections; test for latent TB prior to starting.",
                "organ_clearance_cutoffs": "For acute flares: Intralesional triamcinolone acetonide (3-5 mg/mL) injected directly into early nodules provides rapid relief."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PIONEER I & II",
                "pmid_or_doi": "10.1056/NEJMoa1504370",
                "cebm_level": 2,
                "sample_size": 633,
                "endpoints": "HiSCR clinical response achieved in 59% with weekly adalimumab vs 27% placebo (p<0.001); flare frequency and pain scores significantly reduced."
            }
        }
    },
    {
        "id": "DOC-CARD-294",
        "icd10": "L12.0",
        "condition": "Bullous Pemphigoid",
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (Topical Clobetasol Trial) & The Lancet (Ritux 3)",
        "citation": "Joly P et al. A comparison of oral and topical corticosteroids in patients with bullous pemphigoid. N Engl J Med. 2002;346(5):321-327.",
        "doi_or_source": "10.1056/NEJMoa011592",
        "clinical_evidence": "Bullous Pemphigoid (BP) is the most common autoimmune subepidermal blistering disease of the elderly, driven by pathogenic IgG autoantibodies directed against hemidesmosomal adhesion proteins BP180 (type XVII collagen, NC16A domain) and BP230. Hallmark presentation is tense, fluid-filled bullae on normal or erythematous/urticarial skin, accompanied by intense pruritus, with negative Nikolsky sign. Direct immunofluorescence (DIF) of perilesional skin demonstrates pathognomonic linear deposition of IgG and complement C3 along the dermal-epidermal basement membrane zone. In the landmark randomized Phase 3 trial (n=341 patients), high-potency topical clobetasol propionate cream (20-30 g daily) was superior to standard oral prednisone (1 mg/kg/day) for overall survival at 1 year (76% vs 58%; p=0.02) and had fewer severe adverse events (29% vs 54%; p=0.002) while providing equivalent disease control (99% vs 100%). In refractory disease, rituximab (Ritux 3 trial) achieves complete remission off therapy in >70%.",
        "solution_protocol": {
            "non_pharmacological_targets": "Gentle skin wound care with non-adherent silicone dressings; sterile needle aspiration of large tense blisters while leaving the protective blister roof intact; cool colloidal oatmeal compresses; avoidance of skin shearing forces.",
            "monitoring_cadence": "Bullous Pemphigoid Disease Area Index (BPDAI) and pruritus numerical score weekly during induction; quantitative serum anti-BP180 and anti-BP230 ELISA titers every 3 months; monitor blood glucose, blood pressure, and electrolytes.",
            "clinical_thresholds": "BPDAI score reduction >80% with absence of new blisters defines disease control; extensive disease in patients unable to apply topical creams warrants low-dose oral prednisone (0.5 mg/kg/day) combined with steroid-sparing agents (doxycycline or methotrexate)."
        },
        "patient_plain_language": "Bullous pemphigoid is an autoimmune skin condition that primarily affects older adults. Your body's immune system mistakenly attacks the protein 'glue' that attaches the outer layer of your skin (epidermis) to the deeper layer (dermis). This causes large, tense, fluid-filled blisters to form on your skin that do not pop easily, usually preceded by weeks of intense, itchy red patches that feel like severe hives.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my skin biopsy direct immunofluorescence (DIF) confirm linear IgG and C3 antibody bands along the basement membrane?",
            "safety_question": "Can we manage my blisters using high-strength prescription steroid creams (clobetasol) to avoid the severe side effects of oral steroid pills?",
            "action_threshold_question": "Could any of my regular medications (such as DPP-4 inhibitor diabetes pills like sitagliptin, or furosemide) have triggered this blister reaction?"
        },
        "red_flags": [
            "Blisters covering more than 30% of your body surface, open weeping raw skin with high fever and shaking chills (secondary skin infection/sepsis), or mouth sores preventing eating"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bullous pemphigoid is a rare autoimmune skin condition that causes large, fluid-filled blisters on areas of skin that flex, such as the lower abdomen, thighs, or armpits.",
                "plain_analogy": "The microscopic Velcro holding the outer skin to the inner skin being dissolved by autoantibodies, letting fluid pool into tight blisters.",
                "lifestyle_action": "Do not tear off blister roofs. Apply steroid cream gently. Check with your doctor if taking DPP-4 diabetes medications."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Clobetasol Propionate 0.05% Cream", "Prednisone Oral", "Rituximab", "Doxycycline 100 mg", "Nicotinamide"],
                "dosing_gdmt": "First-line: Clobetasol propionate 0.05% cream 20-30 g daily applied to all affected skin, tapering over 4-6 months. Or Doxycycline 100 mg BID.",
                "black_box_warning": "High-dose oral steroids in frail elderly: High 1-year mortality (>30-40%) driven by sepsis and cardiovascular events; prefer topical clobetasol.",
                "organ_clearance_cutoffs": "Monitor for skin atrophy with prolonged topical steroids; screen for osteoporosis and provide calcium/vitamin D."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NEJM Clobetasol BP Trial",
                "pmid_or_doi": "10.1056/NEJMoa011592",
                "cebm_level": 2,
                "sample_size": 341,
                "endpoints": "1-year survival significantly superior with topical clobetasol vs oral prednisone (76% vs 58%; p=0.02); severe adverse events cut in half (29% vs 54%)."
            }
        }
    },
    {
        "id": "DOC-CARD-295",
        "icd10": "L80",
        "condition": "Vitiligo",
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (TRuE-V1 & TRuE-V2 Trials) & Vitiligo Guidelines",
        "citation": "Rosmarin D et al. Two Phase 3 Trials of Ruxolitinib Cream for Vitiligo (TRuE-V1 & TRuE-V2). N Engl J Med. 2022;387(16):1445-1455.",
        "doi_or_source": "10.1056/NEJMoa2118828",
        "clinical_evidence": "Vitiligo is an acquired autoimmune depigmenting disorder characterized by progressive destruction of epidermal melanocytes, mediated by CD8+ cytotoxic T lymphocytes producing interferon-gamma (IFN-gamma) through the JAK-STAT signaling pathway (JAK1/JAK2). In the landmark double-blind Phase 3 TRuE-V1 and TRuE-V2 trials (n=674 patients aged >=12 with non-segmental vitiligo), topical ruxolitinib 1.5% cream (a selective JAK1/JAK2 inhibitor applied BID for 24-52 weeks) achieved the primary endpoint of >=75% improvement in the facial Vitiligo Area Scoring Index (F-VASI75) in 29.8% to 30.9% of patients compared with 7.4% to 11.4% with vehicle control (p<0.001). At 52 weeks, over 50% achieved F-VASI75 and 30% achieved F-VASI90, with marked repigmentation across body lesions (T-VASI50 in 50%). Combining topical therapies with narrow-band ultraviolet B (NB-UVB) phototherapy accelerates follicular melanocyte stem cell migration and repigmentation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Broad-spectrum SPF 50+ sunscreen applied to depigmented macules (preventing sunburn in unprotected amelanotic skin and reducing contrasting tanning in surrounding skin); avoidance of skin trauma (Koebner phenomenon triggers new patches); cosmetic camouflage counseling.",
            "monitoring_cadence": "Facial and Total Vitiligo Area Scoring Index (F-VASI and T-VASI) every 3 months; Wood's lamp examination (delineating subclinical active depigmentation); baseline TSH, free T4, and anti-TPO antibodies (screening for concurrent Hashimoto's thyroiditis in 20-30%).",
            "clinical_thresholds": "Rapidly progressive 'active' vitiligo (spreading macules, confetti-like depigmentation, Koebner phenomenon) warrants oral mini-pulse corticosteroid therapy (dexamethasone 4-5 mg on 2 consecutive days weekly for 3 months) to arrest progression."
        },
        "patient_plain_language": "Vitiligo is an autoimmune skin condition where your immune system mistakenly attacks and destroys your body's melanocytes (the specialized cells that produce skin pigment). As pigment cells are lost, chalky-white patches (macules) appear on your skin, commonly around your mouth, eyes, hands, fingers, and elbows. In recent years, breakthrough topical JAK inhibitor creams have been developed that block the immune signal, allowing pigment to naturally fill back in.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Facial and Total Vitiligo Area Scoring Index (F-VASI / T-VASI)?",
            "safety_question": "Have we checked my thyroid blood tests (TSH and thyroid antibodies) to screen for autoimmune thyroid disease?",
            "action_threshold_question": "Can I combine topical ruxolitinib cream (Opzelura) with narrowband UVB light therapy to speed up my skin repigmentation?"
        },
        "red_flags": [
            "Sudden rapid eruption of dozens of tiny white spots (confetti-like vitiligo indicating hyper-active disease), severe blistering sunburn on white patches, or severe depression"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Vitiligo is a disease that causes loss of skin color in patches, occurring when pigment-producing cells die or stop functioning.",
                "plain_analogy": "Autoimmune immune cells turning off the skin's color printers, leaving smooth chalky-white patches.",
                "lifestyle_action": "Apply SPF 50+ to white patches daily to prevent sunburn. Avoid friction and tight waistbands. Check thyroid yearly."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Ruxolitinib 1.5% Cream (Opzelura)", "Tacrolimus 0.1% Ointment", "Clobetasol Propionate", "Narrowband UVB Phototherapy"],
                "dosing_gdmt": "Ruxolitinib 1.5% cream applied as a thin layer BID to affected areas up to 10% body surface area. Narrowband UVB phototherapy 2-3 times weekly.",
                "black_box_warning": "Topical JAK Inhibitors: Boxed warning for serious infections, mortality, malignancy, major adverse cardiovascular events (MACE), and thrombosis.",
                "organ_clearance_cutoffs": "Do not use in combination with therapeutic biologics or other JAK inhibitors; monitor for application site acne and pruritus."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TRuE-V1 & TRuE-V2",
                "pmid_or_doi": "10.1056/NEJMoa2118828",
                "cebm_level": 2,
                "sample_size": 674,
                "endpoints": "F-VASI75 achieved in 30% with ruxolitinib cream vs 8% vehicle (p<0.001) at 24 weeks; >50% achieved F-VASI75 at 52 weeks with durable repigmentation."
            }
        }
    },
    {
        "id": "DOC-CARD-296",
        "icd10": "L63.9",
        "condition": "Alopecia Areata",
        "specialty": "Dermatology",
        "organ_system": "Integumentary",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (BRAVE-AA1 & BRAVE-AA2) & Lancet (ALLEGRO)",
        "citation": "King B et al. Two Phase 3 Trials of Baricitinib for Alopecia Areata (BRAVE-AA1 and BRAVE-AA2). N Engl J Med. 2022;386(18):1687-1699.",
        "doi_or_source": "10.1056/NEJMoa2119426",
        "clinical_evidence": "Alopecia Areata (AA) is an autoimmune non-scarring hair loss disorder characterized by the collapse of hair follicle immune privilege, driven by autoreactive CD8+NKG2D+ T lymphocytes attacking hair bulb melanocytes via the IFN-gamma and IL-15 / JAK-STAT signaling pathways. Clinical phenotypes range from patchy hair loss to complete scalp baldness (Alopecia Totalis) and complete loss of all body hair (Alopecia Universalis). In the landmark randomized double-blind Phase 3 BRAVE-AA1 and BRAVE-AA2 trials (n=1200 patients with severe AA, baseline Severity of Alopecia Tool [SALT] score >=50), the oral JAK1/JAK2 inhibitor baricitinib (4 mg daily) achieved the primary endpoint of a SALT score <=20 (>=80% scalp hair coverage) in 35.2% to 38.8% of patients compared with only 3.3% to 6.2% on placebo at week 36 (p<0.001). Continued treatment out to 52 weeks increased SALT <=20 response rates to over 40%, with prominent eyebrow and eyelash regrowth.",
        "solution_protocol": {
            "non_pharmacological_targets": "Gentle hair styling (avoiding traction, pulling, or harsh chemical relaxers); scalp sun protection (sunscreen SPF 50+ or hats to prevent scalp sunburn on bare patches); psychological counseling for alopecia-related distress and depression.",
            "monitoring_cadence": "Severity of Alopecia Tool (SALT) scoring and dermoscopic trichoscopy (evaluating yellow dots, black dots, and pathognomonic exclamation mark hairs) every 3 months; complete blood count, lipid panel, and liver/renal function tests on JAK inhibitors.",
            "clinical_thresholds": "Patchy mild-to-moderate AA (<30-50% scalp loss) is treated first-line with intralesional triamcinolone acetonide (2.5-5.0 mg/mL every 4-6 weeks); severe AA (SALT score >=50) warrants oral JAK inhibitor therapy (Baricitinib 2-4 mg or Ritlecitinib 50 mg daily)."
        },
        "patient_plain_language": "Alopecia areata is an autoimmune condition where your immune system mistakenly targets and attacks your hair follicles. The immune cells cause the hair follicles to go into a dormant, resting state, causing your hair to suddenly fall out in round or oval patches the size of a coin. In more severe cases, it can cause the loss of all scalp hair, eyebrows, eyelashes, and body hair. Fortunately, the hair roots remain alive, meaning hair can fully regrow once the immune attack is calmed.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Severity of Alopecia Tool (SALT) score percentage?",
            "safety_question": "Am I a candidate for local cortisone injections into the bare patches, or is my hair loss extensive enough to warrant an oral JAK inhibitor like baricitinib or ritlecitinib?",
            "action_threshold_question": "What baseline blood tests (such as lipid panel, tuberculosis test, and hepatitis screen) are required before starting oral JAK inhibitors?"
        },
        "red_flags": [
            "Rapid total loss of all scalp hair, eyebrows, and eyelashes over a few weeks, severe emotional depression, or signs of serious systemic infection while taking JAK inhibitors"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Alopecia areata is an autoimmune disease that happens when your immune system attacks your hair follicles and causes your hair to fall out in patches.",
                "plain_analogy": "The immune system putting a temporary lock on hair follicles, freezing hair growth without destroying the follicle root.",
                "lifestyle_action": "Wear wide-brimmed hats to protect bare scalp from sunburn. Treat early patches with localized cortisone shots."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Baricitinib (Olumiant)", "Ritlecitinib (Litfulo)", "Triamcinolone Acetonide (Intralesional)", "Minoxidil Topical 5%"],
                "dosing_gdmt": "Baricitinib: Start 2 mg PO daily, titrate to 4 mg daily for severe disease. Intralesional Triamcinolone 2.5-5 mg/mL injected q4-6 weeks.",
                "black_box_warning": "Oral JAK Inhibitors: Boxed warning for serious infections, mortality, malignancies (lymphomas), MACE, and thrombosis.",
                "organ_clearance_cutoffs": "Screen for latent TB, viral hepatitis, and baseline lipids prior to starting; reduce baricitinib to 2 mg if eGFR 30-60 mL/min."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "BRAVE-AA1 & AA2",
                "pmid_or_doi": "10.1056/NEJMoa2119426",
                "cebm_level": 2,
                "sample_size": 1200,
                "endpoints": "SALT score <=20 (>=80% scalp hair coverage) achieved in 39% with baricitinib 4 mg vs 6% placebo (p<0.001); eyebrow and eyelash regrowth sustained."
            }
        }
    },
    {
        "id": "DOC-CARD-297",
        "icd10": "B02.9",
        "condition": "Herpes Zoster (Shingles) & Postherpetic Neuralgia",
        "specialty": "Infectious Disease & Neurology",
        "organ_system": "Integumentary & Nervous",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (ZOE-50 & ZOE-70 Trials) & CDC/ACIP Guidelines",
        "citation": "Lal H et al. Efficacy of an adjuvanted herpes zoster subunit vaccine in older adults (ZOE-50). N Engl J Med. 2015;372(22):2087-2096.",
        "doi_or_source": "10.1056/NEJMoa1501184",
        "clinical_evidence": "Herpes Zoster (shingles) results from reactivation of latent Varicella-Zoster Virus (VZV) in cranial nerve or dorsal root ganglia, presenting as unilateral, dermatomal, grouped erythematous papules and vesicles that do not cross the anatomical midline, preceded by burning neuropathic pain. Postherpetic Neuralgia (PHN), defined as debilitating neuropathic pain persisting >=90 days after rash onset, is the most common complication (occurring in 10-20% of patients, rising to >30% in those >=80 years). In the landmark Phase 3 ZOE-50 trial (n=15,411 adults >=50 years) and ZOE-70 trial (n=13,900 adults >=70 years), the recombinant adjuvanted zoster subunit vaccine (Shingrix, 2 doses at 0 and 2-6 months) demonstrated an unprecedented 97.2% vaccine efficacy in preventing herpes zoster across all age groups >=50 (p<0.001) and reduced postherpetic neuralgia incidence by 91.2%. Acute oral antiviral therapy (valacyclovir 1 g TID for 7 days) initiated within 72 hours of rash onset accelerates lesion healing and halves the duration of acute pain.",
        "solution_protocol": {
            "non_pharmacological_targets": "Universal recombinant zoster vaccination (Shingrix, 2-dose series) for all immunocompetent adults >=50 years and immunocompromised adults >=19 years; keeping the blistering rash clean, dry, and loosely covered to prevent viral transmission to varicella-naive contacts; cool tap water compresses.",
            "monitoring_cadence": "Dermatomal rash inspection and visual analog pain scale at days 3, 7, and 14, and at 3 months (assessing for chronic PHN); immediate ophthalmology slit-lamp exam if involvement of the V1 ophthalmic branch of trigeminal nerve (Hutchinson's sign: vesicles on tip of nose).",
            "clinical_thresholds": "Presence of vesicles on the tip or side of the nose (Hutchinson's sign) indicates Herpes Zoster Ophthalmicus with direct nasociliary nerve involvement (carries 50% risk of blinding keratitis, anterior uveitis, or glaucoma), mandating emergency same-day ophthalmologic evaluation."
        },
        "patient_plain_language": "Herpes zoster (commonly called shingles) is a painful blistering rash caused by the chickenpox virus (varicella-zoster virus). After you recover from chickenpox, the virus stays dormant and asleep inside your nerve roots for decades. Years later, when your immune system is stressed or ages, the virus wakes up and travels down the nerve path to your skin, creating a painful, tingling, blistering rash in a single stripe on one side of your chest, face, or belly. In some people, the nerve pain can last for months or years after the rash heals (postherpetic neuralgia).",
        "doctor_consultation_checklist": {
            "parameter_question": "Am I within the 72-hour time window to start oral antiviral pills (valacyclovir) to speed up healing and protect my nerves?",
            "safety_question": "Do I have any blisters near my nose or eye that could threaten my eyesight (Herpes Zoster Ophthalmicus)?",
            "action_threshold_question": "If my nerve pain persists after the rash clears, which nerve pain medication (such as gabapentin or a lidocaine patch) will relieve the burning?"
        },
        "red_flags": [
            "Blisters on the tip of your nose or near your eye (Zoster Ophthalmicus emergency), facial paralysis with ear pain and ear blisters (Ramsay Hunt syndrome), or high fever with confusion"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Shingles is a viral infection that causes a painful rash, caused by the varicella-zoster virus — the same virus that causes chickenpox.",
                "plain_analogy": "The sleeping chickenpox virus waking up decades later and marching down a single nerve highway, causing a stripe of burning blisters on the skin.",
                "lifestyle_action": "Get vaccinated with the 2-dose Shingrix vaccine. Start antiviral pills within 72 hours of rash. Keep blisters covered."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Zoster Vaccine Recombinant (Shingrix)", "Valacyclovir (Valtrex)", "Acyclovir", "Gabapentin (for PHN)", "Lidocaine 5% Topical Patch"],
                "dosing_gdmt": "Acute: Valacyclovir 1,000 mg PO TID for 7 days. Prevention: Shingrix 2 doses IM (0 and 2-6 months). Postherpetic pain: Gabapentin 300-900 mg TID.",
                "black_box_warning": "Valacyclovir: Dose-adjust in renal impairment; acute renal failure and thrombotic microangiopathy reported in high doses.",
                "organ_clearance_cutoffs": "Reduce valacyclovir dose if CrCl <50 mL/min (e.g. 1 g BID if CrCl 30-49; 1 g daily if CrCl 10-29 mL/min)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ZOE-50 & ZOE-70",
                "pmid_or_doi": "10.1056/NEJMoa1501184",
                "cebm_level": 2,
                "sample_size": 15411,
                "endpoints": "Shingrix vaccine efficacy in preventing shingles was 97.2% across adults >=50 (p<0.001); postherpetic neuralgia incidence reduced by 91.2%."
            }
        }
    },
    {
        "id": "DOC-CARD-298",
        "icd10": "B27.00",
        "condition": "Infectious Mononucleosis (Epstein-Barr Virus)",
        "specialty": "Infectious Disease",
        "organ_system": "Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CDC Clinical Guidance & Diagnostic Synthesis",
        "source_body": "CDC Infectious Disease Guidance & JAMA Rational Clinical Exam",
        "citation": "Ebell MH et al. Does this patient have infectious mononucleosis? JAMA. 2016;315(14):1502-1509.",
        "doi_or_source": "10.1001/jama.2016.2111",
        "clinical_evidence": "Infectious Mononucleosis ('mono', glandular fever) is caused predominantly by Epstein-Barr Virus (EBV / human herpesvirus 4), transmitted via oral secretions ('kissing disease') and infecting mucosal epithelial cells and B lymphocytes. The classic clinical triad comprises fever, tonsillar pharyngitis (often with thick white-gray exudates and palatal petechiae), and prominent posterior cervical lymphadenopathy. Diagnostic laboratory criteria include atypical lymphocytosis (>=10% atypical/reactive lymphocytes on peripheral blood smear, sensitivity 75%, specificity 92%) and a positive heterophile antibody test (Monospot test, sensitivity 85%, specificity 99% in adults; may be false-negative in the first week). In Monospot-negative cases, EBV viral capsid antigen (VCA) IgM and IgG establish definitive acute diagnosis. Splenomegaly is present in >50-60% of patients, carrying a catastrophic risk of atraumatic splenic rupture (predominantly occurring between days 4 and 21 of illness). Amoxicillin/ampicillin triggers an erythematous maculopapular drug eruption in up to 90% of mono patients.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of all competitive sports, heavy lifting, contact athletics, and vigorous physical exertion for a minimum of 3 to 4 weeks from symptom onset (prevents traumatic splenic rupture); adequate oral hydration and rest; throat lozenges and warm salt water gargles.",
            "monitoring_cadence": "Abdominal palpation and bedside ultrasound evaluating spleen dimensions prior to athletic clearance; liver function tests (mild self-limiting transaminitis occurs in >80%); complete blood count with differential.",
            "clinical_thresholds": "Impending airway obstruction from massive 'kissing' tonsillar hypertrophy, severe autoimmune hemolytic anemia, or thrombocytopenia justifies a short course of oral corticosteroids (prednisone 40-60 mg daily tapered over 7 days)."
        },
        "patient_plain_language": "Infectious mononucleosis (often called 'mono' or the 'kissing disease') is a common viral infection caused by the Epstein-Barr virus (EBV), spread through saliva. It causes severe fatigue, a sore throat with swollen white tonsils, high fever, and swollen, tender lymph nodes in the neck. In addition, the infection causes your spleen (an organ in your upper left abdomen that filters blood) to swell. Because the swollen spleen is soft and fragile, all contact sports must be avoided for at least a month to prevent it from rupturing.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my Monospot test or EBV viral capsid antigen (VCA IgM) confirm acute Epstein-Barr virus infection?",
            "safety_question": "How many weeks must I strictly avoid contact sports, gym workouts, or heavy lifting to prevent my spleen from rupturing?",
            "action_threshold_question": "Why should I avoid amoxicillin or penicillin antibiotics (which cause a full-body rash in mono patients)?"
        },
        "red_flags": [
            "Sudden severe sharp pain in the upper left abdomen or left shoulder tip (Kehr sign indicating acute Splenic Rupture emergency), difficulty breathing, or inability to swallow liquids"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Infectious mononucleosis, also called mono, is a contagious illness caused by the Epstein-Barr virus that causes extreme fatigue, fever, and swollen lymph nodes.",
                "plain_analogy": "A viral infection that temporarily swells the lymph nodes and inflates the spleen like a delicate, fragile water balloon.",
                "lifestyle_action": "Strictly avoid all contact sports for at least 4 weeks. Rest and drink liquids. Never take amoxicillin for mono sore throats."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Acetaminophen", "Ibuprofen", "Prednisone (Short-course for airway compromise)"],
                "dosing_gdmt": "Symptomatic: Acetaminophen 500-1000 mg q6h PRN (max 3g/day). For severe tonsillar airway obstruction: Prednisone 50 mg daily x 5-7 days.",
                "black_box_warning": "Amoxicillin/Ampicillin: Triggers severe generalized maculopapular rash in >80-90% of mono patients; do not prescribe for viral pharyngitis.",
                "organ_clearance_cutoffs": "Monitor for mild reactive hepatitis; transaminases spontaneously normalize within 4-6 weeks without antiviral therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "JAMA Rational Clinical Exam Mono",
                "pmid_or_doi": "10.1001/jama.2016.2111",
                "cebm_level": 1,
                "sample_size": 1820,
                "endpoints": "Posterior cervical lymphadenopathy (LR+ 3.1) and atypical lymphocytosis >=10% (LR+ 26) have high diagnostic accuracy; sports avoidance prevents splenic rupture."
            }
        }
    },
    {
        "id": "DOC-CARD-299",
        "icd10": "M86.9",
        "condition": "Acute & Chronic Osteomyelitis",
        "specialty": "Infectious Disease & Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (OVIVA Trial) & IDSA Practice Guidelines",
        "citation": "Li HK et al. Oral versus Intravenous Antibiotics for Bone and Joint Infection (OVIVA). N Engl J Med. 2019;380(5):425-436.",
        "doi_or_source": "10.1056/NEJMoa1710926",
        "clinical_evidence": "Osteomyelitis is an infection of bone tissue, categorized by pathogenesis into hematogenous (predominantly prepubertal children and vertebral osteomyelitis in elderly), contiguous focus (post-trauma or orthopedic surgical fixation), and diabetic vascular insufficiency (diabetic foot osteomyelitis). Staphylococcus aureus (including MRSA) is the predominant pathogen (>50-70%). The definitive diagnostic standard is deep bone biopsy with microbiological culture and histopathology; superficial swab cultures are unreliable. In the landmark multicenter randomized noninferiority OVIVA trial (n=1054 patients with complex bone and joint infections), oral antibiotic therapy administered during the first 6 weeks was noninferior to standard intravenous antibiotic therapy with respect to definitive treatment failure at 1 year (13.2% oral vs 14.6% IV; difference -1.4 percentage points; 95% CI -5.6 to 2.9; p<0.001 for noninferiority). Oral therapy dramatically reduced central venous catheter complications (1.0% vs 9.4%; p<0.001) and hospital stay.",
        "solution_protocol": {
            "non_pharmacological_targets": "Thorough surgical debridement of all devitalized, necrotic bone (sequestrum) and infected hardware; dead-space management with antibiotic-impregnated polymethylmethacrylate (PMMA) beads; offloading diabetic foot ulcers with total contact casting; hyperbaric oxygen in refractory hypoxic bone.",
            "monitoring_cadence": "Serum C-reactive protein (CRP) and ESR weekly (monitoring biochemical response to therapy); repeat plain radiography or contrast-enhanced MRI at 6-12 weeks; blood glucose optimization (target HbA1c <7.5%).",
            "clinical_thresholds": "A positive 'probe-to-bone' test (palpation of hard, gritty bone with a sterile metallic probe through an open diabetic ulcer) has >90% positive predictive value for underlying osteomyelitis, mandating radiographic and antibiotic evaluation."
        },
        "patient_plain_language": "Osteomyelitis is a severe bacterial infection deep inside a bone. Bacteria can reach the bone through the bloodstream, from a deep puncture wound or open fracture, or by spreading inward from a chronic diabetic foot ulcer. The infection causes deep throbbing bone pain, swelling, fever, and drainage of pus. Treatment requires surgical cleaning of the dead bone tissue followed by several weeks of targeted antibiotic medication.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my deep bone biopsy culture identify the exact bacteria causing the infection and its antibiotic sensitivities?",
            "safety_question": "Based on the landmark OVIVA trial, can I safely take oral antibiotic pills instead of needing a central PICC line for intravenous antibiotics?",
            "action_threshold_question": "Has all the dead bone (sequestrum) been surgically removed so the antibiotics can successfully reach the healthy living bone?"
        },
        "red_flags": [
            "High fever with chills and worsening deep bone pain, pus draining from a surgical scar or skin ulcer, or bone visible through an open wound"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Osteomyelitis is an infection of the bone, caused by bacteria or fungi that travel through the bloodstream or spread from nearby tissue.",
                "plain_analogy": "A bacterial infection penetrating deep into the fortress walls of the bone, requiring deep cleaning and targeted antibiotics to eradicate.",
                "lifestyle_action": "Complete the entire 6-week course of antibiotics without missing doses. Keep diabetic foot ulcers completely offloaded."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Vancomycin IV", "Daptomycin", "Ciprofloxacin", "Rifampin (Adjunctive for biofilm)", "Levofloxacin"],
                "dosing_gdmt": "OVIVA Protocol: Transition to highly bioavailable oral antibiotics (e.g. Levofloxacin 750 mg daily + Rifampin 300-600 mg BID for staphylococcal hardware) for 6 weeks.",
                "black_box_warning": "Fluoroquinolones: Tendonitis, tendon rupture, and peripheral neuropathy; reserve for verified bacterial sensitivities.",
                "organ_clearance_cutoffs": "Monitor vancomycin AUC/MIC (target 400-600) and serum creatinine; monitor CPK weekly on daptomycin."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "OVIVA Trial",
                "pmid_or_doi": "10.1056/NEJMoa1710926",
                "cebm_level": 2,
                "sample_size": 1054,
                "endpoints": "Oral antibiotic therapy noninferior to IV therapy at 1 year (treatment failure 13.2% vs 14.6%); IV line complications dropped from 9.4% to 1.0%."
            }
        }
    },
    {
        "id": "DOC-CARD-300",
        "icd10": "A04.72",
        "condition": "Recurrent Clostridioides difficile Infection",
        "specialty": "Gastroenterology & Infectious Disease",
        "organ_system": "Digestive",
        "cebm_level": 2,
        "evidence_tier": "Level 2: Multicenter Phase 3 Randomized Controlled Trial",
        "source_body": "NEJM (PUNCH CD3 Trial & MODIFY I/II) & IDSA/SHEA Guidelines",
        "citation": "Khanna S et al. Efficacy and Safety of RBX2660 in Patients with Recurrent Clostridioides difficile Infection: Results from the PUNCH CD3 Phase 3 Randomized Clinical Trial. Drugs. 2022;82(15):1527-1538.",
        "doi_or_source": "10.1007/s40265-022-01797-x",
        "clinical_evidence": "Recurrent Clostridioides difficile Infection (rCDI) represents a major infectious disease challenge driven by persistent intestinal dysbiosis following broad-spectrum antibiotic exposure. The risk of subsequent recurrence rises exponentially from 25% after a first episode to 45% after a second, and >65% after two or more recurrences. In the pivotal Phase 3 PUNCH CD3 trial (n=267 patients with recurrent CDI), a single rectal dose of the fecal microbiota product fecal microbiota, live-jslm (Rebyota) achieved treatment success (absence of CDI diarrhea through 8 weeks) in 70.6% of patients compared with 57.5% with placebo (posterior probability of superiority 0.991). The oral microbiota pill Vowst (SER-109, ECOSPOR III trial) reduced recurrence rates at 8 weeks from 40% with placebo to 12% (relative risk 0.32; p<0.001). The monoclonal antibody bezlotoxumab (anti-toxin B, MODIFY trials) reduces recurrence by 38% (HR 0.62; p=0.0001). IDSA/SHEA guidelines establish oral fidaxomicin (200 mg BID for 10 days) as the preferred first-line antimicrobial over vancomycin due to lower recurrence rates (15% vs 25%).",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate cessation of the inciting broad-spectrum antibiotic whenever clinically feasible; avoid anti-motility agents (loperamide/diphenoxylate, which precipitate toxic megacolon); vigorous soap and water handwashing (alcohol-based hand rubs do NOT kill C. diff spores); contact isolation precautions.",
            "monitoring_cadence": "Clinical tracking of unformed bowel movements (target <=3 stools/day); repeat stool toxin testing is NOT recommended within 4 weeks of treatment to assess cure (spores and antigen remain detectable).",
            "clinical_thresholds": "Severe CDI (white blood cell count >=15,000/mcL or serum creatinine >1.5 mg/dL) or fulminant CDI (hypotension, ileus, megacolon) warrants oral Vancomycin 500 mg QID plus IV Metronidazole 500 mg TID and emergent surgical consultation."
        },
        "patient_plain_language": "Recurrent Clostridioides difficile (C. diff) infection is a bacterial bowel infection that causes severe, watery diarrhea, abdominal cramping, and fever. It usually happens after taking antibiotics for another infection. The antibiotics wipe out the beneficial, protective bacteria in your gut, allowing C. diff spores to hatch, multiply, and release toxins that inflame your colon. Once you have had C. diff, it has a high tendency to return, which is now treated with revolutionary microbiome-restoring therapies that repopulate your gut with healthy bacteria.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my stool test confirm active C. diff toxins (toxin A/B EIA or molecular PCR)?",
            "safety_question": "Am I receiving fidaxomicin (Dificid) or a tapered vancomycin regimen rather than standard short-course antibiotics to minimize recurrence?",
            "action_threshold_question": "Am I a candidate for an FDA-approved fecal microbiota restoration therapy (like Rebyota or oral Vowst pills) to restore my gut's healthy bacteria permanently?"
        },
        "red_flags": [
            "Severe rigid abdominal pain, sudden cessation of diarrhea accompanied by a ballooning distended belly (Toxic Megacolon emergency), high fever, or systolic BP <90 mmHg"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Clostridioides difficile is a bacterium that causes severe diarrhea and colitis, an inflammation of the colon.",
                "plain_analogy": "A weed taking over a garden lawn after weed-killer wiped out all the healthy grass; healthy microbial seeds are needed to crowd the weed back out.",
                "lifestyle_action": "Wash hands with soap and water (alcohol gels do not kill spores). Disinfect surfaces with bleach. Avoid unnecessary antibiotics."
            },
            "stack_2_openfda": {
                "approved_drugs": ["Fidaxomicin (Dificid)", "Fecal Microbiota (Rebyota / Vowst)", "Bezlotoxumab (Zinplava)", "Vancomycin Oral"],
                "dosing_gdmt": "First recurrence: Fidaxomicin 200 mg PO BID for 10 days. Second recurrence: Vancomycin taper followed by oral Vowst (SER-109) 4 capsules daily x 3 days.",
                "black_box_warning": "Bezlotoxumab: Increased incidence of heart failure exacerbations; reserve for patients without pre-existing congestive heart failure.",
                "organ_clearance_cutoffs": "Oral vancomycin and fidaxomicin act locally in the gut lumen with minimal systemic absorption; safe in renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PUNCH CD3 / ECOSPOR III",
                "pmid_or_doi": "10.1007/s40265-022-01797-x",
                "cebm_level": 2,
                "sample_size": 267,
                "endpoints": "Microbiota restoration (Rebyota / Vowst) reduces 8-week recurrence rate from 40% to 12% (p<0.001); long-term sustained cure >85%."
            }
        }
    }
]