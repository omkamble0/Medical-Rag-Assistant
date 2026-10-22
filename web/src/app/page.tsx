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
  Columns3,
  Flame,
  Globe2,
  X,
  ChevronRight,
  HeartPulse,
  Award,
  CheckCircle2,
  ArrowLeft,
  BookOpen,
  SlidersHorizontal,
  Clock,
  Layers,
  Wand2,
  Calculator,
  Compass,
  ArrowRight
} from "lucide-react";
import { ClinicalCalculatorWidget } from "@/components/clinical-calculator-widget";
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
  
  // Primary Workspace View: 'wiki' | 'assistant' | 'split'
  const [primaryView, setPrimaryView] = useState<"assistant" | "wiki" | "split">("wiki");
  const [selectedWikiTopicId, setSelectedWikiTopicId] = useState<string>("DOC-CARD-001");
  const [searchTarget, setSearchTarget] = useState<"all" | "wiki" | "assistant">("all");

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

  const searchPlaceholder =
    searchTarget === "wiki"
      ? "Search 600 Wiki articles or 133,000+ CMS & WHO ICD codes..."
      : searchTarget === "assistant"
      ? "Ask AI Clinical Assistant any diagnostic or clinical query..."
      : mode === "patient"
      ? "Describe your symptoms or ask a health question..."
      : "Search clinical guidelines, trials, or treatment protocols...";

  // Update suggestions & taxonomy matches when query changes
  useEffect(() => {
    const list = getMatchingSuggestions(query, 6);
    setFilteredSuggestions(list);
    setSelectedIndex(-1);

    if (query.trim().length >= 2) {
      const timer = setTimeout(() => {
        searchClinicalTaxonomy(query.trim(), undefined, 4)
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

  // Preset popular conditions
  const popularPills = [
    { label: "High Blood Pressure", query: "What are the first-line treatments and DASH diet guidelines for high blood pressure?", badge: "WHO / AHA", icon: "❤️" },
    { label: "Diabetes & GLP-1", query: "Semaglutide cardiovascular outcomes and titration schedule in Type 2 Diabetes", badge: "ADA / WHO", icon: "🩸" },
    { label: "Asthma Inhalers", query: "What is the recommended inhaler approach for mild to moderate asthma?", badge: "GINA / WHO", icon: "🫁" },
    { label: "Cholesterol & Statins", query: "Are statin side effects dangerous and what are the alternatives for high cholesterol?", badge: "ESC / AHA", icon: "💊" },
    { label: "Anxiety & Mood", query: "What are the best evidence-based treatments for chronic anxiety and panic disorders?", badge: "NICE / WHO", icon: "🕊️" },
    { label: "COVID & Antivirals", query: "Paxlovid antiviral efficacy and timing in high-risk COVID-19 patients", badge: "CDC / WHO", icon: "🛡️" },
    { label: "Emergency Triage", query: "I have severe crushing chest pain, cold sweats, and cannot breathe", badge: "Safety Check", icon: "🚨" },
  ];

  // Navigation handlers for Medical Wiki integration
  const handleOpenWikiTopic = (topicIdOrName: string) => {
    setSelectedWikiTopicId(topicIdOrName);
    setPrimaryView("wiki");
    setIsFocused(false);
  };

  const handleOpenWikiSplit = (topicIdOrName: string, queryForAssistant?: string) => {
    setSelectedWikiTopicId(topicIdOrName);
    setPrimaryView("split");
    setIsFocused(false);
    if (queryForAssistant) {
      setQuery(queryForAssistant);
      handleSearch(queryForAssistant);
    }
  };

  const handleSearch = async (overrideQuery?: string, targetMode?: UserMode) => {
    const q = overrideQuery || query;
    if (!q.trim()) return;

    // If searchTarget is specifically 'wiki', navigate directly to matching topic
    if (searchTarget === "wiki") {
      const clean = q.toLowerCase().trim();
      const matched = filteredSuggestions.find(
        (s) => s.label.toLowerCase().includes(clean) || clean.includes(s.label.toLowerCase())
      );
      if (matched) {
        handleOpenWikiTopic(matched.id.replace("sug-", ""));
        return;
      }
    }

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
    if (searchTarget === "wiki") {
      handleOpenWikiTopic(sug.id.replace("sug-", ""));
    } else {
      handleSearch(sug.query);
    }
  };

  const handleClearTopic = () => {
    setResult(null);
    setPatientResult(null);
    setQuery("");
    setIsFocused(false);
    setActiveCitation(null);
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

  // Real-time matching against 600 verified wiki topics
  const matchedWikiTopic = React.useMemo(() => {
    if (!activeQueryText || !activeQueryText.trim()) return null;
    const clean = activeQueryText.toLowerCase().trim();
    let found = filteredSuggestions.find((s) => s.label.toLowerCase() === clean);
    if (found) return found;
    found = filteredSuggestions.find(
      (s) => s.label.toLowerCase().includes(clean) || clean.includes(s.label.toLowerCase())
    );
    return found || null;
  }, [activeQueryText, filteredSuggestions]);

  return (
    <main className="min-h-screen bg-[#F6F8FB] text-slate-900 pb-24">
      {/* Top Clean Header */}
      <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-2xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-18 flex items-center justify-between gap-4">
          {/* Logo & Platform Tagline */}
          <div 
            className="flex items-center gap-3 cursor-pointer select-none"
            onClick={handleClearTopic}
            title="Return to AegisMed Home"
          >
            <div className="p-2.5 rounded-2xl bg-gradient-to-tr from-indigo-600 to-blue-500 text-white shadow-sm shadow-indigo-200">
              <HeartPulse className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-bold tracking-tight text-slate-900">
                  AegisMed
                </h1>
                <span className="px-2 py-0.5 text-[11px] font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-full hidden xs:inline-block">
                  Evidence-Based Clinical Engine
                </span>
              </div>
              <p className="text-xs text-slate-500 hidden sm:block">
                {taxonomyStats?.total_conditions
                  ? `${taxonomyStats.total_conditions.toLocaleString()} CMS & WHO Clinical Conditions • 600 Rich Monographs`
                  : "133,000+ CMS & WHO Conditions • 600 Rich Monographs"}
              </p>
            </div>
          </div>

          {/* Primary View Switcher & Audience Controls */}
          <div className="flex items-center gap-2">
            {/* Primary Workspace View Switcher */}
            <div className="flex items-center gap-1 bg-slate-100/90 p-1 rounded-2xl border border-slate-200">
              <button
                type="button"
                onClick={() => setPrimaryView("wiki")}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold transition-all ${
                  primaryView === "wiki"
                    ? "bg-white text-indigo-700 shadow-xs border border-slate-200/80"
                    : "text-slate-600 hover:text-slate-900"
                }`}
                title="Primary Medical Wiki & Clinical Compendium (600 Topics)"
              >
                <BookOpen className="w-4 h-4 text-indigo-600" />
                <span>Medical Wiki</span>
                <span className="hidden xs:inline-block text-[10px] font-extrabold px-1.5 py-0.2 bg-indigo-100 text-indigo-800 rounded-md">
                  600
                </span>
              </button>

              <button
                type="button"
                onClick={() => setPrimaryView("assistant")}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold transition-all ${
                  primaryView === "assistant"
                    ? "bg-white text-indigo-700 shadow-xs border border-slate-200/80"
                    : "text-slate-600 hover:text-slate-900"
                }`}
                title="Interactive AI Clinical Assistant"
              >
                <Sparkles className="w-4 h-4 text-indigo-600" />
                <span>AI Assistant</span>
              </button>

              <button
                type="button"
                onClick={() => setPrimaryView("split")}
                className={`hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs sm:text-sm font-bold transition-all ${
                  primaryView === "split"
                    ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-xs"
                    : "text-slate-600 hover:text-slate-900"
                }`}
                title="Open Medical Wiki on Left and AI Chat Assistant on Right"
              >
                <Columns3 className="w-4 h-4" />
                <span>Co-Pilot Split</span>
              </button>
            </div>

            {/* Audience Perspective Selector */}
            <div className="hidden sm:flex items-center gap-1 bg-slate-100/90 p-1 rounded-2xl border border-slate-200">
              <button
                type="button"
                onClick={() => {
                  setCompareMode(false);
                  setMode("patient");
                  if (result) handleSearch(query, "patient");
                }}
                className={`flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                  !compareMode && mode === "patient"
                    ? "bg-white text-indigo-700 shadow-xs border border-slate-200/80"
                    : "text-slate-600 hover:text-slate-900"
                }`}
                title="Patient & Family plain-language register"
              >
                <HeartHandshake className="w-3.5 h-3.5 text-indigo-600" />
                <span>Patient</span>
              </button>

              <button
                type="button"
                onClick={() => {
                  setCompareMode(false);
                  setMode("professional");
                  if (result) handleSearch(query, "professional");
                }}
                className={`flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                  !compareMode && mode === "professional"
                    ? "bg-white text-teal-700 shadow-xs border border-slate-200/80"
                    : "text-slate-600 hover:text-slate-900"
                }`}
                title="Clinician post-graduate medical register"
              >
                <Stethoscope className="w-3.5 h-3.5 text-teal-600" />
                <span>Clinician</span>
              </button>
            </div>

            {/* Clinical Calculator Button */}
            <button
              type="button"
              onClick={() => setShowCalculator(!showCalculator)}
              className={`flex items-center gap-1 px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                showCalculator
                  ? "bg-indigo-900 text-indigo-300 shadow-sm border border-indigo-700"
                  : "bg-white text-slate-700 hover:text-slate-900 border border-slate-200"
              }`}
              title="Open Clinical Calculators & Drug Interaction Suite"
            >
              <Calculator className="w-3.5 h-3.5 text-indigo-500" />
              <span className="hidden sm:inline">Calculators</span>
            </button>
          </div>
        </div>
      </header>

      {/* Interactive Clinical Calculator & DDI Suite */}
      {showCalculator && (
        <div className="max-w-5xl mx-auto px-4 sm:px-6 pt-4 animate-fade-in">
          <ClinicalCalculatorWidget onClose={() => setShowCalculator(false)} />
        </div>
      )}

      {/* Main Search & Hero Section */}
      {!hasTopic && primaryView === "assistant" ? (
        /* ================= LANDING HERO VIEW (Assistant Mode) ================= */
        <section className="max-w-4xl mx-auto px-4 sm:px-6 pt-8 pb-6 text-center animate-fade-in">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-indigo-100 text-indigo-700 text-xs font-semibold shadow-xs mb-3">
            <Globe2 className="w-3.5 h-3.5 text-indigo-600" />
            <span>Accurate Medical Knowledge Grounded in WHO & Peer-Reviewed Trials</span>
          </div>

          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 tracking-tight mb-3">
            Understand Your Health With Confidence.
          </h2>
          <p className="text-slate-600 text-sm sm:text-base max-w-2xl mx-auto mb-6 leading-relaxed">
            Search 133,000+ official CMS ICD-10 & WHO ICD-11 conditions, explore 600 verified medical wiki monographs, or consult the AI clinical assistant for symptoms and evidence-backed treatments.
          </p>

          {/* Search Scope Filter Pills */}
          <div className="flex items-center justify-center gap-1.5 mb-3">
            <button
              type="button"
              onClick={() => setSearchTarget("all")}
              className={`px-3 py-1 rounded-full text-xs font-bold transition-all ${
                searchTarget === "all"
                  ? "bg-indigo-600 text-white shadow-2xs"
                  : "bg-white text-slate-600 hover:text-slate-900 border border-slate-200"
              }`}
            >
              ✨ Universal
            </button>
            <button
              type="button"
              onClick={() => setSearchTarget("wiki")}
              className={`px-3 py-1 rounded-full text-xs font-bold transition-all flex items-center gap-1 ${
                searchTarget === "wiki"
                  ? "bg-indigo-600 text-white shadow-2xs"
                  : "bg-white text-slate-600 hover:text-slate-900 border border-slate-200"
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Medical Wiki (600)</span>
            </button>
            <button
              type="button"
              onClick={() => setSearchTarget("assistant")}
              className={`px-3 py-1 rounded-full text-xs font-bold transition-all flex items-center gap-1 ${
                searchTarget === "assistant"
                  ? "bg-indigo-600 text-white shadow-2xs"
                  : "bg-white text-slate-600 hover:text-slate-900 border border-slate-200"
              }`}
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span>AI Assistant</span>
            </button>
          </div>

          {/* Hero Search Box */}
          <div className="relative max-w-3xl mx-auto mb-6">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSearch();
              }}
              className="relative flex items-center w-full h-14 sm:h-15 bg-white rounded-2xl border-2 border-slate-200/90 focus-within:border-indigo-600 focus-within:ring-4 focus-within:ring-indigo-100 shadow-md transition-all"
            >
              <div className="absolute left-4 flex items-center pointer-events-none text-slate-400">
                <Search className="w-5 h-5" />
              </div>

              <input
                ref={inputRef}
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onFocus={() => setIsFocused(true)}
                onKeyDown={handleKeyDown}
                placeholder={searchPlaceholder}
                className="w-full h-full pl-12 pr-32 sm:pr-36 bg-transparent text-slate-900 placeholder:text-slate-400 text-sm sm:text-base outline-none font-normal"
              />

              <div className="absolute right-2 flex items-center gap-1.5">
                {query && (
                  <button
                    type="button"
                    onClick={() => {
                      setQuery("");
                      inputRef.current?.focus();
                    }}
                    className="p-2 text-slate-400 hover:text-slate-600 hover:bg-slate-100 rounded-xl transition-colors"
                    title="Clear input"
                  >
                    <X className="w-4 h-4" />
                  </button>
                )}

                <button
                  type="submit"
                  disabled={loading || !query.trim()}
                  className="px-5 sm:px-6 py-2 h-10 sm:h-11 rounded-xl bg-indigo-600 hover:bg-indigo-700 active:scale-98 text-white font-semibold text-xs sm:text-sm tracking-wide transition-all shadow-xs disabled:opacity-50 flex items-center gap-2"
                >
                  {loading ? (
                    <>
                      <RefreshCw className="w-4 h-4 animate-spin" />
                      <span>Searching...</span>
                    </>
                  ) : (
                    <span>Search</span>
                  )}
                </button>
              </div>
            </form>

            {/* Autocomplete Dropdown with Instant Wiki Knowledge Card & 133,000+ CMS/WHO Taxonomy */}
            {isFocused && (filteredSuggestions.length > 0 || taxonomyResults.length > 0) && (
              <div
                ref={dropdownRef}
                className="absolute left-0 right-0 top-full mt-2 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 text-left overflow-hidden animate-fade-in divide-y divide-slate-100"
              >
                {/* Instant Medical Wiki Knowledge Card */}
                {filteredSuggestions.length > 0 && (
                  <>
                    <div className="p-3.5 bg-gradient-to-r from-indigo-50/90 via-purple-50/70 to-blue-50/60 border-b border-indigo-100 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                      <div className="flex items-start gap-2.5">
                        <div className="p-2 bg-white text-indigo-600 rounded-xl shadow-2xs border border-indigo-100 text-base shrink-0">
                          {filteredSuggestions[0].icon || "📖"}
                        </div>
                        <div>
                          <div className="flex items-center gap-1.5 flex-wrap">
                            <span className="text-xs font-bold text-slate-900">
                              {filteredSuggestions[0].label}
                            </span>
                            <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white text-indigo-700 font-bold border border-indigo-200">
                              WikiMed Topic
                            </span>
                            <span className="text-[10px] px-1.5 py-0.5 rounded bg-emerald-50 text-emerald-700 font-semibold border border-emerald-200">
                              {filteredSuggestions[0].category}
                            </span>
                          </div>
                          <p className="text-[11px] text-slate-600 line-clamp-1 mt-0.5 max-w-xl">
                            {filteredSuggestions[0].description}
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center gap-2 self-end sm:self-center shrink-0">
                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleOpenWikiTopic(filteredSuggestions[0].id.replace("sug-", ""));
                          }}
                          className="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold flex items-center gap-1 shadow-2xs transition-all"
                          title="Open full 10-section Wiki article"
                        >
                          <BookOpen className="w-3.5 h-3.5" />
                          <span>Read Wiki</span>
                        </button>

                        <button
                          type="button"
                          onClick={(e) => {
                            e.stopPropagation();
                            handleSelectSuggestion(filteredSuggestions[0]);
                          }}
                          className="px-3 py-1.5 rounded-xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 text-xs font-semibold flex items-center gap-1 shadow-2xs transition-all"
                          title="Ask the AI Assistant"
                        >
                          <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                          <span>Ask AI</span>
                        </button>
                      </div>
                    </div>

                    <div className="px-4 py-2 bg-slate-50/80 border-b border-slate-100 flex items-center justify-between text-xs text-slate-500 font-semibold">
                      <span className="flex items-center gap-1.5">
                        <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                        Matching Wiki Topics & Clinical Guidelines
                      </span>
                      <span className="text-[11px] text-slate-400">Use ↑↓ keys or click</span>
                    </div>

                    <div className="max-h-56 overflow-y-auto divide-y divide-slate-100">
                      {filteredSuggestions.map((sug, idx) => {
                        const isSelected = selectedIndex === idx;
                        return (
                          <div
                            key={sug.id}
                            onClick={() => handleSelectSuggestion(sug)}
                            className={`p-3 sm:px-4 sm:py-2.5 cursor-pointer transition-colors flex items-center justify-between gap-3 ${
                              isSelected ? "bg-indigo-50/80" : "hover:bg-slate-50"
                            }`}
                          >
                            <div className="flex items-start gap-2.5 min-w-0">
                              <span className="text-lg mt-0.5 shrink-0">{sug.icon || "🩺"}</span>
                              <div className="min-w-0">
                                <div className="flex items-center gap-2 flex-wrap">
                                  <span className="text-xs sm:text-sm font-bold text-slate-900 truncate">
                                    {sug.label}
                                  </span>
                                  <span className="px-1.5 py-0.5 rounded text-[9px] font-bold bg-indigo-50 text-indigo-700 border border-indigo-200">
                                    {sug.healthBody}
                                  </span>
                                </div>
                                <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                                  {sug.description}
                                </p>
                              </div>
                            </div>

                            <div className="flex items-center gap-1.5 shrink-0">
                              <button
                                type="button"
                                onClick={(e) => {
                                  e.stopPropagation();
                                  handleOpenWikiTopic(sug.id.replace("sug-", ""));
                                }}
                                className="px-2 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-[11px] font-bold flex items-center gap-1 transition-colors"
                                title="Open 10-section Wiki article directly"
                              >
                                <BookOpen className="w-3 h-3" />
                                <span>Wiki</span>
                              </button>
                              <ChevronRight className="w-4 h-4 text-slate-400 self-center" />
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </>
                )}

                {/* CMS ICD-10 & WHO ICD-11 Master Taxonomy (133,000+ Conditions) */}
                {taxonomyResults.length > 0 && (
                  <div className="bg-slate-50/60">
                    <div className="px-4 py-2 bg-gradient-to-r from-slate-100 via-blue-50/60 to-slate-100 border-b border-slate-200/80 flex items-center justify-between text-xs text-slate-700 font-bold">
                      <span className="flex items-center gap-1.5">
                        <Globe2 className="w-3.5 h-3.5 text-blue-600" />
                        Official CMS ICD-10 & WHO ICD-11 Master Catalog ({taxonomyStats?.total_conditions ? `${taxonomyStats.total_conditions.toLocaleString()} conditions` : "133,000+ conditions"})
                      </span>
                      <span className="text-[10px] text-slate-500 font-mono">FTS5 Search</span>
                    </div>

                    <div className="max-h-56 overflow-y-auto divide-y divide-slate-100">
                      {taxonomyResults.map((tax) => (
                        <div
                          key={`${tax.source}-${tax.id}`}
                          onClick={() => {
                            setQuery(tax.title);
                            setIsFocused(false);
                            handleSearch(tax.title);
                          }}
                          className="p-3 sm:px-4 sm:py-2.5 cursor-pointer hover:bg-white transition-colors flex items-center justify-between gap-3 group"
                        >
                          <div className="flex items-start gap-2.5 min-w-0">
                            <span className="text-base mt-0.5 shrink-0">
                              {tax.source === "CMS_ICD10" ? "🏛️" : "🌐"}
                            </span>
                            <div className="min-w-0">
                              <div className="flex items-center gap-2 flex-wrap">
                                <span className="font-mono text-xs font-bold px-1.5 py-0.5 rounded bg-slate-200 text-slate-800 border border-slate-300">
                                  {tax.code}
                                </span>
                                <span className="text-xs sm:text-sm font-semibold text-slate-900 group-hover:text-indigo-600 transition-colors truncate">
                                  {tax.title}
                                </span>
                                <span
                                  className={`px-1.5 py-0.2 rounded text-[9px] font-bold ${
                                    tax.source === "CMS_ICD10"
                                      ? "bg-blue-50 text-blue-700 border border-blue-200"
                                      : "bg-emerald-50 text-emerald-700 border border-emerald-200"
                                  }`}
                                >
                                  {tax.source === "CMS_ICD10" ? "CMS ICD-10" : "WHO ICD-11"}
                                </span>
                                {tax.has_curated_monograph && (
                                  <span className="px-1.5 py-0.2 rounded text-[9px] font-bold bg-purple-50 text-purple-700 border border-purple-200">
                                    ★ Oxford CEBM Monograph
                                  </span>
                                )}
                              </div>
                              <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                                {tax.category || "Clinical Diagnostic Classification"}
                              </p>
                            </div>
                          </div>

                          <div className="flex items-center gap-1.5 shrink-0">
                            <button
                              type="button"
                              onClick={(e) => {
                                e.stopPropagation();
                                setQuery(tax.title);
                                setIsFocused(false);
                                handleSearch(tax.title);
                              }}
                              className="px-2.5 py-1 rounded-lg bg-white hover:bg-indigo-50 border border-slate-200 hover:border-indigo-200 text-slate-700 hover:text-indigo-700 text-[11px] font-semibold flex items-center gap-1 transition-colors shadow-2xs"
                            >
                              <Sparkles className="w-3 h-3 text-indigo-500" />
                              <span>Ask AI</span>
                            </button>
                            <ChevronRight className="w-4 h-4 text-slate-300 group-hover:text-indigo-500 transition-colors self-center" />
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Real-Time Query Validation & Medical Normalization */}
            <div className="mt-3 text-left">
              <QueryValidationComponent
                query={query}
                onApplyCorrection={(corrected) => {
                  setQuery(corrected);
                  handleSearch(corrected);
                }}
              />
            </div>
          </div>

          {/* Quick Explore Condition Pills */}
          <div className="flex flex-wrap items-center justify-center gap-2 max-w-4xl mx-auto">
            <span className="text-xs text-slate-500 font-semibold mr-1 flex items-center gap-1">
              <Flame className="w-3.5 h-3.5 text-amber-500" /> Quick Topics:
            </span>
            {popularPills.map((pill, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => {
                  setQuery(pill.query);
                  handleSearch(pill.query);
                }}
                className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-white hover:bg-indigo-50/60 border border-slate-200 hover:border-indigo-200 text-xs text-slate-700 hover:text-indigo-700 font-medium transition-all shadow-2xs"
              >
                <span>{pill.icon}</span>
                <span>{pill.label}</span>
                <span className="px-1.5 py-0.2 bg-slate-100 text-[10px] font-bold text-slate-600 rounded-md">
                  {pill.badge}
                </span>
              </button>
            ))}

            <button
              type="button"
              onClick={() => setPrimaryView("wiki")}
              className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-gradient-to-r from-indigo-50 to-purple-50 hover:from-indigo-100 hover:to-purple-100 border border-indigo-200 text-xs text-indigo-900 font-bold transition-all shadow-2xs"
            >
              <BookOpen className="w-3.5 h-3.5 text-indigo-600" />
              <span>Browse 600 Wiki Articles</span>
              <span className="px-1.5 py-0.2 bg-indigo-200/70 text-[10px] font-extrabold text-indigo-900 rounded-md">
                WikiMed
              </span>
            </button>
          </div>
        </section>
      ) : (
        /* ================= COMPACT SEARCH & ACTIVE TOPIC HEADING VIEW ================= */
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-2">
          {/* Compact Refinement Search Bar */}
          <div className="flex flex-col md:flex-row items-stretch md:items-center gap-3 mb-4">
            <div className="relative flex-1">
              {/* Compact Search Scope Selector */}
              <div className="flex items-center gap-1.5 mb-2">
                <button
                  type="button"
                  onClick={() => setSearchTarget("all")}
                  className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold transition-all ${
                    searchTarget === "all"
                      ? "bg-indigo-600 text-white shadow-2xs"
                      : "bg-white text-slate-600 hover:text-slate-900 border border-slate-200"
                  }`}
                >
                  ✨ Universal
                </button>
                <button
                  type="button"
                  onClick={() => setSearchTarget("wiki")}
                  className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold transition-all flex items-center gap-1 ${
                    searchTarget === "wiki"
                      ? "bg-indigo-600 text-white shadow-2xs"
                      : "bg-white text-slate-600 hover:text-slate-900 border border-slate-200"
                  }`}
                >
                  <BookOpen className="w-3 h-3" />
                  <span>Medical Wiki (600)</span>
                </button>
                <button
                  type="button"
                  onClick={() => setSearchTarget("assistant")}
                  className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold transition-all flex items-center gap-1 ${
                    searchTarget === "assistant"
                      ? "bg-indigo-600 text-white shadow-2xs"
                      : "bg-white text-slate-600 hover:text-slate-900 border border-slate-200"
                  }`}
                >
                  <Sparkles className="w-3 h-3" />
                  <span>AI Assistant</span>
                </button>
              </div>

              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  handleSearch();
                }}
                className="relative flex items-center w-full h-12 bg-white rounded-xl border border-slate-200 focus-within:border-indigo-600 focus-within:ring-3 focus-within:ring-indigo-100 shadow-xs transition-all"
              >
                <div className="absolute left-3.5 flex items-center pointer-events-none text-slate-400">
                  <Search className="w-4 h-4" />
                </div>

                <input
                  ref={inputRef}
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  onFocus={() => setIsFocused(true)}
                  onKeyDown={handleKeyDown}
                  placeholder={searchPlaceholder}
                  className="w-full h-full pl-10 pr-28 bg-transparent text-slate-900 placeholder:text-slate-400 text-sm outline-none font-normal"
                />

                <div className="absolute right-1.5 flex items-center gap-1">
                  {query && (
                    <button
                      type="button"
                      onClick={() => {
                        setQuery("");
                        inputRef.current?.focus();
                      }}
                      className="p-1.5 text-slate-400 hover:text-slate-600 hover:bg-slate-100 rounded-lg transition-colors"
                      title="Clear search input"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  )}

                  <button
                    type="submit"
                    disabled={loading || !query.trim()}
                    className="px-4 py-1.5 h-9 rounded-lg bg-indigo-600 hover:bg-indigo-700 active:scale-98 text-white font-semibold text-xs transition-all shadow-2xs disabled:opacity-50 flex items-center gap-1.5"
                  >
                    {loading ? (
                      <>
                        <RefreshCw className="w-3.5 h-3.5 animate-spin" />
                        <span>Searching</span>
                      </>
                    ) : (
                      <span>Search</span>
                    )}
                  </button>
                </div>
              </form>

              {/* Autocomplete Dropdown in Compact View with Instant Wiki Card & 133k+ Taxonomy */}
              {isFocused && (filteredSuggestions.length > 0 || taxonomyResults.length > 0) && (
                <div
                  ref={dropdownRef}
                  className="absolute left-0 right-0 top-full mt-2 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 text-left overflow-hidden animate-fade-in divide-y divide-slate-100"
                >
                  {filteredSuggestions.length > 0 && (
                    <>
                      {/* Instant Wiki Knowledge Card Preview */}
                      <div className="p-3 bg-gradient-to-r from-indigo-50/90 via-purple-50/70 to-blue-50/60 border-b border-indigo-100 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2.5">
                        <div className="flex items-start gap-2.5">
                          <div className="p-1.5 bg-white text-indigo-600 rounded-xl shadow-2xs border border-indigo-100 text-sm shrink-0">
                            {filteredSuggestions[0].icon || "📖"}
                          </div>
                          <div>
                            <div className="flex items-center gap-1.5 flex-wrap">
                              <span className="text-xs font-bold text-slate-900">
                                {filteredSuggestions[0].label}
                              </span>
                              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white text-indigo-700 font-bold border border-indigo-200">
                                WikiMed Topic
                              </span>
                            </div>
                            <p className="text-[11px] text-slate-600 line-clamp-1 mt-0.5 max-w-lg">
                              {filteredSuggestions[0].description}
                            </p>
                          </div>
                        </div>

                        <div className="flex items-center gap-1.5 self-end sm:self-center shrink-0">
                          <button
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              handleOpenWikiTopic(filteredSuggestions[0].id.replace("sug-", ""));
                            }}
                            className="px-2.5 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-[11px] font-bold flex items-center gap-1 shadow-2xs transition-all"
                          >
                            <BookOpen className="w-3 h-3" />
                            <span>Read Wiki</span>
                          </button>

                          <button
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              handleSelectSuggestion(filteredSuggestions[0]);
                            }}
                            className="px-2.5 py-1 rounded-lg bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 text-[11px] font-semibold flex items-center gap-1 shadow-2xs transition-all"
                          >
                            <Sparkles className="w-3 h-3 text-indigo-600" />
                            <span>Ask AI</span>
                          </button>
                        </div>
                      </div>

                      <div className="px-4 py-1.5 bg-slate-50/80 border-b border-slate-100 flex items-center justify-between text-[11px] text-slate-500 font-semibold">
                        <span className="flex items-center gap-1.5">
                          <Sparkles className="w-3 h-3 text-indigo-600" />
                          Suggested Medical Topics
                        </span>
                        <span className="text-[10px] text-slate-400">Click or press Enter</span>
                      </div>

                      <div className="max-h-56 overflow-y-auto divide-y divide-slate-100">
                        {filteredSuggestions.map((sug, idx) => {
                          const isSelected = selectedIndex === idx;
                          return (
                            <div
                              key={sug.id}
                              onClick={() => handleSelectSuggestion(sug)}
                              className={`p-2.5 sm:px-3 sm:py-2 cursor-pointer transition-colors flex items-center justify-between gap-3 ${
                                isSelected ? "bg-indigo-50/80" : "hover:bg-slate-50"
                              }`}
                            >
                              <div className="flex items-start gap-2.5 min-w-0">
                                <span className="text-base mt-0.5 shrink-0">{sug.icon || "🩺"}</span>
                                <div className="min-w-0">
                                  <div className="flex items-center gap-2 flex-wrap">
                                    <span className="text-xs font-bold text-slate-900 truncate">
                                      {sug.label}
                                    </span>
                                    <span className="px-1.5 py-0.5 rounded text-[9px] font-bold bg-indigo-50 text-indigo-700 border border-indigo-200">
                                      {sug.healthBody}
                                    </span>
                                  </div>
                                  <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                                    {sug.description}
                                  </p>
                                </div>
                              </div>

                              <div className="flex items-center gap-1 shrink-0">
                                <button
                                  type="button"
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    handleOpenWikiTopic(sug.id.replace("sug-", ""));
                                  }}
                                  className="px-2 py-0.5 rounded-md bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-[10px] font-bold flex items-center gap-1 transition-colors"
                                  title="Open 10-section Wiki article"
                                >
                                  <BookOpen className="w-3 h-3" />
                                  <span>Wiki</span>
                                </button>
                                <ChevronRight className="w-3.5 h-3.5 text-slate-400 self-center" />
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </>
                  )}

                  {/* Official CMS & WHO Master Taxonomy (133k+ DB) */}
                  {taxonomyResults.length > 0 && (
                    <div className="bg-slate-50/60">
                      <div className="px-4 py-1.5 bg-gradient-to-r from-slate-100 via-blue-50/60 to-slate-100 border-b border-slate-200/80 flex items-center justify-between text-[11px] text-slate-700 font-bold">
                        <span className="flex items-center gap-1.5">
                          <Globe2 className="w-3.5 h-3.5 text-blue-600" />
                          CMS ICD-10 & WHO ICD-11 Catalog ({taxonomyStats?.total_conditions ? `${taxonomyStats.total_conditions.toLocaleString()} conditions` : "133k+ conditions"})
                        </span>
                        <span className="text-[9px] text-slate-500 font-mono">FTS5 Search</span>
                      </div>

                      <div className="max-h-52 overflow-y-auto divide-y divide-slate-100">
                        {taxonomyResults.map((tax) => (
                          <div
                            key={`${tax.source}-${tax.id}`}
                            onClick={() => {
                              setQuery(tax.title);
                              setIsFocused(false);
                              handleSearch(tax.title);
                            }}
                            className="p-2 sm:px-3 sm:py-2 cursor-pointer hover:bg-white transition-colors flex items-center justify-between gap-3 group"
                          >
                            <div className="flex items-start gap-2 min-w-0">
                              <span className="text-sm mt-0.5 shrink-0">
                                {tax.source === "CMS_ICD10" ? "🏛️" : "🌐"}
                              </span>
                              <div className="min-w-0">
                                <div className="flex items-center gap-1.5 flex-wrap">
                                  <span className="font-mono text-[10px] font-bold px-1.5 py-0.2 rounded bg-slate-200 text-slate-800 border border-slate-300">
                                    {tax.code}
                                  </span>
                                  <span className="text-xs font-semibold text-slate-900 group-hover:text-indigo-600 transition-colors truncate">
                                    {tax.title}
                                  </span>
                                  <span
                                    className={`px-1.5 py-0.2 rounded text-[8px] font-bold ${
                                      tax.source === "CMS_ICD10"
                                        ? "bg-blue-50 text-blue-700 border border-blue-200"
                                        : "bg-emerald-50 text-emerald-700 border border-emerald-200"
                                    }`}
                                  >
                                    {tax.source === "CMS_ICD10" ? "CMS ICD-10" : "WHO ICD-11"}
                                  </span>
                                </div>
                                <p className="text-[10px] text-slate-500 line-clamp-1 mt-0.5">
                                  {tax.category || "Clinical Diagnostic Entity"}
                                </p>
                              </div>
                            </div>

                            <div className="flex items-center gap-1 shrink-0">
                              <button
                                type="button"
                                onClick={(e) => {
                                  e.stopPropagation();
                                  setQuery(tax.title);
                                  setIsFocused(false);
                                  handleSearch(tax.title);
                                }}
                                className="px-2 py-0.5 rounded-md bg-white hover:bg-indigo-50 border border-slate-200 hover:border-indigo-200 text-slate-700 hover:text-indigo-700 text-[10px] font-semibold flex items-center gap-1 transition-colors shadow-2xs"
                              >
                                <Sparkles className="w-3 h-3 text-indigo-500" />
                                <span>Ask AI</span>
                              </button>
                              <ChevronRight className="w-3.5 h-3.5 text-slate-300 group-hover:text-indigo-500 transition-colors self-center" />
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Compact Real-Time Query Validation */}
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

            {/* Reset / New Search Button (Only when active topic exists) */}
            {hasTopic && (
              <button
                type="button"
                onClick={handleClearTopic}
                className="flex items-center justify-center gap-1.5 px-3.5 h-12 rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-600 hover:text-slate-900 text-xs font-semibold transition-all shadow-2xs whitespace-nowrap"
                title="Clear topic and return to home"
              >
                <ArrowLeft className="w-4 h-4 text-slate-500" />
                <span>New Topic</span>
              </button>
            )}
          </div>

          {/* Dedicated Topic Heading Banner (Only in Assistant mode when active topic exists) */}
          {hasTopic && primaryView === "assistant" && (
            <div className="p-4 sm:p-5 bg-white border border-slate-200/90 rounded-2xl shadow-xs transition-all">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <div className="flex flex-wrap items-center gap-2 mb-1.5">
                    <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-50 text-indigo-700 border border-indigo-200">
                      <Sparkles className="w-3.5 h-3.5" />
                      Medical Topic Guide
                    </span>

                    {compareMode ? (
                      <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-purple-50 text-purple-700 border border-purple-200 flex items-center gap-1">
                        <Columns3 className="w-3 h-3" />
                        Dual Perspective Sync
                      </span>
                    ) : mode === "professional" ? (
                      <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-teal-50 text-teal-700 border border-teal-200 flex items-center gap-1">
                        <Stethoscope className="w-3 h-3" />
                        Clinician Mode
                      </span>
                    ) : (
                      <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-blue-50 text-blue-700 border border-blue-200 flex items-center gap-1">
                        <HeartHandshake className="w-3 h-3" />
                        Patient & Family Guide
                      </span>
                    )}

                    {result?.sources && result.sources.length > 0 && (
                      <span className="px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center gap-1">
                        <CheckCircle2 className="w-3 h-3 text-emerald-600" />
                        {result.sources.length} Verified Sources
                      </span>
                    )}
                  </div>

                  {/* Auto-Correction Notice */}
                  {(result?.validation?.corrections_made?.length || patientResult?.validation?.corrections_made?.length) ? (
                    <div className="mb-2 inline-flex items-center gap-1.5 px-3 py-1 rounded-xl bg-amber-50 border border-amber-200 text-xs text-amber-900 font-medium">
                      <Wand2 className="w-3.5 h-3.5 text-amber-600" />
                      <span>Showing results for:</span>
                      <span className="font-bold text-slate-900">
                        {(result?.validation?.corrections_made || patientResult?.validation?.corrections_made || []).join(", ")}
                      </span>
                    </div>
                  ) : null}

                  {/* Clear & Polished Topic Heading */}
                  <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight leading-snug">
                    {activeQueryText || "Medical Search Topic"}
                  </h2>
                </div>

                {/* Quick Health Standard Badges */}
                <div className="flex items-center gap-2 flex-shrink-0 self-start sm:self-center">
                  <div className="flex items-center gap-1 px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-lg text-[11px] font-medium text-slate-600">
                    <ShieldCheck className="w-3.5 h-3.5 text-indigo-600" />
                    <span>Verified Medical Guidelines</span>
                  </div>
                </div>
              </div>

              {/* Quick Switch Pills Bar */}
              <div className="mt-3.5 pt-3 border-t border-slate-100 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
                <span className="text-[11px] text-slate-400 font-semibold uppercase tracking-wider mr-1 whitespace-nowrap flex items-center gap-1">
                  <Flame className="w-3 h-3 text-amber-500" /> Switch Topic:
                </span>
                {popularPills.map((pill, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => {
                      setQuery(pill.query);
                      handleSearch(pill.query);
                    }}
                    className="flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-50 hover:bg-indigo-50 border border-slate-200 hover:border-indigo-200 text-xs text-slate-600 hover:text-indigo-700 font-medium whitespace-nowrap transition-all"
                  >
                    <span>{pill.icon}</span>
                    <span>{pill.label}</span>
                  </button>
                ))}
              </div>
            </div>
          )}
        </section>
      )}

      {/* Main Results & Workspace Layout */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
        {primaryView === "wiki" ? (
          /* ================= PRIMARY MEDICAL WIKI COMPENDIUM VIEW ================= */
          <div className="space-y-6 animate-fade-in">
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
              onAskCopilot={(q) => {
                setQuery(q);
                setPrimaryView("split");
                handleSearch(q);
              }}
            />
          </div>
        ) : primaryView === "split" ? (
          /* ================= SPLIT VIEW: WIKI DOSSIER + AI CO-PILOT ================= */
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start animate-fade-in">
            {/* Left Column: Medical Wiki Viewer (7 cols) */}
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

            {/* Right Column: AI Co-Pilot Assistant Thread (5 cols) */}
            <div className="lg:col-span-5 h-[85vh] bg-white border border-slate-200 rounded-2xl shadow-xs p-4 flex flex-col overflow-hidden">
              <div className="flex items-center justify-between pb-3 mb-2 border-b border-slate-100 shrink-0">
                <div className="flex items-center gap-2">
                  <div className="p-1.5 bg-gradient-to-tr from-indigo-600 to-purple-600 text-white rounded-xl shadow-2xs">
                    <Sparkles className="w-4 h-4" />
                  </div>
                  <div>
                    <h3 className="text-xs font-bold text-slate-900">AI Clinical Co-Pilot</h3>
                    <p className="text-[10px] text-slate-500">Ask interactive reasoning questions about this condition</p>
                  </div>
                </div>
                <button
                  type="button"
                  onClick={() => setPrimaryView("wiki")}
                  className="text-xs text-indigo-600 hover:text-indigo-800 font-semibold"
                >
                  Full Wiki
                </button>
              </div>
              <div className="flex-1 overflow-y-auto">
                <IntegratedChatThread
                  initialTopic={query || selectedWikiTopicId}
                  mode={mode}
                  response={result}
                  activeCitation={activeCitation}
                  onSelectCitation={handleSelectCitation}
                />
              </div>
            </div>
          </div>
        ) : loading ? (
          /* Sleek Loading State */
          <div className="p-8 sm:p-12 bg-white border border-slate-200 rounded-2xl text-center shadow-xs animate-fade-in space-y-4 max-w-4xl mx-auto">
            <div className="w-12 h-12 rounded-2xl bg-indigo-50 border border-indigo-100 flex items-center justify-center mx-auto text-indigo-600 shadow-xs">
              <RefreshCw className="w-6 h-6 animate-spin text-indigo-600" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-slate-900">
                Grounding Evidence & Synthesizing Clinical Truth...
              </h3>
              <p className="text-xs text-slate-500 mt-1 max-w-md mx-auto">
                Retrieving WHO Guidelines, Oxford CEBM clinical studies, and generating dual-perspective medical summaries.
              </p>
            </div>
            <div className="flex justify-center gap-1.5 pt-2">
              <span className="w-2 h-2 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: "0ms" }} />
              <span className="w-2 h-2 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: "150ms" }} />
              <span className="w-2 h-2 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: "300ms" }} />
            </div>
          </div>
        ) : compareMode && result && patientResult ? (
          /* Side-by-Side Dual-Perspective Synchronizer */
          <div className="space-y-6">
            {result?.triage_alert && (
              <div className="max-w-4xl mx-auto my-3">
                <TriageBanner alert={result.triage_alert} />
              </div>
            )}
            <div className="p-4 bg-gradient-to-r from-indigo-50 via-white to-teal-50 border border-slate-200 rounded-2xl text-center text-xs sm:text-sm text-slate-700 shadow-2xs">
              <span className="font-bold text-indigo-900">Side-by-Side Dual Perspective:</span> Grounded in the identical peer-reviewed evidence set across plain English (patient) and clinical register (physician).
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="space-y-4">
                <PatientView
                  response={patientResult}
                  activeCitation={activeCitation}
                  onSelectCitation={handleSelectCitation}
                  onSelectElaboration={(q) => {
                    setQuery(q);
                    handleSearch(q);
                  }}
                />
              </div>
              <div className="space-y-4">
                <ClinicianView
                  response={result}
                  activeCitation={activeCitation}
                  onSelectCitation={handleSelectCitation}
                  onSelectElaboration={(q) => {
                    setQuery(q);
                    handleSearch(q);
                  }}
                />
              </div>
            </div>

            {/* Inline Integrated Conversational Chatbot & Follow-ups in Compare Mode */}
            <IntegratedChatThread
              initialTopic={activeQueryText}
              mode={mode}
              response={result}
              activeCitation={activeCitation}
              onSelectCitation={handleSelectCitation}
            />

            {/* Shared Evidence Repository */}
            <div className="mt-8">
              <CitationDrawer
                sources={result.sources}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>
          </div>
        ) : result ? (
          /* Standard Single-Perspective + Evidence Drawer Layout */
          <div className="space-y-6">
            {result?.triage_alert && (
              <div className="max-w-4xl mx-auto my-3">
                <TriageBanner alert={result.triage_alert} />
              </div>
            )}

            {/* Verified WikiMed Grounded Dossier Callout Card */}
            {matchedWikiTopic && (
              <div className="p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-indigo-50/90 via-purple-50/70 to-blue-50/80 border border-indigo-200/90 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-2xs animate-fade-in">
                <div className="flex items-start gap-3.5">
                  <div className="p-2.5 bg-gradient-to-tr from-indigo-600 to-purple-600 text-white rounded-xl shadow-xs text-base shrink-0">
                    <BookOpen className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="text-xs font-mono font-bold px-2 py-0.5 rounded-md bg-white text-indigo-700 border border-indigo-200">
                        WikiMed Grounded Dossier
                      </span>
                      <span className="text-sm font-extrabold text-slate-900">
                        {matchedWikiTopic.label}
                      </span>
                      <span className="text-xs px-2 py-0.5 rounded-md bg-emerald-100/70 text-emerald-800 font-semibold border border-emerald-200">
                        {matchedWikiTopic.category}
                      </span>
                    </div>
                    <p className="text-xs text-slate-600 mt-1 max-w-2xl leading-relaxed">
                      Full 10-section encyclopedic breakdown available: physical analogies, ICD-10 criteria, GDMT titrations, and landmark trial DOIs.
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-2 self-end sm:self-center shrink-0">
                  <button
                    type="button"
                    onClick={() => handleOpenWikiTopic(matchedWikiTopic.id.replace("sug-", ""))}
                    className="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold transition-all shadow-xs flex items-center gap-1.5"
                  >
                    <BookOpen className="w-3.5 h-3.5" />
                    <span>Read 10-Section Wiki</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleOpenWikiSplit(matchedWikiTopic.id.replace("sug-", ""), activeQueryText)}
                    className="px-3 py-2 rounded-xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200 text-xs font-semibold transition-all shadow-2xs flex items-center gap-1.5"
                    title="Open Co-Pilot Split View"
                  >
                    <Columns3 className="w-3.5 h-3.5 text-indigo-600" />
                    <span>Co-Pilot Split</span>
                  </button>
                </div>
              </div>
            )}

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              {/* Main AI Response Pane */}
              <div className="lg:col-span-8 space-y-6">
                {mode === "professional" ? (
                  <ClinicianView
                    response={result}
                    activeCitation={activeCitation}
                    onSelectCitation={handleSelectCitation}
                    onSelectElaboration={(q) => {
                      setQuery(q);
                      handleSearch(q);
                    }}
                  />
              ) : (
                <PatientView
                  response={result}
                  activeCitation={activeCitation}
                  onSelectCitation={handleSelectCitation}
                  onSelectElaboration={(q) => {
                    setQuery(q);
                    handleSearch(q);
                  }}
                />
              )}

              {/* Inline Integrated Conversational Chatbot & Follow-ups */}
              <IntegratedChatThread
                initialTopic={activeQueryText}
                mode={mode}
                response={result}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>

            {/* Evidence & Citations Sidebar */}
            <div className="lg:col-span-4 sticky top-24">
              <CitationDrawer
                sources={result.sources}
                activeCitation={activeCitation}
                onSelectCitation={handleSelectCitation}
              />
            </div>
          </div>
        </div>
      ) : null}
    </section>

      {/* Footer with International Health Bodies & Oxford CEBM Standards */}
      <footer className="max-w-7xl mx-auto px-4 mt-20 pt-8 border-t border-slate-200 text-center text-xs text-slate-500 space-y-3">
        <div className="flex flex-wrap items-center justify-center gap-3 text-slate-600 font-semibold">
          <span>WHO World Health Organization</span>
          <span>•</span>
          <span>Peer-Reviewed Clinical Evidence</span>
          <span>•</span>
          <span>ADA / AHA / NICE / ESC Guidelines</span>
          <span>•</span>
          <span>Emergency Triage Safety</span>
        </div>
        <p className="text-slate-400 max-w-2xl mx-auto leading-relaxed">
          AegisMed is an evidence-based clinical and patient decision-support tool. All summaries are grounded in peer-reviewed clinical literature. Not a substitute for professional in-person medical diagnosis.
        </p>
      </footer>
    </main>
  );
}
