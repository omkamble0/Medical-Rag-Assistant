"""
AegisMed Production Layered Architecture & Safety Guardrail Test Suite
Validates:
1. Dependency Injection (DIContainer)
2. Hybrid Retrieval & Medical Content Chunking
3. BM25 Sparse Index & CEBM Evidence Reranking
4. RAG Evaluation (Groundedness, Relevance, Citation Precision, Hallucination Risk)
5. Clinical Safety Guardrails (Red Flags, Pregnancy/Teratogens, NTI Drugs, Beers, Reye's Syndrome, eGFR)
6. Conservative Triage & Low-Confidence Clarifying Questions
7. HIPAA Safe Harbor PII Scrubbing & Security Headers
8. Observability & Prometheus Metrics Exporter
9. Medical Knowledge Provenance & Versioning Service
10. End-to-End Clinical Orchestrator Pipeline
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.config import Settings
from app.di.container import DIContainer
from app.interfaces.retriever import RetrievedChunk
from app.retrieval.bm25 import BM25Index
from app.retrieval.chunker import MedicalContentChunker
from app.retrieval.reranker import ClinicalEvidenceReranker
from app.retrieval.evaluator import ClinicalRagEvaluator
from app.retrieval.hybrid_retriever import HybridClinicalRetriever
from app.domain.services.safety_service import ClinicalSafetyService
from app.domain.services.triage_service import ClinicalTriageService
from app.domain.services.knowledge_service import MedicalKnowledgeService
from app.domain.services.escalation_service import ClinicalEscalationService
from app.domain.services.clinical_orchestrator import ClinicalOrchestrator
from app.domain.models.schemas import ClinicalQueryRequest, ClinicalRiskLevel, ConfidenceBand
from app.core.security import scrub_pii
from app.core.metrics import MetricsRegistry
from app.llm.mock_provider import MockClinicalLLMProvider


class TestClinicalProductionLayers(unittest.TestCase):

    def setUp(self):
        self.settings = Settings(OFFLINE_MODE=True, IS_TESTING=True)
        self.container = DIContainer(self.settings)

    # =========================================================================
    # 1. Dependency Injection Container
    # =========================================================================
    def test_dependency_injection_container(self):
        """Test DI container wires components with proper interfaces."""
        retriever = self.container.get_retriever()
        self.assertIsNotNone(retriever)
        
        llm = self.container.get_llm_gateway()
        self.assertIsNotNone(llm)
        
        safety = self.container.get_safety_service()
        self.assertIsInstance(safety, ClinicalSafetyService)
        
        orchestrator = self.container.get_orchestrator()
        self.assertIsInstance(orchestrator, ClinicalOrchestrator)

    # =========================================================================
    # 2. Medical Content Chunking
    # =========================================================================
    def test_medical_content_chunker(self):
        """Test clinical chunking by section and evidence headers."""
        chunker = MedicalContentChunker(chunk_size=120, chunk_overlap=20)
        clinical_text = (
            "CONTRAINDICATIONS: Absolute contraindication in pregnancy due to fetotoxicity. "
            "Do not administer to patients with bilateral renal artery stenosis. "
            "ADVERSE REACTIONS: Dry persistent cough occurs in 10-20% of treated patients. "
            "Hyperkalemia and angioedema have been reported. "
            "DOSAGE AND ADMINISTRATION: Initial starting dose is 5 mg PO daily for hypertension, "
            "titrated up to 20-40 mg daily based on blood pressure response."
        )
        chunks = chunker.chunk_text(
            text=clinical_text,
            doc_id="DOC-ACEI-01",
            title="Lisinopril Prescribing Information",
            evidence_level="LEVEL_1",
            domain="CARDIOVASCULAR"
        )
        self.assertGreaterEqual(len(chunks), 2)
        has_contraindication = any(c.is_contraindication for c in chunks)
        self.assertTrue(has_contraindication)
        self.assertEqual(chunks[0].evidence_level, "LEVEL_1")

    # =========================================================================
    # 3. BM25 Sparse Index & Evidence Reranking
    # =========================================================================
    def test_bm25_and_reranker(self):
        """Test BM25 search and CEBM ranker with explicit ignored reasons."""
        corpus = [
            RetrievedChunk(
                chunk_id="C1",
                doc_id="D1",
                text="Semaglutide GLP-1 receptor agonist reduces major cardiovascular events in diabetes.",
                title="STEP Trial",
                evidence_level="LEVEL_1",
                domain="ENDOCRINOLOGY_METABOLISM",
                relevance_score=0.9
            ),
            RetrievedChunk(
                chunk_id="C2",
                doc_id="D2",
                text="Asthma inhalation therapy with ICS-formoterol reduces exacerbations.",
                title="GINA Guideline",
                evidence_level="LEVEL_1",
                domain="PULMONOLOGY",
                relevance_score=0.8
            ),
            RetrievedChunk(
                chunk_id="C3",
                doc_id="D3",
                text="Case report of rare drug eruption from topical cream in a single patient.",
                title="Case Report 1999",
                evidence_level="LEVEL_5",
                domain="DERMATOLOGY",
                relevance_score=0.3
            )
        ]
        bm25 = BM25Index()
        bm25.fit(corpus)
        bm25_matches = bm25.search("semaglutide diabetes cardiovascular", top_k=2)
        self.assertGreater(len(bm25_matches), 0)
        self.assertEqual(bm25_matches[0][0].chunk_id, "C1")

        reranker = ClinicalEvidenceReranker(min_relevance_score=0.35)
        reranked, ignored = reranker.rerank("semaglutide diabetes", corpus, top_k=2)
        self.assertEqual(reranked[0].chunk_id, "C1")
        # Low scoring Level 5 document should be in ignored list
        self.assertGreater(len(ignored), 0)
        ignored_ids = [ig.chunk_id for ig in ignored]
        self.assertIn("C3", ignored_ids)
        self.assertTrue(any("LEVEL" in ig.reason.upper() and "5" in ig.reason for ig in ignored))

    # =========================================================================
    # 4. RAG Quality Evaluation
    # =========================================================================
    def test_rag_evaluator(self):
        """Test groundedness, citation precision, and hallucination metrics."""
        evaluator = ClinicalRagEvaluator()
        grounded_context = (
            "SGLT2 inhibitors like dapagliflozin reduce heart failure hospitalizations by 26% "
            "in patients with HFrEF (DAPA-HF trial). They also slow decline in eGFR."
        )
        grounded_answer = (
            "Dapagliflozin reduces heart failure hospitalizations by 26% and slows eGFR decline "
            "according to the DAPA-HF trial [1]."
        )
        report = evaluator.evaluate(
            query="What are the benefits of dapagliflozin?",
            response=grounded_answer,
            retrieved_chunks=[RetrievedChunk(
                chunk_id="CH-DAPA-1",
                doc_id="DOC-DAPA",
                text=grounded_context,
                title="DAPA-HF",
                evidence_level="LEVEL_1",
                domain="CARDIOVASCULAR"
            )],
            citations=[1]
        )
        self.assertGreaterEqual(report.groundedness_score, 0.70)
        self.assertLessEqual(report.hallucination_risk, 0.30)
        self.assertGreaterEqual(report.composite_score, 0.70)

    # =========================================================================
    # 5. Clinical Safety Service: Red Flags & High-Risk Interceptions
    # =========================================================================
    def test_safety_tier1_red_flags(self):
        """Test emergency red flag detection immediately triggers CRITICAL escalation."""
        safety = ClinicalSafetyService()
        
        # Cardiac emergency
        res = safety.check_emergency_red_flags("I have crushing substernal chest pain radiating to my left arm and jaw")
        self.assertTrue(res.is_emergency)
        self.assertEqual(res.risk_level, ClinicalRiskLevel.CRITICAL)
        self.assertIn("EMERGENCY", res.escalation_reason.upper())

        # Anaphylaxis emergency
        res_ana = safety.check_emergency_red_flags("Sudden facial swelling, lip edema, stridor, and severe shortness of breath")
        self.assertTrue(res_ana.is_emergency)
        self.assertEqual(res_ana.risk_level, ClinicalRiskLevel.CRITICAL)

    def test_safety_pregnancy_and_teratogens(self):
        """Test black-box teratogen warnings for pregnancy."""
        safety = ClinicalSafetyService()
        res = safety.check_pregnancy_contraindications(
            query="Can I take lisinopril for high blood pressure?",
            is_pregnant=True
        )
        self.assertFalse(res.is_safe)
        self.assertTrue(any("FETAL" in w.upper() or "TERATOGEN" in w.upper() or "BOXED WARNING" in w.upper() for w in res.warnings))
        self.assertEqual(res.risk_level, ClinicalRiskLevel.HIGH)

    def test_safety_pediatric_aspirin_reye_syndrome(self):
        """Test pediatric aspirin contraindication due to Reye's syndrome risk."""
        safety = ClinicalSafetyService()
        res = safety.check_pediatric_safety(
            query="Can I give aspirin to my 8 year old child with a viral fever?",
            patient_age_years=8
        )
        self.assertFalse(res.is_safe)
        self.assertTrue(any("reye's syndrome" in w.lower() for w in res.warnings))

    def test_safety_geriatric_beers_criteria(self):
        """Test AGS Beers criteria for elderly patients."""
        safety = ClinicalSafetyService()
        res = safety.check_geriatric_safety(
            query="Can a 78 year old take diphenhydramine Benadryl every night for sleep?",
            patient_age_years=78
        )
        self.assertFalse(res.is_safe)
        self.assertTrue(any("Beers criteria" in w for w in res.warnings))

    def test_safety_renal_contraindications(self):
        """Test eGFR cutoffs for nephrotoxic and renally cleared medications."""
        safety = ClinicalSafetyService()
        res = safety.check_renal_safety(
            query="Metformin 1000 mg twice daily",
            egfr_ml_min=24.0
        )
        self.assertFalse(res.is_safe)
        self.assertTrue(any("lactic acidosis" in w for w in res.warnings))

    def test_safety_narrow_therapeutic_index(self):
        """Test NTI high-risk drug surveillance (Warfarin, Lithium, Digoxin)."""
        safety = ClinicalSafetyService()
        res = safety.check_high_risk_medications("I take warfarin and want to know about food interactions")
        self.assertTrue(len(res.identified_nti_drugs) > 0)
        self.assertIn("warfarin", res.identified_nti_drugs)

    # =========================================================================
    # 6. Conservative Triage & Low-Confidence Clarifying Questions
    # =========================================================================
    def test_conservative_triage_low_confidence(self):
        """Test system refuses to fabricate advice when confidence < 0.50 and asks clarifying questions."""
        triage = ClinicalTriageService()
        triage_res = triage.evaluate_confidence(
            retrieval_score=0.35,
            evidence_count=0,
            has_red_flags=False,
            is_ambiguous=True
        )
        self.assertTrue(triage_res.should_refuse_advice)
        self.assertGreater(len(triage_res.clarifying_questions), 0)
        self.assertIn("clarify", triage_res.triage_action.lower())

    # =========================================================================
    # 7. HIPAA Safe Harbor PII Scrubbing
    # =========================================================================
    def test_hipaa_pii_scrubber(self):
        """Test HIPAA Safe Harbor de-identification rules."""
        raw_text = (
            "Patient John Doe, SSN 000-12-3456, MRN #9876543, DOB 04/12/1985, "
            "contact: 555-123-4567, email jdoe@clinic.org, reported mild palpitations."
        )
        res = scrub_pii(raw_text)
        cleaned = res.cleaned_text
        self.assertNotIn("000-12-3456", cleaned)
        self.assertNotIn("9876543", cleaned)
        self.assertNotIn("555-123-4567", cleaned)
        self.assertNotIn("jdoe@clinic.org", cleaned)
        self.assertIn("[REDACTED_SSN]", cleaned)
        self.assertIn("[REDACTED_MRN]", cleaned)
        self.assertIn("[REDACTED_PHONE]", cleaned)
        self.assertIn("[REDACTED_EMAIL]", cleaned)

    # =========================================================================
    # 8. Observability & Prometheus Metrics
    # =========================================================================
    def test_metrics_registry_prometheus_export(self):
        """Test structured Prometheus metrics format and counter tracking."""
        metrics = MetricsRegistry()
        metrics.record_query(duration_ms=120.5, success=True, audience="patient")
        metrics.record_safety_trigger(rule_name="emergency_red_flag")
        metrics.record_retrieval(hits=3, misses=0)

        summary = metrics.get_summary()
        self.assertEqual(summary["total_queries"], 1)
        self.assertEqual(summary["safety_triggers"]["emergency_red_flag"], 1)

        prom_text = metrics.export_prometheus()
        self.assertIn("aegismed_requests_total", prom_text)
        self.assertIn("aegismed_safety_triggers_total", prom_text)
        self.assertIn("aegismed_query_latency_ms", prom_text)

    # =========================================================================
    # 9. Medical Knowledge Service & Provenance
    # =========================================================================
    def test_medical_knowledge_service(self):
        """Test source policy verification, evidence cards, and versioning."""
        ks = MedicalKnowledgeService()
        version_info = ks.get_knowledge_version_info()
        self.assertIn("guidelines_version", version_info)
        self.assertIn("trusted_authorities", version_info)
        
        is_trusted = ks.is_source_trusted("The New England Journal of Medicine (NEJM)")
        self.assertTrue(is_trusted)

        card = ks.create_evidence_card(
            title="SGLT2 Inhibitors in Heart Failure",
            journal="The Lancet",
            year=2023,
            evidence_level="LEVEL_1",
            doi_or_pmid="10.1016/S0140-6736(23)00456-7",
            takeaway="Significant reduction in cardiovascular death."
        )
        self.assertEqual(card.evidence_level, "LEVEL_1")
        self.assertTrue(card.is_peer_reviewed)

    # =========================================================================
    # 10. End-to-End Clinical Orchestrator Execution
    # =========================================================================
    def test_orchestrator_patient_query_workflow(self):
        """Test end-to-end pipeline execution for patient mode query."""
        orchestrator = self.container.get_orchestrator()
        req = ClinicalQueryRequest(
            query="What are the proven first-line treatments for high blood pressure?",
            audience="patient",
            patient_age=55
        )
        response = orchestrator.process_query_sync(req)
        self.assertEqual(response.audience, "patient")
        self.assertIn(response.confidence_band, [ConfidenceBand.MEDIUM, ConfidenceBand.HIGH, "medium", "high"])
        self.assertGreater(len(response.evidence), 0)
        self.assertIsNotNone(response.reading_grade_level)
        self.assertIsNotNone(response.rag_evaluation)
        self.assertGreaterEqual(response.rag_evaluation.groundedness_score, 0.50)

    def test_orchestrator_red_flag_interception(self):
        """Test end-to-end pipeline emergency red flag fast-path interception."""
        orchestrator = self.container.get_orchestrator()
        req = ClinicalQueryRequest(
            query="Crushing severe chest pain radiating to left jaw with cold diaphoresis",
            audience="patient"
        )
        response = orchestrator.process_query_sync(req)
        self.assertEqual(response.risk_level, ClinicalRiskLevel.CRITICAL)
        self.assertTrue(response.is_emergency)
        self.assertTrue(response.escalation_required)
        self.assertIn("911", response.diagnosis_summary)


if __name__ == "__main__":
    unittest.main()
