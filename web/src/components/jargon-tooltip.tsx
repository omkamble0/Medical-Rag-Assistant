"use client";

import React, { useState } from "react";
import { JargonItem } from "@/lib/types";
import { Sparkles, HelpCircle, BookOpen } from "lucide-react";

interface JargonGlossaryProps {
  items: JargonItem[];
}

export function JargonGlossary({ items }: JargonGlossaryProps) {
  const [activeTerm, setActiveTerm] = useState<string | null>(null);

  if (!items || items.length === 0) return null;

  return (
    <div className="bg-indigo-50/50 border border-indigo-100 rounded-2xl p-4 sm:p-5 my-4 shadow-xs">
      <div className="flex items-center gap-2 mb-3 text-indigo-900">
        <div className="p-1.5 bg-indigo-100 rounded-lg text-indigo-600">
          <BookOpen className="w-4 h-4" />
        </div>
        <div>
          <h4 className="text-xs font-bold uppercase tracking-wider text-indigo-900">
            Medical Terms Explained Simply
          </h4>
          <p className="text-xs text-indigo-700/80">
            Click any term below to see its plain-language definition
          </p>
        </div>
      </div>

      <div className="flex flex-wrap gap-2">
        {items.map((item, idx) => {
          const isSelected = activeTerm === item.term;
          return (
            <div key={idx} className="relative">
              <button
                type="button"
                onClick={() => setActiveTerm(isSelected ? null : item.term)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                  isSelected
                    ? "bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-300"
                    : "bg-white hover:bg-indigo-100/60 text-indigo-900 border border-indigo-200"
                }`}
              >
                <span>{item.term}</span>
                <HelpCircle className={`w-3.5 h-3.5 ${isSelected ? "text-indigo-200" : "text-indigo-500"}`} />
              </button>

              {isSelected && (
                <div className="absolute z-30 bottom-full left-0 mb-2 w-72 p-3.5 bg-white border border-indigo-100 rounded-2xl shadow-xl text-xs text-slate-700 animate-fade-in">
                  <div className="flex items-center gap-1.5 font-bold text-indigo-900 mb-1">
                    <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                    <span>{item.term}</span>
                  </div>
                  <div className="text-slate-600 leading-relaxed font-normal">
                    {item.plain_english}
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
