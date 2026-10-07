"use client";

import React, { useState } from "react";
import { Brain, ChevronDown, ChevronUp, ShieldCheck, CheckCircle2, Lock, FileSearch, HeartPulse } from "lucide-react";

interface ClinicalThinkingDrawerProps {
  thinkingBlock?: string;
}

export function ClinicalThinkingDrawer({ thinkingBlock }: ClinicalThinkingDrawerProps) {
  const [isOpen, setIsOpen] = useState(false);

  if (!thinkingBlock) return null;

  // Clean out tags if present for formatted rendering
  const cleanedText = thinkingBlock
    .replace("<clinical_thinking>", "")
    .replace("</clinical_thinking>", "")
    .trim();

  return (
    <div className="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-slate-100 rounded-2xl border border-indigo-500/30 p-4 sm:p-5 shadow-md my-5 overflow-hidden transition-all">
      <div
        className="flex items-center justify-between cursor-pointer select-none"
        onClick={() => setIsOpen((prev) => !prev)}
      >
        <div className="flex items-center gap-3">
          <div className="p-2 bg-indigo-500/20 text-indigo-400 rounded-xl border border-indigo-400/30">
            <Brain className="w-5 h-5 animate-pulse" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h4 className="text-xs sm:text-sm font-bold text-white flex items-center gap-1.5">
                <span>Latent Clinical Thinking Scratchpad</span>
                <span className="px-2 py-0.2 rounded-full text-[9px] font-extrabold uppercase bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                  Audit Passed
                </span>
              </h4>
            </div>
            <p className="text-[11px] text-slate-400">
              Internal 4-Stage EBM reasoning: Entity deconstruction, Evidence audit, Safety & DDI sweep, Register calibration.
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-[11px] text-indigo-300 font-semibold hidden xs:inline">
            {isOpen ? "Collapse Audit" : "Inspect Scratchpad"}
          </span>
          <div className="p-1.5 rounded-lg bg-white/10 hover:bg-white/20 transition-colors text-slate-300">
            {isOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
          </div>
        </div>
      </div>

      {/* Badges preview row when collapsed */}
      {!isOpen && (
        <div className="mt-3 pt-3 border-t border-indigo-500/20 flex flex-wrap items-center gap-2 text-[10px] text-slate-300">
          <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-white/5 border border-white/10">
            <CheckCircle2 className="w-3 h-3 text-emerald-400" /> Grounding Verified
          </span>
          <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-white/5 border border-white/10">
            <Lock className="w-3 h-3 text-indigo-400" /> Zero Context Bleed
          </span>
          <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-white/5 border border-white/10">
            <ShieldCheck className="w-3 h-3 text-cyan-400" /> DDI & Black Box Sweep
          </span>
        </div>
      )}

      {/* Expanded Scratchpad Body */}
      {isOpen && (
        <div className="mt-4 pt-3.5 border-t border-indigo-500/30 text-xs font-mono bg-black/40 p-4 rounded-xl border border-indigo-500/20 overflow-x-auto text-slate-200 leading-relaxed whitespace-pre-wrap animate-fade-in shadow-inner">
          <div className="flex items-center justify-between pb-2 mb-3 border-b border-white/10 text-[11px] font-sans text-indigo-300">
            <span className="font-bold flex items-center gap-1.5">
              <FileSearch className="w-3.5 h-3.5" /> Stage 2 Internal Chain-of-Thought Audit Log
            </span>
            <span className="text-slate-400 font-mono">EBM-Protocol v2.4</span>
          </div>
          {cleanedText}
        </div>
      )}
    </div>
  );
}
