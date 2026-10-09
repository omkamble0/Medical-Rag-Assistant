import re
from difflib import SequenceMatcher
from typing import Dict, List, Any, Optional

# Comprehensive medical vocabulary with common typos and phonetic variants
MEDICAL_TERMS: Dict[str, List[str]] = {
    "headache": ["headavhe", "headeache", "hedache", "headach", "headche", "hedach", "headpain"],
    "migraine": ["migrane", "migrainee", "migrain", "migran", "magraine"],
    "diabetes": ["diavtes", "diabtes", "diabetis", "diabetez", "diabetus", "dibetes"],
    "hypertension": ["hypertention", "hypertenssion", "hypertesion", "hipertension", "highbp"],
    "hypotension": ["hypotention", "lowbp", "hypotenssion"],
    "asthma": ["asthama", "athsma", "asma", "azma", "astma"],
    "fever": ["fevr", "feavor", "fiver", "feve", "pyrexia"],
    "cough": ["coug", "coufh", "coff", "coughing", "chough"],
    "pneumonia": ["pnemona", "neumonia", "pnumonia", "pneumona", "pneunomia"],
    "bronchitis": ["bronchitus", "bronkitis", "bronchytis", "bronchtis"],
    "nausea": ["nausia", "nausee", "nauseau", "nauseous", "nausious"],
    "vomiting": ["vomitting", "vometing", "vommiting", "emesis"],
    "diarrhea": ["diarhea", "diarrhea", "diarrea", "diarea", "diarrheoa"],
    "fatigue": ["fatig", "fatige", "fatugue", "exhausion", "tiredness"],
    "insomnia": ["insomnea", "inssomnia", "sleeplessness"],
    "anxiety": ["anxity", "anxietey", "anxiety", "anxety"],
    "depression": ["depresion", "depresson", "depresison"],
    "arthritis": ["athritis", "arthritus", "artritis", "arthiritis"],
    "cholesterol": ["colesterol", "cholestrol", "choleseterol", "cholestorol"],
    "statin": ["statins", "atorvastatin", "rosuvastatin", "simvastatin"],
    "paxlovid": ["paxlovd", "paxolvid", "nirmatrelvir", "paxlovide"],
    "semaglutide": ["semaglutid", "ozempic", "wegovy", "mounjaro", "tirzepatide"],
    "lisinopril": ["lisinoprl", "lisinopril", "prinivil", "zestril"],
    "amlodipine": ["amlodopine", "amlodapine", "norvasc"],
    "metformin": ["metformn", "metformim", "glucophage"],
    "ibuprofen": ["ibruprofen", "ibuprophen", "ibroprofen", "advil", "motrin"],
    "acetaminophen": ["acetominophen", "paracetamol", "tylenol", "acetaminaphen"],
    "antibiotic": ["antibioic", "antibotic", "anti-biotic", "antibiotics"],
    "infection": ["infetion", "infecshun", "infaction"],
    "tachycardia": ["tachicardia", "tackicardia", "fastheartbeat"],
    "bradycardia": ["bradicardia", "slowheartbeat"],
    "arrhythmia": ["arrythmia", "arythmia", "arrhytmia"],
    "palpitations": ["palpitation", "palpatations", "heartflutter"],
    "vertigo": ["vertigo", "dizzyness", "dizzines", "lightheadedness"],
    "concussion": ["concusion", "concusshun", "headinjury"],
    "seizure": ["siezure", "seizur", "sezure", "convulsion"],
    "stroke": ["strok", "apoplexy", "cerebrovascular"],
    "myocardial": ["miocardial", "infarction", "heartattack"]
}

class QueryGuard:
    """
    Tier-1 Query Guard: Validates medical terminology, detects misspellings,
    and returns suggested corrections before vector retrieval or LLM execution.
    """
    
    def normalize(self, q: str) -> str:
        """Strips special characters and lowercases the input."""
        return re.sub(r"[^a-zA-Z0-9\s]", "", q.lower()).strip()

    def similarity(self, a: str, b: str) -> float:
        """Computes character SequenceMatcher ratio between two tokens."""
        return SequenceMatcher(None, a, b).ratio()

    def correct_query(self, q: str) -> Dict[str, Any]:
        """
        Scans each word in the query and finds closest medical terms.
        Returns corrected string and metadata on replacements made.
        """
        clean = self.normalize(q)
        if not clean:
            return {
                "corrected": q,
                "corrections": [],
                "has_corrections": False
            }

        words = clean.split()
        corrected_words = []
        corrections_made = []

        for word in words:
            # Skip very short filler words
            if len(word) <= 2:
                corrected_words.append(word)
                continue

            best_match = word
            best_score = 0.0
            matched_canonical = None

            for canonical, variants in MEDICAL_TERMS.items():
                all_forms = [canonical] + variants
                for v in all_forms:
                    score = self.similarity(word, v)
                    if score > best_score:
                        best_score = score
                        best_match = canonical
                        matched_canonical = canonical

            # Threshold for correction: high similarity match to known variant or misspelling
            if best_score >= 0.75 and best_match != word:
                corrected_words.append(best_match)
                corrections_made.append({
                    "original_word": word,
                    "corrected_word": best_match,
                    "confidence": round(best_score, 2)
                })
            else:
                corrected_words.append(word)

        corrected_text = " ".join(corrected_words)
        has_corrections = len(corrections_made) > 0

        return {
            "corrected": corrected_text,
            "corrections": corrections_made,
            "has_corrections": has_corrections
        }

    def validate(self, q: str) -> Dict[str, Any]:
        """
        Validates query and determines if automatic or user-prompted correction is advised.
        """
        if not q or not q.strip():
            return {
                "original": q,
                "corrected": q,
                "needs_correction": False,
                "confidence": 1.0,
                "corrections": []
            }

        result = self.correct_query(q)
        
        if result["has_corrections"]:
            # Calculate overall confidence based on correction scores
            avg_conf = sum(c["confidence"] for c in result["corrections"]) / len(result["corrections"])
            return {
                "original": q,
                "corrected": result["corrected"],
                "needs_correction": True,
                "confidence": round(avg_conf, 2),
                "corrections": result["corrections"]
            }

        return {
            "original": q,
            "corrected": q,
            "needs_correction": False,
            "confidence": 1.0,
            "corrections": []
        }
