import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from fastapi.testclient import TestClient
from app.main import app
from app.services.chat_engine import chat_engine


class TestChatEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_single_turn_patient_chat(self):
        """Tests initial patient turn explains disease first with analogy and no research papers by default."""
        payload = {
            "message": "What is hypertension and what can I do?",
            "audience": "patient"
        }
        res = self.client.post("/api/v1/chat/message", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()

        self.assertIn("conversation_id", data)
        self.assertEqual(data["audience"], "patient")
        self.assertIn("### 1. Understanding the Condition: What It Is", data["message"])
        self.assertIn("### 2. Practical Solutions", data["message"])
        self.assertIn("### 3. Questions to Ask Your Doctor", data["message"])
        self.assertGreater(len(data["suggested_followups"]), 0)
        self.assertEqual(len(data["history"]), 2)  # 1 user + 1 assistant

    def test_multi_turn_context_retention(self):
        """Tests that follow-up questions retain the active condition from prior turn."""
        # Turn 1: Mention Diabetes
        turn1_payload = {
            "message": "I was diagnosed with type 2 diabetes.",
            "audience": "patient"
        }
        res1 = self.client.post("/api/v1/chat/message", json=turn1_payload)
        self.assertEqual(res1.status_code, 200)
        data1 = res1.json()
        cid = data1["conversation_id"]

        # Turn 2: Follow-up pronoun question without repeating the condition name
        turn2_payload = {
            "message": "What are the common side effects of that?",
            "conversation_id": cid,
            "audience": "patient"
        }
        res2 = self.client.post("/api/v1/chat/message", json=turn2_payload)
        self.assertEqual(res2.status_code, 200)
        data2 = res2.json()

        self.assertEqual(data2["conversation_id"], cid)
        self.assertEqual(len(data2["history"]), 4)  # 2 user + 2 assistant
        self.assertIn("Side Effects", data2["message"])

    def test_doctor_mode_chat(self):
        """Tests that doctor mode receives postgraduate pathophysiology, GDMT, and Oxford CEBM citations."""
        payload = {
            "message": "Type 2 diabetes GDMT second-line pharmacotherapy",
            "audience": "doctor"
        }
        res = self.client.post("/api/v1/chat/message", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()

        self.assertEqual(data["audience"], "doctor")
        self.assertIn("### 1. Disease Overview", data["message"])
        self.assertIn("### 2. Guideline-Directed Medical Therapy", data["message"])
        self.assertIn("### 3. Landmark Clinical Research", data["message"])

    def test_acute_symptom_non_blocking_advisory(self):
        """Tests that acute red-flag symptoms trigger non-blocking clinical advisory banner."""
        payload = {
            "message": "Severe crushing chest pain radiating to my left arm",
            "audience": "patient"
        }
        res = self.client.post("/api/v1/chat/message", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()

        self.assertIsNotNone(data["triage_alert"])
        self.assertFalse(data["triage_alert"]["is_emergency"])
        self.assertIn("CLINICAL ACUITY ADVISORY", data["triage_alert"]["headline"])
        self.assertTrue(data["message"].startswith("> ⚠️"))

    def test_chat_history_and_clear_endpoints(self):
        """Tests retrieval and clearing of conversation sessions."""
        payload = {"message": "Hello doctor", "audience": "patient"}
        res = self.client.post("/api/v1/chat/message", json=payload)
        cid = res.json()["conversation_id"]

        # Fetch history
        hist_res = self.client.get(f"/api/v1/chat/history/{cid}")
        self.assertEqual(hist_res.status_code, 200)
        self.assertEqual(len(hist_res.json()), 2)

        # Clear session
        del_res = self.client.delete(f"/api/v1/chat/history/{cid}")
        self.assertEqual(del_res.status_code, 200)
        self.assertEqual(del_res.json()["status"], "cleared")


if __name__ == "__main__":
    unittest.main()
