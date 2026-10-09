'use client';

import { useState, useCallback } from 'react';

export type Audience = 'patient' | 'doctor';

export interface MedicalSource {
  index: number;
  title: string;
  journal: string;
  year: number;
  snippet: string;
}

export interface MedicalQueryResponse {
  status: string;
  original_query?: string;
  effective_query?: string;
  was_corrected?: boolean;
  answer?: string;
  sources?: MedicalSource[];
  audience?: Audience;
  reading_level?: string;
  provider?: string;
  original?: string;
  corrected?: string;
  confidence?: number;
  corrections?: Array<{
    original_word: string;
    corrected_word: string;
    confidence: number;
  }>;
  message?: string;
}

export function useMedicalQuery() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<MedicalQueryResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const normalizeAudience = (audience: string | undefined): Audience => {
    if (!audience) return 'patient';
    const a = audience.trim().toLowerCase();
    if (['doctor', 'clinician', 'professional', 'physician', 'md', 'healthcare_provider'].includes(a)) {
      return 'doctor';
    }
    return 'patient';
  };

  const ask = useCallback(
    async (
      medicalQuery: string,
      audience: string = 'patient',
      autoCorrect: boolean = false
    ): Promise<MedicalQueryResponse> => {
      if (!medicalQuery || !medicalQuery.trim()) {
        const emptyRes: MedicalQueryResponse = { status: 'error', message: 'Query cannot be empty' };
        setResult(emptyRes);
        return emptyRes;
      }

      setLoading(true);
      setError(null);

      try {
        const normalizedAudience = normalizeAudience(audience);
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

        const response = await fetch(`${apiUrl}/api/v1/medical-query`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            query: medicalQuery.trim(),
            audience: normalizedAudience, // ALWAYS 'patient' or 'doctor'
            auto_correct: autoCorrect,
          }),
        });

        if (!response.ok) {
          throw new Error(`API error: ${response.statusText}`);
        }

        const data: MedicalQueryResponse = await response.json();
        setResult(data);
        return data;
      } catch (err: any) {
        const message = err instanceof Error ? err.message : 'Unknown error';
        const errRes: MedicalQueryResponse = {
          status: 'error',
          message: message,
        };
        setError(message);
        setResult(errRes);
        return errRes;
      } finally {
        setLoading(false);
      }
    },
    []
  );

  const validateOnly = useCallback(async (q: string) => {
    if (!q.trim()) return null;
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await fetch(`${apiUrl}/api/v1/validate-query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: q.trim() }),
      });
      if (!res.ok) return null;
      return await res.json();
    } catch {
      return null;
    }
  }, []);

  const clear = useCallback(() => {
    setResult(null);
    setError(null);
  }, []);

  return {
    ask,
    query: ask,
    validateOnly,
    loading,
    result,
    error,
    clear,
    setResult,
  };
}
