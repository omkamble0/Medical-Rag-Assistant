"use client";

import React, { useState, useRef, useEffect } from "react";
import { JargonItem } from "@/lib/types";
import { Sparkles, HelpCircle, BookOpen, X, CheckCircle2 } from "lucide-react";

interface JargonGlossaryProps {
  items: JargonItem[];
}

export function JargonGlossary({ items }: JargonGlossaryProps) {
  const [activeTerm, setActiveTerm] = useState<string | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  // Close popup if user clicks outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setActiveTerm(null);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  if (!items || items.length === 0) return null;

  return (
    <div
      ref={containerRef}
      className="bg-gradient-to-br from-indigo-50/70 via-white to-indigo-50/40 border border-indigo-100/90 rounded-2xl p-4 sm:p-5 my-4 shadow-xs"
    >
      <div className="flex items-center justify-between gap-2 mb-3">
        <div className="flex items-center gap-2 text-indigo-900">
          <div className="p-1.5 bg-indigo-100 rounded-lg text-indigo-600 shadow-xs">
            <BookOpen className="w-4 h-4" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h4 className="text-xs font-bold uppercase tracking-wider text-indigo-900">
                Medical Terms Explained Simply
              </h4>
              <span className="inline-flex items-center px-1.5 py-0.5 rounded-full text-[10px] font-bold bg-indigo-100 text-indigo-700">
                {items.length} detected
              </span>
            </div>
            <p className="text-xs text-indigo-700/80 mt-0.5">
              Click any medical concept below to see its everyday definition
            </p>
          </div>
        </div>
      </div>

      <div className="flex flex-wrap gap-2">
        {items.map((item, idx) => {
          const isSelected = activeTerm === item.term;
          return (
            <div key={idx} className="relative">
              <button
                type="button"
                aria-expanded={isSelected}
                onClick={() => setActiveTerm(isSelected ? null : item.term)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold transition-all shadow-xs cursor-pointer ${
                  isSelected
                    ? "bg-indigo-600 text-white shadow-md ring-2 ring-indigo-300 scale-102"
                    : "bg-white hover:bg-indigo-50 hover:border-indigo-300 text-indigo-900 border border-indigo-200/80"
                }`}
              >
                <span>{item.term}</span>
                <HelpCircle
                  className={`w-3.5 h-3.5 transition-transform ${
                    isSelected ? "text-indigo-200 rotate-180" : "text-indigo-400 group-hover:text-indigo-600"
                  }`}
                />
              </button>

              {isSelected && (
                <div
                  role="tooltip"
                  className="absolute z-40 bottom-full left-0 mb-2 w-72 max-w-[calc(100vw-2.5rem)] sm:w-80 p-4 bg-white border border-indigo-100 rounded-2xl shadow-xl text-xs text-slate-700 animate-in fade-in zoom-in-95 duration-150"
                >
                  <div className="flex items-center justify-between gap-1.5 font-bold text-indigo-900 mb-2 pb-1.5 border-b border-indigo-50">
                    <div className="flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5 text-indigo-600 shrink-0" />
                      <span className="truncate">{item.term}</span>
                    </div>
                    <button
                      type="button"
                      onClick={(e) => {
                        e.stopPropagation();
                        setActiveTerm(null);
                      }}
                      className="p-1 hover:bg-slate-100 rounded-full text-slate-400 hover:text-slate-600 transition-colors"
                      title="Close definition"
                    >
                      <X className="w-3.5 h-3.5" />
                    </button>
                  </div>
                  <div className="text-slate-600 leading-relaxed font-normal">
                    {item.plain_english}
                  </div>
                  <div className="mt-2.5 pt-2 border-t border-slate-100 flex items-center gap-1 text-[10px] text-emerald-700 font-medium">
                    <CheckCircle2 className="w-3 h-3 text-emerald-500 shrink-0" />
                    <span>Verified plain-language clinical translation</span>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

