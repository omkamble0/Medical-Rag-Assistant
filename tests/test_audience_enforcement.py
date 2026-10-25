"""
Unit tests for AegisMed Hard Audience Normalization & Readability Enforcement Engine.
Verifies:
1. Flesch-Kincaid Grade Level & Flesch Reading Ease computation.
2. Zero-statistical-leak sanitization for Patient Mode (p-values, HRs, 95% CIs, DOIs, trial names).
3. Precision preservation and Oxford CEBM grounding for Doctor Mode.
4. End-to-end audience contract enforcement across RAG generation.
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.core.readability import (
    count_syllables_in_word,
    compute_readability_metrics,
    detect_statistical_leaks,
    sanitize_patient_mode_text,
    enforce_audience_contract
)
from app.models.enums import UserMode
from app.services.rag_engine import process_clinical_query


class TestAudienceEnforcement(unittest.TestCase):

    def test_syllable_counter(self):
        """Test English syllable counter heuristics."""
        self.assertEqual(count_syllables_in_word("cat"), 1)
        self.assertEqual(count_syllables_in_word("water"), 2)
        self.assertEqual(count_syllables_in_word("hospital"), 3)
        self.assertEqual(count_syllables_in_word("hypertension"), 4)
        self.assertGreaterEqual(count_syllables_in_word("cardiovascular"), 5)

    def test_readability_computation(self):
        """Test Flesch-Kincaid Grade Level and Reading Ease calculations."""
        simple_text = (
            "Drink plenty of water every day. Rest when you feel tired. "
            "Call your doctor if your head hurts."
        )
        simple_metrics = compute_readability_metrics(simple_text)
        self.assertLessEqual(simple_metrics["flesch_kincaid_grade"], 6.0)
        self.assertGreaterEqual(simple_metrics["flesch_reading_ease"], 75.0)

        complex_text = (
            "In patients exhibiting acute decompensated heart failure with preserved ejection fraction, "
            "titration of sodium-glucose cotransporter-2 inhibitors demonstrates statistically significant "
            "attenuation of adverse cardiovascular composite endpoints."
        )
        complex_metrics = compute_readability_metrics(complex_text)
        self.assertGreaterEqual(complex_metrics["flesch_kincaid_grade"], 14.0)
        self.assertLessEqual(complex_metrics["flesch_reading_ease"], 30.0)

    def test_statistical_leak_detection(self):
        """Test detection of forbidden statistics in patient mode."""
        leaky_text = (
            "In the SPRINT trial, intensive blood pressure control achieved HR 0.75, "
            "95% CI (0.64–0.89), p < 0.001 with N = 9,361. Refer to doi: 10.1056/NEJMoa1511939."
        )
        leaks = detect_statistical_leaks(leaky_text)
        self.assertTrue(any("SPRINT" in l for l in leaks))
        self.assertTrue(any("p < 0.001" in l or "p<0.001" in l for l in leaks))
        self.assertTrue(any("HR 0.75" in l or "0.75" in l for l in leaks))
        self.assertTrue(any("95% CI" in l for l in leaks))
        self.assertTrue(any("doi:" in l.lower() for l in leaks))

    def test_patient_mode_sanitization(self):
        """Test automated cleansing of statistical soup into everyday reassuring language."""
        leaky_text = (
            "In the SPRINT trial, patients experienced significant benefit (HR 0.78, 95% CI [0.69–0.87], p < 0.001). "
            "A large sample (N = 8,420) demonstrated therapeutic success."
        )
        cleaned = sanitize_patient_mode_text(leaky_text)

        # Forbidden tokens must not appear in cleaned output
        self.assertNotIn("SPRINT", cleaned)
        self.assertNotIn("HR 0.78", cleaned)
        self.assertNotIn("p < 0.001", cleaned)
        self.assertNotIn("95% CI", cleaned)
        self.assertNotIn("N = 8,420", cleaned)

        # Plain language replacements must be present
        self.assertIn("landmark clinical studies", cleaned)
        self.assertIn("as shown in large clinical research studies", cleaned)

    def test_enforce_audience_contract_patient(self):
        """Test enforce_audience_contract for patient mode."""
        text = "Patients taking this medicine had lower blood pressure in the SPRINT trial (HR 0.75, p < 0.01)."
        clean, audit = enforce_audience_contract(text, audience="patient")

        self.assertEqual(audit["audience"], "patient")
        self.assertTrue(audit["enforced"])
        self.assertIn("Grade 6.0", audit["reading_level_label"])
        self.assertNotIn("SPRINT", clean)
        self.assertNotIn("p < 0.01", clean)

    def test_enforce_audience_contract_doctor(self):
        """Test enforce_audience_contract for doctor mode preserves precision and Oxford CEBM grounding."""
        text = (
            "Guideline-directed medical therapy for HFrEF includes SGLT2 inhibitors and ARNI titration. "
            "Landmark RCTs demonstrate significant relative risk reduction (HR 0.74, 95% CI 0.65-0.85, p < 0.001) "
            "supported by Oxford CEBM Level 1 evidentiary consensus."
        )
        clean, audit = enforce_audience_contract(text, audience="doctor")

        self.assertEqual(audit["audience"], "doctor")
        self.assertTrue(audit["enforced"])
        self.assertIn("Postgraduate Clinical Level", audit["reading_level_label"])
        self.assertTrue(audit["has_oxford_cebm_grounding"])
        # Doctor mode MUST keep the precise statistical data
        self.assertIn("HR 0.74", clean)
        self.assertIn("p < 0.001", clean)
        self.assertIn("Oxford CEBM Level 1", clean)

    def test_process_clinical_query_reading_level_integration(self):
        """Test that rag_engine output contains validated dynamic reading levels."""
        res_patient = process_clinical_query("hypertension", UserMode.PATIENT)
        self.assertIn("Grade 6.0", res_patient.reading_level)
        self.assertIn("Flesch-Kincaid", res_patient.reading_level)

        res_doctor = process_clinical_query("hypertension", UserMode.PROFESSIONAL)
        self.assertIn("Postgraduate Clinical Level", res_doctor.reading_level)
        self.assertIn("Flesch-Kincaid", res_doctor.reading_level)


if __name__ == "__main__":
    unittest.main()
