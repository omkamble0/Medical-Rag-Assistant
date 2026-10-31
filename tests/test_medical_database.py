import sys
import os
import unittest
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.services.medical_db import medical_db
from app.models.medical_db_schemas import SymptomCheckerRequest
from app.routes.medical_database import (
    get_database_stats,
    list_diseases,
    get_disease_by_id,
    list_symptoms,
    check_symptoms,
    list_solutions,
    list_papers,
    search_hybrid_endpoint,
    HybridSearchRequest
)


class TestMedicalDatabase(unittest.TestCase):

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

    def test_symptom_checker_differential(self):
        """Verifies symptom checker matches correct conditions."""
        req = SymptomCheckerRequest(
            symptoms=["Occipital morning headache", "Fatigue"],
            top_k=3
        )
        res = medical_db.check_symptoms(req)
        self.assertGreaterEqual(len(res.top_matches), 1)
        self.assertIsNotNone(res.top_matches[0].matched_symptoms)

    def test_hybrid_search(self):
        """Verifies hybrid lexical + vector search."""
        hits = medical_db.search_hybrid("high blood pressure ACE inhibitors", top_k=3)
        self.assertGreaterEqual(len(hits), 1)
        self.assertTrue("similarity_score" in hits[0] or "score" in hits[0])

    def test_api_stats(self):
        stats = medical_db.get_stats()
        self.assertGreaterEqual(stats.total_diseases, 100)
        self.assertIsNotNone(stats.vector_store_status)

    def test_api_get_diseases(self):
        res = medical_db.get_diseases(specialty="Neurology", limit=5)
        self.assertGreaterEqual(len(res), 1)
        self.assertEqual(res[0].specialty, "Neurology")

    def test_api_get_disease_detail(self):
        res = medical_db.get_disease_by_id("DOC-CARD-001")
        assert res is not None
        self.assertEqual(res.name, "Essential Hypertension")
        self.assertEqual(res.icd10_code, "I10")

    def test_api_get_symptoms(self):
        res = medical_db.get_all_symptoms(limit=10)
        self.assertGreaterEqual(len(res), 5)
        self.assertIn("associated_conditions_count", res[0])

    def test_api_post_symptom_checker(self):
        payload = SymptomCheckerRequest(
            symptoms=["wheezing", "cough", "chest tightness"],
            top_k=3
        )
        res = medical_db.check_symptoms(payload)
        self.assertEqual(len(res.top_matches), 3)
        self.assertIsNotNone(res.disclaimer)

    def test_api_get_solutions(self):
        res = medical_db.get_solutions(limit=5)
        self.assertGreaterEqual(len(res), 1)

    def test_api_get_papers(self):
        res = medical_db.get_research_papers(limit=5)
        self.assertGreaterEqual(len(res), 1)

    def test_api_search_hybrid(self):
        res = medical_db.search_hybrid(query="COVID-19 nirmatrelvir ritonavir", top_k=2)
        self.assertGreaterEqual(len(res), 1)


if __name__ == "__main__":
    unittest.main()
