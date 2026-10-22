"""
Assemble and validate the complete new diseases dataset.
Combines:
- Parts 1 to 5 (DOC-CARD-101 to 200: 100 diseases)
- Parts 6 to 10 (DOC-CARD-201 to 300: 100 diseases)
- Parts 11 to 15 (DOC-CARD-301 to 400: 100 False-Twin & Critical Diseases)
- Parts 16 to 20 (DOC-CARD-401 to 500: 100 Advanced Specialty Twins & Diseases)
Total: 400 new verified conditions (DOC-CARD-101 to 500), combined with the original 100 base conditions = exactly 500 diseases.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Parts 1 to 5 (101 to 200)
from scripts.dataset_parts.part1_cardio_pulm import PART_1_DISEASES
from scripts.dataset_parts.part2_endo_gi import PART_2_DISEASES
from scripts.dataset_parts.part3_neuro_renal import PART_3_DISEASES
from scripts.dataset_parts.part4_rheum_id import PART_4_DISEASES
from scripts.dataset_parts.part5_hemonc_derm_psych_misc import PART_5_DISEASES

# Parts 6 to 10 (201 to 300)
from scripts.dataset_parts.part6_cardio_pulm_vascular import PART_6_DISEASES
from scripts.dataset_parts.part7_gi_hepatic_endo import PART_7_DISEASES
from scripts.dataset_parts.part8_neuro_psych_specialty import PART_8_DISEASES
from scripts.dataset_parts.part9_nephro_rheum_immunology import PART_9_DISEASES
from scripts.dataset_parts.part10_hematology_oncology_infectious_derm import PART_10_DISEASES

# Parts 11 to 15 (301 to 400)
from scripts.dataset_parts.part11_false_twins import PART_11_DISEASES
from scripts.dataset_parts.part12_endo_electrolyte_twins import PART_12_DISEASES
from scripts.dataset_parts.part13_neuro_psych_twins import PART_13_DISEASES
from scripts.dataset_parts.part14_gi_heme_twins import PART_14_DISEASES
from scripts.dataset_parts.part15_id_critcare_twins import PART_15_DISEASES

# Parts 16 to 20 (401 to 500)
from scripts.dataset_parts.part16_adv_cardio_twins import PART_16_DISEASES
from scripts.dataset_parts.part17_adv_pulm_twins import PART_17_DISEASES
from scripts.dataset_parts.part18_adv_gi_twins import PART_18_DISEASES
from scripts.dataset_parts.part19_adv_neph_twins import PART_19_DISEASES
from scripts.dataset_parts.part20_adv_oncheme_twins import PART_20_DISEASES

# Parts 21 to 22 (501 to 550)
from scripts.dataset_parts.part21_emergency_toxicology_metabolic import PART_21_DISEASES
from scripts.dataset_parts.part22_pediatric_rare_neuro_genetics import PART_22_DISEASES

# Part 23 (551 to 600: Everyday Symptoms, Common Minor Injuries, Ambulatory Day-to-Day Conditions)
from scripts.dataset_parts.part23_everyday_symptoms_and_minor_injuries import PART_23_DISEASES

PARTS_1_TO_5 = [
    PART_1_DISEASES,
    PART_2_DISEASES,
    PART_3_DISEASES,
    PART_4_DISEASES,
    PART_5_DISEASES,
]

PARTS_6_TO_10 = [
    PART_6_DISEASES,
    PART_7_DISEASES,
    PART_8_DISEASES,
    PART_9_DISEASES,
    PART_10_DISEASES,
]

PARTS_11_TO_15 = [
    PART_11_DISEASES,
    PART_12_DISEASES,
    PART_13_DISEASES,
    PART_14_DISEASES,
    PART_15_DISEASES,
]

PARTS_16_TO_20 = [
    PART_16_DISEASES,
    PART_17_DISEASES,
    PART_18_DISEASES,
    PART_19_DISEASES,
    PART_20_DISEASES,
]

PARTS_21_TO_22 = [
    PART_21_DISEASES,
    PART_22_DISEASES,
]

NEW_100_DISEASES: List[Dict[str, Any]] = []
for p in PARTS_1_TO_5:
    NEW_100_DISEASES.extend(p)

NEW_200_TO_300_DISEASES: List[Dict[str, Any]] = []
for p in PARTS_6_TO_10:
    NEW_200_TO_300_DISEASES.extend(p)

NEW_301_TO_400_DISEASES: List[Dict[str, Any]] = []
for p in PARTS_11_TO_15:
    NEW_301_TO_400_DISEASES.extend(p)

NEW_401_TO_500_DISEASES: List[Dict[str, Any]] = []
for p in PARTS_16_TO_20:
    NEW_401_TO_500_DISEASES.extend(p)

NEW_501_TO_550_DISEASES: List[Dict[str, Any]] = []
for p in PARTS_21_TO_22:
    NEW_501_TO_550_DISEASES.extend(p)

NEW_551_TO_600_DISEASES: List[Dict[str, Any]] = list(PART_23_DISEASES)

ALL_NEW_DISEASES: List[Dict[str, Any]] = (
    NEW_100_DISEASES +
    NEW_200_TO_300_DISEASES +
    NEW_301_TO_400_DISEASES +
    NEW_401_TO_500_DISEASES +
    NEW_501_TO_550_DISEASES +
    NEW_551_TO_600_DISEASES
)

NEW_ICD10_MAP: Dict[str, str] = {
    item["id"]: item["icd10"] for item in ALL_NEW_DISEASES
}

def validate():
    assert len(NEW_100_DISEASES) == 100, f"Expected 100 diseases (101-200), got {len(NEW_100_DISEASES)}"
    assert len(NEW_200_TO_300_DISEASES) == 100, f"Expected 100 diseases (201-300), got {len(NEW_200_TO_300_DISEASES)}"
    assert len(NEW_301_TO_400_DISEASES) == 100, f"Expected 100 diseases (301-400), got {len(NEW_301_TO_400_DISEASES)}"
    assert len(NEW_401_TO_500_DISEASES) == 100, f"Expected 100 diseases (401-500), got {len(NEW_401_TO_500_DISEASES)}"
    assert len(NEW_501_TO_550_DISEASES) == 50, f"Expected 50 diseases (501-550), got {len(NEW_501_TO_550_DISEASES)}"
    assert len(NEW_551_TO_600_DISEASES) == 50, f"Expected 50 diseases (551-600), got {len(NEW_551_TO_600_DISEASES)}"
    assert len(ALL_NEW_DISEASES) == 500, f"Expected 500 total new diseases (101-600), got {len(ALL_NEW_DISEASES)}"

    required_keys = [
        "id", "icd10", "condition", "specialty", "organ_system",
        "cebm_level", "evidence_tier", "source_body", "citation",
        "doi_or_source", "clinical_evidence", "solution_protocol",
        "patient_plain_language", "doctor_consultation_checklist", "red_flags"
    ]
    sol_keys = ["non_pharmacological_targets", "monitoring_cadence", "clinical_thresholds"]
    doc_keys = ["parameter_question", "safety_question", "action_threshold_question"]

    for idx, d in enumerate(ALL_NEW_DISEASES):
        expected_id = f"DOC-CARD-{101 + idx}"
        assert d["id"] == expected_id, f"Index {idx}: expected {expected_id}, got {d['id']}"
        for k in required_keys:
            assert k in d and d[k], f"Missing/empty key '{k}' in {d['id']}"
        for sk in sol_keys:
            assert sk in d["solution_protocol"] and d["solution_protocol"][sk], f"Missing '{sk}' in {d['id']}"
        for dk in doc_keys:
            assert dk in d["doctor_consultation_checklist"] and d["doctor_consultation_checklist"][dk], f"Missing '{dk}' in {d['id']}"
        assert isinstance(d["red_flags"], list) and len(d["red_flags"]) > 0, f"Invalid red_flags in {d['id']}"

    print(f"[OK] Validation passed: exactly 500 new diseases (DOC-CARD-101 to DOC-CARD-600) verified.")

if __name__ == "__main__":
    validate()
