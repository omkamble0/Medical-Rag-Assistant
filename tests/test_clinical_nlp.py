import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "api")))

from app.services.clinical_nlp import (
    clinical_nlp,
    ClinicalIntent,
    AcuityLevel,
    extract_negated_and_asserted_clauses,
    classify_clinical_intents
)


class TestClinicalNLP(unittest.TestCase):
    def test_negex_assertion_vs_negation(self):
        """Verifies clinical NegEx algorithm accurately isolates negated findings."""
        query = "Patient has severe palpitations and dyspnea, but denies chest pain and no nausea"
        analysis = clinical_nlp.process(query)

        self.assertIn("chest", analysis.negated_symptoms)
        self.assertIn("pain", analysis.negated_symptoms)
        self.assertIn("nausea", analysis.negated_symptoms)
        self.assertIn("palpitations", analysis.asserted_symptoms)
        self.assertIn("dyspnea", analysis.asserted_symptoms)

    def test_acronym_disambiguation(self):
        """Verifies clinical acronym dictionary accurately expands medical abbreviations."""
        query = "Protocol for STEMI and DKA management in ED"
        expanded_text, acronyms = clinical_nlp.expand_acronyms(query)

        self.assertIn("STEMI", acronyms)
        self.assertIn("ST-Elevation Myocardial Infarction", acronyms["STEMI"])
        self.assertIn("DKA", acronyms)
        self.assertIn("Diabetic Ketoacidosis", acronyms["DKA"])
        self.assertIn("ED", acronyms)

    def test_greek_latin_morphology(self):
        """Verifies Greek and Latin root stemmer identifies organ systems and pathological suffixes."""
        query = "Evaluation of carditis, nephropathy, and hepatomegaly"
        roots = clinical_nlp.analyze_morphology(query)

        detected_words = [r["detected_in"] for r in roots]
        self.assertIn("carditis", detected_words)
        self.assertIn("nephropathy", detected_words)
        self.assertIn("hepatomegaly", detected_words)

        roots_dict = {r["root"]: r for r in roots}
        self.assertIn("cardi", roots_dict)
        self.assertEqual("CARDIOVASCULAR", roots_dict["cardi"]["organ_system_or_type"])
        self.assertIn("itis", roots_dict)
        self.assertEqual("pathology", roots_dict["itis"]["organ_system_or_type"])
        self.assertIn("nephro", roots_dict)
        self.assertEqual("NEPHROLOGY", roots_dict["nephro"]["organ_system_or_type"])

    def test_clinical_intent_and_acuity_classification(self):
        """Verifies multi-intent classification and emergency acuity grading."""
        # Emergency triage query
        emergency_q = "Sudden crushing chest pain radiating to left jaw with diaphoresis"
        intents, primary, acuity = classify_clinical_intents(emergency_q)
        self.assertEqual(acuity, AcuityLevel.EMERGENCY_LIFE_THREATENING)
        self.assertIn(ClinicalIntent.EMERGENCY_TRIAGE, intents)

        # GDMT query
        treatment_q = "First-line GDMT medication regimen and titration protocols for HFrEF"
        intents2, primary2, acuity2 = classify_clinical_intents(treatment_q)
        self.assertEqual(primary2, ClinicalIntent.TREATMENT_GDMT)

        # Workup query
        workup_q = "Diagnostic workup, criteria, and lab differential for suspected lupus"
        intents3, primary3, acuity3 = classify_clinical_intents(workup_q)
        self.assertEqual(primary3, ClinicalIntent.DIAGNOSTIC_WORKUP)

    def test_metrics_and_pharmacology_extraction(self):
        """Verifies extraction of dosages, blood pressure, labs, and vitals."""
        query = "Patient taking Metformin 1000mg BID and Lisinopril 20mg daily with BP 155/95 mmHg and HbA1c 8.2%"
        meds, metrics = clinical_nlp.extract_metrics_and_drugs(query)

        med_names = [m["drug"].lower() for m in meds]
        self.assertTrue(any("metformin" in m for m in med_names))
        self.assertTrue(any("lisinopril" in m for m in med_names))

        self.assertIn("blood_pressure", metrics)
        self.assertEqual(metrics["blood_pressure"], "155/95 mmHg")
        self.assertIn("hba1c", metrics)
        self.assertEqual(metrics["hba1c"], "8.2%")

    def test_dynamic_contextual_jargon_extraction(self):
        """Verifies dynamic contextual clinical jargon engine detects specialized terms and definitions."""
        from app.services.jargon_engine import extract_contextual_jargon

        text = "Patient with stage 3 CKD has eGFR 48 mL/min and microalbuminuria. Initiating SGLT2 inhibitors and monitoring troponin."
        jargon = extract_contextual_jargon(text, max_items=5)

        terms = [j.term for j in jargon]
        self.assertTrue(any("eGFR" in t for t in terms))
        self.assertTrue(any("Microalbuminuria" in t for t in terms))
        self.assertTrue(any("SGLT2" in t for t in terms))
        self.assertTrue(any("Troponin" in t for t in terms))

        # Check plain-English definitions
        egfr_item = next(j for j in jargon if "eGFR" in j.term)
        self.assertIn("kidneys", egfr_item.plain_english.lower())


if __name__ == "__main__":
    unittest.main()

