"use client";

import React from "react";
import { EmergencyTriageAlert } from "@/lib/types";
import { AlertOctagon, PhoneCall, Activity, ShieldAlert, HeartPulse } from "lucide-react";

interface TriageBannerProps {
  alert: EmergencyTriageAlert;
}

export function TriageBanner({ alert }: TriageBannerProps) {
  return (
    <div className="w-full bg-gradient-to-br from-rose-600 to-red-700 text-white rounded-2xl p-6 sm:p-8 shadow-xl shadow-red-200 animate-fade-in">
      <div className="flex items-start gap-4">
        <div className="p-3 bg-white/20 backdrop-blur-sm rounded-2xl text-white shadow-sm flex-shrink-0">
          <HeartPulse className="w-8 h-8 animate-pulse" />
        </div>
        <div className="flex-1">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/20 text-white text-xs font-bold tracking-wide uppercase mb-3">
            <ShieldAlert className="w-3.5 h-3.5" />
            Immediate Safety Alert
          </div>
          <h2 className="text-xl sm:text-2xl font-black text-white tracking-tight mb-2">
            {alert.headline}
          </h2>
          <p className="text-red-100 text-sm sm:text-base leading-relaxed mb-5">
            {alert.critical_guidance}
          </p>

          {/* Red Flag Symptoms */}
          {alert.red_flag_symptoms && alert.red_flag_symptoms.length > 0 && (
            <div className="bg-white/10 backdrop-blur-sm rounded-xl p-4 border border-white/20 mb-5">
              <h4 className="text-xs font-bold uppercase tracking-wider text-red-100 mb-2.5">
                Critical Red-Flag Symptoms:
              </h4>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs sm:text-sm text-white">
                {alert.red_flag_symptoms.map((symptom, idx) => (
                  <li key={idx} className="flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-white flex-shrink-0" />
                    <span>{symptom}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Emergency Hotlines */}
          <div className="flex flex-wrap gap-2.5 items-center">
            <span className="text-xs font-bold text-white mr-1 flex items-center gap-1.5">
              <PhoneCall className="w-4 h-4" /> Direct Emergency Lines:
            </span>
            {alert.emergency_contacts.map((contact, idx) => (
              <span
                key={idx}
                className="px-3.5 py-1.5 bg-white text-red-700 font-bold rounded-xl text-xs sm:text-sm shadow-sm"
              >
                {contact}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
