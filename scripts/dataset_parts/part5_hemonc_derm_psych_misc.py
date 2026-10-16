"""
part5_hemonc_derm_psych_misc.py
"""

PART_5_DISEASES = [
    {
        "id": "DOC-CARD-181",
        "icd10": "D50.9",
        "condition": "Iron Deficiency Anemia (IDA)",
        "specialty": "Hematology",
        "organ_system": "Hemic & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AGA Clinical Practice Guideline on Iron Deficiency Anemia",
        "source_body": "Gastroenterology",
        "citation": "Ko CW et al. AGA Clinical Practice Guidelines on the Gastrointestinal Evaluation of Iron Deficiency Anemia. Gastroenterology. 2020;159(3):1085-1094.",
        "doi_or_source": "10.1053/j.gastro.2020.06.046",
        "clinical_evidence": "Iron deficiency anemia is the most common nutritional deficiency worldwide, defined by microcytic hypochromic red cell indices (MCV < 80 fL) with low body iron stores: serum ferritin < 30-45 ng/mL (in non-inflammatory states; ferritin < 100 ng/mL in inflammatory states) or transferrin saturation (TSAT) < 20%. In adult men and postmenopausal women, IDA is GI tract blood loss until proven otherwise; bidirectional endoscopy (EGD and colonoscopy) is strongly recommended by AGA guidelines to rule out occult gastrointestinal malignancy (detected in 10-15%). Oral iron supplementation (oral ferrous sulfate 65 mg elemental iron on alternate days) optimizes fractional iron absorption by limiting hepcidin surges. Intravenous iron formulations (ferric carboxymaltose, ferumoxytol, iron sucrose) are indicated for oral intolerance, malabsorption (celiac, IBD, bariatric surgery), third-trimester pregnancy, or heavy ongoing bleeding.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary enhancement with heme iron sources (lean red meat, poultry, fish); consume non-heme iron foods alongside ascorbic acid (vitamin C) to boost absorption; avoid drinking black tea or coffee with iron-rich meals (tannins inhibit absorption).",
            "monitoring_cadence": "Reticulocyte count at 7-10 days post-iron therapy; CBC (hemoglobin/hematocrit) at 4-8 weeks; repeat ferritin and TSAT at 3 months.",
            "clinical_thresholds": "Serum ferritin < 30-45 ng/mL is the most sensitive and specific threshold for depleted marrow iron stores."
        },
        "patient_plain_language": "Iron deficiency anemia occurs when your body does not have enough iron mineral to build hemoglobin, the iron-rich protein in red blood cells that carries oxygen to your muscles and brain. Without enough iron, you feel exhausted, look pale, become short of breath with stairs, and may crave chewing ice.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current ferritin, transferrin saturation, and hemoglobin level?",
            "safety_question": "If I am an adult male or postmenopausal woman, has a screening colonoscopy and upper endoscopy been scheduled to find where blood might be leaking?",
            "action_threshold_question": "Would every-other-day iron dosing or intravenous iron work better if daily pills cause severe constipation or stomach upset?"
        },
        "red_flags": [
            "Severe shortness of breath at rest, chest pain (angina triggered by severe anemia), dark black tarry stools, or hemoglobin dropping below 7 g/dL"
        ]
    },
    {
        "id": "DOC-CARD-182",
        "icd10": "D51.9",
        "condition": "Vitamin B12 Deficiency (Pernicious / Megaloblastic Anemia)",
        "specialty": "Hematology",
        "organ_system": "Hemic & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review / Clinical Practice Guideline",
        "source_body": "N Engl J Med",
        "citation": "Green R. Vitamin B12 deficiency from the perspective of a practicing hematologist. Blood. 2017;129(19):2603-2611. / Stabler SP. Vitamin B12 Deficiency. N Engl J Med. 2013;368(2):149-160.",
        "doi_or_source": "10.1056/NEJMcp1113996",
        "clinical_evidence": "Vitamin B12 (cobalamin) deficiency causes megaloblastic macrocytic anemia (MCV often > 100-110 fL) with hypersegmented neutrophils, and irreversible neuropsychiatric pathology (subacute combined degeneration of the spinal cord: bilateral peripheral neuropathy, loss of vibratory and position sense, spastic ataxia, and cognitive decline). Etiologies include autoimmune pernicious anemia (destruction of gastric parietal cells; anti-intrinsic factor antibodies), malabsorption (terminal ileal disease, Crohn's, bariatric resection), prolonged metformin or PPI use, and strict veganism. Serum B12 < 200 pg/mL confirms deficiency; borderline levels (200-350 pg/mL) require metabolic confirmation via elevated serum methylmalonic acid (MMA) and homocysteine (distinguishing B12 from folate deficiency, where MMA remains normal). Cochrane review shows oral high-dose cyanocobalamin (1,000-2,000 mcg daily) is as effective as intramuscular injections (1,000 mcg weekly then monthly) for hematologic recovery, though IM is preferred for severe neurologic impairment.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary incorporation of fortified nutritional yeast, dairy, eggs, or meat; daily oral supplementation for strict vegans; falls prevention physiotherapy for sensory ataxia.",
            "monitoring_cadence": "CBC and reticulocyte count at 1-2 weeks after initiating therapy; MMA and homocysteine normalization check at 2-3 months; annual surveillance EGD for pernicious anemia (high risk of gastric carcinoid and adenocarcinoma).",
            "clinical_thresholds": "Serum B12 < 200 pg/mL or MMA > 0.4 µmol/L confirms biochemical B12 deficiency."
        },
        "patient_plain_language": "Vitamin B12 deficiency is a shortage of a vital nutrient needed to produce healthy red blood cells and maintain the protective coating (myelin) around your nerves. Low B12 causes anemia as well as numbness, pins-and-needles tingling in your feet, clumsiness, and memory fog.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my serum B12 and methylmalonic acid (MMA) level?",
            "safety_question": "Was my intrinsic factor antibody tested to see if autoimmune pernicious anemia is preventing my stomach from absorbing B12?",
            "action_threshold_question": "Do I need high-dose intramuscular B12 injections right away to protect my spinal cord nerves from permanent damage?"
        },
        "red_flags": [
            "Rapid progressive numbness spreading up both legs, unsteady clumsy walking with frequent falls, severe confusion, or hallucinations"
        ]
    },
    {
        "id": "DOC-CARD-183",
        "icd10": "D69.3",
        "condition": "Immune Thrombocytopenia (ITP)",
        "specialty": "Hematology",
        "organ_system": "Hemic & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASH Clinical Practice Guidelines",
        "source_body": "Blood Adv",
        "citation": "Neunert C et al. American Society of Hematology 2019 guidelines for immune thrombocytopenia. Blood Adv. 2019;3(23):3829-3866.",
        "doi_or_source": "10.1182/bloodadvances.2019000966",
        "clinical_evidence": "Primary immune thrombocytopenia (ITP) is an acquired autoimmune disorder characterized by isolated thrombocytopenia (platelet count < 100 x 10⁹/L) caused by autoantibody-mediated platelet destruction (anti-GPIIb/IIIa) and impaired megakaryocyte thrombopoiesis, in the absence of other cytopenias or underlying disorders. Presentation ranges from asymptomatic bruising/petechiae to mucosal bleeding (epistaxis, gingival bleeding, menorrhagia) and catastrophic intracranial hemorrhage (1-2%). First-line therapy for platelets < 20-30 x 10⁹/L or active bleeding consists of oral corticosteroids: high-dose dexamethasone (40 mg daily for 4 days; achieves faster initial responses and higher sustained remission rates than prednisone) or prednisone (1 mg/kg/day for 1-2 weeks tapered). IVIG (1 g/kg single dose) rapidly raises platelets within 24-48 hours during emergency bleeding. Second-line therapies for persistent/chronic ITP include Thrombopoietin Receptor Agonists (TPO-RAs: romiplostim, eltrombopag, avatrombopag; sustained response >70-80%), rituximab, or laparoscopic splenectomy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid contact sports or high-impact activities while platelet count < 30-50 x 10⁹/L; avoid antiplatelet and anticoagulant medications (aspirin, NSAIDs); use soft-bristle toothbrush.",
            "monitoring_cadence": "CBC with platelet count weekly during induction, then every 1-3 months once stable; screening for underlying secondary ITP causes (H. pylori, HCV, HIV, ANA).",
            "clinical_thresholds": "Platelet count < 20-30 x 10⁹/L or significant mucosal bleeding warrants active medical intervention; target platelets > 50 x 10⁹/L for minor procedures and > 100 x 10⁹/L for neurosurgery."
        },
        "patient_plain_language": "Immune thrombocytopenia (ITP) is a condition where your immune system mistakenly creates antibodies that tag your blood-clotting cells (platelets) for removal in your spleen. With fewer platelets in your blood, you bruise very easily, develop tiny red pinpoint rash dots (petechiae), and bleed longer from small cuts.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact platelet count today, and have secondary causes like Hepatitis C, HIV, or H. pylori been ruled out?",
            "safety_question": "Why is short-course dexamethasone preferred over weeks of high-dose prednisone to avoid long-term steroid side effects?",
            "action_threshold_question": "At what specific platelet number (such as below 30,000) should we start treatment or escalate to a thrombopoietin receptor agonist (TPO-RA)?"
        },
        "red_flags": [
            "Sudden severe headache or visual changes (intracranial hemorrhage emergency), extensive mouth blood blisters ('wet purpura'), or heavy gastrointestinal bleeding"
        ]
    },
    {
        "id": "DOC-CARD-184",
        "icd10": "C90.00",
        "condition": "Multiple Myeloma",
        "specialty": "Hematology",
        "organ_system": "Hemic & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IMWG Consensus Criteria / GRIFFIN & MAIA Phase 3 RCTs",
        "source_body": "The Lancet",
        "citation": "Kumar SK et al. International Myeloma Working Group consensus criteria for the evaluation of response and minimal residual disease in multiple myeloma. Lancet Oncol. 2016;17(8):e328-e346. / Facon T et al. N Engl J Med. 2019;380(22):2104-2115.",
        "doi_or_source": "10.1056/NEJMoa1817249",
        "clinical_evidence": "Multiple myeloma is a clonal plasma cell malignancy characterized by bone marrow plasmacytosis (≥10%) and the presence of CRAB criteria (Hypercalcemia > 11 mg/dL, Renal insufficiency [creatinine > 2 mg/dL or CrCl < 40], Anemia [Hb < 10 g/dL], Bone lytic lesions) or myeloma-defining biomarkers (SLiM: ≥60% clonal marrow plasma cells, serum involved/uninvolved free light chain ratio ≥ 100, >1 focal MRI bone lesion). Workup requires serum/urine protein electrophoresis with immunofixation (SPEP/UPEP/IFE), serum free light chains (sFLC), and whole-body low-dose CT or PET-CT. Triplet and quadruplet induction regimens incorporating the anti-CD38 monoclonal antibody daratumumab, proteasome inhibitor bortezomib, immunomodulatory drug lenalidomide, and dexamethasone (Dara-VRd or Dara-Rd) produce deep responses and unprecedented progression-free survival (MAIA and GRIFFIN trials). Autologous stem cell transplant (ASCT) remains standard for eligible patients, followed by lenalidomide maintenance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Generous daily hydration (≥ 2-3 liters/day) to prevent renal tubular light-chain cast nephropathy; avoid all NSAIDs; bone protection with zoledronic acid or denosumab plus weight-bearing exercises to reduce pathological fractures.",
            "monitoring_cadence": "Monthly SPEP, UPEP, and serum free light chains during therapy; CBC, creatinine, and calcium every 2-4 weeks; skeletal surveys/PET-CT annually.",
            "clinical_thresholds": "M-protein disappearance plus negative immunofixation and marrow flow cytometry with <1 clonal cell per 100,000 cells defines Minimal Residual Disease (MRD) negativity (10⁻⁵)."
        },
        "patient_plain_language": "Multiple myeloma is a cancer of the plasma cells, which are the white blood cells that make antibodies. When abnormal plasma cells multiply uncontrollably inside your bone marrow, they crowd out healthy blood cells, dissolve weak holes in bones, and produce abnormal proteins that can damage your kidneys.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current M-spike on protein electrophoresis and my serum free light chain kappa/lambda ratio?",
            "safety_question": "Am I receiving a monthly bone-strengthening medication (like zoledronic acid) and blood clot prevention while on my myeloma medications?",
            "action_threshold_question": "Based on my age and general health, am I a candidate for an autologous stem cell transplant after induction chemotherapy?"
        },
        "red_flags": [
            "Sudden severe back pain with leg weakness or numbness (spinal cord compression emergency), sudden confusion from high calcium, or acute drop in urine output"
        ]
    },
    {
        "id": "DOC-CARD-185",
        "icd10": "C91.10",
        "condition": "Chronic Lymphocytic Leukemia (CLL)",
        "specialty": "Hematology",
        "organ_system": "Hemic & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NCCN Guidelines / ELEVATE-TN & RESONATE Phase 3 RCTs",
        "source_body": "The Lancet (ELEVATE-TN)",
        "citation": "Sharman JP et al. Acalabrutinib with or without obinutuzumab versus chlorambucil and obinutuzumab for treatment-naive chronic lymphocytic leukaemia (ELEVATE TN). Lancet. 2020;395(10232):1278-1291.",
        "doi_or_source": "10.1016/S0140-6736(20)30262-2",
        "clinical_evidence": "Chronic lymphocytic leukemia is the most prevalent adult leukemia in Western countries, defined by persistent clonal B-cell lymphocytosis in peripheral blood (≥ 5 x 10⁹/L) co-expressing CD5, CD19, CD20 (dim), and CD23 on flow cytometry. Staged via Rai (0 to IV) or Binet (A to C) systems. Asymptomatic early-stage disease (Rai 0, Binet A) managed with active surveillance ('watch and wait'), as randomized trials showed early chemotherapy does not improve overall survival. Treatment indications (iwCLL criteria): constitutional 'B' symptoms, progressive bone marrow failure, massive splenomegaly, or lymphocyte doubling time < 6 months. Targeted front-line oral therapies targeting Bruton tyrosine kinase (BTK inhibitors: acalabrutinib, zanubrutinib) or BCL-2 (venetoclax combined with anti-CD20 antibody obinutuzumab) have completely displaced traditional chemoimmunotherapy (FCR), achieving superior progression-free survival even in high-risk TP53-mutated or del(17p) disease.",
        "solution_protocol": {
            "non_pharmacological_targets": "Universal annual influenza, pneumococcal (PCV20), and recombinant zoster (Shingrix) vaccinations (avoid live-attenuated vaccines due to humoral immune defect); sun protection and annual full-body dermatologic exams (8-fold increased skin cancer risk).",
            "monitoring_cadence": "CBC, differential, and clinical examination of lymph nodes, liver, and spleen every 3 months for active disease or every 6-12 months during observation; FISH for del(17p), TP53 mutation, and IGHV mutation status prior to initiating therapy.",
            "clinical_thresholds": "Lymphocyte count doubling time < 6 months, platelets < 100 x 10⁹/L, or hemoglobin < 10 g/dL meets iwCLL treatment criteria."
        },
        "patient_plain_language": "Chronic lymphocytic leukemia (CLL) is a slow-growing cancer of the blood and bone marrow involving white blood cells called B-lymphocytes. In its early stages, it often causes no symptoms and is found on routine blood tests; many people live normal active lives for years under careful monitoring without ever needing chemotherapy.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current absolute lymphocyte count, hemoglobin, and platelet count?",
            "safety_question": "Why is the evidence-based 'watch and wait' approach the safest strategy for me right now rather than starting treatment immediately?",
            "action_threshold_question": "What are my genetic risk markers, such as IGHV mutation status and TP53/del(17p), to determine the best modern targeted pill if treatment is ever needed?"
        },
        "red_flags": [
            "Rapid asymmetrical enlargement of a single lymph node mass with high fevers and weight loss (Richter transformation into high-grade lymphoma), or severe recurrent bacterial infections"
        ]
    },
    {
        "id": "DOC-CARD-186",
        "icd10": "D45",
        "condition": "Polycythemia Vera (PV)",
        "specialty": "Hematology",
        "organ_system": "Hemic & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WHO Classification / CYTO-PV Phase 3 RCT",
        "source_body": "N Engl J Med",
        "citation": "Marchioli R et al. Cardiovascular events and intensity of treatment in polycythemia vera (CYTO-PV). N Engl J Med. 2013;368(1):22-33.",
        "doi_or_source": "10.1056/NEJMoa1208500",
        "clinical_evidence": "Polycythemia vera is a Philadelphia-chromosome-negative myeloproliferative neoplasm characterized by autonomous erythrocytosis, driving hyperviscosity and major thrombotic complications (arterial and venous, including Budd-Chiari and portal vein thrombosis). >98% of patients harbor the activating JAK2 V617F or exon 12 driver mutation. Diagnostic criteria require: elevated hemoglobin/hematocrit (>16.5 g/dL / 49% in men; >16.0 g/dL / 48% in women), hypercellular bone marrow with trilineage panmyelosis, JAK2 mutation, and subnormal serum erythropoietin (EPO). Landmark CYTO-PV trial proved that strict hematocrit maintenance < 45% reduced cardiovascular death and major thrombosis fourfold compared to a 45-50% target (HR 3.91, 95% CI 1.45-10.53, p=0.007). All patients receive low-dose aspirin (81-100 mg daily; ECLAP trial). High-risk patients (age ≥60 or prior thrombosis) require cytoreductive therapy (hydroxyurea or ropeginterferon alfa-2b; ruxolitinib in refractory cases). Aquagenic pruritus (itching triggered by warm showers) is a hallmark symptom.",
        "solution_protocol": {
            "non_pharmacological_targets": "Therapeutic phlebotomy (removal of 450-500 mL blood) to maintain hematocrit strictly < 45%; avoidance of iron supplementation (relative iron deficiency is therapeutically desired to slow red cell manufacturing); smoking cessation; manage aquagenic pruritus with lower shower temperatures and antihistamines.",
            "monitoring_cadence": "CBC with hematocrit every 2-4 weeks during phlebotomy induction, then every 2-3 months once stabilized; annual abdominal ultrasound to assess spleen size.",
            "clinical_thresholds": "Target hematocrit strictly < 45.0% in all patients to prevent fatal thrombotic events."
        },
        "patient_plain_language": "Polycythemia vera is a rare chronic bone marrow condition where a gene mutation instructs your marrow factories to produce far too many red blood cells. The extra cells make your blood unusually thick and sluggish, like motor oil in winter, increasing the danger of blood clots.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my exact hematocrit percentage today, and is it safely below the critical 45% ceiling?",
            "safety_question": "Am I on daily low-dose aspirin to prevent blood clots, and have I been cautioned never to take iron vitamin pills?",
            "action_threshold_question": "Based on my age and clot history, do I need a cytoreductive pill like hydroxyurea in addition to therapeutic blood donation (phlebotomy)?"
        },
        "red_flags": [
            "Sudden severe abdominal pain with abdominal swelling (hepatic vein thrombosis / Budd-Chiari syndrome), sudden leg swelling/pain (DVT), or acute stroke warning signs"
        ]
    },
    {
        "id": "DOC-CARD-187",
        "icd10": "L71.9",
        "condition": "Rosacea",
        "specialty": "Dermatology",
        "organ_system": "Integumentary & Skin",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review / Expert Consensus",
        "source_body": "Cochrane Database Syst Rev",
        "citation": "van Zuuren EJ et al. Interventions for rosacea. Cochrane Database Syst Rev. 2015;(4):CD003262. / Schaller M et al. Br J Dermatol. 2017;176(2):431-438.",
        "doi_or_source": "10.1002/14651858.CD003262.pub5",
        "clinical_evidence": "Rosacea is a chronic inflammatory centrofacial dermatosis characterized by neurovascular dysregulation and innate immune hyperreactivity (cathelicidin LL-37 processing by kallikrein 5, Demodex folliculorum mite hypersensitivity). Phenotypes include: Erythematotelangiectatic (persistent centrofacial erythema, flushing, telangiectasias), Papulopustular (dome-shaped red papules and pustules without comedones, distinguishing it from acne vulgaris), Phymatous (sebaceous hyperplasia, rhinophyma), and Ocular rosacea (blepharitis, conjunctivitis, burning/grittiness; present in >50%). First-line topical therapies for papulopustular rosacea: ivermectin 1% cream (superior to metronidazole; anti-parasitic against Demodex and anti-inflammatory), azelaic acid 15% gel, or metronidazole 0.75-1%. Subantimicrobial-dose oral doxycycline (40 mg modified-release daily; anti-inflammatory without antibacterial resistance) is indicated for moderate-to-severe disease. Persistent facial erythema responds to topical alpha-agonists (brimonidine 0.33%, oxymetazoline 1%) or vascular pulsed-dye laser (PDL).",
        "solution_protocol": {
            "non_pharmacological_targets": "Identify and avoid individual flushing triggers: hot beverages, spicy foods, alcohol (especially red wine), extreme temperatures, emotional stress; daily mineral broad-spectrum sunscreen (zinc oxide/titanium dioxide SPF 30+); gentle soap-free facial cleansers.",
            "monitoring_cadence": "Clinical reassessment of inflammatory lesion counts and erythema grade at 8-12 weeks; ophthalmology evaluation if ocular symptoms (grittiness, photophobia, chalazia) are present.",
            "clinical_thresholds": "Presence of inflammatory papules and pustules without comedones confirms papulopustular rosacea."
        },
        "patient_plain_language": "Rosacea is a chronic skin condition causing persistent facial redness, flushing, and small acne-like bumps across your nose, cheeks, and forehead. Unlike teenage acne, there are no blackheads, and flare-ups are often triggered by sun, heat, spicy foods, or hot coffee.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my skin examination show primarily redness and visible veins, or active inflammatory bumps?",
            "safety_question": "Would a topical prescription like ivermectin (Soolantra) or low-dose anti-inflammatory doxycycline clear my bumps with fewer side effects?",
            "action_threshold_question": "Are my dry, irritated eyes related to ocular rosacea, and do I need specialized eyelid hygiene or eye drops?"
        },
        "red_flags": [
            "Severe eye pain, intense photophobia (light sensitivity), or corneal clouding indicating severe ocular rosacea with risk of corneal ulceration"
        ]
    },
    {
        "id": "DOC-CARD-188",
        "icd10": "L63.9",
        "condition": "Alopecia Areata",
        "specialty": "Dermatology",
        "organ_system": "Integumentary & Skin",
        "cebm_level": 1,
        "evidence_tier": "Level 1: BRAVE-AA1 & BRAVE-AA2 Phase 3 RCTs",
        "source_body": "N Engl J Med",
        "citation": "King B et al. Two Phase 3 Trials of Baricitinib for Alopecia Areata (BRAVE-AA1 and BRAVE-AA2). N Engl J Med. 2022;386(18):1687-1699.",
        "doi_or_source": "10.1056/NEJMoa2110343",
        "clinical_evidence": "Alopecia areata is an autoimmune condition caused by collapse of immune privilege in anagen hair follicles, mediated by CD8+ NKG2D+ T-cell infiltration and IFN-gamma/IL-15 signaling. Classic presentation is sudden onset of well-circumscribed, smooth, circular patches of non-scarring hair loss on the scalp or beard, showing pathognomonic exclamation-mark hairs and yellow/black dots on dermoscopy (trichoscopy). May progress to alopecia totalis (entire scalp) or alopecia universalis (complete body hair loss). Severity of Alopecia Tool (SALT) scores extent of hair loss. For limited patchy disease (SALT < 20-30%), first-line therapy is intralesional corticosteroid injections (triamcinolone acetonide 2.5-5 mg/mL into the dermis every 4-6 weeks) or potent topical corticosteroids. Landmark BRAVE-AA1 and BRAVE-AA2 phase 3 trials established oral Janus kinase (JAK) inhibitors (baricitinib 2-4 mg daily; ritlecitinib 50 mg daily) as breakthrough FDA-approved therapies for severe disease (SALT score ≥ 50), producing significant scalp hair regrowth (SALT score ≤ 20 achieved in ~35-40% of patients vs 3-5% placebo at 36 weeks).",
        "solution_protocol": {
            "non_pharmacological_targets": "Psychosocial counseling and peer support groups (high burden of anxiety and depression); scalp sun protection (broad-spectrum sunscreen SPF 50+, hats/scarves); gentle hair care.",
            "monitoring_cadence": "SALT score tracking every 3 months; pre-treatment screening for latent TB, viral hepatitis, CBC, lipids, and liver/renal function prior to initiating oral JAK inhibitors.",
            "clinical_thresholds": "SALT score ≥ 50 (≥50% scalp hair loss) or rapidly progressive widespread disease qualifies for systemic oral JAK inhibitor therapy."
        },
        "patient_plain_language": "Alopecia areata is an autoimmune condition where your body's immune cells mistakenly attack the roots of your hair follicles, causing them to suddenly drop into a resting phase. This results in smooth, round, coin-shaped bald spots on your scalp or beard without any skin scarring.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current SALT score (percentage of scalp hair loss)?",
            "safety_question": "Would tiny in-office cortisone injections directly into the bald spots help wake up the hair roots faster for my patchy spots?",
            "action_threshold_question": "If my hair loss is widespread, am I a candidate for the newer oral JAK inhibitor pills (like baricitinib or ritlecitinib)?"
        },
        "red_flags": [
            "Severe clinical signs of depression, social isolation, or suicidal ideation resulting from the acute cosmetic and emotional impact of hair loss"
        ]
    },
    {
        "id": "DOC-CARD-189",
        "icd10": "L73.2",
        "condition": "Hidradenitis Suppurativa",
        "specialty": "Dermatology",
        "organ_system": "Integumentary & Skin",
        "cebm_level": 1,
        "evidence_tier": "Level 1: PIONEER I/II & SUNSHINE/SUNRISE Phase 3 RCTs",
        "source_body": "The Lancet",
        "citation": "Kimball AB et al. Two Phase 3 Trials of Adalimumab for Hidradenitis Suppurativa (PIONEER I and II). N Engl J Med. 2016;375(5):422-434. / Kimball AB et al. Secukinumab in moderate-to-severe hidradenitis suppurativa (SUNSHINE and SUNRISE). Lancet. 2023;401(10378):747-761.",
        "doi_or_source": "10.1016/S0140-6736(23)00022-3",
        "clinical_evidence": "Hidradenitis suppurativa (HS) is a chronic, painful, inflammatory follicular occlusion disorder predominantly affecting apocrine gland-bearing intertriginous skin (axillae, inguinal, perineal, inframammary regions). Manifests as recurrent painful inflammatory nodules, sterile abscesses, discharging epithelialized sinus tracts (tunnels), and dense bridged scarring. Staged using Hurley classification: Stage I (isolated nodules/abscesses, no sinus tracts), Stage II (recurrent abscesses with sinus tracts and scarring, separated), Stage III (diffuse coalescent tracts and interconnected abscesses across an entire anatomic area). Medical therapy: Topical clindamycin 1% for mild Hurley I; oral combination antibiotics (clindamycin 300 mg BID + rifampin 300 mg BID for 10-12 weeks) for Hurley II flares. Pivotal Phase 3 trials demonstrated that biological therapy targeting TNF (adalimumab 40 mg weekly, PIONEER trials) or IL-17A (secukinumab 300 mg every 2-4 weeks, SUNSHINE/SUNRISE trials) significantly achieves HiSCR (Hidradenitis Suppurativa Clinical Response: ≥50% reduction in inflammatory nodules without abscess increase). Deroofing or wide surgical excision is required for established chronic epithelialized tunnels.",
        "solution_protocol": {
            "non_pharmacological_targets": "Smoking cessation (smoking is the strongest modifiable risk factor, present in >80%); structured weight management (friction reduction); wear loose-fitting breathable cotton clothing; antiseptic washes (chlorhexidine or benzoyl peroxide wash); wound care dressings.",
            "monitoring_cadence": "HiSCR and International Hidradenitis Suppurativa Severity Score (IHS4) calculated at baseline and every 12 weeks of biological therapy; pain visual analog scale (VAS); annual screening for metabolic syndrome and depression.",
            "clinical_thresholds": "Moderate-to-severe disease (Hurley Stage II/III or IHS4 > 3) failing oral antibiotics indicates initiation of targeted biological therapy (adalimumab or secukinumab)."
        },
        "patient_plain_language": "Hidradenitis suppurativa is a painful, chronic inflammatory skin condition where clogged hair follicles in sensitive sweat-prone areas—like your armpits, groin, and under breasts—turn into deep, tender boils that can rupture, drain, and form under-the-skin tunnels.",
        "doctor_consultation_checklist": {
            "parameter_question": "What Hurley stage is my condition, and how many active inflammatory nodules and draining tunnels do I have?",
            "safety_question": "Why should painful chronic tunnels undergo surgical 'deroofing' or excision rather than repetitive incisions that lead to worse scarring?",
            "action_threshold_question": "Am I a candidate for FDA-approved biologic injections (like Humira or Cosentyx) to stop new boils from forming?"
        },
        "red_flags": [
            "Severe rapidly spreading surrounding erythema with high fever and chills (secondary systemic cellulitis/bacteremia), or chronic non-healing ulcerating wounds"
        ]
    },
    {
        "id": "DOC-CARD-190",
        "icd10": "L80",
        "condition": "Vitiligo",
        "specialty": "Dermatology",
        "organ_system": "Integumentary & Skin",
        "cebm_level": 1,
        "evidence_tier": "Level 1: TRuE-V1 & TRuE-V2 Phase 3 RCTs",
        "source_body": "N Engl J Med",
        "citation": "Rosmarin D et al. Two Phase 3 Trials of Ruxolitinib Cream for Vitiligo (TRuE-V1 and TRuE-V2). N Engl J Med. 2022;387(16):1445-1455.",
        "doi_or_source": "10.1056/NEJMoa2118828",
        "clinical_evidence": "Vitiligo is an acquired autoimmune depigmenting disorder characterized by progressive destruction of epidermal melanocytes, mediated by autoreactive CD8+ cytotoxic T cells driven by IFN-gamma and JAK1/JAK2 signaling. Clinically presents as well-demarcated, amelanotic milky-white macules and patches without epidermal atrophy or scale, exhibiting bright blue-white fluorescence under Wood's lamp. Segmental (unilateral, dermatomal) vs Non-segmental (bilateral, symmetric; ~90% of cases). Koebner phenomenon (depigmentation at sites of cutaneous friction/trauma) indicates active disease. The landmark TRuE-V1 and TRuE-V2 randomized phase 3 trials established the topical JAK inhibitor ruxolitinib 1.5% cream (applied twice daily) as the first FDA-approved disease-directed therapy for non-segmental vitiligo in patients ≥ 12 years, achieving ≥75% improvement in Facial Vitiligo Area Scoring Index (F-VASI75) in ~30% of patients at 24 weeks and ~50% at 52 weeks. Narrowband ultraviolet B (NB-UVB) phototherapy (2-3 times/week) synergizes with medical therapy to stimulate melanocyte stem cell migration from hair follicles.",
        "solution_protocol": {
            "non_pharmacological_targets": "Meticulous sun protection of depigmented patches (broad-spectrum SPF 50+; depigmented skin has zero melanin and burns easily, triggering Koebner phenomenon); avoid tight abrasive clothing and repetitive friction; cosmetic camouflage creams.",
            "monitoring_cadence": "F-VASI and Total VASI score assessment at 3, 6, and 12 months; annual screening for associated autoimmune conditions (serum TSH, free T4, anti-TPO antibodies; Hashimoto thyroiditis occurs in 15-25%).",
            "clinical_thresholds": "F-VASI75 response (≥75% repigmentation of facial vitiligo) indicates optimal therapeutic milestone."
        },
        "patient_plain_language": "Vitiligo is an autoimmune condition where your body's immune defense system attacks its own pigment-producing cells (melanocytes) in your skin. This causes smooth, chalk-white patches to appear on your hands, face, or body where pigment has been lost.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current VASI score, and are my vitiligo patches currently stable or actively spreading?",
            "safety_question": "Have my thyroid levels (TSH and thyroid antibodies) been checked, given how frequently vitiligo overlaps with thyroid conditions?",
            "action_threshold_question": "Can I start topical ruxolitinib (Opzelura) cream combined with narrowband UVB light therapy to bring back color to my skin?"
        },
        "red_flags": [
            "Severe sunburn on depigmented skin patches, or signs of associated autoimmune polyglandular syndromes (severe lethargy, postural syncope, hyperpigmentation elsewhere)"
        ]
    },
    {
        "id": "DOC-CARD-191",
        "icd10": "F42.9",
        "condition": "Obsessive-Compulsive Disorder (OCD)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: APA Practice Guideline / Cochrane Systematic Review",
        "source_body": "Am J Psychiatry",
        "citation": "Koran LM et al. Practice Guideline for the Treatment of Patients With Obsessive-Compulsive Disorder. Am J Psychiatry. 2007;164(7 Suppl):5-53. / Skapinakis P et al. Lancet Psychiatry. 2016;3(8):730-739.",
        "doi_or_source": "10.1016/S2215-0366(16)30069-4",
        "clinical_evidence": "Obsessive-compulsive disorder is characterized by recurrent, persistent, intrusive, and distressing thoughts, urges, or images (obsessions) and/or repetitive physical behaviors or mental acts (compulsions) that the individual feels driven to perform to reduce anxiety, consuming > 1 hour/day or causing clinically significant distress. Cortico-striato-thalamo-cortical (CSTC) circuit hyperactivity underlies pathophysiology. First-line evidence-based psychotherapeutic treatment is specialized Cognitive Behavioral Therapy incorporating Exposure and Response Prevention (ERP; effect size g=1.39). First-line pharmacotherapy mandates high-dose selective serotonin reuptake inhibitors (SSRIs: fluoxetine 60-80 mg, sertraline 200 mg, escitalopram 20-40 mg, or fluvoxamine 200-300 mg daily), requiring higher doses and longer trial durations (10-12 weeks at maximum tolerated dose) than required for major depressive disorder. Clomipramine (tricyclic with potent serotonin reuptake inhibition) is second-line; augmentation with atypical antipsychotics (aripiprazole 5-10 mg, risperidone 1-2 mg) improves refractory cases.",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured Exposure and Response Prevention (ERP) behavioral therapy homework (facing feared triggers hierarchically while voluntarily refraining from ritualistic compulsions); family accommodation reduction.",
            "monitoring_cadence": "Yale-Brown Obsessive Compulsive Scale (Y-BOCS) tracking every 4 weeks; clinical evaluation at 8-12 weeks before declaring an SSRI trial ineffective.",
            "clinical_thresholds": "Y-BOCS score reduction ≥ 35% defines full clinical response; Y-BOCS ≤ 12 indicates clinical remission."
        },
        "patient_plain_language": "OCD is a mental health condition where your brain gets stuck on distressing, intrusive thoughts, doubts, or fears (obsessions). To quiet the intense anxiety, you feel an overwhelming urge to perform repetitive routines, checks, or mental rituals (compulsions), which only temporarily relieves the anxiety before the cycle repeats.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current Yale-Brown Obsessive Compulsive Scale (Y-BOCS) baseline score?",
            "safety_question": "Can I be connected with a therapist trained specifically in Exposure and Response Prevention (ERP), the gold-standard therapy for OCD?",
            "action_threshold_question": "Are we aware that OCD requires higher doses of SSRI medications and up to 10 to 12 weeks to see significant improvement?"
        },
        "red_flags": [
            "Severe compulsions occupying >8 hours/day resulting in severe skin breakdown (bleeding hands from washing), malnutrition, or active suicidal ideation"
        ]
    },
    {
        "id": "DOC-CARD-192",
        "icd10": "F41.0",
        "condition": "Panic Disorder",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review / APA Practice Guideline",
        "source_body": "Cochrane Database Syst Rev",
        "citation": "Bighelli I et al. Psychological therapies versus pharmacological interventions for panic disorder with or without agoraphobia in adults. Cochrane Database Syst Rev. 2018;(4):CD011504.",
        "doi_or_source": "10.1002/14651858.CD011504.pub2",
        "clinical_evidence": "Panic disorder is characterized by recurrent, unexpected panic attacks—abrupt surges of intense fear or intense discomfort reaching a peak within minutes, accompanied by ≥ 4 somatic and cognitive symptoms (palpitations, sweating, trembling, dyspnea, choking sensation, chest pain, nausea, dizziness, chills/heat sensations, paresthesias, derealization/depersonalization, fear of losing control, fear of dying)—followed by ≥ 1 month of persistent concern about additional attacks or maladaptive behavioral changes (avoidance). First-line treatment consists of Cognitive Behavioral Therapy (CBT with interoceptive exposure to panic-related sensations) or SSRIs/SNRIs (sertraline, paroxetine, citalopram, venlafaxine). SSRIs should be initiated at half standard starting doses (e.g., sertraline 25 mg) because panic disorder patients exhibit heightened sensitivity to initial jitteriness/anxiety. Benzodiazepines provide rapid acute relief but carry risks of physical dependence, tolerance, cognitive blunting, and increased relapse rates upon discontinuation, and are not recommended for long-term maintenance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Interoceptive exposure exercises in CBT (spinning in chair, hyperventilating, breathing through straw to extinguish conditioned somatic fear); diaphragmatic slow breathing (4 seconds in, 6 seconds out); elimination of caffeine and energy drinks; regular aerobic exercise.",
            "monitoring_cadence": "Panic Disorder Severity Scale (PDSS) every 2-4 weeks; clinical reassessment of agoraphobic avoidance patterns; reassess at 6-8 weeks for SSRI dose titration.",
            "clinical_thresholds": "PDSS score reduction ≥ 40% represents significant clinical response; PDSS ≤ 3 indicates remission."
        },
        "patient_plain_language": "Panic disorder is a condition where your body's 'fight-or-flight' alarm system misfires without any real danger, flooding your system with adrenaline. Within minutes, your heart pounds, your chest tightens, and you feel dizzy and terrified that you are having a heart attack or losing your mind.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have medical tests (such as a 12-lead ECG and thyroid panel) verified that my heart and thyroid are completely normal?",
            "safety_question": "Why should my daily antidepressant medication start at a low dose to prevent an initial temporary spike in jitteriness?",
            "action_threshold_question": "Can I learn CBT interoceptive exposure techniques to train my brain that normal bodily sensations like a fast heartbeat are not dangerous?"
        },
        "red_flags": [
            "Severe agoraphobia causing complete inability to leave home, concurrent major depression with active suicidal thoughts, or escalating high-dose benzodiazepine abuse"
        ]
    },
    {
        "id": "DOC-CARD-193",
        "icd10": "F40.10",
        "condition": "Social Anxiety Disorder (Social Phobia)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NICE Clinical Guideline 159 / Lancet Network Meta-Analysis",
        "source_body": "The Lancet Psychiatry",
        "citation": "Mayo-Wilson E et al. Psychological and pharmacological interventions for social anxiety disorder in adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2014;1(5):368-376.",
        "doi_or_source": "10.1016/S2215-0366(14)70329-3",
        "clinical_evidence": "Social anxiety disorder is characterized by marked, persistent fear or anxiety about one or more social situations in which the individual is exposed to possible scrutiny by others (social interactions, being observed eating/drinking, performing in front of others), fearing negative evaluation, embarrassment, or humiliation. The largest comprehensive network meta-analysis (Lancet Psychiatry, 101 trials, 13,164 participants) demonstrated that individual Cognitive Behavioral Therapy (CBT based on the Clark and Wells or Heimberg models with video feedback and behavioral experiments) has the largest effect size and longest-lasting benefits. First-line pharmacotherapy for generalized social anxiety disorder is SSRIs (sertraline 50-200 mg, paroxetine 20-50 mg, escitalopram 10-20 mg) or SNRIs (venlafaxine XR 75-225 mg). For discrete performance-only social anxiety (e.g., public speaking, musical performances), as-needed non-selective beta-blockers (propranolol 10-40 mg orally taken 30-60 minutes before the event) effectively suppress peripheral autonomic somatic symptoms (tremors, tachycardia, voice shaking) without cognitive sedation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Individual CBT incorporating video feedback and behavioral experiments (testing catastrophic predictions about social blunders); gradual social exposure hierarchies; eliminating 'safety behaviors' (avoiding eye contact, rehearsing phrases, hiding face).",
            "monitoring_cadence": "Liebowitz Social Anxiety Scale (LSAS) monitoring every 4-6 weeks; assessment of alcohol use at every visit (high risk of self-medicating social anxiety).",
            "clinical_thresholds": "LSAS score reduction ≥ 30% indicates treatment response; LSAS ≤ 30 indicates minimal social anxiety symptoms."
        },
        "patient_plain_language": "Social anxiety disorder is far more intense than ordinary shyness. It is an intense, paralyzing fear of being watched, judged, scrutinized, or embarrassed in social or performance situations, causing sweating, trembling, blushing, and leading people to avoid conversations, meetings, or public speaking.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my baseline score on the Liebowitz Social Anxiety Scale (LSAS)?",
            "safety_question": "Can I use an as-needed beta-blocker like propranolol before public speaking to stop my physical trembling and heart racing without feeling sedated?",
            "action_threshold_question": "Can I receive individual Cognitive Behavioral Therapy focused specifically on challenging catastrophic social fears and dropping safety behaviors?"
        },
        "red_flags": [
            "Severe social withdrawal leading to functional disability, dropping out of school/work, or comorbid severe alcohol dependence used for social self-medication"
        ]
    },
    {
        "id": "DOC-CARD-194",
        "icd10": "F10.20",
        "condition": "Alcohol Use Disorder (AUD)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: APA Practice Guideline for the Pharmacological Treatment of AUD",
        "source_body": "Am J Psychiatry",
        "citation": "Reus VI et al. The American Psychiatric Association Practice Guideline for the Pharmacological Treatment of Patients With Alcohol Use Disorder. Am J Psychiatry. 2018;175(1):86-90.",
        "doi_or_source": "10.1176/appi.ajp.2017.1750101",
        "clinical_evidence": "Diagnostic criteria (DSM-5) require ≥ 2 of 11 criteria over a 12-month period, categorized into mild (2-3), moderate (4-5), and severe (≥6 criteria: tolerance, withdrawal, craving, inability to cut down, spending excess time obtaining/using, neglecting social/occupational roles). Acute alcohol withdrawal is managed with protocolized symptom-triggered benzodiazepines (CIWA-Ar protocol). First-line FDA-approved pharmacotherapies for maintaining abstinence and reducing heavy drinking days: Oral naltrexone (50 mg daily) or once-monthly extended-release injectable naltrexone (Vivitrol 380 mg IM; opioid receptor antagonist reducing the dopamine-mediated reinforcing reward of alcohol; Cochrane review confirms 28% reduction in heavy drinking days; contraindicated in patients taking opioid analgesics or in acute hepatitis/liver failure); and Acamprosate (666 mg TID; modulates NMDA glutamate neurotransmission, ideal for maintaining abstinence in patients with liver disease; cleared renally, contraindicated if CrCl < 30 mL/min). Disulfiram is second-line. Combining pharmacotherapy with evidence-based psychosocial interventions (Motivational Interviewing, CBT, Twelve-Step Facilitation) optimizes recovery outcomes.",
        "solution_protocol": {
            "non_pharmacological_targets": "Participation in mutual-help support groups (Alcoholics Anonymous, SMART Recovery); structured Motivational Enhancement Therapy or CBT; complete household removal of all alcohol; identify and manage relapse triggers (HALT: Hungry, Angry, Lonely, Tired).",
            "monitoring_cadence": "AUDIT-C score, timeline followback drinking days, liver function tests (AST, ALT, GGT), and MCV at 1, 3, 6, and 12 months; renal function panel prior to acamprosate.",
            "clinical_thresholds": "CIWA-Ar score > 8 indicates need for protocolized symptom-triggered benzodiazepines; CIWA-Ar > 15 warrants inpatient medical detoxification."
        },
        "patient_plain_language": "Alcohol use disorder is a chronic medical brain disease where changes in brain chemistry make it extremely difficult to control or stop drinking alcohol despite harm to your health, relationships, or career. It is a treatable condition, and modern medications can significantly reduce cravings.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were my liver function tests (AST, ALT, GGT) and platelet counts?",
            "safety_question": "Would a daily anti-craving pill like naltrexone or acamprosate help quiet my thoughts about drinking alcohol?",
            "action_threshold_question": "If I stop drinking cold turkey, do I require a medically supervised detox protocol to prevent dangerous withdrawal seizures or delirium tremens?"
        },
        "red_flags": [
            "Signs of severe alcohol withdrawal (hallucinations, coarse tremors, drenching sweats, tachycardia, or seizures [Delirium Tremens Emergency])"
        ]
    },
    {
        "id": "DOC-CARD-195",
        "icd10": "D25.9",
        "condition": "Uterine Leiomyomas (Fibroids)",
        "specialty": "Gynecology",
        "organ_system": "Reproductive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACOG Practice Bulletin / Cochrane Review",
        "source_body": "Obstet Gynecol",
        "citation": "American College of Obstetricians and Gynecologists. Management of Symptomatic Uterine Leiomyomas: ACOG Practice Bulletin No. 228. Obstet Gynecol. 2021;137(6):e100-e115.",
        "doi_or_source": "10.1097/AOG.0000000000004401",
        "clinical_evidence": "Uterine leiomyomas (fibroids) are benign monoclonal smooth muscle neoplasms of the myometrium, occurring in up to 70-80% of women by age 50. Symptoms depend on anatomical location (FIGO classification: submucosal [Types 0-2], intramural [Types 3-5], subserosal [Types 6-7]). Submucosal and intramural fibroids distorting the uterine cavity cause heavy menstrual bleeding (HMB / menorrhagia) leading to iron deficiency anemia; large fibroids cause pelvic pressure, urinary frequency, and hydronephrosis. Transvaginal ultrasonography is first-line imaging; saline-infusion sonohysterography (SIS) or pelvic MRI defines submucosal mapping. Medical therapy for HMB: Levonorgestrel-releasing IUD (52 mg LNG-IUD; reduces menstrual blood loss by >80%), tranexamic acid (1,300 mg TID during heavy flow), or oral GnRH antagonists combined with add-back hormone therapy (elagolix or relugolix combination therapy; FDA-approved, suppresses HMB while preventing bone loss). Uterine artery embolization (UAE), hysteroscopic/laparoscopic myomectomy, or radiofrequency ablation provide fertility-preserving or uterine-preserving procedural options; hysterectomy is definitive.",
        "solution_protocol": {
            "non_pharmacological_targets": "Dietary iron and vitamin C supplementation to treat associated microcytic anemia; structured symptom tracking with menstrual diary; pelvic floor conditioning.",
            "monitoring_cadence": "CBC (hemoglobin/ferritin) at 1 and 3 months; pelvic ultrasound annually or sooner if bulk symptoms worsen; renal ultrasound if large fibroid risks ureteral compression.",
            "clinical_thresholds": "Submucosal fibroids (FIGO Types 0-2) are primarily amenable to outpatient hysteroscopic resection, restoring normal cavity architecture and reducing bleeding."
        },
        "patient_plain_language": "Uterine fibroids are non-cancerous muscular growths that develop in the wall of your uterus. While many cause zero symptoms, depending on their size and location they can cause very heavy or prolonged periods, pelvic pressure, bloating, and fatigue from low iron.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is the measured size and exact anatomical location (submucosal, intramural, or subserosal) of my fibroids on ultrasound?",
            "safety_question": "Has my heavy bleeding caused iron deficiency anemia, and do I need oral or intravenous iron to restore my energy?",
            "action_threshold_question": "If I desire to have children in the future, which uterine-preserving treatments (like a progesterone IUD, medication, or myomectomy) are best for me?"
        },
        "red_flags": [
            "Sudden severe acute pelvic pain with fever indicating fibroid red degeneration or torsion of a pedunculated subserosal fibroid, or severe acute bleeding causing syncope"
        ]
    },
    {
        "id": "DOC-CARD-196",
        "icd10": "F53.0",
        "condition": "Postpartum Depression (PPD)",
        "specialty": "Psychiatry",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACOG Clinical Practice Guideline / SKYLARK Phase 3 RCT",
        "source_body": "Am J Psychiatry",
        "citation": "Deligiannidis KM et al. Zuranolone for the Treatment of Postpartum Depression (SKYLARK). Am J Psychiatry. 2023;180(9):668-675. / ACOG Clinical Guidance. Screening and Diagnosis of Mental Health Conditions in Perinatal Women. Obstet Gynecol. 2023;141(6):1232-1261.",
        "doi_or_source": "10.1176/appi.ajp.20220785",
        "clinical_evidence": "Postpartum depression affects ~10-15% of women following childbirth, defined as a major depressive episode occurring during pregnancy or within the first 12 months postpartum (distinguished from transient 'postpartum blues' which peak at 3-5 days and resolve by 10-14 days without functional impairment). Presentation features persistent sadness, profound emotional detachment or anhedonia toward the newborn, excessive guilt, sleep disturbance unrelated to infant wakings, severe anxiety, and obsessive fears of infant harm. The Edinburgh Postnatal Depression Scale (EPDS) is the validated screening standard (score ≥ 10-12 indicates positive screen). Mild-to-moderate PPD responds well to evidence-based psychotherapy (Interpersonal Psychotherapy [IPT] or CBT). Moderate-to-severe PPD warrants pharmacotherapy: SSRIs (sertraline is preferred during breastfeeding due to minimal infant breastmilk excretion and low relative infant dose <0.5%). The breakthrough GABA-A receptor positive allosteric modulator zuranolone (50 mg orally once nightly with fatty food for 14 days; SKYLARK phase 3 trial) demonstrated rapid, statistically significant reduction in HAM-D depression scores by day 3 with sustained remission at day 45.",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured family support plan prioritizing uninterrupted 4-6 hour maternal sleep blocks; peer postpartum support groups; Interpersonal Psychotherapy (IPT); registered lactation consultant support if breastfeeding difficulties exacerbate distress.",
            "monitoring_cadence": "EPDS repeat screening at 2, 4, and 8 weeks post-intervention; direct maternal suicide and infant safety risk inquiry at every clinical contact.",
            "clinical_thresholds": "EPDS score ≥ 10 or any positive score on Question 10 (suicidal thoughts) mandates immediate comprehensive clinical evaluation."
        },
        "patient_plain_language": "Postpartum depression is a medical complication of childbirth caused by massive hormonal drops and chemical shifts in the brain. It is not a sign of personal weakness or being a 'bad mother'. It causes deep sadness, feeling disconnected from your baby, and overwhelming anxiety that can be effectively treated.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my score on the Edinburgh Postnatal Depression Scale (EPDS) screen?",
            "safety_question": "Is sertraline (Zoloft) safe for my baby if I am currently breastfeeding?",
            "action_threshold_question": "Am I a candidate for the newer fast-acting 14-day oral medication (zuranolone/Zurzuvae) to help me feel better within days?"
        },
        "red_flags": [
            "Delusions, auditory hallucinations, severe disorientation, or irrational impulses to harm the baby (Postpartum Psychosis Emergency requiring immediate hospitalization)"
        ]
    },
    {
        "id": "DOC-CARD-197",
        "icd10": "J05.0",
        "condition": "Croup (Laryngotracheobronchitis)",
        "specialty": "Pediatrics",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review / Clinical Practice Guideline",
        "source_body": "Cochrane Database Syst Rev",
        "citation": "Russell KF et al. Glucocorticoids for croup. Cochrane Database Syst Rev. 2011;(1):CD001955. / Bjornson CL, Johnson DW. Croup. Lancet. 2008;371(9609):329-339.",
        "doi_or_source": "10.1002/14651858.CD001955.pub3",
        "clinical_evidence": "Croup is an acute viral infection of the upper airway primarily caused by human parainfluenza virus type 1 (70-80%), peaking in infants and toddlers aged 6 months to 3 years during autumn/early winter. Inflammatory subglottic edema leads to the hallmark clinical triad: barking cough (resembling a seal or dog), inspiratory stridor, and hoarseness, characteristically worsening at night. Severity is stratified via the Westley Croup Score (evaluating stridor, retractions, air entry, cyanosis, and level of consciousness). Cochrane meta-analyses definitively prove that a single dose of oral dexamethasone (0.15-0.6 mg/kg, max 16 mg) significantly reduces hospital admissions (RR 0.52), shortens length of emergency department stay, reduces return visits, and decreases the need for nebulized epinephrine across all severity grades (mild, moderate, and severe). For moderate-to-severe croup with resting stridor and retractions, nebulized racemic epinephrine (0.5 mL of 2.25% solution) or L-epinephrine provides rapid subglottic vasoconstriction and symptom relief within 10-30 minutes, requiring a 2-4 hour observation window to monitor for post-epinephrine rebound stridor.",
        "solution_protocol": {
            "non_pharmacological_targets": "Keep the child calm and comforted in the parent's lap (agitation and crying dramatically increases negative intrathoracic airway pressure and worsens subglottic collapse); avoid painful or intrusive procedures (e.g., throat exams or IVs unless necessary); cool mist humidification.",
            "monitoring_cadence": "Westley Croup Score every 30-60 minutes in the emergency department; mandatory 2 to 4 hour observation following nebulized epinephrine prior to safe discharge.",
            "clinical_thresholds": "Resting stridor, sternal/intercostal retractions, or agitation indicates moderate-to-severe croup requiring nebulized epinephrine in addition to oral dexamethasone."
        },
        "patient_plain_language": "Croup is a common childhood viral infection that causes swelling in the voice box and windpipe just below the vocal cords. The narrowed airway produces a very distinctive deep, barking cough that sounds like a barking seal, along with a high-pitched squeaking noise when breathing in (stridor).",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my child's Westley Croup Score and do they have stridor when resting quietly?",
            "safety_question": "Has my child received a dose of oral dexamethasone, which calms the airway swelling for the next 24 to 72 hours?",
            "action_threshold_question": "If my child received an adrenaline breathing treatment, how many hours do we need to be observed to ensure the stridor does not rebound?"
        },
        "red_flags": [
            "High-pitched squeaking (stridor) while resting quietly, skin sucking in between ribs and at the base of the throat with each breath, drooling with inability to swallow, or blue lips"
        ]
    },
    {
        "id": "DOC-CARD-198",
        "icd10": "J21.0",
        "condition": "Pediatric Bronchiolitis (RSV)",
        "specialty": "Pediatrics",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAP Clinical Practice Guideline",
        "source_body": "Pediatrics",
        "citation": "Ralston SL et al. Clinical Practice Guideline: The Diagnosis, Management, and Prevention of Bronchiolitis. Pediatrics. 2014;134(5):e1474-e1502.",
        "doi_or_source": "10.1542/peds.2014-2742",
        "clinical_evidence": "Bronchiolitis is the leading cause of hospitalization in infants < 12 months, predominantly caused by Respiratory Syncytial Virus (RSV, 70-80%). Viral necrosis of bronchiolar epithelium, mucus plugging, and submucosal edema produce air trapping, tachypnea, expiratory wheezing, diffuse crackles, and increased work of breathing (nasal flaring, subcostal retractions). AAP evidence-based guidelines emphasize supportive care as the foundation of management: nasal suctioning (saline drops and bulb suction) and maintenance of adequate hydration (oral feeds or IV/nasogastric fluids if tachypneic with respiratory rate > 60-70 breaths/min risking aspiration). The AAP guideline explicitly recommends AGAINST the routine use of bronchodilators (albuterol), systemic corticosteroids, or chest physiotherapy, as randomized trials demonstrate they do not alter disease progression, reduce hospitalizations, or shorten stay. Supplemental oxygen is indicated only if pulse oximetry persistently falls below 90%. High-risk infants benefit from immunoprophylaxis with the long-acting monoclonal antibody nirsevimab (Beyfortus; single IM injection providing >75-80% protection against RSV lower respiratory infection; MELODY trial; NEJM 2022).",
        "solution_protocol": {
            "non_pharmacological_targets": "Nasal bulb or mechanical suctioning with gentle isotonic saline drops before every feeding and before sleep; small, frequent feedings to avoid fatigue and vomiting; strict hand hygiene; eliminate infant exposure to secondhand tobacco smoke.",
            "monitoring_cadence": "Respiratory rate, work of breathing (retractions), pulse oximetry, and hydration assessment (wet diapers) every 2-4 hours; peak clinical severity typically occurs on days 3-5 of illness.",
            "clinical_thresholds": "Sustained pulse oximetry < 90% or inability to maintain oral hydration due to severe tachypnea (>60-70 breaths/min) mandates inpatient admission."
        },
        "patient_plain_language": "Bronchiolitis is a common winter viral infection (most often caused by RSV) that clogs the tiniest breathing branches (bronchioles) in an infant's lungs with mucus. Babies start with common cold symptoms before developing fast breathing, wheezing, and a chest that sucks in when inhaling.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my infant's current oxygen saturation and respiratory rate count over a full minute?",
            "safety_question": "Why do pediatric guidelines recommend gentle nose suctioning and fluids rather than asthma inhalers or steroid syrups that do not help in RSV?",
            "action_threshold_question": "How many wet diapers should my baby produce in 24 hours to confirm they are staying well-hydrated despite rapid breathing?"
        },
        "red_flags": [
            "Pauses in breathing lasting longer than 15-20 seconds (apnea), grunting with breaths, blueish tint around the mouth (cyanosis), or extreme exhaustion where baby is too tired to feed"
        ]
    },
    {
        "id": "DOC-CARD-199",
        "icd10": "H81.10",
        "condition": "Benign Paroxysmal Positional Vertigo (BPPV)",
        "specialty": "ENT / Otolaryngology",
        "organ_system": "Nervous",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO-HNSF Clinical Practice Guideline / Cochrane Review",
        "source_body": "Otolaryngol Head Neck Surg",
        "citation": "Bhattacharyya N et al. Clinical Practice Guideline: Benign Paroxysmal Positional Vertigo (Update). Otolaryngol Head Neck Surg. 2017;156(3_suppl):S1-S47.",
        "doi_or_source": "10.1177/0194599816689667",
        "clinical_evidence": "BPPV is the most common cause of peripheral vertigo, caused by otoconia (calcium carbonate crystals) dislodged from the utricular macula migrating into a semicircular canal (canalithiasis; posterior canal involved in 85-95%). Pathognomonic presentation is brief (<1 minute), intense episodes of rotational spinning vertigo provoked by head position changes relative to gravity (rolling over in bed, looking up at a high shelf, bending forward). Gold standard diagnosis is the Dix-Hallpike maneuver, which elicits torsional, upbeating nystagmus with a 2-5 second latency and duration < 60 seconds that fatigues upon repeated testing. First-line definitive therapy is the canalith repositioning procedure (Epley maneuver; Cochrane systematic review proves >80-90% resolution of vertigo and negative Dix-Hallpike after 1-2 treatments vs 30% control, NNT=1.5). Vestibular suppressant medications (meclizine, benzodiazepines) are explicitly NOT recommended for routine treatment because they impair central compensation, cause cognitive blunting, and do not resolve otoconia displacement.",
        "solution_protocol": {
            "non_pharmacological_targets": "Canalith repositioning procedure (Epley maneuver performed by a trained clinician); Brandt-Daroff home habituation exercises for persistent residual mild dizziness; fall prevention precautions when getting out of bed.",
            "monitoring_cadence": "Clinical reassessment and repeat Dix-Hallpike test at 1 month to ensure resolution; reassess if recurrent positional vertigo returns (occurs in ~30-50% over 5 years).",
            "clinical_thresholds": "Positive Dix-Hallpike test with classic torsional upbeating nystagmus confirms posterior canal BPPV; negative test confirms successful repositioning."
        },
        "patient_plain_language": "BPPV is a common inner-ear balance disorder where tiny calcium 'ear stones' come loose from their normal spot and float into the semicircular balance canals. When you tilt your head or roll over in bed, the loose crystals slosh the ear fluid, tricking your brain into feeling like the room is violently spinning.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my Dix-Hallpike test trigger the spinning sensation and tell you which ear and canal the loose crystals are in?",
            "safety_question": "Can we perform an in-office Epley repositioning maneuver right now to guide the loose crystals back where they belong?",
            "action_threshold_question": "Why should I avoid taking dizziness pills like meclizine (Antivert) that only cause drowsiness without fixing the loose crystals?"
        },
        "red_flags": [
            "Dizziness accompanied by double vision, slurred speech, facial numbness, weakness in an arm or leg, or inability to sit upright without falling (ruling out central brainstem/cerebellar stroke)"
        ]
    },
    {
        "id": "DOC-CARD-200",
        "icd10": "E11.319",
        "condition": "Diabetic Retinopathy",
        "specialty": "Ophthalmology",
        "organ_system": "Sensory & Ophthalmic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAO Preferred Practice Pattern / DRCR.net Protocol T RCT",
        "source_body": "Ophthalmology",
        "citation": "Flaxel CJ et al. Diabetic Retinopathy Preferred Practice Pattern. Ophthalmology. 2020;127(1):P66-P145. / Wells JA et al. DRCR.net Protocol T. N Engl J Med. 2015;372(13):1193-1204.",
        "doi_or_source": "10.1056/NEJMoa1414264",
        "clinical_evidence": "Diabetic retinopathy is a leading cause of preventable blindness in working-age adults, caused by chronic microvascular damage from hyperglycemia leading to retinal capillary basement membrane thickening, pericyte loss, microaneurysms, retinal hemorrhages, and vascular leakage. Classified into Non-Proliferative (NPDR: mild, moderate, severe based on 4-2-1 rule: retinal hemorrhages in 4 quadrants, venous beading in 2 quadrants, IRMA in 1 quadrant) and Proliferative (PDR: pathological neovascularization of the disc [NVD] or retina [NVE] driven by VEGF ischemia, risking vitreous hemorrhage and tractional retinal detachment). Diabetic macular edema (DME: fluid accumulation in the fovea) can occur at any stage. Foundational systemic control (UKPDS and DCCT trials) reduces retinopathy progression: HbA1c < 7.0%, blood pressure < 130/80 mmHg, and lipid management. First-line therapy for center-involved DME with visual impairment is intravitreal anti-VEGF injections (aflibercept, ranibizumab, or faricimab; Protocol T trial showed aflibercept achieved superior visual gains in eyes with initial visual acuity 20/50 or worse). Panretinal photocoagulation (PRP) laser or anti-VEGF therapy stabilizes high-risk PDR.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict glycemic control (HbA1c target < 7.0%); blood pressure target < 130/80 mmHg; manage dyslipidemia; smoking cessation; aerobic exercise.",
            "monitoring_cadence": "Annual dilated fundus examination by an ophthalmologist/optometrist starting immediately at diagnosis in Type 2 diabetes, or within 5 years of diagnosis in Type 1 diabetes; every 3-6 months for moderate-to-severe NPDR; optical coherence tomography (OCT) to monitor macular thickness.",
            "clinical_thresholds": "Optical coherence tomography (OCT) demonstrating central macular thickness > 300 µm with intraretinal cysts indicates center-involved diabetic macular edema requiring intravitreal anti-VEGF therapy."
        },
        "patient_plain_language": "Diabetic retinopathy is damage to the delicate blood vessels in the light-sensing retina at the back of your eye caused by high blood sugar. In its early stages, weak spots leak fluid into the center of vision; in later stages, abnormal fragile blood vessels sprout that can bleed into the eye, causing dark floaters or vision loss.",
        "doctor_consultation_checklist": {
            "parameter_question": "What stage of diabetic retinopathy (mild, moderate, severe NPDR, or proliferative) was seen on my dilated eye exam?",
            "safety_question": "Did my optical coherence tomography (OCT) eye scan detect any diabetic macular swelling in my central vision?",
            "action_threshold_question": "How often should I receive eye exams, and would anti-VEGF eye injections help preserve and restore my vision?"
        },
        "red_flags": [
            "Sudden shower of new dark floating spots (floaters), dark cobwebs, sudden painless loss of vision, or a dark curtain descending across your field of view (vitreous hemorrhage or retinal detachment)"
        ]
    }
]