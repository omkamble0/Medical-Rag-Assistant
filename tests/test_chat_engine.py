import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.models.chat_schemas import ChatRequest
from app.services.chat_engine import chat_engine


class TestChatEngine(unittest.TestCase):

    def test_single_turn_patient_chat(self):
        """Tests initial patient turn explains disease first with analogy and no research papers by default."""
        req = ChatRequest(
            message="What is hypertension and what can I do?",
            audience="patient"
        )
        res = chat_engine.process_message(req)
        data = res.model_dump()

        self.assertIsNotNone(data["conversation_id"])
        self.assertEqual(data["audience"], "patient")
        self.assertIn("### 1. Understanding the Condition: What It Is", data["message"])
        self.assertIn("### 2. Practical Solutions", data["message"])
        self.assertIn("### 3. Questions to Ask Your Doctor", data["message"])
        self.assertGreater(len(data["suggested_followups"]), 0)
        self.assertEqual(len(data["history"]), 2)  # 1 user + 1 assistant

    def test_multi_turn_context_retention(self):
        """Tests that follow-up questions retain the active condition from prior turn."""
        # Turn 1: Mention Diabetes
        req1 = ChatRequest(
            message="I was diagnosed with type 2 diabetes.",
            audience="patient"
        )
        res1 = chat_engine.process_message(req1)
        cid = res1.conversation_id

        # Turn 2: Follow-up pronoun question without repeating the condition name
        req2 = ChatRequest(
            message="What are the common side effects of that?",
            conversation_id=cid,
            audience="patient"
        )
        res2 = chat_engine.process_message(req2)
        data2 = res2.model_dump()

        self.assertEqual(data2["conversation_id"], cid)
        self.assertEqual(len(data2["history"]), 4)  # 2 user + 2 assistant
        self.assertIn("Side Effects", data2["message"])

    def test_doctor_mode_chat(self):
        """Tests that doctor mode receives postgraduate pathophysiology, GDMT, and Oxford CEBM citations."""
        req = ChatRequest(
            message="Type 2 diabetes GDMT second-line pharmacotherapy",
            audience="doctor"
        )
        res = chat_engine.process_message(req)
        data = res.model_dump()

        self.assertEqual(data["audience"], "doctor")
        self.assertIn("### 1. Disease Overview", data["message"])
        self.assertIn("### 2. Guideline-Directed Medical Therapy", data["message"])
        self.assertIn("### 3. Landmark Clinical Research", data["message"])

    def test_acute_symptom_non_blocking_advisory(self):
        """Tests that acute red-flag symptoms trigger non-blocking clinical advisory banner."""
        req = ChatRequest(
            message="Severe crushing chest pain radiating to my left arm",
            audience="patient"
        )
        res = chat_engine.process_message(req)
        data = res.model_dump()

        self.assertIsNotNone(data["triage_alert"])
        self.assertFalse(data["triage_alert"]["is_emergency"])
        self.assertIn("CLINICAL ACUITY ADVISORY", data["triage_alert"]["headline"])
        self.assertTrue(data["message"].startswith("> ⚠️"))

    def test_chat_history_and_clear_endpoints(self):
        """Tests retrieval and clearing of conversation sessions."""
        req = ChatRequest(message="Hello doctor", audience="patient")
        res = chat_engine.process_message(req)
        cid = res.conversation_id

        # Fetch history
        history = chat_engine.get_session_history(cid)
        self.assertEqual(len(history), 2)

        # Clear session
        cleared = chat_engine.clear_session(cid)
        self.assertTrue(cleared)
        self.assertEqual(len(chat_engine.get_session_history(cid)), 0)


if __name__ == "__main__":
    unittest.main()
