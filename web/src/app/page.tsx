"use client";

import React, { useState, useEffect, useRef } from "react";
import { UserMode, SearchResponse } from "@/lib/types";
import { searchClinicalRAG, searchClinicalTaxonomy, fetchTaxonomyStats, TaxonomyEntity } from "@/lib/api";
import { ClinicianView } from "@/components/clinician-view";
import { PatientView } from "@/components/patient-view";
import { CitationDrawer } from "@/components/citation-drawer";
import { TriageBanner } from "@/components/triage-banner";
import { getMatchingSuggestions, SearchSuggestion } from "@/lib/suggestions";
import { QueryValidationComponent } from "@/components/QueryValidationComponent";
import {
  Search,
  Stethoscope,
  HeartHandshake,
  ShieldCheck,
  Sparkles,
  RefreshCw,
  X,
  ChevronRight,
  HeartPulse,
  ArrowLeft,
  BookOpen,
  Calculator,
  ArrowRight,
  Columns3,
  CheckCircle2,
  Lock,
  ExternalLink,
  Activity
} from "lucide-react";
import { ClinicalCalculatorWidget } from "@/components/clinical-calculator-widget";
import { ClinicalGovernanceAudit } from "@/components/clinical-governance-audit";
import { IntegratedChatThread } from "@/components/integrated-chat-thread";
import { MedicalWikiViewer } from "@/components/medical-wiki-viewer";

export default function Home() {
  const [query, setQuery] = useState("");
  const [mode, setMode] = useState<UserMode>("patient");
  const [compareMode, setCompareMode] = useState(false);
  const [loading, setLoading] = useState(false);
  const [activeCitation, setActiveCitation] = useState<number | null>(null);

  const [result, setResult] = useState<SearchResponse | null>(null);
  const [patientResult, setPatientResult] = useState<SearchResponse | null>(null);
  const [showCalculator, setShowCalculator] = useState<boolean>(false);
  const [showAuditGovernance, setShowAuditGovernance] = useState<boolean>(false);

  // Primary Workspace View: 'assistant' | 'wiki' | 'split'
  const [primaryView, setPrimaryView] = useState<"assistant" | "wiki" | "split">("assistant");
  const [selectedWikiTopicId, setSelectedWikiTopicId] = useState<string>("DOC-CARD-001");

  // Autocomplete state
  const [isFocused, setIsFocused] = useState(false);
  const [filteredSuggestions, setFilteredSuggestions] = useState<SearchSuggestion[]>([]);
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);
  const [taxonomyResults, setTaxonomyResults] = useState<TaxonomyEntity[]>([]);
  const [taxonomyStats, setTaxonomyStats] = useState<{ total_conditions: number; cms_icd10_count: number; who_icd11_count: number } | null>(null);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const hasTopic = Boolean(result || patientResult || loading);

  // Fetch taxonomy stats on mount
  useEffect(() => {
    fetchTaxonomyStats()
      .then((data) => setTaxonomyStats(data))
      .catch((err) => console.debug("Taxonomy stats notice:", err));
  }, []);

  // Update suggestions when query changes
  useEffect(() => {
    const list = getMatchingSuggestions(query, 5);
    setFilteredSuggestions(list);
    setSelectedIndex(-1);

    if (query.trim().length >= 2) {
      const timer = setTimeout(() => {
        searchClinicalTaxonomy(query.trim(), undefined, 3)
          .then((res) => setTaxonomyResults(res.results || []))
          .catch(() => setTaxonomyResults([]));
      }, 120);
      return () => clearTimeout(timer);
    } else {
      setTaxonomyResults([]);
    }
  }, [query]);

  // Click outside to close autocomplete
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node) &&
        inputRef.current &&
        !inputRef.current.contains(event.target as Node)
      ) {
        setIsFocused(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Curated prominent queries for instant demonstration
  const featuredQueries = [
    {
      title: "Hypertension Guidelines",
      subtitle: "First-line therapies with renal protection (microalbuminuria)",
      query: "What are the first-line medication options for stage 2 hypertension with microalbuminuria?",
      tag: "ACC/AHA",
      icon: "💊"
    },
    {
      title: "Chest Pain Triage",
      subtitle: "Crushing substernal pressure with left arm radiation",
      query: "I have severe crushing substernal chest pain, cold sweats, and difficulty breathing",
      tag: "Emergency Check",
      icon: "🚨"
    },
    {
      title: "Diabetes & GLP-1/SGLT2i",
      subtitle: "Cardiorenal risk reduction and titration schedule",
      query: "Semaglutide cardiovascular outcomes and titration schedule in Type 2 Diabetes",
      tag: "ADA 2024",
      icon: "🩸"
    },
    {
      title: "Asthma Controller Therapy",
      subtitle: "GINA guidelines on SMART regimen for mild-to-moderate asthma",
      query: "What is the recommended inhaler approach for mild to moderate asthma?",
      tag: "GINA",
      icon: "🫁"
    }
  ];

  const handleOpenWikiTopic = (topicIdOrName: string) => {
    setSelectedWikiTopicId(topicIdOrName);
    setPrimaryView("wiki");
    setIsFocused(false);
  };

  const handleSearch = async (overrideQuery?: string, targetMode?: UserMode) => {
    const q = overrideQuery || query;
    if (!q.trim()) return;

    setPrimaryView("assistant");
    setIsFocused(false);
    setLoading(true);
    setActiveCitation(null);

    const currentMode = targetMode || mode;

    if (compareMode) {
      const [proRes, patRes] = await Promise.all([
        searchClinicalRAG(q, "professional"),
        searchClinicalRAG(q, "patient"),
      ]);
      setResult(proRes);
      setPatientResult(patRes);
    } else {
      const res = await searchClinicalRAG(q, currentMode);
      setResult(res);
      setPatientResult(null);
    }

    setLoading(false);
  };

  const handleSelectSuggestion = (sug: SearchSuggestion) => {
    setQuery(sug.query);
    setIsFocused(false);
    handleSearch(sug.query);
  };

  const handleClearTopic = () => {
    setResult(null);
    setPatientResult(null);
    setQuery("");
    setIsFocused(false);
    setActiveCitation(null);
    setPrimaryView("assistant");
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (!isFocused || filteredSuggestions.length === 0) return;

    if (e.key === "ArrowDown") {
      e.preventDefault();
      setSelectedIndex((prev) => (prev < filteredSuggestions.length - 1 ? prev + 1 : 0));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setSelectedIndex((prev) => (prev > 0 ? prev - 1 : filteredSuggestions.length - 1));
    } else if (e.key === "Enter") {
      if (selectedIndex >= 0 && selectedIndex < filteredSuggestions.length) {
        e.preventDefault();
        handleSelectSuggestion(filteredSuggestions[selectedIndex]);
      }
    } else if (e.key === "Escape") {
      setIsFocused(false);
    }
  };

  const handleSelectCitation = (index: number) => {
    setActiveCitation(index);
    const element = document.getElementById(`source-${index}`);
    if (element) {
      element.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }
  };

  const activeQueryText = result?.query || patientResult?.query || query;

  return (
    <div className="min-h-screen bg-[#F8FAFC] text-slate-900 font-sans selection:bg-indigo-100 selection:text-indigo-900">
      {/* ================= REFINED TOP NAVBAR ================= */}
      <header className="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-slate-200/70">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
          {/* Brand Logo */}
          <div
            onClick={handleClearTopic}
            className="flex items-center gap-2.5 cursor-pointer select-none group"
          >
            <div className="w-9 h-9 rounded-xl bg-slate-900 text-white flex items-center justify-center shadow-xs group-hover:bg-indigo-600 transition-colors">
              <HeartPulse className="w-5 h-5 text-indigo-400 group-hover:text-white transition-colors" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-base font-extrabold tracking-tight text-slate-900">AegisMed</span>
                <span className="text-[10px] font-bold tracking-wider uppercase px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 border border-slate-200">
                  Clinical AI
                </span>
              </div>
            </div>
          </div>

          {/* Center Navigation Tabs */}
          <nav className="hidden md:flex items-center gap-1 p-1 bg-slate-100/80 rounded-xl border border-slate-200/60">
            <button
              type="button"
              onClick={() => {
                setPrimaryView("assistant");
                setShowCalculator(false);
                setShowAuditGovernance(false);
              }}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                primaryView === "assistant" && !showCalculator && !showAuditGovernance
                  ? "bg-white text-slate-900 shadow-xs font-bold"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
              <span>AI Assistant</span>
            </button>

            <button
              type="button"
              onClick={() => {
                setPrimaryView("wiki");
                setShowCalculator(false);
                setShowAuditGovernance(false);
              }}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                primaryView === "wiki" && !showCalculator && !showAuditGovernance
                  ? "bg-white text-slate-900 shadow-xs font-bold"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <BookOpen className="w-3.5 h-3.5 text-slate-500" />
              <span>Medical Library</span>
              <span className="text-[10px] px-1 rounded bg-slate-200/80 text-slate-700">600</span>
            </button>

            <button
              type="button"
              onClick={() => {
                setShowCalculator(!showCalculator);
                setShowAuditGovernance(false);
              }}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                showCalculator
                  ? "bg-white text-slate-900 shadow-xs font-bold"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <Calculator className="w-3.5 h-3.5 text-slate-500" />
              <span>Calculators</span>
            </button>

            <button
              type="button"
              onClick={() => {
                setShowAuditGovernance(!showAuditGovernance);
                setShowCalculator(false);
              }}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                showAuditGovernance
                  ? "bg-white text-slate-900 shadow-xs font-bold"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" />
              <span>Safety & Audit</span>
            </button>
          </nav>

          {/* Right Mode Toggle */}
          <div className="flex items-center gap-2">
            <div className="flex items-center p-1 bg-slate-100 rounded-xl border border-slate-200/80">
              <button
                type="button"
                onClick={() => {
                  setCompareMode(false);
                  setMode("patient");
                  if (result) handleSearch(query, "patient");
                }}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                  !compareMode && mode === "patient"
                    ? "bg-white text-indigo-700 shadow-2xs font-bold"
                    : "text-slate-500 hover:text-slate-900"
                }`}
              >
                <HeartHandshake className="w-3.5 h-3.5" />
                <span>Patient</span>
              </button>
              <button
                type="button"
                onClick={() => {
                  setCompareMode(false);
                  setMode("professional");
                  if (result) handleSearch(query, "professional");
                }}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                  !compareMode && mode === "professional"
                    ? "bg-white text-teal-700 shadow-2xs font-bold"
                    : "text-slate-500 hover:text-slate-900"
                }`}
              >
                <Stethoscope className="w-3.5 h-3.5" />
                <span>Clinician</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* ================= POPUP MODALS: CALCULATOR & AUDIT ================= */}
      {showCalculator && (
        <div className="max-w-5xl mx-auto px-4 sm:px-6 pt-6 animate-fade-in">
          <ClinicalCalculatorWidget onClose={() => setShowCalculator(false)} />
        </div>
      )}

      {showAuditGovernance && (
        <div className="max-w-5xl mx-auto px-4 sm:px-6 pt-6 animate-fade-in">
          <ClinicalGovernanceAudit onClose={() => setShowAuditGovernance(false)} />
        </div>
      )}

      {/* ================= LANDING HERO (Clean, Premium, Authoritative) ================= */}
      {!hasTopic && primaryView === "assistant" && !showCalculator && !showAuditGovernance ? (
        <section className="max-w-3xl mx-auto px-4 sm:px-6 pt-16 sm:pt-20 pb-16 text-center animate-fade-in">
          {/* Subtle Trust Pill */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 border border-slate-200 text-slate-700 text-xs font-medium mb-6">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>Grounded in Peer-Reviewed Medical Guidelines (ACC/AHA, ESC, ADA, GINA)</span>
          </div>

          {/* Authoritative Main Headline */}
          <h1 className="text-4xl sm:text-5xl font-extrabold text-slate-900 tracking-tight leading-tight mb-4">
            Medical answers, <br className="hidden sm:inline" />
            <span className="bg-gradient-to-r from-indigo-600 to-blue-600 bg-clip-text text-transparent">
              verified by evidence.
            </span>
          </h1>

          <p className="text-slate-600 text-base sm:text-lg max-w-xl mx-auto mb-10 leading-relaxed">
            Consult the AI clinical engine with zero hallucinations. Every response provides Oxford CEBM citation traceability, dosage thresholds, and drug safety checks.
          </p>

          {/* Floating Search Input Card */}
          <div className="relative mb-8 text-left">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSearch();
              }}
              className="relative flex items-center w-full h-16 bg-white rounded-2xl border border-slate-200/90 shadow-[0_4px_20px_-4px_rgba(0,0,0,0.06)] focus-within:border-indigo-500 focus-within:ring-4 focus-within:ring-indigo-50/80 transition-all"
            >
              <div className="pl-5 text-slate-400">
                <Search className="w-5 h-5" />
              </div>

              <input
                ref={inputRef}
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onFocus={() => setIsFocused(true)}
                onKeyDown={handleKeyDown}
                placeholder={
                  mode === "patient"
                    ? "Ask in plain English (e.g. Stage 2 high blood pressure with kidney protection)..."
                    : "Enter diagnostic query, GDMT titration, or contraindication check..."
                }
                className="w-full h-full pl-3.5 pr-36 bg-transparent text-slate-900 placeholder:text-slate-400 text-sm sm:text-base outline-none"
              />

              <div className="absolute right-2.5 flex items-center gap-1.5">
                {query && (
                  <button
                    type="button"
                    onClick={() => {
                      setQuery("");
                      inputRef.current?.focus();
                    }}
                    className="p-1.5 text-slate-400 hover:text-slate-600 rounded-lg transition-colors"
                  >
                    <X className="w-4 h-4" />
                  </button>
                )}

                <button
                  type="submit"
                  disabled={loading || !query.trim()}
                  className="px-5 py-2.5 h-11 rounded-xl bg-slate-900 hover:bg-indigo-600 text-white font-semibold text-xs sm:text-sm tracking-wide transition-all shadow-xs disabled:opacity-40 flex items-center gap-2"
                >
                  {loading ? (
                    <RefreshCw className="w-4 h-4 animate-spin" />
                  ) : (
                    <>
                      <span>Ask AI</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </>
                  )}
                </button>
              </div>
            </form>

            {/* Autocomplete Dropdown */}
            {isFocused && (filteredSuggestions.length > 0 || taxonomyResults.length > 0) && (
              <div
                ref={dropdownRef}
                className="absolute left-0 right-0 top-full mt-2 bg-white border border-slate-200 rounded-xl shadow-lg z-50 text-left overflow-hidden divide-y divide-slate-100"
              >
                <div className="p-2 max-h-56 overflow-y-auto">
                  {filteredSuggestions.map((sug, idx) => (
                    <div
                      key={sug.id}
                      onClick={() => handleSelectSuggestion(sug)}
                      className={`px-3 py-2 rounded-lg cursor-pointer transition-colors flex items-center justify-between gap-3 ${
                        selectedIndex === idx ? "bg-indigo-50" : "hover:bg-slate-50"
                      }`}
                    >
                      <div className="min-w-0">
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-bold text-slate-900 truncate">
                            {sug.label}
                          </span>
                          <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-100 text-slate-600">
                            {sug.healthBody}
                          </span>
                        </div>
                        <p className="text-[11px] text-slate-500 truncate mt-0.5">
                          {sug.description}
                        </p>
                      </div>
                      <ChevronRight className="w-3.5 h-3.5 text-slate-400 shrink-0" />
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div className="mt-2 text-left">
              <QueryValidationComponent
                query={query}
                compact={true}
                onApplyCorrection={(corrected) => {
                  setQuery(corrected);
                  handleSearch(corrected);
                }}
              />
            </div>
          </div>

          {/* Curated Prompt Cards (2x2 Clean Grid) */}
          <div className="text-left mt-8">
            <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-3">
              Explore Common Clinical Scenarios:
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {featuredQueries.map((item, idx) => (
                <div
                  key={idx}
                  onClick={() => {
                    setQuery(item.query);
                    handleSearch(item.query);
                  }}
                  className="p-3.5 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-300 hover:shadow-xs cursor-pointer transition-all flex items-start gap-3 group"
                >
                  <span className="text-lg shrink-0 mt-0.5">{item.icon}</span>
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center justify-between gap-2">
                      <span className="text-xs font-bold text-slate-900 group-hover:text-indigo-600 transition-colors">
                        {item.title}
                      </span>
                      <span className="text-[10px] font-semibold px-1.5 py-0.2 rounded bg-slate-100 text-slate-600">
                        {item.tag}
                      </span>
                    </div>
                    <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                      {item.subtitle}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Minimalist Trust Badges */}
          <div className="flex flex-wrap items-center justify-center gap-6 mt-12 text-xs text-slate-500">
            <span className="flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-600" />
              <span>Zero-Hallucination Guardrails</span>
            </span>
            <span className="flex items-center gap-1.5">
              <Activity className="w-4 h-4 text-indigo-600" />
              <span>Oxford CEBM Level 1-5 Ranking</span>
            </span>
            <span className="flex items-center gap-1.5">
              <Lock className="w-4 h-4 text-slate-600" />
              <span>HIPAA Safe Harbor De-identification</span>
            </span>
          </div>
        </section>
      ) : null}

      {/* ================= COMPACT REFINED TOPIC BAR (When Result is Active) ================= */}
      {hasTopic && primaryView === "assistant" && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-2 animate-fade-in">
          <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 pb-4 border-b border-slate-200/80 mb-6">
            <div className="flex items-center gap-3">
              <button
                type="button"
                onClick={handleClearTopic}
                className="p-2 rounded-xl bg-white border border-slate-200 text-slate-600 hover:text-slate-900 hover:bg-slate-50 transition-colors shadow-2xs"
                title="Back to Home"
              >
                <ArrowLeft className="w-4 h-4" />
              </button>
              <div>
                <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400">
                  {mode === "professional" ? "Clinician Protocol" : "Patient Guide"}
                </span>
                <h2 className="text-xl font-bold text-slate-900 leading-tight">
                  {activeQueryText}
                </h2>
              </div>
            </div>

            {/* Quick Toggle Mode on Result Screen */}
            <div className="flex items-center gap-2 self-start sm:self-center">
              <div className="flex items-center p-1 bg-slate-100 rounded-xl border border-slate-200">
                <button
                  type="button"
                  onClick={() => {
                    setCompareMode(false);
                    setMode("patient");
                    handleSearch(activeQueryText, "patient");
                  }}
                  className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                    !compareMode && mode === "patient" ? "bg-white text-indigo-700 shadow-2xs font-bold" : "text-slate-500"
                  }`}
                >
                  Patient View
                </button>
                <button
                  type="button"
                  onClick={() => {
                    setCompareMode(false);
                    setMode("professional");
                    handleSearch(activeQueryText, "professional");
                  }}
                  className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                    !compareMode && mode === "professional" ? "bg-white text-teal-700 shadow-2xs font-bold" : "text-slate-500"
                  }`}
                >
                  Clinician View
                </button>
              </div>

              <button
                type="button"
                onClick={() => setCompareMode(!compareMode)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold border transition-all ${
                  compareMode
                    ? "bg-purple-600 text-white border-purple-600 shadow-xs"
                    : "bg-white text-slate-700 border-slate-200 hover:bg-slate-50"
                }`}
                title="Compare Patient and Clinician side-by-side"
              >
                <Columns3 className="w-3.5 h-3.5" />
                <span>Compare</span>
              </button>
            </div>
          </div>
        </section>
      )}

      {/* ================= RESULTS / WIKI / SPLIT WORKSPACE ================= */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {primaryView === "wiki" ? (
          <div className="py-6 animate-fade-in">
            <MedicalWikiViewer
              initialTopicId={selectedWikiTopicId}
              mode={mode === "professional" ? "clinician" : "patient"}
              onModeChange={(newMode) => setMode(newMode === "clinician" ? "professional" : "patient")}
              embedded={true}
              onSelectQueryForAssistant={(q) => {
                setQuery(q);
                setPrimaryView("assistant");
                handleSearch(q);
              }}
            />
          </div>
        ) : primaryView === "split" ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start py-6 animate-fade-in">
            <div className="lg:col-span-7 h-[85vh]">
              <MedicalWikiViewer
                initialTopicId={selectedWikiTopicId}
                mode={mode === "professional" ? "clinician" : "patient"}
                onModeChange={(newMode) => setMode(newMode === "clinician" ? "professional" : "patient")}
                embedded={true}
                onSelectQueryForAssistant={(q) => {
                  setQuery(q);
                  handleSearch(q);
                }}
              />
            </div>
            <div className="lg:col-span-5 h-[85vh] bg-white border border-slate-200 rounded-2xl shadow-xs p-4 flex flex-col overflow-hidden">
              <IntegratedChatThread
                initialTopic={query || selectedWikiTopicId}
                mode={mode}
                response={result}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>
          </div>
        ) : loading ? (
          /* Sleek Loading State */
          <div className="p-12 bg-white border border-slate-200/80 rounded-2xl text-center shadow-xs animate-fade-in space-y-4 max-w-lg mx-auto my-12">
            <div className="w-12 h-12 rounded-xl bg-indigo-50 flex items-center justify-center mx-auto text-indigo-600">
              <RefreshCw className="w-5 h-5 animate-spin" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-900">
                Synthesizing Evidence & Safety Guardrails...
              </h3>
              <p className="text-xs text-slate-500 mt-1">
                Cross-referencing Oxford CEBM guidelines with deterministic clinical safety rules.
              </p>
            </div>
          </div>
        ) : compareMode && result && patientResult ? (
          /* Dual Perspective Compare View */
          <div className="space-y-6 pb-16">
            {result?.triage_alert && (
              <div className="max-w-4xl mx-auto">
                <TriageBanner alert={result.triage_alert} />
              </div>
            )}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <PatientView
                response={patientResult}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
              <ClinicianView
                response={result}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>
            <div className="mt-8">
              <CitationDrawer
                sources={result.sources}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>
          </div>
        ) : result ? (
          /* Single Perspective + Evidence Drawer Layout */
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start pb-16">
            <div className="lg:col-span-8 space-y-6">
              {result?.triage_alert && <TriageBanner alert={result.triage_alert} />}

              {mode === "professional" ? (
                <ClinicianView
                  response={result}
                  activeCitation={activeCitation}
                  onSelectCitation={handleSelectCitation}
                />
              ) : (
                <PatientView
                  response={result}
                  activeCitation={activeCitation}
                  onSelectCitation={handleSelectCitation}
                />
              )}

              <IntegratedChatThread
                initialTopic={activeQueryText}
                mode={mode}
                response={result}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>

            {/* Evidence Sidebar */}
            <div className="lg:col-span-4 sticky top-24">
              <CitationDrawer
                sources={result.sources}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>
          </div>
        ) : null}
      </main>

      {/* ================= REFINED FOOTER ================= */}
      <footer className="border-t border-slate-200/80 mt-20 py-8 bg-white/50 text-center text-xs text-slate-400">
        <p className="max-w-xl mx-auto leading-relaxed">
          AegisMed is an evidence-based clinical decision support tool grounded in peer-reviewed medical literature. Not a substitute for formal in-person clinical diagnosis.
        </p>
      </footer>
    </div>
  );
}
