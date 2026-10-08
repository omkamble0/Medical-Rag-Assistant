// web/src/hooks/useMedicalSimplifier.ts

'use client';

import { useState, useCallback } from 'react';

export interface SimplifiedResponse {
  success: boolean;
  data: {
    original: string;
    simplified: string;
    audience: string;
    simplification_applied: boolean;
    model_used: string;
    processing_time_ms: number;
    source: string;
  };
  processing_time_ms: number;
  model_version: string;
}

export interface SimplifierError {
  message: string;
  status?: number;
}

export function useMedicalSimplifier() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<SimplifierError | null>(null);
  const [cache, setCache] = useState<Map<string, SimplifiedResponse>>(new Map());

  const getCacheKey = (text: string, audience: string): string => {
    return `${audience}:${text.substring(0, 50)}`;
  };

  const simplify = useCallback(
    async (text: string, audience: 'patient' | 'doctor'): Promise<SimplifiedResponse> => {
      setLoading(true);
      setError(null);

      try {
        // Check cache first
        const cacheKey = getCacheKey(text, audience);
        if (cache.has(cacheKey)) {
          const cachedResult = cache.get(cacheKey)!;
          setLoading(false);
          return cachedResult;
        }

        const response = await fetch('/api/v1/simplify', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            text,
            audience,
            source: 'frontend',
          }),
        });

        if (!response.ok) {
          const errorData = await response.json().catch(() => ({}));
          throw new Error(errorData.detail || 'Simplification failed');
        }

        const data: SimplifiedResponse = await response.json();

        // Cache the result
        setCache(prev => new Map(prev).set(cacheKey, data));

        setLoading(false);
        return data;
      } catch (err) {
        const error: SimplifierError = {
          message: err instanceof Error ? err.message : 'Unknown error',
          status: err instanceof Error ? undefined : 500,
        };
        setError(error);
        setLoading(false);
        throw error;
      }
    },
    [cache]
  );

  const clear = useCallback(() => {
    setCache(new Map());
    setError(null);
  }, []);

  return {
    simplify,
    loading,
    error,
    clear,
  };
}
