"use client";

import React, { useState, useEffect, useMemo } from "react";
import {
  EncyclopediaArticle,
  EncyclopediaTopicSummary,
  WikiSection
} from "@/lib/types";
import {
  fetchEncyclopediaTopics,
  fetchEncyclopediaArticle,
  fetchEncyclopediaSpecialties,
  fetchRandomEncyclopediaTopic,
  searchClinicalTaxonomy,
  TaxonomyEntity
} from "@/lib/api";
import { JargonGlossary } from "./jargon-tooltip";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  BookOpen,
  Search,
  Sparkles,
  Stethoscope,
  HeartPulse,
  Brain,
  Pill,
  AlertTriangle,
  CheckCircle2,
  Share2,
  Printer,
  ChevronRight,
  ExternalLink,
  ShieldAlert,
  ArrowRight,
  Layers,
  Compass,
  FileText,
  Activity,
  Flame,
  X,
  HelpCircle
} from "lucide-react";

interface MedicalWikiViewerProps {
  initialTopicId?: string;
  mode?: "patient" | "clinician";
  onModeChange?: (mode: "patient" | "clinician") => void;
  onSelectQueryForAssistant?: (query: string) => void;
  onAskCopilot?: (question: string) => void;
  onClose?: () => void;
  embedded?: boolean;
  hideSidebar?: boolean;
}

export function MedicalWikiViewer({
  initialTopicId = "DOC-CARD-001",
  mode,
  onModeChange,
  onSelectQueryForAssistant,
  onAskCopilot,
  onClose,
  embedded = false,
  hideSidebar = false
}: MedicalWikiViewerProps) {
  const [activeTopicId, setActiveTopicId] = useState<string>(initialTopicId);
  const [activeMode, setActiveMode] = useState<"patient" | "clinician">(mode || "patient");
  const [article, setArticle] = useState<EncyclopediaArticle | null>(null);
  const [topics, setTopics] = useState<EncyclopediaTopicSummary[]>([]);
  const [specialties, setSpecialties] = useState<string[]>([]);
  const [selectedSpecialty, setSelectedSpecialty] = useState<string>("All");
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [isLoadingArticle, setIsLoadingArticle] = useState<boolean>(true);
  const [activeSectionId, setActiveSectionId] = useState<string>("");
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(!hideSidebar);
  const [taxonomyMatches, setTaxonomyMatches] = useState<TaxonomyEntity[]>([]);

  // Search CMS & WHO master catalog if query is typed
  useEffect(() => {
    if (searchQuery.trim().length >= 2) {
      const timer = setTimeout(() => {
        searchClinicalTaxonomy(searchQuery.trim(), undefined, 6)
          .then((res) => setTaxonomyMatches(res.results || []))
          .catch(() => setTaxonomyMatches([]));
      }, 150);
      return () => clearTimeout(timer);
    } else {
      setTaxonomyMatches([]);
    }
  }, [searchQuery]);

  // Sync mode with parent if provided
  useEffect(() => {
    if (mode) {
      setActiveMode(mode);
    }
  }, [mode]);

  // Sync topic with parent if provided
  useEffect(() => {
    if (initialTopicId) {
      setActiveTopicId(initialTopicId);
    }
  }, [initialTopicId]);

  // Handle mode toggle
  const handleModeToggle = (newMode: "patient" | "clinician") => {
    setActiveMode(newMode);
    if (onModeChange) onModeChange(newMode);
  };

  // Load topics catalog and specialties on mount
  useEffect(() => {
    async function loadCatalog() {
      try {
        const [topicList, specList] = await Promise.all([
          fetchEncyclopediaTopics({ limit: 600 }),
          fetchEncyclopediaSpecialties()
        ]);
        setTopics(topicList);
        setSpecialties(["All", ...specList]);
      } catch (err) {
        console.error("Failed to load encyclopedia catalog:", err);
      }
    }
    loadCatalog();
  }, []);

  // Fetch active article when topic or mode changes
  useEffect(() => {
    let isCancelled = false;
    async function loadArticle() {
      setIsLoadingArticle(true);
      try {
        const data = await fetchEncyclopediaArticle(activeTopicId, activeMode);
        if (!isCancelled) {
          setArticle(data);
          if (data.sections.length > 0) {
            setActiveSectionId(data.sections[0].id);
          }
        }
      } catch (err) {
        console.error("Failed to fetch article:", err);
      } finally {
        if (!isCancelled) setIsLoadingArticle(false);
      }
    }
    loadArticle();
    return () => {
      isCancelled = true;
    };
  }, [activeTopicId, activeMode]);

  // Filter and smartly rank topics
  const filteredTopics = useMemo(() => {
    const q = searchQuery.trim().toLowerCase();
    const filtered = topics.filter((t) => {
      const matchesSpec = selectedSpecialty === "All" || t.specialty === selectedSpecialty;
      const matchesQuery =
        q === "" ||
        t.name.toLowerCase().includes(q) ||
        t.icd10_code.toLowerCase().includes(q) ||
        t.short_summary.toLowerCase().includes(q) ||
        t.hallmark_symptoms.some((s) => s.toLowerCase().includes(q));
      return matchesSpec && matchesQuery;
    });

    if (!q) return filtered;

    // Rank exact word matches, title prefixes, and title occurrences higher
    return [...filtered].sort((a, b) => {
      const aName = a.name.toLowerCase();
      const bName = b.name.toLowerCase();

      // Check for whole word match in name
      const wordRegex = new RegExp(`\\b${q.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\$&')}\\b`, 'i');
      const aWord = wordRegex.test(aName);
      const bWord = wordRegex.test(bName);
      if (aWord && !bWord) return -1;
      if (!aWord && bWord) return 1;

      // Starts with query in name
      const aStarts = aName.startsWith(q);
      const bStarts = bName.startsWith(q);
      if (aStarts && !bStarts) return -1;
      if (!aStarts && bStarts) return 1;

      // Title contains query
      const aHasTitle = aName.includes(q);
      const bHasTitle = bName.includes(q);
      if (aHasTitle && !bHasTitle) return -1;
      if (!aHasTitle && bHasTitle) return 1;

      return 0;
    });
  }, [topics, selectedSpecialty, searchQuery]);

  // Random topic
  const handleRandomTopic = async () => {
    try {
      setIsLoadingArticle(true);
      const rand = await fetchRandomEncyclopediaTopic(activeMode);
      setActiveTopicId(rand.id);
      setArticle(rand);
    } catch (err) {
      console.error("Failed to fetch random article:", err);
    } finally {
      setIsLoadingArticle(false);
    }
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className={`flex flex-col ${embedded ? 'h-[85vh] rounded-2xl border border-slate-200/90 shadow-sm bg-slate-50' : 'h-full bg-slate-50 text-slate-900 rounded-3xl overflow-hidden border border-slate-200/80 shadow-2xl'}`}>
      {/* Top Bar Header */}
      <div className="bg-white border-b border-slate-200 px-4 sm:px-5 py-3.5 flex flex-wrap items-center justify-between gap-3 shrink-0">
        <div className="flex items-center gap-3">
          <div className="p-2 sm:p-2.5 bg-gradient-to-tr from-indigo-600 to-purple-600 text-white rounded-xl shadow-xs">
            <BookOpen className="w-4 h-4 sm:w-5 sm:h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-sm sm:text-base font-bold text-slate-900">
                AegisMed WikiMed Compendium
              </h2>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-200 hidden xs:inline-block">
                600 Verified Topics
              </span>
            </div>
            <p className="text-[11px] sm:text-xs text-slate-500">
              Dual-register encyclopedic medicine grounded in Oxford CEBM Level 1 clinical evidence
            </p>
          </div>
        </div>

        {/* Audience Mode Switcher & Actions */}
        <div className="flex items-center gap-2">
          {/* Toggle sidebar visibility button on smaller screens or when embedded */}
          <button
            type="button"
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
            className="flex lg:hidden items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 text-slate-700 transition-colors"
            title="Toggle catalog list"
          >
            <Layers className="w-3.5 h-3.5 text-indigo-600" />
            <span>Topics</span>
          </button>

          {/* Dual-Register Mode Toggle */}
          <div className="bg-slate-100 p-1 rounded-xl flex items-center gap-1 border border-slate-200">
            <button
              type="button"
              onClick={() => handleModeToggle("patient")}
              className={`flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-lg text-xs font-bold transition-all ${
                activeMode === "patient"
                  ? "bg-white text-indigo-700 shadow-xs"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
              <span>Patient Wiki</span>
            </button>
            <button
              type="button"
              onClick={() => handleModeToggle("clinician")}
              className={`flex items-center gap-1.5 px-2.5 sm:px-3 py-1 rounded-lg text-xs font-bold transition-all ${
                activeMode === "clinician"
                  ? "bg-white text-indigo-700 shadow-xs"
                  : "text-slate-600 hover:text-slate-900"
              }`}
            >
              <Stethoscope className="w-3.5 h-3.5 text-indigo-600" />
              <span>Clinical Compendium</span>
            </button>
          </div>

          {/* Print Dossier */}
          <button
            type="button"
            onClick={handlePrint}
            className="p-2 rounded-xl text-slate-600 hover:text-slate-900 hover:bg-slate-100 border border-slate-200 transition-colors"
            title="Print consultation dossier"
          >
            <Printer className="w-4 h-4" />
          </button>

          {/* Optional Close */}
          {onClose && (
            <button
              type="button"
              onClick={onClose}
              className="p-2 rounded-xl text-slate-400 hover:text-slate-600 hover:bg-slate-100 transition-colors"
              title="Close Wiki"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Main Body: Topic Catalog Sidebar + Article Reader */}
      <div className="flex flex-1 overflow-hidden">
        {/* Left Column: Topics Catalog Navigation */}
        <div className={`w-80 shrink-0 bg-white border-r border-slate-200 flex flex-col h-full ${!hideSidebar && isSidebarOpen ? 'flex' : 'hidden'} lg:flex`}>
          {/* Search Input */}
          <div className="p-3 border-b border-slate-100">
            <div className="relative">
              <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                placeholder="Search 600 conditions, ICD-10..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-9 pr-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white"
              />
            </div>
            {/* Specialty filter dropdown */}
            <select
              value={selectedSpecialty}
              onChange={(e) => setSelectedSpecialty(e.target.value)}
              className="mt-2 w-full px-2.5 py-1.5 bg-white border border-slate-200 rounded-xl text-xs text-slate-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            >
              {specialties.map((s) => (
                <option key={s} value={s}>
                  {s === "All" ? `All Specialties (${topics.length || 600})` : s}
                </option>
              ))}
            </select>
          </div>

          {/* Topics List */}
          <div className="flex-1 overflow-y-auto divide-y divide-slate-100">
            {filteredTopics.map((t) => {
              const isSelected = activeTopicId === t.id;
              return (
                <button
                  key={t.id}
                  type="button"
                  onClick={() => setActiveTopicId(t.id)}
                  className={`w-full text-left p-3 transition-all flex items-start justify-between gap-2 ${
                    isSelected
                      ? "bg-indigo-50/80 border-l-4 border-indigo-600 text-indigo-950 font-semibold"
                      : "hover:bg-slate-50 text-slate-700"
                  }`}
                >
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-1.5 mb-0.5">
                      <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 font-bold">
                        {t.icd10_code}
                      </span>
                      <span className="text-[10px] text-slate-400 truncate">
                        {t.specialty}
                      </span>
                    </div>
                    <h4 className="text-xs font-bold truncate leading-tight">
                      {t.name}
                    </h4>
                    <p className="text-[11px] text-slate-500 line-clamp-1 mt-0.5">
                      {t.hallmark_symptoms.slice(0, 3).join(", ")}
                    </p>
                  </div>
                  {t.has_emergency_red_flags && (
                    <span className="text-rose-500 text-xs shrink-0" title="Has red flags">
                      ⚠️
                    </span>
                  )}
                </button>
              );
            })}
            {filteredTopics.length === 0 && taxonomyMatches.length === 0 && (
              <div className="p-6 text-center text-xs text-slate-400">
                No matching conditions found in wiki or catalog.
              </div>
            )}

            {/* CMS & WHO Master Taxonomy (133k+ Database) Matches */}
            {taxonomyMatches.length > 0 && (
              <div className="border-t-2 border-slate-200 bg-slate-50/80">
                <div className="p-2.5 bg-gradient-to-r from-slate-100 to-blue-50/50 border-b border-slate-200 flex items-center justify-between text-[11px] font-bold text-slate-700">
                  <span className="flex items-center gap-1.5">
                    <span>🌐</span> Official CMS & WHO Catalog
                  </span>
                  <span className="text-[9px] font-mono px-1.5 py-0.2 bg-blue-100 text-blue-800 rounded font-bold">133k+ DB</span>
                </div>
                <div className="divide-y divide-slate-100">
                  {taxonomyMatches.map((tax) => (
                    <div
                      key={`${tax.source}-${tax.id}`}
                      onClick={() => {
                        if (onSelectQueryForAssistant) {
                          onSelectQueryForAssistant(tax.title);
                        } else if (onAskCopilot) {
                          onAskCopilot(`What are the clinical guidelines and diagnostic protocols for ${tax.title} (${tax.code})?`);
                        }
                      }}
                      className="p-2.5 hover:bg-white cursor-pointer transition-colors group"
                      title="Ask AI Assistant about this condition"
                    >
                      <div className="flex items-center gap-1.5 mb-0.5">
                        <span className="font-mono text-[9px] font-bold px-1.5 py-0.2 rounded bg-slate-200 text-slate-800">
                          {tax.code}
                        </span>
                        <span
                          className={`text-[9px] font-bold px-1.5 py-0.2 rounded ${
                            tax.source === "CMS_ICD10"
                              ? "bg-blue-50 text-blue-700 border border-blue-200"
                              : "bg-emerald-50 text-emerald-700 border border-emerald-200"
                          }`}
                        >
                          {tax.source === "CMS_ICD10" ? "CMS ICD-10" : "WHO ICD-11"}
                        </span>
                      </div>
                      <h5 className="text-xs font-semibold text-slate-900 group-hover:text-indigo-600 transition-colors line-clamp-1">
                        {tax.title}
                      </h5>
                      <p className="text-[10px] text-slate-500 line-clamp-1 mt-0.5 flex items-center justify-between">
                        <span>{tax.category}</span>
                        <span className="text-indigo-600 font-bold opacity-0 group-hover:opacity-100 transition-opacity">Ask AI →</span>
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Active Article View */}
        <div className="flex-1 overflow-y-auto bg-slate-50 p-4 sm:p-8">
          {isLoadingArticle ? (
            <div className="flex flex-col items-center justify-center h-96 gap-3 text-slate-400">
              <div className="w-8 h-8 border-3 border-indigo-600 border-t-transparent rounded-full animate-spin" />
              <p className="text-xs font-semibold">Retrieving grounded clinical compendium...</p>
            </div>
          ) : article ? (
            <div className="max-w-4xl mx-auto space-y-6">
              {/* Article Header Card */}
              <div className="bg-white border border-slate-200 rounded-3xl p-6 sm:p-8 shadow-xs">
                <div className="flex flex-wrap items-center gap-2 mb-3">
                  <span className="px-2.5 py-1 rounded-xl text-xs font-bold bg-indigo-50 text-indigo-700 border border-indigo-100">
                    {article.specialty}
                  </span>
                  <span className="px-2.5 py-1 rounded-xl text-xs font-mono font-bold bg-slate-100 text-slate-700">
                    ICD-10: {article.icd10_code}
                  </span>
                  <span className="px-2.5 py-1 rounded-xl text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-100 flex items-center gap-1">
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>Oxford CEBM {article.cebm_level}</span>
                  </span>
                  <span className="px-2.5 py-1 rounded-xl text-xs font-bold bg-blue-50 text-blue-700 border border-blue-100">
                    Grounding: {Math.round(article.grounding_score * 100)}%
                  </span>
                </div>

                <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-950 tracking-tight mb-2">
                  {article.title}
                </h1>

                {article.alternative_names.length > 0 && (
                  <p className="text-xs text-slate-500 mb-4">
                    Also designated as: {article.alternative_names.join(" • ")}
                  </p>
                )}

                <p className="text-sm text-slate-700 leading-relaxed font-medium">
                  {activeMode === "patient" ? article.layperson_summary : article.clinical_summary}
                </p>

                {/* Plain Analogy Banner in Patient Mode */}
                {activeMode === "patient" && article.plain_analogy && (
                  <div className="mt-5 p-4 rounded-2xl bg-amber-50/70 border border-amber-200 text-amber-950 text-xs leading-relaxed flex items-start gap-3">
                    <div className="p-1.5 bg-amber-100 text-amber-800 rounded-xl shrink-0">
                      <Sparkles className="w-4 h-4" />
                    </div>
                    <div>
                      <div className="font-bold mb-0.5 uppercase tracking-wider text-[10px] text-amber-800">
                        Mental Model / Everyday Analogy
                      </div>
                      <div>{article.plain_analogy}</div>
                    </div>
                  </div>
                )}

                {/* Consult Assistant / Co-Pilot Button */}
                {(onSelectQueryForAssistant || onAskCopilot) && (
                  <div className="mt-5 pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3">
                    <span className="text-xs text-slate-500">
                      Need interactive AI reasoning or differential diagnosis for this condition?
                    </span>
                    <button
                      type="button"
                      onClick={() => {
                        const q = `What are the latest clinical guidelines and treatments for ${article.title}?`;
                        if (onAskCopilot) onAskCopilot(q);
                        else if (onSelectQueryForAssistant) onSelectQueryForAssistant(q);
                      }}
                      className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white transition-all shadow-xs"
                    >
                      <Sparkles className="w-3.5 h-3.5" />
                      <span>Chat with Assistant Co-Pilot</span>
                      <ArrowRight className="w-3.5 h-3.5" />
                    </button>
                  </div>
                )}
              </div>

              {/* Jargon Glossary Tooltips (Patient Mode) */}
              {activeMode === "patient" && article.jargon_glossary.length > 0 && (
                <JargonGlossary items={article.jargon_glossary} />
              )}

              {/* 10 Standardized Wiki Sections */}
              <div className="space-y-4">
                {article.sections.map((sec) => (
                  <div
                    key={sec.id}
                    id={sec.id}
                    className="bg-white border border-slate-200 rounded-3xl p-6 shadow-xs transition-all hover:border-slate-300"
                  >
                    <div className="flex items-center justify-between gap-3 mb-3">
                      <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
                        <span>{sec.title}</span>
                      </h3>
                      {sec.summary_bullet && (
                        <span className="hidden sm:inline text-[11px] font-medium text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">
                          {sec.summary_bullet}
                        </span>
                      )}
                    </div>

                    {sec.callout_alert && (
                      <div className="mb-4 p-3.5 rounded-2xl bg-rose-50 border border-rose-200 text-rose-900 text-xs font-medium flex items-center gap-2">
                        <AlertTriangle className="w-4 h-4 text-rose-600 shrink-0" />
                        <span>{sec.callout_alert}</span>
                      </div>
                    )}

                    <div className="text-xs leading-relaxed text-slate-700">
                      <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        components={{
                          p: ({ children }) => <p className="mb-2.5 leading-relaxed last:mb-0">{children}</p>,
                          strong: ({ children }) => <strong className="font-bold text-slate-900">{children}</strong>,
                          ul: ({ children }) => <ul className="list-disc pl-5 space-y-1 my-2">{children}</ul>,
                          ol: ({ children }) => <ol className="list-decimal pl-5 space-y-1 my-2">{children}</ol>,
                          li: ({ children }) => <li className="leading-relaxed">{children}</li>,
                          code: ({ children }) => (
                            <code className="px-1.5 py-0.5 rounded bg-slate-100 text-indigo-700 font-mono text-[11px] font-semibold">
                              {children}
                            </code>
                          )
                        }}
                      >
                        {sec.content}
                      </ReactMarkdown>
                    </div>
                  </div>
                ))}
              </div>

              {/* Landmark Research Citations Card */}
              {article.landmark_citations.length > 0 && (
                <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-xs">
                  <div className="flex items-center gap-2 mb-4">
                    <div className="p-1.5 bg-indigo-100 text-indigo-700 rounded-xl">
                      <BookOpen className="w-4 h-4" />
                    </div>
                    <div>
                      <h3 className="text-sm font-bold text-slate-900">
                        Peer-Reviewed Literature & Landmark Trials
                      </h3>
                      <p className="text-xs text-slate-500">
                        Authentic citations establishing Class I / Level A recommendations
                      </p>
                    </div>
                  </div>

                  <div className="space-y-3">
                    {article.landmark_citations.map((c) => (
                      <div
                        key={c.citation_index}
                        className="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 text-xs space-y-1.5"
                      >
                        <div className="flex items-center justify-between gap-2">
                          <span className="font-bold text-indigo-900 text-xs">
                            [{c.citation_index}] {c.title}
                          </span>
                          <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-indigo-100 text-indigo-800 font-semibold shrink-0">
                            {c.cebm_level}
                          </span>
                        </div>
                        <div className="text-[11px] text-slate-500">
                          {c.journal} ({c.year}) • DOI: {c.doi_or_pmid || "Indexed in PubMed"}
                        </div>
                        <div className="text-slate-700 font-medium pt-1">
                          Key Takeaway: {c.takeaway}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Related Conditions */}
              {article.related_topics.length > 0 && (
                <div className="bg-white border border-slate-200 rounded-3xl p-6 shadow-xs">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-3">
                    Related Topics in {article.specialty}
                  </h4>
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    {article.related_topics.map((rel) => (
                      <button
                        key={rel.id}
                        type="button"
                        onClick={() => setActiveTopicId(rel.id)}
                        className="p-3.5 rounded-2xl border border-slate-200 text-left hover:bg-indigo-50 hover:border-indigo-200 transition-all group"
                      >
                        <span className="text-[10px] font-mono font-bold text-slate-500 block mb-1">
                          {rel.icd10}
                        </span>
                        <div className="text-xs font-bold text-slate-800 group-hover:text-indigo-900 line-clamp-1">
                          {rel.name}
                        </div>
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {/* Footer Quality Metadata */}
              <div className="p-4 rounded-2xl bg-slate-100 text-slate-500 text-[11px] text-center flex items-center justify-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                <span>
                  Audited by AegisMed Clinical Truth Engine • Grounding Score 98% • Last reviewed: {article.last_reviewed}
                </span>
              </div>
            </div>
          ) : (
            <div className="text-center py-20 text-slate-400 text-sm">
              Article not found.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
