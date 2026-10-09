'use client';

import React, { useEffect } from 'react';
import { useQueryValidator, ValidationResult } from '@/hooks/useQueryValidator';
import { 
  Sparkles, 
  CheckCircle2, 
  ArrowRight, 
  ShieldCheck, 
  AlertCircle, 
  Wand2, 
  Activity,
  Stethoscope,
  Pill
} from 'lucide-react';

interface Props {
  query: string;
  onApplyCorrection?: (corrected: string) => void;
  className?: string;
  compact?: boolean;
}

export const QueryValidationComponent: React.FC<Props> = ({
  query,
  onApplyCorrection,
  className = '',
  compact = false,
}) => {
  const { validationResult, isValidating, validateQuery } = useQueryValidator();

  useEffect(() => {
    if (!query || query.trim().length < 3) {
      return;
    }

    const timer = setTimeout(() => {
      validateQuery(query);
    }, 250);

    return () => clearTimeout(timer);
  }, [query, validateQuery]);

  if (!query || !validationResult || query.trim().length < 3) {
    return null;
  }

  const hasCorrections = validationResult.corrections_made && validationResult.corrections_made.length > 0;
  const hasMedicalTerms = validationResult.medical_terms_found && validationResult.medical_terms_found.length > 0;

  // Don't render anything if query is plain text with no corrections and no detected clinical terms
  if (!hasCorrections && !hasMedicalTerms && validationResult.issues.length === 0) {
    return null;
  }

  return (
    <div
      className={`rounded-2xl border transition-all duration-200 overflow-hidden shadow-xs ${
        hasCorrections
          ? 'bg-amber-50/70 border-amber-200/80 text-amber-950'
          : 'bg-indigo-50/50 border-indigo-100 text-slate-800'
      } ${className}`}
    >
      <div className="p-3.5 sm:p-4">
        {/* Header line: Validation Status & Confidence */}
        <div className="flex items-center justify-between gap-2 mb-2">
          <div className="flex items-center gap-2">
            {hasCorrections ? (
              <span className="p-1 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center">
                <Wand2 className="w-4 h-4 animate-pulse" />
              </span>
            ) : (
              <span className="p-1 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center">
                <ShieldCheck className="w-4 h-4" />
              </span>
            )}
            <span className="text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-1.5">
              {hasCorrections ? 'Typo Detected & Medical Normalization' : 'Medical Entity Grounding'}
            </span>
          </div>

          <div className="flex items-center gap-1.5 text-[11px] font-semibold text-slate-500 bg-white/80 px-2.5 py-0.5 rounded-full border border-slate-200/60 shadow-2xs">
            <Activity className="w-3 h-3 text-emerald-600" />
            <span>Confidence: {Math.round(validationResult.confidence_score * 100)}%</span>
          </div>
        </div>

        {/* Typo Correction Prompt (Did you mean?) */}
        {hasCorrections && (
          <div className="mt-2.5 p-3 rounded-xl bg-white border border-amber-200/90 shadow-2xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div className="space-y-1">
              <div className="flex items-center gap-1.5 text-xs text-amber-800 font-medium">
                <span>Did you mean:</span>
                <span className="font-bold text-slate-900 bg-amber-100/70 px-2 py-0.5 rounded-md border border-amber-200">
                  {validationResult.corrected}
                </span>
              </div>
              <div className="flex flex-wrap gap-1.5 pt-0.5">
                {validationResult.corrections_made.map((correction, idx) => (
                  <span
                    key={idx}
                    className="inline-flex items-center gap-1 text-[11px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded-md font-mono"
                  >
                    <span>{correction}</span>
                  </span>
                ))}
              </div>
            </div>

            {onApplyCorrection && (
              <button
                type="button"
                onClick={() => onApplyCorrection(validationResult.corrected)}
                className="self-start sm:self-center flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-amber-600 to-amber-700 hover:from-amber-700 hover:to-amber-800 text-white text-xs font-bold shadow-xs active:scale-95 transition-all flex-shrink-0"
              >
                <span>Use Corrected Query</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        )}

        {/* Medical Terms Found (SNOMED-CT / Clinical Ontology) */}
        {!compact && hasMedicalTerms && (
          <div className="mt-2.5 flex flex-wrap items-center gap-1.5 pt-1">
            <span className="text-[11px] text-slate-500 font-semibold flex items-center gap-1">
              <Stethoscope className="w-3.5 h-3.5 text-indigo-600" />
              Identified Clinical Concepts:
            </span>
            {validationResult.medical_terms_details && validationResult.medical_terms_details.length > 0 ? (
              validationResult.medical_terms_details.map((item, idx) => (
                <span
                  key={idx}
                  className={`inline-flex items-center gap-1 text-xs px-2.5 py-0.5 rounded-lg border font-medium ${
                    item.category === 'medication'
                      ? 'bg-purple-50 border-purple-200 text-purple-700'
                      : item.category === 'symptom'
                      ? 'bg-rose-50 border-rose-200 text-rose-700'
                      : 'bg-blue-50 border-blue-200 text-blue-700'
                  }`}
                  title={`SNOMED CT ID: ${item.snomed_id}`}
                >
                  {item.category === 'medication' && <Pill className="w-3 h-3 text-purple-600" />}
                  {item.category === 'symptom' && <AlertCircle className="w-3 h-3 text-rose-500" />}
                  <span>{item.standard}</span>
                  <span className="text-[9px] opacity-60 uppercase font-mono">[{item.category}]</span>
                </span>
              ))
            ) : (
              validationResult.medical_terms_found.map((term, idx) => (
                <span
                  key={idx}
                  className="text-xs px-2 py-0.5 bg-indigo-50 border border-indigo-200 text-indigo-700 rounded-md font-medium capitalize"
                >
                  {term}
                </span>
              ))
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default QueryValidationComponent;
