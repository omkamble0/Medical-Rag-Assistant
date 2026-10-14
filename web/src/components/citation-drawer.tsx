"use client";

import React from "react";
import { SourceDocument } from "@/lib/types";
import { BookOpen, ExternalLink, Award, CheckCircle2, ShieldCheck } from "lucide-react";

interface CitationDrawerProps {
  sources: SourceDocument[];
  activeCitation: number | null;
  onSelectCitation: (index: number) => void;
}

export function CitationDrawer({ sources, activeCitation, onSelectCitation }: CitationDrawerProps) {
  if (!sources || sources.length === 0) return null;

  return (
    <div className="bg-white border border-slate-200/90 rounded-2xl p-5 sm:p-6 shadow-sm">
      <div className="flex items-center justify-between gap-2 mb-4 pb-3.5 border-b border-slate-100">
        <div className="flex items-center gap-2.5 text-slate-900">
          <div className="p-2 bg-indigo-50 text-indigo-600 rounded-xl border border-indigo-100">
            <BookOpen className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-slate-900">
              Verified Medical Sources
            </h3>
            <p className="text-xs text-slate-500">
              WHO & Peer-Reviewed Evidence Repository
            </p>
          </div>
        </div>
        <span className="text-xs font-bold px-2.5 py-1 bg-slate-100 text-slate-700 rounded-full border border-slate-200">
          {sources.length} Studies
        </span>
      </div>

      <div className="space-y-3.5">
        {sources.map((source) => {
          const isHighlighted = activeCitation === source.citation_index;
          return (
            <div
              key={source.id}
              id={`source-${source.citation_index}`}
              onClick={() => onSelectCitation(source.citation_index)}
              className={`p-4 rounded-2xl border transition-all duration-200 cursor-pointer ${
                isHighlighted
                  ? "bg-indigo-50/50 border-indigo-300 ring-2 ring-indigo-200 shadow-md"
                  : "bg-white border-slate-200/80 hover:border-slate-300 hover:bg-slate-50/60 shadow-2xs"
              }`}
            >
              {/* Header with Citation Badge & Oxford CEBM Tier */}
              <div className="flex items-start justify-between gap-2 mb-2">
                <div className="flex items-center gap-2">
                  <span className="flex items-center justify-center w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 font-bold text-xs border border-indigo-200">
                    [{source.citation_index}]
                  </span>
                  <span className="text-xs font-semibold text-slate-700 truncate max-w-[180px]">
                    {source.journal}
                  </span>
                </div>
                <span className="text-xs font-medium text-slate-400">({source.year})</span>
              </div>

              {/* Title */}
              <h4 className="text-xs sm:text-sm font-bold text-slate-900 leading-snug mb-2 hover:text-indigo-600 transition-colors">
                {source.title}
              </h4>

              {/* Oxford CEBM Level Badge */}
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-teal-50 border border-teal-200 text-teal-800 text-[11px] font-semibold mb-2.5">
                <Award className="w-3.5 h-3.5 text-teal-600" />
                <span>{source.evidence_level}</span>
              </div>

              {/* Verified Snippet / Grounding Quote */}
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-200/60 text-xs text-slate-600 leading-relaxed italic mb-2.5">
                &ldquo;{source.snippet}&rdquo;
              </div>

              {/* Footer with Relevance & DOI */}
              <div className="flex items-center justify-between text-xs text-slate-500 pt-2 border-t border-slate-100">
                <span className="flex items-center gap-1 text-emerald-600 font-semibold">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Verified Source
                </span>
                {source.doi_or_pmid && (
                  <a
                    href={`https://doi.org/${source.doi_or_pmid}`}
                    target="_blank"
                    rel="noreferrer"
                    onClick={(e) => e.stopPropagation()}
                    className="flex items-center gap-1 text-slate-500 hover:text-indigo-600 transition-colors font-medium text-[11px]"
                  >
                    <span>DOI Link</span>
                    <ExternalLink className="w-3 h-3 opacity-80" />
                  </a>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
