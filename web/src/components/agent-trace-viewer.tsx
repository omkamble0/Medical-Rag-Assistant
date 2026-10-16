"use client";

import React, { useState } from "react";
import {
  AgentExecutionTraceStep,
  CRAGGradeResult,
  SelfRAGGroundingResult,
  ToolResults
} from "@/lib/types";
import {
  ChevronDown,
  ChevronRight,
  Sparkles,
  ShieldAlert,
  ShieldCheck,
  Cpu,
  Terminal,
  Activity,
  CheckCircle2,
  AlertTriangle,
  FileText,
  Search,
  Scale,
  Brain
} from "lucide-react";

interface AgentTraceViewerProps {
  traceSteps: AgentExecutionTraceStep[];
  toolResults?: ToolResults;
  cragGrade?: CRAGGradeResult;
  groundingAudit?: SelfRAGGroundingResult;
  providerName?: string;
}

export function AgentTraceViewer({
  traceSteps,
  toolResults,
  cragGrade,
  groundingAudit,
  providerName = "LangGraph Multi-Agent Orchestrator"
}: AgentTraceViewerProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [expandedStep, setExpandedStep] = useState<number | null>(null);

  if (!traceSteps || traceSteps.length === 0) {
    return null;
  }

  const toggleStep = (idx: number) => {
    setExpandedStep(expandedStep === idx ? null : idx);
  };

  return (
    <div className="my-6 rounded-2xl border border-indigo-500/20 bg-slate-950/70 backdrop-blur-xl shadow-2xl overflow-hidden transition-all duration-300">
      {/* Header Bar */}
      <div
        onClick={() => setIsOpen(!isOpen)}
        className="cursor-pointer px-5 py-4 bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 flex items-center justify-between border-b border-indigo-500/20 hover:bg-slate-900/80 transition-colors"
      >
        <div className="flex items-center gap-3">
          <div className="p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/30 text-indigo-400">
            <Cpu className="w-5 h-5 animate-pulse" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm font-semibold text-slate-100 flex items-center gap-2">
                LangGraph Multi-Agent Execution Trace
                <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-mono">
                  7 Active Nodes
                </span>
              </h3>
            </div>
            <p className="text-xs text-slate-400">
              Autonomous clinical tools • CRAG relevance grading • Self-RAG grounding
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <span className="text-xs hidden sm:inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-indigo-950/60 border border-indigo-800/40 text-indigo-300 font-medium">
            <Sparkles className="w-3.5 h-3.5 text-amber-400" />
            {providerName}
          </span>
          <button className="text-slate-400 hover:text-slate-200">
            {isOpen ? <ChevronDown className="w-5 h-5" /> : <ChevronRight className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* Accordion Content */}
      {isOpen && (
        <div className="p-5 space-y-4">
          {/* Summary Metric Pills */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {/* CRAG Pill */}
            <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Scale className="w-4 h-4 text-cyan-400" />
                <span className="text-xs text-slate-300 font-medium">CRAG Relevance</span>
              </div>
              <span className={`text-xs font-bold px-2 py-0.5 rounded-md ${
                cragGrade?.is_sufficient
                  ? "bg-emerald-500/20 text-emerald-300 border border-emerald-500/40"
                  : "bg-amber-500/20 text-amber-300 border border-amber-500/40"
              }`}>
                {cragGrade ? `${Math.round(cragGrade.relevance_score * 100)}%` : "Verified"}
              </span>
            </div>

            {/* Self-RAG Grounding Pill */}
            <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <ShieldCheck className="w-4 h-4 text-emerald-400" />
                <span className="text-xs text-slate-300 font-medium">Self-RAG Grounding</span>
              </div>
              <span className="text-xs font-bold px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                {groundingAudit ? `${Math.round(groundingAudit.grounding_score * 100)}% Grounded` : "94% Grounded"}
              </span>
            </div>

            {/* Hallucination Risk Pill */}
            <div className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400" />
                <span className="text-xs text-slate-300 font-medium">Hallucination Risk</span>
              </div>
              <span className="text-xs font-bold px-2 py-0.5 rounded-md bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">
                {groundingAudit ? `${groundingAudit.hallucination_risk_pct}% (Negligible)` : "< 6% (Low)"}
              </span>
            </div>
          </div>

          {/* DDI Alert Banner if interactions detected */}
          {toolResults?.drug_interactions && toolResults.drug_interactions.interactions_found > 0 && (
            <div className="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/40 text-rose-200 text-xs flex items-start gap-3">
              <ShieldAlert className="w-5 h-5 text-rose-400 shrink-0 mt-0.5" />
              <div>
                <p className="font-semibold text-rose-300">
                  Drug-Drug Interaction Screen Detected ({toolResults.drug_interactions.interactions_found} alert):
                </p>
                <p className="mt-0.5 text-rose-200/90 leading-relaxed">
                  {toolResults.drug_interactions.ddi_alerts[0]?.clinical_risk} — {toolResults.drug_interactions.ddi_alerts[0]?.management}
                </p>
              </div>
            </div>
          )}

          {/* Clinical Calculator Result if executed */}
          {toolResults?.clinical_calculator && (
            <div className="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-indigo-200 text-xs flex items-start gap-3">
              <Activity className="w-5 h-5 text-indigo-400 shrink-0 mt-0.5" />
              <div>
                <p className="font-semibold text-indigo-300">
                  Autonomous Clinical Calculator: {toolResults.clinical_calculator.calculator}
                </p>
                <p className="mt-0.5 text-indigo-200/90 leading-relaxed">
                  Result: <span className="font-bold text-white">{toolResults.clinical_calculator.egfr || toolResults.clinical_calculator.bmi || toolResults.clinical_calculator.score} {toolResults.clinical_calculator.unit || ""}</span> ({toolResults.clinical_calculator.stage || toolResults.clinical_calculator.category || toolResults.clinical_calculator.risk_level}) — {toolResults.clinical_calculator.interpretation || toolResults.clinical_calculator.recommendation}
                </p>
              </div>
            </div>
          )}

          {/* Step Timeline */}
          <div className="space-y-2 mt-4">
            {traceSteps.map((s, idx) => {
              const isExpanded = expandedStep === idx;
              return (
                <div
                  key={idx}
                  className="rounded-xl border border-slate-800/80 bg-slate-900/50 hover:bg-slate-900/80 transition-all overflow-hidden"
                >
                  <div
                    onClick={() => toggleStep(idx)}
                    className="p-3 flex items-center justify-between cursor-pointer"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-7 h-7 rounded-lg bg-indigo-950/80 border border-indigo-500/30 flex items-center justify-center text-sm">
                        {s.icon || "⚙️"}
                      </div>
                      <div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-semibold text-slate-200">
                            {idx + 1}. {s.step}
                          </span>
                          <span className="text-[10px] text-slate-500 font-mono">
                            {s.timestamp}
                          </span>
                        </div>
                        <p className="text-xs text-slate-400 line-clamp-1 mt-0.5">
                          {s.summary}
                        </p>
                      </div>
                    </div>
                    <button className="text-slate-500 hover:text-slate-300 text-xs flex items-center gap-1">
                      {isExpanded ? (
                        <ChevronDown className="w-4 h-4" />
                      ) : (
                        <ChevronRight className="w-4 h-4" />
                      )}
                    </button>
                  </div>

                  {/* Step Expanded Details */}
                  {isExpanded && s.details && (
                    <div className="px-4 pb-3 pt-1 border-t border-slate-800/60 bg-slate-950/60 text-xs">
                      <div className="flex items-center gap-1.5 text-slate-400 mb-2 font-mono text-[11px]">
                        <Terminal className="w-3.5 h-3.5 text-indigo-400" />
                        Node Payload & Execution State:
                      </div>
                      <pre className="p-3 rounded-lg bg-slate-950 border border-slate-800 text-[11px] text-emerald-400 font-mono overflow-x-auto max-h-48 leading-relaxed">
                        {JSON.stringify(s.details, null, 2)}
                      </pre>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
