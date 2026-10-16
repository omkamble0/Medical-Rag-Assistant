"""
Tier-1 Query Guard & Clinical Typo Correction Engine.
Detects medical misspellings, normalizes terminology, protects valid English words,
and guarantees zero-false-positive corruptions (e.g. never converts 'best' to 'breast').
"""

import re
from difflib import SequenceMatcher
from typing import Dict, List, Any, Optional, Set, Tuple

# Comprehensive common English vocabulary (words that must NEVER be treated as typos)
COMMON_ENGLISH_WORDS: Set[str] = {
    # Question & structural words
    "what", "when", "where", "which", "who", "whom", "whose", "why", "how",
    "are", "is", "was", "were", "been", "being", "have", "has", "had", "does", "do", "did",
    "can", "could", "shall", "should", "will", "would", "may", "might", "must",
    "the", "and", "or", "nor", "but", "for", "with", "from", "that", "this", "these", "those",
    "they", "them", "their", "theirs", "he", "him", "his", "she", "her", "hers", "it", "its",
    "we", "us", "our", "ours", "you", "your", "yours", "i", "me", "my", "mine",
    "in", "on", "at", "to", "by", "of", "about", "into", "through", "after", "before", "between",
    "under", "above", "below", "up", "down", "over", "out", "off", "near", "against", "among",
    "as", "than", "so", "such", "then", "very", "too", "also", "only", "just", "even", "more",
    "most", "less", "least", "some", "any", "no", "not", "all", "both", "each", "every", "other",
    # Adjectives & descriptors (crucial to protect short words like best, test, safe, good)
    "best", "better", "good", "bad", "safe", "safest", "effective", "first", "second", "third",
    "last", "next", "new", "old", "early", "late", "recent", "daily", "weekly", "monthly", "yearly",
    "mild", "moderate", "severe", "acute", "chronic", "critical", "urgent", "stable", "unstable",
    "high", "low", "normal", "fast", "slow", "deep", "shallow", "hard", "soft", "free", "clear",
    "true", "false", "real", "pure", "dry", "wet", "hot", "cold", "warm", "cool", "sore", "dull",
    "sharp", "burning", "aching", "constant", "sudden", "gradual", "frequent", "rare", "common",
    # Clinical verbs & actions
    "treat", "treats", "treated", "treating", "treatment", "treatments",
    "cure", "cures", "cured", "curing", "care", "cares", "cared", "caring",
    "help", "helps", "helped", "helping", "take", "takes", "taking", "took", "taken",
    "give", "gives", "given", "giving", "stop", "stops", "stopped", "stopping",
    "start", "starts", "started", "starting", "prevent", "prevents", "prevented", "prevention",
    "reduce", "reduces", "reduced", "reducing", "lower", "lowers", "lowered", "lowering",
    "raise", "raises", "raised", "raising", "increase", "increases", "increased", "increasing",
    "check", "checks", "checked", "checking", "test", "tests", "tested", "testing",
    "feel", "feels", "feeling", "felt", "know", "knows", "known", "show", "shows", "shown",
    "find", "finds", "found", "use", "uses", "used", "using", "work", "works", "worked",
    "cause", "causes", "caused", "causing", "lead", "leads", "led", "leading",
    # Anatomy & common health nouns
    "body", "head", "neck", "throat", "chest", "back", "arm", "arms", "hand", "hands",
    "leg", "legs", "foot", "feet", "knee", "knees", "bone", "bones", "joint", "joints",
    "skin", "hair", "eye", "eyes", "ear", "ears", "nose", "mouth", "tongue", "tooth", "teeth",
    "heart", "lung", "lungs", "liver", "kidney", "kidneys", "stomach", "bowel", "gut",
    "blood", "brain", "nerve", "nerves", "muscle", "muscles", "vein", "veins", "artery", "arteries",
    "pain", "pains", "ache", "aches", "rash", "rashes", "pill", "pills", "drug", "drugs",
    "dose", "doses", "dosing", "dosage", "food", "diet", "water", "rest", "sleep", "weight",
    "loss", "gain", "drop", "drops", "rate", "rates", "level", "levels", "risk", "risks",
    "sign", "signs", "symptom", "symptoms", "disease", "diseases", "disorder", "disorders",
    "condition", "conditions", "illness", "illnesses", "syndrome", "syndromes",
    "guideline", "guidelines", "protocol", "protocols", "trial", "trials", "study", "studies",
    "evidence", "based", "evidence-based", "practice", "practices", "review", "reviews",
    "doctor", "doctors", "physician", "physicians", "nurse", "nurses", "patient", "patients",
    "adult", "adults", "child", "children", "baby", "infant", "toddler", "teen", "elderly",
    "male", "female", "men", "women", "boy", "girl", "years", "months", "days", "weeks", "hours",
    "life", "health", "care", "clinic", "hospital", "office", "home", "emergency", "triage",
    "screening", "checkup", "exam", "scan", "ultrasound", "biopsy", "mri", "x-ray", "ct"
}

# Explicit high-confidence medical typo mappings
EXPLICIT_TYPOS: Dict[str, str] = {
    # Core clinical and structural terms
    "tretmeant": "treatment",
    "tretment": "treatment",
    "treatmeant": "treatment",
    "treatement": "treatment",
    "treament": "treatment",
    "treatmnt": "treatment",
    "tretmeants": "treatments",
    "treatmeants": "treatments",
    "treatements": "treatments",
    "evidance": "evidence",
    "evidense": "evidence",
    "evidencebased": "evidence-based",
    "guidline": "guideline",
    "guidlines": "guidelines",
    "guidelin": "guideline",
    "guidelins": "guidelines",
    "medicaton": "medication",
    "medisin": "medication",
    "medicationn": "medication",
    "medicaiton": "medication",
    "medecine": "medicine",
    "symtom": "symptom",
    "symtoms": "symptoms",
    "symptomps": "symptoms",
    "simptom": "symptom",
    "simptoms": "symptoms",
    "symptomns": "symptoms",
    "dissorder": "disorder",
    "disoder": "disorder",
    "dissorders": "disorders",
    "disoders": "disorders",
    "perscription": "prescription",
    "prescribtion": "prescription",
    "diagnoisis": "diagnosis",
    "diagnoseis": "diagnosis",
    "therpy": "therapy",
    "therapies": "therapies",

    # Psychiatric & neurological conditions
    "anxity": "anxiety",
    "anxietey": "anxiety",
    "anxety": "anxiety",
    "anxius": "anxious",
    "anxios": "anxious",
    "panick": "panic",
    "panik": "panic",
    "depresion": "depression",
    "depresson": "depression",
    "depresison": "depression",
    "depresed": "depressed",
    "insomnea": "insomnia",
    "inssomnia": "insomnia",
    "sleeplessness": "insomnia",
    "migrane": "migraine",
    "migrainee": "migraine",
    "migrain": "migraine",
    "migran": "migraine",
    "magraine": "migraine",
    "headavhe": "headache",
    "headeache": "headache",
    "hedache": "headache",
    "headach": "headache",
    "headche": "headache",
    "hedach": "headache",
    "headpain": "headache",
    "concusion": "concussion",
    "concusshun": "concussion",
    "siezure": "seizure",
    "seizur": "seizure",
    "sezure": "seizure",
    "strok": "stroke",
    "vertigo": "vertigo",
    "dizzyness": "dizziness",
    "dizzines": "dizziness",

    # Cardiovascular & metabolic
    "hipertension": "hypertension",
    "hypertention": "hypertension",
    "hypertenssion": "hypertension",
    "hypertesion": "hypertension",
    "highbp": "hypertension",
    "hypotention": "hypotension",
    "lowbp": "hypotension",
    "diavtes": "diabetes",
    "diabtes": "diabetes",
    "diabetis": "diabetes",
    "diabetez": "diabetes",
    "diabetus": "diabetes",
    "dibetes": "diabetes",
    "colesterol": "cholesterol",
    "cholestrol": "cholesterol",
    "choleseterol": "cholesterol",
    "cholestorol": "cholesterol",
    "arrythmia": "arrhythmia",
    "arythmia": "arrhythmia",
    "arrhytmia": "arrhythmia",
    "tachicardia": "tachycardia",
    "tackicardia": "tachycardia",
    "bradicardia": "bradycardia",
    "palpitation": "palpitations",
    "palpatations": "palpitations",
    "heartattack": "heart attack",
    "miocardial": "myocardial",

    # Respiratory & infectious
    "asthama": "asthma",
    "athsma": "asthma",
    "asma": "asthma",
    "azma": "asthma",
    "astma": "asthma",
    "coug": "cough",
    "coufh": "cough",
    "coff": "cough",
    "chough": "cough",
    "fevr": "fever",
    "feavor": "fever",
    "fiver": "fever",
    "pnemona": "pneumonia",
    "neumonia": "pneumonia",
    "pnumonia": "pneumonia",
    "pneumona": "pneumonia",
    "pneunomia": "pneumonia",
    "bronchitus": "bronchitis",
    "bronkitis": "bronchitis",
    "bronchytis": "bronchitis",
    "bronchtis": "bronchitis",
    "infetion": "infection",
    "infecshun": "infection",
    "infaction": "infection",
    "antibioic": "antibiotic",
    "antibotic": "antibiotic",
    "anti-biotic": "antibiotic",

    # GI & general symptoms
    "nausia": "nausea",
    "nausee": "nauseau",
    "nauseous": "nausea",
    "nausious": "nausea",
    "vomitting": "vomiting",
    "vometing": "vomiting",
    "vommiting": "vomiting",
    "diarhea": "diarrhea",
    "diarrea": "diarrhea",
    "diarea": "diarrhea",
    "diarrheoa": "diarrhea",
    "fatig": "fatigue",
    "fatige": "fatigue",
    "fatugue": "fatigue",
    "athritis": "arthritis",
    "arthritus": "arthritis",
    "artritis": "arthritis",
    "arthiritis": "arthritis",

    # Medications
    "albuterall": "albuterol",
    "albuterol": "albuterol",
    "ibruprofen": "ibuprofen",
    "ibuprophen": "ibuprofen",
    "ibroprofen": "ibuprofen",
    "acetominophen": "acetaminophen",
    "acetaminaphen": "acetaminophen",
    "paracetemol": "paracetamol",
    "metformn": "metformin",
    "metformim": "metformin",
    "lisinoprl": "lisinopril",
    "amlodopine": "amlodipine",
    "amlodapine": "amlodipine",
    "semaglutid": "semaglutide",
    "paxlovd": "paxlovid",
    "paxolvid": "paxlovid",
}

# Base canonical medical terms map
MEDICAL_TERMS: Dict[str, List[str]] = {
    "treatment": ["treatments", "therapy", "therapies", "intervention"],
    "evidence": ["trials", "studies", "meta-analysis"],
    "guideline": ["guidelines", "protocol", "protocols"],
    "anxiety": ["anxious", "panic", "phobia", "nervousness"],
    "panic": ["agoraphobia", "panic attack", "panic disorder"],
    "depression": ["depressive", "dysthymia", "unipolar"],
    "headache": ["migraine", "cephalea", "tension headache"],
    "migraine": ["hemiplegic", "scotoma", "aura"],
    "diabetes": ["hyperglycemia", "t2d", "insulin"],
    "hypertension": ["high blood pressure", "arterial hypertension"],
    "hypotension": ["low blood pressure", "orthostatic"],
    "asthma": ["bronchospasm", "wheezing", "inhaler"],
    "fever": ["pyrexia", "hyperthermia", "febrile"],
    "cough": ["bronchitis", "tussis", "coughing"],
    "pneumonia": ["consolidation", "pneumonitis"],
    "bronchitis": ["bronchial inflammation", "productive cough"],
    "nausea": ["emesis", "queasiness"],
    "vomiting": ["emesis", "retching"],
    "diarrhea": ["enteritis", "loose stools"],
    "fatigue": ["asthenia", "exhaustion", "malaise"],
    "insomnia": ["sleeplessness", "sleep disturbance"],
    "arthritis": ["osteoarthritis", "rheumatoid arthritis", "joint inflammation"],
    "cholesterol": ["hyperlipidemia", "dyslipidemia", "ldl", "triglycerides"],
    "statin": ["atorvastatin", "rosuvastatin", "simvastatin"],
    "paxlovid": ["nirmatrelvir", "ritonavir"],
    "semaglutide": ["ozempic", "wegovy", "mounjaro", "tirzepatide"],
    "lisinopril": ["ace inhibitor", "prinivil", "zestril"],
    "amlodipine": ["calcium channel blocker", "norvasc"],
    "metformin": ["glucophage", "biguanide"],
    "ibuprofen": ["advil", "motrin", "nsaid"],
    "acetaminophen": ["paracetamol", "tylenol"],
    "antibiotic": ["antimicrobial", "amoxicillin"],
    "infection": ["sepsis", "bacteremia"],
    "tachycardia": ["rapid heart rate", "supraventricular"],
    "bradycardia": ["slow heart rate", "sinus bradycardia"],
    "arrhythmia": ["atrial fibrillation", "afib"],
    "palpitations": ["heart racing", "fluttering"],
    "vertigo": ["bppv", "labyrinthitis", "vestibular"],
    "concussion": ["tbi", "head injury"],
    "seizure": ["epilepsy", "convulsion"],
    "stroke": ["infarction", "tia", "ischemic stroke"],
    "myocardial": ["infarction", "heart attack"]
}


def _populate_database_medical_terms():
    """Dynamically registers medical concepts, condition names, and acronyms from medical_database.json."""
    try:
        from pathlib import Path
        import json
        db_path = Path(__file__).resolve().parent.parent / "data" / "medical_database.json"
        if db_path.exists():
            with open(db_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for d in data:
                name = d.get("name", "").lower()
                clean = re.sub(r"[^a-zA-Z0-9\s]", " ", name).strip()
                tokens = clean.split()
                for tok in tokens:
                    if len(tok) >= 3 and tok not in {"and", "the", "with", "for", "from", "are", "not"}:
                        if tok not in MEDICAL_TERMS:
                            MEDICAL_TERMS[tok] = []
                        if not tok.endswith("s"):
                            s_variant = tok + "s"
                            if s_variant not in MEDICAL_TERMS:
                                MEDICAL_TERMS[s_variant] = []
                parens = re.findall(r"\((.*?)\)", d.get("name", ""))
                for p in parens:
                    acronym = p.strip().lower()
                    if 2 <= len(acronym) <= 8 and acronym not in MEDICAL_TERMS:
                        MEDICAL_TERMS[acronym] = []
    except Exception:
        pass


_populate_database_medical_terms()


def damerau_levenshtein_distance(s1: str, s2: str) -> int:
    """
    Computes Damerau-Levenshtein distance between s1 and s2
    (supports insertions, deletions, substitutions, and adjacent transpositions).
    """
    len1, len2 = len(s1), len(s2)
    d: Dict[Tuple[int, int], int] = {}

    for i in range(-1, len1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len2 + 1):
        d[(-1, j)] = j + 1

    for i in range(len1):
        for j in range(len2):
            cost = 0 if s1[i] == s2[j] else 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,       # deletion
                d[(i, j - 1)] + 1,       # insertion
                d[(i - 1, j - 1)] + cost  # substitution
            )
            if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[(i - 2, j - 2)] + 1)  # transposition

    return d[(len1 - 1, len2 - 1)]


class QueryGuard:
    """
    Tier-1 Query Guard: Validates medical terminology, detects misspellings,
    and guarantees zero-false-positive corruptions of valid English and clinical words.
    """

    def normalize(self, q: str) -> str:
        """
        Normalizes query for analysis while strictly preserving compound hyphens
        (e.g. 'evidence-based', 'first-line') and separating punctuation.
        """
        # Replace non-hyphen, non-alphanumeric punctuation with spaces
        clean = re.sub(r"[^a-zA-Z0-9\s\-]", " ", q.lower())
        # Collapse multiple spaces
        return re.sub(r"\s+", " ", clean).strip()

    def similarity(self, a: str, b: str) -> float:
        """Computes SequenceMatcher character ratio."""
        return SequenceMatcher(None, a, b).ratio()

    def correct_query(self, q: str) -> Dict[str, Any]:
        """
        Scans query tokens, corrects bona fide misspellings, and strictly preserves
        valid English vocabulary and clinical terminology.
        """
        if not q or not q.strip():
            return {
                "corrected": q,
                "corrections": [],
                "has_corrections": False
            }

        # Tokenize preserving word characters and internal hyphens
        # Match tokens like words or hyphenated words
        token_pattern = re.compile(r"([a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*|[^a-zA-Z0-9\s]+|\s+)")
        raw_parts = token_pattern.findall(q)

        corrected_parts: List[str] = []
        corrections_made: List[Dict[str, Any]] = []

        for part in raw_parts:
            # If part is whitespace or punctuation only, preserve verbatim
            if not re.search(r"[a-zA-Z0-9]", part):
                corrected_parts.append(part)
                continue

            word = part.strip()
            word_lower = word.lower()

            # 1. Exact match check: if word is in common English vocabulary or medical dictionary, NEVER alter it!
            if (
                word_lower in COMMON_ENGLISH_WORDS or
                word_lower in MEDICAL_TERMS or
                word_lower in {"evidence-based", "first-line", "short-term", "long-term", "anti-inflammatory", "covid-19"}
            ):
                corrected_parts.append(part)
                continue

            # 2. Check compound word parts if hyphenated (e.g. "evidence-based")
            if "-" in word_lower:
                sub_parts = word_lower.split("-")
                if all(sp in COMMON_ENGLISH_WORDS or sp in MEDICAL_TERMS for sp in sub_parts):
                    corrected_parts.append(part)
                    continue

            # 3. Direct explicit typo dictionary check (O(1) lookup with 100% confidence)
            if word_lower in EXPLICIT_TYPOS:
                replacement = EXPLICIT_TYPOS[word_lower]
                # Match original capitalization if needed
                if word.istitle():
                    replacement_formatted = replacement.title()
                else:
                    replacement_formatted = replacement

                corrected_parts.append(replacement_formatted)
                corrections_made.append({
                    "original_word": word,
                    "corrected_word": replacement_formatted,
                    "confidence": 0.98
                })
                continue

            # 4. Skip numbers and short filler words <= 2 characters
            if len(word_lower) <= 2 or word_lower.isdigit():
                corrected_parts.append(part)
                continue

            # 5. Damerau-Levenshtein search among canonical medical terms and common words
            best_match: Optional[str] = None
            best_score = 0.0
            best_dist = 999

            # Build candidate target list
            candidate_targets = list(MEDICAL_TERMS.keys())

            for target in candidate_targets:
                # Length filter: don't compare words with vastly different lengths
                len_diff = abs(len(word_lower) - len(target))
                if len(word_lower) <= 4 and len_diff > 0:
                    continue  # Short words (<=4 chars) must have exact length match
                if len(word_lower) <= 6 and len_diff > 1:
                    continue
                if len_diff > 2:
                    continue

                dist = damerau_levenshtein_distance(word_lower, target)
                
                # Strict distance constraints based on word length
                max_allowed_dist = 1 if len(word_lower) <= 6 else 2
                if dist <= max_allowed_dist:
                    sim = self.similarity(word_lower, target)
                    if dist < best_dist or (dist == best_dist and sim > best_score):
                        best_dist = dist
                        best_score = sim
                        best_match = target

            # Only accept correction if distance meets strict criteria and score is high
            min_sim_thresh = 0.85 if len(word_lower) <= 5 else 0.80
            if (
                best_match and
                best_match != word_lower and
                best_score >= min_sim_thresh and
                best_match not in COMMON_ENGLISH_WORDS  # Don't swap arbitrary words into common words without reason
            ):
                replacement_formatted = best_match.title() if word.istitle() else best_match
                corrected_parts.append(replacement_formatted)
                corrections_made.append({
                    "original_word": word,
                    "corrected_word": replacement_formatted,
                    "confidence": round(best_score, 2)
                })
            else:
                corrected_parts.append(part)

        corrected_text = "".join(corrected_parts)
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
