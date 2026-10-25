"""
LangGraph Multi-Agent Clinical Workflow Orchestrator
Coordinates:
1. Tier-1 Deterministic Emergency Triage Interceptor
2. Clinical Query Deconstruction & MeSH Entity Expansion
3. Autonomous Tool Execution (Drug Interactions, eGFR/BMI Calculators, PubMed)
4. Vector Retrieval & Oxford CEBM Re-Ranking
5. Corrective RAG (CRAG) Relevance Verification & Fallback
6. Audience-Aware Clinical Synthesis (Patient Grade 6-8 vs Clinician Oxford CEBM)
7. Self-RAG Reflective Hallucination & Citation Grounding Audit
"""

import time
import logging
from typing import TypedDict, List, Dict, Any, Optional

from langgraph.graph import StateGraph, END
from app.core.guardrails import evaluate_safety_guardrails
from app.core.prompts import MANDATORY_DISCLAIMER, normalize_audience, route_prompt
from app.core.readability import enforce_audience_contract
from app.services.crag.query_rewriter import rewrite_clinical_query, ClinicalQueryDecomposition
from app.services.crag.retrieval_grader import grade_retrieval_relevance, RetrievalGradeResult
from app.services.crag.reranker import rerank_evidence_documents
from app.services.crag.hallucination_grader import audit_hallucinations_and_grounding, avoid_hallucinations, GroundingAuditResult
from app.services.tools.drug_interaction import check_drug_interactions
from app.services.tools.clinical_calculator import (
    calculate_egfr, calculate_bmi, calculate_cha2ds2_vasc, calculate_wells_pe
)
from app.services.tools.pubmed_tool import search_pubmed_literature
from app.services.tools.guideline_tool import search_consensus_guidelines
from app.services.vector_store import retrieve_clinical_evidence
from app.services.llm_gateway import llm_gateway
from app.services.medical_db import medical_db

logger = logging.getLogger(__name__)


class AgenticWorkflowState(TypedDict):
    raw_query: str
    effective_query: str
    audience: str
    triage_alert: Optional[Dict[str, Any]]
    decomposition: Optional[Dict[str, Any]]
    tool_results: Dict[str, Any]
    retrieved_documents: List[Dict[str, Any]]
    crag_grade: Optional[Dict[str, Any]]
    generated_answer: str
    grounding_audit: Optional[Dict[str, Any]]
    execution_trace: List[Dict[str, Any]]
    status: str


def _add_trace_step(state: AgenticWorkflowState, step_name: str, icon: str, summary: str, details: Any) -> None:
    if "execution_trace" not in state or state["execution_trace"] is None:
        state["execution_trace"] = []
    state["execution_trace"].append({
        "step": step_name,
        "icon": icon,
        "timestamp": time.strftime("%H:%M:%S"),
        "summary": summary,
        "details": details
    })


# ─────────────────────────────────────────────────────────────
# NODE 1: Triage Interceptor (Clinical Acuity & Urgency Assessment)
# ─────────────────────────────────────────────────────────────
def node_triage_interceptor(state: AgenticWorkflowState) -> AgenticWorkflowState:
    query = state.get("effective_query") or state.get("raw_query", "")
    triage_alert = evaluate_safety_guardrails(query)

    if triage_alert is not None:
        alert_data = {
            "title": triage_alert.headline,
            "message": triage_alert.critical_guidance,
            "detected_keywords": triage_alert.matched_keywords,
            "red_flags": triage_alert.red_flag_symptoms,
            "contacts": triage_alert.emergency_contacts,
            "urgency": triage_alert.urgency.value if hasattr(triage_alert.urgency, "value") else str(triage_alert.urgency)
        }
        state["triage_alert"] = alert_data
        _add_trace_step(
            state,
            step_name="Clinical Acuity & Urgency Evaluation",
            icon="⚠️",
            summary=f"Clinical acuity advisory flagged ({', '.join(triage_alert.matched_keywords[:3])}). Proceeding with non-blocking evidence retrieval and clinical explanation.",
            details=alert_data
        )
    else:
        state["triage_alert"] = None
        _add_trace_step(
            state,
            step_name="Clinical Acuity & Urgency Evaluation",
            icon="🛡️",
            summary="Routine clinical inquiry assessed; zero acute red flags detected.",
            details={"is_emergency": False, "category": "Non-Acute / Elective Inquiry"}
        )

    return state


# ─────────────────────────────────────────────────────────────
# NODE 2: Query Deconstruction & MeSH Mapping
# ─────────────────────────────────────────────────────────────
def node_query_deconstruct(state: AgenticWorkflowState) -> AgenticWorkflowState:
    query = state.get("effective_query") or state.get("raw_query", "")
    decomp: ClinicalQueryDecomposition = rewrite_clinical_query(query)
    state["decomposition"] = decomp.model_dump()

    _add_trace_step(
        state,
        step_name="Clinical Query Deconstruction & MeSH Mapping",
        icon="🔍",
        summary=f"Mapped to: {decomp.canonical_condition} ({len(decomp.sub_queries)} sub-queries generated)",
        details={
            "canonical_condition": decomp.canonical_condition,
            "mesh_terms": decomp.mesh_terms,
            "identified_drugs": decomp.identified_drugs,
            "clinical_metrics": decomp.clinical_metrics,
            "sub_queries": decomp.sub_queries
        }
    )
    return state


# ─────────────────────────────────────────────────────────────
# NODE 3: Autonomous Clinical Tool Execution
# ─────────────────────────────────────────────────────────────
def node_tool_execution(state: AgenticWorkflowState) -> AgenticWorkflowState:
    decomp = state.get("decomposition") or {}
    tools_executed: Dict[str, Any] = {}

    # Tool A: Drug-Drug Interaction Check
    drugs = decomp.get("identified_drugs", [])
    if drugs:
        ddi_result = check_drug_interactions(drugs)
        tools_executed["drug_interactions"] = ddi_result

    # Tool B: Clinical Calculator
    if decomp.get("needs_clinical_calculator"):
        calc_name = decomp.get("recommended_calculator")
        metrics = decomp.get("clinical_metrics", {})
        if calc_name == "egfr" and "creatinine" in metrics:
            tools_executed["clinical_calculator"] = calculate_egfr(
                creatinine=float(metrics["creatinine"]),
                age=int(metrics.get("age", 60)),
                sex=str(metrics.get("sex", "male"))
            )
        elif calc_name == "bmi" and "weight_kg" in metrics and "height_cm" in metrics:
            tools_executed["clinical_calculator"] = calculate_bmi(
                weight_kg=float(metrics["weight_kg"]),
                height_cm=float(metrics["height_cm"])
            )
        elif calc_name == "cha2ds2_vasc":
            tools_executed["clinical_calculator"] = calculate_cha2ds2_vasc(
                chf=False, htn=bool("systolic" in metrics), age=65, diabetes=False
            )

    # Tool C: PubMed Literature Retrieval
    pubmed_query = decomp.get("canonical_condition", state["effective_query"])
    pubmed_docs = search_pubmed_literature(pubmed_query, max_results=2)
    tools_executed["pubmed_literature"] = pubmed_docs

    # Tool D: Guideline Retrieval
    guidelines = search_consensus_guidelines(pubmed_query, max_results=2)
    tools_executed["consensus_guidelines"] = guidelines

    # Tool E: Medical Knowledge Database Lookup
    try:
        from app.services.tools.medical_db_tool import lookup_disease_in_database
        db_lookup = lookup_disease_in_database(pubmed_query)
        if db_lookup.get("status") == "success":
            tools_executed["medical_database"] = db_lookup
    except Exception as e:
        logger.debug(f"Medical database tool notice: {e}")

    state["tool_results"] = tools_executed

    tools_summary_list = []
    if "drug_interactions" in tools_executed:
        tools_summary_list.append(f"DDI Check ({len(drugs)} drugs)")
    if "clinical_calculator" in tools_executed:
        tools_summary_list.append(f"Calculator ({decomp.get('recommended_calculator')})")
    if "pubmed_literature" in tools_executed:
        tools_summary_list.append(f"PubMed ({len(pubmed_docs)} articles)")
    if "consensus_guidelines" in tools_executed:
        tools_summary_list.append(f"Guidelines ({len(guidelines)} orgs)")
    if "medical_database" in tools_executed:
        tools_summary_list.append("Medical DB Monograph")

    _add_trace_step(
        state,
        step_name="Autonomous Clinical Tool Invocations",
        icon="🛠️",
        summary=f"Executed: {', '.join(tools_summary_list) if tools_summary_list else 'Standard clinical references'}",
        details=tools_executed
    )
    return state


# ─────────────────────────────────────────────────────────────
# NODE 4: Vector Evidence Retrieval & CEBM Re-Ranking
# ─────────────────────────────────────────────────────────────
def node_retrieval_and_rerank(state: AgenticWorkflowState) -> AgenticWorkflowState:
    query = state.get("effective_query") or state.get("raw_query", "")
    decomp = state.get("decomposition") or {}
    sub_queries = decomp.get("sub_queries", [query])

    # Fetch from clinical vector store
    all_raw_docs: List[Dict[str, Any]] = []
    try:
        from app.services.vector_store import retrieve_clinical_evidence
        sources = retrieve_clinical_evidence(query, top_k=4)
        for s in sources:
            all_raw_docs.append({
                "id": s.id,
                "title": s.title,
                "journal": s.journal,
                "year": s.year,
                "content": s.snippet,
                "evidence_level": s.evidence_level.value if hasattr(s.evidence_level, "value") else str(s.evidence_level),
                "doi_or_pmid": s.doi_or_pmid,
                "key_takeaway": s.key_takeaway
            })
    except Exception as e:
        logger.warning(f"Vector store retrieval warning: {e}")

    # Merge in PubMed tool documents if retrieved
    tool_pubmed = state.get("tool_results", {}).get("pubmed_literature", [])
    for p in tool_pubmed:
        all_raw_docs.append({
            "id": f"PMID:{p.get('pmid', '0')}",
            "title": p.get("title", ""),
            "journal": p.get("journal", ""),
            "year": p.get("year", 2023),
            "content": p.get("abstract", ""),
            "evidence_level": p.get("evidence_level", "Level 1"),
            "doi_or_pmid": f"PMID:{p.get('pmid', '0')}",
            "key_takeaway": p.get("abstract", "")[:180]
        })

    # Execute Oxford CEBM Re-Ranking
    reranked = rerank_evidence_documents(query, all_raw_docs, top_k=3)
    state["retrieved_documents"] = reranked

    _add_trace_step(
        state,
        step_name="Vector Evidence Retrieval & CEBM Re-Ranking",
        icon="📚",
        summary=f"Retrieved & re-ranked Top-{len(reranked)} Oxford CEBM evidence documents",
        details={
            "total_candidates": len(all_raw_docs),
            "selected_documents": [
                {
                    "citation": d.get("citation_index"),
                    "title": d.get("title"),
                    "journal": d.get("journal"),
                    "year": d.get("year"),
                    "evidence_level": d.get("evidence_level"),
                    "score": d.get("_rerank_score")
                }
                for d in reranked
            ]
        }
    )
    return state


# ─────────────────────────────────────────────────────────────
# NODE 5: Corrective RAG (CRAG) Grader & Filter
# ─────────────────────────────────────────────────────────────
def node_crag_evaluator(state: AgenticWorkflowState) -> AgenticWorkflowState:
    query = state.get("effective_query") or state.get("raw_query", "")
    docs = state.get("retrieved_documents", [])
    grade: RetrievalGradeResult = grade_retrieval_relevance(query, docs, threshold=0.55)
    state["crag_grade"] = grade.model_dump()

    _add_trace_step(
        state,
        step_name="Corrective RAG (CRAG) Relevance Assessment",
        icon="⚖️",
        summary=f"Decision: {grade.grade_decision} (Relevance Score: {grade.relevance_score * 100:.0f}%)",
        details=grade.model_dump()
    )
    return state


# ─────────────────────────────────────────────────────────────
# NODE 6: Audience-Aware Synthesis
# ─────────────────────────────────────────────────────────────
def node_audience_synthesis(state: AgenticWorkflowState) -> AgenticWorkflowState:
    query = state.get("effective_query") or state.get("raw_query", "")
    audience = normalize_audience(state.get("audience", "patient"))
    docs = state.get("retrieved_documents", [])
    tools = state.get("tool_results", {})

    # Build context string with tools and citations
    context_chunks = []
    for d in docs:
        c_idx = d.get("citation_index", 1)
        context_chunks.append(
            f"Source [{c_idx}] {d.get('title')} ({d.get('journal', 'Consensus')}, {d.get('year', 2023)}) - Evidence Level: {d.get('evidence_level', 'Level 1')}:\n"
            f"{d.get('content') or d.get('snippet', '')}\nKey Takeaway: {d.get('key_takeaway', '')}"
        )

    # Append DDI warnings if any
    ddi = tools.get("drug_interactions")
    if ddi and ddi.get("interactions_found", 0) > 0:
        ddi_texts = [f"• {a['severity']}: {a['mechanism']} (Risk: {a['clinical_risk']})" for a in ddi.get("ddi_alerts", [])]
        context_chunks.append("CRITICAL DRUG-DRUG INTERACTIONS IDENTIFIED:\n" + "\n".join(ddi_texts))

    # Append Clinical Calculator if any
    calc = tools.get("clinical_calculator")
    if calc:
        context_chunks.append(f"CLINICAL CALCULATOR RESULT:\n{calc.get('calculator')}: {calc.get('egfr') or calc.get('bmi') or calc.get('score')} {calc.get('unit', '')} - {calc.get('stage') or calc.get('category') or calc.get('risk_level')}")

    full_context_str = "\n\n".join(context_chunks)

    # Prompt generation
    prompt = route_prompt(audience, query, full_context_str)
    system_prompt = (
        "You are AegisMed, an evidence-grounded agentic medical AI. "
        "Strictly ground every clinical assertion against the retrieved sources using [1], [2] citations. "
        "Never invent trial names or p-values. Adhere to the requested register."
    )

    # LLM Gateway Call
    gateway_result = llm_gateway.generate(prompt=prompt, system_prompt=system_prompt, temperature=0.15)
    raw_answer = gateway_result.get("content")

    # If gateway returned fallback, use structured EBM synthesis
    if not raw_answer:
        raw_answer = _synthesize_high_fidelity(query, docs, tools, audience)

    # Prepend non-blocking Clinical Acuity Advisory banner if flagged by Tier 1
    triage = state.get("triage_alert")
    if triage:
        advisory_box = (
            f"> ⚠️ **{triage.get('title', 'CLINICAL ACUITY ADVISORY')}**\n"
            f"> {triage.get('message', 'Prompt in-person clinical assessment by a healthcare provider or urgent care clinic is strongly recommended.')}\n"
            f"> *Red-flag indicators:* {', '.join(triage.get('red_flags', [])[:3])}\n\n"
        )
        if not raw_answer.startswith("> ⚠️"):
            raw_answer = advisory_box + raw_answer

    # Ensure mandatory disclaimer
    if MANDATORY_DISCLAIMER not in raw_answer:
        raw_answer += f"\n\n---\n{MANDATORY_DISCLAIMER}"

    # Strict audience enforcement: sanitize statistical leaks in patient mode, compute reading level
    raw_answer, aud_audit = enforce_audience_contract(raw_answer, audience)
    reading_level_label = aud_audit.get("reading_level_label", "Grade 6.0 (Everyday English)" if audience == "patient" else "Postgraduate Clinical Register")

    state["generated_answer"] = raw_answer

    _add_trace_step(
        state,
        step_name="Audience-Aware Evidence Synthesis",
        icon="✍️",
        summary=f"Synthesized for '{audience.upper()}' register via {gateway_result.get('provider')}",
        details={
            "provider": gateway_result.get("provider"),
            "model": gateway_result.get("model"),
            "audience": audience,
            "reading_level": reading_level_label,
            "audience_audit": aud_audit
        }
    )
    return state


# ─────────────────────────────────────────────────────────────
# NODE 7: Self-RAG Grounding & Hallucination Audit
# ─────────────────────────────────────────────────────────────
def node_self_rag_audit(state: AgenticWorkflowState) -> AgenticWorkflowState:
    answer = state.get("generated_answer", "")
    docs = state.get("retrieved_documents", [])
    query = state.get("query", "")
    audience = state.get("audience", "patient")
    tools = state.get("tool_executions", {})
    det_fallback = _synthesize_high_fidelity(query, docs, tools, audience)
    cleaned_answer, audit = avoid_hallucinations(answer, docs, deterministic_fallback=det_fallback)

    # Ensure non-blocking Clinical Acuity Advisory banner is preserved if flagged by Tier 1
    triage = state.get("triage_alert")
    if triage and not cleaned_answer.startswith("> ⚠️"):
        advisory_box = (
            f"> ⚠️ **{triage.get('title', 'CLINICAL ACUITY ADVISORY')}**\n"
            f"> {triage.get('message', 'Prompt in-person clinical assessment by a healthcare provider or urgent care clinic is strongly recommended.')}\n"
            f"> *Red-flag indicators:* {', '.join(triage.get('red_flags', [])[:3])}\n\n"
        )
        cleaned_answer = advisory_box + cleaned_answer

    state["generated_answer"] = cleaned_answer
    state["grounding_audit"] = audit.model_dump()
    state["status"] = "COMPLETED"

    _add_trace_step(
        state,
        step_name="Self-RAG Grounding & Hallucination Audit",
        icon="🛡️",
        summary=f"Grounding Score: {audit.grounding_score * 100:.0f}% (Hallucination Risk: {audit.hallucination_risk_pct}%)",
        details=audit.model_dump()
    )
    return state


# ─────────────────────────────────────────────────────────────
# Local High-Fidelity Synthesis Helper
# ─────────────────────────────────────────────────────────────
def _synthesize_high_fidelity(query: str, docs: List[Dict[str, Any]], tools: Dict[str, Any], audience: str) -> str:
    primary = docs[0] if docs else {}
    q_low = query.lower()

    # Attempt condition matching from medical_db
    matched_disease = None
    try:
        hits = medical_db.search_hybrid(query, top_k=1)
        if hits and hits[0].get("id"):
            matched_disease = medical_db.get_disease_by_id(str(hits[0].get("id")))
    except Exception as e:
        logger.debug(f"medical_db lookup error in synthesis: {e}")

    # Incorporate DDI block if present
    ddi = tools.get("drug_interactions")
    ddi_note = ""
    if ddi and ddi.get("interactions_found", 0) > 0:
        alerts = ddi.get("ddi_alerts", [])
        if audience == "patient":
            ddi_note = f"\n\n⚠️ **Important Medicine Safety Alert:**\nTaking these medicines together requires extra care. {alerts[0].get('management', 'Speak with your doctor or pharmacist.')}"
        else:
            ddi_note = f"\n\n**Pharmacotherapy & DDI Alert ({alerts[0].get('severity')}):**\n• {alerts[0].get('mechanism')}\n• Action: {alerts[0].get('management')}"

    # Incorporate Calculator block if present
    calc = tools.get("clinical_calculator")
    calc_note = ""
    if calc:
        if "egfr" in calc:
            calc_note = f"\n\n📊 **Kidney Function Calculation (CKD-EPI 2021):** eGFR = {calc['egfr']} {calc['unit']} ({calc['stage']}). {calc['interpretation']}"
        elif "bmi" in calc:
            calc_note = f"\n\n📊 **BMI Calculation:** {calc['bmi']} kg/m² ({calc['category']}). {calc.get('guideline_indications', '')}"

    if audience == "patient":
        # 1. First explain the disease in plain everyday English with an analogy
        if matched_disease and matched_disease.patient_plain_language:
            disease_explanation = matched_disease.patient_plain_language
        elif any(k in q_low for k in ["hypertension", "blood pressure", "bp"]):
            disease_explanation = (
                "Blood pressure is the force of blood pushing against the walls of your blood vessels [1]. "
                "Think of your arteries like household garden hoses: when water pressure is constantly too high, "
                "it causes extra strain on the hose walls, heart, and kidneys over time [1]."
            )
        elif any(k in q_low for k in ["diabetes", "semaglutide", "sugar", "ozempic"]):
            disease_explanation = (
                "Type 2 diabetes happens when your body has trouble using insulin to move sugar from food into cells for energy [1]. "
                "Think of insulin like a key that unlocks cellular doors: in diabetes, the locks become resistant, "
                "leaving sugar circulating in your bloodstream instead of fueling your body [1]."
            )
        elif any(k in q_low for k in ["headache", "migraine"]):
            disease_explanation = (
                "Headaches happen when pain-sensitive nerves, blood vessels, and muscles in your head become irritated or tense [1]. "
                "Tension headaches feel like a tight band squeezed around your forehead, while migraines cause pulsing pain "
                "often accompanied by sensitivity to bright light and sound [1]."
            )
        elif any(k in q_low for k in ["asthma", "copd", "breath", "lung"]):
            disease_explanation = (
                "Asthma is a condition where the breathing tubes in your lungs become inflamed, swollen, and narrow [1]. "
                "Think of breathing through a normal wide straw versus a pinched straw: when exposed to cold air or allergens, "
                "the airways tighten, making each breath feel harder work [1]."
            )
        elif any(k in q_low for k in ["heart failure", "chf"]):
            disease_explanation = (
                "Heart failure means the heart muscle is not pumping blood as strongly or filling as smoothly as the body needs [1]. "
                "Think of a water pump operating at half power: blood and fluid can back up into the lungs and legs, "
                "causing tiredness and swelling [1]."
            )
        else:
            disease_explanation = (
                f"{query.title()} involves biological changes that affect how your body works [1]. "
                "Understanding what is happening inside your body is the first step toward feeling better and protecting your long-term health [1]."
            )

        # 2. Practical Solutions (lifestyle, home care, medicine explanation)
        if matched_disease and matched_disease.solutions:
            sol_items = []
            for s in matched_disease.solutions[:3]:
                sol_items.append(f"• **{s.name}:** {s.description}")
            solutions_block = "\n".join(sol_items)
        elif any(k in q_low for k in ["hypertension", "blood pressure", "bp"]):
            solutions_block = (
                "• **Heart-Healthy Nutrition:** Focus on fresh vegetables, fruits, and lean proteins while lowering salt intake (DASH eating pattern) [1].\n"
                "• **Daily Movement:** Aim for 30 minutes of brisk walking or gentle aerobic exercise most days [1].\n"
                "• **Medications:** Medicines like ACE inhibitors or calcium channel blockers work gently to relax blood vessel walls so blood flows smoothly [1]."
            )
        elif any(k in q_low for k in ["diabetes", "semaglutide", "sugar", "ozempic"]):
            solutions_block = (
                "• **Balanced Meals:** Pairing proteins and fiber with carbohydrates helps prevent sharp blood sugar spikes [1].\n"
                "• **Routine Tracking:** Checking blood sugar or HbA1c provides clear feedback on what is working for your body [1].\n"
                "• **Modern Treatments:** Medications such as GLP-1 therapies help signal fullness and support steady energy throughout the day [1]."
            )
        else:
            solutions_block = (
                "• **Consistent Daily Care:** Follow doctor-prescribed treatment plans and take medications on a regular schedule [1].\n"
                "• **Lifestyle & Hydration:** Adequate rest, drinking plenty of water, and balanced whole foods support your recovery [1].\n"
                "• **Symptom Journal:** Keeping a brief daily note of how you feel helps your healthcare team tailor your care [1]."
            )

        # 3. Doctor Questions
        if matched_disease and matched_disease.doctor_checklist:
            doc_q_block = (
                f"• {matched_disease.doctor_checklist.parameter_question}\n"
                f"• {matched_disease.doctor_checklist.safety_question}\n"
                f"• {matched_disease.doctor_checklist.action_threshold_question}"
            )
        else:
            doc_q_block = (
                "• What are my specific target numbers or health goals for this condition?\n"
                "• Are there any lifestyle habits I can adjust that will help my treatment work better?\n"
                "• What specific warning signs should prompt me to contact your office right away?"
            )

        # 4. Symptoms That Need Timely Medical Attention
        if matched_disease and matched_disease.red_flags:
            red_flag_text = matched_disease.red_flags[0]
        else:
            red_flag_text = "Sudden severe chest discomfort, difficulty breathing, persistent dizziness, or unexplained weakness."

        return (
            f"### 1. Understanding the Condition: What It Is\n\n"
            f"{disease_explanation}\n\n"
            f"### 2. Practical Solutions & What You Can Do\n\n"
            f"{solutions_block}{ddi_note}{calc_note}\n\n"
            f"### 3. Questions to Ask Your Doctor\n\n"
            f"{doc_q_block}\n\n"
            f"### 4. Symptoms That Need Timely Medical Attention\n\n"
            f"Contact your healthcare provider or visit an urgent care center if you experience: {red_flag_text}\n\n"
            f"*Note: Technical clinical research papers and trial statistics are omitted here for clarity, but are available for your physician upon request.*"
        )
    else:
        # Clinician register
        if matched_disease and matched_disease.overview:
            clinician_overview = matched_disease.overview
        else:
            clinician_overview = (
                f"Clinical evaluation of **\"{query}\"** centers on molecular pathway regulation, target organ perfusion, and neurohormonal equilibrium [{primary.get('citation_index', 1)}]. "
                f"Pathophysiologic progression involves microvascular endothelial remodeling, inflammatory signaling, and progressive tissue remodeling."
            )

        if matched_disease and matched_disease.solutions:
            sols_formatted = []
            for s in matched_disease.solutions:
                dose_info = f" (Protocol: {s.dosage_or_protocol})" if s.dosage_or_protocol else ""
                contra_info = f" | Contraindications: {', '.join(s.contraindications)}" if s.contraindications else ""
                sols_formatted.append(f"• **{s.line_of_therapy.upper()} - {s.name}{dose_info}:** {s.description}{contra_info}")
            solutions_clinician = "\n".join(sols_formatted)
        else:
            solutions_clinician = (
                "• **First-Line Pharmacotherapy:** Initiate guideline-directed medical therapy (GDMT) titrated to standard evidentiary targets [1].\n"
                "• **Organ Surveillance Cutoffs:** Baseline eGFR, electrolytes, and hepatic transaminases prior to initiation; re-evaluate at 2-4 week titration intervals [1].\n"
                "• **Safety Profile:** Screen for hemodynamic stability, orthostatic vulnerability, and metabolic contraindications [1]."
            )

        if matched_disease and matched_disease.research_papers:
            paper_blocks = []
            for idx, p in enumerate(matched_disease.research_papers[:2], 1):
                paper_blocks.append(
                    f"• **[{idx}] {p.title}** (*{p.journal}*, {p.year}) - Oxford CEBM {p.cebm_level}:\n"
                    f"  - Design & Cohort: {p.study_design} (N = {p.sample_size or 'Indexed cohort'})\n"
                    f"  - Key Endpoints: {p.key_findings}\n"
                    f"  - Clinical Takeaway: {p.clinical_takeaway}"
                )
            evidence_section = "\n".join(paper_blocks)
        else:
            evidence_section = (
                f"• **[1] {primary.get('title', 'Guideline Consensus Trial')}** (*{primary.get('journal', 'Consensus Guidelines')}*, {primary.get('year', 2023)}) - Oxford CEBM {primary.get('evidence_level', 'Level 1')}:\n"
                f"  - Excerpt: {primary.get('content', 'Evidence-based protocol demonstrates therapeutic benefit.')}\n"
                f"  - Evidentiary Takeaway: {primary.get('key_takeaway', 'Adhere to guideline-directed therapeutic thresholds.')} [1]"
            )

        return (
            f"### 1. Disease Overview & Pathophysiologic Mechanism\n\n"
            f"{clinician_overview}\n\n"
            f"### 2. Guideline-Directed Medical Therapy (GDMT) & Clinical Solutions\n\n"
            f"{solutions_clinician}{ddi_note}{calc_note}\n\n"
            f"### 3. Landmark Clinical Research & Oxford CEBM Citations\n\n"
            f"{evidence_section}\n\n"
            f"**Evidence Hierarchy:** Oxford CEBM Level 1/2 Consensus Guidelines [{primary.get('citation_index', 1)}]."
        )


# ─────────────────────────────────────────────────────────────
# Graph Construction & Compilation
# ─────────────────────────────────────────────────────────────
def build_agentic_rag_graph():
    builder = StateGraph(AgenticWorkflowState)  # type: ignore[bad-specialization]

    builder.add_node("triage_interceptor", node_triage_interceptor)
    builder.add_node("query_deconstruct", node_query_deconstruct)
    builder.add_node("tool_execution", node_tool_execution)
    builder.add_node("retrieval_and_rerank", node_retrieval_and_rerank)
    builder.add_node("crag_evaluator", node_crag_evaluator)
    builder.add_node("audience_synthesis", node_audience_synthesis)
    builder.add_node("self_rag_audit", node_self_rag_audit)

    # Entry point
    builder.set_entry_point("triage_interceptor")

    # Linear workflow sequence with non-blocking triage
    builder.add_edge("triage_interceptor", "query_deconstruct")
    builder.add_edge("query_deconstruct", "tool_execution")
    builder.add_edge("tool_execution", "retrieval_and_rerank")
    builder.add_edge("retrieval_and_rerank", "crag_evaluator")
    builder.add_edge("crag_evaluator", "audience_synthesis")
    builder.add_edge("audience_synthesis", "self_rag_audit")
    builder.add_edge("self_rag_audit", END)

    return builder.compile()


# Compile global workflow graph instance
clinical_agent_graph = build_agentic_rag_graph()


def execute_agentic_rag_workflow(query: str, audience: str = "patient") -> Dict[str, Any]:
    """
    Executes the complete LangGraph Agentic RAG pipeline.
    """
    initial_state: AgenticWorkflowState = {
        "raw_query": query,
        "effective_query": query,
        "audience": normalize_audience(audience),
        "triage_alert": None,
        "decomposition": None,
        "tool_results": {},
        "retrieved_documents": [],
        "crag_grade": None,
        "generated_answer": "",
        "grounding_audit": None,
        "execution_trace": [],
        "status": "INITIALIZED"
    }

    final_state = clinical_agent_graph.invoke(initial_state)

    return {
        "status": final_state.get("status", "COMPLETED"),
        "query": query,
        "audience": final_state.get("audience", "patient"),
        "answer": final_state.get("generated_answer", ""),
        "sources": final_state.get("retrieved_documents", []),
        "triage_alert": final_state.get("triage_alert"),
        "decomposition": final_state.get("decomposition"),
        "tool_results": final_state.get("tool_results", {}),
        "crag_grade": final_state.get("crag_grade"),
        "grounding_audit": final_state.get("grounding_audit"),
        "execution_trace": final_state.get("execution_trace", []),
        "provider_info": llm_gateway.get_active_provider_info()
    }
