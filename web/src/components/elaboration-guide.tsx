"use client";

import React from "react";
import { ElaborationOption } from "@/lib/types";
import { HelpCircle, ArrowRight, Sparkles, Compass, CheckCircle2 } from "lucide-react";

interface ElaborationGuideProps {
  leadings: ElaborationOption[];
  onSelectOption: (query: string) => void;
}

export function ElaborationGuide({ leadings, onSelectOption }: ElaborationGuideProps) {
  if (!leadings || leadings.length === 0) return null;

  return (
    <div className="bg-gradient-to-r from-blue-50/70 via-indigo-50/50 to-white border border-indigo-100 rounded-2xl p-5 sm:p-6 shadow-xs animate-fade-in my-6">
      <div className="flex items-start justify-between gap-3 mb-4 pb-3.5 border-b border-indigo-100/80">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-600 text-white rounded-xl shadow-xs shadow-indigo-200">
            <Compass className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm sm:text-base font-bold text-slate-900">
                Explore Specific Sub-Topics & Guidelines
              </h3>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-100 text-indigo-700 border border-indigo-200">
                Evidence-Guided
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              Select a specialized clinical branch below to get tailored recommendations backed by medical research.
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
        {leadings.map((opt, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => onSelectOption(opt.query)}
            className="group text-left p-4 rounded-xl bg-white hover:bg-indigo-50/60 border border-slate-200/90 hover:border-indigo-300 shadow-2xs hover:shadow-sm transition-all flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-2">
                <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-slate-100 group-hover:bg-indigo-100 text-slate-700 group-hover:text-indigo-700 transition-colors">
                  {opt.health_body}
                </span>
                <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-0.5 transition-all" />
              </div>
              <h4 className="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-indigo-900 mb-1 leading-snug">
                {opt.label}
              </h4>
              <p className="text-[11px] sm:text-xs text-slate-500 line-clamp-2 leading-relaxed">
                {opt.context}
              </p>
            </div>

            <div className="mt-3 pt-2 border-t border-slate-100 flex items-center gap-1 text-[11px] text-indigo-600 font-semibold opacity-90 group-hover:opacity-100">
              <Sparkles className="w-3 h-3" />
              <span>Explore Evidence</span>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
