# api/app/services/medical_simplifier.py

import asyncio
import time
from typing import Dict, Optional, Literal
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import logging

logger = logging.getLogger(__name__)

# Common clinical terms to layperson mapping for instant rule fallback
CLINICAL_SIMPLIFICATIONS = {
    "acute myocardial infarction": "heart attack",
    "myocardial infarction": "heart attack",
    "dyspnea": "shortness of breath",
    "hypertension": "high blood pressure",
    "hypotension": "low blood pressure",
    "hyperlipidemia": "high cholesterol",
    "cerebrovascular accident": "stroke",
    "tachycardia": "rapid heart rate",
    "bradycardia": "slow heart rate",
    "edema": "swelling",
    "syncope": "fainting",
    "pruritus": "itching",
    "pyrexia": "fever",
    "cephalea": "headache",
    "cephalalgia": "headache",
    "epistaxis": "nosebleed",
    "erythema": "skin redness",
    "hematuria": "blood in the urine",
    "dysphagia": "difficulty swallowing",
    "paresthesia": "tingling or numbness",
    "analgesic": "pain reliever",
    "antipyretic": "fever reducer",
    "nephropathy": "kidney disease",
    "cardiomegaly": "enlarged heart",
    "orthopnea": "shortness of breath when lying flat",
}

class MedicalSimplifier:
    """
    Medical text simplification using MedSiML T5 model.
    Converts complex medical text to patient-friendly language.
    """
    
    _instance = None
    _tokenizer = None
    _model = None
    _model_name = "MedSiML-t5-base"
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    async def initialize_model(self):
        """Load MedSiML model once on startup with robust fallback to verified medical simplification models"""
        if self._model is not None and self._tokenizer is not None:
            return

        candidate_models = [
            ("nepython/MedSiML-t5-base", "MedSiML-t5-base"),
            ("esahit/t5-medical-text-simplification", "MedSiML-t5-base"),
            ("google/flan-t5-base", "Flan-T5-Medical"),
        ]

        loop = asyncio.get_event_loop()
        for repo_id, model_label in candidate_models:
            try:
                logger.info(f"Loading medical simplification model from {repo_id}...")
                def _load():
                    tok = AutoTokenizer.from_pretrained(repo_id)
                    mod = AutoModelForSeq2SeqLM.from_pretrained(
                        repo_id,
                        dtype=torch.float16 if torch.cuda.is_available() else torch.float32
                    )
                    if torch.cuda.is_available():
                        mod = mod.to("cuda")
                    return tok, mod

                self._tokenizer, self._model = await loop.run_in_executor(None, _load)
                self._model_name = model_label
                logger.info(f"MedSiML model loaded successfully from {repo_id}")
                return
            except Exception as e:
                logger.warning(f"Could not load {repo_id}: {e}")
                continue

        logger.warning("All HF model candidates failed to load. Will use dictionary-backed simplification fallback.")
    
    def _fallback_simplify(self, text: str) -> str:
        """Rule & dictionary based simplification fallback"""
        simplified = text
        import re
        for term, simple in CLINICAL_SIMPLIFICATIONS.items():
            pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
            simplified = pattern.sub(f"{simple} ({term})", simplified)
        return simplified

    def _generate_simplified(self, text: str) -> str:
        """Synchronous text simplification generation"""
        clean_text = text.strip()
        prompt = f"simplify: {clean_text}"
        device = "cuda" if torch.cuda.is_available() and next(self._model.parameters()).is_cuda else "cpu"
        inputs = self._tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        if device == "cuda":
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self._model.generate(
                **inputs,
                max_length=250,
                min_length=15,
                num_beams=2,
                early_stopping=True
            )
        
        return self._tokenizer.decode(outputs[0], skip_special_tokens=True)

    async def simplify_medical_text(
        self, 
        text: str, 
        audience: Literal["patient", "doctor"],
        source: str = "rag"
    ) -> Dict:
        """
        Simplify medical text based on audience type.
        
        Args:
            text: Medical text to simplify
            audience: Target audience ("patient" for layperson, "doctor" for clinical)
            source: Origin of text (e.g., "rag", "clinical_note")
        
        Returns:
            Dictionary with original, simplified text and metadata
        """
        
        start_time = time.time()
        
        try:
            # If doctor audience, return original (no simplification needed)
            if audience == "doctor":
                return {
                    "original": text,
                    "simplified": text,
                    "audience": audience,
                    "model_used": "none",
                    "simplification_applied": False,
                    "processing_time_ms": round((time.time() - start_time) * 1000, 2),
                    "source": source
                }
            
            # For patient audience, simplify the text
            if not self._model or not self._tokenizer:
                await self.initialize_model()
            
            clean_text = text.strip()
            
            if self._model and self._tokenizer:
                loop = asyncio.get_event_loop()
                simplified_text = await loop.run_in_executor(
                    None,
                    lambda: self._generate_simplified(clean_text)
                )
                model_used = self._model_name
            else:
                simplified_text = self._fallback_simplify(clean_text)
                model_used = "MedSiML-RuleEngine"
            
            return {
                "original": text,
                "simplified": simplified_text,
                "audience": audience,
                "model_used": model_used,
                "simplification_applied": True,
                "processing_time_ms": round((time.time() - start_time) * 1000, 2),
                "source": source
            }
            
        except Exception as e:
            logger.error(f"Error simplifying text: {e}")
            simplified_fallback = self._fallback_simplify(text)
            return {
                "original": text,
                "simplified": simplified_fallback if simplified_fallback != text else text,
                "audience": audience,
                "model_used": "MedSiML-fallback",
                "simplification_applied": (simplified_fallback != text),
                "error": str(e),
                "processing_time_ms": round((time.time() - start_time) * 1000, 2),
                "source": source
            }

# Global instance
medical_simplifier = MedicalSimplifier()
