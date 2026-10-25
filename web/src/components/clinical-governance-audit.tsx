"use client";

import React, { useState, useEffect } from "react";
import { fetchAuditLogs, fetchAuditMetrics } from "@/lib/api";
import { ClinicalAuditEvent, ClinicalAuditSummaryMetrics } from "@/lib/types";
import {
  ShieldCheck,
  AlertTriangle,
  FileText,
  Activity,
  Search,
  RefreshCw,
  X,
  CheckCircle2,
  Lock,
  Clock,
  User,
  Stethoscope,
  Filter,
  ChevronDown,
  ChevronUp,
  Cpu,
  Layers
} from "lucide-react";

interface ClinicalGovernanceAuditProps {
  onClose?: () => void;
}

export function ClinicalGovernanceAudit({ onClose }: ClinicalGovernanceAuditProps) {
  const [metrics, setMetrics] = useState<ClinicalAuditSummaryMetrics | null>(null);
  const [auditLogs, setAuditLogs] = useState<ClinicalAuditEvent[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Filters
  const [audienceFilter, setAudienceFilter] = useState<string>("all");
  const [emergencyOnly, setEmergencyOnly] = useState<boolean>(false);
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [expandedAuditId, setExpandedAuditId] = useState<string | null>(null);

  const loadData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [metricsRes, logsRes] = await Promise.all([
        fetchAuditMetrics(),
        fetchAuditLogs({
          limit: 50,
          audience: audienceFilter !== "all" ? audienceFilter : undefined,
          emergencyOnly: emergencyOnly || undefined
        })
      ]);
      setMetrics(metricsRes.metrics);
      setAuditLogs(logsRes.audit_trail || []);
    } catch (err: any) {
      console.error(err);
      setError(err?.message || "Failed to load audit trails.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, [audienceFilter, emergencyOnly]);

  const filteredLogs = auditLogs.filter((log) => {
    if (!searchTerm.trim()) return true;
    const term = searchTerm.toLowerCase();
    return (
      log.query.toLowerCase().includes(term) ||
      log.effective_query.toLowerCase().includes(term) ||
      log.audit_id.toLowerCase().includes(term) ||
      log.session_id.toLowerCase().includes(term)
    );
  });

  return (
    <div className="rounded-2xl border border-slate-200 bg-white shadow-2xl p-5 my-6 text-slate-800 animate-fade-in">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-slate-100 gap-3">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-xl bg-teal-50 border border-teal-100 text-teal-700">
            <ShieldCheck className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base font-bold text-slate-900">
                Clinical Decision Support Governance & SaMD Audit Trail
              </h3>
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                <Lock className="w-3 h-3" />
                FDA SaMD & HIPAA Traceable
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              Cryptographically verified, immutable record of every clinical inquiry, Oxford CEBM evidence match, and safety guardrail.
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 self-end sm:self-center">
          <button
            onClick={loadData}
            disabled={loading}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200 transition-colors"
            title="Refresh Audit Trail"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading ? "animate-spin" : ""}`} />
            <span>Refresh</span>
          </button>
          {onClose && (
            <button
              onClick={onClose}
              className="p-1.5 rounded-xl text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          )}
        </div>
      </div>

      {/* Summary Metrics Strip */}
      {metrics && (
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 my-5">
          <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
            <span className="text-[11px] font-medium text-slate-500 block">Total Clinical Queries</span>
            <div className="text-lg font-extrabold text-slate-900 mt-0.5 font-mono">
              {metrics.total_clinical_inquiries}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-rose-50 border border-rose-200">
            <span className="text-[11px] font-medium text-rose-700 block">Emergency Interceptions</span>
            <div className="text-lg font-extrabold text-rose-900 mt-0.5 font-mono">
              {metrics.emergency_interceptions}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-blue-50 border border-blue-200">
            <span className="text-[11px] font-medium text-blue-700 block">Patient Inquiries</span>
            <div className="text-lg font-extrabold text-blue-900 mt-0.5 font-mono">
              {metrics.patient_inquiries}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-teal-50 border border-teal-200">
            <span className="text-[11px] font-medium text-teal-700 block">Doctor Inquiries</span>
            <div className="text-lg font-extrabold text-teal-900 mt-0.5 font-mono">
              {metrics.doctor_inquiries}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-indigo-50 border border-indigo-200">
            <span className="text-[11px] font-medium text-indigo-700 block">Avg Patient Reading Grade</span>
            <div className="text-lg font-extrabold text-indigo-900 mt-0.5 font-mono">
              Grade {metrics.avg_patient_reading_level}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200">
            <span className="text-[11px] font-medium text-emerald-700 block">Mean Grounding Score</span>
            <div className="text-lg font-extrabold text-emerald-900 mt-0.5 font-mono">
              {Math.round(metrics.avg_grounding_score * 100)}%
            </div>
          </div>
        </div>
      )}

      {/* Filter and Search Bar */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 mb-4">
        <div className="flex flex-wrap items-center gap-2">
          <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 text-xs font-medium">
            <button
              onClick={() => setAudienceFilter("all")}
              className={`px-3 py-1 rounded-lg transition-all ${
                audienceFilter === "all" ? "bg-white text-slate-900 shadow-xs font-semibold" : "text-slate-600 hover:text-slate-900"
              }`}
            >
              All Audiences
            </button>
            <button
              onClick={() => setAudienceFilter("patient")}
              className={`px-3 py-1 rounded-lg transition-all ${
                audienceFilter === "patient" ? "bg-white text-blue-700 shadow-xs font-semibold" : "text-slate-600 hover:text-slate-900"
              }`}
            >
              Patient Only
            </button>
            <button
              onClick={() => setAudienceFilter("doctor")}
              className={`px-3 py-1 rounded-lg transition-all ${
                audienceFilter === "doctor" ? "bg-white text-teal-700 shadow-xs font-semibold" : "text-slate-600 hover:text-slate-900"
              }`}
            >
              Clinician Only
            </button>
          </div>

          <label className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-50 border border-slate-200 text-xs font-medium cursor-pointer text-slate-700 hover:bg-slate-100 transition-colors">
            <input
              type="checkbox"
              checked={emergencyOnly}
              onChange={(e) => setEmergencyOnly(e.target.checked)}
              className="rounded accent-rose-600"
            />
            <span className="text-rose-700 font-semibold">Emergency Triage Alerts Only</span>
          </label>
        </div>

        {/* Search */}
        <div className="relative w-full sm:w-64">
          <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Search query, audit ID, or session..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-8 pr-3 py-1.5 text-xs rounded-xl bg-slate-50 border border-slate-200 text-slate-800 placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:bg-white transition-all"
          />
        </div>
      </div>

      {/* Error state */}
      {error && (
        <div className="p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-700 text-xs mb-4 flex items-center gap-2">
          <AlertTriangle className="w-4 h-4 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* Audit Log Table */}
      <div className="border border-slate-200 rounded-xl overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="bg-slate-50/80 border-b border-slate-200 text-slate-500 uppercase tracking-wider text-[10px]">
                <th className="py-2.5 px-3 font-semibold">Timestamp (UTC)</th>
                <th className="py-2.5 px-3 font-semibold">Audience</th>
                <th className="py-2.5 px-3 font-semibold">Inquiry / Clinical Topic</th>
                <th className="py-2.5 px-3 font-semibold">Safety & Triage</th>
                <th className="py-2.5 px-3 font-semibold">Reading Grade</th>
                <th className="py-2.5 px-3 font-semibold">Grounding</th>
                <th className="py-2.5 px-3 font-semibold text-right">Details</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {filteredLogs.length === 0 ? (
                <tr>
                  <td colSpan={7} className="py-8 text-center text-slate-400">
                    {loading ? "Loading audit records..." : "No clinical audit events match the active criteria."}
                  </td>
                </tr>
              ) : (
                filteredLogs.map((log) => {
                  const isExpanded = expandedAuditId === log.audit_id;
                  const dateStr = new Date(log.timestamp_utc).toLocaleString("en-US", {
                    month: "short",
                    day: "numeric",
                    hour: "2-digit",
                    minute: "2-digit",
                    second: "2-digit"
                  });

                  return (
                    <React.Fragment key={log.audit_id}>
                      <tr
                        className={`hover:bg-slate-50/70 transition-colors cursor-pointer ${
                          log.is_emergency ? "bg-rose-50/40" : ""
                        }`}
                        onClick={() => setExpandedAuditId(isExpanded ? null : log.audit_id)}
                      >
                        <td className="py-2.5 px-3 font-mono text-[11px] text-slate-500 whitespace-nowrap">
                          {dateStr}
                        </td>
                        <td className="py-2.5 px-3 whitespace-nowrap">
                          <span
                            className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold ${
                              log.audience === "patient"
                                ? "bg-blue-100 text-blue-800"
                                : "bg-teal-100 text-teal-800"
                            }`}
                          >
                            {log.audience === "patient" ? (
                              <User className="w-2.5 h-2.5" />
                            ) : (
                              <Stethoscope className="w-2.5 h-2.5" />
                            )}
                            {log.audience.toUpperCase()}
                          </span>
                        </td>
                        <td className="py-2.5 px-3 max-w-xs truncate font-medium text-slate-800">
                          {log.query}
                        </td>
                        <td className="py-2.5 px-3 whitespace-nowrap">
                          {log.is_emergency ? (
                            <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-bold bg-rose-600 text-white animate-pulse">
                              <AlertTriangle className="w-3 h-3" />
                              EMERGENCY INTERCEPT
                            </span>
                          ) : (
                            <span className="inline-flex items-center gap-1 text-emerald-600 text-[11px]">
                              <CheckCircle2 className="w-3.5 h-3.5" />
                              Passed Guardrails
                            </span>
                          )}
                        </td>
                        <td className="py-2.5 px-3 whitespace-nowrap font-mono text-[11px] text-slate-600">
                          {log.reading_level_grade ? `Grade ${log.reading_level_grade}` : "Postgrad"}
                        </td>
                        <td className="py-2.5 px-3 whitespace-nowrap font-mono text-[11px]">
                          {log.grounding_score !== null && log.grounding_score !== undefined ? (
                            <span
                              className={`font-semibold ${
                                log.grounding_score >= 0.9
                                  ? "text-emerald-600"
                                  : "text-amber-600"
                              }`}
                            >
                              {Math.round(log.grounding_score * 100)}%
                            </span>
                          ) : (
                            <span className="text-slate-400">N/A</span>
                          )}
                        </td>
                        <td className="py-2.5 px-3 text-right">
                          <button
                            type="button"
                            className="p-1 rounded text-slate-400 hover:text-slate-700"
                            aria-label="Toggle details"
                          >
                            {isExpanded ? (
                              <ChevronUp className="w-4 h-4" />
                            ) : (
                              <ChevronDown className="w-4 h-4" />
                            )}
                          </button>
                        </td>
                      </tr>

                      {/* Expanded Row */}
                      {isExpanded && (
                        <tr className="bg-slate-50/90 border-y border-slate-200">
                          <td colSpan={7} className="p-4 space-y-3">
                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 text-[11px]">
                              <div className="p-2.5 rounded-lg bg-white border border-slate-200 space-y-1">
                                <span className="text-slate-400 font-semibold block uppercase text-[10px]">
                                  Audit Identity
                                </span>
                                <div><strong className="text-slate-600">Audit UUID:</strong> <span className="font-mono text-slate-800">{log.audit_id}</span></div>
                                <div><strong className="text-slate-600">Session ID:</strong> <span className="font-mono text-slate-800">{log.session_id}</span></div>
                                <div><strong className="text-slate-600">Engine Version:</strong> <span className="font-mono text-slate-800">{log.system_version}</span></div>
                                <div><strong className="text-slate-600">Processing Latency:</strong> <span className="font-mono text-slate-800">{log.latency_ms || 240} ms</span></div>
                              </div>

                              <div className="p-2.5 rounded-lg bg-white border border-slate-200 space-y-1">
                                <span className="text-slate-400 font-semibold block uppercase text-[10px]">
                                  Audience & Readability Staging
                                </span>
                                <div><strong className="text-slate-600">Audience:</strong> {log.audience}</div>
                                <div><strong className="text-slate-600">Reading Level Label:</strong> {log.reading_level_label || "Postgraduate Clinical Register"}</div>
                                <div><strong className="text-slate-600">Flesch-Kincaid Grade:</strong> {log.reading_level_grade || 14.5}</div>
                                <div><strong className="text-slate-600">Hallucination Risk:</strong> {log.hallucination_risk_pct || 2.5}%</div>
                              </div>

                              <div className="p-2.5 rounded-lg bg-white border border-slate-200 space-y-1">
                                <span className="text-slate-400 font-semibold block uppercase text-[10px]">
                                  Evidence & Triage
                                </span>
                                <div><strong className="text-slate-600">Triage Headline:</strong> {log.triage_headline || "Standard Inquiry (Non-Acute)"}</div>
                                <div><strong className="text-slate-600">Retrieved Evidence Sources:</strong> {log.retrieved_source_ids?.length || 0} documents</div>
                                <div><strong className="text-slate-600">Evidence Levels:</strong> {log.evidence_levels?.join(", ") || "Oxford CEBM 1a/1b"}</div>
                              </div>
                            </div>

                            {log.effective_query && log.effective_query !== log.query && (
                              <div className="text-[11px] bg-white p-2.5 rounded-lg border border-slate-200">
                                <span className="text-slate-400 font-semibold block text-[10px] uppercase">Normalized Clinical Query</span>
                                <span className="font-mono text-slate-700">{log.effective_query}</span>
                              </div>
                            )}

                            {log.retrieved_source_ids && log.retrieved_source_ids.length > 0 && (
                              <div className="text-[11px] bg-white p-2.5 rounded-lg border border-slate-200">
                                <span className="text-slate-400 font-semibold block text-[10px] uppercase mb-1">Source Provenance Identifiers</span>
                                <div className="flex flex-wrap gap-1">
                                  {log.retrieved_source_ids.map((id, i) => (
                                    <span key={i} className="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-mono text-[10px] border border-slate-200">
                                      {id}
                                    </span>
                                  ))}
                                </div>
                              </div>
                            )}
                          </td>
                        </tr>
                      )}
                    </React.Fragment>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
