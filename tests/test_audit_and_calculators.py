"""
Unit tests for AegisMed Clinical Auditability Engine & CURB-65 Pneumonia Calculator.
Verifies:
1. SQLite persistence and cryptographic audit UUID generation.
2. Filtering by audience and emergency triage flag.
3. Summary metrics aggregation (SaMD / HIPAA compliance posture).
4. CURB-65 community-acquired pneumonia 30-day mortality risk stratification.
"""

import sys
import os
import unittest
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.core.audit_logger import ClinicalAuditLogger
from app.services.tools.clinical_calculator import calculate_curb65


import tempfile

class TestAuditAndCalculators(unittest.TestCase):
    def setUp(self):
        # Use an isolated temporary directory for test SQLite DB
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_db_path = Path(self.temp_dir.name) / "test_audit.db"
        self.logger = ClinicalAuditLogger(db_path=self.test_db_path)

    def tearDown(self):
        try:
            self.temp_dir.cleanup()
        except Exception:
            pass

    def test_log_and_query_clinical_event(self):
        """Test recording an audit event and retrieving it by session ID."""
        audit_id = self.logger.log_clinical_event(
            query="chest pain",
            effective_query="chest pain",
            audience="patient",
            session_id="SESS-TEST-001",
            is_emergency=True,
            triage_headline="ACUTE CARDIAC WARNING",
            reading_level_grade=6.0,
            reading_level_label="Grade 6.0 - Everyday English",
            hallucination_risk_pct=3.5,
            grounding_score=0.97,
            latency_ms=250
        )
        self.assertIsNotNone(audit_id)
        self.assertTrue(len(audit_id) > 10)

        # Query back
        logs = self.logger.query_audit_trail(session_id="SESS-TEST-001")
        self.assertEqual(len(logs), 1)
        record = logs[0]
        self.assertEqual(record["audit_id"], audit_id)
        self.assertEqual(record["audience"], "patient")
        self.assertTrue(record["is_emergency"])
        self.assertEqual(record["triage_headline"], "ACUTE CARDIAC WARNING")
        self.assertEqual(record["reading_level_grade"], 6.0)
        self.assertEqual(record["grounding_score"], 0.97)

    def test_audit_metrics_aggregation(self):
        """Test calculation of compliance summary metrics."""
        self.logger.log_clinical_event(
            query="hypertension",
            effective_query="hypertension",
            audience="patient",
            reading_level_grade=5.8,
            grounding_score=0.96
        )
        self.logger.log_clinical_event(
            query="heart attack",
            effective_query="heart attack",
            audience="patient",
            is_emergency=True,
            reading_level_grade=6.2,
            grounding_score=0.98
        )
        self.logger.log_clinical_event(
            query="HFrEF GDMT protocol",
            effective_query="HFrEF GDMT protocol",
            audience="doctor",
            grounding_score=0.99
        )

        metrics = self.logger.get_audit_summary_metrics()
        self.assertEqual(metrics["total_clinical_inquiries"], 3)
        self.assertEqual(metrics["emergency_interceptions"], 1)
        self.assertEqual(metrics["patient_inquiries"], 2)
        self.assertEqual(metrics["doctor_inquiries"], 1)
        self.assertEqual(metrics["audit_integrity_status"], "SECURE_IMMUTABLE")

    def test_curb65_calculator_low_risk(self):
        """Test CURB-65 score 0 (low risk, outpatient candidate)."""
        res = calculate_curb65(
            confusion=False,
            bun_over_19=False,
            rr_over_30=False,
            sbp_under_90_or_dbp_under_60=False,
            age_over_65=False
        )
        self.assertEqual(res["score"], 0)
        self.assertIn("Low Risk", res["risk_level"])
        self.assertIn("Outpatient", res["clinical_action"])

    def test_curb65_calculator_intermediate_risk(self):
        """Test CURB-65 score 2 (intermediate risk, age >= 65 and tachypnea)."""
        res = calculate_curb65(
            confusion=False,
            bun_over_19=False,
            rr_over_30=True,
            sbp_under_90_or_dbp_under_60=False,
            age_over_65=True
        )
        self.assertEqual(res["score"], 2)
        self.assertIn("Intermediate Risk", res["risk_level"])
        self.assertEqual(len(res["criteria_present"]), 2)

    def test_curb65_calculator_severe_risk(self):
        """Test CURB-65 score 4 (severe pneumonia, ICU consideration)."""
        res = calculate_curb65(
            confusion=True,
            bun_over_19=True,
            rr_over_30=True,
            sbp_under_90_or_dbp_under_60=True,
            age_over_65=False
        )
        self.assertEqual(res["score"], 4)
        self.assertIn("Severe Pneumonia", res["risk_level"])
        self.assertIn("Intensive Care Unit (ICU)", res["clinical_action"])


if __name__ == "__main__":
    unittest.main()
