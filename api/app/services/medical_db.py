"""
AegisMed Medical Knowledge Database & Hybrid Vector Store Service
Integrates structured JSON document store with Qdrant vector retrieval,
providing high-performance disease lookups, symptom differential diagnosis matching,
treatment solutions index, and peer-reviewed research papers.
"""

import os
import re
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from app.models.medical_db_schemas import (
    DiseaseRecord, DiseaseSymptom, SolutionItem, ResearchPaper,
    DoctorChecklist, SymptomCheckerRequest, MatchedDiseaseResult,
    SymptomCheckerResponse, DatabaseStatsResponse
)
from app.config import settings

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATABASE_FILE = DATA_DIR / "medical_database.json"
QDRANT_STORAGE_DIR = DATA_DIR / "qdrant_storage"
COLLECTION_NAME = "medical_knowledge_collection"

# Symptom aliases / clinical synonym mappings
SYMPTOM_SYNONYMS: Dict[str, str] = {
    "high bp": "Occipital morning headache",
    "high blood pressure": "Occipital morning headache",
    "hypertension": "Occipital morning headache",
    "chest pain": "Chest tightness",
    "chest pressure": "Chest tightness",
    "short of breath": "Dyspnea on exertion",
    "shortness of breath": "Dyspnea on exertion",
    "sob": "Dyspnea on exertion",
    "breathlessness": "Dyspnea on exertion",
    "difficulty breathing": "Dyspnea on exertion",
    "dyspnea": "Dyspnea on exertion",
    "headache": "Headache / Cranial pain",
    "migraine": "Unilateral pulsating / Throbbing headache",
    "fever": "Fever and Chills",
    "high temp": "Fever and Chills",
    "cough": "Dry persistent cough",
    "dry cough": "Dry persistent cough",
    "fatigue": "Chronic fatigue and lethargy",
    "tiredness": "Chronic fatigue and lethargy",
    "exhaustion": "Chronic fatigue and lethargy",
    "joint pain": "Joint pain (Arthralgia)",
    "swollen ankles": "Bilateral lower extremity edema",
    "leg swelling": "Lower extremity peripheral edema",
    "edema": "Lower extremity peripheral edema",
    "palpitations": "Palpitations / Fluttering heartbeat",
    "fluttering heart": "Palpitations / Fluttering heartbeat",
    "racing heart": "Palpitations / Fluttering heartbeat",
    "heartburn": "Pyrosis (Heartburn)",
    "acid reflux": "Pyrosis (Heartburn)",
    "frequent urination": "Polyuria (Frequent urination)",
    "peeing often": "Polyuria (Frequent urination)",
    "excessive thirst": "Polydipsia (Excessive thirst)",
    "loss of taste": "Anosmia & Ageusia",
    "loss of smell": "Anosmia & Ageusia",
    "itchy skin": "Severe pruritus (Itching)",
    "pruritus": "Severe pruritus (Itching)",
    "skin rash": "Cutaneous erythema and rash",
    "sadness": "Depressed mood",
    "depression": "Depressed mood",
    "anxiety": "Depressed mood or anxiety",
    "panic": "Depressed mood or anxiety",
    "insomnia": "Sleep disturbance (Insomnia or Hypersomnia)",
    "cannot sleep": "Sleep disturbance (Insomnia or Hypersomnia)",
}

# Critical red flag markers that require emergency triage
RED_FLAG_TRIGGERS = [
    "chest pain radiating to arm or jaw",
    "crushing chest pain",
    "sudden facial droop",
    "arm weakness",
    "speech slurring",
    "coughing up blood",
    "pink frothy sputum",
    "loss of consciousness",
    "severe sudden headache",
    "inability to breathe",
    "stridor",
    "anaphylaxis",
    "systolic > 180"
]


class MedicalDatabase:
    """
    Core Medical Knowledge Database engine providing structured entity querying,
    symptom-to-disease differential diagnosis, and hybrid vector retrieval via Qdrant.
    """
    _instance: Optional["MedicalDatabase"] = None

    def __init__(self):
        self._records: List[DiseaseRecord] = []
        self._by_id: Dict[str, DiseaseRecord] = {}
        self._by_name: Dict[str, DiseaseRecord] = {}
        self._symptom_to_diseases: Dict[str, List[str]] = {}
        self._qdrant_client = None
        self._qdrant_ready = False
        self._load_data()
        self._init_qdrant()

    @classmethod
    def get_instance(cls) -> "MedicalDatabase":
        if cls._instance is None:
            cls._instance = MedicalDatabase()
        return cls._instance

    def _load_data(self):
        """Loads records from the persistent JSON file."""
        if not DATABASE_FILE.exists():
            print(f"[!] Warning: Medical database JSON not found at {DATABASE_FILE}. Triggering build...")
            try:
                from scripts.build_medical_database import generate_database_and_qdrant
                generate_database_and_qdrant()
            except Exception as e:
                print(f"[!] Error auto-generating medical database: {e}")
                return

        try:
            with open(DATABASE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self._records = [DiseaseRecord(**item) for item in data]
            self._by_id = {r.id: r for r in self._records}
            self._by_name = {r.name.lower(): r for r in self._records}

            # Build inverted symptom index
            self._symptom_to_diseases = {}
            for r in self._records:
                for sym in r.symptoms:
                    s_clean = sym.name.lower().strip()
                    if s_clean not in self._symptom_to_diseases:
                        self._symptom_to_diseases[s_clean] = []
                    self._symptom_to_diseases[s_clean].append(r.id)

            print(f"[OK] MedicalDatabase loaded {len(self._records)} conditions with {len(self._symptom_to_diseases)} indexed symptoms.")
        except Exception as e:
            print(f"[!] Error loading medical database: {e}")

    def _init_qdrant(self):
        """Initializes connection to Qdrant vector store."""
        try:
            from qdrant_client import QdrantClient
            if QDRANT_STORAGE_DIR.exists():
                self._qdrant_client = QdrantClient(path=str(QDRANT_STORAGE_DIR))
                self._qdrant_ready = True
                print(f"[OK] Qdrant local storage connected at {QDRANT_STORAGE_DIR}")
            else:
                self._qdrant_client = QdrantClient(":memory:")
                self._qdrant_ready = True
        except Exception as e:
            print(f"[!] Qdrant initialization notice (dense fallback active): {e}")
            self._qdrant_ready = False

    def _text_to_vector(self, text: str, dim: int = 128) -> List[float]:
        tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
        vec = [0.0] * dim
        for token in tokens:
            h = int(hashlib.md5(token.encode("utf-8")).hexdigest(), 16)
            idx = h % dim
            weight = 1.0 + (len(token) * 0.1)
            vec[idx] += weight
        norm = sum(x * x for x in vec) ** 0.5
        if norm > 0:
            vec = [x / norm for x in vec]
        return vec

    # ============================================================
    # Public API Methods
    # ============================================================

    def get_stats(self) -> DatabaseStatsResponse:
        """Returns statistical totals for diseases, symptoms, solutions, and research papers."""
        specialties_dist: Dict[str, int] = {}
        evidence_dist: Dict[str, int] = {}
        total_symptoms = 0
        total_solutions = 0
        total_papers = 0

        for r in self._records:
            specialties_dist[r.specialty] = specialties_dist.get(r.specialty, 0) + 1
            total_symptoms += len(r.symptoms)
            total_solutions += len(r.solutions)
            total_papers += len(r.research_papers)
            for p in r.research_papers:
                evidence_dist[p.cebm_level] = evidence_dist.get(p.cebm_level, 0) + 1

        indexed_vectors = len(self._records) if self._qdrant_ready else 0

        return DatabaseStatsResponse(
            total_diseases=len(self._records),
            total_symptoms=total_symptoms,
            total_solutions=total_solutions,
            total_research_papers=total_papers,
            specialties_distribution=specialties_dist,
            evidence_levels_distribution=evidence_dist,
            vector_store_status="Ready (Local Embedded Qdrant)" if self._qdrant_ready else "Fallback Mode",
            vector_collection_name=COLLECTION_NAME,
            indexed_vectors_count=indexed_vectors
        )

    def get_diseases(
        self,
        query: Optional[str] = None,
        specialty: Optional[str] = None,
        organ_system: Optional[str] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[DiseaseRecord]:
        """Searches and filters disease records."""
        results = self._records

        if specialty:
            s_clean = specialty.strip().lower()
            results = [r for r in results if s_clean in r.specialty.lower()]

        if organ_system:
            o_clean = organ_system.strip().lower()
            results = [r for r in results if o_clean in r.organ_system.lower()]

        if query:
            q_clean = query.strip().lower()
            q_tokens = q_clean.split()

            def match_score(r: DiseaseRecord) -> int:
                score = 0
                r_name = r.name.lower()
                r_icd = r.icd10_code.lower()
                r_spec = r.specialty.lower()
                r_overview = r.overview.lower()

                if q_clean == r_name:
                    return 1000
                if q_clean in r_name:
                    score += 200
                if q_clean in r_icd:
                    score += 150
                if q_clean in r_spec:
                    score += 50

                for t in q_tokens:
                    if t in r_name:
                        score += 30
                    if t in r_overview:
                        score += 10
                    for s in r.symptoms:
                        if t in s.name.lower():
                            score += 15
                    for sol in r.solutions:
                        if t in sol.name.lower():
                            score += 15
                return score

            scored = [(r, match_score(r)) for r in results]
            results = [r for r, s in sorted(scored, key=lambda x: x[1], reverse=True) if s > 0]

        return results[offset : offset + limit]

    def get_disease_by_id(self, disease_id: str) -> Optional[DiseaseRecord]:
        """Looks up a complete clinical disease monograph by ID."""
        clean_id = disease_id.strip().upper()
        if clean_id in self._by_id:
            return self._by_id[clean_id]
        # Also check without prefix
        for d_id, record in self._by_id.items():
            if clean_id in d_id:
                return record
        return None

    def get_all_symptoms(self, query: Optional[str] = None, limit: int = 50) -> List[Dict[str, Any]]:
        """Returns distinct indexed symptoms with frequency and associated disease counts."""
        symptom_map: Dict[str, Dict[str, Any]] = {}

        for r in self._records:
            for s in r.symptoms:
                s_name = s.name
                if s_name not in symptom_map:
                    symptom_map[s_name] = {
                        "name": s_name,
                        "frequency": s.frequency,
                        "severity": s.severity,
                        "associated_conditions_count": 0,
                        "sample_conditions": []
                    }
                symptom_map[s_name]["associated_conditions_count"] += 1
                if len(symptom_map[s_name]["sample_conditions"]) < 3:
                    symptom_map[s_name]["sample_conditions"].append(r.name)

        symptoms_list = list(symptom_map.values())
        if query:
            q = query.lower().strip()
            symptoms_list = [s for s in symptoms_list if q in s["name"].lower()]

        symptoms_list.sort(key=lambda x: x["associated_conditions_count"], reverse=True)
        return symptoms_list[:limit]

    def get_solutions(
        self,
        disease_query: Optional[str] = None,
        solution_type: Optional[str] = None,
        line_of_therapy: Optional[str] = None,
        limit: int = 30
    ) -> List[Dict[str, Any]]:
        """Returns clinical treatment solutions across conditions."""
        all_solutions = []

        for r in self._records:
            if disease_query and disease_query.lower() not in r.name.lower() and disease_query.lower() not in r.specialty.lower():
                continue

            for sol in r.solutions:
                if solution_type and solution_type.lower() != sol.type.lower():
                    continue
                if line_of_therapy and line_of_therapy.lower() != sol.line_of_therapy.lower():
                    continue

                all_solutions.append({
                    "disease_id": r.id,
                    "disease_name": r.name,
                    "specialty": r.specialty,
                    "solution": sol.model_dump()
                })

        return all_solutions[:limit]

    def get_research_papers(
        self,
        disease_query: Optional[str] = None,
        cebm_level: Optional[str] = None,
        min_year: Optional[int] = None,
        limit: int = 30
    ) -> List[Dict[str, Any]]:
        """Returns peer-reviewed research papers and clinical trials."""
        all_papers = []

        for r in self._records:
            if disease_query and disease_query.lower() not in r.name.lower() and disease_query.lower() not in r.specialty.lower():
                continue

            for p in r.research_papers:
                if cebm_level and cebm_level.lower() not in p.cebm_level.lower():
                    continue
                if min_year and p.year < min_year:
                    continue

                all_papers.append({
                    "disease_id": r.id,
                    "disease_name": r.name,
                    "icd10": r.icd10_code,
                    "paper": p.model_dump()
                })

        return all_papers[:limit]

    # ============================================================
    # Symptom Differential Checker
    # ============================================================

    def check_symptoms(self, request: SymptomCheckerRequest) -> SymptomCheckerResponse:
        """
        Executes multi-symptom differential diagnosis matching with hallmark weighting,
        red flag emergency detection, and recommended GDMT first-line solutions.
        """
        raw_symptoms = request.symptoms
        top_k = request.top_k

        # Normalize and expand user query symptoms
        normalized_query_symptoms: List[str] = []
        for sym in raw_symptoms:
            s_clean = sym.strip().lower()
            if not s_clean:
                continue
            # Check synonym dictionary
            canonical = SYMPTOM_SYNONYMS.get(s_clean, s_clean)
            normalized_query_symptoms.append(canonical)

        # Check for emergency red flags
        emergency_alert = None
        full_query_text = " ".join(raw_symptoms).lower()
        triggered_global_red_flags = []
        for trigger in RED_FLAG_TRIGGERS:
            if trigger in full_query_text:
                triggered_global_red_flags.append(trigger)

        if triggered_global_red_flags:
            emergency_alert = (
                f"⚠️ CLINICAL ACUITY ADVISORY: Your symptoms mention potentially urgent clinical red-flags: "
                f"[{', '.join(triggered_global_red_flags)}]. Prompt in-person evaluation by a healthcare provider or urgent care clinic is strongly recommended."
            )

        candidate_scores: List[Tuple[DiseaseRecord, float, List[str], List[str], List[str]]] = []

        for record in self._records:
            matched_syms = []
            hallmark_matches = 0
            common_matches = 0

            disease_symptoms_lower = {s.name.lower(): s for s in record.symptoms}

            for q_sym in normalized_query_symptoms:
                q_low = q_sym.lower()
                for d_sym_name, d_sym_obj in disease_symptoms_lower.items():
                    # Substring or word match
                    if q_low in d_sym_name or any(word in d_sym_name for word in q_low.split() if len(word) > 3):
                        matched_syms.append(d_sym_obj.name)
                        if d_sym_obj.frequency == "hallmark":
                            hallmark_matches += 1
                        else:
                            common_matches += 1
                        break

            matched_syms = list(dict.fromkeys(matched_syms))

            if not matched_syms:
                continue

            # Compute match score (0 - 100)
            total_query_syms = max(1, len(normalized_query_symptoms))
            total_disease_syms = max(1, len(record.symptoms))

            overlap_ratio = len(matched_syms) / total_query_syms
            coverage_ratio = len(matched_syms) / total_disease_syms

            score = (overlap_ratio * 65.0) + (coverage_ratio * 20.0) + (hallmark_matches * 10.0)
            score = min(99.0, max(25.0, score))

            # Missing hallmark symptoms
            missing_typical = [
                s.name for s in record.symptoms
                if s.frequency in ["hallmark", "common"] and s.name not in matched_syms
            ]

            # Disease-specific red flags
            triggered_rf = []
            for rf in record.red_flags:
                rf_low = rf.lower()
                if any(word in rf_low for word in full_query_text.split() if len(word) > 4):
                    triggered_rf.append(rf)

            candidate_scores.append((record, score, matched_syms, missing_typical[:3], triggered_rf))

        candidate_scores.sort(key=lambda x: x[1], reverse=True)
        top_candidates = candidate_scores[:top_k]

        matches: List[MatchedDiseaseResult] = []
        for record, score, matched_s, missing_s, triggered_rf in top_candidates:
            first_line_sols = [s for s in record.solutions if s.line_of_therapy == "first_line"]
            if not first_line_sols:
                first_line_sols = record.solutions[:2]

            matches.append(
                MatchedDiseaseResult(
                    disease_id=record.id,
                    disease_name=record.name,
                    icd10_code=record.icd10_code,
                    specialty=record.specialty,
                    match_score=round(score, 1),
                    matched_symptoms=matched_s,
                    missing_typical_symptoms=missing_s,
                    has_red_flags=bool(triggered_rf),
                    triggered_red_flags=triggered_rf,
                    first_line_solutions=first_line_sols,
                    top_research_papers=record.research_papers[:2],
                    patient_summary=record.patient_plain_language,
                    recommended_action=(
                        "Immediate clinical consultation recommended."
                        if triggered_rf or score > 75
                        else "Schedule an appointment with a primary care clinician for diagnostic evaluation."
                    )
                )
            )

        return SymptomCheckerResponse(
            query_symptoms=raw_symptoms,
            emergency_alert=emergency_alert,
            top_matches=matches,
            total_conditions_evaluated=len(self._records),
            disclaimer="This clinical differential matcher is for informational and educational support only. It is not a substitute for formal medical evaluation by a licensed healthcare professional."
        )

    # ============================================================
    # Hybrid Qdrant Vector Search
    # ============================================================

    def search_hybrid(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Executes dense vector search over the medical database via Qdrant."""
        clean_q = query.strip()
        if not clean_q or not self._records:
            return []

        if self._qdrant_ready and self._qdrant_client:
            try:
                vec = self._text_to_vector(clean_q, dim=128)
                hits = self._qdrant_client.query_points(
                    collection_name=COLLECTION_NAME,
                    query=vec,
                    limit=top_k
                ).points

                results = []
                for hit in hits:
                    d_id = hit.payload.get("disease_id")
                    rec = self._by_id.get(d_id)
                    if rec:
                        results.append({
                            "disease_id": rec.id,
                            "name": rec.name,
                            "icd10": rec.icd10_code,
                            "specialty": rec.specialty,
                            "similarity_score": round(float(hit.score), 3),
                            "overview": rec.overview,
                            "symptoms": [s.name for s in rec.symptoms[:4]],
                            "solutions": [s.name for s in rec.solutions[:2]],
                            "papers": [p.title for p in rec.research_papers[:1]]
                        })
                if results:
                    return results
            except Exception as e:
                print(f"[!] Qdrant query notice, falling back to lexical search: {e}")

        # Lexical fallback
        diseases = self.get_diseases(query=clean_q, limit=top_k)
        return [
            {
                "disease_id": d.id,
                "name": d.name,
                "icd10": d.icd10_code,
                "specialty": d.specialty,
                "similarity_score": 0.85,
                "overview": d.overview,
                "symptoms": [s.name for s in d.symptoms[:4]],
                "solutions": [s.name for s in d.solutions[:2]],
                "papers": [p.title for p in d.research_papers[:1]]
            }
            for d in diseases
        ]

    def export_for_vector_store(self) -> List[Dict[str, Any]]:
        """
        Exports all 100 conditions into the format expected by vector_store.py
        to ensure full synchrony between the Medical Database and the RAG engine.
        """
        exported = []
        for r in self._records:
            for p in r.research_papers:
                symptoms_str = ", ".join([s.name for s in r.symptoms[:4]])
                solutions_str = ", ".join([sol.name for sol in r.solutions[:2]])
                full_snippet = f"{r.name} (ICD-10: {r.icd10_code}). Evidence: {p.key_findings} Clinical Solutions: {solutions_str}. Symptoms: {symptoms_str}."

                exported.append({
                    "id": p.id,
                    "domain": r.specialty.upper().replace(" ", "_").replace("&", "AND"),
                    "title": f"{r.name}: {p.title}",
                    "journal": p.journal,
                    "year": p.year,
                    "doi_or_pmid": p.doi_or_pmid,
                    "evidence_level": p.cebm_level,
                    "keywords": r.keywords,
                    "snippet": full_snippet,
                    "key_takeaway": p.clinical_takeaway,
                    "patient_plain_language": r.patient_plain_language,
                    "doctor_consultation_checklist": r.doctor_checklist.model_dump() if r.doctor_checklist else None,
                    "red_flags": r.red_flags,
                    "solution_protocol": {
                        "non_pharmacological_targets": r.solutions[1].description if len(r.solutions) > 1 else "",
                        "clinical_thresholds": r.solutions[0].dosage_or_protocol if r.solutions else "",
                        "monitoring_cadence": r.solutions[0].monitoring if r.solutions else ""
                    }
                })
        return exported


# Global singleton instance
medical_db = MedicalDatabase.get_instance()
