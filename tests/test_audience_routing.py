import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.core.prompts import normalize_audience, route_prompt, PATIENT_PROMPT, CLINICIAN_PROMPT
from app.models.enums import UserMode
from app.services.rag_agent import MedicalRAGAgent

class TestAudienceRouting(unittest.TestCase):
    def setUp(self):
        self.rag = MedicalRAGAgent()

    def test_normalize_audience(self):
        """Test audience normalization to canonical values."""
        
        # Test patient variations (should all → 'patient')
        self.assertEqual(normalize_audience('patient'), 'patient')
        self.assertEqual(normalize_audience('Patient'), 'patient')
        self.assertEqual(normalize_audience(None), 'patient')
        self.assertEqual(normalize_audience('invalid_value'), 'patient')
        
        # Test doctor variations (should all → 'doctor')
        self.assertEqual(normalize_audience('doctor'), 'doctor')
        self.assertEqual(normalize_audience('Doctor'), 'doctor')
        self.assertEqual(normalize_audience('clinician'), 'doctor')
        self.assertEqual(normalize_audience('professional'), 'doctor')
        self.assertEqual(normalize_audience('physician'), 'doctor')
        self.assertEqual(normalize_audience('md'), 'doctor')
        self.assertEqual(normalize_audience('healthcare_provider'), 'doctor')
        
        # Test with UserMode enum
        self.assertEqual(normalize_audience(UserMode.PATIENT), 'patient')
        self.assertEqual(normalize_audience(UserMode.PROFESSIONAL), 'doctor')
        self.assertEqual(normalize_audience(UserMode.DOCTOR), 'doctor')

    def test_prompt_routing(self):
        """Test that correct prompt is selected based on audience."""
        
        query = "What is a heart attack?"
        context = "A myocardial infarction is an acute coronary syndrome..."
        
        # Patient mode should return PATIENT_PROMPT formatted
        patient_prompt = route_prompt('patient', query, context)
        self.assertIn("6th-grade reading level", patient_prompt)
        self.assertIn("plain, everyday English", patient_prompt)
        self.assertIn("myocardial infarction", patient_prompt)
        
        # Doctor mode should return CLINICIAN_PROMPT formatted
        doctor_prompt = route_prompt('doctor', query, context)
        self.assertIn("graduate-level medical terminology", doctor_prompt)
        self.assertIn("Hazard Ratios", doctor_prompt)
        self.assertIn("p-values", doctor_prompt)
        
        # All doctor variants should produce same prompt
        clinician_prompt = route_prompt('clinician', query, context)
        professional_prompt = route_prompt('professional', query, context)
        self.assertEqual(doctor_prompt, clinician_prompt)
        self.assertEqual(doctor_prompt, professional_prompt)

    def test_language_level_separation(self):
        """Verify patient vs doctor prompts have strict language level differences."""
        
        # Patient prompt should contain 6th-grade / everyday English
        self.assertIn("6th-grade", PATIENT_PROMPT)
        self.assertIn("everyday English", PATIENT_PROMPT)
        self.assertIn("myocardial infarction", PATIENT_PROMPT)
        
        # Doctor prompt should contain clinical terminology instructions
        self.assertIn("graduate-level", CLINICIAN_PROMPT)
        self.assertIn("Hazard Ratios", CLINICIAN_PROMPT)
        self.assertIn("p-values", CLINICIAN_PROMPT)
        self.assertIn("Oxford CEBM", CLINICIAN_PROMPT)

    def test_generation_output_distinction_same_query(self):
        """Verify same query produces clearly distinct outputs for patient vs doctor."""
        query = "hypertension"
        patient_output = self.rag.generate(query, audience="patient")
        doctor_output = self.rag.generate(query, audience="doctor")
        
        self.assertEqual(patient_output["audience"], "patient")
        self.assertEqual(doctor_output["audience"], "doctor")
        
        # Answers must be distinct in style and structure
        self.assertNotEqual(patient_output["answer"], doctor_output["answer"])
        
        # Patient output features
        self.assertIn("Grade 6.0", patient_output["reading_level"])
        self.assertIn("blood pressure", patient_output["answer"].lower())
        
        # Doctor output features
        self.assertIn("Postgraduate Clinical Level", doctor_output["reading_level"])
        self.assertTrue(
            "guideline" in doctor_output["answer"].lower() or 
            "clinical" in doctor_output["answer"].lower() or
            "cebm" in doctor_output["answer"].lower()
        )

if __name__ == '__main__':
    unittest.main()
