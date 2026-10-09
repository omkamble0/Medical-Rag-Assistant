# medical_query_validator/query_validator.py

import re
from typing import Dict, List, Tuple, Any, Set
from difflib import SequenceMatcher

# Comprehensive Medical Terms Database (SNOMED-CT / MeSH / ICD-11 inspired)
MEDICAL_TERMS_DB = {
    # Symptoms & Conditions
    "headache": {"category": "symptom", "standard": "Headache", "snomed_id": "25064002"},
    "headaches": {"category": "symptom", "standard": "Headache", "snomed_id": "25064002"},
    "migraine": {"category": "condition", "standard": "Migraine", "snomed_id": "37796009"},
    "diabetes": {"category": "condition", "standard": "Diabetes Mellitus", "snomed_id": "73211009"},
    "hypertension": {"category": "condition", "standard": "Hypertension", "snomed_id": "38341003"},
    "hypotension": {"category": "condition", "standard": "Hypotension", "snomed_id": "45007003"},
    "asthma": {"category": "condition", "standard": "Asthma", "snomed_id": "195967001"},
    "dyspnea": {"category": "symptom", "standard": "Dyspnea", "snomed_id": "267036007"},
    "fever": {"category": "symptom", "standard": "Fever", "snomed_id": "386661006"},
    "pyrexia": {"category": "symptom", "standard": "Fever", "snomed_id": "386661006"},
    "nausea": {"category": "symptom", "standard": "Nausea", "snomed_id": "422587007"},
    "vomiting": {"category": "symptom", "standard": "Vomiting", "snomed_id": "422400008"},
    "emesis": {"category": "symptom", "standard": "Vomiting", "snomed_id": "422400008"},
    "diarrhea": {"category": "symptom", "standard": "Diarrhea", "snomed_id": "62315008"},
    "constipation": {"category": "symptom", "standard": "Constipation", "snomed_id": "14760008"},
    "fatigue": {"category": "symptom", "standard": "Fatigue", "snomed_id": "84229001"},
    "cough": {"category": "symptom", "standard": "Cough", "snomed_id": "49727002"},
    "pneumonia": {"category": "condition", "standard": "Pneumonia", "snomed_id": "233604007"},
    "bronchitis": {"category": "condition", "standard": "Bronchitis", "snomed_id": "32398004"},
    "edema": {"category": "symptom", "standard": "Edema", "snomed_id": "267038008"},
    "swelling": {"category": "symptom", "standard": "Edema", "snomed_id": "267038008"},
    "infarction": {"category": "condition", "standard": "Infarction", "snomed_id": "55641003"},
    "tachycardia": {"category": "symptom", "standard": "Tachycardia", "snomed_id": "3424008"},
    "bradycardia": {"category": "symptom", "standard": "Bradycardia", "snomed_id": "48867003"},
    "arrhythmia": {"category": "condition", "standard": "Cardiac Arrhythmia", "snomed_id": "698247007"},
    "angina": {"category": "symptom", "standard": "Angina Pectoris", "snomed_id": "194828000"},
    "syncope": {"category": "symptom", "standard": "Syncope", "snomed_id": "271594007"},
    "fainting": {"category": "symptom", "standard": "Syncope", "snomed_id": "271594007"},
    "dizziness": {"category": "symptom", "standard": "Dizziness", "snomed_id": "404640003"},
    "vertigo": {"category": "symptom", "standard": "Vertigo", "snomed_id": "399153001"},
    "insomnia": {"category": "condition", "standard": "Insomnia", "snomed_id": "193462001"},
    "arthritis": {"category": "condition", "standard": "Arthritis", "snomed_id": "3723001"},
    "osteoarthritis": {"category": "condition", "standard": "Osteoarthritis", "snomed_id": "396275006"},
    "osteoporosis": {"category": "condition", "standard": "Osteoporosis", "snomed_id": "64859006"},
    "anemia": {"category": "condition", "standard": "Anemia", "snomed_id": "271737000"},
    "jaundice": {"category": "symptom", "standard": "Jaundice", "snomed_id": "18165001"},
    "sepsis": {"category": "condition", "standard": "Sepsis", "snomed_id": "91302008"},
    "stroke": {"category": "condition", "standard": "Cerebrovascular Accident", "snomed_id": "230690007"},
    "seizure": {"category": "symptom", "standard": "Seizure", "snomed_id": "91175000"},
    "epilepsy": {"category": "condition", "standard": "Epilepsy", "snomed_id": "84757009"},
    "gastritis": {"category": "condition", "standard": "Gastritis", "snomed_id": "4556007"},
    "appendicitis": {"category": "condition", "standard": "Appendicitis", "snomed_id": "74400008"},
    "diverticulitis": {"category": "condition", "standard": "Diverticulitis", "snomed_id": "426000000"},
    "pancreatitis": {"category": "condition", "standard": "Pancreatitis", "snomed_id": "75694006"},
    "hepatitis": {"category": "condition", "standard": "Hepatitis", "snomed_id": "128241005"},
    "cirrhosis": {"category": "condition", "standard": "Cirrhosis of Liver", "snomed_id": "19943007"},
    "cholesterol": {"category": "biomarker", "standard": "Serum Cholesterol", "snomed_id": "121868005"},
    "hyperlipidemia": {"category": "condition", "standard": "Hyperlipidemia", "snomed_id": "166816003"},
    "pruritus": {"category": "symptom", "standard": "Pruritus (Itching)", "snomed_id": "418290006"},
    "itching": {"category": "symptom", "standard": "Pruritus", "snomed_id": "418290006"},
    "rash": {"category": "symptom", "standard": "Skin Rash", "snomed_id": "271807003"},
    "eczema": {"category": "condition", "standard": "Atopic Dermatitis", "snomed_id": "24079001"},
    "psoriasis": {"category": "condition", "standard": "Plaque Psoriasis", "snomed_id": "9014002"},
    "urticaria": {"category": "symptom", "standard": "Urticaria (Hives)", "snomed_id": "126485001"},
    "hives": {"category": "symptom", "standard": "Urticaria", "snomed_id": "126485001"},
    "anaphylaxis": {"category": "emergency", "standard": "Anaphylaxis", "snomed_id": "39579001"},
    "hypoglycemia": {"category": "condition", "standard": "Hypoglycemia", "snomed_id": "267384006"},
    "hyperglycemia": {"category": "condition", "standard": "Hyperglycemia", "snomed_id": "80394007"},
    "neuropathy": {"category": "condition", "standard": "Peripheral Neuropathy", "snomed_id": "386033004"},
    "hypothyroidism": {"category": "condition", "standard": "Hypothyroidism", "snomed_id": "40930008"},
    "hyperthyroidism": {"category": "condition", "standard": "Hyperthyroidism", "snomed_id": "34486009"},
    "depression": {"category": "condition", "standard": "Major Depressive Disorder", "snomed_id": "35489007"},
    "anxiety": {"category": "condition", "standard": "Generalized Anxiety Disorder", "snomed_id": "21897009"},
    "preeclampsia": {"category": "condition", "standard": "Preeclampsia", "snomed_id": "398254007"},
    "fibromyalgia": {"category": "condition", "standard": "Fibromyalgia", "snomed_id": "203082005"},
    "gout": {"category": "condition", "standard": "Gouty Arthritis", "snomed_id": "90560007"},

    # Medications
    "metformin": {"category": "medication", "standard": "Metformin", "snomed_id": "372567009"},
    "lisinopril": {"category": "medication", "standard": "Lisinopril", "snomed_id": "387449005"},
    "amlodipine": {"category": "medication", "standard": "Amlodipine", "snomed_id": "386864001"},
    "atorvastatin": {"category": "medication", "standard": "Atorvastatin", "snomed_id": "387584000"},
    "simvastatin": {"category": "medication", "standard": "Simvastatin", "snomed_id": "387585004"},
    "ibuprofen": {"category": "medication", "standard": "Ibuprofen", "snomed_id": "387207008"},
    "paracetamol": {"category": "medication", "standard": "Acetaminophen", "snomed_id": "387517004"},
    "acetaminophen": {"category": "medication", "standard": "Acetaminophen", "snomed_id": "387517004"},
    "aspirin": {"category": "medication", "standard": "Aspirin", "snomed_id": "387458008"},
    "amoxicillin": {"category": "medication", "standard": "Amoxicillin", "snomed_id": "372687004"},
    "azithromycin": {"category": "medication", "standard": "Azithromycin", "snomed_id": "387293003"},
    "semaglutide": {"category": "medication", "standard": "Semaglutide", "snomed_id": "763158003"},
    "ozempic": {"category": "medication", "standard": "Semaglutide (Ozempic)", "snomed_id": "763158003"},
    "mounjaro": {"category": "medication", "standard": "Tirzepatide (Mounjaro)", "snomed_id": "1198595007"},
    "tirzepatide": {"category": "medication", "standard": "Tirzepatide", "snomed_id": "1198595007"},
    "paxlovid": {"category": "medication", "standard": "Nirmatrelvir/Ritonavir (Paxlovid)", "snomed_id": "1208940003"},
    "insulin": {"category": "medication", "standard": "Insulin", "snomed_id": "387340001"},
    "albuterol": {"category": "medication", "standard": "Albuterol / Salbutamol", "snomed_id": "372897005"},
    "salbutamol": {"category": "medication", "standard": "Salbutamol", "snomed_id": "372897005"},
    "budesonide": {"category": "medication", "standard": "Budesonide", "snomed_id": "387144002"},
    "prednisone": {"category": "medication", "standard": "Prednisone", "snomed_id": "387274005"},
    "gabapentin": {"category": "medication", "standard": "Gabapentin", "snomed_id": "386845007"},
    "omeprazole": {"category": "medication", "standard": "Omeprazole", "snomed_id": "387083002"},
    "pantoprazole": {"category": "medication", "standard": "Pantoprazole", "snomed_id": "387131008"},
    "doxycycline": {"category": "medication", "standard": "Doxycycline", "snomed_id": "387413000"},
}

# Known common typos & acronym normalizations
MEDICAL_ACRONYMS = {
    "bp": "blood pressure",
    "hbp": "high blood pressure",
    "hr": "heart rate",
    "sob": "shortness of breath",
    "mi": "myocardial infarction",
    "cad": "coronary artery disease",
    "ckd": "chronic kidney disease",
    "chf": "congestive heart failure",
    "hfref": "heart failure with reduced ejection fraction",
    "hfpef": "heart failure with preserved ejection fraction",
    "afib": "atrial fibrillation",
    "a-fib": "atrial fibrillation",
    "copd": "chronic obstructive pulmonary disease",
    "gerd": "gastroesophageal reflux disease",
    "ibs": "irritable bowel syndrome",
    "ibd": "inflammatory bowel disease",
    "uti": "urinary tract infection",
    "dvt": "deep vein thrombosis",
    "pe": "pulmonary embolism",
    "t2d": "type 2 diabetes",
    "t2dm": "type 2 diabetes mellitus",
    "t1d": "type 1 diabetes",
    "pcos": "polycystic ovary syndrome",
    "osa": "obstructive sleep apnea",
    "ra": "rheumatoid arthritis",
    "oa": "osteoarthritis",
    "aki": "acute kidney injury",
    "mdd": "major depressive disorder",
    "gad": "generalized anxiety disorder",
    "ptsd": "post-traumatic stress disorder",
    "adhd": "attention deficit hyperactivity disorder",
    "bph": "benign prostatic hyperplasia",
    "aom": "acute otitis media",
    "cap": "community-acquired pneumonia",
    "cvi": "chronic venous insufficiency",
    "nstemi": "non-ST-elevation myocardial infarction",
    "stemi": "ST-elevation myocardial infarction",
    "gdm": "gestational diabetes mellitus",
    "sle": "systemic lupus erythematosus",
    "prep": "pre-exposure prophylaxis",
    "hcv": "hepatitis C virus",
    "hbv": "hepatitis B virus",
    "hiv": "human immunodeficiency virus",
    "ms": "multiple sclerosis",
    "tb": "tuberculosis",
}

class MedicalQueryValidator:
    """
    3-Layer Medical Query Validation System:
    Layer 1: Typo Detection & Fuzzy Correction (difflib/edit-distance matching against medical lexicon)
    Layer 2: Medical Term Validation (identify validated clinical entities, categories, and SNOMED codes)
    Layer 3: Query Normalization (acronym expansion & syntax standardization)
    """

    def __init__(self):
        self.terms_db = MEDICAL_TERMS_DB
        self.acronyms_db = MEDICAL_ACRONYMS
        self.vocabulary = set(self.terms_db.keys())

    def _similarity(self, word1: str, word2: str) -> float:
        """Calculate string similarity ratio"""
        return SequenceMatcher(None, word1.lower(), word2.lower()).ratio()

    def find_best_medical_match(self, word: str, threshold: float = 0.75) -> Tuple[Optional[str], float]:
        """
        Find closest medical term match in dictionary using fuzzy sequence matching.
        """
        cleaned_word = word.lower().strip(",.!?\"'();:")
        if len(cleaned_word) < 3:
            return None, 0.0

        if cleaned_word in self.vocabulary:
            return cleaned_word, 1.0

        best_term = None
        best_score = 0.0

        for term in self.vocabulary:
            score = self._similarity(cleaned_word, term)
            # Boost score if initial letters match
            if cleaned_word[0] == term[0]:
                score += 0.05
            if score > best_score:
                best_score = score
                best_term = term

        if best_score >= threshold:
            return best_term, min(best_score, 1.0)
        return None, best_score

    def detect_and_correct_typos(self, text: str) -> Tuple[str, List[str], float]:
        """
        Layer 1: Detect typos and replace with closest valid medical term.
        Returns (corrected_text, list_of_corrections, average_confidence).
        """
        words = re.findall(r'\b\w+\b', text)
        corrections = []
        scores = []
        corrected_text = text

        for word in words:
            w_lower = word.lower()
            # Ignore common non-medical short English words
            if w_lower in {"i", "have", "and", "the", "a", "an", "for", "with", "what", "is", "are", "treatment", "how", "to", "cure", "pain", "my", "in", "of", "on", "can", "does", "feel"}:
                scores.append(1.0)
                continue

            # Check for acronym first
            if w_lower in self.acronyms_db:
                expansion = self.acronyms_db[w_lower]
                pattern = r'\b' + re.escape(word) + r'\b'
                corrected_text = re.sub(pattern, expansion, corrected_text, flags=re.IGNORECASE)
                corrections.append(f"{word} → {expansion} (acronym expansion)")
                scores.append(0.99)
                continue

            # Check for typo match in medical dictionary
            best_match, score = self.find_best_medical_match(w_lower, threshold=0.74)
            if best_match and best_match != w_lower:
                pattern = r'\b' + re.escape(word) + r'\b'
                # Preserve original case if capitalized
                replacement = best_match.capitalize() if word.istitle() else best_match
                corrected_text = re.sub(pattern, replacement, corrected_text)
                corrections.append(f"{word} → {replacement}")
                scores.append(score)
            elif best_match:
                scores.append(1.0)

        avg_confidence = round(sum(scores) / len(scores), 2) if scores else 0.95
        return corrected_text, corrections, avg_confidence

    def extract_medical_terms(self, text: str) -> List[Dict[str, Any]]:
        """
        Layer 2: Identify and validate medical terms against SNOMED database.
        """
        found_terms = []
        text_lower = text.lower()

        # Check multi-word and single-word terms
        for term, data in self.terms_db.items():
            pattern = r'\b' + re.escape(term) + r'\b'
            if re.search(pattern, text_lower):
                found_terms.append({
                    "term": term,
                    "standard": data["standard"],
                    "category": data["category"],
                    "snomed_id": data["snomed_id"]
                })

        return found_terms

    def normalize_query(self, text: str) -> str:
        """
        Layer 3: Normalize whitespace, punctuation, and medical abbreviations.
        """
        normalized = text.strip()
        # Expand known acronyms
        for acronym, expanded in self.acronyms_db.items():
            pattern = r'\b' + re.escape(acronym) + r'\b'
            normalized = re.sub(pattern, expanded, normalized, flags=re.IGNORECASE)
        # Clean extra whitespace
        normalized = re.sub(r'\s+', ' ', normalized)
        return normalized

    def validate_and_correct(self, query: str) -> Dict[str, Any]:
        """
        Complete 3-Layer Validation Pipeline:
        1. Typo detection & correction
        2. Medical term validation & SNOMED mapping
        3. Query normalization & confidence scoring
        """
        if not query or not query.strip():
            return {
                "original": query,
                "corrected": "",
                "is_valid": False,
                "corrections_made": [],
                "confidence_score": 0.0,
                "medical_terms_found": [],
                "issues": ["Query is empty. Please enter clinical symptoms or questions."]
            }

        # Step 1: Typo Detection & Correction
        corrected_text, corrections, typo_score = self.detect_and_correct_typos(query)

        # Step 2: Query Normalization
        normalized_query = self.normalize_query(corrected_text)

        # Step 3: Extract Medical Terms
        medical_terms_info = self.extract_medical_terms(normalized_query)
        medical_terms_names = [t["term"] for t in medical_terms_info]

        issues = []
        is_valid = True
        final_confidence = typo_score

        if not medical_terms_names and len(normalized_query.split()) > 3:
            issues.append("No standardized medical symptoms or conditions detected in query.")
            final_confidence = max(0.65, final_confidence - 0.15)
        elif medical_terms_names:
            final_confidence = min(1.0, max(0.90, final_confidence + 0.05))

        return {
            "original": query,
            "corrected": normalized_query,
            "is_valid": is_valid,
            "corrections_made": corrections,
            "confidence_score": round(final_confidence, 2),
            "medical_terms_found": medical_terms_names,
            "medical_terms_details": medical_terms_info,
            "issues": issues
        }

# Global singleton instance
validator = MedicalQueryValidator()
