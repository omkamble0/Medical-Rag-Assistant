import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from fastapi.testclient import TestClient
from app.main import app
from app.services.encyclopedia_engine import encyclopedia_engine


class TestEncyclopediaEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_list_topic_summaries(self):
        """Verifies topic summary listing for 550 conditions."""
        topics = encyclopedia_engine.get_topic_summaries(limit=20)
        self.assertGreaterEqual(len(topics), 10)
        top = topics[0]
        self.assertIsNotNone(top.name)
        self.assertIsNotNone(top.icd10_code)
        self.assertIsNotNone(top.specialty)
        self.assertGreaterEqual(len(top.hallmark_symptoms), 1)

    def test_get_patient_wiki_article(self):
        """Verifies 10-section Patient Wiki generation with physical analogies and myths vs facts."""
        article = encyclopedia_engine.get_article("DOC-CARD-001", mode="patient")
        self.assertIsNotNone(article)
        assert article is not None
        self.assertEqual(article.mode, "patient")
        self.assertEqual(len(article.sections), 10)
        self.assertIn("Hypertension", article.title)

        section_titles = [s.title for s in article.sections]
        self.assertTrue(any("At a Glance" in t for t in section_titles))
        self.assertTrue(any("Analogy" in t for t in section_titles))
        self.assertTrue(any("Myths" in t for t in section_titles))
        self.assertTrue(any("Red Flags" in t for t in section_titles))
        self.assertTrue(any("Questions to Ask" in t for t in section_titles))

        # Check anti-hallucination grounding score
        self.assertGreaterEqual(article.grounding_score, 0.95)
        self.assertGreaterEqual(len(article.landmark_citations), 1)
        self.assertGreaterEqual(len(article.jargon_glossary), 1)

    def test_get_clinician_compendium_article(self):
        """Verifies Clinician Compendium generation with ICD-10, GDMT titration, and trial citations."""
        article = encyclopedia_engine.get_article("DOC-CARD-001", mode="clinician")
        self.assertIsNotNone(article)
        assert article is not None
        self.assertEqual(article.mode, "clinician")
        self.assertGreaterEqual(len(article.sections), 8)

        section_titles = [s.title for s in article.sections]
        self.assertTrue(any("Nosology" in t for t in section_titles))
        self.assertTrue(any("Pathophysiology" in t for t in section_titles))
        self.assertTrue(any("GDMT" in t for t in section_titles))
        self.assertTrue(any("Landmark" in t for t in section_titles))

    def test_fuzzy_name_lookup(self):
        """Verifies finding an article by condition name substring."""
        article = encyclopedia_engine.get_article("Heart Failure with Reduced Ejection Fraction", mode="patient")
        self.assertIsNotNone(article)
        assert article is not None
        self.assertIn("Heart Failure", article.title)

    def test_api_encyclopedia_endpoints(self):
        """Verifies encyclopedia queries for topics, articles, and specialties."""
        # 1. Topics
        topics = encyclopedia_engine.get_topic_summaries(limit=5)
        self.assertEqual(len(topics), 5)

        # 2. Article
        art = encyclopedia_engine.get_article("DOC-CARD-001", mode="patient")
        self.assertIsNotNone(art)
        assert art is not None
        self.assertEqual(art.id, "DOC-CARD-001")
        self.assertEqual(art.mode, "patient")
        self.assertEqual(len(art.sections), 10)

        # 3. Specialties
        from app.services.medical_db import medical_db
        specs = sorted(list(medical_db.get_stats().specialties_distribution.keys()))
        self.assertIn("Cardiovascular", specs)

        # 4. Random topic selection
        import random
        chosen = random.choice(topics)
        rand_art = encyclopedia_engine.get_article(chosen.id, mode="patient")
        self.assertIsNotNone(rand_art)


if __name__ == "__main__":
    unittest.main()
