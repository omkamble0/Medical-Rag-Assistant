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

    def test_best_evidence_based_no_breast_corruption(self):
        # Regression test for reported issue: 'best' must never be changed to 'breast'
        q = "What are the best evidence-based treatments for chronic anxiety and panic disorders?"
        res = self.guard.validate(q)
        self.assertFalse(res["needs_correction"])
        self.assertEqual(res["corrected"], q)
        self.assertNotIn("breast", res["corrected"].lower())
        self.assertIn("best", res["corrected"].lower())
        self.assertIn("evidence-based", res["corrected"].lower())

        # Test true typo correction for 'tretmeant'
        q_typo = "best evidence based tretmeant"
        res_typo = self.guard.validate(q_typo)
        self.assertTrue(res_typo["needs_correction"])
        self.assertEqual(res_typo["corrected"], "best evidence based treatment")
        self.assertNotIn("breast", res_typo["corrected"].lower())

        # Test protection of common short English words
        q_common = "safe dose fast rest test care pain rate"
        res_common = self.guard.validate(q_common)
        self.assertFalse(res_common["needs_correction"])
        self.assertEqual(res_common["corrected"], q_common)

    def test_rag_agent_retrieval_and_generation(self):
        patient_res = self.rag.generate("headache", audience="patient")
        self.assertIn("answer", patient_res)
        self.assertGreater(len(patient_res["sources"]), 0)
        self.assertEqual(patient_res["audience"], "patient")

        doctor_res = self.rag.generate("hypertension", audience="doctor")
        self.assertIn("answer", doctor_res)
        self.assertGreater(len(doctor_res["sources"]), 0)
        self.assertEqual(doctor_res["audience"], "doctor")

    def test_hallucination_avoider_and_checker(self):
        from app.services.crag.hallucination_grader import avoid_hallucinations, audit_hallucinations_and_grounding
        sources = [
            {"citation_index": 1, "title": "EPIC-HR Trial", "content": "Paxlovid reduced COVID-19 hospitalization by 89% in 2,246 patients."}
        ]
        # Text with a phantom citation [9]
        dirty_text = "Treatment reduced hospitalization by 89% [1]. Unverified assertions also made [9]."
        cleaned, audit = avoid_hallucinations(dirty_text, sources)
        self.assertNotIn("[9]", cleaned)
        self.assertIn("[1]", cleaned)
        self.assertTrue(len(audit.corrections_applied) > 0)
        self.assertTrue(audit.grounding_score >= 0.70)
        self.assertTrue(audit.is_grounded)

    def test_enhanced_semantic_search_and_retrieval(self):
        from app.services.vector_store import retrieve_clinical_evidence
        # Test panic disorder retrieval with hyphenated concept
        sources = retrieve_clinical_evidence("What are the best evidence-based treatments for chronic anxiety and panic disorders?", top_k=2)
        self.assertGreater(len(sources), 0)
        top = sources[0]
        # Must match psychiatric / anxiety / panic evidence
        self.assertTrue(any(w in f"{top.title} {top.snippet}".lower() for w in ["anxiety", "panic", "ssri", "cbt", "mental"]))

    def test_detailed_explanations_patient_and_doctor(self):
        from app.services.rag_engine import process_clinical_query
        from app.models.enums import UserMode

        # Patient register verification
        res_patient = process_clinical_query("What are evidence-based treatments for hypertension?", user_mode=UserMode.PATIENT)
        self.assertIn("### 1. Understanding the Condition: What It Is & How It Works", res_patient.answer)
        self.assertIn("### 2. Detailed Medical Explanation: What Clinical Research Shows", res_patient.answer)
        self.assertIn("### 3. Research-Backed Practical Solutions & Daily Care", res_patient.answer)
        self.assertIsNotNone(res_patient.patient_suggestions)
        self.assertGreater(len(res_patient.patient_suggestions.lifestyle_recommendations), 0)

        # Doctor register verification
        res_doc = process_clinical_query("What are evidence-based treatments for hypertension?", user_mode=UserMode.PROFESSIONAL)
        self.assertIn("### 1. Disease Overview, Pathophysiologic Mechanisms & Biomarkers", res_doc.answer)
        self.assertIn("### 2. In-Depth Clinical Trial & Research Paper Analysis", res_doc.answer)
        self.assertIn("### 3. Guideline-Directed Medical Therapy (GDMT) Solutions & Titration Protocols", res_doc.answer)
        self.assertIn("### 4. Organ Surveillance, Pharmacokinetics & Adverse Reaction Mitigation", res_doc.answer)
        self.assertIsNotNone(res_doc.clinician_suggestions)
        self.assertGreater(len(res_doc.clinician_suggestions.titration_protocols), 0)


if __name__ == "__main__":
    unittest.main()

