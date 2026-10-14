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

  const hasCorrections = Array.isArray(validationResult.corrections_made) && validationResult.corrections_made.length > 0;

  // Only render if a real typo/correction is detected
  if (!hasCorrections) {
    return null;
  }

  return (
    <div className={`mt-2 p-3 rounded-xl bg-amber-50/90 border border-amber-200 text-amber-900 shadow-2xs animate-fade-in ${className}`}>
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5">
        <div className="flex items-center gap-2 text-xs">
          <Wand2 className="w-4 h-4 text-amber-600 flex-shrink-0" />
          <span>Did you mean:</span>
          <span className="font-bold text-slate-900 bg-amber-100 px-2 py-0.5 rounded border border-amber-200">
            {validationResult.corrected}
          </span>
        </div>

        {onApplyCorrection && (
          <button
            type="button"
            onClick={() => onApplyCorrection(validationResult.corrected)}
            className="self-start sm:self-center flex items-center gap-1.5 px-3 py-1 rounded-lg bg-amber-600 hover:bg-amber-700 text-white text-xs font-semibold shadow-2xs transition-all flex-shrink-0"
          >
            <span>Search for &ldquo;{validationResult.corrected}&rdquo;</span>
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        )}
      </div>
    </div>
  );
};

export default QueryValidationComponent;
