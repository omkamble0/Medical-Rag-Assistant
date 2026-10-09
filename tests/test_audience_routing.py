import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.core.prompts import normalize_audience, route_prompt, PATIENT_PROMPT, CLINICIAN_PROMPT
from app.models.enums import UserMode

class TestAudienceRouting(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
