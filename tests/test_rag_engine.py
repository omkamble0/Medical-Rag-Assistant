import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.services.query_guard import QueryGuard
from app.services.rag_agent import MedicalRAGAgent

class TestRAGEngine(unittest.TestCase):
    def setUp(self):
        self.guard = QueryGuard()
        self.rag = MedicalRAGAgent()

    def test_query_guard_typo_correction(self):
        res1 = self.guard.validate("headavhe symptoms")
        self.assertTrue(res1["needs_correction"])
        self.assertIn("headache", res1["corrected"])

        res2 = self.guard.validate("diabtes management")
        self.assertTrue(res2["needs_correction"])
        self.assertIn("diabetes", res2["corrected"])

        res3 = self.guard.validate("normal blood pressure")
        self.assertFalse(res3["needs_correction"])

    def test_rag_agent_retrieval_and_generation(self):
        patient_res = self.rag.generate("headache", audience="patient")
        self.assertIn("answer", patient_res)
        self.assertGreater(len(patient_res["sources"]), 0)
        self.assertEqual(patient_res["audience"], "patient")

        doctor_res = self.rag.generate("hypertension", audience="doctor")
        self.assertIn("answer", doctor_res)
        self.assertGreater(len(doctor_res["sources"]), 0)
        self.assertEqual(doctor_res["audience"], "doctor")

if __name__ == "__main__":
    unittest.main()
