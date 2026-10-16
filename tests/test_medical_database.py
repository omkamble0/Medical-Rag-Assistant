import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from fastapi.testclient import TestClient
from app.main import app
from app.services.medical_db import medical_db
from app.models.medical_db_schemas import SymptomCheckerRequest


class TestMedicalDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_database_loads_all_records(self):
        """Verifies that the database loaded 100 clinical conditions."""
        stats = medical_db.get_stats()
        self.assertGreaterEqual(stats.total_diseases, 100)
        self.assertGreaterEqual(stats.total_symptoms, 400)
        self.assertGreaterEqual(stats.total_solutions, 150)
        self.assertGreaterEqual(stats.total_research_papers, 100)
        self.assertIn("Cardiovascular", stats.specialties_distribution)
        self.assertIn("Neurology", stats.specialties_distribution)

    def test_get_disease_by_id(self):
        """Verifies full clinical dossier lookup by ID."""
        record = medical_db.get_disease_by_id("DOC-CARD-001")
        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual(record.name, "Essential Hypertension")
        self.assertEqual(record.icd10_code, "I10")
        self.assertEqual(record.specialty, "Cardiovascular")
        self.assertGreaterEqual(len(record.symptoms), 4)
        self.assertGreaterEqual(len(record.solutions), 2)
        self.assertGreaterEqual(len(record.research_papers), 1)
        self.assertIsNotNone(record.doctor_checklist)
        self.assertTrue(len(record.red_flags) > 0)

    def test_disease_filtering(self):
        """Verifies search filtering by specialty and query."""
        cardio = medical_db.get_diseases(specialty="Cardiovascular")
        self.assertGreaterEqual(len(cardio), 5)
        for r in cardio:
            self.assertEqual(r.specialty, "Cardiovascular")

        search_res = medical_db.get_diseases(query="Diabetes")
        self.assertTrue(any("Diabetes" in r.name for r in search_res))

    def test_symptom_differential_checker(self):
        """Verifies multi-symptom differential diagnosis matching."""
        req = SymptomCheckerRequest(
            symptoms=["chest pain", "shortness of breath", "swollen ankles"],
            top_k=3
        )
        res = medical_db.check_symptoms(req)
        self.assertIsNotNone(res)
        self.assertEqual(len(res.top_matches), 3)
        top_match = res.top_matches[0]
        self.assertGreater(top_match.match_score, 50.0)
        self.assertTrue(len(top_match.matched_symptoms) > 0)
        self.assertTrue(len(top_match.first_line_solutions) > 0)
        self.assertTrue(len(top_match.top_research_papers) > 0)

    def test_symptom_checker_emergency_red_flag_alert(self):
        """Verifies that acute emergency red flags trigger critical guidance banner."""
        req = SymptomCheckerRequest(
            symptoms=["crushing chest pain radiating to arm or jaw", "difficulty breathing"],
            top_k=3
        )
        res = medical_db.check_symptoms(req)
        self.assertIsNotNone(res.emergency_alert)
        assert res.emergency_alert is not None
        self.assertIn("CLINICAL ACUITY ADVISORY", res.emergency_alert)

    def test_solutions_and_papers_search(self):
        """Verifies querying solutions and research papers."""
        sols = medical_db.get_solutions(disease_query="Hypertension", limit=5)
        self.assertGreaterEqual(len(sols), 1)

        papers = medical_db.get_research_papers(disease_query="Hypertension", limit=5)
        self.assertGreaterEqual(len(papers), 1)
        self.assertIn("Level", papers[0]["paper"]["cebm_level"])

    def test_hybrid_vector_search(self):
        """Verifies Qdrant hybrid vector similarity search."""
        hits = medical_db.search_hybrid("heart failure with reduced ejection fraction", top_k=3)
        self.assertGreaterEqual(len(hits), 1)
        self.assertTrue(any("Heart Failure" in h["name"] for h in hits))

    # ============================================================
    # REST API Endpoint Tests via TestClient
    # ============================================================

    def test_api_get_stats(self):
        res = self.client.get("/api/v1/database/stats")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(data["total_diseases"], 100)
        self.assertIn("vector_store_status", data)

    def test_api_get_diseases(self):
        res = self.client.get("/api/v1/database/diseases?specialty=Neurology&limit=5")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(len(data), 1)
        self.assertEqual(data[0]["specialty"], "Neurology")

    def test_api_get_disease_detail(self):
        res = self.client.get("/api/v1/database/diseases/DOC-CARD-001")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["name"], "Essential Hypertension")
        self.assertEqual(data["icd10_code"], "I10")

    def test_api_get_symptoms(self):
        res = self.client.get("/api/v1/database/symptoms?limit=10")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(len(data), 5)
        self.assertIn("associated_conditions_count", data[0])

    def test_api_post_symptom_checker(self):
        payload = {
            "symptoms": ["wheezing", "cough", "chest tightness"],
            "top_k": 3
        }
        res = self.client.post("/api/v1/database/symptom-checker", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(len(data["top_matches"]), 3)
        self.assertIn("disclaimer", data)

    def test_api_get_solutions(self):
        res = self.client.get("/api/v1/database/solutions?limit=5")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(len(data), 1)

    def test_api_get_papers(self):
        res = self.client.get("/api/v1/database/papers?limit=5")
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(len(data), 1)

    def test_api_search_hybrid(self):
        payload = {"query": "COVID-19 nirmatrelvir ritonavir", "top_k": 2}
        res = self.client.post("/api/v1/database/search-hybrid", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(len(data), 1)


if __name__ == "__main__":
    unittest.main()
