"use client";

import React from "react";
import { EmergencyTriageAlert } from "@/lib/types";
import { Stethoscope, ShieldAlert, AlertTriangle } from "lucide-react";

interface TriageBannerProps {
  alert: EmergencyTriageAlert;
}

export function TriageBanner({ alert }: TriageBannerProps) {
  return (
    <div className="w-full bg-gradient-to-br from-amber-500 via-rose-500 to-red-600 text-white rounded-2xl p-6 sm:p-7 shadow-lg shadow-rose-200/50 animate-fade-in border border-white/20">
      <div className="flex items-start gap-4">
        <div className="p-3 bg-white/20 backdrop-blur-md rounded-2xl text-white shadow-inner flex-shrink-0">
          <AlertTriangle className="w-7 h-7 animate-pulse text-amber-100" />
        </div>
        <div className="flex-1">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/20 text-white text-xs font-bold tracking-wide uppercase mb-2.5">
            <ShieldAlert className="w-3.5 h-3.5" />
            Clinical Acuity Advisory
          </div>
          <h2 className="text-lg sm:text-xl font-black text-white tracking-tight mb-2">
            {alert.headline}
          </h2>
          <p className="text-rose-50 text-xs sm:text-sm leading-relaxed mb-4">
            {alert.critical_guidance}
          </p>

          {/* Red Flag Symptoms */}
          {alert.red_flag_symptoms && alert.red_flag_symptoms.length > 0 && (
            <div className="bg-black/15 backdrop-blur-sm rounded-xl p-3.5 border border-white/15 mb-4">
              <h4 className="text-xs font-bold uppercase tracking-wider text-amber-100 mb-2">
                Identified Clinical Indicators Requiring Assessment:
              </h4>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-xs text-white">
                {alert.red_flag_symptoms.map((symptom, idx) => (
                  <li key={idx} className="flex items-center gap-2">
                    <span className="w-1.5 h-1.5 rounded-full bg-amber-200 flex-shrink-0" />
                    <span>{symptom}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Recommended Clinical Resources */}
          {alert.emergency_contacts && alert.emergency_contacts.length > 0 && (
            <div className="flex flex-wrap gap-2 items-center">
              <span className="text-xs font-semibold text-rose-100 mr-1 flex items-center gap-1.5">
                <Stethoscope className="w-3.5 h-3.5" /> Clinical Resources:
              </span>
              {alert.emergency_contacts.map((contact, idx) => (
                <span
                  key={idx}
                  className="px-3 py-1 bg-white/90 text-rose-900 font-semibold rounded-lg text-xs shadow-2xs"
                >
                  {contact}
                </span>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
