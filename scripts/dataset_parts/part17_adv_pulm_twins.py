"""
part17_adv_pulm_twins.py
"""

PART_17_DISEASES = [
    {
        "id": "DOC-CARD-421",
        "icd10": "J80",
        "condition": "Acute Respiratory Distress Syndrome (ARDS - Berlin Definition)",
        "specialty": "Critical Care & Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ARDSNet & PROSEVA Landmark Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "Guerin C et al. Prone Positioning in Severe Acute Respiratory Distress Syndrome (PROSEVA). N Engl J Med. 2013;368(23):2159-2168.",
        "doi_or_source": "10.1056/NEJMoa1214103",
        "clinical_evidence": "The landmark ARDSNet trial established low tidal volume lung-protective ventilation (6 mL/kg predicted body weight, plateau pressure <30 cmH2O), cutting mortality from 39.8% to 31.0% (p=0.007). In severe ARDS (PaO2/FiO2 <150), early prolonged prone positioning (>=16 hours/day; PROSEVA trial, n=466) reduced 28-day mortality from 32.8% to 16.0% (hazard ratio 0.39; p<0.001).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict lung-protective ventilation (4-6 mL/kg PBW, plateau pressure <=30 cmH2O, driving pressure <=14 cmH2O); prone positioning >=16 hours daily for PaO2/FiO2 <150; conservative fluid management strategy (FACTT trial); neuromuscular blockade for patient-ventilator dyssynchrony.",
            "monitoring_cadence": "Continuous arterial blood gas monitoring every 2-4 hours; continuous pulse oximetry targeting SpO2 88-92%; plateau and driving pressure measurements every 4 hours.",
            "clinical_thresholds": "PaO2/FiO2 ratio: Mild (200-300), Moderate (100-200), Severe (<100 mmHg) with PEEP >=5 cmH2O and bilateral opacities not fully explained by heart failure."
        },
        "patient_plain_language": "A severe, life-threatening lung inflammation that develops rapidly after pneumonia, sepsis, or severe trauma. The microscopic air sacs (alveoli) fill with inflammatory fluid and collapse, preventing oxygen from crossing into your blood. Patients need a breathing machine set to gentle low volumes and lying on their stomach (proning) to open healthy lung areas.",
        "doctor_consultation_checklist": {
            "parameter_question": "Is the ventilator set to low tidal volume (6 mL/kg ideal body weight) to avoid tearing delicate lung tissue?",
            "safety_question": "Has prone positioning (turning onto the stomach for at least 16 hours a day) been initiated for severe oxygen drops?",
            "action_threshold_question": "Is a conservative fluid strategy being used to keep excess water out of the healing lungs?"
        },
        "red_flags": [
            "Severe refractory hypoxemia with PaO2/FiO2 <80 despite 100% oxygen and prone positioning (VV-ECMO evaluation)",
            "Sudden unilateral loss of breath sounds indicating tension pneumothorax from barotrauma"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "ARDS is severe, rapid fluid buildup in the lung air sacs caused by systemic inflammation or infection.",
                "plain_analogy": "A sponge dropped in muddy water that becomes heavy, waterlogged, and incapable of absorbing air.",
                "lifestyle_action": "Requires emergency intensive care unit management with mechanical ventilation and prone positioning."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Lung-Protective Mechanical Ventilation (First Line)",
                    "Inhaled Epoprostenol / Nitric Oxide (Refractory Hypoxemia)",
                    "Neuromuscular Blockade (Cisatracurium)"
                ],
                "dosing_gdmt": "Ventilator tidal volume 6 mL/kg PBW; cisatracurium continuous infusion 37.5 mg/h for severe dyssynchrony.",
                "black_box_warning": "Avoid fluid overload; liberal fluid management worsens ventilator-free days and ICU stay.",
                "organ_clearance_cutoffs": "Dose adjustments based on continuous arterial blood gas analysis and kidney clearance."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "PROSEVA-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1214103",
                "cebm_level": 2,
                "sample_size": 466,
                "endpoints": "Prone positioning for >=16 hours daily halves 28-day mortality in severe ARDS (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-422",
        "icd10": "J47.9",
        "condition": "Non-Cystic Fibrosis Bronchiectasis (Chronic Airway Dilation)",
        "specialty": "Pulmonology & Infectious Disease",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: BTS Bronchiectasis Guidelines & EMBRACE Trial",
        "source_body": "Thorax & Lancet Respiratory Medicine",
        "citation": "Hill AT et al. British Thoracic Society Guideline for Bronchiectasis in Adults. Thorax. 2019;74(Suppl 1):1-69.",
        "doi_or_source": "10.1136/thoraxjnl-2018-212463",
        "clinical_evidence": "Chronic airway clearance techniques combined with long-term macrolide maintenance therapy (Azithromycin 250-500 mg 3x/week; EMBRACE and BAT trials) reduces annual exacerbation frequency by >50% and improves quality of life. Inhaled hypertonic saline (3-7%) facilitates mucociliary clearance; sputum culture screening guides targeted eradication of Pseudomonas aeruginosa.",
        "solution_protocol": {
            "non_pharmacological_targets": "Airway clearance techniques (oscillating positive expiratory pressure / flutter valve, active cycle of breathing) twice daily; pulmonary rehabilitation; annual influenza, COVID-19, and pneumococcal vaccinations; adequate hydration.",
            "monitoring_cadence": "High-resolution chest CT (HRCT showing bronchoarterial ratio >1.0 / 'signet ring' sign); sputum cultures at every clinic visit and during flares.",
            "clinical_thresholds": "Presence of Pseudomonas aeruginosa colonization in sputum warrants prompt eradication attempt with inhaled colistin/tobramycin and oral ciprofloxacin."
        },
        "patient_plain_language": "Your breathing tubes (bronchi) have become permanently stretched out, widened, and scarred from recurrent infections. Because these widened airways lose their natural sweepers (cilia), thick mucus pools inside them like stagnant water in an old pipe, creating a breeding ground for chronic cough, bacteria, and recurrent chest infections.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did high-resolution chest CT (HRCT) confirm bronchiectasis with signet-ring airway widening?",
            "safety_question": "What specific bacteria (such as Pseudomonas aeruginosa) were identified in my latest sputum culture?",
            "action_threshold_question": "Am I using an airway clearing flutter device daily and taking preventive azithromycin to stop flares?"
        },
        "red_flags": [
            "Coughing up gross blood (>100 mL/day - Massive Hemoptysis requiring bronchial artery embolization)",
            "Acute severe breathlessness with purulent green sputum and high fever"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bronchiectasis is permanent widening and scarring of breathing tubes leading to pooled mucus and infections.",
                "plain_analogy": "An old, stretched-out garden hose with permanent bulges where dirty water collects and breeds bacteria.",
                "lifestyle_action": "Perform chest airway clearance twice daily, stay hydrated, and take prescribed anti-infective medications."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Azithromycin oral (Maintenance 250 mg 3x/week)",
                    "Hypertonic Saline 7% Nebulized",
                    "Inhaled Tobramycin / Colistin (for Pseudomonas)"
                ],
                "dosing_gdmt": "Azithromycin 250 mg orally three times weekly (Mon/Wed/Fri); Nebulized 7% Hypertonic Saline BID.",
                "black_box_warning": "Rule out non-tuberculous mycobacteria (NTM) before starting azithromycin (prevents macrolide resistance).",
                "organ_clearance_cutoffs": "Monitor hearing and hepatic function during long-term macrolide use."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "EMBRACE-TRIAL",
                "pmid_or_doi": "10.1016/S1473-3099(12)70104-1",
                "cebm_level": 2,
                "sample_size": 141,
                "endpoints": "Maintenance azithromycin significantly reduces pulmonary exacerbations in bronchiectasis (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-423",
        "icd10": "E84.0",
        "condition": "Cystic Fibrosis (CFTR Modulator Triplet Therapy)",
        "specialty": "Pulmonology & Medical Genetics",
        "organ_system": "Respiratory & Digestive",
        "cebm_level": 1,
        "evidence_tier": "Level 1: Trikafta Landmark Trial & CFF Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Middleton PG et al. Elexacaftor-Tezacaftor-Ivacaftor for Cystic Fibrosis with a Phe508del Allele. N Engl J Med. 2019;381(19):1809-1819.",
        "doi_or_source": "10.1056/NEJMoa1908639",
        "clinical_evidence": "The transformative phase 3 trial of triple CFTR modulator therapy (Elexacaftor-Tezacaftor-Ivacaftor / Trikafta, n=403) produced unprecedented clinical breakthroughs: a 14.3 percentage-point increase in percent predicted FEV1 (p<0.001), 63% reduction in pulmonary exacerbations, and sweat chloride reduction of 41.8 mmol/L in patients with at least one F508del mutation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Daily high-calorie, high-fat diet with fat-soluble vitamin (A, D, E, K) supplementation; pancreatic enzyme replacement therapy (PERT) with all meals/snacks; daily airway clearance therapy (high-frequency chest compression vest); regular aerobic exercise.",
            "monitoring_cadence": "Quarterly clinic visits measuring spirometry (FEV1), sputum cultures, and BMI; annual screening for CF-related diabetes (OGTT) and CF liver disease (LFTs and ultrasound).",
            "clinical_thresholds": "Sweat chloride >=60 mmol/L or two disease-causing CFTR mutations confirms CF diagnosis."
        },
        "patient_plain_language": "A genetic condition affecting a microscopic salt channel (CFTR). Because salt cannot move normally, mucus everywhere in your body becomes abnormally thick and sticky like dry glue. It blocks your airways causing severe lung damage and plugs your pancreas so you cannot digest food without enzyme pills.",
        "doctor_consultation_checklist": {
            "parameter_question": "Do I carry at least one F508del CFTR mutation making me eligible for triple modulator therapy (Trikafta)?",
            "safety_question": "What is my current FEV1 breathing percentage and sweat chloride level on Trikafta?",
            "action_threshold_question": "Am I taking sufficient pancreatic enzyme capsules with every meal and snack to absorb fats and vitamins?"
        },
        "red_flags": [
            "Sudden sharp chest pain with breathlessness (spontaneous pneumothorax from subpleural bleb rupture)",
            "Massive hemoptysis (>200 mL of bright red blood coughed up in 24 hours)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Cystic fibrosis is a genetic disease causing abnormally thick, sticky mucus in the lungs and digestive organs.",
                "plain_analogy": "A factory lubrication line where the fluid has turned into sticky molasses, gumming up all the machinery.",
                "lifestyle_action": "Take Trikafta with fat-containing meals, perform vest airway clearance daily, and take digestive enzymes."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Elexacaftor/Tezacaftor/Ivacaftor (Trikafta)",
                    "Pancrelipase (Creon / Zenpep)",
                    "Dornase Alfa (Pulmozyme nebulized)",
                    "Inhaled Tobramycin"
                ],
                "dosing_gdmt": "Trikafta: two morning tablets (fixed-dose elexacaftor/tezacaftor/ivacaftor) with fat-containing meal; one evening ivacaftor tablet.",
                "black_box_warning": "Trikafta requires baseline and quarterly liver function tests; potential cataracts in pediatric patients.",
                "organ_clearance_cutoffs": "Dose reduction with moderate/strong CYP3A4 inhibitors (e.g., ketoconazole, fluconazole)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "TRIKAFTA-PHE508",
                "pmid_or_doi": "10.1056/NEJMoa1908639",
                "cebm_level": 2,
                "sample_size": 403,
                "endpoints": "Trikafta produces 14.3% absolute FEV1 improvement and reduces pulmonary exacerbations by 63%."
            }
        }
    },
    {
        "id": "DOC-CARD-424",
        "icd10": "D86.0",
        "condition": "Pulmonary Sarcoidosis (Non-Caseating Granulomatous Disease)",
        "specialty": "Pulmonology & Rheumatology",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATS Clinical Practice Guideline on Sarcoidosis",
        "source_body": "American Journal of Respiratory and Critical Care Medicine",
        "citation": "Crouser ED et al. Diagnosis and Detection of Sarcoidosis: An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;201(8):e26-e51.",
        "doi_or_source": "10.1164/rccm.202002-0251ST",
        "clinical_evidence": "Asymptomatic Stage I sarcoidosis (bilateral hilar lymphadenopathy alone) undergoes spontaneous remission in >60-80% of cases and requires observation without steroids. Symptomatic Stage II-IV pulmonary sarcoidosis or dangerous extrapulmonary involvement (cardiac, neuro, ocular, or hypercalcemia) mandates Oral Prednisone (20-40 mg/day with slow taper). Methotrexate is the first-line steroid-sparing agent; Infliximab for refractory disease.",
        "solution_protocol": {
            "non_pharmacological_targets": "Avoid calcium and vitamin D supplements (sarcoid granulomas express 1-alpha-hydroxylase, synthesizing excess active 1,25-OH vitamin D causing hypercalcemia and kidney stones); sun protection; smoking cessation.",
            "monitoring_cadence": "Annual screening for silent cardiac sarcoidosis with 12-lead ECG; baseline comprehensive eye exam; serial pulmonary function tests (FVC, DLCO) every 3-6 months; serum calcium and 24-hour urine calcium.",
            "clinical_thresholds": "Bilateral hilar adenopathy on chest X-ray with non-caseating granulomas on endobronchial ultrasound (EBUS) biopsy, after excluding tuberculosis and fungal infection."
        },
        "patient_plain_language": "Your immune cells cluster together to form microscopic clumps of inflammation called granulomas, most often in the lymph nodes and tissue of your lungs. Many patients have a mild form that clears up entirely on its own. However, if it affects lung breathing, vision, or heart rhythm, steroid pills are used to calm the inflammation.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my lymph node biopsy confirm non-caseating granulomas and completely rule out tuberculosis and fungal infections?",
            "safety_question": "Have I had an ECG or cardiac MRI to check for hidden electrical inflammation in my heart muscle?",
            "action_threshold_question": "Are my blood and urine calcium levels normal, and why must I avoid over-the-counter vitamin D supplements?"
        },
        "red_flags": [
            "Palpitations, lightheadedness, or syncope (Cardiac Sarcoidosis with life-threatening ventricular arrhythmia)",
            "Sudden loss of visual acuity, eye redness, or severe pain (Anterior/Posterior Uveitis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Sarcoidosis is an immune condition where tiny clumps of inflammatory cells form in the lungs and other organs.",
                "plain_analogy": "Small knots of scar tissue and lint gathering inside the fine filters of an air conditioner.",
                "lifestyle_action": "Avoid extra vitamin D and calcium, attend regular eye and heart checkups, and take prescribed medicines."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral (First Line for active disease)",
                    "Methotrexate oral/subQ (Steroid-sparing)",
                    "Infliximab (Anti-TNF for refractory)"
                ],
                "dosing_gdmt": "Prednisone 20-40 mg daily for 4-12 weeks, followed by slow taper to 5-10 mg daily; Methotrexate 10-20 mg once weekly.",
                "black_box_warning": "Long-term corticosteroids risk osteoporosis, diabetes, and infection; add bisphosphonates for chronic use.",
                "organ_clearance_cutoffs": "Methotrexate requires monthly liver enzymes and CBC; contraindicated in severe renal failure."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS-SARCOID",
                "pmid_or_doi": "10.1164/rccm.202002-0251ST",
                "cebm_level": 1,
                "sample_size": 2800,
                "endpoints": "Observation alone is successful in 75% of Stage I disease; oral prednisone halts lung decline in active stages."
            }
        }
    },
    {
        "id": "DOC-CARD-425",
        "icd10": "J67.9",
        "condition": "Chronic Hypersensitivity Pneumonitis (Bird Fancier / Farmer's Lung)",
        "specialty": "Pulmonology & Occupational Medicine",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATS/JRS/ALAT Guideline on Hypersensitivity Pneumonitis",
        "source_body": "American Journal of Respiratory and Critical Care Medicine",
        "citation": "Raghu G et al. Diagnosis of Hypersensitivity Pneumonitis: An Official ATS/JRS/ALAT Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;202(3):e36-e69.",
        "doi_or_source": "10.1164/rccm.202005-2032ST",
        "clinical_evidence": "COMPLETE ANTIGEN REMOVAL is the single most critical intervention; continuing exposure causes irreversible progression to fibrotic HP with poor survival. Bronchoalveolar lavage (BAL) showing marked lymphocytic alveolitis (>20-30% lymphocytes, often >50%) and HRCT showing the 'three-density sign' (combination of ground-glass, normal lung, and air-trapping mosaicism) establishes diagnosis. Systemic corticosteroids for non-fibrotic flares.",
        "solution_protocol": {
            "non_pharmacological_targets": "Identify and completely eliminate inciting organic antigen (pigeons, parakeets, down feather pillows/comforters, hot tubs, contaminated HVAC/humidifiers, moldy hay); use HEPA air purifiers; professional mold remediation.",
            "monitoring_cadence": "High-resolution chest CT with inspiratory and expiratory views (to demonstrate air trapping); PFTs with DLCO every 3-6 months; home environmental inspection.",
            "clinical_thresholds": "Three-density pattern (headcheese sign) on HRCT with BAL lymphocytosis >20% and known exposure to avian or fungal antigens."
        },
        "patient_plain_language": "An allergic inflammation deep inside your lungs triggered by repeatedly breathing in organic dusts—such as proteins from pet birds (parakeets, pigeons), down feather bedding, hot tub mist, or damp mold. Removing the bird or feather bedding from your home is the only way to stop your lungs from developing permanent stiff scars.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have we tested and identified the exact environmental trigger (pet birds, down feather pillows, home mold)?",
            "safety_question": "Did high-resolution chest CT show expiratory air trapping and the classic three-density pattern?",
            "action_threshold_question": "Will taking oral steroids help reverse the lung inflammation once the allergen is completely removed from my home?"
        },
        "red_flags": [
            "Resting oxygen saturation dropping <88% during walking (progressive irreversible pulmonary fibrosis)",
            "Severe persistent cough with weight loss and finger clubbing"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Hypersensitivity pneumonitis is allergic lung inflammation caused by breathing in bird proteins, mold, or down feathers.",
                "plain_analogy": "Fine sawdust repeatedly settling into a precision watch mechanism, causing the delicate gears to jam.",
                "lifestyle_action": "Permanently remove all birds, feather pillows, and mold sources from your home; use HEPA filters."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Complete Environmental Antigen Elimination (Foundational)",
                    "Prednisone oral (for acute/subacute HP)",
                    "Mycophenolate Mofetil / Azathioprine (Steroid-sparing)",
                    "Nintedanib (if progressive fibrosis)"
                ],
                "dosing_gdmt": "Prednisone 0.5 mg/kg/day x 4 weeks, tapered over 3 months; Mycophenolate 1,000-1,500 mg BID.",
                "black_box_warning": "Antigen avoidance is mandatory; pharmacotherapy fails if the patient remains exposed to the antigen.",
                "organ_clearance_cutoffs": "Mycophenolate requires monitoring of CBC and liver enzymes; teratogenic black box warning."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS-HP-GUIDELINE",
                "pmid_or_doi": "10.1164/rccm.202005-2032ST",
                "cebm_level": 1,
                "sample_size": 1600,
                "endpoints": "Complete antigen avoidance arrests lung decline and improves FVC in over 80% of non-fibrotic HP patients."
            }
        }
    },
    {
        "id": "DOC-CARD-426",
        "icd10": "J62.8",
        "condition": "Silicosis (Eggshell Calcification Pneumoconiosis)",
        "specialty": "Occupational Medicine & Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: OSHA Crystalline Silica Standard & WHO Guidelines",
        "source_body": "American Journal of Respiratory and Critical Care Medicine",
        "citation": "Barnes H et al. Occupational Lung Diseases: Crystalline Silica Exposure and Silicosis. Lancet Respir Med. 2021;9(8):897-909.",
        "doi_or_source": "10.1016/S2213-2600(20)30537-4",
        "clinical_evidence": "Inhalation of respirable crystalline silica (sandblasting, stone cutting, artificial stone countertops) causes irreversible macrophage lysis, fibrotic nodule formation, and progressive massive fibrosis (PMF). SILICOSIS CARRIES A 3-TO-30-FOLD INCREASED RISK OF ACTIVE TUBERCULOSIS (Silicotuberculosis). Routine annual screening with Tuberculin Skin Test (TST >=5 mm) or IGRA and prompt latent TB therapy (Rifampin or Isoniazid) is mandatory.",
        "solution_protocol": {
            "non_pharmacological_targets": "IMMEDIATE CESSATION OF SILICA EXPOSURE; use NIOSH-certified N95/P100 respirators; wet-cutting engineering controls; annual influenza and pneumococcal vaccination; smoking cessation.",
            "monitoring_cadence": "Annual screening for active and latent tuberculosis (TST/IGRA and chest X-ray); annual spirometry and DLCO; monitor for progressive massive fibrosis (PMF).",
            "clinical_thresholds": "Chest radiograph showing round opacities predominantly in upper lung zones with classic 'eggshell calcification' of hilar lymph nodes."
        },
        "patient_plain_language": "An occupational lung disease caused by inhaling fine silica dust from stone cutting, sandblasting, or manufacturing quartz countertops. The sharp mineral crystals cannot be cleared by your lungs, causing permanent nodules and hard scars. People with silicosis have a very high risk of contracting tuberculosis, so regular TB testing is essential.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did chest imaging show upper lung nodules and eggshell calcification of the lymph nodes?",
            "safety_question": "Have I been tested for latent tuberculosis (IGRA blood test or skin test) to start preventive TB medication?",
            "action_threshold_question": "What legal and occupational health protections do I have to avoid any further dust exposure at work?"
        },
        "red_flags": [
            "Coughing up blood (hemoptysis), night sweats, and unexplained fever (Silicotuberculosis until proven otherwise)",
            "Rapidly worsening breathlessness with giant coalescent upper lobe masses (Progressive Massive Fibrosis)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Silicosis is permanent scarring of the lungs caused by inhaling crystalline silica dust from stone or sand.",
                "plain_analogy": "Fine glass shards blown into an air mattress that permanently puncture and stiffen the fabric.",
                "lifestyle_action": "Never work with stone or sand without certified wet-cutting and N95/P100 respirators; get tested for TB."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Latent Tuberculosis Prophylaxis (Rifampin / Isoniazid)",
                    "Inhaled Bronchodilators (for airflow obstruction)",
                    "Whole Lung Lavage (for acute silicoproteinosis)",
                    "Lung Transplantation (End-stage)"
                ],
                "dosing_gdmt": "Rifampin 600 mg daily x 4 months (or Isoniazid + Rifapentine weekly x 12 weeks) for positive TB screen.",
                "black_box_warning": "No pharmacological agent can dissolve inhaled silica crystals; prevention is the only cure.",
                "organ_clearance_cutoffs": "Monitor liver function tests during anti-tuberculosis therapy."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "OSHA-SILICA",
                "pmid_or_doi": "10.1016/S2213-2600(20)30537-4",
                "cebm_level": 1,
                "sample_size": 3500,
                "endpoints": "Preventive therapy for latent TB reduces active tuberculosis incidence in silicosis by over 70%."
            }
        }
    },
    {
        "id": "DOC-CARD-427",
        "icd10": "J60",
        "condition": "Coal Workers' Pneumoconiosis (Black Lung & Caplan Syndrome)",
        "specialty": "Occupational Medicine & Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: NIOSH Coal Mine Dust Guidelines",
        "source_body": "Lancet",
        "citation": "Perret JL et al. Coal Workers' Pneumoconiosis and Progressive Massive Fibrosis. Lancet. 2017;389(10083):2059-2070.",
        "doi_or_source": "10.1016/S0140-6736(17)30587-7",
        "clinical_evidence": "Chronic inhalation of coal mine dust results in coal macules and nodules, progressing to debilitating Progressive Massive Fibrosis (PMF). Caplan syndrome represents coal workers' pneumoconiosis complicated by rheumatoid arthritis with large necrobiotic rheumatoid nodules in the lungs. No medical reversal exists; prevention, pulmonary rehabilitation, and bronchodilators form the therapeutic foundation.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate removal from coal mine dust exposure; participation in federal Black Lung Benefits programs; smoking cessation; aerobic pulmonary rehabilitation; vaccinations.",
            "monitoring_cadence": "Spirometry and DLCO every 1-2 years; chest radiograph utilizing ILO International Classification of Pneumoconioses; screening for rheumatoid factor and anti-CCP.",
            "clinical_thresholds": "Presence of coal macules (1-5 mm opacities) on chest X-ray in a patient with significant underground coal mining history."
        },
        "patient_plain_language": "A chronic occupational lung scarring disease caused by decades of inhaling coal dust underground ('Black Lung'). The coal dust accumulates in the upper lungs, forming black spots and large hard scar blocks. When combined with rheumatoid arthritis, it causes large lung nodules known as Caplan syndrome.",
        "doctor_consultation_checklist": {
            "parameter_question": "What stage of coal workers' pneumoconiosis (simple vs progressive massive fibrosis) do my chest X-rays show?",
            "safety_question": "Have I been screened for rheumatoid arthritis if large round lung nodules are present (Caplan syndrome)?",
            "action_threshold_question": "How do I enroll in pulmonary rehabilitation and file for occupational Black Lung health compensation?"
        },
        "red_flags": [
            "Sudden severe breathlessness with dark black sputum expectoration (Melanoptysis from cavitary PMF)",
            "Cor pulmonale with severe leg swelling and jugular venous distension"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Coal workers' pneumoconiosis is irreversible lung scarring caused by inhaling underground coal mine dust.",
                "plain_analogy": "Black soot caked permanently onto the exhaust pipes and filters of an engine.",
                "lifestyle_action": "Leave dusty mining environments, enroll in pulmonary rehab, avoid smoking, and get regular chest scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Inhaled LAMA/LABA (Tiotropium/Olodaterol)",
                    "Pulmonary Rehabilitation",
                    "Supplemental Oxygen Therapy",
                    "Lung Transplantation"
                ],
                "dosing_gdmt": "Tiotropium 2.5 mcg / Olodaterol 2.5 mcg inhaled daily for chronic airflow obstruction.",
                "black_box_warning": "Dust inhalation is irreversible; avoid exposure; supportive symptom management.",
                "organ_clearance_cutoffs": "Dose adjustments for comorbid cardiovascular disease."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "NIOSH-CWP",
                "pmid_or_doi": "10.1016/S0140-6736(17)30587-7",
                "cebm_level": 1,
                "sample_size": 4200,
                "endpoints": "Early removal from coal dust prevents progression from simple pneumoconiosis to disabling massive fibrosis."
            }
        }
    },
    {
        "id": "DOC-CARD-428",
        "icd10": "J61",
        "condition": "Asbestosis & Pleural Plaques (Amphibole / Chrysotile Fibrosis)",
        "specialty": "Occupational Medicine & Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATS Statement on Asbestos-Related Diseases",
        "source_body": "American Journal of Respiratory and Critical Care Medicine",
        "citation": "American Thoracic Society. Diagnosis and Initial Management of Nonmalignant Diseases Related to Asbestos. Am J Respir Crit Care Med. 2004;170(6):691-715.",
        "doi_or_source": "10.1164/rccm.200310-1436ST",
        "clinical_evidence": "Asbestos fiber inhalation causes bilateral lower lobe predominant interstitial pulmonary fibrosis (asbestosis) and calcified parietal pleural plaques along the diaphragm and chest wall (pathognomonic hallmark). Asbestos exposure multiplies the risk of bronchogenic lung carcinoma (synergistic 50-fold risk multiplier with tobacco smoking) and Malignant Mesothelioma (independent of smoking).",
        "solution_protocol": {
            "non_pharmacological_targets": "ABSOLUTE TOBACCO SMOKING CESSATION (critical synergistic multiplier for lung cancer); annual low-dose chest CT screening for lung cancer; removal from ongoing exposure; oxygen therapy for hypoxemia.",
            "monitoring_cadence": "High-resolution chest CT (HRCT showing subpleural dot-like opacities, intralobular thickening, and diaphragmatic calcified pleural plaques); annual spirometry and DLCO.",
            "clinical_thresholds": "History of asbestos latency (>20-30 years), bilateral lower-zone inspiratory crackles (Velcro rales), and bilateral calcified diaphragmatic pleural plaques on CT."
        },
        "patient_plain_language": "Breathing in microscopic mineral fibers (asbestos) from old shipyards, brake linings, pipes, or insulation decades ago. The sharp needle-like fibers remain trapped in the lower lungs and chest lining for life, causing calcified armor plates on your diaphragm (pleural plaques) and lung scarring. Smoking while exposed to asbestos multiplies your lung cancer risk by 50 times.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my chest CT show benign calcified pleural plaques on the diaphragm or interstitial lung fibrosis?",
            "safety_question": "Why is complete smoking cessation the most urgent life-saving step to avoid lung cancer?",
            "action_threshold_question": "Am I enrolled in annual low-dose chest CT cancer screening to detect any early lung nodules?"
        },
        "red_flags": [
            "New-onset unprovoked pleural effusion with unilateral chest pain (Malignant Pleural Mesothelioma until proven otherwise)",
            "Unexplained weight loss, coughing up blood, or solitary enlarging lung nodule"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Asbestosis is lung scarring and calcified chest wall plaques caused by inhaling needle-like asbestos fibers.",
                "plain_analogy": "Tiny mineral needles permanently embedded in the lining and filters of a furnace.",
                "lifestyle_action": "Never smoke, get screened with yearly low-dose CT scans, and report any blood in your cough."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Annual Low-Dose CT Lung Cancer Screening",
                    "Supplemental Oxygen Therapy",
                    "Inhaled Bronchodilators",
                    "Smoking Cessation Pharmacotherapy (Varenicline)"
                ],
                "dosing_gdmt": "Varenicline 0.5 mg daily titrated to 1 mg BID x 12 weeks for tobacco cessation; oxygen for resting PaO2 <=55 mmHg.",
                "black_box_warning": "Asbestos exposure combined with cigarette smoking creates a synergistic 50-to-60-fold increase in lung cancer.",
                "organ_clearance_cutoffs": "Renal dose adjustments for varenicline."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS-ASBESTOS",
                "pmid_or_doi": "10.1164/rccm.200310-1436ST",
                "cebm_level": 1,
                "sample_size": 5100,
                "endpoints": "Smoking cessation reduces the synergistic 50-fold lung cancer risk in asbestos-exposed individuals by >50%."
            }
        }
    },
    {
        "id": "DOC-CARD-429",
        "icd10": "J86.9",
        "condition": "Pleural Empyema (Complicated Parapneumonic Infection)",
        "specialty": "Thoracic Surgery & Pulmonology",
        "organ_system": "Respiratory & Infectious",
        "cebm_level": 1,
        "evidence_tier": "Level 1: MIST-2 Landmark Trial & BTS Pleural Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Rahman NM et al. Intrapleural Use of Tissue Plasminogen Activator and DNase in Pleural Infection (MIST-2). N Engl J Med. 2011;365(6):518-526.",
        "doi_or_source": "10.1056/NEJMoa1012740",
        "clinical_evidence": "The landmark MIST-2 randomized trial (n=210) proved that combined intrapleural Tissue Plasminogen Activator (tPA 10 mg) and Recombinant Human DNase (5 mg) given twice daily for 3 days improved fluid drainage, reduced surgical referral by 77% (hazard ratio 0.23; p=0.003), and shortened hospital stay by 6.7 days versus placebo. Large-bore or small-bore chest tube drainage is mandatory.",
        "solution_protocol": {
            "non_pharmacological_targets": "Immediate diagnostic pleural fluid thoracentesis; tube thoracostomy (chest drain) for macroscopic pus or loculations; early thoracic surgery consultation for VATS decortication if medical therapy fails; high-protein nutrition.",
            "monitoring_cadence": "Pleural fluid analysis (pH, glucose, LDH, Gram stain, culture); repeat chest ultrasound or CT at 48-72 hours to assess residual loculations and fluid clearance.",
            "clinical_thresholds": "Macroscopic frank pus in pleural space, positive pleural Gram stain/culture, or pleural fluid pH <7.20 (or glucose <40 mg/dL, LDH >1,000 U/L) mandates complete tube drainage."
        },
        "patient_plain_language": "A severe complication of pneumonia where the infection spills into the water space surrounding your lung (pleural cavity), creating a walled-off pocket of thick pus (empyema). Antibiotics alone cannot penetrate thick pus; a tube must be inserted into your chest wall to drain the infected fluid, often using clot-dissolving medicines (tPA and DNase) to liquefy the sludge.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the pleural tap show pus or an acidic pH below 7.20 proving that a chest drain is required?",
            "safety_question": "Are we using the MIST-2 regimen (clot-dissolving tPA and DNase enzymes) flushed into the tube to dissolve the pockets?",
            "action_threshold_question": "Will I need keyhole chest surgery (VATS) to scrape away the peel if the fluid does not drain?"
        },
        "red_flags": [
            "Persisting high fever and septic shock despite chest tube drainage (indicates undrained loculated collection)",
            "Large air leak through chest tube with subcutaneous emphysema (bronchopleural fistula)"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Pleural empyema is an infection causing pockets of pus to collect in the chest space around the lung.",
                "plain_analogy": "An abscess forming inside the double-walled insulation of a house, requiring a drainage pipe to clear it.",
                "lifestyle_action": "Seek immediate emergency hospital care for high fever and sharp side pain; chest drainage is mandatory."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Intrapleural tPA (10 mg) + DNase (5 mg) BID x 3 days",
                    "Ampicillin/Sulbactam IV (Unasyn) or Ceftriaxone + Metronidazole",
                    "VATS Decortication (Surgical)"
                ],
                "dosing_gdmt": "tPA 10 mg + DNase 5 mg instilled into chest tube, clamped for 1-2 hours, then opened to suction BID x 6 doses.",
                "black_box_warning": "tPA alone or DNase alone is INEFFECTIVE; the combination is required to dissolve fibrin and bacterial DNA.",
                "organ_clearance_cutoffs": "Dose adjustments for renal impairment with IV antibiotics; monitor for intrapleural bleeding."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MIST-2-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1012740",
                "cebm_level": 2,
                "sample_size": 210,
                "endpoints": "Combined intrapleural tPA-DNase reduces surgical intervention by 77% and hospital stay by 6.7 days (p=0.003)."
            }
        }
    },
    {
        "id": "DOC-CARD-430",
        "icd10": "C78.2",
        "condition": "Malignant Pleural Effusion (Metastatic Pleural Carcinomatosis)",
        "specialty": "Interventional Pulmonology & Oncology",
        "organ_system": "Respiratory & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: TIME2 & AMPLE Landmark Trials",
        "source_body": "JAMA & Lancet Oncology",
        "citation": "Thomas R et al. Indwelling Pleural Catheter vs Talc Pleurodesis in Malignant Pleural Effusion (AMPLE). Lancet Oncol. 2017;18(7):921-932.",
        "doi_or_source": "10.1016/S1470-2045(17)30360-1",
        "clinical_evidence": "Malignant pleural effusion (MPE) causes recurrent dyspnea in advanced cancer. The AMPLE (n=146) and TIME2 (n=144) trials established that outpatient Indwelling Pleural Catheters (IPC / PleurX) achieve equivalent dyspnea relief while significantly reducing hospital days (10 days IPC vs 12 days talc pleurodesis; p<0.001) and re-intervention rates compared to chemical talc pleurodesis.",
        "solution_protocol": {
            "non_pharmacological_targets": "Choose between outpatient indwelling pleural catheter (allows home drainage) vs inpatient talc slurry pleurodesis; palliative symptom control; systemic antineoplastic therapy targeting primary malignancy; avoid dehydration.",
            "monitoring_cadence": "Daily to every-other-day drainage volume tracking at home via vacuum bottles; monitoring catheter exit site for infection; follow-up chest radiographs.",
            "clinical_thresholds": "Pleural fluid cytology confirming malignant adenocarcinoma, squamous, or small cell carcinoma cells."
        },
        "patient_plain_language": "Cancer cells from the lung, breast, or other organs spread to the lining of your chest, causing fluid to continuously leak and crush the lung. Instead of staying in the hospital for days, doctors can place a tiny permanent soft catheter (IPC) under your skin so you or a nurse can drain the fluid at home with small vacuum bottles whenever breathlessness occurs.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did the fluid cytology test identify the specific cancer cells causing the fluid buildup?",
            "safety_question": "Is a permanent home catheter (IPC) better for me than hospital talc powder glue (pleurodesis)?",
            "action_threshold_question": "How often should I drain fluid at home, and what signs of catheter infection should I watch for?"
        },
        "red_flags": [
            "Drainage fluid suddenly turns cloudy, milky, or foul-smelling with fever (Catheter-related empyema)",
            "Inability to breathe with severe chest pain during fluid drainage (indicates unexpandable 'trapped lung')"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Malignant pleural effusion is recurrent fluid buildup around the lung caused by cancer cells on the chest lining.",
                "plain_analogy": "A leaky radiator in a car engine compartment continuously filling the space and squeezing the air intake.",
                "lifestyle_action": "Drain the fluid at home using your catheter as instructed, keep the dressing clean, and report fever immediately."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Indwelling Pleural Catheter (IPC / PleurX)",
                    "Talc Slurry Pleurodesis (5 g sterile talc)",
                    "Systemic Targeted / Immunotherapy"
                ],
                "dosing_gdmt": "IPC drained 2-3 times weekly with 1,000 mL vacuum bottles; Talc 5 g slurry via chest tube.",
                "black_box_warning": "Never drain more than 1,000-1,500 mL at a single session (prevents re-expansion pulmonary edema).",
                "organ_clearance_cutoffs": "No systemic toxicity from IPC; monitor catheter exit site."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AMPLE-TRIAL",
                "pmid_or_doi": "10.1016/S1470-2045(17)30360-1",
                "cebm_level": 2,
                "sample_size": 146,
                "endpoints": "Indwelling pleural catheters significantly reduce hospital days without sacrificing dyspnea relief."
            }
        }
    },
    {
        "id": "DOC-CARD-431",
        "icd10": "I27.24",
        "condition": "Chronic Thromboembolic Pulmonary Hypertension (CTEPH)",
        "specialty": "Cardiology & Thoracic Surgery",
        "organ_system": "Circulatory & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: CHEST-1 Landmark Trial & ESC/ERS PH Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Ghofrani HA et al. Riociguat for the Treatment of Chronic Thromboembolic Pulmonary Hypertension (CHEST-1). N Engl J Med. 2013;369(4):319-329.",
        "doi_or_source": "10.1056/NEJMoa1209657",
        "clinical_evidence": "CTEPH is the ONLY potentially curable form of pulmonary hypertension. PULMONARY ENDARTERECTOMY (PEA / open surgical removal of fibrotic clots) performed at an expert center cures hypertension and restores near-normal hemodynamics in >75% of patients. In inoperable CTEPH or residual post-PEA hypertension, soluble guanylate cyclase stimulator Riociguat (CHEST-1 trial, n=261) improves 6-minute walk distance (+46 meters; p<0.001) and pulmonary vascular resistance.",
        "solution_protocol": {
            "non_pharmacological_targets": "Lifelong therapeutic anticoagulation (unfractionated heparin, LMWH, or warfarin; target INR 2.5-3.5); multidisciplinary evaluation at an expert CTEPH surgical center; balloon pulmonary angioplasty (BPA) for distal disease.",
            "monitoring_cadence": "Ventilation-Perfusion (V/Q) lung scan (screening test of choice; normal V/Q scan rules out CTEPH); invasive right heart catheterization and pulmonary angiography.",
            "clinical_thresholds": "Mean pulmonary arterial pressure (mPAP) >20 mmHg with PAWP <=15 mmHg and PVR >2 Wood units, in the presence of mismatched perfusion defects on V/Q scan after >=3 months anticoagulation."
        },
        "patient_plain_language": "After a pulmonary embolism, old blood clots do not dissolve normally. Instead, they transform into tough, fibrotic yellow scars that permanently block your lung arteries, forcing your right heart to pump against crushing pressure. Unlike other forms of high lung pressure, this condition can be completely cured by expert surgeons who carefully peel the old scars out of the lung arteries.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did my V/Q lung scan show mismatched perfusion blockages confirming CTEPH?",
            "safety_question": "Has my case been reviewed by an experienced pulmonary endarterectomy (PEA) surgical center for cure?",
            "action_threshold_question": "If surgery is not possible, am I taking Riociguat (Adempas) to open the pulmonary blood vessels?"
        },
        "red_flags": [
            "Right heart failure with severe abdominal ascites, jaundice, and fainting spells",
            "Acute worsening of shortness of breath indicating new recurrent pulmonary thromboembolism"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "CTEPH is chronic high blood pressure in lung arteries caused by old, scarred blood clots.",
                "plain_analogy": "Hardened sediment and lime scale clogging the main water pipes leaving a central pump.",
                "lifestyle_action": "Stay on lifelong blood thinners, get evaluated at an expert surgical center, and attend regular walking tests."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Riociguat oral (Adempas - Approved for CTEPH)",
                    "Pulmonary Endarterectomy (PEA - Curative Surgery)",
                    "Warfarin / DOAC Anticoagulation (Lifelong)",
                    "Balloon Pulmonary Angioplasty (BPA)"
                ],
                "dosing_gdmt": "Riociguat 1.0 mg TID, titrated by 0.5 mg every 2 weeks to max 2.5 mg TID; Warfarin target INR 2.5-3.5.",
                "black_box_warning": "Riociguat carries black box warning for embryo-fetal toxicity; DO NOT COMBINE WITH PDE5 INHIBITORS (causes fatal hypotension).",
                "organ_clearance_cutoffs": "Dose titration requires close blood pressure monitoring; adjust for smoking status."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "CHEST-1",
                "pmid_or_doi": "10.1056/NEJMoa1209657",
                "cebm_level": 2,
                "sample_size": 261,
                "endpoints": "Riociguat increases 6-minute walk distance by 46 meters and drops pulmonary vascular resistance by 226 dynes (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-432",
        "icd10": "I27.0",
        "condition": "Pulmonary Arterial Hypertension (Group 1 WHO PAH)",
        "specialty": "Cardiology & Pulmonology",
        "organ_system": "Circulatory & Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AMBITION Landmark Trial & ESC/ERS PH Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Galiè N et al. Initial Use of Ambrisentan plus Tadalafil in Pulmonary Arterial Hypertension (AMBITION). N Engl J Med. 2015;373(9):834-844.",
        "doi_or_source": "10.1056/NEJMoa1413687",
        "clinical_evidence": "The landmark AMBITION trial (n=500) established that upfront combination therapy targeting two distinct biological pathways (Endothelin Receptor Antagonist Ambrisentan + PDE5 Inhibitor Tadalafil) reduced the risk of clinical failure by 50% (hazard ratio 0.50; p<0.001) compared to monotherapy. High-risk patients require triple therapy including continuous IV/SubQ Prostacyclin (Epoprostenol / Treprostinil).",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict sodium (<2 g/day) and fluid restriction; supervised pulmonary rehabilitation; avoid pregnancy (carries 30-50% maternal mortality in PAH); prompt treatment of respiratory infections.",
            "monitoring_cadence": "Right heart catheterization at baseline and after therapeutic changes; 6-minute walk test and NT-proBNP every 3-6 months; COMPERA or REVEAL 2.0 risk score calculation.",
            "clinical_thresholds": "Resting mPAP >20 mmHg, pulmonary capillary wedge pressure (PAWP) <=15 mmHg, and pulmonary vascular resistance (PVR) >2 Wood Units."
        },
        "patient_plain_language": "The microscopic blood vessels inside your lungs become pathologically thick, narrow, and stiff. Your heart's right pumping chamber has to strain with extreme force to push blood through the tight vessels, leading to exhaustion, breathlessness, and right heart strain. Starting two medications at the exact same time works twice as well as taking one alone.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my pulmonary vascular resistance (PVR) and right heart pressure on heart catheterization?",
            "safety_question": "Am I on upfront combination therapy (such as an endothelin blocker plus a PDE5 inhibitor) as recommended?",
            "action_threshold_question": "What is my current 6-minute walk distance and REVEAL risk score?"
        },
        "red_flags": [
            "Fainting (syncope) during simple walking or stair climbing (Indicates acute right ventricular failure)",
            "Rapidly progressive swelling in legs and abdomen with blue lips and cold fingers"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "PAH is severe narrowing and stiffening of small lung arteries causing right-sided heart strain.",
                "plain_analogy": "A sprinkler system with severely clogged nozzles, forcing the pump behind it to burn out under extreme strain.",
                "lifestyle_action": "Take your pulmonary vasodilators every single day, avoid pregnancy and saunas, and track your walking stamina."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Ambrisentan (Letairis - Endothelin Antagonist)",
                    "Tadalafil (Adcirca - PDE5 Inhibitor)",
                    "Epoprostenol IV (Veletri - Prostacyclin)",
                    "Selexipag oral"
                ],
                "dosing_gdmt": "Ambrisentan 5-10 mg daily + Tadalafil 40 mg daily; Epoprostenol titrated continuously via ambulatory pump.",
                "black_box_warning": "Endothelin antagonists carry black box warning for embryo-fetal toxicity (REMS program); PDE5i contraindicated with nitrates.",
                "organ_clearance_cutoffs": "Dose adjustments and monitoring of liver enzymes and hemoglobin."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AMBITION-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1413687",
                "cebm_level": 2,
                "sample_size": 500,
                "endpoints": "Upfront combination Ambrisentan + Tadalafil reduces clinical failure events by 50% compared to monotherapy (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-433",
        "icd10": "E34.0",
        "condition": "Bronchial Carcinoid Tumor (Neuroendocrine Bronchospasm)",
        "specialty": "Thoracic Oncology & Pulmonology",
        "organ_system": "Respiratory & Neoplastic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ENETS Consensus Guidelines & NCCN Guidelines",
        "source_body": "Neuroendocrinology",
        "citation": "Caplin ME et al. ENETS Consensus Guidelines for the Management of Patients with Digestive Neuroendocrine Neoplasms: Colorectal and Lung. Neuroendocrinology. 2015;101(2):165-177.",
        "doi_or_source": "10.1159/000371852",
        "clinical_evidence": "Typical and atypical bronchial neuroendocrine carcinoids arise from pulmonary Kulchitsky cells, presenting with recurrent pneumonia, hemoptysis, and pseudo-asthma wheezing. SURGICAL PARENCHYMAL-SPARING RESECTION (sleeve resection or lobectomy with mediastinal lymph node dissection) is the curative gold standard (yielding >90% 10-year survival in typical carcinoids). Somatostatin analogues (Octreotide/Lanreotide) control carcinoid syndrome.",
        "solution_protocol": {
            "non_pharmacological_targets": "Complete surgical resection whenever feasible; avoid foods containing high tyramine or histamine during carcinoid flush; bronchoscopic airway debulking for non-operable central obstruction.",
            "monitoring_cadence": "68Ga-DOTATATE PET/CT (superior sensitivity for somatostatin receptor-expressing neuroendocrine tumors); 24-hour urine 5-HIAA; serum Chromogranin A.",
            "clinical_thresholds": "Histopathology: Typical carcinoid (<2 mitoses/2 mm2, no necrosis); Atypical carcinoid (2-10 mitoses/2 mm2 or punctate necrosis)."
        },
        "patient_plain_language": "A slow-growing neuroendocrine tumor growing inside a lung breathing tube. Because it partly blocks airflow and secretes hormone chemicals, it often gets misdiagnosed for years as adult-onset 'asthma' with wheezing and coughing up spots of blood. Removing the small plug of tumor with keyhole surgery cures the disease in the vast majority of patients.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did 68Ga-DOTATATE PET scan show somatostatin receptor uptake and confirm no spread beyond the lung?",
            "safety_question": "Is my tumor a typical carcinoid (<2 mitoses) or atypical carcinoid on biopsy?",
            "action_threshold_question": "Can a lung-saving sleeve resection be performed instead of removing my entire lung?"
        },
        "red_flags": [
            "Sudden flushing of the face and neck with diarrhea and wheezing (Carcinoid Syndrome)",
            "Coughing up frank blood with sudden airway obstruction"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Bronchial carcinoid is a slow-growing tumor in the lung airways that can mimic asthma with wheezing.",
                "plain_analogy": "A smooth round cork lodged in the intake pipe of a vacuum cleaner, restricting airflow and whistling.",
                "lifestyle_action": "Consult thoracic surgery for tumor resection, and undergo specialized DOTATATE PET scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Parenchymal-Sparing Surgical Resection (Curative)",
                    "Octreotide LAR (Sandostatin - Somatostatin Analogue)",
                    "Lanreotide SubQ",
                    "Everolimus (for advanced atypical)"
                ],
                "dosing_gdmt": "Octreotide LAR 20-30 mg IM every 4 weeks; or Lanreotide 120 mg deep SC every 4 weeks.",
                "black_box_warning": "Octreotide can cause biliary sludge and cholelithiasis; monitor with periodic gallbladder ultrasound.",
                "organ_clearance_cutoffs": "Dose reduction in renal or hepatic impairment."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ENETS-LUNG",
                "pmid_or_doi": "10.1159/000371852",
                "cebm_level": 1,
                "sample_size": 1450,
                "endpoints": "Complete surgical resection yields >90% 10-year survival in typical bronchial carcinoids."
            }
        }
    },
    {
        "id": "DOC-CARD-434",
        "icd10": "J84.112",
        "condition": "Idiopathic Pulmonary Fibrosis (UIP Pattern - Antifibrotic GDMT)",
        "specialty": "Pulmonology & Interstitial Lung Disease",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: INPULSIS & ASCEND Landmark Trials",
        "source_body": "New England Journal of Medicine",
        "citation": "King TE Jr et al. A Phase 3 Trial of Pirfenidone in Patients with Idiopathic Pulmonary Fibrosis (ASCEND). N Engl J Med. 2014;370(22):2083-2092.",
        "doi_or_source": "10.1056/NEJMoa1402582",
        "clinical_evidence": "The landmark ASCEND (Pirfenidone, n=555) and INPULSIS-1/2 (Nintedanib, n=1,066) multicenter randomized trials proved that antifibrotic therapy significantly slows disease progression, cutting the annual rate of FVC decline by ~50% (approx 110-125 mL/year saved; p<0.001) and reducing acute exacerbation risk. Early initiation halts irreversible honeycombing.",
        "solution_protocol": {
            "non_pharmacological_targets": "Early initiation of antifibrotic therapy; early referral for lung transplantation evaluation; supplemental ambulatory oxygen for exertional desaturation (SpO2 <88%); supervised pulmonary rehabilitation.",
            "monitoring_cadence": "High-resolution chest CT (HRCT demonstrating Usual Interstitial Pneumonia / UIP pattern: subpleural, basal predominance with reticular opacities and honeycombing without inconsistent features); PFTs (FVC, DLCO) every 3-6 months.",
            "clinical_thresholds": "HRCT definite UIP pattern or surgical lung biopsy showing spatial and temporal heterogeneity of fibrosis."
        },
        "patient_plain_language": "A progressive scarring disease where the elastic, sponge-like walls of your lungs slowly turn into thick, stiff, fibrous scar tissue. It causes a dry nagging cough and shortness of breath when walking. While existing scars cannot be erased, modern antifibrotic pills (Pirfenidone or Nintedanib) cut the speed of future scarring in half.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did high-resolution chest CT confirm the definitive UIP honeycombing pattern of IPF?",
            "safety_question": "Am I taking one of the two proven antifibrotic medicines (Pirfenidone or Nintedanib) to protect my lung volume?",
            "action_threshold_question": "Have I been referred early to a lung transplant center while my breathing function is still preserved?"
        },
        "red_flags": [
            "Rapid drop in walking oxygen saturation requiring higher oxygen liter flows (Acute IPF Exacerbation)",
            "Severe resting breathlessness with cyanosis and dry Velcro crackles on lung exam"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "IPF is progressive, irreversible scarring of the lung air sacs that stiffens the lungs over time.",
                "plain_analogy": "A flexible bath sponge that slowly dries out and hardens into rigid, unbendable cardboard.",
                "lifestyle_action": "Take your antifibrotic pill daily with meals, use walking oxygen as prescribed, and do pulmonary rehab."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Pirfenidone oral (Esbriet - Antifibrotic)",
                    "Nintedanib oral (OFEV - Tyrosine Kinase Inhibitor)",
                    "Ambulatory Supplemental Oxygen",
                    "Lung Transplantation"
                ],
                "dosing_gdmt": "Pirfenidone 267 mg TID titrated to 801 mg TID with meals; or Nintedanib 150 mg BID with food.",
                "black_box_warning": "Pirfenidone causes severe photosensitivity rash (sunscreen required); Nintedanib causes diarrhea in >60% of patients.",
                "organ_clearance_cutoffs": "Both antifibrotics require baseline and monthly liver function tests (ALT/AST/bilirubin)."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ASCEND-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1402582",
                "cebm_level": 2,
                "sample_size": 555,
                "endpoints": "Pirfenidone cuts the rate of FVC decline in half and reduces death or disease progression by 43% (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-435",
        "icd10": "J84.89",
        "condition": "Cryptogenic Organizing Pneumonia (COP - Steroid-Responsive)",
        "specialty": "Pulmonology & Critical Care",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ERS/ATS Task Force on Organizing Pneumonia",
        "source_body": "European Respiratory Journal",
        "citation": "Cordier JF. Cryptogenic Organizing Pneumonia. Eur Respir J. 2006;28(2):422-446.",
        "doi_or_source": "10.1183/09031936.06.00013505",
        "clinical_evidence": "COP (formerly BOOP) is characterized by intra-alveolar fibromyxoid plugs (Masson bodies) and classic HRCT peripheral consolidations with the 'reverse halo' (atoll) sign. SYSTEMIC CORTICOSTEROIDS (Prednisone 0.75-1.0 mg/kg/day) achieve dramatic clinical and radiological resolution within 48-72 hours in >80% of patients. Relapses occur in 13-50% during steroid tapering, requiring slow withdrawal over 6-12 months.",
        "solution_protocol": {
            "non_pharmacological_targets": "Prolonged oral corticosteroid taper (minimum 6-12 months) to prevent relapse; avoid rapid weaning; calcium and vitamin D supplementation during steroid therapy; annual influenza and pneumococcal vaccination.",
            "monitoring_cadence": "Chest CT at 1, 3, and 6 months documenting clearing of consolidations; serial spirometry and DLCO; monitoring for steroid adverse effects (blood glucose, bone density).",
            "clinical_thresholds": "Reverse halo (atoll) sign on HRCT (central ground-glass surrounded by dense crescentic consolidation) with transbronchial biopsy demonstrating Masson bodies."
        },
        "patient_plain_language": "Inflammatory plugs of connective tissue fill your microscopic air sacs, often appearing on X-rays like patches of stubborn bacterial pneumonia that never clear with antibiotics. Unlike permanent lung fibrosis, COP is remarkably steroid-responsive: taking Prednisone pills melts the inflammatory patches away within days, though the medicine must be tapered slowly to prevent relapse.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did lung biopsy or CT show the classic 'reverse halo' sign of Cryptogenic Organizing Pneumonia?",
            "safety_question": "Why did repeated courses of standard antibiotics fail to clear my lung patches?",
            "action_threshold_question": "Why must my steroid medicine (Prednisone) be tapered very slowly over 6 to 12 months to prevent a rebound flare?"
        },
        "red_flags": [
            "Sudden recurrence of high fever, cough, and breathlessness during steroid reduction (Disease Relapse)",
            "Steroid-induced hyperglycemia with blood sugar >300 mg/dL or severe mood changes"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "COP is a non-infectious inflammatory lung condition where air sacs fill with healing tissue plugs.",
                "plain_analogy": "Clogged storm drains filled with fallen leaves and mulch that rapidly clear once swept by steroid medicine.",
                "lifestyle_action": "Take your steroid medicine exactly as prescribed, never stop abruptly, and attend follow-up CT scans."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Prednisone oral (First Line - Highly Responsive)",
                    "Macrolide (Clarithromycin - for mild cases)",
                    "Azathioprine / Mycophenolate (for frequent relapses)"
                ],
                "dosing_gdmt": "Prednisone 0.75-1 mg/kg/day x 4-8 weeks, then 0.5 mg/kg/day x 4-8 weeks, then tapered over 6-12 months.",
                "black_box_warning": "Rapid tapering (<6 months) triggers disease relapse in up to 50% of patients.",
                "organ_clearance_cutoffs": "Bone protection with bisphosphonates; monitor for opportunistic infections."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ERS-COP-TASKFORCE",
                "pmid_or_doi": "10.1183/09031936.06.00013505",
                "cebm_level": 1,
                "sample_size": 1120,
                "endpoints": "Oral corticosteroids achieve complete clinical and radiographic resolution in over 80% of COP patients."
            }
        }
    },
    {
        "id": "DOC-CARD-436",
        "icd10": "M30.1",
        "condition": "Eosinophilic Granulomatosis with Polyangiitis (EGPA / Churg-Strauss)",
        "specialty": "Rheumatology & Pulmonology",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: MIRRA Landmark Trial & ACR/EULAR Guidelines",
        "source_body": "New England Journal of Medicine",
        "citation": "Wechsler ME et al. Mepolizumab or Placebo for Eosinophilic Granulomatosis with Polyangiitis (MIRRA). N Engl J Med. 2017;376(20):1921-1932.",
        "doi_or_source": "10.1056/NEJMoa1702079",
        "clinical_evidence": "EGPA presents with severe adult-onset asthma, chronic rhinosinusitis, peripheral eosinophilia (>1,000/mcL or >10%), and necrotizing vasculitis (mononeuritis multiplex, cardiac involvement). The landmark MIRRA trial (n=136) proved that anti-IL-5 monoclonal antibody Mepolizumab (300 mg SC monthly) achieved significantly more weeks of remission (28% vs 3%; p<0.001) and allowed 44% of patients to reduce daily prednisolone to <=4 mg.",
        "solution_protocol": {
            "non_pharmacological_targets": "Targeted biologic therapy to eliminate chronic steroid dependence; sinus rinses; cardiac screening (cardiac involvement causes 50% of EGPA deaths); early physical therapy for foot/wrist drop.",
            "monitoring_cadence": "Serial Absolute Eosinophil Count (AEC; target <300/mcL); ANCA serology (MPO-ANCA positive in ~40-50%); 12-lead ECG, troponin, and cardiac MRI.",
            "clinical_thresholds": "Five-Factor Score (FFS) assessing high-risk organ involvement (renal insufficiency, proteinuria >1g, cardiomyopathy, GI involvement, CNS involvement)."
        },
        "patient_plain_language": "A rare autoimmune condition combining severe asthma, nasal polyps, and very high levels of allergy cells (eosinophils) that attack and inflame your blood vessels. It can cause numbness or weakness in your hands or feet (wrist or foot drop) and can affect the heart. Modern biologic injections like Mepolizumab block the allergy cells and allow patients to stop dangerous steroids.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my absolute eosinophil count and was my MPO-ANCA antibody test positive or negative?",
            "safety_question": "Have I had an echocardiogram or cardiac MRI to make sure the blood vessel inflammation has spared my heart?",
            "action_threshold_question": "Am I a candidate for monthly Mepolizumab injections (anti-IL-5) to taper down my steroid pills?"
        },
        "red_flags": [
            "Sudden numbness, tingling, or weakness in a single hand or foot (Mononeuritis Multiplex foot drop)",
            "Chest pain, breathlessness, or elevated troponin indicating eosinophilic myocarditis"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "EGPA is an autoimmune disease causing severe asthma, high eosinophil allergy cells, and inflamed blood vessels.",
                "plain_analogy": "An overzealous security team that starts damaging the walls and electrical wires inside its own building.",
                "lifestyle_action": "Take your asthma and biologic treatments faithfully, report hand/foot numbness immediately, and check heart labs."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Mepolizumab SubQ (Nucala 300 mg - First Line Biologic)",
                    "Prednisone oral",
                    "Cyclophosphamide IV (for life-threatening organ involvement)",
                    "Rituximab IV"
                ],
                "dosing_gdmt": "Mepolizumab 300 mg (three 100 mg SC injections) every 4 weeks; Prednisone 1 mg/kg/day initially.",
                "black_box_warning": "Mepolizumab dose for EGPA (300 mg) is THREE TIMES higher than the severe asthma dose (100 mg).",
                "organ_clearance_cutoffs": "Monitor for herpes zoster reactivation; pre-treatment varicella vaccination recommended."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "MIRRA-TRIAL",
                "pmid_or_doi": "10.1056/NEJMoa1702079",
                "cebm_level": 2,
                "sample_size": 136,
                "endpoints": "Mepolizumab 300 mg monthly achieves sustained remission and halves oral steroid requirements in EGPA (p<0.001)."
            }
        }
    },
    {
        "id": "DOC-CARD-437",
        "icd10": "B44.81",
        "condition": "Allergic Bronchopulmonary Aspergillosis (ABPA)",
        "specialty": "Pulmonology & Allergy",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ISHAM ABPA Working Group Consensus",
        "source_body": "Journal of Allergy and Clinical Immunology",
        "citation": "Agarwal R et al. Allergic Bronchopulmonary Aspergillosis: Review of Literature and ISHAM Working Group Consensus. J Allergy Clin Immunol. 2013;132(4):804-812.",
        "doi_or_source": "10.1016/j.jaci.2013.07.007",
        "clinical_evidence": "ABPA is an intense hypersensitivity reaction to Aspergillus fumigatus colonizing the bronchial tree in asthma or cystic fibrosis patients. Oral Itraconazole (200 mg BID x 16 weeks) combined with Oral Corticosteroids suppresses fungal burden, reduces exacerbation rate by >50%, and clears central bronchiectasis with high-attenuation mucus (HAM) plugging. Biologic anti-IgE (Omalizumab) or anti-IL-5 is effective for steroid-dependent disease.",
        "solution_protocol": {
            "non_pharmacological_targets": "Oral antifungal azole therapy plus systemic corticosteroids; environmental avoidance of compost, decaying leaves, mulch, and damp basements; pulmonary hygiene.",
            "monitoring_cadence": "Total serum IgE level (classic biomarker: baseline >1,000 IU/mL; 25-50% drop signifies clinical remission); Aspergillus-specific IgE and IgG; high-resolution chest CT.",
            "clinical_thresholds": "Pre-existing asthma or CF, total IgE >1,000 IU/mL, positive Aspergillus skin test or specific IgE, and central (internal) bronchiectasis."
        },
        "patient_plain_language": "An intense allergic overreaction in your lungs caused by mold spores (Aspergillus) that live in soil and mulch. If you have asthma or cystic fibrosis, the mold sets up home in your airways. Your body releases massive amounts of allergy antibodies (IgE), causing thick brown mucus plugs and airway damage. Antifungal pills plus steroids clear the mold and calm the allergy.",
        "doctor_consultation_checklist": {
            "parameter_question": "What was my total serum IgE level (is it over 1,000 IU/mL) and is it dropping with treatment?",
            "safety_question": "Did my chest CT scan show central bronchiectasis or thick mucus plugs ('finger-in-glove' sign)?",
            "action_threshold_question": "Am I taking oral Itraconazole antifungal capsules with an acidic drink (like orange juice) to ensure full absorption?"
        },
        "red_flags": [
            "Coughing up firm, rubbery, brownish-black plugs of thick mucus with severe wheezing",
            "Massive rise in total IgE (>100% increase) indicating an acute ABPA flare"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "ABPA is an allergic reaction to common mold spores in the lungs that causes thick mucus plugs and asthma flares.",
                "plain_analogy": "Mold growing inside the exhaust vents of an air purifier, causing the machine's filter to swell shut.",
                "lifestyle_action": "Avoid handling compost and leaf mulch, take your antifungal and steroid pills, and monitor blood IgE levels."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Itraconazole oral (Sporanox)",
                    "Prednisone oral",
                    "Voriconazole (if Itraconazole intolerant)",
                    "Omalizumab (Xolair - Anti-IgE)"
                ],
                "dosing_gdmt": "Itraconazole 200 mg BID with food/acidic beverage x 16 weeks; Prednisone 0.5 mg/kg/day tapered over 3-4 months.",
                "black_box_warning": "Itraconazole requires therapeutic drug monitoring (target trough >1.0 mcg/mL); strong CYP3A4 inhibitor.",
                "organ_clearance_cutoffs": "Monitor liver enzymes monthly; black box warning for congestive heart failure with itraconazole."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ISHAM-ABPA",
                "pmid_or_doi": "10.1016/j.jaci.2013.07.007",
                "cebm_level": 1,
                "sample_size": 1300,
                "endpoints": "Oral Itraconazole combined with steroids halves exacerbation frequency and clears high-attenuation mucus plugs."
            }
        }
    },
    {
        "id": "DOC-CARD-438",
        "icd10": "E66.2",
        "condition": "Obesity Hypoventilation Syndrome (Pickwickian Sleep Hypoventilation)",
        "specialty": "Sleep Medicine & Pulmonology",
        "organ_system": "Respiratory & Metabolic",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ATS Clinical Practice Guideline on OHS",
        "source_body": "American Journal of Respiratory and Critical Care Medicine",
        "citation": "Mokhlesi B et al. Evaluation and Management of Obesity Hypoventilation Syndrome: An Official American Thoracic Society Clinical Practice Guideline. Am J Respir Crit Care Med. 2019;200(3):e6-e24.",
        "doi_or_source": "10.1164/rccm.201905-1071ST",
        "clinical_evidence": "OHS triad consists of Obesity (BMI >=30 kg/m2), daytime hypercapnia (arterial PaCO2 >=45 mmHg), and sleep-disordered breathing in the absence of alternative causes. Positive Airway Pressure (PAP: CPAP for comorbid severe OSA, or Non-Invasive Bi-level PAP for persistent hypoventilation) corrects hypercapnia, eliminates nocturnal hypoxia, and cuts 5-year mortality from 23% to <4% (p<0.001). Bariatric metabolic surgery provides definitive reversal.",
        "solution_protocol": {
            "non_pharmacological_targets": "Nocturnal positive airway pressure (CPAP or Bi-level PAP) used >=4-6 hours every night; medically supervised weight loss or bariatric metabolic surgery (achieves resolution of OHS in >70%); complete avoidance of sedatives, opioids, and alcohol.",
            "monitoring_cadence": "Arterial blood gas measuring daytime PaCO2 and PaO2; serum venous bicarbonate (bicarbonate >=27 mEq/L is highly sensitive screening threshold for daytime hypercapnia); diagnostic sleep study (polysomnography).",
            "clinical_thresholds": "Awake daytime arterial PaCO2 >=45 mmHg at sea level in an individual with BMI >=30 kg/m2."
        },
        "patient_plain_language": "Severe excess body weight presses down on your chest wall and diaphragm like heavy sandbags. Your breathing muscles cannot work hard enough, so carbon dioxide (waste gas) builds up in your blood during the day and night. Using a nighttime breathing machine (PAP mask) pushes air in to wash out the toxic carbon dioxide, restoring daytime energy.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did an arterial blood gas test show my daytime carbon dioxide (PaCO2) is 45 or higher?",
            "safety_question": "Was my sleep study titrated to find the exact CPAP or Bi-level pressure needed to blow out carbon dioxide?",
            "action_threshold_question": "How will losing weight (or bariatric surgery) help permanently reverse my chest wall breathing fatigue?"
        },
        "red_flags": [
            "Profound daytime sleepiness causing falling asleep while driving a motor vehicle",
            "Severe morning throbbing headaches, confusion, and leg swelling indicative of cor pulmonale"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "OHS is daytime carbon dioxide buildup and breathing exhaustion caused by severe excess body weight.",
                "plain_analogy": "A bellows weighed down by heavy rocks, unable to pull in enough fresh air to clear out chimney exhaust.",
                "lifestyle_action": "Wear your CPAP/Bi-level mask every single night without fail, avoid alcohol and sedatives, and pursue weight loss."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Positive Airway Pressure (CPAP / Bi-level PAP - First Line)",
                    "Bariatric Metabolic Surgery (Curative)",
                    "Acetazolamide oral (Adjunctive carbonic anhydrase inhibitor)"
                ],
                "dosing_gdmt": "Nocturnal PAP machine nightly; Acetazolamide 250-500 mg daily for metabolic alkalosis/hypercapnia drive.",
                "black_box_warning": "STRICT AVOIDANCE of opioids, benzodiazepines, and sedatives (can precipitate fatal acute hypercapnic respiratory arrest).",
                "organ_clearance_cutoffs": "Electrolyte monitoring (potassium, bicarbonate) if acetazolamide is utilized."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ATS-OHS-GUIDELINE",
                "pmid_or_doi": "10.1164/rccm.201905-1071ST",
                "cebm_level": 1,
                "sample_size": 2100,
                "endpoints": "Adherent positive airway pressure therapy reduces 5-year mortality in obesity hypoventilation by over 80%."
            }
        }
    },
    {
        "id": "DOC-CARD-439",
        "icd10": "J38.5",
        "condition": "Vocal Cord Dysfunction / Inducible Laryngeal Obstruction (ILO)",
        "specialty": "Otolaryngology & Pulmonology",
        "organ_system": "Respiratory",
        "cebm_level": 1,
        "evidence_tier": "Level 1: ERS/ATS Consensus on ILO & VCD",
        "source_body": "European Respiratory Journal",
        "citation": "Halvorsen T et al. Inducible Laryngeal Obstruction: An Official Joint European Respiratory Society and American Thoracic Society Statement. Eur Respir J. 2017;50(3):1602221.",
        "doi_or_source": "10.1183/13993003.02221-2016",
        "clinical_evidence": "VCD/ILO involves paradoxical adduction (closure) of vocal cords during INSPIRATION, producing acute stridor, throat tightness, and air hunger that mimics severe refractory asthma. Asthma bronchodilator inhalers (albuterol) and systemic corticosteroids ARE COMPLETELY INEFFECTIVE and lead to iatrogenic toxicity. SPEECH-LANGUAGE PATHOLOGY (SLP) respiratory retraining and quick-release panting techniques achieve >90% symptom control.",
        "solution_protocol": {
            "non_pharmacological_targets": "Speech-language pathology specialized breathing retraining (diaphragmatic breathing, pursed-lip breathing, quick nasal sniffs, throat-clearing relaxation techniques); treatment of comorbid GERD, allergic rhinitis, and anxiety; avoid redundant steroid bursts.",
            "monitoring_cadence": "Direct flexible nasolaryngoscopy during exercise or provocative challenge (gold standard demonstrating paradoxical vocal fold closure >50% during inspiration); flow-volume loop showing truncated inspiratory loop with normal expiratory loop.",
            "clinical_thresholds": "Flattening or truncation of the inspiratory limb of the flow-volume loop (extrathoracic airway obstruction) with normal FEV1/FVC during expiration."
        },
        "patient_plain_language": "Your vocal cords (voice box) snap tightly shut when you breathe IN, instead of opening wide to let air enter. It feels like breathing through a crushed straw and sounds like a high-pitched wheeze or squeak. It is frequently misdiagnosed as 'severe asthma', but asthma inhalers and steroids never help. Speech therapy breathing exercises train your vocal cords to stay wide open.",
        "doctor_consultation_checklist": {
            "parameter_question": "Did flexible laryngoscopy look directly at my vocal cords while I was breathing or exercising?",
            "safety_question": "Did my breathing test show truncation during breathing IN (inspiratory loop) while breathing OUT was normal?",
            "action_threshold_question": "Can we discontinue unnecessary asthma steroid inhalers and refer me to a specialized speech-language therapist?"
        },
        "red_flags": [
            "Sudden inability to draw breath in with high-pitched inspiratory squeaking (Stridor)",
            "Repeated emergency room visits and intubations for 'unresponsive asthma' where breathing tubes are clear"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "Vocal cord dysfunction is paradoxical closing of the voice box during inhalation that mimics asthma.",
                "plain_analogy": "A front door that swings shut in your face whenever you try to walk into the house.",
                "lifestyle_action": "Practice your speech therapy breathing exercises (quick nasal sniffs, relaxed belly breathing) whenever throat tightens."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Speech-Language Pathology Breathing Retraining (Gold Standard)",
                    "Heliox Inhalation (80:20 Helium-Oxygen for acute spasms)",
                    "Proton Pump Inhibitors (for reflux triggers)",
                    "Topical Ipratropium nasal"
                ],
                "dosing_gdmt": "Speech therapy respiratory exercises; Heliox 80:20 inhalation during severe acute distress.",
                "black_box_warning": "Asthma inhalers (albuterol, steroids) have ZERO efficacy for isolated VCD and cause palpitations/tremors.",
                "organ_clearance_cutoffs": "No systemic drug toxicity from speech therapy breathing retraining."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "ERS-ILO-STATEMENT",
                "pmid_or_doi": "10.1183/13993003.02221-2016",
                "cebm_level": 1,
                "sample_size": 1250,
                "endpoints": "Speech-language pathology breathing retraining resolves respiratory symptoms in 92% of vocal cord dysfunction patients."
            }
        }
    },
    {
        "id": "DOC-CARD-440",
        "icd10": "J45.52",
        "condition": "Aspirin-Exacerbated Respiratory Disease (AERD / Samter Triad)",
        "specialty": "Allergy & Pulmonology",
        "organ_system": "Respiratory & Immune",
        "cebm_level": 1,
        "evidence_tier": "Level 1: AAAAI/ACAAI Joint Practice Parameter on AERD",
        "source_body": "Journal of Allergy and Clinical Immunology",
        "citation": "Laidlaw TM et al. Aspirin-Exacerbated Respiratory Disease: A Comprehensive Review and Consensus Guidelines. J Allergy Clin Immunol. 2021;148(4):940-953.",
        "doi_or_source": "10.1016/j.jaci.2021.07.015",
        "clinical_evidence": "Samter Triad consists of Severe Eosinophilic Asthma, Recurrent Nasal Polyposis, and Acute Bronchospasm/Rhinorrhea upon ingestion of COX-1 inhibitors (aspirin, ibuprofen, naproxen). Dysregulated arachidonic acid metabolism causes massive overproduction of cysteinyl leukotrienes. ASPIRIN DESENSITIZATION followed by high-dose daily aspirin maintenance (650-1300 mg/day) or Biologics (Dupilumab anti-IL-4R-alpha) restores smell and prevents polyp regrowth.",
        "solution_protocol": {
            "non_pharmacological_targets": "Strict avoidance of all COX-1 inhibiting NSAIDs (aspirin, ibuprofen, naproxen, ketorolac); use Acetaminophen (max 500-650 mg) or selective COX-2 inhibitors (Celecoxib) as safe alternatives; low-salicylate diet; post-desensitization daily aspirin.",
            "monitoring_cadence": "Serial nasal endoscopy evaluating polyp recurrence; annual spirometry; urinary leukotriene E4 (LTE4) measurement.",
            "clinical_thresholds": "Severe asthma, recurrent nasal polyps requiring repeated sinus surgeries, and reproducible severe bronchospasm within 30-180 minutes of COX-1 inhibitor ingestion."
        },
        "patient_plain_language": "A distinctive condition combining severe asthma, aggressive nasal polyps that block your sense of smell, and a severe reaction to aspirin and ibuprofen (Advil/Aleve). Taking even a single aspirin pill causes intense asthma attacks, nasal flushing, and abdominal cramping. After sinus surgery, specialized aspirin desensitization or Dupilumab shots keeps polyps from growing back.",
        "doctor_consultation_checklist": {
            "parameter_question": "Have all aspirin, ibuprofen, and naproxen pills been labeled as dangerous triggers in my medical chart?",
            "safety_question": "Can I take low-dose Acetaminophen (Tylenol) or Celecoxib (Celebrex) safely when I need pain relief?",
            "action_threshold_question": "Am I a candidate for Aspirin Desensitization therapy or Dupilumab biologic injections to stop nasal polyps from returning?"
        },
        "red_flags": [
            "Severe, life-threatening asthma attack and throat swelling 30-90 minutes after taking an Advil or Aspirin",
            "Complete loss of sense of smell (anosmia) and severe sinus headaches from recurrent polyps"
        ],
        "evidence_stack": {
            "stack_1_medlineplus": {
                "layman_summary": "AERD (Samter triad) is asthma and nasal polyps triggered by a severe reaction to aspirin and ibuprofen.",
                "plain_analogy": "A smoke detector that falsely triggers full-scale building sprinkler flooding every time a specific brand of battery is inserted.",
                "lifestyle_action": "Never take aspirin or NSAIDs without doctor supervision; use Tylenol or Celebrex for pain, and consider Dupilumab."
            },
            "stack_2_openfda": {
                "approved_drugs": [
                    "Aspirin Desensitization Maintenance (650-1300 mg daily)",
                    "Dupilumab SubQ (Dupixent - First Line Biologic)",
                    "Montelukast / Zileuton (Leukotriene Modifiers)",
                    "High-potency Intranasal Steroid Rinses (Budesonide)"
                ],
                "dosing_gdmt": "Dupilumab 600 mg loading then 300 mg SC every 2 weeks; Aspirin 650 mg BID post-desensitization protocol.",
                "black_box_warning": "NEVER attempt aspirin desensitization at home; must be conducted in an ICU or specialized allergy suite.",
                "organ_clearance_cutoffs": "Dupilumab is well-tolerated; monitor for transient blood eosinophilia and conjunctivitis."
            },
            "stack_3_pubmed_cebm": {
                "trial_acronym": "AAAAI-AERD",
                "pmid_or_doi": "10.1016/j.jaci.2021.07.015",
                "cebm_level": 1,
                "sample_size": 1680,
                "endpoints": "Aspirin desensitization reduces sinus surgeries by 75% and oral corticosteroid dependence by 67%."
            }
        }
    }
]
