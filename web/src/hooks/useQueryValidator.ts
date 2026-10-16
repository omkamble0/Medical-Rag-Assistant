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

// Common English words that must NEVER be flagged as typos or altered into medical words
const COMMON_ENGLISH_WORDS = new Set([
  'what', 'when', 'where', 'which', 'who', 'whom', 'whose', 'why', 'how',
  'are', 'is', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'does', 'do', 'did',
  'can', 'could', 'shall', 'should', 'will', 'would', 'may', 'might', 'must',
  'the', 'and', 'or', 'nor', 'but', 'for', 'with', 'from', 'that', 'this', 'these', 'those',
  'they', 'them', 'their', 'theirs', 'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its',
  'we', 'us', 'our', 'ours', 'you', 'your', 'yours', 'i', 'me', 'my', 'mine',
  'in', 'on', 'at', 'to', 'by', 'of', 'about', 'into', 'through', 'after', 'before', 'between',
  'under', 'above', 'below', 'up', 'down', 'over', 'out', 'off', 'near', 'against', 'among',
  'as', 'than', 'so', 'such', 'then', 'very', 'too', 'also', 'only', 'just', 'even', 'more',
  'most', 'less', 'least', 'some', 'any', 'no', 'not', 'all', 'both', 'each', 'every', 'other',
  'best', 'better', 'good', 'bad', 'safe', 'safest', 'effective', 'first', 'second', 'third',
  'last', 'next', 'new', 'old', 'early', 'late', 'recent', 'daily', 'weekly', 'monthly', 'yearly',
  'mild', 'moderate', 'severe', 'acute', 'chronic', 'critical', 'urgent', 'stable', 'unstable',
  'high', 'low', 'normal', 'fast', 'slow', 'deep', 'shallow', 'hard', 'soft', 'free', 'clear',
  'true', 'false', 'real', 'pure', 'dry', 'wet', 'hot', 'cold', 'warm', 'cool', 'sore', 'dull',
  'sharp', 'burning', 'aching', 'constant', 'sudden', 'gradual', 'frequent', 'rare', 'common',
  'treat', 'treats', 'treated', 'treating', 'treatment', 'treatments',
  'cure', 'cures', 'care', 'help', 'take', 'give', 'stop', 'start', 'prevent', 'reduce',
  'lower', 'raise', 'increase', 'check', 'test', 'tests', 'feel', 'know', 'show', 'find', 'use',
  'body', 'head', 'neck', 'throat', 'chest', 'back', 'arm', 'hand', 'leg', 'foot', 'knee',
  'skin', 'hair', 'eye', 'ear', 'nose', 'mouth', 'heart', 'lung', 'liver', 'kidney', 'stomach',
  'pain', 'pains', 'ache', 'aches', 'rash', 'pill', 'pills', 'drug', 'drugs', 'dose', 'diet',
  'food', 'rest', 'sleep', 'weight', 'loss', 'gain', 'rate', 'risk', 'sign', 'signs',
  'symptom', 'symptoms', 'disease', 'diseases', 'disorder', 'disorders', 'condition', 'conditions',
  'guideline', 'guidelines', 'protocol', 'protocols', 'trial', 'trials', 'study', 'studies',
  'evidence', 'based', 'evidence-based', 'doctor', 'patient', 'patients', 'adult', 'child',
  'anxiety', 'panic', 'depression', 'stress', 'fear'
]);

// Explicit typo corrections
const EXPLICIT_TYPOS: Record<string, string> = {
  tretmeant: 'treatment',
  tretment: 'treatment',
  treatmeant: 'treatment',
  treatement: 'treatment',
  treament: 'treatment',
  treatmnt: 'treatment',
  tretmeants: 'treatments',
  treatmeants: 'treatments',
  treatements: 'treatments',
  evidance: 'evidence',
  evidense: 'evidence',
  guidline: 'guideline',
  guidlines: 'guidelines',
  guidelin: 'guideline',
  guidelins: 'guidelines',
  medicaton: 'medication',
  medisin: 'medication',
  medicationn: 'medication',
  medicaiton: 'medication',
  symtom: 'symptom',
  symtoms: 'symptoms',
  symptomps: 'symptoms',
  simptom: 'symptom',
  simptoms: 'symptoms',
  dissorder: 'disorder',
  disoder: 'disorder',
  dissorders: 'disorders',
  disoders: 'disorders',
  anxity: 'anxiety',
  anxietey: 'anxiety',
  anxety: 'anxiety',
  anxius: 'anxious',
  panick: 'panic',
  panik: 'panic',
  depresion: 'depression',
  depresson: 'depression',
  hipertension: 'hypertension',
  hypertention: 'hypertension',
  diavtes: 'diabetes',
  diabtes: 'diabetes',
  diabetis: 'diabetes',
  colesterol: 'cholesterol',
  cholestrol: 'cholesterol',
  asthama: 'asthma',
  athsma: 'asthma',
  headavhe: 'headache',
  migrane: 'migraine',
  athritis: 'arthritis',
  pnemona: 'pneumonia',
  bronchitus: 'bronchitis',
  nausia: 'nausea',
  vomitting: 'vomiting',
  diarhea: 'diarrhea',
  fatig: 'fatigue',
  insomnea: 'insomnia',
  albuterall: 'albuterol',
  ibruprofen: 'ibuprofen',
  acetominophen: 'acetaminophen',
  metformn: 'metformin',
  semaglutid: 'semaglutide',
  paxlovd: 'paxlovid',
};

// Built-in client-side medical dictionary
const CLIENT_MEDICAL_DICT: Record<string, { standard: string; category: string; snomed_id: string }> = {
  anxiety: { standard: 'Generalized Anxiety Disorder', category: 'condition', snomed_id: '21897009' },
  panic: { standard: 'Panic Disorder', category: 'condition', snomed_id: '371631005' },
  depression: { standard: 'Major Depressive Disorder', category: 'condition', snomed_id: '370143000' },
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
  cholesterol: { standard: 'Hypercholesterolemia', category: 'condition', snomed_id: '13644009' },
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

function damerauLevenshtein(s1: string, s2: string): number {
  const l1 = s1.length;
  const l2 = s2.length;
  const d: number[][] = [];

  for (let i = 0; i <= l1; i++) {
    d[i] = [];
    d[i][0] = i;
  }
  for (let j = 0; j <= l2; j++) {
    d[0][j] = j;
  }

  for (let i = 1; i <= l1; i++) {
    for (let j = 1; j <= l2; j++) {
      const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
      d[i][j] = Math.min(
        d[i - 1][j] + 1,       // deletion
        d[i][j - 1] + 1,       // insertion
        d[i - 1][j - 1] + cost  // substitution
      );
      if (i > 1 && j > 1 && s1[i - 1] === s2[j - 2] && s1[i - 2] === s2[j - 1]) {
        d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1); // transposition
      }
    }
  }
  return d[l1][l2];
}

function clientSideValidation(query: string): ValidationResult {
  // Regex splitting by tokens preserving internal hyphens
  const tokens = query.match(/[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*|[^a-zA-Z0-9\s]+|\s+/g) || [];
  const corrections: string[] = [];
  const foundTerms: string[] = [];
  const details: MedicalTermDetail[] = [];
  let correctedText = '';

  for (const token of tokens) {
    if (!/[a-zA-Z0-9]/.test(token)) {
      correctedText += token;
      continue;
    }

    const cleanWord = token.trim().toLowerCase();

    // 1. If valid English word, never alter
    if (COMMON_ENGLISH_WORDS.has(cleanWord)) {
      correctedText += token;
      if (CLIENT_MEDICAL_DICT[cleanWord] && !foundTerms.includes(cleanWord)) {
        foundTerms.push(cleanWord);
        const entry = CLIENT_MEDICAL_DICT[cleanWord];
        details.push({
          term: cleanWord,
          standard: entry.standard,
          category: entry.category,
          snomed_id: entry.snomed_id,
        });
      }
      continue;
    }

    // 2. If already valid in medical dictionary
    if (CLIENT_MEDICAL_DICT[cleanWord]) {
      correctedText += token;
      if (!foundTerms.includes(cleanWord)) {
        foundTerms.push(cleanWord);
        const entry = CLIENT_MEDICAL_DICT[cleanWord];
        details.push({
          term: cleanWord,
          standard: entry.standard,
          category: entry.category,
          snomed_id: entry.snomed_id,
        });
      }
      continue;
    }

    // 3. Direct explicit typo lookup
    if (EXPLICIT_TYPOS[cleanWord]) {
      const replacement = EXPLICIT_TYPOS[cleanWord];
      correctedText += replacement;
      corrections.push(`${token} -> ${replacement}`);
      if (CLIENT_MEDICAL_DICT[replacement] && !foundTerms.includes(replacement)) {
        foundTerms.push(replacement);
        const entry = CLIENT_MEDICAL_DICT[replacement];
        details.push({
          term: replacement,
          standard: entry.standard,
          category: entry.category,
          snomed_id: entry.snomed_id,
        });
      }
      continue;
    }

    // 4. Fuzzy typo correction for unknown tokens
    if (cleanWord.length >= 4) {
      let bestCandidate = '';
      let bestDist = 999;

      for (const term of Object.keys(CLIENT_MEDICAL_DICT)) {
        const lenDiff = Math.abs(cleanWord.length - term.length);
        if (cleanWord.length <= 5 && lenDiff > 1) continue;
        if (lenDiff > 2) continue;

        const dist = damerauLevenshtein(cleanWord, term);
        const maxDist = cleanWord.length <= 6 ? 1 : 2;
        if (dist <= maxDist && dist < bestDist) {
          bestDist = dist;
          bestCandidate = term;
        }
      }

      if (bestCandidate && bestDist <= (cleanWord.length <= 6 ? 1 : 2)) {
        correctedText += bestCandidate;
        corrections.push(`${token} -> ${bestCandidate}`);
        if (!foundTerms.includes(bestCandidate)) {
          foundTerms.push(bestCandidate);
          const entry = CLIENT_MEDICAL_DICT[bestCandidate];
          details.push({
            term: bestCandidate,
            standard: entry.standard,
            category: entry.category,
            snomed_id: entry.snomed_id,
          });
        }
        continue;
      }
    }

    correctedText += token;
  }

  const hasCorrections = corrections.length > 0;

  return {
    original: query,
    corrected: hasCorrections ? correctedText : query,
    is_valid: !hasCorrections,
    corrections_made: corrections,
    confidence_score: hasCorrections ? 0.98 : 1.0,
    medical_terms_found: foundTerms,
    medical_terms_details: details,
    issues: hasCorrections ? ['Medical misspelling detected'] : [],
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

    const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
    const endpoints = [
      '/api/v1/validate-query',
      `${apiUrl}/api/v1/validate-query`,
      'http://localhost:8001/validate-query',
    ];

    for (const url of endpoints) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 1500);

        const response = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query }),
          signal: controller.signal,
        });
        clearTimeout(timeoutId);

        if (response.ok) {
          const rawData = await response.json();
          const correctionsMade: string[] = Array.isArray(rawData.corrections_made) && rawData.corrections_made.length > 0
            ? rawData.corrections_made
            : Array.isArray(rawData.corrections) && rawData.corrections.length > 0
            ? rawData.corrections.map((c: any) => `${c.original_word || c.original} -> ${c.corrected_word || c.corrected}`)
            : [];

          const data: ValidationResult = {
            ...rawData,
            original: rawData.original || query,
            corrected: rawData.corrected || query,
            is_valid: rawData.is_valid !== undefined ? Boolean(rawData.is_valid) : correctionsMade.length === 0,
            corrections_made: correctionsMade,
            confidence_score: typeof rawData.confidence_score === 'number'
              ? rawData.confidence_score
              : typeof rawData.confidence === 'number'
              ? rawData.confidence
              : 1.0,
            medical_terms_found: Array.isArray(rawData.medical_terms_found) ? rawData.medical_terms_found : [],
            issues: Array.isArray(rawData.issues) ? rawData.issues : [],
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
