"use client";

import React, { useState, useEffect } from "react";
import {
  fetchClinicalResearchRecommendations,
} from "@/lib/api";
import {
  ClinicalResearchRecommendation,
  PatientResearchRecommendation,
  DoctorResearchRecommendation,
  UserMode,
} from "@/lib/types";
import {
  BookOpenCheck,
  Stethoscope,
  HeartHandshake,
  ShieldCheck,
  Sparkles,
  HelpCircle,
  Copy,
  Check,
  AlertTriangle,
  ExternalLink,
  Layers,
  ArrowRight,
  FlaskConical,
  RefreshCw,
} from "lucide-react";

interface ResearchRecommendationDeckProps {
  condition: string;
  userMode: UserMode;
  onSelectCitation?: (citationIndex: number) => void;
}

export function ResearchRecommendationDeck({
  condition,
  userMode,
  onSelectCitation,
}: ResearchRecommendationDeckProps) {
  const [loading, setLoading] = useState<boolean>(true);
  const [data, setData] = useState<ClinicalResearchRecommendation | null>(null);
  const [copiedQuestionIdx, setCopiedQuestionIdx] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const audience = userMode === "professional" ? "doctor" : "patient";

  useEffect(() => {
    let isMounted = true;
    if (!condition || !condition.trim()) {
      setLoading(false);
      return;
    }

    setLoading(true);
    setError(null);

    fetchClinicalResearchRecommendations(condition, audience, 5)
      .then((res) => {
        if (isMounted) {
          setData(res);
          setLoading(false);
        }
      })
      .catch((err) => {
        if (isMounted) {
          console.warn("Recommendation load notice:", err);
          setError("Clinical research recommendations temporarily unavailable.");
          setLoading(false);
        }
      });

    return () => {
      isMounted = false;
    };
  }, [condition, audience]);

  const handleCopyQuestion = (text: string, idx: number) => {
    navigator.clipboard.writeText(text);
    setCopiedQuestionIdx(idx);
    setTimeout(() => setCopiedQuestionIdx(null), 2000);
  };

  if (!condition) {
    return null;
  }

  if (loading) {
    return (
      <div className="p-6 rounded-2xl border border-slate-200 bg-white/70 backdrop-blur-md shadow-xs animate-pulse">
        <div className="flex items-center gap-3 mb-4">
          <div className="w-8 h-8 rounded-xl bg-slate-200" />
          <div className="h-5 w-48 rounded bg-slate-200" />
        </div>
        <div className="space-y-2.5">
          <div className="h-4 w-full rounded bg-slate-100" />
          <div className="h-4 w-5/6 rounded bg-slate-100" />
          <div className="h-4 w-2/3 rounded bg-slate-100" />
        </div>
      </div>
    );
  }

  if (error || !data) {
    return null;
  }

  const isPatient = data.audience === "patient";

  return (
    <div className="rounded-2xl border border-slate-200/90 bg-gradient-to-b from-white to-slate-50/50 shadow-xs overflow-hidden transition-all">
      {/* Header Banner */}
      <div
        className={`px-5 py-4 border-b flex flex-wrap items-center justify-between gap-3 ${
          isPatient
            ? "bg-indigo-50/70 border-indigo-100 text-indigo-950"
            : "bg-teal-50/70 border-teal-100 text-teal-950"
        }`}
      >
        <div className="flex items-center gap-2.5">
          <div
            className={`p-2 rounded-xl text-white shadow-2xs ${
              isPatient ? "bg-indigo-600 shadow-indigo-200" : "bg-teal-700 shadow-teal-200"
            }`}
          >
            {isPatient ? <HeartHandshake className="w-4 h-4" /> : <Stethoscope className="w-4 h-4" />}
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight">
              {isPatient
                ? "Recent Medical Research & Proven Guidelines"
                : "Evidence-Based Clinical Trials & Guideline Dossier"}
            </h3>
            <p className="text-xs opacity-75">
              Live evidence grounded in PubMed, Europe PMC, and consensus society guidelines for{" "}
              <span className="font-semibold">{condition}</span>
            </p>
          </div>
        </div>

        <span
          className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold ${
            isPatient
              ? "bg-indigo-100 text-indigo-800 border border-indigo-200"
              : "bg-teal-100 text-teal-900 border border-teal-200"
          }`}
        >
          <Sparkles className="w-3 h-3" />
          {data.reading_level}
        </span>
      </div>

      <div className="p-5 sm:p-6 space-y-6">
        {/* PATIENT VIEW */}
        {isPatient && (
          <>
            {/* Overview Box */}
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200/80 text-sm text-slate-800 leading-relaxed">
              {(data as PatientResearchRecommendation).overview}
            </div>

            {/* Plain-Language Findings */}
            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-2">
                <BookOpenCheck className="w-4 h-4 text-indigo-600" />
                <span>What Research Shows For Your Care</span>
              </h4>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                {(data as PatientResearchRecommendation).plain_language_findings.map((f, idx) => (
                  <div
                    key={idx}
                    className="p-4 rounded-xl border border-slate-200/90 bg-white hover:border-indigo-300 hover:shadow-2xs transition-all flex flex-col justify-between"
                  >
                    <div>
                      <h5 className="text-sm font-bold text-slate-900 mb-1.5">{f.topic}</h5>
                      <p className="text-xs text-slate-700 leading-normal">{f.what_it_means_for_you}</p>
                    </div>
                    <div className="mt-3 pt-2.5 border-t border-slate-100 text-2xs text-slate-500 font-mono flex items-center justify-between">
                      <span>Source: {f.source}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Questions to Ask Doctor */}
            {(data as PatientResearchRecommendation).questions_for_doctor.length > 0 && (
              <div className="p-4 rounded-xl bg-gradient-to-r from-indigo-50/60 via-purple-50/30 to-white border border-indigo-100">
                <h4 className="text-xs font-bold uppercase tracking-wider text-indigo-900 mb-3 flex items-center gap-2">
                  <HelpCircle className="w-4 h-4 text-indigo-600" />
                  <span>Important Questions to Bring to Your Doctor's Appointment</span>
                </h4>
                <div className="space-y-2">
                  {(data as PatientResearchRecommendation).questions_for_doctor.map((q, idx) => (
                    <div
                      key={idx}
                      className="flex items-start justify-between gap-3 p-2.5 rounded-lg bg-white/80 border border-indigo-100/70 hover:bg-white text-xs text-slate-800 transition-all"
                    >
                      <span className="flex-1 font-medium leading-relaxed">
                        <span className="font-bold text-indigo-600 mr-2">{idx + 1}.</span>
                        {q}
                      </span>
                      <button
                        type="button"
                        onClick={() => handleCopyQuestion(q, idx)}
                        className="p-1 rounded text-slate-400 hover:text-indigo-600 transition-colors"
                        title="Copy question to clipboard"
                      >
                        {copiedQuestionIdx === idx ? (
                          <Check className="w-3.5 h-3.5 text-emerald-600" />
                        ) : (
                          <Copy className="w-3.5 h-3.5" />
                        )}
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Reputable Resources */}
            {(data as PatientResearchRecommendation).reputable_resources.length > 0 && (
              <div className="flex flex-wrap items-center gap-2 pt-2 text-2xs text-slate-500">
                <span className="font-semibold text-slate-700">Verified Patient Directories:</span>
                {(data as PatientResearchRecommendation).reputable_resources.map((r, idx) => (
                  <span
                    key={idx}
                    className="px-2.5 py-1 rounded-md bg-slate-100 text-slate-700 border border-slate-200"
                  >
                    {r}
                  </span>
                ))}
              </div>
            )}
          </>
        )}

        {/* CLINICIAN VIEW */}
        {!isPatient && (
          <>
            {/* Synthesis Header */}
            <div className="p-4 rounded-xl bg-teal-50/50 border border-teal-200/70 text-xs text-teal-950 leading-relaxed font-sans">
              {(data as DoctorResearchRecommendation).evidence_synthesis}
            </div>

            {/* Landmark RCTs & Trials */}
            <div>
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-2">
                <FlaskConical className="w-4 h-4 text-teal-700" />
                <span>Landmark Clinical Trials & Oxford CEBM Evidence</span>
              </h4>
              <div className="space-y-2.5">
                {(data as DoctorResearchRecommendation).key_trials_and_rcts.map((t, idx) => (
                  <div
                    key={idx}
                    className="p-4 rounded-xl border border-slate-200/90 bg-white hover:border-teal-300 transition-all text-xs"
                  >
                    <div className="flex flex-wrap items-center justify-between gap-2 mb-1.5">
                      <span className="font-bold text-slate-900 text-sm">{t.title}</span>
                      <span className="px-2 py-0.5 rounded text-2xs font-mono font-bold bg-teal-100 text-teal-900 border border-teal-200">
                        {t.evidence_level}
                      </span>
                    </div>
                    <p className="text-slate-600 mb-2 leading-relaxed">{t.key_findings}</p>
                    <div className="p-2.5 rounded-lg bg-slate-50 border border-slate-100 font-medium text-slate-800 mb-2">
                      <span className="font-bold text-teal-800">Clinical Implication: </span>
                      {t.clinical_implication}
                    </div>
                    <div className="flex flex-wrap items-center justify-between gap-2 text-2xs text-slate-500 font-mono">
                      <span>
                        {t.journal} ({t.year})
                      </span>
                      {t.doi_or_pmid && <span>{t.doi_or_pmid}</span>}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Guideline Consensus */}
            {(data as DoctorResearchRecommendation).guideline_consensus.length > 0 && (
              <div>
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3 flex items-center gap-2">
                  <ShieldCheck className="w-4 h-4 text-emerald-600" />
                  <span>Cross-Society Guideline Consensus</span>
                </h4>
                <div className="space-y-2 text-xs">
                  {(data as DoctorResearchRecommendation).guideline_consensus.map((gl, idx) => (
                    <div
                      key={idx}
                      className="p-3 rounded-lg border border-slate-200 bg-white flex items-start gap-2.5"
                    >
                      <span className="text-teal-700 font-bold mt-0.5">•</span>
                      <div className="flex-1">
                        <span className="font-bold text-slate-900">{gl.guideline} </span>
                        <span className="text-slate-500">({gl.authority}): </span>
                        <span className="text-slate-700">{gl.recommendation}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Contraindications & Safety */}
            {(data as DoctorResearchRecommendation).contraindications_and_safety.length > 0 && (
              <div className="p-4 rounded-xl bg-rose-50/60 border border-rose-200/80 text-xs">
                <h4 className="font-bold uppercase tracking-wider text-rose-950 mb-2.5 flex items-center gap-2">
                  <AlertTriangle className="w-4 h-4 text-rose-600" />
                  <span>Clinical Surveillance, Safety & Organ Clearance Warnings</span>
                </h4>
                <ul className="space-y-1.5 text-slate-700">
                  {(data as DoctorResearchRecommendation).contraindications_and_safety.map((item, idx) => (
                    <li key={idx} className="flex items-start gap-1.5">
                      <span className="text-rose-600 font-bold">•</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </>
        )}

        {/* Disclaimer */}
        <div className="pt-3 border-t border-slate-100 text-2xs text-slate-400 italic">
          {data.disclaimer}
        </div>
      </div>
    </div>
  );
}
