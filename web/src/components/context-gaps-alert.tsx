"use client";

import React from "react";
import { ParsedQueryAnalysis } from "@/lib/types";
import { AlertCircle, FileQuestion, CheckCircle2, ChevronRight, Activity } from "lucide-react";

interface ContextGapsAlertProps {
  analysis?: ParsedQueryAnalysis;
  contextGaps?: string[];
  onSelectClarification?: (query: string) => void;
}

export function ContextGapsAlert({ analysis, contextGaps, onSelectClarification }: ContextGapsAlertProps) {
  const gaps = contextGaps || analysis?.context_gaps || [];
  const missingVars = analysis?.missing_variables || [];
  const clarifications = analysis?.recommended_clarifications || [];

  if (gaps.length === 0 && missingVars.length === 0) return null;

  return (
    <div className="bg-amber-50/80 border border-amber-200/90 rounded-2xl p-4 sm:p-5 my-4 shadow-2xs">
      <div className="flex items-start gap-3">
        <div className="p-2 bg-amber-100 text-amber-800 rounded-xl border border-amber-200 flex-shrink-0 mt-0.5">
          <AlertCircle className="w-5 h-5" />
        </div>
        <div className="flex-1 min-w-0">
          <div className="flex flex-wrap items-center gap-2 mb-1">
            <h4 className="text-xs sm:text-sm font-bold text-amber-950">
              Guideline Variable Dependencies & Context Gaps
            </h4>
            <span className="px-2 py-0.2 rounded-full text-[10px] font-extrabold uppercase tracking-wide bg-amber-200/80 text-amber-900 border border-amber-300">
              Anti-Hallucination Safe Mode
            </span>
          </div>

          <p className="text-xs text-amber-900/90 mb-2 leading-relaxed">
            Medical guidelines require specific baseline lab values or clinical staging before definite recommendations apply:
          </p>

          <ul className="space-y-1.5 mb-3">
            {gaps.map((gap, idx) => (
              <li key={idx} className="text-xs text-amber-950 flex items-start gap-2">
                <span className="text-amber-600 font-bold">•</span>
                <span>{gap}</span>
              </li>
            ))}
          </ul>

          {clarifications.length > 0 && (
            <div className="pt-2.5 border-t border-amber-200/70">
              <span className="text-[11px] font-bold text-amber-900 uppercase tracking-wider block mb-1.5">
                Recommended Query Disambiguations:
              </span>
              <div className="flex flex-wrap gap-1.5">
                {clarifications.map((clar, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => onSelectClarification && onSelectClarification(clar)}
                    className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-white hover:bg-amber-100/70 border border-amber-200 text-[11px] font-semibold text-amber-900 transition-colors shadow-2xs cursor-pointer"
                  >
                    <span>{clar}</span>
                    <ChevronRight className="w-3 h-3 text-amber-600" />
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
