"use client";

import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { SearchResponse } from "@/lib/types";
import { JargonGlossary } from "./jargon-tooltip";
import { DoctorChecklist } from "./doctor-checklist";
import {
  HeartHandshake, Sparkles, BookOpenCheck, Stethoscope, Lightbulb,
  ShieldCheck, CheckCircle2, AlertTriangle, Activity, Apple, Users, HelpCircle
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
                title={`View Verified Reference [${citIdx}]`}
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
              Clear, easy-to-understand explanation for you and your family
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1.5 text-xs text-indigo-800 font-medium bg-indigo-50 px-3 py-1.5 rounded-xl border border-indigo-200">
            <CheckCircle2 className="w-4 h-4 text-indigo-600" />
            <span>Peer-Reviewed Evidence</span>
          </div>
          <div className="hidden sm:flex items-center gap-1.5 text-xs text-emerald-700 font-semibold bg-emerald-50 px-3 py-1.5 rounded-xl border border-emerald-200">
            <ShieldCheck className="w-4 h-4 text-emerald-600" />
            <span>Doctor-Approved Guidance</span>
          </div>
        </div>
      </div>

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

              const tLow = textContent.toLowerCase();
              if (tLow.includes("understanding") || tLow.includes("what it is") || tLow.includes("at a glance")) {
                icon = <HeartHandshake className="w-4 h-4 text-indigo-500" />;
                badgeColor = "bg-indigo-50 border-indigo-200 text-indigo-900";
              } else if (tLow.includes("how it works") || tLow.includes("analogy") || tLow.includes("inside the body")) {
                icon = <Lightbulb className="w-4 h-4 text-amber-500" />;
                badgeColor = "bg-amber-50 border-amber-200 text-amber-900";
              } else if (tLow.includes("what does it feel like") || tLow.includes("symptoms") || tLow.includes("signs")) {
                icon = <Activity className="w-4 h-4 text-blue-500" />;
                badgeColor = "bg-blue-50 border-blue-200 text-blue-900";
              } else if (tLow.includes("causes") || tLow.includes("who is at risk")) {
                icon = <Users className="w-4 h-4 text-purple-500" />;
                badgeColor = "bg-purple-50 border-purple-200 text-purple-900";
              } else if (tLow.includes("diagnose")) {
                icon = <Stethoscope className="w-4 h-4 text-teal-500" />;
                badgeColor = "bg-teal-50 border-teal-200 text-teal-900";
              } else if (tLow.includes("research") || tLow.includes("explanation") || tLow.includes("clinical")) {
                icon = <BookOpenCheck className="w-4 h-4 text-violet-500" />;
                badgeColor = "bg-violet-50 border-violet-200 text-violet-900";
              } else if (tLow.includes("practical") || tLow.includes("solutions") || tLow.includes("daily care")) {
                icon = <Apple className="w-4 h-4 text-emerald-500" />;
                badgeColor = "bg-emerald-50 border-emerald-200 text-emerald-900";
              } else if (tLow.includes("myths")) {
                icon = <HelpCircle className="w-4 h-4 text-amber-500" />;
                badgeColor = "bg-amber-50 border-amber-200 text-amber-900";
              } else if (tLow.includes("questions") || tLow.includes("doctor")) {
                icon = <HeartHandshake className="w-4 h-4 text-sky-500" />;
                badgeColor = "bg-sky-50 border-sky-200 text-sky-900";
              } else if (tLow.includes("warning") || tLow.includes("attention") || tLow.includes("red flags") || tLow.includes("urgent")) {
                icon = <AlertTriangle className="w-4 h-4 text-rose-500" />;
                badgeColor = "bg-rose-50 border-rose-200 text-rose-900";
              }

              return (
                <div className={`mt-6 mb-3 p-3.5 rounded-2xl border ${badgeColor} flex items-center gap-2.5 shadow-2xs`}>
                  <span className="p-1.5 rounded-xl bg-white/90 shadow-2xs shrink-0">{icon}</span>
                  <h3 className="text-base sm:text-lg font-bold tracking-tight">
                    {children}
                  </h3>
                </div>
              );
            },
            p: ({ children }) => {
              if (typeof children === "string") {
                return <p className="mb-4 leading-relaxed text-slate-700 text-sm sm:text-base">{renderInlineCitations(children)}</p>;
              }
              return <div className="mb-4 leading-relaxed text-slate-700 text-sm sm:text-base">{children}</div>;
            },
            ul: ({ children }) => (
              <ul className="space-y-3 my-4 list-disc pl-5 text-slate-700 marker:text-indigo-500">
                {children}
              </ul>
            ),
            li: ({ children }) => (
              <li className="leading-relaxed pl-1 text-sm sm:text-base">
                {typeof children === "string" ? renderInlineCitations(children) : children}
              </li>
            ),
            strong: ({ children }) => (
              <strong className="font-bold text-slate-900">
                {children}
              </strong>
            ),
            em: ({ children }) => (
              <em className="text-slate-600 italic">
                {children}
              </em>
            ),
            blockquote: ({ children }) => (
              <div className="my-4 p-4 rounded-2xl bg-amber-50/80 border-l-4 border-amber-500 text-amber-950 shadow-2xs text-sm sm:text-base leading-relaxed">
                {children}
              </div>
            ),
            code: ({ children }) => (
              <code className="px-1.5 py-0.5 rounded-md bg-slate-100 text-indigo-700 font-mono text-xs font-bold border border-slate-200">
                {children}
              </code>
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
