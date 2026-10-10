import sys
import os
import unittest
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.main import app
from fastapi.testclient import TestClient
from app.services.guideline_client import load_guideline_sources, map_guidelines_to_domains
from app.services.pubmed_client import search_pubmed, normalize_pubmed_result

class TestResearchRecommendations(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_guideline_client_loading(self):
        """Test guideline loader and domain mapping."""
        guidelines = load_guideline_sources()
        self.assertGreater(len(guidelines), 0)
        
        domain_map = map_guidelines_to_domains()
        self.assertIn("hypertension", domain_map)
        self.assertIn("diabetes", domain_map)
        self.assertIn("asthma", domain_map)

    def test_pubmed_client_search(self):
        """Test PubMed search and fallback handling."""
        results = asyncio.run(search_pubmed("hypertension", max_results=3))
        self.assertGreater(len(results), 0)
        first = results[0]
        self.assertIn("title", first)
        self.assertIn("journal", first)
        self.assertIn("snippet", first)
        
        norm = normalize_pubmed_result(first)
        self.assertEqual(norm["title"], first["title"])

    def test_patient_research_recommendations_endpoint(self):
        """Test POST /api/v1/research-recommendations for patient audience."""
        res = self.client.post(
            "/api/v1/research-recommendations",
            json={"condition": "hypertension", "audience": "patient", "max_results": 4}
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["audience"], "patient")
        self.assertIn("Grade 6.0", data["reading_level"])
        self.assertIn("plain_language_findings", data)
        self.assertIn("questions_for_doctor", data)
        self.assertIn("reputable_resources", data)
        self.assertIn("disclaimer", data)
        self.assertGreater(len(data["sources"]), 0)

    def test_doctor_research_recommendations_endpoint(self):
        """Test POST /api/v1/research-recommendations for doctor / clinician audience."""
        res = self.client.post(
            "/api/v1/research-recommendations",
            json={"condition": "Type 2 Diabetes", "audience": "clinician", "max_results": 4}
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["status"], "ok")
        # Should be normalized from 'clinician' to 'doctor'
        self.assertEqual(data["audience"], "doctor")
        self.assertIn("Postgraduate Clinical Level", data["reading_level"])
        self.assertIn("key_trials_and_rcts", data)
        self.assertIn("guideline_consensus", data)
        self.assertIn("contraindications_and_safety", data)
        self.assertIn("disclaimer", data)
        self.assertGreater(len(data["sources"]), 0)

if __name__ == "__main__":
    unittest.main()
