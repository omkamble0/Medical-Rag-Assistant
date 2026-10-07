"use client";

import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { SearchResponse } from "@/lib/types";
import { ConfidenceRadar } from "./confidence-radar";
import { ElaborationGuide } from "./elaboration-guide";
import { ClinicalThinkingDrawer } from "./clinical-thinking-drawer";
import { ContextGapsAlert } from "./context-gaps-alert";
import {
  Stethoscope, CheckCircle2, FileCheck2, ShieldCheck,
  Layers, FlaskConical, GitCompare, AlertOctagon
} from "lucide-react";

interface ClinicianViewProps {
  response: SearchResponse;
  activeCitation: number | null;
  onSelectCitation: (index: number) => void;
  onSelectElaboration?: (query: string) => void;
}

export function ClinicianView({ response, activeCitation, onSelectCitation, onSelectElaboration }: ClinicianViewProps) {
  // Helper to inject interactive citation badges into text nodes
  const renderInlineCitations = (content: string) => {
    const parts = content.split(/(\[\d+(?:,\s*\d+)*\])/g);
    return parts.map((part, index) => {
      const match = part.match(/^\[(\d+(?:,\s*\d+)*)\]$/);
      if (match) {
        const citationIndices = match[1].split(",").map((s) => parseInt(s.trim(), 10));
        return (
          <span key={index} className="inline-flex gap-1 mx-1 align-baseline">
            {citationIndices.map((citIdx) => (
              <button
                key={citIdx}
                type="button"
                onClick={() => onSelectCitation(citIdx)}
                className={`px-2 py-0.5 rounded text-xs font-mono font-bold transition-all ${
                  activeCitation === citIdx
                    ? "bg-teal-600 text-white ring-2 ring-teal-300 shadow-sm"
                    : "bg-teal-50 hover:bg-teal-100 text-teal-800 border border-teal-200"
                }`}
                title={`Inspect Source [${citIdx}] in Evidence Drawer`}
              >
                [{citIdx}]
              </button>
            ))}
          </span>
        );
      }
      return <span key={index}>{part}</span>;
    });
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Clinician Header Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 p-4 sm:p-5 bg-gradient-to-r from-teal-50/80 via-emerald-50/30 to-white border border-teal-100 rounded-2xl shadow-xs">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-teal-600 text-white rounded-xl shadow-xs shadow-teal-200">
            <Stethoscope className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base sm:text-lg font-bold text-slate-900">
                Clinician Mode (Evidence-Based Synthesis)
              </h3>
              <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-teal-100 text-teal-800 border border-teal-200">
                Post-Graduate
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              Oxford CEBM Grounding, guideline benchmarks & quantitative hazard ratios
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {response.accuracy_score && (
            <div className="flex items-center gap-1.5 text-xs text-teal-800 font-bold bg-teal-50 px-3 py-1.5 rounded-xl border border-teal-200">
              <ShieldCheck className="w-4 h-4 text-teal-600" />
              <span>{response.accuracy_score}% Evidentiary Accuracy</span>
            </div>
          )}
          <div className="flex items-center gap-2 text-xs font-mono font-medium text-slate-600 bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-2xs">
            <FileCheck2 className="w-3.5 h-3.5 text-teal-600" />
            <span>Latency: {response.latency_ms}ms</span>
          </div>
        </div>
      </div>

      {/* Stage 1 Inbound Context Gaps & Missing Variables Alert */}
      {(response.context_gaps || response.query_analysis?.context_gaps) && (
        <ContextGapsAlert
          analysis={response.query_analysis}
          contextGaps={response.context_gaps}
          onSelectClarification={onSelectElaboration}
        />
      )}

      {/* Stage 2 Latent Clinical Thinking Scratchpad Audit */}
      {response.clinical_thinking && (
        <ClinicalThinkingDrawer thinkingBlock={response.clinical_thinking} />
      )}

      {/* Confidence Radar */}
      <ConfidenceRadar metrics={response.confidence} />

      {/* Smart Elaboration Guide */}
      {response.elaboration_leadings && onSelectElaboration && (
        <ElaborationGuide
          leadings={response.elaboration_leadings}
          onSelectOption={onSelectElaboration}
        />
      )}

      {/* Clinical Synthesized Content Card with ReactMarkdown */}
      <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-8 shadow-sm leading-relaxed text-slate-800 text-sm sm:text-[15px]">
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            h1: ({ children }) => (
              <h1 className="text-lg font-bold text-teal-950 uppercase tracking-wide mt-5 mb-2 flex items-center gap-2 border-b border-slate-100 pb-1">
                <CheckCircle2 className="w-4 h-4 text-teal-600" />
                <span>{children}</span>
              </h1>
            ),
            h2: ({ children }) => (
              <h2 className="text-base font-bold text-teal-950 uppercase tracking-wide mt-5 mb-2 flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-teal-600" />
                <span>{children}</span>
              </h2>
            ),
            h3: ({ children }) => (
              <div className="mt-6 mb-2.5 p-2.5 rounded-lg bg-teal-50/60 border border-teal-100 flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-teal-600 shrink-0" />
                <h3 className="text-sm sm:text-base font-bold text-teal-950 uppercase tracking-wider">
                  {children}
                </h3>
              </div>
            ),
            p: ({ children }) => {
              if (typeof children === "string") {
                return <p className="mb-3 leading-relaxed">{renderInlineCitations(children)}</p>;
              }
              return <div className="mb-3 leading-relaxed">{children}</div>;
            },
            ul: ({ children }) => (
              <ul className="space-y-1.5 mb-3 list-disc list-inside text-slate-700">
                {children}
              </ul>
            ),
            li: ({ children }) => (
              <li className="leading-relaxed pl-1">
                {typeof children === "string" ? renderInlineCitations(children) : children}
              </li>
            ),
            strong: ({ children }) => (
              <strong className="font-semibold text-slate-900">
                {children}
              </strong>
            ),
            em: ({ children }) => (
              <em className="text-slate-600 text-xs italic">
                {children}
              </em>
            ),
            code: ({ children }) => (
              <code className="px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 text-xs font-mono">
                {children}
              </code>
            )
          }}
        >
          {response.answer}
        </ReactMarkdown>
      </div>

      {/* Structured Clinician Suggestions (Subgroups, Titration, Guidelines, Contraindications) */}
      {response.clinician_suggestions && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Trial Subgroups */}
          {response.clinician_suggestions.trial_subgroup_analyses.length > 0 && (
            <div className="bg-slate-50 border border-slate-200/90 rounded-xl p-4 shadow-2xs">
              <div className="flex items-center gap-2 mb-2.5 text-teal-900 font-bold text-xs uppercase tracking-wider">
                <Layers className="w-4 h-4 text-teal-600" />
                <span>Trial Subgroup Analyses</span>
              </div>
              <ul className="space-y-1.5 text-xs text-slate-700">
                {response.clinician_suggestions.trial_subgroup_analyses.map((item, idx) => (
                  <li key={idx} className="flex items-start gap-1.5">
                    <span className="text-teal-600 font-bold">•</span>
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Titration Protocols */}
          {response.clinician_suggestions.titration_protocols.length > 0 && (
            <div className="bg-slate-50 border border-slate-200/90 rounded-xl p-4 shadow-2xs">
              <div className="flex items-center gap-2 mb-2.5 text-teal-900 font-bold text-xs uppercase tracking-wider">
                <FlaskConical className="w-4 h-4 text-teal-600" />
                <span>Titration & Escalation Protocol</span>
              </div>
              <ul className="space-y-1.5 text-xs text-slate-700">
                {response.clinician_suggestions.titration_protocols.map((item, idx) => (
                  <li key={idx} className="flex items-start gap-1.5">
                    <span className="text-teal-600 font-bold">•</span>
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Guideline Comparisons */}
          {response.clinician_suggestions.guideline_comparisons.length > 0 && (
            <div className="bg-slate-50 border border-slate-200/90 rounded-xl p-4 shadow-2xs">
              <div className="flex items-center gap-2 mb-2.5 text-teal-900 font-bold text-xs uppercase tracking-wider">
                <GitCompare className="w-4 h-4 text-teal-600" />
                <span>Cross-Guideline Alignment</span>
              </div>
              <ul className="space-y-1.5 text-xs text-slate-700">
                {response.clinician_suggestions.guideline_comparisons.map((item, idx) => (
                  <li key={idx} className="flex items-start gap-1.5">
                    <span className="text-teal-600 font-bold">•</span>
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Contraindications & Interactions */}
          {response.clinician_suggestions.contraindications_interactions.length > 0 && (
            <div className="bg-rose-50/50 border border-rose-200/80 rounded-xl p-4 shadow-2xs">
              <div className="flex items-center gap-2 mb-2.5 text-rose-950 font-bold text-xs uppercase tracking-wider">
                <AlertOctagon className="w-4 h-4 text-rose-600" />
                <span>Contraindications & CYP Interactions</span>
              </div>
              <ul className="space-y-1.5 text-xs text-slate-700">
                {response.clinician_suggestions.contraindications_interactions.map((item, idx) => (
                  <li key={idx} className="flex items-start gap-1.5">
                    <span className="text-rose-600 font-bold">•</span>
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
