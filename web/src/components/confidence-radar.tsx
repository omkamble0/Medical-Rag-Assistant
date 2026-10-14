"use client";

import React from "react";
import { ConfidenceMetrics } from "@/lib/types";
import { ShieldCheck, ShieldAlert, AlertTriangle, BookOpenCheck, Activity, Clock, Award } from "lucide-react";

interface ConfidenceRadarProps {
  metrics: ConfidenceMetrics;
}

export function ConfidenceRadar({ metrics }: ConfidenceRadarProps) {
  const percentage = Math.round(metrics.overall_score * 100);

  const getStatusConfig = () => {
    switch (metrics.status) {
      case "high":
        return {
          cardBg: "bg-emerald-50/70 border-emerald-200",
          textColor: "text-emerald-900",
          iconBg: "bg-emerald-100 text-emerald-700",
          badgeBg: "bg-emerald-100 text-emerald-800 border-emerald-300",
          barColor: "bg-emerald-500",
          icon: <ShieldCheck className="w-5 h-5 text-emerald-600" />,
          label: "High Evidence Certainty",
          summary: "Strong consensus across peer-reviewed clinical trials & international guidelines (WHO / Oxford CEBM Level 1).",
        };
      case "moderate":
        return {
          cardBg: "bg-amber-50/70 border-amber-200",
          textColor: "text-amber-900",
          iconBg: "bg-amber-100 text-amber-700",
          badgeBg: "bg-amber-100 text-amber-800 border-amber-300",
          barColor: "bg-amber-500",
          icon: <AlertTriangle className="w-5 h-5 text-amber-600" />,
          label: "Moderate Evidentiary Consensus",
          summary: "Substantiated by recognized clinical literature and specialty society recommendations.",
        };
      default:
        return {
          cardBg: "bg-rose-50/70 border-rose-200",
          textColor: "text-rose-900",
          iconBg: "bg-rose-100 text-rose-700",
          badgeBg: "bg-rose-100 text-rose-800 border-rose-300",
          barColor: "bg-rose-500",
          icon: <ShieldAlert className="w-5 h-5 text-rose-600" />,
          label: "Emerging Evidence / Inquire With Doctor",
          summary: "Preliminary data available; consultation with your treating physician is strongly advised.",
        };
    }
  };

  const config = getStatusConfig();

  return (
    <div className={`p-4 sm:p-5 rounded-2xl border ${config.cardBg} transition-all duration-200 shadow-sm`}>
      <div className="flex flex-wrap items-center justify-between gap-3 mb-3">
        <div className="flex items-center gap-3">
          <div className={`p-2 rounded-xl ${config.iconBg}`}>
            {config.icon}
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
                Medical Evidence Grounding
              </span>
            </div>
            <h4 className={`text-sm sm:text-base font-bold ${config.textColor}`}>
              {config.label}
            </h4>
          </div>
        </div>

        <div className={`px-3 py-1 rounded-full text-xs font-bold border ${config.badgeBg} flex items-center gap-1.5 shadow-sm`}>
          <Award className="w-3.5 h-3.5" />
          <span>{percentage}% Grounded in Evidence</span>
        </div>
      </div>

      <p className="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4">
        {metrics.explanation || config.summary}
      </p>

      {/* Tri-factor Metric Breakdown in Clean White Micro-cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-3 border-t border-slate-200/80">
        <div className="bg-white p-3 rounded-xl border border-slate-200/80 shadow-xs">
          <div className="flex items-center justify-between text-xs text-slate-500 mb-1.5">
            <span className="flex items-center gap-1.5 font-medium">
              <BookOpenCheck className="w-3.5 h-3.5 text-indigo-500" />
              Guideline Match
            </span>
            <span className="font-bold text-slate-800">
              {Math.round(metrics.retrieval_relevance * 100)}%
            </span>
          </div>
          <div className="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div
              className="bg-indigo-500 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.round(metrics.retrieval_relevance * 100)}%` }}
            />
          </div>
        </div>

        <div className="bg-white p-3 rounded-xl border border-slate-200/80 shadow-xs">
          <div className="flex items-center justify-between text-xs text-slate-500 mb-1.5">
            <span className="flex items-center gap-1.5 font-medium">
              <Activity className="w-3.5 h-3.5 text-teal-600" />
              Claim Density
            </span>
            <span className="font-bold text-slate-800">
              {Math.round(metrics.grounding_ratio * 100)}%
            </span>
          </div>
          <div className="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div
              className="bg-teal-500 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.round(metrics.grounding_ratio * 100)}%` }}
            />
          </div>
        </div>

        <div className="bg-white p-3 rounded-xl border border-slate-200/80 shadow-xs">
          <div className="flex items-center justify-between text-xs text-slate-500 mb-1.5">
            <span className="flex items-center gap-1.5 font-medium">
              <Clock className="w-3.5 h-3.5 text-blue-500" />
              Guideline Freshness
            </span>
            <span className="font-bold text-slate-800">
              {Math.round(metrics.evidence_freshness * 100)}%
            </span>
          </div>
          <div className="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div
              className="bg-blue-500 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.round(metrics.evidence_freshness * 100)}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
