"use client";

import React, { useState } from "react";
import { DoctorQuestion } from "@/lib/types";
import { CheckCircle2, Circle, Stethoscope, Copy, Check, Sparkles, Activity, ShieldAlert, Zap, Info } from "lucide-react";

interface DoctorChecklistProps {
  questions: DoctorQuestion[];
}

export function DoctorChecklist({ questions }: DoctorChecklistProps) {
  const [checkedIds, setCheckedIds] = useState<Record<number, boolean>>({});
  const [copied, setCopied] = useState(false);
  const [expandedRationale, setExpandedRationale] = useState<Record<number, boolean>>({});

  if (!questions || questions.length === 0) return null;

  const toggleCheck = (idx: number, e: React.MouseEvent) => {
    e.stopPropagation();
    setCheckedIds((prev) => ({
      ...prev,
      [idx]: !prev[idx],
    }));
  };

  const toggleRationale = (idx: number, e: React.MouseEvent) => {
    e.stopPropagation();
    setExpandedRationale((prev) => ({
      ...prev,
      [idx]: !prev[idx],
    }));
  };

  const handleCopyQuestions = () => {
    const textToCopy = questions
      .map((q, i) => `${i + 1}. [${q.psa_type ? q.psa_type.toUpperCase() : 'P-S-A'}: ${q.category}] ${q.question}${q.rationale ? ` (Rationale: ${q.rationale})` : ''}`)
      .join("\n\n");
    navigator.clipboard.writeText(textToCopy);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const getPsaBadge = (type?: string) => {
    const t = (type || "").toLowerCase();
    if (t === "parameter") {
      return (
        <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-extrabold uppercase tracking-wider bg-blue-50 text-blue-700 border border-blue-200">
          <Activity className="w-3 h-3 text-blue-600" />
          <span>P • Parameter</span>
        </span>
      );
    }
    if (t === "safety") {
      return (
        <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-extrabold uppercase tracking-wider bg-amber-50 text-amber-800 border border-amber-200">
          <ShieldAlert className="w-3 h-3 text-amber-600" />
          <span>S • Safety</span>
        </span>
      );
    }
    return (
      <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-extrabold uppercase tracking-wider bg-emerald-50 text-emerald-800 border border-emerald-200">
        <Zap className="w-3 h-3 text-emerald-600" />
        <span>A • Action</span>
      </span>
    );
  };

  return (
    <div className="bg-white border border-slate-200/80 rounded-2xl p-5 sm:p-6 my-6 shadow-sm">
      <div className="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3.5 border-b border-slate-100">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-xl border border-indigo-100 shadow-2xs">
            <Stethoscope className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm sm:text-base font-bold text-slate-900 flex items-center gap-1.5">
                <span>Doctor Consultation Checklist</span>
                <Sparkles className="w-4 h-4 text-indigo-500" />
              </h3>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-50 text-indigo-700 border border-indigo-200">
                P-S-A Framework
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              Structured discussion points: Parameter baseline, Safety checks, and Shared Decision Actions.
            </p>
          </div>
        </div>

        <button
          type="button"
          onClick={handleCopyQuestions}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200 text-xs font-semibold transition-all shadow-2xs"
        >
          {copied ? (
            <>
              <Check className="w-3.5 h-3.5 text-emerald-600" />
              <span className="text-emerald-700">Copied to Clipboard!</span>
            </>
          ) : (
            <>
              <Copy className="w-3.5 h-3.5 text-slate-500" />
              <span>Copy Checklist</span>
            </>
          )}
        </button>
      </div>

      <div className="space-y-3">
        {questions.map((q, idx) => {
          const isChecked = !!checkedIds[idx];
          const isRationaleOpen = !!expandedRationale[idx];
          return (
            <div
              key={idx}
              onClick={(e) => toggleCheck(idx, e)}
              className={`p-4 rounded-xl border transition-all cursor-pointer select-none ${
                isChecked
                  ? "bg-slate-50/80 border-slate-200 text-slate-400 shadow-none"
                  : "bg-white hover:bg-indigo-50/20 border-slate-200/90 hover:border-indigo-200 text-slate-800 shadow-2xs"
              }`}
            >
              <div className="flex items-start gap-3">
                <div className="mt-0.5 flex-shrink-0">
                  {isChecked ? (
                    <CheckCircle2 className="w-4 h-4 text-emerald-500" />
                  ) : (
                    <Circle className="w-4 h-4 text-slate-300" />
                  )}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex flex-wrap items-center gap-1.5 mb-1.5">
                    {getPsaBadge(q.psa_type)}
                    <span className="inline-block px-2 py-0.5 bg-slate-100 text-slate-700 border border-slate-200 text-[10px] font-semibold rounded-md uppercase tracking-wider">
                      {q.category}
                    </span>
                  </div>

                  <p className={`text-xs sm:text-sm leading-relaxed ${isChecked ? "line-through text-slate-400" : "font-medium text-slate-900"}`}>
                    {q.question}
                  </p>

                  {q.rationale && (
                    <div className="mt-2 pt-2 border-t border-slate-100">
                      <button
                        type="button"
                        onClick={(e) => toggleRationale(idx, e)}
                        className="inline-flex items-center gap-1 text-[11px] font-medium text-indigo-600 hover:text-indigo-800 transition-colors"
                      >
                        <Info className="w-3 h-3 text-indigo-500" />
                        <span>{isRationaleOpen ? "Hide Clinical Context" : "Why ask this? (Clinical Rationale)"}</span>
                      </button>

                      {isRationaleOpen && (
                        <p className="mt-1 text-[11px] text-slate-600 bg-slate-50/90 p-2.5 rounded-lg border border-slate-200/80 leading-normal animate-fade-in">
                          <strong>Clinical Context:</strong> {q.rationale}
                        </p>
                      )}
                    </div>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
