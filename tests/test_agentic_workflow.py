import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.services.agent_workflow import execute_agentic_rag_workflow
from app.services.tools.clinical_calculator import (
    calculate_egfr, calculate_bmi, calculate_cha2ds2_vasc, calculate_wells_pe
)
from app.services.tools.drug_interaction import check_drug_interactions, screen_single_drug_safety
from app.services.crag.query_rewriter import rewrite_clinical_query
from app.services.crag.retrieval_grader import grade_retrieval_relevance
from app.services.crag.reranker import rerank_evidence_documents
from app.services.crag.hallucination_grader import audit_hallucinations_and_grounding


class TestAgenticWorkflow(unittest.TestCase):

    def test_clinical_calculators(self):
        # 1. eGFR
        egfr_res = calculate_egfr(creatinine=1.4, age=65, sex="male")
        self.assertIn("egfr", egfr_res)
        self.assertTrue(egfr_res["egfr"] > 0)
        self.assertIn("stage", egfr_res)
        self.assertTrue(len(egfr_res["pharmacotherapy_alerts"]) > 0)

        # 2. BMI
        bmi_res = calculate_bmi(weight_kg=95.0, height_cm=175.0)
        self.assertEqual(bmi_res["bmi"], 31.0)
        self.assertEqual(bmi_res["category"], "Class I Obesity")

        # 3. CHA2DS2-VASc
        afib_res = calculate_cha2ds2_vasc(chf=True, htn=True, age=70, sex="male")
        self.assertEqual(afib_res["score"], 3)
        self.assertIn("Oral Anticoagulation", afib_res["recommendation"])

        # 4. Wells PE
        wells_res = calculate_wells_pe(dvt_signs=True, hr_over_100=True)
        self.assertEqual(wells_res["score"], 4.5)
        self.assertIn("Moderate Probability", wells_res["probability_tier"])

    def test_drug_interactions(self):
        # Check Paxlovid + Simvastatin
        ddi = check_drug_interactions(["Paxlovid", "Simvastatin"])
        self.assertEqual(ddi["interactions_found"], 1)
        self.assertEqual(ddi["ddi_alerts"][0]["severity"], "CONTRAINDICATED")
        self.assertIn("rhabdomyolysis", ddi["ddi_alerts"][0]["clinical_risk"].lower())

        # Single safety profile
        safety = screen_single_drug_safety("Semaglutide")
        self.assertTrue(safety["has_profile"])
        self.assertIn("Thyroid", safety["black_box_warning"])

    def test_query_rewriter_mesh(self):
        decomp = rewrite_clinical_query("My sugar is high and doctor prescribed semaglutide")
        self.assertIn("Type 2 Diabetes", decomp.canonical_condition)
        self.assertIn("Semaglutide", decomp.identified_drugs)
        self.assertEqual(len(decomp.sub_queries), 3)

    def test_crag_retrieval_and_reranking(self):
        sample_docs = [
            {"title": "Expert Opinion on Hypertension", "evidence_level": "Level 5", "snippet": "Consider lifestyle changes."},
            {"title": "Meta-Analysis on First-Line Antihypertensives (NEJM)", "evidence_level": "Level 1", "snippet": "Thiazides and ACE inhibitors reduce MACE."}
        ]
        # Re-ranking should prioritize Level 1
        reranked = rerank_evidence_documents("hypertension first line", sample_docs, top_k=2)
        self.assertEqual(len(reranked), 2)
        self.assertIn("Level 1", reranked[0]["evidence_level"])

        # Grading
        grade = grade_retrieval_relevance("hypertension", reranked)
        self.assertTrue(grade.is_sufficient)
        self.assertEqual(grade.grade_decision, "PASSED_CORRECTIVE_FILTER")

    def test_self_rag_hallucination_grader(self):
        sample_answer = "ACE inhibitors lower blood pressure [1]. Lifestyle modifications are also recommended [1]."
        sources = [
            {"citation_index": 1, "title": "AHA Guidelines", "content": "ACE inhibitors reduce blood pressure."}
        ]
        audit = audit_hallucinations_and_grounding(sample_answer, sources)
        self.assertTrue(audit.is_grounded)
        self.assertTrue(audit.grounding_score >= 0.70)
        self.assertEqual(len(audit.unsupported_claims), 0)

    def test_full_langgraph_pipeline_patient_and_doctor(self):
        # Patient mode execution
        res_patient = execute_agentic_rag_workflow("What are the main symptoms of migraine?", audience="patient")
        self.assertEqual(res_patient["status"], "COMPLETED")
        self.assertIn("answer", res_patient)
        self.assertEqual(len(res_patient["execution_trace"]), 7)

        # Doctor mode execution
        res_doctor = execute_agentic_rag_workflow("What is the titration and DDI profile of Semaglutide?", audience="doctor")
        self.assertEqual(res_doctor["status"], "COMPLETED")
        self.assertIn("answer", res_doctor)
        self.assertEqual(res_doctor["audience"], "doctor")

    def test_clinical_acuity_advisory_non_blocking(self):
        res_emerg = execute_agentic_rag_workflow("I have crushing chest pain, cold sweats, and elephant on my chest", audience="patient")
        # Non-blocking redesign: completes full pipeline while flagging clinical acuity advisory
        self.assertEqual(res_emerg["status"], "COMPLETED")
        self.assertIsNotNone(res_emerg["triage_alert"])
        self.assertIn("CLINICAL ACUITY ADVISORY", res_emerg["answer"])
        self.assertIn("### 1. Understanding the Condition", res_emerg["answer"])
        self.assertEqual(len(res_emerg["execution_trace"]), 7)


if __name__ == "__main__":
    unittest.main()
