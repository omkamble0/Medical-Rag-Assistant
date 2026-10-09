'use client';

import React, { useState } from 'react';
import { useMedicalQuery } from '@/hooks/useMedicalQuery';
import {
  Search,
  Sparkles,
  Stethoscope,
  HeartHandshake,
  AlertCircle,
  CheckCircle2,
  BookOpen,
  ArrowRight,
  ShieldCheck,
  RotateCcw,
  ExternalLink,
  ChevronDown,
  ChevronUp,
} from 'lucide-react';

export function MedicalQueryPanel() {
  const [query, setQuery] = useState('');
  const [audience, setAudience] = useState<'patient' | 'doctor'>('patient');
  const [expandedSources, setExpandedSources] = useState<{ [key: number]: boolean }>({});
  const { ask, loading, result, error, clear } = useMedicalQuery();

  const handleSearch = async (overrideQuery?: string, autoCorrect: boolean = false) => {
    const q = overrideQuery || query;
    if (!q.trim()) return;
    await ask(q, audience, autoCorrect);
  };

  const handleApplyCorrection = async (corrected: string) => {
    setQuery(corrected);
    await ask(corrected, audience, true);
  };

  const handleIgnoreCorrection = async (original: string) => {
    await ask(original, audience, true);
  };

  const toggleSourceExpand = (index: number) => {
    setExpandedSources((prev) => ({
      ...prev,
      [index]: !prev[index],
    }));
  };

  const sampleQueries = [
    { label: 'headavhe (Typo Test)', q: 'headavhe symptoms and warning signs' },
    { label: 'diabtes (Typo Test)', q: 'diabtes management and first line medication' },
    { label: 'High BP (Patient)', q: 'What is the DASH diet and normal blood pressure target?' },
    { label: 'Asthma (Doctor)', q: 'GINA guideline recommendations for ICS-formoterol in asthma', targetAudience: 'doctor' },
  ];

  return (
    <div className="w-full max-w-4xl mx-auto space-y-6">
      {/* Search Input Card */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 shadow-2xl backdrop-blur-md">
        {/* Audience Selector Tabs */}
        <div className="flex items-center justify-between pb-4 border-b border-slate-800/80 mb-4">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-teal-400" />
            <span className="text-sm font-semibold text-slate-200 tracking-wide uppercase">
              Agentic RAG Engine
            </span>
          </div>

          <div className="flex items-center bg-slate-950 p-1 rounded-xl border border-slate-800">
            <button
              type="button"
              onClick={() => setAudience('patient')}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
                audience === 'patient'
                  ? 'bg-gradient-to-r from-teal-500 to-emerald-500 text-white shadow-md'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <HeartHandshake className="w-3.5 h-3.5" />
              Patient Mode
            </button>

            <button
              type="button"
              onClick={() => setAudience('doctor')}
              className={`flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all ${
                audience === 'doctor'
                  ? 'bg-gradient-to-r from-indigo-500 to-blue-600 text-white shadow-md'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Stethoscope className="w-3.5 h-3.5" />
              Doctor Mode
            </button>
          </div>
        </div>

        {/* Query Input Form */}
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSearch();
          }}
          className="relative"
        >
          <div className="relative flex items-center">
            <Search className="absolute left-4 w-5 h-5 text-slate-400" />
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder={
                audience === 'patient'
                  ? 'Ask about symptoms, conditions, or treatments (e.g. "headavhe symptoms")...'
                  : 'Search clinical management protocols, trial endpoints, or DDx...'
              }
              className="w-full pl-12 pr-32 py-3.5 bg-slate-950/90 border border-slate-700/70 rounded-xl text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 text-sm md:text-base transition-all"
            />
            <div className="absolute right-2 flex items-center gap-1.5">
              {query && (
                <button
                  type="button"
                  onClick={() => {
                    setQuery('');
                    clear();
                  }}
                  className="p-1.5 text-slate-400 hover:text-slate-200 rounded-lg hover:bg-slate-800"
                >
                  <RotateCcw className="w-4 h-4" />
                </button>
              )}
              <button
                type="submit"
                disabled={loading || !query.trim()}
                className="flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 disabled:opacity-50 text-white font-medium text-xs md:text-sm rounded-lg shadow-lg shadow-teal-500/20 transition-all"
              >
                {loading ? (
                  <span className="flex items-center gap-1.5">
                    <Sparkles className="w-4 h-4 animate-spin" />
                    Analyzing...
                  </span>
                ) : (
                  <span className="flex items-center gap-1.5">
                    <Sparkles className="w-4 h-4" />
                    Ask RAG
                  </span>
                )}
              </button>
            </div>
          </div>
        </form>

        {/* Quick Sample Chips */}
        <div className="flex flex-wrap items-center gap-2 mt-3 pt-2">
          <span className="text-xs text-slate-400 font-medium">Quick Examples:</span>
          {sampleQueries.map((item, idx) => (
            <button
              key={idx}
              type="button"
              onClick={() => {
                setQuery(item.q);
                if (item.targetAudience) setAudience(item.targetAudience as any);
                handleSearch(item.q);
              }}
              className="px-2.5 py-1 text-xs bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 hover:text-white rounded-lg border border-slate-700/50 transition-colors"
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>

      {/* Query Guard Typo Interception Banner */}
      {result && result.status === 'needs_correction' && (
        <div className="bg-amber-950/40 border border-amber-500/40 rounded-2xl p-5 shadow-xl animate-in fade-in slide-in-from-top-2 duration-300">
          <div className="flex items-start gap-3">
            <AlertCircle className="w-6 h-6 text-amber-400 flex-shrink-0 mt-0.5" />
            <div className="space-y-3 flex-1">
              <div>
                <h4 className="text-sm font-semibold text-amber-200">
                  Query Guard: Medical Typo Detected
                </h4>
                <p className="text-sm text-slate-300 mt-1">
                  Did you mean:{' '}
                  <span className="font-bold text-amber-300 underline decoration-amber-400/60 decoration-2">
                    &quot;{result.corrected}&quot;
                  </span>
                  ?
                </p>
                {result.corrections && result.corrections.length > 0 && (
                  <div className="flex flex-wrap gap-2 mt-2">
                    {result.corrections.map((corr, i) => (
                      <span
                        key={i}
                        className="text-xs bg-amber-900/60 text-amber-200 px-2 py-0.5 rounded border border-amber-700/40"
                      >
                        &quot;{corr.original_word}&quot; → &quot;{corr.corrected_word}&quot; ({Math.round(corr.confidence * 100)}% match)
                      </span>
                    ))}
                  </div>
                )}
              </div>

              <div className="flex items-center gap-3 pt-1">
                <button
                  type="button"
                  onClick={() => handleApplyCorrection(result.corrected || '')}
                  className="flex items-center gap-1.5 px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-semibold text-xs rounded-xl shadow-md transition-colors"
                >
                  <CheckCircle2 className="w-4 h-4" />
                  Search with &quot;{result.corrected}&quot;
                </button>
                <button
                  type="button"
                  onClick={() => handleIgnoreCorrection(result.original || query)}
                  className="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium rounded-xl border border-slate-700 transition-colors"
                >
                  Keep &quot;{result.original || query}&quot;
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Error Message */}
      {error && (
        <div className="bg-rose-950/40 border border-rose-500/40 rounded-2xl p-4 text-rose-200 text-sm flex items-center gap-2">
          <AlertCircle className="w-5 h-5 text-rose-400 flex-shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {/* Answer & Sources Panel */}
      {result && result.status === 'ok' && (
        <div className="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 shadow-2xl backdrop-blur-md space-y-6 animate-in fade-in duration-300">
          {/* Header & Meta */}
          <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
            <div className="flex items-center gap-2">
              <span
                className={`px-2.5 py-1 rounded-full text-xs font-semibold uppercase tracking-wider ${
                  result.audience === 'patient'
                    ? 'bg-teal-500/20 text-teal-300 border border-teal-500/30'
                    : 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30'
                }`}
              >
                {result.audience === 'patient' ? 'Patient Synthesis' : 'Clinical Synthesis'}
              </span>

              {result.was_corrected && (
                <span className="px-2 py-0.5 rounded text-xs bg-amber-500/20 text-amber-300 border border-amber-500/30">
                  Auto-Corrected: &quot;{result.effective_query}&quot;
                </span>
              )}
            </div>

            <div className="flex items-center gap-2 text-xs text-slate-400">
              <span>Engine: {result.provider || 'Evidence RAG'}</span>
            </div>
          </div>

          {/* Formatted Answer */}
          <div className="prose prose-invert max-w-none text-slate-200 text-sm md:text-base leading-relaxed whitespace-pre-line">
            {result.answer}
          </div>

          {/* Evidence Sources Accordion */}
          {result.sources && result.sources.length > 0 && (
            <div className="pt-4 border-t border-slate-800/80 space-y-3">
              <div className="flex items-center gap-2 text-xs font-semibold text-slate-400 uppercase tracking-wider">
                <BookOpen className="w-4 h-4 text-teal-400" />
                Grounding Evidence & Citations ({result.sources.length})
              </div>

              <div className="grid grid-cols-1 gap-3">
                {result.sources.map((source, idx) => {
                  const isExpanded = Boolean(expandedSources[idx]);
                  return (
                    <div
                      key={idx}
                      className="bg-slate-950/80 border border-slate-800/90 rounded-xl p-4 transition-all hover:border-slate-700"
                    >
                      <div
                        onClick={() => toggleSourceExpand(idx)}
                        className="flex items-center justify-between cursor-pointer select-none"
                      >
                        <div className="flex items-center gap-2">
                          <span className="flex items-center justify-center w-5 h-5 rounded-full bg-teal-500/20 text-teal-400 text-xs font-bold border border-teal-500/30">
                            [{source.index || idx + 1}]
                          </span>
                          <h5 className="text-sm font-medium text-slate-200 hover:text-teal-300 transition-colors">
                            {source.title}
                          </h5>
                        </div>
                        <div className="flex items-center gap-2">
                          <span className="text-xs text-slate-400 hidden sm:inline">
                            {source.journal} ({source.year})
                          </span>
                          {isExpanded ? (
                            <ChevronUp className="w-4 h-4 text-slate-400" />
                          ) : (
                            <ChevronDown className="w-4 h-4 text-slate-400" />
                          )}
                        </div>
                      </div>

                      {isExpanded && (
                        <div className="mt-3 pt-3 border-t border-slate-800/60 text-xs text-slate-300 leading-relaxed bg-slate-900/60 p-3 rounded-lg">
                          <div className="text-slate-400 mb-1 font-semibold">Evidence Excerpt:</div>
                          {source.snippet}
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
