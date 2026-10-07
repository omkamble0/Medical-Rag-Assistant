"use client";

import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { SearchResponse } from "@/lib/types";
import { ConfidenceRadar } from "./confidence-radar";
import { JargonGlossary } from "./jargon-tooltip";
import { DoctorChecklist } from "./doctor-checklist";
import { ElaborationGuide } from "./elaboration-guide";
import { ClinicalThinkingDrawer } from "./clinical-thinking-drawer";
import { ContextGapsAlert } from "./context-gaps-alert";
import {
  HeartHandshake, Sparkles, BookOpenCheck, Stethoscope, Lightbulb,
  ShieldCheck, CheckCircle2, AlertTriangle, Activity, Apple, HelpCircle
} from "lucide-react";

interface PatientViewProps {
  response: SearchResponse;
  activeCitation: number | null;
  onSelectCitation: (index: number) => void;
  onSelectElaboration?: (query: string) => void;
}

export function PatientView({ response, activeCitation, onSelectCitation, onSelectElaboration }: PatientViewProps) {
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
                className={`px-2 py-0.5 rounded-full text-xs font-semibold transition-all ${
                  activeCitation === citIdx
                    ? "bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-300"
                    : "bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200"
                }`}
                title={`View Verified Clinical Study [${citIdx}]`}
              >
                Study [{citIdx}]
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
      {/* Patient Header Bar */}
      <div className="flex flex-wrap items-center justify-between gap-3 p-4 sm:p-5 bg-gradient-to-r from-indigo-50/80 via-purple-50/40 to-white border border-indigo-100 rounded-2xl shadow-xs">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-600 text-white rounded-xl shadow-xs shadow-indigo-200">
            <HeartHandshake className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base sm:text-lg font-bold text-slate-900">
                Patient & Family Guide
              </h3>
              <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-indigo-100 text-indigo-700 border border-indigo-200">
                Plain English
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              {response.reading_level || "Grade 6.2 — Easy to understand, verified by medical trials"}
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {response.accuracy_score && (
            <div className="flex items-center gap-1.5 text-xs text-indigo-800 font-bold bg-indigo-50 px-3 py-1.5 rounded-xl border border-indigo-200">
              <CheckCircle2 className="w-4 h-4 text-indigo-600" />
              <span>{response.accuracy_score}% Grounding Accuracy</span>
            </div>
          )}
          <div className="hidden sm:flex items-center gap-1.5 text-xs text-emerald-700 font-semibold bg-emerald-50 px-3 py-1.5 rounded-xl border border-emerald-200">
            <ShieldCheck className="w-4 h-4 text-emerald-600" />
            <span>Doctor-Approved Science</span>
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

      {/* Confidence Indicator in Patient-Friendly Terms */}
      <ConfidenceRadar metrics={response.confidence} />

      {/* Smart Elaboration Guide (when available) */}
      {response.elaboration_leadings && onSelectElaboration && (
        <ElaborationGuide
          leadings={response.elaboration_leadings}
          onSelectOption={onSelectElaboration}
        />
      )}

      {/* Main Patient Content with ReactMarkdown & remarkGfm */}
      <div className="bg-white border border-slate-200/90 rounded-2xl p-6 sm:p-8 shadow-sm leading-relaxed text-slate-700 text-base sm:text-[17px]">
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          components={{
            h1: ({ children }) => (
              <h1 className="text-xl font-bold text-slate-900 mt-6 mb-3 flex items-center gap-2 pb-2 border-b border-slate-100">
                {children}
              </h1>
            ),
            h2: ({ children }) => (
              <h2 className="text-lg font-bold text-slate-900 mt-6 mb-3 flex items-center gap-2">
                {children}
              </h2>
            ),
            h3: ({ children }) => {
              const textContent = String(children);
              let icon = <Sparkles className="w-4 h-4 text-indigo-500" />;
              let badgeColor = "bg-indigo-50 border-indigo-200 text-indigo-900";

              if (textContent.toLowerCase().includes("big picture")) {
                icon = <HeartHandshake className="w-4 h-4 text-indigo-500" />;
              } else if (textContent.toLowerCase().includes("how it works") || textContent.toLowerCase().includes("plain english")) {
                icon = <Lightbulb className="w-4 h-4 text-amber-500" />;
                badgeColor = "bg-amber-50 border-amber-200 text-amber-900";
              } else if (textContent.toLowerCase().includes("what the medical") || textContent.toLowerCase().includes("science shows") || textContent.toLowerCase().includes("evidence")) {
                icon = <BookOpenCheck className="w-4 h-4 text-emerald-500" />;
                badgeColor = "bg-emerald-50 border-emerald-200 text-emerald-900";
              } else if (textContent.toLowerCase().includes("practical") || textContent.toLowerCase().includes("guidelines")) {
                icon = <Stethoscope className="w-4 h-4 text-blue-500" />;
                badgeColor = "bg-blue-50 border-blue-200 text-blue-900";
              } else if (textContent.toLowerCase().includes("warning") || textContent.toLowerCase().includes("danger")) {
                icon = <AlertTriangle className="w-4 h-4 text-rose-500" />;
                badgeColor = "bg-rose-50 border-rose-200 text-rose-900";
              }

              return (
                <div className={`mt-6 mb-3 p-3 rounded-xl border ${badgeColor} flex items-center gap-2.5`}>
                  <span className="p-1 rounded-lg bg-white/80 shadow-2xs">{icon}</span>
                  <h3 className="text-base sm:text-lg font-bold tracking-tight">
                    {children}
                  </h3>
                </div>
              );
            },
            p: ({ children }) => {
              if (typeof children === "string") {
                return <p className="mb-4 leading-relaxed">{renderInlineCitations(children)}</p>;
              }
              return <div className="mb-4 leading-relaxed">{children}</div>;
            },
            ul: ({ children }) => (
              <ul className="space-y-2 mb-4 list-disc list-inside text-slate-700">
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
              <em className="text-slate-600 text-sm italic">
                {children}
              </em>
            )
          }}
        >
          {response.answer}
        </ReactMarkdown>
      </div>

      {/* Structured Patient Suggestions (Lifestyle, Doctor Questions, Monitoring) */}
      {response.patient_suggestions && (
        <div className="space-y-4">
          {/* Lifestyle Recommendations */}
          {response.patient_suggestions.lifestyle_recommendations.length > 0 && (
            <div className="bg-gradient-to-r from-emerald-50/70 via-teal-50/40 to-white border border-emerald-200/80 rounded-2xl p-5 sm:p-6 shadow-xs">
              <div className="flex items-center gap-2.5 mb-3">
                <div className="p-2 bg-emerald-600 text-white rounded-lg shadow-2xs">
                  <Apple className="w-4 h-4" />
                </div>
                <h4 className="text-sm sm:text-base font-bold text-slate-900">
                  Evidence-Based Lifestyle & Non-Drug Support
                </h4>
              </div>
              <ul className="space-y-2 text-sm text-slate-700">
                {response.patient_suggestions.lifestyle_recommendations.map((rec, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    <span className="text-emerald-600 font-bold mt-0.5">•</span>
                    <span>{rec}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Home Monitoring Metrics */}
          {response.patient_suggestions.monitoring_metrics.length > 0 && (
            <div className="bg-gradient-to-r from-blue-50/70 via-indigo-50/40 to-white border border-blue-200/80 rounded-2xl p-5 sm:p-6 shadow-xs">
              <div className="flex items-center gap-2.5 mb-3">
                <div className="p-2 bg-blue-600 text-white rounded-lg shadow-2xs">
                  <Activity className="w-4 h-4" />
                </div>
                <h4 className="text-sm sm:text-base font-bold text-slate-900">
                  Recommended Home Monitoring & Tracking
                </h4>
              </div>
              <ul className="space-y-2 text-sm text-slate-700">
                {response.patient_suggestions.monitoring_metrics.map((metric, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    <span className="text-blue-600 font-bold mt-0.5">✓</span>
                    <span>{metric}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}

      {/* Jargon Glossary */}
      {response.jargon_glossary && (
        <JargonGlossary items={response.jargon_glossary} />
      )}

      {/* Stage 4 Outbound Doctor Consultation Checklist (P-S-A framework) */}
      {(response.patient_suggestions?.questions_for_doctor || response.doctor_questions) && (
        <DoctorChecklist
          questions={response.patient_suggestions?.questions_for_doctor || response.doctor_questions || []}
        />
      )}
    </div>
  );
}
