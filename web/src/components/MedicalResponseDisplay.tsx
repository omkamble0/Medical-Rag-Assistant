// web/src/components/MedicalResponseDisplay.tsx

'use client';

import React, { useState, useEffect } from 'react';
import { useMedicalSimplifier, SimplifiedResponse } from '@/hooks/useMedicalSimplifier';

interface Props {
  ragResponse: string;
  title?: string;
}

export function MedicalResponseDisplay({ ragResponse, title = 'Medical Response' }: Props) {
  const [audience, setAudience] = useState<'patient' | 'doctor'>('patient');
  const [simplified, setSimplified] = useState<SimplifiedResponse | null>(null);
  const { simplify, loading, error } = useMedicalSimplifier();

  useEffect(() => {
    let isMounted = true;
    const handleSimplification = async () => {
      if (audience === 'patient' && !simplified && ragResponse) {
        try {
          const result = await simplify(ragResponse, audience);
          if (isMounted) {
            setSimplified(result);
          }
        } catch (err) {
          console.error('Simplification error:', err);
        }
      }
    };

    handleSimplification();
    return () => {
      isMounted = false;
    };
  }, [ragResponse, audience, simplified, simplify]);

  const displayText = audience === 'patient' && simplified
    ? simplified.data.simplified
    : ragResponse;

  return (
    <div className="w-full bg-white rounded-lg shadow-md p-6">
      {/* Header */}
      <div className="mb-4">
        <h2 className="text-2xl font-bold text-gray-800">{title}</h2>
        <p className="text-sm text-gray-500 mt-1">
          Choose how you&apos;d like to view this information
        </p>
      </div>

      {/* Audience Selector */}
      <div className="flex gap-4 mb-6">
        <label className="flex items-center cursor-pointer">
          <input
            type="radio"
            name="audience"
            value="patient"
            checked={audience === 'patient'}
            onChange={(e) => {
              setAudience(e.target.value as 'patient' | 'doctor');
            }}
            className="mr-2 w-4 h-4"
          />
          <span className="text-sm font-medium text-gray-700">
            Patient-Friendly View
          </span>
        </label>

        <label className="flex items-center cursor-pointer">
          <input
            type="radio"
            name="audience"
            value="doctor"
            checked={audience === 'doctor'}
            onChange={(e) => {
              setAudience(e.target.value as 'patient' | 'doctor');
            }}
            className="mr-2 w-4 h-4"
          />
          <span className="text-sm font-medium text-gray-700">
            Medical Professional View
          </span>
        </label>
      </div>

      {/* Loading Indicator */}
      {loading && (
        <div className="mb-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-blue-500 rounded-full animate-pulse"></div>
            <span className="text-sm text-blue-700">
              Simplifying medical content for you...
            </span>
          </div>
        </div>
      )}

      {/* Error Display */}
      {error && (
        <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg">
          <p className="text-sm text-red-700 font-medium">Simplification Error</p>
          <p className="text-sm text-red-600 mt-1">{error.message}</p>
        </div>
      )}

      {/* Main Content */}
      <div className={`p-4 rounded-lg border-2 ${
        audience === 'patient' 
          ? 'bg-green-50 border-green-200' 
          : 'bg-blue-50 border-blue-200'
      }`}>
        <div className={`text-sm font-semibold mb-3 ${
          audience === 'patient'
            ? 'text-green-800'
            : 'text-blue-800'
        }`}>
          {audience === 'patient' ? '👤 Explained Simply' : '👨‍⚕️ Clinical Information'}
        </div>
        
        <div className="prose prose-sm max-w-none text-gray-800 leading-relaxed">
          <p>{displayText}</p>
        </div>
      </div>

      {/* Metadata Footer */}
      {simplified && audience === 'patient' && (
        <div className="mt-4 pt-4 border-t border-gray-200 text-xs text-gray-500">
          <p>
            ℹ️ Simplified by MedSiML Model in {simplified.processing_time_ms.toFixed(2)}ms
          </p>
        </div>
      )}

      {audience === 'doctor' && (
        <div className="mt-4 pt-4 border-t border-gray-200 text-xs text-gray-500">
          <p>ℹ️ Full clinical terminology preserved</p>
        </div>
      )}
    </div>
  );
}
