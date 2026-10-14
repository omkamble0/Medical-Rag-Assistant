"use client";

import React, { useState, useEffect, useMemo } from "react";
import {
  DiseaseRecord,
  DatabaseStatsResponse,
  SymptomCheckerResponse,
  MatchedDiseaseResult
} from "@/lib/types";
import {
  fetchDatabaseStats,
  fetchDiseases,
  fetchDiseaseById,
  checkSymptomsDifferential,
  fetchSymptoms,
  fetchSolutions,
  fetchResearchPapers
} from "@/lib/api";
import {
  Database,
  Stethoscope,
  Activity,
  Pill,
  BookOpen,
  Search,
  Filter,
  AlertTriangle,
  CheckCircle2,
  ChevronDown,
  ChevronRight,
  ExternalLink,
  Sparkles,
  Zap,
  ShieldAlert,
  Flame,
  X,
  Layers,
  HeartPulse,
  Brain,
  Microscope,
  Info,
  Clock,
  ArrowRight
} from "lucide-react";

interface MedicalDatabaseExplorerProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectQueryForAssistant?: (query: string) => void;
}

type TabType = "diseases" | "symptom-checker" | "solutions" | "research";

export function MedicalDatabaseExplorer({
  isOpen,
  onClose,
  onSelectQueryForAssistant
}: MedicalDatabaseExplorerProps) {
  const [activeTab, setActiveTab] = useState<TabType>("diseases");

  // Stats state
  const [stats, setStats] = useState<DatabaseStatsResponse | null>(null);
  const [loadingStats, setLoadingStats] = useState<boolean>(true);

  // Diseases state
  const [diseases, setDiseases] = useState<DiseaseRecord[]>([]);
  const [loadingDiseases, setLoadingDiseases] = useState<boolean>(false);
  const [selectedSpecialty, setSelectedSpecialty] = useState<string>("All");
  const [searchDiseaseQuery, setSearchDiseaseQuery] = useState<string>("");
  const [expandedDiseaseId, setExpandedDiseaseId] = useState<string | null>(null);
  const [selectedDiseaseMonograph, setSelectedDiseaseMonograph] = useState<DiseaseRecord | null>(null);

  // Symptom checker state
  const [selectedSymptoms, setSelectedSymptoms] = useState<string[]>([]);
  const [customSymptomInput, setCustomSymptomInput] = useState<string>("");
  const [popularSymptoms, setPopularSymptoms] = useState<any[]>([]);
  const [checkerLoading, setCheckerLoading] = useState<boolean>(false);
  const [checkerResult, setCheckerResult] = useState<SymptomCheckerResponse | null>(null);

  // Solutions state
  const [solutionsList, setSolutionsList] = useState<any[]>([]);
  const [loadingSolutions, setLoadingSolutions] = useState<boolean>(false);
  const [solutionTypeFilter, setSolutionTypeFilter] = useState<string>("all");

  // Research papers state
  const [papersList, setPapersList] = useState<any[]>([]);
  const [loadingPapers, setLoadingPapers] = useState<boolean>(false);
  const [cebmFilter, setCebmFilter] = useState<string>("all");

  // Load stats and initial diseases on open
  useEffect(() => {
    if (!isOpen) return;

    const loadInitialData = async () => {
      try {
        setLoadingStats(true);
        const s = await fetchDatabaseStats();
        setStats(s);
      } catch (err) {
        console.warn("Failed to load database stats", err);
      } finally {
        setLoadingStats(false);
      }

      try {
        setLoadingDiseases(true);
        const d = await fetchDiseases({ limit: 40 });
        setDiseases(d);
      } catch (err) {
        console.warn("Failed to load diseases", err);
      } finally {
        setLoadingDiseases(false);
      }

      try {
        const syms = await fetchSymptoms(undefined, 24);
        setPopularSymptoms(syms);
      } catch (err) {
        console.warn("Failed to load symptoms", err);
      }
    };

    loadInitialData();
  }, [isOpen]);

  // Filter diseases when specialty or query changes
  useEffect(() => {
    if (!isOpen || activeTab !== "diseases") return;

    const delayDebounceFn = setTimeout(async () => {
      setLoadingDiseases(true);
      try {
        const d = await fetchDiseases({
          query: searchDiseaseQuery || undefined,
          specialty: selectedSpecialty === "All" ? undefined : selectedSpecialty,
          limit: 50
        });
        setDiseases(d);
      } catch (e) {
        console.warn("Disease query failed", e);
      } finally {
        setLoadingDiseases(false);
      }
    }, 250);

    return () => clearTimeout(delayDebounceFn);
  }, [searchDiseaseQuery, selectedSpecialty, activeTab, isOpen]);

  // Load solutions when solutions tab active
  useEffect(() => {
    if (!isOpen || activeTab !== "solutions") return;
    const loadSolutionsData = async () => {
      setLoadingSolutions(true);
      try {
        const type = solutionTypeFilter === "all" ? undefined : solutionTypeFilter;
        const sols = await fetchSolutions({ type, limit: 35 });
        setSolutionsList(sols);
      } catch (e) {
        console.warn("Solutions fetch failed", e);
      } finally {
        setLoadingSolutions(false);
      }
    };
    loadSolutionsData();
  }, [activeTab, solutionTypeFilter, isOpen]);

  // Load papers when research tab active
  useEffect(() => {
    if (!isOpen || activeTab !== "research") return;
    const loadPapersData = async () => {
      setLoadingPapers(true);
      try {
        const cebm = cebmFilter === "all" ? undefined : cebmFilter;
        const papers = await fetchResearchPapers({ cebm_level: cebm, limit: 35 });
        setPapersList(papers);
      } catch (e) {
        console.warn("Papers fetch failed", e);
      } finally {
        setLoadingPapers(false);
      }
    };
    loadPapersData();
  }, [activeTab, cebmFilter, isOpen]);

  // Symptom selection toggle
  const toggleSymptom = (symptomName: string) => {
    setSelectedSymptoms((prev) =>
      prev.includes(symptomName) ? prev.filter((s) => s !== symptomName) : [...prev, symptomName]
    );
  };

  const addCustomSymptom = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    const clean = customSymptomInput.trim();
    if (clean && !selectedSymptoms.includes(clean)) {
      setSelectedSymptoms((prev) => [...prev, clean]);
      setCustomSymptomInput("");
    }
  };

  // Run symptom differential checker
  const handleRunSymptomCheck = async () => {
    if (selectedSymptoms.length === 0) return;
    setCheckerLoading(true);
    try {
      const res = await checkSymptomsDifferential({
        symptoms: selectedSymptoms,
        top_k: 4
      });
      setCheckerResult(res);
    } catch (e) {
      console.error("Differential check error", e);
    } finally {
      setCheckerLoading(false);
    }
  };

  const handleLaunchInAssistant = (diseaseName: string) => {
    const prompt = `What are the verified clinical guidelines, first-line drug treatments, and trial endpoints for ${diseaseName}?`;
    if (onSelectQueryForAssistant) {
      onSelectQueryForAssistant(prompt);
      onClose();
    }
  };

  const specialtiesList = useMemo(() => {
    if (!stats?.specialties_distribution) {
      return ["All", "Cardiovascular", "Pulmonology", "Endocrinology", "Neurology", "Gastroenterology", "Infectious Disease", "Rheumatology", "Nephrology", "Dermatology", "Psychiatry", "Oncology"];
    }
    return ["All", ...Object.keys(stats.specialties_distribution).sort()];
  }, [stats]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/80 backdrop-blur-md overflow-hidden animate-in fade-in duration-200">
      <div className="relative w-full max-w-6xl max-h-[92vh] flex flex-col bg-slate-900 border border-slate-700/70 rounded-2xl shadow-2xl shadow-cyan-950/40 text-slate-100 overflow-hidden">
        
        {/* Modal Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between p-5 border-b border-slate-800 bg-gradient-to-r from-slate-900 via-slate-900/90 to-cyan-950/30 gap-4">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 rounded-xl bg-gradient-to-br from-cyan-500/20 to-blue-600/30 border border-cyan-500/40 flex items-center justify-center text-cyan-400 shadow-inner">
              <Database className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-xl font-bold tracking-tight text-white">
                  AegisMed Clinical Knowledge Base
                </h2>
                <span className="text-[10px] uppercase font-semibold px-2 py-0.5 rounded-full bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">
                  Hybrid Qdrant + JSON
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                Comprehensive repository of 100+ clinical conditions, granular symptoms, GDMT solutions, and Oxford CEBM trials.
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {stats && (
              <div className="hidden md:flex items-center gap-3 text-xs bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                <span className="flex items-center gap-1.5 text-cyan-300 font-medium">
                  <Activity className="w-3.5 h-3.5" /> {stats.total_diseases} Conditions
                </span>
                <span className="text-slate-600">•</span>
                <span className="text-emerald-400 font-medium">
                  {stats.total_symptoms} Symptoms
                </span>
                <span className="text-slate-600">•</span>
                <span className="text-amber-300 font-medium">
                  {stats.total_solutions} Protocols
                </span>
              </div>
            )}
            <button
              onClick={onClose}
              className="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-lg transition-colors"
              title="Close Explorer"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Tab Navigation */}
        <div className="flex items-center border-b border-slate-800 px-5 bg-slate-900/60 overflow-x-auto text-sm font-medium">
          <button
            onClick={() => setActiveTab("diseases")}
            className={`flex items-center gap-2 py-3 px-3.5 border-b-2 transition-all whitespace-nowrap ${
              activeTab === "diseases"
                ? "border-cyan-400 text-cyan-300 font-semibold"
                : "border-transparent text-slate-400 hover:text-slate-200"
            }`}
          >
            <Stethoscope className="w-4 h-4" />
            <span>Disease Directory ({stats?.total_diseases || 100})</span>
          </button>

          <button
            onClick={() => setActiveTab("symptom-checker")}
            className={`flex items-center gap-2 py-3 px-3.5 border-b-2 transition-all whitespace-nowrap ${
              activeTab === "symptom-checker"
                ? "border-cyan-400 text-cyan-300 font-semibold"
                : "border-transparent text-slate-400 hover:text-slate-200"
            }`}
          >
            <Microscope className="w-4 h-4 text-purple-400" />
            <span>Symptom Differential Matcher</span>
            <span className="text-[10px] bg-purple-500/20 text-purple-300 px-1.5 py-0.2 rounded font-mono">
              AI Tool
            </span>
          </button>

          <button
            onClick={() => setActiveTab("solutions")}
            className={`flex items-center gap-2 py-3 px-3.5 border-b-2 transition-all whitespace-nowrap ${
              activeTab === "solutions"
                ? "border-cyan-400 text-cyan-300 font-semibold"
                : "border-transparent text-slate-400 hover:text-slate-200"
            }`}
          >
            <Pill className="w-4 h-4 text-emerald-400" />
            <span>GDMT Treatments & Protocols</span>
          </button>

          <button
            onClick={() => setActiveTab("research")}
            className={`flex items-center gap-2 py-3 px-3.5 border-b-2 transition-all whitespace-nowrap ${
              activeTab === "research"
                ? "border-cyan-400 text-cyan-300 font-semibold"
                : "border-transparent text-slate-400 hover:text-slate-200"
            }`}
          >
            <BookOpen className="w-4 h-4 text-amber-400" />
            <span>Oxford CEBM Research Trials</span>
          </button>
        </div>

        {/* Tab Body Contents */}
        <div className="flex-1 overflow-y-auto p-5 space-y-6">
          
          {/* ─────────────────────────────────────────────────────────────
              TAB 1: DISEASE DIRECTORY
              ───────────────────────────────────────────────────────────── */}
          {activeTab === "diseases" && (
            <div className="space-y-5">
              {/* Controls bar */}
              <div className="flex flex-col md:flex-row gap-3">
                <div className="relative flex-1">
                  <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
                  <input
                    type="text"
                    value={searchDiseaseQuery}
                    onChange={(e) => setSearchDiseaseQuery(e.target.value)}
                    placeholder="Search by condition name, ICD-10 (e.g. I10, E11), symptoms, or drugs..."
                    className="w-full bg-slate-800/80 border border-slate-700/80 rounded-xl pl-10 pr-4 py-2 text-sm text-slate-100 placeholder-slate-400 focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400"
                  />
                  {searchDiseaseQuery && (
                    <button
                      onClick={() => setSearchDiseaseQuery("")}
                      className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                    >
                      <X className="w-4 h-4" />
                    </button>
                  )}
                </div>

                {/* Specialty Pill Scroll */}
                <div className="flex items-center gap-1.5 overflow-x-auto pb-1 md:pb-0 scrollbar-thin">
                  {specialtiesList.map((spec) => (
                    <button
                      key={spec}
                      onClick={() => setSelectedSpecialty(spec)}
                      className={`text-xs px-3 py-1.5 rounded-lg whitespace-nowrap transition-colors border ${
                        selectedSpecialty === spec
                          ? "bg-cyan-500/20 text-cyan-300 border-cyan-500/40 font-medium"
                          : "bg-slate-800/60 text-slate-400 border-slate-700/70 hover:bg-slate-700 hover:text-slate-200"
                      }`}
                    >
                      {spec}
                    </button>
                  ))}
                </div>
              </div>

              {/* Disease Cards Grid */}
              {loadingDiseases ? (
                <div className="flex flex-col items-center justify-center py-16 text-slate-400">
                  <div className="w-8 h-8 border-2 border-cyan-400 border-t-transparent rounded-full animate-spin mb-3"></div>
                  <p className="text-sm">Querying verified clinical database...</p>
                </div>
              ) : diseases.length === 0 ? (
                <div className="text-center py-16 text-slate-400 bg-slate-800/40 border border-slate-800 rounded-xl p-8">
                  <p className="text-base font-medium text-slate-300">No matching medical conditions found.</p>
                  <p className="text-xs text-slate-500 mt-1">Try clearing your search query or selecting a different medical specialty.</p>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {diseases.map((disease) => {
                    const isExpanded = expandedDiseaseId === disease.id;

                    return (
                      <div
                        key={disease.id}
                        className={`p-4 rounded-xl border transition-all duration-200 ${
                          isExpanded
                            ? "bg-slate-800/90 border-cyan-500/50 shadow-lg shadow-cyan-950/20"
                            : "bg-slate-800/40 border-slate-700/60 hover:border-slate-600 hover:bg-slate-800/60"
                        }`}
                      >
                        {/* Card Header */}
                        <div className="flex items-start justify-between gap-3">
                          <div className="space-y-1">
                            <div className="flex items-center gap-2 flex-wrap">
                              <h3 className="text-base font-semibold text-white tracking-tight">
                                {disease.name}
                              </h3>
                              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-500/15 text-blue-300 border border-blue-500/30 font-medium">
                                ICD-10: {disease.icd10_code}
                              </span>
                            </div>
                            <div className="flex items-center gap-2 text-xs text-slate-400">
                              <span className="text-cyan-400 font-medium">{disease.specialty}</span>
                              <span>•</span>
                              <span>{disease.organ_system}</span>
                              <span>•</span>
                              <span className={`px-1.5 py-0.2 rounded text-[10px] ${
                                disease.severity === "Severe" || disease.severity === "Life-Threatening"
                                  ? "bg-red-500/15 text-red-300"
                                  : "bg-amber-500/15 text-amber-300"
                              }`}>
                                {disease.severity}
                              </span>
                            </div>
                          </div>

                          <button
                            onClick={() => setExpandedDiseaseId(isExpanded ? null : disease.id)}
                            className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-700 rounded-lg transition-colors"
                          >
                            {isExpanded ? <ChevronDown className="w-5 h-5 text-cyan-400" /> : <ChevronRight className="w-5 h-5" />}
                          </button>
                        </div>

                        {/* Plain Language Summary */}
                        <p className="text-xs text-slate-300 mt-3 leading-relaxed">
                          {disease.patient_plain_language}
                        </p>

                        {/* Hallmark Symptoms Badges */}
                        <div className="flex flex-wrap gap-1.5 mt-3">
                          {disease.symptoms.slice(0, 3).map((sym, idx) => (
                            <span
                              key={idx}
                              className="text-[11px] px-2 py-0.5 rounded-md bg-slate-700/60 text-slate-300 border border-slate-600/50 flex items-center gap-1"
                            >
                              <Activity className="w-2.5 h-2.5 text-cyan-400" />
                              {sym.name}
                            </span>
                          ))}
                          {disease.symptoms.length > 3 && (
                            <span className="text-[11px] px-1.5 py-0.5 text-slate-400">
                              +{disease.symptoms.length - 3} more
                            </span>
                          )}
                        </div>

                        {/* Accordion Expanded Details */}
                        {isExpanded && (
                          <div className="mt-4 pt-4 border-t border-slate-700 space-y-4 animate-in fade-in duration-150">
                            {/* Clinical Overview */}
                            <div>
                              <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-1">
                                Clinical Monograph Overview
                              </span>
                              <p className="text-xs text-slate-300 bg-slate-900/60 p-3 rounded-lg border border-slate-800 leading-relaxed">
                                {disease.overview}
                              </p>
                            </div>

                            {/* Full Symptoms List */}
                            <div>
                              <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2">
                                Clinical Symptoms Profile ({disease.symptoms.length})
                              </span>
                              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                {disease.symptoms.map((s, i) => (
                                  <div
                                    key={i}
                                    className="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800/80 text-xs"
                                  >
                                    <div className="flex items-center justify-between">
                                      <span className="font-medium text-slate-200">{s.name}</span>
                                      <span className={`text-[10px] px-1.5 rounded uppercase ${
                                        s.frequency === "hallmark"
                                          ? "bg-purple-500/20 text-purple-300"
                                          : "bg-slate-700 text-slate-300"
                                      }`}>
                                        {s.frequency}
                                      </span>
                                    </div>
                                    {s.description && (
                                      <p className="text-[11px] text-slate-400 mt-1 leading-snug">
                                        {s.description}
                                      </p>
                                    )}
                                  </div>
                                ))}
                              </div>
                            </div>

                            {/* First-Line GDMT Solutions */}
                            <div>
                              <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2">
                                First-Line GDMT Solutions & Protocols
                              </span>
                              <div className="space-y-2">
                                {disease.solutions.map((sol, i) => (
                                  <div
                                    key={i}
                                    className="p-3 rounded-lg bg-emerald-950/20 border border-emerald-500/30 text-xs"
                                  >
                                    <div className="flex items-center justify-between">
                                      <span className="font-semibold text-emerald-300">
                                        {sol.name}
                                      </span>
                                      <span className="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 uppercase font-mono">
                                        {sol.line_of_therapy.replace("_", " ")}
                                      </span>
                                    </div>
                                    <p className="text-slate-300 text-xs mt-1 leading-relaxed">
                                      {sol.description}
                                    </p>
                                    {sol.dosage_or_protocol && (
                                      <div className="mt-2 text-[11px] text-slate-400 bg-slate-900/80 p-2 rounded border border-slate-800">
                                        <strong className="text-cyan-400">Dosing / Protocol:</strong> {sol.dosage_or_protocol}
                                      </div>
                                    )}
                                    {sol.contraindications && sol.contraindications.length > 0 && (
                                      <div className="mt-1.5 text-[11px] text-red-300/90">
                                        <strong>Contraindications:</strong> {sol.contraindications.join(", ")}
                                      </div>
                                    )}
                                  </div>
                                ))}
                              </div>
                            </div>

                            {/* Research Paper Citation */}
                            {disease.research_papers && disease.research_papers.length > 0 && (
                              <div>
                                <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-1.5">
                                  Oxford CEBM Evidence & Landmark Trials
                                </span>
                                {disease.research_papers.map((p, i) => (
                                  <div
                                    key={i}
                                    className="p-3 rounded-lg bg-blue-950/20 border border-blue-500/30 text-xs"
                                  >
                                    <div className="flex items-center justify-between flex-wrap gap-2">
                                      <span className="font-medium text-blue-200">{p.title}</span>
                                      <span className="text-[10px] px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-semibold">
                                        {p.cebm_level}
                                      </span>
                                    </div>
                                    <p className="text-[11px] text-slate-400 mt-1">
                                      {p.journal} ({p.year}) • {p.study_design}
                                    </p>
                                    <p className="text-slate-300 text-xs mt-2 italic bg-slate-900/60 p-2 rounded border border-slate-800">
                                      &ldquo;{p.key_findings}&rdquo;
                                    </p>
                                    {p.url && (
                                      <a
                                        href={p.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="inline-flex items-center gap-1 text-[11px] text-cyan-400 hover:underline mt-2"
                                      >
                                        View Citation ({p.doi_or_pmid}) <ExternalLink className="w-3 h-3" />
                                      </a>
                                    )}
                                  </div>
                                ))}
                              </div>
                            )}

                            {/* Red Flags Alert */}
                            {disease.red_flags && disease.red_flags.length > 0 && (
                              <div className="p-3 rounded-lg bg-red-950/30 border border-red-500/40 text-xs">
                                <div className="flex items-center gap-2 font-semibold text-red-400 mb-1">
                                  <AlertTriangle className="w-4 h-4 text-red-400" /> Emergency Red Flags
                                </div>
                                <ul className="list-disc list-inside space-y-1 text-slate-300 text-xs">
                                  {disease.red_flags.map((rf, i) => (
                                    <li key={i}>{rf}</li>
                                  ))}
                                </ul>
                              </div>
                            )}

                            {/* Doctor Consultation Checklist */}
                            {disease.doctor_checklist && (
                              <div className="p-3 rounded-lg bg-slate-900 border border-slate-800 text-xs space-y-1.5">
                                <span className="font-semibold text-cyan-400 block mb-1">
                                  📋 Doctor Consultation Checklist:
                                </span>
                                <p className="text-slate-300">
                                  <strong>Parameter Question:</strong> {disease.doctor_checklist.parameter_question}
                                </p>
                                <p className="text-slate-300">
                                  <strong>Safety Question:</strong> {disease.doctor_checklist.safety_question}
                                </p>
                                <p className="text-slate-300">
                                  <strong>Action Threshold Question:</strong> {disease.doctor_checklist.action_threshold_question}
                                </p>
                              </div>
                            )}

                            {/* Action to Launch in Assistant */}
                            <div className="pt-2 flex justify-end">
                              <button
                                onClick={() => handleLaunchInAssistant(disease.name)}
                                className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 text-xs font-semibold shadow-md shadow-cyan-500/20 transition-colors"
                              >
                                <Sparkles className="w-3.5 h-3.5" />
                                Run RAG Query for {disease.name}
                              </button>
                            </div>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          )}

          {/* ─────────────────────────────────────────────────────────────
              TAB 2: SYMPTOM DIFFERENTIAL CHECKER
              ───────────────────────────────────────────────────────────── */}
          {activeTab === "symptom-checker" && (
            <div className="space-y-6">
              {/* Header Box */}
              <div className="p-4 rounded-xl bg-gradient-to-r from-purple-950/40 via-slate-900 to-slate-900 border border-purple-500/30 flex items-start gap-3">
                <div className="w-10 h-10 rounded-lg bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-purple-300 shrink-0 mt-0.5">
                  <Microscope className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-semibold text-purple-200">
                    Autonomous Symptom Differential Diagnostic Matcher
                  </h3>
                  <p className="text-xs text-slate-300 mt-1 leading-relaxed">
                    Select or type multiple patient symptoms. The diagnostic engine maps symptoms across 100+ conditions, weights hallmark markers, intercepts acute red-flags, and calculates match confidence with first-line solutions.
                  </p>
                </div>
              </div>

              {/* Symptom Selector Input */}
              <div className="space-y-3 bg-slate-800/40 p-4 rounded-xl border border-slate-700/60">
                <label className="text-xs font-semibold uppercase text-slate-400 tracking-wider">
                  Active Selected Symptoms ({selectedSymptoms.length})
                </label>

                {/* Selected Tags */}
                <div className="flex flex-wrap gap-2 min-h-9 p-2 bg-slate-900/80 rounded-lg border border-slate-700/80 items-center">
                  {selectedSymptoms.length === 0 ? (
                    <span className="text-xs text-slate-500 italic pl-1">
                      No symptoms selected yet. Click pills below or type custom symptoms.
                    </span>
                  ) : (
                    selectedSymptoms.map((sym) => (
                      <span
                        key={sym}
                        className="inline-flex items-center gap-1.5 text-xs bg-purple-500/20 text-purple-200 border border-purple-500/40 px-2.5 py-1 rounded-md"
                      >
                        {sym}
                        <button
                          onClick={() => toggleSymptom(sym)}
                          className="hover:text-white"
                        >
                          <X className="w-3.5 h-3.5" />
                        </button>
                      </span>
                    ))
                  )}
                </div>

                {/* Custom symptom input form */}
                <form onSubmit={addCustomSymptom} className="flex gap-2">
                  <input
                    type="text"
                    value={customSymptomInput}
                    onChange={(e) => setCustomSymptomInput(e.target.value)}
                    placeholder="Type a symptom (e.g. 'swollen ankles', 'acid reflux', 'wheezing')..."
                    className="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-3.5 py-2 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-purple-400"
                  />
                  <button
                    type="submit"
                    className="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded-lg text-xs font-medium transition-colors"
                  >
                    Add
                  </button>
                </form>

                {/* Quick Add Pills */}
                <div>
                  <span className="text-[11px] text-slate-400 block mb-2 font-medium">
                    Quick-Add Common Symptoms:
                  </span>
                  <div className="flex flex-wrap gap-1.5 max-h-32 overflow-y-auto pr-1">
                    {popularSymptoms.map((s) => {
                      const isSelected = selectedSymptoms.includes(s.name);
                      return (
                        <button
                          key={s.name}
                          onClick={() => toggleSymptom(s.name)}
                          className={`text-xs px-2.5 py-1 rounded-md transition-colors border ${
                            isSelected
                              ? "bg-purple-600 text-white border-purple-500 font-medium"
                              : "bg-slate-800 text-slate-300 border-slate-700 hover:bg-slate-700 hover:text-white"
                          }`}
                        >
                          {isSelected ? "✓ " : "+ "}
                          {s.name}
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Execute Matcher Button */}
                <div className="pt-2 flex justify-end">
                  <button
                    onClick={handleRunSymptomCheck}
                    disabled={selectedSymptoms.length === 0 || checkerLoading}
                    className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white text-xs font-semibold shadow-lg shadow-purple-600/30 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {checkerLoading ? (
                      <>
                        <div className="w-3.5 h-3.5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                        Evaluating Differential...
                      </>
                    ) : (
                      <>
                        <Sparkles className="w-4 h-4" />
                        Run Differential Diagnosis Matcher
                      </>
                    )}
                  </button>
                </div>
              </div>

              {/* Differential Results */}
              {checkerResult && (
                <div className="space-y-4 animate-in fade-in duration-200">
                  {/* Emergency Banner if triggered */}
                  {checkerResult.emergency_alert && (
                    <div className="p-4 rounded-xl bg-red-950/50 border border-red-500/70 text-red-200 flex items-start gap-3 shadow-lg shadow-red-950/40">
                      <ShieldAlert className="w-6 h-6 text-red-400 shrink-0 mt-0.5" />
                      <div>
                        <h4 className="font-bold text-sm text-red-300">
                          Critical Emergency Triage Alert
                        </h4>
                        <p className="text-xs text-red-200 mt-1 leading-relaxed">
                          {checkerResult.emergency_alert}
                        </p>
                      </div>
                    </div>
                  )}

                  <div className="flex items-center justify-between">
                    <h4 className="text-sm font-bold text-slate-200 uppercase tracking-wider">
                      Differential Diagnosis Candidate Matches ({checkerResult.top_matches.length})
                    </h4>
                    <span className="text-xs text-slate-400">
                      Evaluated across {checkerResult.total_conditions_evaluated} clinical conditions
                    </span>
                  </div>

                  <div className="space-y-4">
                    {checkerResult.top_matches.map((match, i) => (
                      <div
                        key={match.disease_id}
                        className="p-4 rounded-xl bg-slate-800/60 border border-slate-700/80 hover:border-slate-600 transition-all space-y-3"
                      >
                        <div className="flex items-start justify-between gap-3">
                          <div>
                            <div className="flex items-center gap-2">
                              <span className="w-5 h-5 rounded-full bg-purple-500/20 text-purple-300 text-xs font-bold flex items-center justify-center">
                                {i + 1}
                              </span>
                              <h5 className="text-base font-semibold text-white">
                                {match.disease_name}
                              </h5>
                              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">
                                {match.icd10_code}
                              </span>
                            </div>
                            <span className="text-xs text-cyan-400 block mt-0.5 ml-7">
                              {match.specialty}
                            </span>
                          </div>

                          {/* Match Score Meter */}
                          <div className="text-right">
                            <span className="text-lg font-black text-emerald-400">
                              {match.match_score}%
                            </span>
                            <span className="text-[10px] text-slate-400 block">Match Confidence</span>
                          </div>
                        </div>

                        {/* Symptoms Overlap Breakdown */}
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                          <div className="p-2.5 rounded-lg bg-emerald-950/20 border border-emerald-500/30">
                            <span className="font-semibold text-emerald-300 block mb-1">
                              ✓ Matched Reported Symptoms:
                            </span>
                            <div className="flex flex-wrap gap-1">
                              {match.matched_symptoms.map((s, idx) => (
                                <span
                                  key={idx}
                                  className="text-[11px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-200"
                                >
                                  {s}
                                </span>
                              ))}
                            </div>
                          </div>

                          <div className="p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
                            <span className="font-semibold text-slate-400 block mb-1">
                              Typical Manifestations Not Reported:
                            </span>
                            <div className="flex flex-wrap gap-1">
                              {match.missing_typical_symptoms.map((s, idx) => (
                                <span
                                  key={idx}
                                  className="text-[11px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400"
                                >
                                  {s}
                                </span>
                              ))}
                            </div>
                          </div>
                        </div>

                        {/* First-line solution snippet */}
                        {match.first_line_solutions.length > 0 && (
                          <div className="p-2.5 rounded-lg bg-cyan-950/20 border border-cyan-500/30 text-xs">
                            <strong className="text-cyan-300">
                              Recommended GDMT First-Line Protocol:
                            </strong>{" "}
                            <span className="text-slate-200">
                              {match.first_line_solutions[0].name} — {match.first_line_solutions[0].description.slice(0, 160)}...
                            </span>
                          </div>
                        )}

                        {/* Doctor Consultation Next Step */}
                        <div className="flex items-center justify-between text-xs pt-1">
                          <span className="text-slate-400 italic">
                            Action: {match.recommended_action}
                          </span>
                          <button
                            onClick={() => handleLaunchInAssistant(match.disease_name)}
                            className="inline-flex items-center gap-1.5 text-cyan-400 hover:text-cyan-300 font-semibold"
                          >
                            Explore full monograph <ArrowRight className="w-3.5 h-3.5" />
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>

                  <p className="text-[11px] text-slate-500 italic mt-3 text-center">
                    {checkerResult.disclaimer}
                  </p>
                </div>
              )}
            </div>
          )}

          {/* ─────────────────────────────────────────────────────────────
              TAB 3: GDMT SOLUTIONS & PROTOCOLS
              ───────────────────────────────────────────────────────────── */}
          {activeTab === "solutions" && (
            <div className="space-y-4">
              <div className="flex items-center justify-between flex-wrap gap-3">
                <div>
                  <h3 className="text-base font-semibold text-white">
                    Guideline-Directed Medical Therapy (GDMT) Solutions
                  </h3>
                  <p className="text-xs text-slate-400">
                    Verified pharmacological therapies, organ-clearance thresholds, and non-pharmacological protocols.
                  </p>
                </div>

                <div className="flex items-center gap-2">
                  <span className="text-xs text-slate-400">Filter:</span>
                  <select
                    value={solutionTypeFilter}
                    onChange={(e) => setSolutionTypeFilter(e.target.value)}
                    className="bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1 text-xs text-slate-200 focus:outline-none focus:border-cyan-400"
                  >
                    <option value="all">All Modalities</option>
                    <option value="pharmacological">Pharmacological Rx</option>
                    <option value="lifestyle">Lifestyle & Nutrition</option>
                    <option value="non_pharmacological">Non-Pharmacological</option>
                  </select>
                </div>
              </div>

              {loadingSolutions ? (
                <div className="py-16 text-center text-slate-400">
                  <div className="w-8 h-8 border-2 border-emerald-400 border-t-transparent rounded-full animate-spin mx-auto mb-2"></div>
                  <p className="text-xs">Loading evidence-backed solutions...</p>
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {solutionsList.map((item, idx) => {
                    const sol = item.solution;
                    return (
                      <div
                        key={idx}
                        className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/70 hover:border-emerald-500/40 space-y-2 text-xs"
                      >
                        <div className="flex items-start justify-between gap-2">
                          <div>
                            <span className="font-semibold text-emerald-300 text-sm block">
                              {sol.name}
                            </span>
                            <span className="text-[11px] text-cyan-400">
                              Indication: {item.disease_name} ({item.specialty})
                            </span>
                          </div>
                          <span className="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                            {sol.line_of_therapy.replace("_", " ")}
                          </span>
                        </div>

                        <p className="text-slate-300 leading-relaxed">
                          {sol.description}
                        </p>

                        {sol.dosage_or_protocol && (
                          <div className="p-2 rounded bg-slate-900 border border-slate-800 text-[11px]">
                            <strong className="text-slate-300">Dosing / Protocol:</strong> {sol.dosage_or_protocol}
                          </div>
                        )}

                        {sol.contraindications && sol.contraindications.length > 0 && (
                          <div className="text-[11px] text-red-300">
                            <strong>Contraindications:</strong> {sol.contraindications.join(", ")}
                          </div>
                        )}

                        {sol.monitoring && (
                          <div className="text-[11px] text-amber-300/90">
                            <strong>Monitoring:</strong> {sol.monitoring}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          )}

          {/* ─────────────────────────────────────────────────────────────
              TAB 4: OXFORD CEBM RESEARCH TRIALS
              ───────────────────────────────────────────────────────────── */}
          {activeTab === "research" && (
            <div className="space-y-4">
              <div className="flex items-center justify-between flex-wrap gap-3">
                <div>
                  <h3 className="text-base font-semibold text-white">
                    Oxford CEBM Peer-Reviewed Trials Library
                  </h3>
                  <p className="text-xs text-slate-400">
                    Landmark randomized controlled trials, systematic reviews, and consensus guidelines (NEJM, Lancet, JAMA).
                  </p>
                </div>

                <div className="flex items-center gap-2">
                  <span className="text-xs text-slate-400">Evidence Level:</span>
                  <select
                    value={cebmFilter}
                    onChange={(e) => setCebmFilter(e.target.value)}
                    className="bg-slate-800 border border-slate-700 rounded-lg px-2.5 py-1 text-xs text-slate-200 focus:outline-none focus:border-cyan-400"
                  >
                    <option value="all">All Evidence Levels</option>
                    <option value="Level 1">Level 1 (Meta-Analyses / Systematic Reviews)</option>
                    <option value="Level 2">Level 2 (Randomized Controlled Trials)</option>
                  </select>
                </div>
              </div>

              {loadingPapers ? (
                <div className="py-16 text-center text-slate-400">
                  <div className="w-8 h-8 border-2 border-amber-400 border-t-transparent rounded-full animate-spin mx-auto mb-2"></div>
                  <p className="text-xs">Loading landmark research papers...</p>
                </div>
              ) : (
                <div className="space-y-3">
                  {papersList.map((item, idx) => {
                    const p = item.paper;
                    return (
                      <div
                        key={idx}
                        className="p-4 rounded-xl bg-slate-800/40 border border-slate-700/70 hover:border-blue-500/40 space-y-2 text-xs"
                      >
                        <div className="flex items-start justify-between gap-3 flex-wrap">
                          <div className="space-y-0.5">
                            <span className="text-sm font-semibold text-white block">
                              {p.title}
                            </span>
                            <span className="text-xs text-cyan-400">
                              Clinical Condition: {item.disease_name} (ICD-10: {item.icd10})
                            </span>
                          </div>
                          <span className="text-xs px-2.5 py-1 rounded-md bg-blue-500/20 text-blue-300 font-semibold border border-blue-500/30">
                            {p.cebm_level}
                          </span>
                        </div>

                        <div className="flex items-center gap-3 text-xs text-slate-400">
                          <span className="font-medium text-slate-300">{p.journal}</span>
                          <span>•</span>
                          <span>{p.year}</span>
                          <span>•</span>
                          <span>{p.study_design}</span>
                        </div>

                        <div className="p-3 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-200 leading-relaxed italic">
                          &ldquo;{p.key_findings}&rdquo;
                        </div>

                        <div className="flex items-center justify-between pt-1">
                          <span className="text-[11px] text-slate-400">
                            <strong>Takeaway:</strong> {p.clinical_takeaway}
                          </span>

                          {p.url && (
                            <a
                              href={p.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="inline-flex items-center gap-1 text-xs text-cyan-400 hover:text-cyan-300 font-medium"
                            >
                              DOI / Source <ExternalLink className="w-3.5 h-3.5" />
                            </a>
                          )}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          )}

        </div>

        {/* Modal Footer */}
        <div className="p-4 border-t border-slate-800 bg-slate-900/90 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400">
          <div className="flex items-center gap-2">
            <Info className="w-4 h-4 text-cyan-400 shrink-0" />
            <span>
              All database records are cross-validated against WHO, ACC/AHA, ESC, ADA, and GINA consensus guidelines.
            </span>
          </div>

          <button
            onClick={onClose}
            className="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-medium transition-colors"
          >
            Close Explorer
          </button>
        </div>

      </div>
    </div>
  );
}
