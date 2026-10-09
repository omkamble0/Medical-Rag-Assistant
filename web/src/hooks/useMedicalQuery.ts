'use client';

import { useState, useCallback } from 'react';

export interface MedicalSource {
  index: number;
  title: string;
  journal: string;
  year: number;
  snippet: string;
}

export interface MedicalQueryResponse {
  status: 'ok' | 'needs_correction' | 'error';
  original_query?: string;
  effective_query?: string;
  was_corrected?: boolean;
  answer?: string;
  sources?: MedicalSource[];
  audience?: 'patient' | 'doctor';
  provider?: string;
  // Typo correction fields
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

  const ask = useCallback(
    async (
      query: string,
      audience: 'patient' | 'doctor' = 'patient',
      autoCorrect: boolean = false
    ): Promise<MedicalQueryResponse> => {
      if (!query.trim()) {
        const emptyRes: MedicalQueryResponse = { status: 'error', message: 'Query cannot be empty' };
        setResult(emptyRes);
        return emptyRes;
      }

      setLoading(true);
      setError(null);

      try {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
        const res = await fetch(`${apiUrl}/api/v1/medical-query`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query: query.trim(),
            audience,
            auto_correct: autoCorrect,
          }),
        });

        if (!res.ok) {
          throw new Error(`Server responded with status ${res.status}`);
        }

        const data: MedicalQueryResponse = await res.json();
        setResult(data);
        return data;
      } catch (err: any) {
        const errRes: MedicalQueryResponse = {
          status: 'error',
          message: err.message || 'Failed to communicate with medical RAG backend',
        };
        setError(err.message || 'Network error');
        setResult(errRes);
        return errRes;
      } finally {
        setLoading(false);
      }
    },
    []
  );

  const validateOnly = useCallback(async (query: string) => {
    if (!query.trim()) return null;
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await fetch(`${apiUrl}/api/v1/validate-query`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query.trim() }),
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

  return { ask, validateOnly, loading, result, error, clear, setResult };
}
