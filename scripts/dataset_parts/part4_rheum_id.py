"""
part4_rheum_id.py
"""

PART_4_DISEASES = [
    {
        "id": "DOC-CARD-161",
        "icd10": "M45.9",
        "condition": "Ankylosing Spondylitis (Axial Spondyloarthritis)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ASAS-EULAR Management Recommendations",
        "source_body": "Ann Rheum Dis",
        "citation": "Ramiro S et al. ASAS-EULAR recommendations for the management of axial spondyloarthritis: 2022 update. Ann Rheum Dis. 2023;82(1):19-34.",
        "doi_or_source": "10.1136/ard-2022-223296",
        "clinical_evidence": "Axial spondyloarthritis (axSpA) is a chronic inflammatory rheumatic disease predominantly affecting the axial skeleton and sacroiliac joints, strongly associated with HLA-B27 (>85%). It presents as chronic inflammatory back pain (onset <45 years, insidious onset, improvement with exercise but not with rest, morning stiffness >30 minutes, waking during the second half of the night). Sacroiliitis on MRI (active bone marrow edema) or pelvic radiographs (modified New York criteria) confirms diagnosis. First-line pharmacotherapy is continuous treatment with full-dose NSAIDs (naproxen, celecoxib). For patients with persistently high disease activity (ASDAS ≥ 2.1) despite ≥ 2 NSAIDs, biological DMARDs targeting TNF (adalimumab, etanercept, infliximab) or IL-17A (secukinumab, ixekizumab), or JAK inhibitors (upadacitinib, tofacitinib) provide significant symptom relief, suppress spinal inflammation, and improve function.",
        "solution_protocol": {
            "non_pharmacological_targets": "Lifelong daily structured spinal extension physiotherapy and home exercise program; pulmonary deep-breathing exercises to maintain chest wall expansion; strict smoking cessation (smoking accelerates syndesmophyte formation and spinal fusion).",
            "monitoring_cadence": "Ankylosing Spondylitis Disease Activity Score (ASDAS-CRP) and BASDAI every 3-6 months; annual cervical/thoracic/lumbar spinal mobility measurements (Bath AS Metrology Index [BASMI]); screening for anterior uveitis.",
            "clinical_thresholds": "ASDAS ≥ 2.1 indicates high disease activity, qualifying for biologic therapy (TNF inhibitor or IL-17 inhibitor)."
        },
        "patient_plain_language": "Ankylosing spondylitis is a chronic autoimmune form of arthritis that targets your spine and pelvic joints. Unlike ordinary mechanical back pain, the stiffness and ache feel worse after resting or sleeping and actually improve when you get up and move around. Over years, it can cause the spinal bones to fuse together.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current ASDAS-CRP disease activity score, and did my pelvic MRI show active bone marrow inflammation in my sacroiliac joints?",
            "safety_question": "If my stomach or kidneys cannot handle high-dose daily anti-inflammatory pills, can we move forward with a targeted biologic injection like a TNF or IL-17 inhibitor?",
            "action_threshold_question": "What daily spinal stretching exercises should I do every morning to prevent my spine from becoming stiff and fused?"
        },
        "red_flags": [
            "Sudden painful, red, light-sensitive eye with blurry vision (acute anterior uveitis emergency), or severe new back pain after minor trauma (spinal fracture risk)"
        ]
    },
    {
        "id": "DOC-CARD-162",
        "icd10": "L40.50",
        "condition": "Psoriatic Arthritis (PsA)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: GRAPPA Treatment Recommendations",
        "source_body": "Nat Rev Rheumatol",
        "citation": "Coates LC et al. Group for Research and Assessment of Psoriasis and Psoriatic Arthritis (GRAPPA): updated treatment recommendations for psoriatic arthritis 2021. Nat Rev Rheumatol. 2022;18(8):465-479.",
        "doi_or_source": "10.1038/s41584-022-00798-0",
        "clinical_evidence": "Psoriatic arthritis affects ~20-30% of patients with cutaneous psoriasis, presenting across six clinical domains: peripheral arthritis (often asymmetric, involving DIP joints), enthesitis (inflammation at tendon insertions, e.g., Achilles, plantar fascia), dactylitis ('sausage digits'), axial disease, skin psoriasis, and nail dystrophy (pitting, onycholysis; strongly correlates with DIP arthritis). CASPAR criteria require inflammatory articular disease plus ≥ 3 points from personal/family psoriasis, nail dystrophy, negative RF, current/past dactylitis, and juxta-articular new bone formation. Conventional synthetic DMARDs (methotrexate 15-25 mg/week) treat peripheral arthritis. GRAPPA guidelines recommend targeted biologics—TNF inhibitors, IL-17A inhibitors (secukinumab), IL-23 inhibitors (guselkumab, risankizumab), or JAK inhibitors (upadacitinib)—to inhibit structural joint damage and clear skin lesions simultaneously.",
        "solution_protocol": {
            "non_pharmacological_targets": "Low-impact joint conditioning (swimming, cycling); physical therapy and orthotics for foot enthesitis; weight management (obesity impairs biologic response); smoking cessation.",
            "monitoring_cadence": "DAPSA (Disease Activity in Psoriatic Arthritis) score, swollen/tender joint counts, and Leeds Enthesitis Index every 3 months until remission; regular dermatologic skin checks.",
            "clinical_thresholds": "Erosive changes on hand/foot radiographs or active dactylitis/enthesitis warrants early escalation to targeted biologic/targeted synthetic DMARDs."
        },
        "patient_plain_language": "Psoriatic arthritis is an autoimmune condition where your immune system attacks both your skin and your joints. Beyond red, scaly skin patches, it can cause swollen fingers or toes that look like little sausages, painful heels where tendons attach to bone, and stiff, aching joints.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current DAPSA joint activity score and how many joints currently show swelling?",
            "safety_question": "Which medication (such as an IL-17, IL-23, or TNF blocker) will best clear my skin psoriasis and protect my joints from permanent bone damage at the same time?",
            "action_threshold_question": "Are my fingernails showing signs of pitting that link directly to my joint pain?"
        },
        "red_flags": [
            "Rapid development of a hot, acutely swollen, exquisitely painful single joint that requires joint fluid aspiration to rule out septic arthritis"
        ]
    },
    {
        "id": "DOC-CARD-163",
        "icd10": "M34.9",
        "condition": "Systemic Sclerosis (Scleroderma)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR Recommendations for Scleroderma Management",
        "source_body": "Ann Rheum Dis",
        "citation": "Kowal-Bielecka O et al. Update of EULAR recommendations for the treatment of systemic sclerosis. Ann Rheum Dis. 2017;76(8):1327-1339.",
        "doi_or_source": "10.1136/annrheumdis-2016-209909",
        "clinical_evidence": "Systemic sclerosis is a complex autoimmune disease characterized by microvascular obliteration, immune dysregulation, and progressive widespread fibrosis of skin and internal organs. Divided into limited cutaneous (lcSSc: CREST syndrome; anti-centromere positive in 60-80%) and diffuse cutaneous (dcSSc: anti-Scl-70/topoisomerase I or anti-RNA polymerase III positive; rapid proximal skin thickening and early visceral organ failure). Scleroderma renal crisis (SRC) presents with acute malignant hypertension and oliguric renal failure, strongly linked to anti-RNA polymerase III and high-dose corticosteroid use (>15 mg/day prednisone is contraindicated); immediate ACE inhibitor therapy (captopril) is lifesaving. Interstitial lung disease (SSc-ILD) is the leading cause of death; mycophenolate mofetil (SLS II trial; Lancet Respir Med 2016) and nintedanib (SENSCIS trial; NEJM 2019) preserve FVC and slow lung fibrosis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of cold exposure; keep core body and extremities warm (heated gloves/socks); elevate head of bed 6 inches to manage refractory GERD; skin moisturization and stretching.",
            "monitoring_cadence": "Daily home blood pressure monitoring (to detect impending scleroderma renal crisis); annual pulmonary function testing (FVC and DLCO) and annual transthoracic echocardiogram to screen for pulmonary arterial hypertension; modified Rodnan Skin Score (mRSS).",
            "clinical_thresholds": "Drop in FVC ≥ 10% or FVC 5-9% with DLCO drop ≥ 15% indicates progressive SSc-ILD requiring initiation or intensification of antifibrotic/immunosuppressive therapy."
        },
        "patient_plain_language": "Systemic sclerosis, or scleroderma, is a rare autoimmune disorder where the body produces too much collagen protein, causing the skin to become tight, thick, and firm. In addition to fingers turning white and painful in the cold (Raynaud's), it can cause acid reflux and stiffen lung tissues.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were my latest pulmonary function test results (FVC and DLCO) to check for lung inflammation or scarring?",
            "safety_question": "Why must I strictly avoid steroid medications like prednisone, which could trigger a sudden scleroderma kidney crisis?",
            "action_threshold_question": "What is my home blood pressure goal, and what sudden spike should prompt me to take captopril and call immediately?"
        },
        "red_flags": [
            "Sudden spike in blood pressure (systolic > 150 or diastolic > 90) accompanied by headache, blurry vision, or decreased urination (Scleroderma Renal Crisis Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-164",
        "icd10": "M35.00",
        "condition": "Sjögren's Syndrome",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ACR/EULAR Classification Criteria and Recommendations",
        "source_body": "Ann Rheum Dis",
        "citation": "Ramos-Casals M et al. EULAR recommendations for the management of Sjögren's syndrome with topical and systemic therapies. Ann Rheum Dis. 2020;79(1):3-18.",
        "doi_or_source": "10.1136/annrheumdis-2019-216114",
        "clinical_evidence": "Sjögren's syndrome is a systemic autoimmune disease characterized by lymphocytic infiltration of exocrine glands, predominantly the lacrimal and salivary glands, resulting in severe keratoconjunctivitis sicca (dry eyes) and xerostomia (dry mouth). ACR-EULAR criteria require a score ≥ 4 based on: labial salivary gland biopsy with focal lymphocytic sialadenitis (focus score ≥ 1/4 mm²), positive anti-SSA/Ro antibodies, ocular staining score ≥ 5, Schirmer's test ≤ 5 mm/5 min, and unstimulated whole saliva flow rate ≤ 0.1 mL/min. Symptomatic secretagogue therapy (pilocarpine 5 mg QID or cevimeline 30 mg TID) stimulates M3 muscarinic receptors to increase saliva and tear secretion. Topical ophthalmic cyclosporine (0.05%) or lifitegrast (5%) treats ocular surface inflammation. Hydroxychloroquine (200-400 mg/day) reduces inflammatory arthralgias and systemic fatigue. Patients have a ~15-20 fold increased lifetime risk of non-Hodgkin B-cell lymphoma (predominantly MALT lymphoma).",
        "solution_protocol": {
            "non_pharmacological_targets": "Frequent water sipping; sugar-free xylitol gum/lozenges; preservative-free artificial tears; home cool mist humidifiers; meticulous oral hygiene (flossing, fluoridated prescription toothpaste, biannual dental exams).",
            "monitoring_cadence": "Dental exams every 3-6 months (high risk of rampant dental caries); annual serum protein electrophoresis (SPEP), quantitative immunoglobulins, and complete blood count; screening for persistent parotid gland swelling or lymphadenopathy to detect lymphoma early.",
            "clinical_thresholds": "Unstimulated salivary flow ≤ 0.1 mL/min or Schirmer's ≤ 5 mm/5 min objective cutoffs; development of monoclonal paraprotein, cryoglobulins, or low C4 warrants lymphoma workup."
        },
        "patient_plain_language": "Sjögren's syndrome is an autoimmune condition where your immune system attacks your body's moisture-producing glands. The primary symptoms are severely dry, gritty eyes and a dry mouth that makes chewing dry crackers, speaking for long periods, or swallowing difficult.",
        "doctor_consultation_checklist": {
            "parameter_question": "Were my anti-SSA (Ro) and anti-SSB (La) antibody blood tests positive?",
            "safety_question": "Am I using prescription high-fluoride toothpaste to prevent the rampant dental cavities that occur when saliva is low?",
            "action_threshold_question": "Can I try a prescription salivary stimulant pill like cevimeline or pilocarpine to help me produce more natural saliva?"
        },
        "red_flags": [
            "Persistent, painless enlargement of one or both salivary/parotid glands, unexplained night sweats, weight loss, or swollen lymph nodes (high lymphoma risk)"
        ]
    },
    {
        "id": "DOC-CARD-165",
        "icd10": "M35.3",
        "condition": "Polymyalgia Rheumatica (PMR)",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR/ACR Collaborative Recommendations",
        "source_body": "Ann Rheum Dis",
        "citation": "Dejaco C et al. 2015 Recommendations for the management of polymyalgia rheumatica: a European League Against Rheumatism/American College of Rheumatology collaborative initiative. Ann Rheum Dis. 2015;74(10):1799-1807.",
        "doi_or_source": "10.1136/annrheumdis-2015-207892",
        "clinical_evidence": "Polymyalgia rheumatica is an inflammatory disorder occurring almost exclusively in individuals > 50 years (mean age 73), presenting with sudden-onset, severe bilateral aching and morning stiffness (>45 minutes) in the shoulder girdle, pelvic girdle, and neck, accompanied by elevated inflammatory markers (ESR > 40 mm/hr, CRP > 10 mg/L). Musculoskeletal ultrasound characteristically demonstrates bilateral subacromial/subdeltoid bursitis, trochanteric bursitis, or biceps tenosynovitis. Hallmark diagnostic feature is a rapid, dramatic clinical response (>70% improvement within 48-72 hours) to moderate-dose oral corticosteroids (prednisone 12.5-25 mg/day). Tapering is performed slowly over 12-24 months. For frequent relapsers or high steroid-toxicity risk, the IL-6 receptor antagonist sarilumab is FDA-approved (SAPHYR trial; NEJM 2023: 28% sustained remission on sarilumab vs 10% on placebo, p=0.02). Approximately 15-20% of PMR patients develop concurrent Giant Cell Arteritis (GCA).",
        "solution_protocol": {
            "non_pharmacological_targets": "Bone-protection measures: calcium (1,000-1,200 mg/day), vitamin D (800-1,000 IU/day), baseline DEXA scan, and bisphosphonate therapy if high fracture risk; gentle progressive range-of-motion physical therapy.",
            "monitoring_cadence": "ESR and CRP at baseline, 1 month, and before each planned prednisone dose reduction; vigilant screening for symptoms of giant cell arteritis (headache, scalp tenderness, jaw claudication, vision loss) at every visit.",
            "clinical_thresholds": "Rapid symptomatic relief (>70% improvement in pain/stiffness) within 72 hours of starting 15 mg prednisone strongly supports PMR diagnosis."
        },
        "patient_plain_language": "Polymyalgia rheumatica (PMR) is an inflammatory condition affecting older adults that causes severe stiffness and aching across both shoulders, hips, thighs, and neck, particularly upon waking in the morning. Getting out of bed or lifting your arms to put on a jacket can feel almost impossible, but it responds quickly to low-dose steroid medication.",
        "doctor_consultation_checklist": {
            "parameter_question": "What were my baseline ESR and CRP inflammation lab values, and did my ultrasound show shoulder bursitis?",
            "safety_question": "Are my bones being protected against osteoporosis with calcium, vitamin D, and a bone density scan while taking prednisone?",
            "action_threshold_question": "What is our gradual monthly tapering schedule for prednisone, and what symptoms indicate that we are tapering too quickly?"
        },
        "red_flags": [
            "Sudden new throbbing temple headache, scalp tenderness when brushing hair, jaw muscle pain when chewing food, or sudden blurry vision/loss of sight (Giant Cell Arteritis Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-166",
        "icd10": "M33.90",
        "condition": "Dermatomyositis / Polymyositis",
        "specialty": "Rheumatology",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: EULAR/ACR Classification Criteria / ProDERM Trial",
        "source_body": "N Engl J Med",
        "citation": "Aggarwal R et al. Trial of Intravenous Immune Globulin in Dermatomyositis (ProDERM). N Engl J Med. 2022;387(14):1264-1278.",
        "doi_or_source": "10.1056/NEJMoa2117912",
        "clinical_evidence": "Idiopathic inflammatory myopathies are characterized by symmetric, progressive proximal skeletal muscle weakness (difficulty climbing stairs, rising from a chair, lifting objects overhead) and markedly elevated serum creatine kinase (CK, often 5-50x ULN). Dermatomyositis features pathognomonic cutaneous signs: heliotrope rash (violaceous periorbital erythema and edema) and Gottron's papules (scaly violaceous plaques over MCP and PIP joints), plus shawl sign, V-sign, and mechanic's hands (anti-synthetase syndrome). Myositis-specific antibodies (anti-Mi-2, anti-Jo-1, anti-TIF1-gamma, anti-NXP2, anti-MDA5) define clinical phenotypes and cancer risk. Anti-TIF1-gamma and anti-NXP2 carry high risk of age-associated underlying malignancy (ovarian, breast, lung, GI), mandating comprehensive cancer screening. First-line therapy is high-dose oral prednisone (1 mg/kg/day) plus steroid-sparing immunosuppressants (methotrexate, azathioprine). The landmark ProDERM phase 3 trial established IVIG (2 g/kg monthly) as safe and significantly superior to placebo (79% response vs 44%, p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict sun protection (broad-spectrum SPF 50+, protective clothing; UV light directly exacerbates cutaneous dermatomyositis); physical therapy with gentle active-assisted range of motion during acute phase, progressing to resistance training during remission; speech therapy for dysphagia.",
            "monitoring_cadence": "Serum CK, aldolase, and Manual Muscle Testing (MMT-8) every 4-8 weeks; pulmonary function tests (FVC, DLCO) and high-resolution chest CT to detect rapidly progressive interstitial lung disease (especially if anti-MDA5 positive); comprehensive age-appropriate cancer screening.",
            "clinical_thresholds": "Anti-TIF1-gamma or anti-NXP2 positive antibodies require intensive age-appropriate and CT body cancer screening."
        },
        "patient_plain_language": "Dermatomyositis is an autoimmune condition where your immune system causes inflammation in both your muscles and skin. It causes progressive muscle weakness in your thighs and shoulders—making it hard to stand up from a low chair or brush your hair—along with distinct purple-red rashes over your eyelids and knuckles.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my current blood creatine kinase (CK) muscle enzyme level, and what did my myositis autoantibody panel reveal?",
            "safety_question": "Has a comprehensive screening for underlying cancer been scheduled, as recommended for adults diagnosed with dermatomyositis?",
            "action_threshold_question": "Did my lung CT scan and breathing tests show any signs of inflammatory lung disease?"
        },
        "red_flags": [
            "Severe choking and difficulty swallowing (pharyngeal muscle paralysis / high aspiration risk), or rapid shortness of breath over days to weeks (anti-MDA5 rapidly progressive interstitial lung disease)"
        ]
    },
    {
        "id": "DOC-CARD-167",
        "icd10": "M75.10",
        "condition": "Rotator Cuff Tendinopathy and Tears",
        "specialty": "Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAOS Clinical Practice Guideline",
        "source_body": "J Am Acad Orthop Surg",
        "citation": "American Academy of Orthopaedic Surgeons. Management of Rotator Cuff Injuries: Clinical Practice Guideline. J Am Acad Orthop Surg. 2020;28(5):e193-e201.",
        "doi_or_source": "10.5435/JAAOS-D-19-00463",
        "clinical_evidence": "Rotator cuff disorders encompass tendinopathy, partial-thickness tears, and full-thickness tears primarily involving the supraspinatus tendon. Patients present with anterolateral shoulder pain exacerbated by overhead activity, pain radiating to the deltoid insertion, and nocturnal pain when lying on the affected side. Physical exam reveals painful arc (60-120 degrees), positive Hawkins-Kennedy/Neer impingement signs, and weakness on empty-can (Jobe's) or external rotation tests. MRI of the shoulder is the imaging gold standard. Cochrane reviews and randomized clinical trials confirm that structured, supervised physical therapy focusing on rotator cuff strengthening and scapular stabilizing exercises is as effective as surgical acromioplasty or repair for non-traumatic, degenerative rotator cuff tears at 1, 2, and 5-year follow-up. Acute full-thickness traumatic tears in young, active patients benefit from prompt surgical repair within 3 months to prevent muscle retraction and fatty infiltration.",
        "solution_protocol": {
            "non_pharmacological_targets": "Structured active rotator cuff and periscapular strengthening physical therapy (at least 12 weeks); avoid repetitive overhead lifting and heavy carrying during acute inflammatory phase; sleep positioning with pillow support under arm.",
            "monitoring_cadence": "Clinical shoulder range of motion, strength testing, and validated outcome scores (ASES or Constant score) at 6 and 12 weeks of physical therapy; repeat MRI if acute functional loss occurs.",
            "clinical_thresholds": "Failure of conservative therapy after 3-6 months in symptomatic full-thickness tears or acute traumatic full-thickness tears warrants orthopedic surgical evaluation."
        },
        "patient_plain_language": "The rotator cuff is a team of four muscles and tendons that keep your shoulder ball centered in its socket. Wear-and-tear or injury can fray or tear these tendons, causing aching pain on the outside of your shoulder, especially when reaching up overhead or trying to sleep on that side.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my shoulder MRI show tendinitis, a partial-thickness tear, or a complete full-thickness tendon tear?",
            "safety_question": "Can I try a dedicated 12-week physical therapy strengthening program before considering surgery, based on AAOS guidelines?",
            "action_threshold_question": "Would a guided subacromial corticosteroid injection provide enough pain relief to allow me to participate effectively in physical therapy?"
        },
        "red_flags": [
            "Sudden total inability to lift the arm following acute trauma (indicating an acute full-thickness tear requiring prompt surgical repair), or sudden severe joint warmth with fever"
        ]
    },
    {
        "id": "DOC-CARD-168",
        "icd10": "M72.2",
        "condition": "Plantar Fasciitis",
        "specialty": "Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: JOSPT Clinical Practice Guideline",
        "source_body": "J Orthop Sports Phys Ther",
        "citation": "Martin RL et al. Heel Pain—Plantar Fasciitis: Revision 2014. Clinical Practice Guidelines Linked to the International Classification of Functioning, Disability, and Health from the Orthopaedic Section of the APTA. J Orthop Sports Phys Ther. 2014;44(11):A1-A33.",
        "doi_or_source": "10.2519/jospt.2014.0303",
        "clinical_evidence": "Plantar fasciitis is a degenerative non-inflammatory fasciosis of the thick plantar aponeurosis origin at the medial calcaneal tuberosity. Pathognomonic clinical presentation is sharp, stabbing heel pain with the first steps in the morning upon getting out of bed, or after prolonged periods of sitting (post-static dyskinesia), which temporarily eases after walking a few minutes, but worsens by the end of the day. Risk factors include obesity (BMI > 30), limited ankle dorsiflexion (<0 degrees), pes planus or pes cavus, and prolonged occupational weight-bearing. Evidence-based first-line conservative management resolves >90% of cases within 6-12 months: plantar fascia-specific stretching exercises, gastrocnemius/soleus calf stretching, prefabricated or custom arch orthoses (NNT=5), night splints maintaining neutral dorsiflexion, and cushioned supportive footwear. Corticosteroid injections provide short-term relief (<4-6 weeks) but carry risks of plantar fascia rupture and calcaneal fat pad atrophy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Plantar fascia-specific stretching (pulling toes back toward shin for 30 seconds, 3 times before taking first morning step); calf muscle eccentric stretching; wear supportive shoes with arch support at all times (never walk barefoot, even indoors); night splints; ice bottle rolling.",
            "monitoring_cadence": "Clinical reassessment of morning pain visual analogue scale (VAS) and Foot Function Index at 6 and 12 weeks of conservative stretching; imaging only if symptoms persist beyond 3 months.",
            "clinical_thresholds": "Symptoms persisting > 6 months despite compliant conservative therapy classify as chronic recalcitrant plantar fasciitis, qualifying for extracorporeal shockwave therapy (ESWT)."
        },
        "patient_plain_language": "Plantar fasciitis is an irritation and thickening of the strong, shock-absorbing band of tissue that supports the arch of your foot. It causes sharp, stabbing heel pain during your very first morning steps out of bed, which feels like stepping on a nail before it gradually loosens up.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my exam confirm plantar fasciitis rather than a calcaneal stress fracture, nerve entrapment (tarsal tunnel), or fat pad atrophy?",
            "safety_question": "Why should I try night splints, custom orthotics, and stretching before considering cortisone shots that could weaken the heel fat pad?",
            "action_threshold_question": "If morning heel pain persists after 6 months of stretching, would non-invasive extracorporeal shockwave therapy (ESWT) be appropriate?"
        },
        "red_flags": [
            "Severe persistent heel pain at rest, numbness or tingling in the sole of the foot, or inability to bear weight on the heel"
        ]
    },
    {
        "id": "DOC-CARD-169",
        "icd10": "M75.00",
        "condition": "Adhesive Capsulitis (Frozen Shoulder)",
        "specialty": "Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: JOSPT Clinical Practice Guideline / Cochrane Review",
        "source_body": "J Orthop Sports Phys Ther",
        "citation": "Kelley MJ et al. Shoulder Pain and Mobility Deficits: Adhesive Capsulitis. Clinical Practice Guidelines Linked to the International Classification of Functioning, Disability, and Health From the Orthopaedic Section of the APTA. J Orthop Sports Phys Ther. 2013;43(5):A1-A31.",
        "doi_or_source": "10.2519/jospt.2013.0302",
        "clinical_evidence": "Adhesive capsulitis is characterized by progressive, painful loss of both active and passive glenohumeral range of motion in all planes, predominantly external rotation (>50% reduction or <30 degrees) and abduction, caused by capsular contracture and synovial inflammation. Strongly associated with diabetes mellitus (prevalence up to 20%), thyroid disorders, and periods of prolonged shoulder immobilization. Follows a three-phase continuum: Freezing (painful stage, 2-9 months), Frozen (stiff stage, 4-12 months), and Thawing (recovery stage, 12-42 months). Cochrane systematic reviews and randomized trials demonstrate that an early intra-articular glenohumeral corticosteroid injection (e.g., triamcinolone 40 mg with ultrasound guidance) combined with gentle, pain-free stretching physical therapy significantly accelerates pain relief and functional motion recovery compared to physical therapy alone (standardized mean difference -0.65). Aggressive forceful manipulation is contraindicated in the inflammatory freezing stage.",
        "solution_protocol": {
            "non_pharmacological_targets": "Gentle, pain-free range-of-motion stretching exercises (pendulum exercises, pulley stretches, finger-ladder climbing); strict avoidance of aggressive, forceful stretching that exacerbates capsular synovitis; heat application prior to exercises.",
            "monitoring_cadence": "Goniometric measurement of passive external rotation, abduction, and internal rotation every 4-6 weeks; optimize glycemic control in diabetic patients (HbA1c).",
            "clinical_thresholds": "Passive external rotation deficit > 50% compared to the unaffected contralateral side confirms adhesive capsulitis."
        },
        "patient_plain_language": "Adhesive capsulitis, commonly called 'frozen shoulder', happens when the strong capsule of connective tissue surrounding your shoulder joint becomes inflamed, thickens, and tightens up. The joint loses its lubrication and shrinks, making it difficult to reach your arm behind your back or overhead.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my measured passive external rotation angle compared to my good shoulder?",
            "safety_question": "Would an ultrasound-guided cortisone injection into the shoulder capsule help shorten the painful 'freezing' phase?",
            "action_threshold_question": "How can I ensure my physical therapist uses gentle stretching rather than aggressive forced movements that could inflame the capsule further?"
        },
        "red_flags": [
            "Sudden total loss of shoulder movement accompanied by high fever, severe redness, or chills (ruling out septic arthritis of the shoulder)"
        ]
    },
    {
        "id": "DOC-CARD-170",
        "icd10": "M48.06",
        "condition": "Lumbar Spinal Stenosis",
        "specialty": "Orthopedics",
        "organ_system": "Musculoskeletal",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NASS Evidence-Based Clinical Guideline",
        "source_body": "Spine J",
        "citation": "North American Spine Society. Evidence-based clinical guidelines for multidisciplinary spine care: Diagnosis and treatment of degenerative lumbar spinal stenosis. Spine J. 2013;13(4):e1-e6.",
        "doi_or_source": "10.1016/j.spinee.2012.11.059",
        "clinical_evidence": "Lumbar spinal stenosis involves narrowing of the central spinal canal, lateral recess, or neural foramina by degenerative bone and soft tissue changes (facet arthropathy, ligamentum flavum hypertrophy, disc bulging). Pathognomonic symptom is neurogenic claudication: bilateral or unilateral aching, heaviness, weakness, cramping, or numbness in the buttocks, thighs, or calves brought on by walking or prolonged standing, and characteristically relieved by sitting or lumbar flexion ('shopping cart sign'—forward leaning increases spinal canal cross-sectional area by up to 20%). It is distinguished from vascular claudication, which is provoked by bicycling (flexed posture) and relieved simply by standing still. Lumbosacral spine MRI confirms anatomical stenosis. Conservative management includes flexion-based physical therapy, NSAIDs, and epidural steroid injections. The landmark SPORT trial demonstrated that surgical decompression (laminectomy) produces significant and sustained improvement in pain and function in symptomatic patients failing conservative therapy.",
        "solution_protocol": {
            "non_pharmacological_targets": "Flexion-based core stabilization exercises; stationary bicycling or elliptical training (maintains lumbar spine flexion); use of assistive walking aids or rolling carts to reduce upright lordosis; structured weight loss.",
            "monitoring_cadence": "Walking distance tolerance assessment and Oswestry Disability Index (ODI) every 6-12 weeks; clinical surveillance for cauda equina syndrome.",
            "clinical_thresholds": "Progressive motor weakness (foot drop) or inability to walk > 50-100 meters despite 3-6 months of conservative management indicates surgical decompression."
        },
        "patient_plain_language": "Lumbar spinal stenosis is an age-related narrowing of the bone canal in your lower back that houses your nerves. Standing or walking upright pinches these nerves, causing aching heaviness, cramping, and fatigue in your legs and buttocks that goes away when you sit down or lean forward over a grocery cart.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my lower back MRI show central canal stenosis, lateral recess narrowing, or slipped vertebrae (spondylolisthesis)?",
            "safety_question": "What is the difference between my nerve-related leg symptoms and poor blood circulation in my leg arteries?",
            "action_threshold_question": "If walking becomes severely limited despite physical therapy and steroid injections, what does a minimally invasive decompression surgery involve?"
        },
        "red_flags": [
            "Loss of bowel or bladder control, numbness in the groin/buttocks saddle area, or sudden foot drop (Cauda Equina Syndrome Emergency)"
        ]
    },
    {
        "id": "DOC-CARD-171",
        "icd10": "B02.9",
        "condition": "Herpes Zoster (Shingles)",
        "specialty": "Infectious Disease",
        "organ_system": "Integumentary & Skin",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CDC/ACIP Recommendations / ZOE-50 RCT",
        "source_body": "N Engl J Med",
        "citation": "Lal H et al. Efficacy of an adjuvanted herpes zoster subunit vaccine in older adults (ZOE-50). N Engl J Med. 2015;372(22):2087-2096.",
        "doi_or_source": "10.1056/NEJMoa1501184",
        "clinical_evidence": "Herpes zoster results from reactivation of latent varicella-zoster virus (VZV) in dorsal root or cranial nerve ganglia. Classic presentation involves prodromal dermatomal pain, burning, or allodynia followed by a unilateral, dermatomal eruption of grouped, painful, erythematous maculopapules that rapidly evolve into clear vesicles. Antiviral therapy (valacyclovir 1,000 mg TID or famciclovir 500 mg TID for 7 days) initiated within 72 hours of rash onset accelerates lesion healing, reduces acute viral shedding, and decreases the severity and duration of postherpetic neuralgia (PHN: pain persisting > 90 days after rash onset). Landmark ZOE-50 and ZOE-70 randomized trials established that the 2-dose recombinant adjuvanted zoster vaccine (Shingrix) provides >97% protective efficacy against shingles and >91% protection against PHN in adults ≥ 50 years, with sustained immunity > 10 years. Herpes zoster ophthalmicus (involving CN V1) risks permanent corneal blindness.",
        "solution_protocol": {
            "non_pharmacological_targets": "Keep the rash clean and dry; cover lesions with non-adherent sterile dressings to prevent transmission to varicella-naive or immunocompromised individuals; avoid scratching; cool compresses.",
            "monitoring_cadence": "Clinical review at 7-10 days to ensure crusting; emergent ophthalmology evaluation if vesicles involve the tip or side of the nose (Hutchinson's sign) indicating ophthalmic division (V1) involvement; monitor for postherpetic neuralgia at 30, 60, and 90 days.",
            "clinical_thresholds": "Initiation of oral antivirals within 72 hours of vesicle eruption is the critical evidence-based window."
        },
        "patient_plain_language": "Shingles is a painful blistering rash caused by the chickenpox virus waking up after sleeping quietly in your nerve roots for decades. It typically forms a sensitive band of red blisters on just one side of your chest, back, or face, accompanied by burning nerve pain.",
        "doctor_consultation_checklist": {
            "parameter_question": "Has it been less than 72 hours since the first blisters appeared so I can start antiviral pills immediately?",
            "safety_question": "Does my rash involve my forehead, eye, or the tip of my nose requiring an emergency eye doctor exam?",
            "action_threshold_question": "Once this episode clears, when should I receive the 2-dose Shingrix vaccine to prevent shingles from ever returning?"
        },
        "red_flags": [
            "Blisters on the tip of the nose or around the eye (Hutchinson's sign indicating risk of blindness), or neck stiffness and high fever (zoster meningitis)"
        ]
    },
    {
        "id": "DOC-CARD-172",
        "icd10": "B27.00",
        "condition": "Infectious Mononucleosis (Epstein-Barr Virus)",
        "specialty": "Infectious Disease",
        "organ_system": "Immune & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review / Clinical Guideline",
        "source_body": "N Engl J Med",
        "citation": "Luzuriaga K, Sullivan JL. Infectious Mononucleosis. N Engl J Med. 2010;362(21):1993-2000.",
        "doi_or_source": "10.1056/NEJMcp1001116",
        "clinical_evidence": "Infectious mononucleosis is caused by Epstein-Barr virus (EBV / HHV-4), transmitted via infected saliva ('kissing disease'), peaking in adolescents and young adults aged 15-24 years. Classic clinical triad: fever, exudative pharyngitis, and prominent symmetric posterior cervical and generalized lymphadenopathy, frequently accompanied by marked fatigue, palatal petechiae, hepatosplenomegaly, and transient periorbital edema (Hoagland sign). Laboratory confirmation relies on heterophile antibody testing (Monospot test; sensitivity ~85%, can be false-negative in first week) and peripheral blood smear showing lymphocytosis (>50%) with >10% atypical activated CD8+ cytotoxic T lymphocytes. EBV-specific serologies (viral capsid antigen [VCA] IgM/IgG, EBNA) confirm atypical cases. Administration of aminopenicillins (amoxicillin, ampicillin) induces a characteristic pruritic maculopapular rash in >90% of patients. Splenic rupture occurs in 0.1-0.5% (typically between days 4 and 21 of illness).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict cessation of all contact sports, strenuous exercise, and heavy lifting for at least 3-4 weeks from symptom onset (or until splenomegaly fully resolves) to prevent traumatic splenic rupture; generous hydration; rest.",
            "monitoring_cadence": "Clinical reassessment at 2-3 weeks; abdominal palpation or ultrasound to evaluate spleen size before clearing athletes to return to contact sports.",
            "clinical_thresholds": "Absolute restriction from contact sports for minimum 21 days from symptom onset; systemic corticosteroids are indicated only for impending airway obstruction from severe tonsillar hypertrophy."
        },
        "patient_plain_language": "Infectious mononucleosis ('mono') is a viral infection caused by the Epstein-Barr virus, spread through saliva. It causes severe sore throat with swollen neck glands, fever, and extreme fatigue that can last for weeks, along with temporary enlargement of your spleen.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my Monospot test and blood smear show atypical lymphocytes?",
            "safety_question": "Why must I avoid taking amoxicillin or penicillin-type antibiotics during this illness to prevent a full-body rash?",
            "action_threshold_question": "What is the exact date when I can safely return to sports or the gym without risking rupture of my enlarged spleen?"
        },
        "red_flags": [
            "Sudden severe left upper belly pain or left shoulder tip pain (Kehr's sign indicating splenic rupture emergency), or difficulty breathing/swallowing saliva"
        ]
    },
    {
        "id": "DOC-CARD-173",
        "icd10": "J10.1",
        "condition": "Influenza Infection (Flu)",
        "specialty": "Infectious Disease",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Clinical Practice Guideline",
        "source_body": "Clin Infect Dis",
        "citation": "Uyeki TM et al. Clinical Practice Guidelines by the Infectious Diseases Society of America: 2018 Update on Diagnosis, Treatment, Chemoprophylaxis, and Institutional Outbreak Management of Seasonal Influenza. Clin Infect Dis. 2019;68(6):e1-e47.",
        "doi_or_source": "10.1093/cid/ciy866",
        "clinical_evidence": "Influenza is an acute respiratory infection caused by influenza A and B orthomyxoviruses, presenting abruptly with high fever (38-40°C), rigors, myalgias, prominent headache, dry cough, sore throat, and profound prostration. Rapid molecular assays (RT-PCR) are the preferred diagnostic test with high sensitivity/specificity (>95%). Neuraminidase inhibitors (oral oseltamivir 75 mg BID for 5 days) or the cap-dependent endonuclease inhibitor baloxavir marboxil (single oral dose) shorten symptom duration by ~1-1.5 days and reduce lower respiratory tract complications, otitis media, and hospitalizations when initiated within 48 hours of symptom onset. In hospitalized, severely ill, or high-risk patients (age ≥65, children <2, chronic cardiopulmonary disease, immunosuppressed, pregnant/postpartum), antiviral therapy is recommended as early as possible, regardless of duration of illness.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bed rest; liberal oral hydration; isolation from vulnerable contacts; annual influenza vaccination (universal recommendation for all persons ≥ 6 months of age).",
            "monitoring_cadence": "Clinical reassessment at 48-72 hours post-antiviral therapy; pulse oximetry checks; monitor for secondary bacterial pneumonia (biphasic fever, productive purulent sputum).",
            "clinical_thresholds": "Antiviral therapy should be initiated within 48 hours of illness onset for maximal clinical benefit; high-risk and hospitalized patients should be treated even after 48 hours."
        },
        "patient_plain_language": "Influenza, or the flu, is a highly contagious viral lung infection that strikes suddenly like a freight train, knocking you off your feet with a high fever, shaking chills, severe body aches, headache, and intense fatigue.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my molecular rapid flu swab confirm Influenza A or Influenza B?",
            "safety_question": "Am I within the 48-hour window from my first fever to start an antiviral pill like Tamiflu or Xofluza?",
            "action_threshold_question": "What warning signs indicate that I might be developing a secondary bacterial pneumonia in my lungs?"
        },
        "red_flags": [
            "Severe shortness of breath, blood-tinged sputum, chest pain when breathing, oxygen saturation < 92%, confusion, or a fever that breaks and then suddenly returns worse"
        ]
    },
    {
        "id": "DOC-CARD-174",
        "icd10": "B54",
        "condition": "Malaria (Plasmodium falciparum / vivax)",
        "specialty": "Infectious Disease",
        "organ_system": "Immune & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WHO Guidelines for Malaria / AQUAMAT & SEAQUAMAT Trials",
        "source_body": "The Lancet",
        "citation": "World Health Organization. WHO Guidelines for malaria. Geneva: World Health Organization; 2023. / Dondorp AM et al. Artesunate versus quinine in the treatment of severe falciparum malaria in African children (AQUAMAT): an open-label, randomised trial. Lancet. 2010;376(9753):1647-1657.",
        "doi_or_source": "10.1016/S0140-6736(10)61924-1",
        "clinical_evidence": "Malaria is a mosquito-borne protozoan infection caused by Plasmodium species (P. falciparum, P. vivax, P. ovale, P. malariae, P. knowlesi), transmitted by female Anopheles mosquitoes. Classic presentation features paroxysmal fevers, rigors, diaphoresis, headache, hemolytic anemia, and splenomegaly. Gold standard diagnosis requires microscopic examination of Giemsa-stained thick (sensitivity) and thin (species identification and parasitemia quantification) blood smears, repeated every 12-24 hours if initially negative. Uncomplicated P. falciparum is treated with Artemisinin-based Combination Therapy (ACT: oral artemether-lumefantrine [Coartem] or atovaquone-proguanil [Malarone]). Severe malaria (parasitemia > 5%, cerebral malaria, severe anemia, acute kidney injury, ARDS, lactic acidosis) requires immediate IV artesunate (2.4 mg/kg IV at 0, 12, and 24 hours), which reduced mortality by 35% in Asia (SEAQUAMAT) and 22% in Africa (AQUAMAT) compared to IV quinine. P. vivax and P. ovale require primaquine or tafenoquine to eradicate dormant liver hypnozoites, mandatory after G6PD deficiency screening.",
        "solution_protocol": {
            "non_pharmacological_targets": "Bed nets treated with long-lasting insecticidal netting (LLINs); indoor residual spraying; insect repellent with DEET (20-50%); chemoprophylaxis adherence for travelers to endemic areas.",
            "monitoring_cadence": "Serial blood smears every 12-24 hours until parasitemia clears; G6PD screening prior to 8-aminoquinoline (primaquine/tafenoquine) administration; delayed hemolytic anemia monitoring at 2-4 weeks post-artesunate.",
            "clinical_thresholds": "Parasitemia > 5%, impaired consciousness (Glasgow Coma Scale < 11), jaundice with bilirubin > 3 mg/dL, or serum creatinine > 3 mg/dL classifies as Severe Malaria requiring IV artesunate in ICU."
        },
        "patient_plain_language": "Malaria is a serious, mosquito-transmitted blood infection caused by microscopic parasites that multiply inside your liver and then burst out into your red blood cells. It causes intense cycling waves of shaking chills followed by high, burning fevers and drenching sweats.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my identified Plasmodium species and exact blood parasitemia percentage on my thin smear?",
            "safety_question": "Was my G6PD enzyme level tested before starting primaquine pills to clear the dormant parasites from my liver?",
            "action_threshold_question": "Does my infection show any features of severe malaria requiring intravenous artesunate in the hospital?"
        },
        "red_flags": [
            "Altered mental status, confusion, seizures (cerebral malaria), extreme shortness of breath (ARDS), dark brown/black urine ('blackwater fever'), or inability to sit up"
        ]
    },
    {
        "id": "DOC-CARD-175",
        "icd10": "A90",
        "condition": "Dengue Fever",
        "specialty": "Infectious Disease",
        "organ_system": "Immune & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: WHO Comprehensive Guidelines for Dengue",
        "source_body": "N Engl J Med",
        "citation": "Simmons CP, Farrar JJ, Nguyen vV, Wills B. Dengue. N Engl J Med. 2012;366(15):1423-1432.",
        "doi_or_source": "10.1056/NEJMra1110265",
        "clinical_evidence": "Dengue is an arboviral infection caused by 4 distinct serotypes (DENV-1 to 4) transmitted by diurnal Aedes aegypti and Aedes albopictus mosquitoes. Classic 'breakbone fever' features sudden high fever (up to 40°C), severe retro-orbital headache, diffuse arthralgias/myalgias, and a transient macular rash. Diagnosis is confirmed by serum NS1 antigen or RT-PCR within days 1-5, or IgM serology after day 5. The disease progresses through 3 phases: Febrile (days 1-3), Critical (days 3-7, coinciding with defervescence when capillary permeability peaks), and Recovery. Severe dengue (dengue hemorrhagic fever / dengue shock syndrome) is characterized by severe plasma leakage (defined by hematocrit increase ≥ 20% alongside acute thrombocytopenia < 100,000 cells/µL, or narrow pulse pressure ≤ 20 mmHg), severe bleeding, or severe organ impairment. Management during the critical phase hinges on meticulous, protocolized isotonic IV fluid titration to match microvascular leakage without precipitating pulmonary edema. NSAIDs and aspirin are strictly contraindicated due to antiplatelet effects and bleeding risk.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of all NSAIDs (ibuprofen, naproxen, aspirin); exclusively use acetaminophen (max 3 g/day) for fever; liberal oral rehydration with electrolyte solutions; mosquito repellent and bed netting.",
            "monitoring_cadence": "Daily CBC monitoring hematocrit and platelet count during febrile and critical phases (especially days 3-7 when fever subsides); frequent blood pressure and pulse pressure checks.",
            "clinical_thresholds": "Warning signs: severe abdominal pain, persistent vomiting, mucosal bleeding, lethargy, fluid accumulation (pleural effusion/ascites), liver enlargement > 2 cm, or acute rise in hematocrit with rapid drop in platelets."
        },
        "patient_plain_language": "Dengue fever, known as 'breakbone fever' due to the intense pain in your muscles and joints, is a mosquito-spread tropical virus. The most critical window happens right as the high fever breaks (days 3 to 7), when blood vessels can suddenly become leaky.",
        "doctor_consultation_checklist": {
            "parameter_question": "What is my daily hematocrit and platelet count, and are my blood counts showing signs of plasma leakage?",
            "safety_question": "Have I been advised to completely avoid ibuprofen, Advil, and aspirin to protect me from severe bleeding?",
            "action_threshold_question": "What specific warning signs (like belly pain, vomiting, or nosebleeds) mean I need to be admitted to the hospital immediately?"
        },
        "red_flags": [
            "Narrow pulse pressure (systolic minus diastolic BP ≤ 20 mmHg) or hypotension (dengue shock), persistent vomiting, bleeding from gums/GI tract, or extreme drowsiness"
        ]
    },
    {
        "id": "DOC-CARD-176",
        "icd10": "L08.9",
        "condition": "Community-Acquired MRSA Skin Infection",
        "specialty": "Infectious Disease",
        "organ_system": "Integumentary & Skin",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Practice Guidelines / DAWN RCT",
        "source_body": "N Engl J Med",
        "citation": "Daum RS, Miller LG, Immergluck L, et al. A Placebo-Controlled Trial of Antibiotics for Smaller Skin Abscesses. N Engl J Med. 2017;376(26):2545-2555.",
        "doi_or_source": "10.1056/NEJMoa1607033",
        "clinical_evidence": "Community-associated methicillin-resistant Staphylococcus aureus (CA-MRSA) typically presents as a painful, erythematous, fluctuant skin abscess, furuncle, carbuncle, or purulent cellulitis, often carrying the Panton-Valentine leukocidin (PVL) cytotoxin gene. Landmark randomized trials establish that incision and drainage (I&D) is the primary and essential definitive therapy for cutaneous abscesses. The landmark DAWN trial proved that adding oral antibiotic therapy (trimethoprim-sulfamethoxazole [TMP-SMX 1-2 DS tablets BID] or clindamycin [300-450 mg TID] for 7-10 days) significantly increased cure rates (82-83% vs 69% placebo, p<0.001) and reduced recurrence rates in drainable abscesses. Oral doxycycline (100 mg BID) is an alternative. For recurrent CA-MRSA furunculosis, a 5-day decolonization protocol (intranasal mupirocin 2% ointment BID plus chlorhexidine 4% body washes daily) significantly reduces reinfection and household transmission.",
        "solution_protocol": {
            "non_pharmacological_targets": "Do not squeeze or self-drain boils at home; keep draining wounds covered with clean, dry dressings; wash towels and bed linens in hot water; avoid sharing personal items (razors, towels); regular hand washing.",
            "monitoring_cadence": "Clinical wound reassessment at 48 hours post-incision and drainage; wound culture and susceptibility testing; reassess if surrounding erythema expands beyond marked pen margin.",
            "clinical_thresholds": "Systemic inflammatory response syndrome (fever > 38°C, tachycardia > 90 bpm, tachypnea), rapid progression, or immunocompromise mandates systemic antimicrobial therapy."
        },
        "patient_plain_language": "A MRSA skin abscess is a bacterial infection of the skin that forms a tender, pus-filled boil, often mistaken for a spider bite. Because MRSA is resistant to ordinary penicillins, the boil must be cleanly drained by a clinician and treated with targeted antibiotics.",
        "doctor_consultation_checklist": {
            "parameter_question": "Was my wound culture sent to the lab to verify that it is MRSA and identify which antibiotics work best?",
            "safety_question": "Does my abscess need a complete office drainage procedure rather than just antibiotic pills alone?",
            "action_threshold_question": "If boils keep coming back, should my household follow a chlorhexidine soap and mupirocin nasal decolonization regimen?"
        },
        "red_flags": [
            "Rapidly spreading red streaking from the wound, high fever, low blood pressure, or extreme pain out of proportion to exam (necrotizing fasciitis warning)"
        ]
    },
    {
        "id": "DOC-CARD-177",
        "icd10": "A06.9",
        "condition": "Giardiasis",
        "specialty": "Infectious Disease",
        "organ_system": "Digestive & Hepatobiliary",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Cochrane Systematic Review / CDC Guidelines",
        "source_body": "Cochrane Database Syst Rev",
        "citation": "Gardner TB, Hill DR. Treatment of giardiasis. Clin Microbiol Rev. 2001;14(1):114-128. / Solaymani-Mohammadi S et al. Cochrane Database Syst Rev. 2010;(5):CD007787.",
        "doi_or_source": "10.1128/CMR.14.1.114-128.2001",
        "clinical_evidence": "Giardiasis is an intestinal protozoan infection caused by Giardia duodenalis (lamblia/intestinalis), acquired via ingestion of fecally contaminated water (backcountry hikers drinking wilderness stream water, municipal water supplies, swimming pools) or food. Ingested cysts excyst in the duodenum into flagellated trophozoites that attach to the enterocyte brush border with a ventral sucking disk, causing blunting of microvilli and malabsorption. Incubation period is 1-2 weeks, presenting with foul-smelling, watery, greasy stools that float (steatorrhea), sulfurous burping/eructations, abdominal cramping, flatulence, and significant weight loss, characteristically without fever or blood/fecal leukocytes. Diagnosis is established via stool stool antigen enzyme immunoassay (EIA) or stool multiplex PCR (sensitivity >95%). First-line therapy is tinidazole (single oral dose of 2 g; cure rate >90-95%) or nitazoxanide (500 mg BID for 3 days), which have superseded 5-7 day metronidazole due to superior tolerability and single-dose compliance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Boil wilderness water for at least 1 full minute (or 3 minutes at high altitude) or use <1-micron pore size water filters; practice strict hand hygiene after diaper changing; avoid swallowing recreational pool or lake water.",
            "monitoring_cadence": "Clinical symptom resolution at 2 weeks; repeat stool antigen testing only if symptoms fail to resolve or recur; temporary lactose avoidance for 4-6 weeks (due to transient post-infectious secondary lactase deficiency).",
            "clinical_thresholds": "Stool antigen EIA or PCR positive for Giardia duodenalis confirms diagnosis and directs anti-protozoal therapy."
        },
        "patient_plain_language": "Giardiasis, sometimes called 'beaver fever', is a microscopic parasite infection in your intestines picked up by drinking untreated wilderness stream water or unpurified water. It causes foul-smelling, greasy diarrhea that floats, lots of gas, and characteristic 'rotten egg' burps.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my stool PCR or antigen test confirm active Giardia parasites?",
            "safety_question": "Can I take a single 2-gram dose of tinidazole, which cures over 90% of cases in just one day with fewer side effects than metronidazole?",
            "action_threshold_question": "Should I temporarily avoid dairy milk and ice cream for a few weeks while my intestinal brush border heals?"
        },
        "red_flags": [
            "Severe dehydration with postural dizziness, rapid severe weight loss, or persistent diarrhea lasting > 4 weeks without diagnostic evaluation"
        ]
    },
    {
        "id": "DOC-CARD-178",
        "icd10": "J02.0",
        "condition": "Streptococcal Pharyngitis (Strep Throat)",
        "specialty": "Infectious Disease",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA Clinical Practice Guideline",
        "source_body": "Clin Infect Dis",
        "citation": "Shulman ST et al. Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update by the IDSA. Clin Infect Dis. 2012;55(10):e86-e102.",
        "doi_or_source": "10.1093/cid/cis629",
        "clinical_evidence": "Group A Streptococcus (Streptococcus pyogenes, GAS) accounts for 20-30% of acute pharyngitis in children and 5-15% in adults. Clinical features are scored via Modified Centor / McIsaac criteria (tonsillar exudates, tender anterior cervical lymphadenopathy, fever > 38°C, absence of cough, age-based points). Patients meeting ≥ 2-3 points should undergo Rapid Antigen Detection Testing (RADT) or throat throat molecular NAAT; negative RADT in children/adolescents mandates backup throat culture. Antimicrobial therapy is indicated only for confirmed GAS to prevent acute rheumatic fever, reduce symptom duration by ~1-2 days, and prevent suppurative complications (peritonsillar abscess). Penicillin V (500 mg orally BID/TID for 10 days) or amoxicillin (50 mg/kg once daily, max 1,000 mg for 10 days) remains first-line, as GAS remains 100% susceptible to beta-lactams globally. Cephalosporins, clindamycin, or azithromycin serve as penicillin-allergic options.",
        "solution_protocol": {
            "non_pharmacological_targets": "Replace toothbrush after 24-48 hours of antibiotic therapy; salt-water gargles; warm fluids and honey; return to school/work after 12-24 hours of effective antibiotics and when afebrile.",
            "monitoring_cadence": "Clinical improvement within 48-72 hours; follow-up throat cultures are strictly not indicated in asymptomatic patients post-treatment.",
            "clinical_thresholds": "Positive rapid strep antigen test or throat culture mandates full 10-day course of penicillin/amoxicillin to prevent acute rheumatic fever."
        },
        "patient_plain_language": "Strep throat is a contagious bacterial throat infection caused by Group A Streptococcus bacteria. It typically causes sudden severe throat pain when swallowing, swollen red tonsils with white patches of pus, and fever, noticeably without cold symptoms like a runny nose or cough.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my rapid throat swab test positive for Group A Strep bacteria?",
            "safety_question": "Why is it essential to complete all 10 days of penicillin or amoxicillin even after my throat feels completely fine within 2 days?",
            "action_threshold_question": "If I have a penicillin allergy, which safe alternative antibiotic (like a cephalosporin or clindamycin) should I take?"
        },
        "red_flags": [
            "Inability to swallow saliva (drooling), muffled 'hot potato' voice, severe asymmetric tonsil swelling with uvula deviation (peritonsillar abscess), or difficulty breathing"
        ]
    },
    {
        "id": "DOC-CARD-179",
        "icd10": "A69.20",
        "condition": "Lyme Disease (Borrelia burgdorferi)",
        "specialty": "Infectious Disease",
        "organ_system": "Immune & Lymphatic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: IDSA/AAN/ACR Clinical Practice Guidelines",
        "source_body": "Clin Infect Dis",
        "citation": "Lantos PM et al. Clinical Practice Guidelines by the IDSA, AAN, and ACR: 2020 Guidelines for the Prevention, Diagnosis, and Treatment of Lyme Disease. Clin Infect Dis. 2021;72(1):e1-e48.",
        "doi_or_source": "10.1093/cid/ciaa1215",
        "clinical_evidence": "Lyme disease is a tick-borne spirochetal infection caused by Borrelia burgdorferi sensu stricto (in North America), transmitted by Ixodes scapularis and Ixodes pacificus blacklegged ticks attached for ≥ 36-48 hours. Stage 1 (Early localized): Erythema migrans (EM) rash (expanding annular erythematous patch ≥ 5 cm, often with central clearing / 'bull's-eye') appears 7-14 days post-bite. Diagnosis of EM in an endemic area is purely clinical; serology is insensitive (<40%) in early localized disease and should not be ordered. Stage 2 (Early disseminated): Multiple EM lesions, cranial neuropathy (unilateral or bilateral Bell's palsy), lymphocytic meningitis, or Lyme carditis (AV heart block). Stage 3 (Late): Asymmetric, migratory mono/oligoarthritis (prominently knee). Standard two-tier serologic testing (EIA screen followed by Western blot or second EIA) confirms disseminated/late disease. Oral doxycycline (100 mg BID for 10-14 days) is first-line; amoxicillin (500 mg TID for 14 days) or cefuroxime are alternatives.",
        "solution_protocol": {
            "non_pharmacological_targets": "Tick prevention: wear permethrin-treated clothing, apply 20-30% DEET, perform full-body tick checks within 2 hours of outdoor exposure; remove embedded ticks promptly using fine-tipped tweezers pulling straight out without twisting.",
            "monitoring_cadence": "Clinical follow-up for complete resolution of erythema migrans and systemic symptoms; post-treatment antibody testing is contraindicated because IgG antibodies persist for years.",
            "clinical_thresholds": "A single dose of oral doxycycline (200 mg within 72 hours of tick removal) provides effective post-exposure prophylaxis if tick was attached ≥ 36 hours in a high-endemic area."
        },
        "patient_plain_language": "Lyme disease is a bacterial infection spread by the bite of an infected blacklegged deer tick. The classic first sign is an expanding red rash that often resembles a target or 'bull's-eye', accompanied by flu-like fatigue, headaches, fever, and achy joints.",
        "doctor_consultation_checklist": {
            "parameter_question": "Does my expanding red skin lesion meet the clinical definition of erythema migrans (at least 5 cm across)?",
            "safety_question": "Why is blood antibody testing not recommended for a fresh bull's-eye rash, since it takes weeks for antibodies to show up?",
            "action_threshold_question": "What is my planned antibiotic course (10 to 14 days of oral doxycycline), and are my heart rhythm and facial nerves normal?"
        },
        "red_flags": [
            "Sudden fainting, dizziness, or slow heart rate (Lyme carditis / AV block), severe neck stiffness with light sensitivity (meningitis), or facial drooping"
        ]
    },
    {
        "id": "DOC-CARD-180",
        "icd10": "A41.9",
        "condition": "Sepsis and Septic Shock",
        "specialty": "Critical Care",
        "organ_system": "Circulatory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Surviving Sepsis Campaign International Guidelines",
        "source_body": "Crit Care Med",
        "citation": "Evans L et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit Care Med. 2021;49(11):e1063-e1143.",
        "doi_or_source": "10.1097/CCM.0000000000005337",
        "clinical_evidence": "Sepsis-3 consensus defines sepsis as life-threatening organ dysfunction caused by a dysregulated host response to infection, clinically quantified by an acute increase in SOFA (Sequential Organ Failure Assessment) score ≥ 2 points. Septic shock is a subset characterized by profound circulatory, cellular, and metabolic abnormalities, defined by persistent hypotension requiring vasopressors to maintain MAP ≥ 65 mmHg and serum lactate > 2 mmol/L despite adequate fluid resuscitation, carrying mortality > 40%. The 1-Hour Sepsis Bundle mandates: (1) measure serum lactate level (remeasure if initial > 2 mmol/L), (2) obtain blood cultures prior to antibiotics, (3) administer broad-spectrum IV antimicrobials within 1 hour, (4) rapidly infuse 30 mL/kg of balanced crystalloids (e.g., Plasmalyte or Lactated Ringer's) for hypotension or lactate ≥ 4 mmol/L, and (5) initiate norepinephrine as first-line vasopressor if MAP remains < 65 mmHg during or after fluid loading.",
        "solution_protocol": {
            "non_pharmacological_targets": "Rapid source identification and surgical/percutaneous source control (e.g., abscess drainage, debridement of infected tissue, removal of infected vascular catheters) within 6-12 hours of presentation.",
            "monitoring_cadence": "Continuous arterial line blood pressure monitoring, pulse oximetry, hourly urine output (targeting > 0.5 mL/kg/hr); repeat serum lactate every 2-4 hours until normalized to assess clearance.",
            "clinical_thresholds": "Target mean arterial pressure (MAP) ≥ 65 mmHg; serum lactate clearance (>20% reduction every 2 hours) serves as dynamic surrogate of tissue perfusion."
        },
        "patient_plain_language": "Sepsis is a medical emergency that happens when your body's immune system has an extreme, overwhelming response to an infection. Instead of just fighting the germs, the immune system triggers widespread inflammation that can drop your blood pressure dangerously low and damage vital organs.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my initial blood lactate level and what is my current mean arterial blood pressure (MAP)?",
            "safety_question": "Were blood cultures drawn before starting intravenous broad-spectrum antibiotics, and have broad fluids been infused?",
            "action_threshold_question": "Has the specific source of infection (such as the lungs, urinary tract, or abdomen) been definitively identified and treated?"
        },
        "red_flags": [
            "Systolic blood pressure < 90 mmHg, mottled cold extremities, confusion or inability to stay awake, breathing rate > 25 breaths/min, or no urine output"
        ]
    }
]