"use client";

import React, { useState, useEffect, useRef } from "react";
import { UserMode, SearchResponse } from "@/lib/types";
import { searchClinicalRAG } from "@/lib/api";
import { ClinicianView } from "@/components/clinician-view";
import { PatientView } from "@/components/patient-view";
import { CitationDrawer } from "@/components/citation-drawer";
import { TriageBanner } from "@/components/triage-banner";
import { getMatchingSuggestions, SearchSuggestion } from "@/lib/suggestions";
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
  Layers
} from "lucide-react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [mode, setMode] = useState<UserMode>("patient");
  const [compareMode, setCompareMode] = useState(false);
  const [loading, setLoading] = useState(false);
  const [activeCitation, setActiveCitation] = useState<number | null>(null);

  const [result, setResult] = useState<SearchResponse | null>(null);
  const [patientResult, setPatientResult] = useState<SearchResponse | null>(null);


  // Autocomplete state
  const [isFocused, setIsFocused] = useState(false);
  const [filteredSuggestions, setFilteredSuggestions] = useState<SearchSuggestion[]>([]);
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const hasTopic = Boolean(result || patientResult || loading);

  const searchPlaceholder =
    mode === "patient"
      ? "Describe your symptoms or ask a health question..."
      : "Search clinical guidelines, trials, or treatment protocols...";

  // Update suggestions when query changes
  useEffect(() => {
    const list = getMatchingSuggestions(query, 8);
    setFilteredSuggestions(list);
    setSelectedIndex(-1);
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

  const handleSearch = async (overrideQuery?: string, targetMode?: UserMode) => {
    const q = overrideQuery || query;
    if (!q.trim()) return;

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
                  Clinical Truth Engine
                </span>
              </div>
              <p className="text-xs text-slate-500 hidden sm:block">
                WHO-Aligned Guidelines • Oxford CEBM Evidence Grounding
              </p>
            </div>
          </div>

          {/* Perspective Selector Controls — Patient first */}
          <div className="flex items-center gap-1.5 bg-slate-100/90 p-1.5 rounded-2xl border border-slate-200">
            <button
              type="button"
              onClick={() => {
                setCompareMode(false);
                setMode("patient");
                if (result) handleSearch(query, "patient");
              }}
              className={`flex items-center gap-1.5 px-3 sm:px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                !compareMode && mode === "patient"
                  ? "bg-white text-indigo-700 shadow-sm border border-slate-200/80"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <HeartHandshake className="w-4 h-4 text-indigo-600" />
              <span className="hidden xs:inline">Patient & Family</span>
              <span className="xs:hidden">Patient</span>
            </button>

            <button
              type="button"
              onClick={() => {
                setCompareMode(false);
                setMode("professional");
                if (result) handleSearch(query, "professional");
              }}
              className={`flex items-center gap-1.5 px-3 sm:px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                !compareMode && mode === "professional"
                  ? "bg-white text-teal-700 shadow-sm border border-slate-200/80"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <Stethoscope className="w-4 h-4 text-teal-600" />
              <span className="hidden xs:inline">Clinician / Doctor</span>
              <span className="xs:hidden">Doctor</span>
            </button>

            <div className="w-[1px] h-4 bg-slate-300 mx-1 hidden sm:block" />

            <button
              type="button"
              onClick={() => {
                setCompareMode(true);
                handleSearch(query);
              }}
              className={`hidden sm:flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                compareMode
                  ? "bg-gradient-to-r from-indigo-600 to-teal-600 text-white shadow-sm"
                  : "text-slate-600 hover:text-slate-900"
              }`}
              title="Compare Patient & Clinician translations side-by-side"
            >
              <Columns3 className="w-4 h-4" />
              <span>Compare Both</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Search & Hero Section (Responsive & Dynamic when topic is active) */}
      {!hasTopic ? (
        /* ================= LANDING HERO VIEW ================= */
        <section className="max-w-4xl mx-auto px-4 sm:px-6 pt-10 pb-6 text-center animate-fade-in">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-indigo-100 text-indigo-700 text-xs font-semibold shadow-xs mb-4">
            <Globe2 className="w-3.5 h-3.5 text-indigo-600" />
            <span>Accurate Medical Knowledge Grounded in WHO & Peer-Reviewed Trials</span>
          </div>

          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-slate-900 tracking-tight mb-3">
            Understand Your Health With Confidence.
          </h2>
          <p className="text-slate-600 text-sm sm:text-base max-w-2xl mx-auto mb-8 leading-relaxed">
            Search any disease, symptom, or treatment. Get clear, friendly explanations for patients and families, or rigorous clinical summaries for healthcare professionals.
          </p>

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

            {/* Autocomplete Dropdown */}
            {isFocused && filteredSuggestions.length > 0 && (
              <div
                ref={dropdownRef}
                className="absolute left-0 right-0 top-full mt-2 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 text-left overflow-hidden animate-fade-in"
              >
                <div className="px-4 py-2.5 bg-slate-50 border-b border-slate-100 flex items-center justify-between text-xs text-slate-500 font-semibold">
                  <span className="flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                    Suggested Medical Topics & Guidelines
                  </span>
                  <span className="text-[11px] text-slate-400">Use ↑↓ keys or click</span>
                </div>

                <div className="max-h-80 overflow-y-auto divide-y divide-slate-100">
                  {filteredSuggestions.map((sug, idx) => {
                    const isSelected = selectedIndex === idx;
                    return (
                      <div
                        key={sug.id}
                        onClick={() => handleSelectSuggestion(sug)}
                        className={`p-3.5 sm:px-4 sm:py-3 cursor-pointer transition-colors flex items-start justify-between gap-3 ${
                          isSelected ? "bg-indigo-50/80" : "hover:bg-slate-50"
                        }`}
                      >
                        <div className="flex items-start gap-3">
                          <span className="text-xl mt-0.5">{sug.icon || "🩺"}</span>
                          <div>
                            <div className="flex items-center gap-2">
                              <span className="text-sm font-bold text-slate-900">
                                {sug.label}
                              </span>
                              <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-indigo-50 text-indigo-700 border border-indigo-200">
                                {sug.healthBody}
                              </span>
                            </div>
                            <p className="text-xs text-slate-500 line-clamp-1 mt-0.5">
                              {sug.description}
                            </p>
                          </div>
                        </div>

                        <ChevronRight className="w-4 h-4 text-slate-400 self-center flex-shrink-0" />
                      </div>
                    );
                  })}
                </div>
              </div>
            )}
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
          </div>
        </section>
      ) : (
        /* ================= COMPACT SEARCH & ACTIVE TOPIC HEADING VIEW ================= */
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-5 pb-3">
          {/* Compact Refinement Search Bar */}
          <div className="flex flex-col md:flex-row items-stretch md:items-center gap-3 mb-5">
            <div className="relative flex-1">
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

              {/* Autocomplete Dropdown in Compact View */}
              {isFocused && filteredSuggestions.length > 0 && (
                <div
                  ref={dropdownRef}
                  className="absolute left-0 right-0 top-full mt-2 bg-white border border-slate-200 rounded-2xl shadow-xl z-50 text-left overflow-hidden animate-fade-in"
                >
                  <div className="px-4 py-2 bg-slate-50 border-b border-slate-100 flex items-center justify-between text-xs text-slate-500 font-semibold">
                    <span className="flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                      Suggested Medical Topics
                    </span>
                    <span className="text-[11px] text-slate-400">Click or press Enter</span>
                  </div>

                  <div className="max-h-72 overflow-y-auto divide-y divide-slate-100">
                    {filteredSuggestions.map((sug, idx) => {
                      const isSelected = selectedIndex === idx;
                      return (
                        <div
                          key={sug.id}
                          onClick={() => handleSelectSuggestion(sug)}
                          className={`p-3 cursor-pointer transition-colors flex items-start justify-between gap-3 ${
                            isSelected ? "bg-indigo-50/80" : "hover:bg-slate-50"
                          }`}
                        >
                          <div className="flex items-start gap-2.5">
                            <span className="text-lg mt-0.5">{sug.icon || "🩺"}</span>
                            <div>
                              <div className="flex items-center gap-2">
                                <span className="text-xs font-bold text-slate-900">
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

                          <ChevronRight className="w-3.5 h-3.5 text-slate-400 self-center flex-shrink-0" />
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>

            {/* Reset / New Search Button */}
            <button
              type="button"
              onClick={handleClearTopic}
              className="flex items-center justify-center gap-1.5 px-3.5 h-12 rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-600 hover:text-slate-900 text-xs font-semibold transition-all shadow-2xs whitespace-nowrap"
              title="Clear topic and return to home"
            >
              <ArrowLeft className="w-4 h-4 text-slate-500" />
              <span>New Topic</span>
            </button>
          </div>

          {/* Dedicated Topic Heading Banner */}
          <div className="p-4 sm:p-5 bg-white border border-slate-200/90 rounded-2xl shadow-xs transition-all">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <div className="flex flex-wrap items-center gap-2 mb-1.5">
                  <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-50 text-indigo-700 border border-indigo-200">
                    <Sparkles className="w-3.5 h-3.5" />
                    Synthesized Clinical Topic
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
                      {result.sources.length} Peer-Reviewed Citations
                    </span>
                  )}
                </div>

                {/* Clear & Polished Topic Heading */}
                <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight leading-snug">
                  {activeQueryText || "Clinical Search Topic"}
                </h2>
              </div>

              {/* Quick Health Standard Badges */}
              <div className="flex items-center gap-2 flex-shrink-0 self-start sm:self-center">
                <div className="flex items-center gap-1 px-2.5 py-1 bg-slate-50 border border-slate-200 rounded-lg text-[11px] font-medium text-slate-600">
                  <ShieldCheck className="w-3.5 h-3.5 text-indigo-600" />
                  <span>WHO & Oxford CEBM</span>
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
        </section>
      )}

      {/* Main Results Layout */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
        {loading ? (
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
        ) : result?.is_emergency && result.triage_alert ? (
          /* Emergency Intercept Banner */
          <div className="max-w-4xl mx-auto my-4">
            <TriageBanner alert={result.triage_alert} />
          </div>
        ) : compareMode && result && patientResult ? (
          /* Side-by-Side Dual-Perspective Synchronizer */
          <div className="space-y-6">
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
        ) : null}
      </section>

      {/* Footer with International Health Bodies & Oxford CEBM Standards */}
      <footer className="max-w-7xl mx-auto px-4 mt-20 pt-8 border-t border-slate-200 text-center text-xs text-slate-500 space-y-3">
        <div className="flex flex-wrap items-center justify-center gap-3 text-slate-600 font-semibold">
          <span>WHO World Health Organization</span>
          <span>•</span>
          <span>Oxford CEBM Level 1</span>
          <span>•</span>
          <span>ADA / AHA / NICE / ESC Guidelines</span>
          <span>•</span>
          <span>Tier-1 Emergency Intercept</span>
        </div>
        <p className="text-slate-400 max-w-2xl mx-auto leading-relaxed">
          AegisMed is an evidence-based clinical and patient decision-support tool. All summaries are grounded in peer-reviewed clinical literature. Not a substitute for professional in-person medical diagnosis.
        </p>
      </footer>
    </main>
  );
}
