'use client';

import { useState, useCallback, useRef } from 'react';

export interface MedicalTermDetail {
  term: string;
  standard: string;
  category: string;
  snomed_id: string;
}

export interface ValidationResult {
  original: string;
  corrected: string;
  is_valid: boolean;
  corrections_made: string[];
  confidence_score: number;
  medical_terms_found: string[];
  medical_terms_details?: MedicalTermDetail[];
  issues: string[];
}

// Built-in client-side medical dictionary fallback for instant zero-latency feedback
const CLIENT_MEDICAL_DICT: Record<string, { standard: string; category: string; snomed_id: string }> = {
  headache: { standard: 'Headache', category: 'symptom', snomed_id: '25064002' },
  headaches: { standard: 'Headache', category: 'symptom', snomed_id: '25064002' },
  migraine: { standard: 'Migraine', category: 'condition', snomed_id: '37796009' },
  diabetes: { standard: 'Diabetes Mellitus', category: 'condition', snomed_id: '73211009' },
  hypertension: { standard: 'Hypertension', category: 'condition', snomed_id: '38341003' },
  hypotension: { standard: 'Hypotension', category: 'condition', snomed_id: '45007003' },
  asthma: { standard: 'Asthma', category: 'condition', snomed_id: '195967001' },
  dyspnea: { standard: 'Dyspnea', category: 'symptom', snomed_id: '267036007' },
  fever: { standard: 'Fever', category: 'symptom', snomed_id: '386661006' },
  nausea: { standard: 'Nausea', category: 'symptom', snomed_id: '422587007' },
  vomiting: { standard: 'Vomiting', category: 'symptom', snomed_id: '422400008' },
  diarrhea: { standard: 'Diarrhea', category: 'symptom', snomed_id: '62315008' },
  constipation: { standard: 'Constipation', category: 'symptom', snomed_id: '14760008' },
  fatigue: { standard: 'Fatigue', category: 'symptom', snomed_id: '84229001' },
  cough: { standard: 'Cough', category: 'symptom', snomed_id: '49727002' },
  pneumonia: { standard: 'Pneumonia', category: 'condition', snomed_id: '233604007' },
  bronchitis: { standard: 'Bronchitis', category: 'condition', snomed_id: '32398004' },
  edema: { standard: 'Edema', category: 'symptom', snomed_id: '267038008' },
  swelling: { standard: 'Edema', category: 'symptom', snomed_id: '267038008' },
  infarction: { standard: 'Infarction', category: 'condition', snomed_id: '55641003' },
  tachycardia: { standard: 'Tachycardia', category: 'symptom', snomed_id: '3424008' },
  bradycardia: { standard: 'Bradycardia', category: 'symptom', snomed_id: '48867003' },
  arrhythmia: { standard: 'Cardiac Arrhythmia', category: 'condition', snomed_id: '698247007' },
  angina: { standard: 'Angina Pectoris', category: 'symptom', snomed_id: '194828000' },
  syncope: { standard: 'Syncope', category: 'symptom', snomed_id: '271594007' },
  fainting: { standard: 'Syncope', category: 'symptom', snomed_id: '271594007' },
  dizziness: { standard: 'Dizziness', category: 'symptom', snomed_id: '404640003' },
  vertigo: { standard: 'Vertigo', category: 'symptom', snomed_id: '399153001' },
  insomnia: { standard: 'Insomnia', category: 'condition', snomed_id: '193462001' },
  arthritis: { standard: 'Arthritis', category: 'condition', snomed_id: '3723001' },
  metformin: { standard: 'Metformin', category: 'medication', snomed_id: '372567009' },
  lisinopril: { standard: 'Lisinopril', category: 'medication', snomed_id: '387449005' },
  amlodipine: { standard: 'Amlodipine', category: 'medication', snomed_id: '386864001' },
  atorvastatin: { standard: 'Atorvastatin', category: 'medication', snomed_id: '387584000' },
  semaglutide: { standard: 'Semaglutide', category: 'medication', snomed_id: '763158003' },
  ozempic: { standard: 'Semaglutide (Ozempic)', category: 'medication', snomed_id: '763158003' },
  ibuprofen: { standard: 'Ibuprofen', category: 'medication', snomed_id: '387207008' },
  paracetamol: { standard: 'Acetaminophen', category: 'medication', snomed_id: '387517004' },
  acetaminophen: { standard: 'Acetaminophen', category: 'medication', snomed_id: '387517004' },
  aspirin: { standard: 'Aspirin', category: 'medication', snomed_id: '387458008' },
  amoxicillin: { standard: 'Amoxicillin', category: 'medication', snomed_id: '372687004' },
  insulin: { standard: 'Insulin', category: 'medication', snomed_id: '387340001' },
  paxlovid: { standard: 'Nirmatrelvir/Ritonavir (Paxlovid)', category: 'medication', snomed_id: '1208940003' },
};

// Levenshtein similarity calculation for fallback typo detection
function stringSimilarity(s1: string, s2: string): number {
  const longer = s1.length < s2.length ? s2 : s1;
  const shorter = s1.length < s2.length ? s1 : s2;
  const longerLength = longer.length;
  if (longerLength === 0) return 1.0;

  const costs: number[] = [];
  for (let i = 0; i <= shorter.length; i++) {
    costs[i] = i;
  }
  for (let i = 1; i <= longer.length; i++) {
    costs[0] = i;
    let nw = i - 1;
    for (let j = 1; j <= shorter.length; j++) {
      const cj = Math.min(
        1 + Math.min(costs[j], costs[j - 1]),
        longer.charAt(i - 1) === shorter.charAt(j - 1) ? nw : nw + 1
      );
      nw = costs[j];
      costs[j] = cj;
    }
  }
  return (longerLength - costs[shorter.length]) / longerLength;
}

function clientSideValidation(query: string): ValidationResult {
  const words = query.split(/\b/);
  const corrections: string[] = [];
  const foundTerms: string[] = [];
  const details: MedicalTermDetail[] = [];
  let correctedText = query;

  words.forEach((word) => {
    const cleanWord = word.trim().toLowerCase();
    if (!cleanWord || cleanWord.length < 3) return;

    // Common stop words to skip
    if (['have', 'and', 'the', 'for', 'with', 'what', 'cure', 'pain', 'feel'].includes(cleanWord)) {
      return;
    }

    // Exact match check
    if (CLIENT_MEDICAL_DICT[cleanWord]) {
      const entry = CLIENT_MEDICAL_DICT[cleanWord];
      if (!foundTerms.includes(cleanWord)) {
        foundTerms.push(cleanWord);
        details.push({
          term: cleanWord,
          standard: entry.standard,
          category: entry.category,
          snomed_id: entry.snomed_id,
        });
      }
      return;
    }

    // Fuzzy match for typos
    let bestMatch = '';
    let highestSim = 0;
    for (const term of Object.keys(CLIENT_MEDICAL_DICT)) {
      const sim = stringSimilarity(cleanWord, term);
      if (sim > highestSim && sim >= 0.72) {
        highestSim = sim;
        bestMatch = term;
      }
    }

    if (bestMatch && bestMatch !== cleanWord) {
      const regex = new RegExp(`\\b${word}\\b`, 'g');
      correctedText = correctedText.replace(regex, bestMatch);
      corrections.push(`${word} → ${bestMatch}`);

      const entry = CLIENT_MEDICAL_DICT[bestMatch];
      if (!foundTerms.includes(bestMatch)) {
        foundTerms.push(bestMatch);
        details.push({
          term: bestMatch,
          standard: entry.standard,
          category: entry.category,
          snomed_id: entry.snomed_id,
        });
      }
    }
  });

  return {
    original: query,
    corrected: correctedText,
    is_valid: true,
    corrections_made: corrections,
    confidence_score: corrections.length > 0 ? 0.96 : 0.98,
    medical_terms_found: foundTerms,
    medical_terms_details: details,
    issues: [],
  };
}

export function useQueryValidator() {
  const [validationResult, setValidationResult] = useState<ValidationResult | null>(null);
  const [isValidating, setIsValidating] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const lastQueryRef = useRef<string>('');

  const validateQuery = useCallback(async (query: string): Promise<ValidationResult | null> => {
    if (!query || !query.trim()) {
      setValidationResult(null);
      return null;
    }

    setIsValidating(true);
    setError(null);
    lastQueryRef.current = query;

    // 1. Try validator server endpoint (either standalone port 8001 or main API /api/v1/validate-query)
    const endpoints = [
      'http://localhost:8001/validate-query',
      '/api/v1/validate-query',
      'http://localhost:8000/api/v1/validate-query',
    ];

    for (const url of endpoints) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 1200);

        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query }),
          signal: controller.signal,
        });
        clearTimeout(timeoutId);

        if (response.ok) {
          const rawData = await response.json();
          const data: ValidationResult = {
            ...rawData,
            issues: Array.isArray(rawData.issues) ? rawData.issues : [],
            corrections_made: Array.isArray(rawData.corrections_made) ? rawData.corrections_made : [],
            medical_terms_found: Array.isArray(rawData.medical_terms_found) ? rawData.medical_terms_found : [],
          };
          if (lastQueryRef.current === query) {
            setValidationResult(data);
            setIsValidating(false);
            return data;
          }
        }
      } catch {
        // Continue to fallback
      }
    }

    // 2. Client-side deterministic fallback
    const fallbackResult = clientSideValidation(query);
    if (lastQueryRef.current === query) {
      setValidationResult(fallbackResult);
      setIsValidating(false);
    }
    return fallbackResult;
  }, []);

  const clearValidation = useCallback(() => {
    setValidationResult(null);
    setError(null);
  }, []);

  return {
    validationResult,
    isValidating,
    error,
    validateQuery,
    clearValidation,
  };
}
