import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.core.prompts import route_prompt, build_clinician_prompt, build_patient_prompt
from app.models.enums import UserMode

class TestPrompts(unittest.TestCase):
    def test_prompt_routing_patient_mode(self):
        prompt = route_prompt(UserMode.PATIENT, "headache symptoms", "Tension headache context")
        self.assertIsNotNone(prompt)
        prompt_str = str(prompt)
        self.assertTrue("PATIENT" in prompt_str or "empathetic" in prompt_str.lower() or "6th-grade" in prompt_str)

    def test_prompt_routing_clinician_mode(self):
        prompt = route_prompt(UserMode.PROFESSIONAL, "hypertension protocol", "Clinical guideline context")
        self.assertIsNotNone(prompt)
        prompt_str = str(prompt).lower()
        self.assertTrue("clinician" in prompt_str or "clinical" in prompt_str or "physician" in prompt_str)

if __name__ == "__main__":
    unittest.main()
