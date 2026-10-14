"use client";

import React, { useState } from "react";
import {
  calculateClinicalFormula,
  checkDrugInteractions
} from "@/lib/api";
import {
  Calculator,
  Activity,
  HeartPulse,
  Pill,
  Sparkles,
  CheckCircle2,
  AlertCircle,
  X,
  Sliders,
  ShieldAlert
} from "lucide-react";

interface ClinicalCalculatorWidgetProps {
  onClose?: () => void;
}

export function ClinicalCalculatorWidget({ onClose }: ClinicalCalculatorWidgetProps) {
  const [activeTab, setActiveTab] = useState<"egfr" | "bmi" | "cha2ds2" | "ddi">("egfr");

  // eGFR inputs
  const [creatinine, setCreatinine] = useState("1.3");
  const [age, setAge] = useState("65");
  const [sex, setSex] = useState<"male" | "female">("male");
  const [egfrResult, setEgfrResult] = useState<any>(null);

  // BMI inputs
  const [weightKg, setWeightKg] = useState("85");
  const [heightCm, setHeightCm] = useState("175");
  const [bmiResult, setBmiResult] = useState<any>(null);

  // CHA2DS2 inputs
  const [chf, setChf] = useState(false);
  const [htn, setHtn] = useState(true);
  const [afibAge, setAfibAge] = useState("68");
  const [diabetes, setDiabetes] = useState(false);
  const [stroke, setStroke] = useState(false);
  const [vascular, setVascular] = useState(false);
  const [afibSex, setAfibSex] = useState<"male" | "female">("male");
  const [chaResult, setChaResult] = useState<any>(null);

  // DDI inputs
  const [drugInput, setDrugInput] = useState("Paxlovid, Simvastatin");
  const [ddiResult, setDdiResult] = useState<any>(null);

  const [loading, setLoading] = useState(false);

  // Run eGFR calculation
  const handleCalcEgfr = async () => {
    setLoading(true);
    try {
      const res = await calculateClinicalFormula("egfr", {
        creatinine: parseFloat(creatinine),
        age: parseInt(age),
        sex
      });
      setEgfrResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  // Run BMI calculation
  const handleCalcBmi = async () => {
    setLoading(true);
    try {
      const res = await calculateClinicalFormula("bmi", {
        weight_kg: parseFloat(weightKg),
        height_cm: parseFloat(heightCm)
      });
      setBmiResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  // Run CHA2DS2-VASc calculation
  const handleCalcCha = async () => {
    setLoading(true);
    try {
      const res = await calculateClinicalFormula("cha2ds2_vasc", {
        chf,
        htn,
        age: parseInt(afibAge),
        diabetes,
        stroke_history: stroke,
        vascular_disease: vascular,
        sex: afibSex
      });
      setChaResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  // Run DDI check
  const handleCheckDdi = async () => {
    setLoading(true);
    try {
      const drugs = drugInput.split(",").map(d => d.trim()).filter(Boolean);
      const res = await checkDrugInteractions(drugs);
      setDdiResult(res);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-2xl border border-slate-200 bg-white shadow-xl p-5 my-6 text-slate-800">
      {/* Header */}
      <div className="flex items-center justify-between pb-4 border-b border-slate-100">
        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-xl bg-indigo-50 border border-indigo-100 text-indigo-600">
            <Calculator className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-slate-900 flex items-center gap-2">
              Medical Calculators & Safety Checks
            </h3>
            <p className="text-xs text-slate-500">
              Kidney function (eGFR), BMI staging, stroke risk assessment, and medicine interaction checks
            </p>
          </div>
        </div>
        {onClose && (
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 p-1 rounded-lg hover:bg-slate-100">
            <X className="w-5 h-5" />
          </button>
        )}
      </div>

      {/* Tabs */}
      <div className="flex flex-wrap gap-2 mt-4">
        <button
          onClick={() => setActiveTab("egfr")}
          className={`text-xs px-3.5 py-1.5 rounded-xl font-medium transition-all ${
            activeTab === "egfr"
              ? "bg-indigo-600 text-white shadow-sm"
              : "bg-slate-100 text-slate-600 hover:text-slate-900 border border-slate-200"
          }`}
        >
          Kidney Function (eGFR)
        </button>
        <button
          onClick={() => setActiveTab("bmi")}
          className={`text-xs px-3.5 py-1.5 rounded-xl font-medium transition-all ${
            activeTab === "bmi"
              ? "bg-indigo-600 text-white shadow-sm"
              : "bg-slate-100 text-slate-600 hover:text-slate-900 border border-slate-200"
          }`}
        >
          BMI & Weight Staging
        </button>
        <button
          onClick={() => setActiveTab("cha2ds2")}
          className={`text-xs px-3.5 py-1.5 rounded-xl font-medium transition-all ${
            activeTab === "cha2ds2"
              ? "bg-indigo-600 text-white shadow-sm"
              : "bg-slate-100 text-slate-600 hover:text-slate-900 border border-slate-200"
          }`}
        >
          Stroke Risk (AFib)
        </button>
        <button
          onClick={() => setActiveTab("ddi")}
          className={`text-xs px-3.5 py-1.5 rounded-xl font-medium transition-all ${
            activeTab === "ddi"
              ? "bg-indigo-600 text-white shadow-sm"
              : "bg-slate-100 text-slate-600 hover:text-slate-900 border border-slate-200"
          }`}
        >
          Medicine Interaction Check
        </button>
      </div>

      {/* Tab 1: eGFR */}
      {activeTab === "egfr" && (
        <div className="mt-5 space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div>
              <label className="text-[11px] text-slate-400 block mb-1">Serum Creatinine (mg/dL)</label>
              <input
                type="number"
                step="0.1"
                value={creatinine}
                onChange={e => setCreatinine(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="text-[11px] text-slate-400 block mb-1">Age (Years)</label>
              <input
                type="number"
                value={age}
                onChange={e => setAge(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="text-[11px] text-slate-400 block mb-1">Biological Sex</label>
              <select
                value={sex}
                onChange={e => setSex(e.target.value as any)}
                className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500"
              >
                <option value="male">Male</option>
                <option value="female">Female</option>
              </select>
            </div>
          </div>

          <button
            onClick={handleCalcEgfr}
            disabled={loading}
            className="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold flex items-center gap-2 transition-colors"
          >
            <Activity className="w-4 h-4" />
            Compute eGFR & Renal Cutoffs
          </button>

          {egfrResult && (
            <div className="p-4 rounded-xl bg-slate-900/90 border border-indigo-500/30 space-y-2 mt-3 text-xs">
              <div className="flex items-center justify-between">
                <span className="text-slate-300 font-medium">{egfrResult.calculator}:</span>
                <span className="text-base font-bold text-indigo-400 font-mono">
                  {egfrResult.egfr} {egfrResult.unit}
                </span>
              </div>
              <p className="text-slate-300"><span className="text-indigo-300 font-semibold">Staging:</span> {egfrResult.stage}</p>
              <p className="text-slate-400">{egfrResult.interpretation}</p>
              {egfrResult.pharmacotherapy_alerts && egfrResult.pharmacotherapy_alerts.length > 0 && (
                <div className="mt-2 pt-2 border-t border-slate-800">
                  <span className="text-amber-400 font-semibold block mb-1">Medication Dosing Warnings:</span>
                  <ul className="list-disc list-inside space-y-0.5 text-slate-300">
                    {egfrResult.pharmacotherapy_alerts.map((alt: string, i: number) => (
                      <li key={i}>{alt}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Tab 2: BMI */}
      {activeTab === "bmi" && (
        <div className="mt-5 space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label className="text-[11px] text-slate-400 block mb-1">Weight (kg)</label>
              <input
                type="number"
                value={weightKg}
                onChange={e => setWeightKg(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
            <div>
              <label className="text-[11px] text-slate-400 block mb-1">Height (cm)</label>
              <input
                type="number"
                value={heightCm}
                onChange={e => setHeightCm(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500"
              />
            </div>
          </div>

          <button
            onClick={handleCalcBmi}
            disabled={loading}
            className="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold flex items-center gap-2 transition-colors"
          >
            <Activity className="w-4 h-4" />
            Compute BMI & GLP-1 Indication
          </button>

          {bmiResult && (
            <div className="p-4 rounded-xl bg-slate-900/90 border border-indigo-500/30 space-y-2 mt-3 text-xs">
              <div className="flex items-center justify-between">
                <span className="text-slate-300 font-medium">WHO Body Mass Index:</span>
                <span className="text-base font-bold text-indigo-400 font-mono">
                  {bmiResult.bmi} {bmiResult.unit}
                </span>
              </div>
              <p className="text-slate-300"><span className="text-indigo-300 font-semibold">Classification:</span> {bmiResult.category}</p>
              <p className="text-slate-300/90 leading-relaxed"><span className="text-emerald-400 font-semibold">GLP-1 Indication:</span> {bmiResult.guideline_indications}</p>
            </div>
          )}
        </div>
      )}

      {/* Tab 3: CHA2DS2 */}
      {activeTab === "cha2ds2" && (
        <div className="mt-5 space-y-4">
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
            <label className="flex items-center gap-2 cursor-pointer p-2.5 rounded-xl bg-slate-900 border border-slate-800">
              <input type="checkbox" checked={chf} onChange={e => setChf(e.target.checked)} className="rounded" />
              <span>Heart Failure (+1)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer p-2.5 rounded-xl bg-slate-900 border border-slate-800">
              <input type="checkbox" checked={htn} onChange={e => setHtn(e.target.checked)} className="rounded" />
              <span>Hypertension (+1)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer p-2.5 rounded-xl bg-slate-900 border border-slate-800">
              <input type="checkbox" checked={diabetes} onChange={e => setDiabetes(e.target.checked)} className="rounded" />
              <span>Diabetes (+1)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer p-2.5 rounded-xl bg-slate-900 border border-slate-800">
              <input type="checkbox" checked={stroke} onChange={e => setStroke(e.target.checked)} className="rounded" />
              <span>Prior Stroke / TIA (+2)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer p-2.5 rounded-xl bg-slate-900 border border-slate-800">
              <input type="checkbox" checked={vascular} onChange={e => setVascular(e.target.checked)} className="rounded" />
              <span>Vascular Disease (+1)</span>
            </label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                placeholder="Age"
                value={afibAge}
                onChange={e => setAfibAge(e.target.value)}
                className="w-full px-2.5 py-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-white"
              />
            </div>
          </div>

          <button
            onClick={handleCalcCha}
            disabled={loading}
            className="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold flex items-center gap-2 transition-colors"
          >
            <HeartPulse className="w-4 h-4" />
            Stratify Thromboembolic Risk
          </button>

          {chaResult && (
            <div className="p-4 rounded-xl bg-slate-900/90 border border-indigo-500/30 space-y-2 mt-3 text-xs">
              <div className="flex items-center justify-between">
                <span className="text-slate-300 font-medium">CHA2DS2-VASc Score:</span>
                <span className="text-base font-bold text-indigo-400 font-mono">
                  {chaResult.score} Points ({chaResult.risk_level})
                </span>
              </div>
              <p className="text-emerald-300/90 leading-relaxed font-medium">
                Recommendation: {chaResult.recommendation}
              </p>
              {chaResult.point_breakdown && (
                <p className="text-slate-400 text-[11px]">
                  Points Breakdown: {chaResult.point_breakdown.join(", ")}
                </p>
              )}
            </div>
          )}
        </div>
      )}

      {/* Tab 4: DDI */}
      {activeTab === "ddi" && (
        <div className="mt-5 space-y-4">
          <div>
            <label className="text-[11px] text-slate-400 block mb-1">
              Enter Medications (comma-separated, e.g. &quot;Paxlovid, Simvastatin, Lisinopril&quot;)
            </label>
            <input
              type="text"
              value={drugInput}
              onChange={e => setDrugInput(e.target.value)}
              className="w-full px-3 py-2.5 rounded-xl bg-slate-900 border border-slate-800 text-sm text-white focus:outline-none focus:border-indigo-500"
            />
          </div>

          <button
            onClick={handleCheckDdi}
            disabled={loading}
            className="px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white text-xs font-semibold flex items-center gap-2 transition-colors"
          >
            <Pill className="w-4 h-4" />
            Screen Drug Interactions & Black Box Warnings
          </button>

          {ddiResult && (
            <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3 mt-3 text-xs">
              <div className="flex items-center justify-between">
                <span className="text-slate-300 font-medium">
                  Screened: {ddiResult.screened_medications?.join(", ")}
                </span>
                <span className={`px-2 py-0.5 rounded font-bold ${
                  ddiResult.interactions_found > 0
                    ? "bg-rose-500/20 text-rose-300 border border-rose-500/40"
                    : "bg-emerald-500/20 text-emerald-300 border border-emerald-500/40"
                }`}>
                  {ddiResult.interactions_found} Interactions Detected
                </span>
              </div>

              {ddiResult.ddi_alerts?.map((alert: any, idx: number) => (
                <div key={idx} className="p-3 rounded-lg bg-rose-950/30 border border-rose-500/30 text-rose-200 space-y-1">
                  <div className="flex items-center gap-1.5 font-bold text-rose-400">
                    <ShieldAlert className="w-4 h-4" />
                    {alert.severity} Interaction
                  </div>
                  <p><span className="text-slate-300">Mechanism:</span> {alert.mechanism}</p>
                  <p><span className="text-slate-300">Clinical Risk:</span> {alert.clinical_risk}</p>
                  <p><span className="text-slate-300">Action:</span> {alert.management}</p>
                </div>
              ))}

              {ddiResult.black_box_and_safety_profiles?.map((profile: any, idx: number) => (
                <div key={idx} className="p-3 rounded-lg bg-amber-950/30 border border-amber-500/30 text-amber-200 space-y-1">
                  <span className="font-bold text-amber-300 block">{profile.drug} Safety Profile</span>
                  <p><span className="text-slate-300">Black Box:</span> {profile.black_box_warning}</p>
                  <p><span className="text-slate-300">Organ Cutoffs:</span> {profile.organ_thresholds}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
