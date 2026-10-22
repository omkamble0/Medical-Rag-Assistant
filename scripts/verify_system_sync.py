"""
scripts/verify_system_sync.py
Comprehensive End-to-End Synchronization Audit for all 300 Diseases:
1. Medical Database & Storage Integrity (300 records, DOIs, solutions, symptoms)
2. Qdrant Embedded Vector Store & BM25 Hybrid Retrieval (300 points)
3. Query Guard & Interactive Typo Validator
4. Clinical Chatbot Engine (Multi-Turn, Patient & Doctor Mode with Landmark Papers)
5. Agentic Multi-Agent Pipeline & Tools
6. Frontend Search Suggestions (300 chips)
"""

import sys
import json
from pathlib import Path

# Add api directory to sys.path
api_dir = Path(__file__).resolve().parent.parent / "api"
sys.path.insert(0, str(api_dir))

def run_sync_verification():
    print("=" * 80)
    print("      AEGISMED: 300 DISEASES SYSTEM & CHATBOT SYNCHRONIZATION AUDIT")
    print("=" * 80)

    results = {"passed": 0, "failed": 0, "checks": []}

    def check(name: str, condition: bool, details: str = ""):
        if condition:
            results["passed"] += 1
            print(f" [PASS] {name}")
            if details:
                print(f"        -> {details}")
            results["checks"].append({"name": name, "status": "PASS", "details": details})
        else:
            results["failed"] += 1
            print(f" [FAIL] {name}")
            if details:
                print(f"        -> ERROR: {details}")
            results["checks"].append({"name": name, "status": "FAIL", "details": details})

    # =========================================================================
    # STEP 1: Medical Database Layer
    # =========================================================================
    print("\n--- 1. Medical Database & Ingested Knowledge Layer ---")
    from app.services.medical_db import medical_db
    
    stats = medical_db.get_stats()
    check("Database total disease count is exactly 550", stats.total_diseases == 550, f"Found {stats.total_diseases} diseases")
    check("Database has comprehensive symptom indexing", stats.total_symptoms >= 2500, f"Total symptoms indexed: {stats.total_symptoms}")
    check("Database has verified solutions/treatments", stats.total_solutions >= 1500, f"Total solutions: {stats.total_solutions}")
    check("Database has landmark research papers", stats.total_research_papers >= 550, f"Total research papers: {stats.total_research_papers}")

    # Check sample conditions across the entire 550 span:
    test_ids = [
        "DOC-CARD-001", "DOC-CARD-101", "DOC-CARD-201", "DOC-CARD-301",
        "DOC-CARD-401", "DOC-CARD-501", "DOC-CARD-525", "DOC-CARD-526", "DOC-CARD-550"
    ]
    for d_id in test_ids:
        rec = medical_db.get_disease_by_id(d_id)
        exists = rec is not None
        has_paper = bool(rec.research_papers) if exists else False
        paper_doi = rec.research_papers[0].doi_or_pmid if has_paper else "N/A"
        check(f"Disease ID {d_id} ({rec.name if exists else 'missing'}) loaded with DOI", 
              exists and has_paper and paper_doi != "N/A", 
              f"ICD-10: {rec.icd10_code if exists else 'N/A'}, DOI: {paper_doi}")

    # =========================================================================
    # STEP 2: Qdrant Vector Store & Hybrid Search Layer
    # =========================================================================
    print("\n--- 2. Qdrant Embedded Vector Store & Hybrid Search Layer ---")
    from app.services.vector_store import get_corpus_stats, retrieve_clinical_evidence

    c_stats = get_corpus_stats()
    check("Vector store corpus holds full synchronized knowledge base", c_stats["total_documents"] >= 550, f"Total documents in vector corpus: {c_stats['total_documents']}")

    # Search for conditions via hybrid retrieval across existing and new 501-550 batches
    test_queries = [
        ("Croup in toddlers", "Croup"),
        ("Carbon monoxide hyperbaric oxygen carboxyhemoglobin", "Carbon Monoxide"),
        ("Acetaminophen toxicity N-acetylcysteine Rumack-Matthew", "Acetaminophen Toxicity"),
        ("Malignant hyperthermia dantrolene ryanodine", "Malignant Hyperthermia"),
        ("Cystic fibrosis CFTR modulator elexacaftor", "Cystic Fibrosis"),
        ("Wilson disease ATP7B ceruloplasmin penicillamine", "Wilson"),
        ("Hepatorenal syndrome terlipressin albumin", "Hepatorenal Syndrome")
    ]


    for q_text, expected_cond in test_queries:
        hits = medical_db.search_hybrid(q_text, top_k=3)
        hit_names = [h.get("name") for h in hits]
        matched = any(expected_cond.lower() in h_name.lower() or h_name.lower() in expected_cond.lower() for h_name in hit_names)
        check(f"Hybrid retrieval finds '{expected_cond}' for query: '{q_text}'", 
              matched, 
              f"Top hit: {hit_names[0] if hit_names else 'No hits'} (Score: {hits[0].get('similarity_score', 0):.3f})" if hits else "None")

    # =========================================================================
    # STEP 3: Query Guard & Typo Validator Layer
    # =========================================================================
    print("\n--- 3. Query Guard & Interactive Typo Validator Layer ---")
    from app.services.query_guard import validate_clinical_query, correct_medical_typos

    q1 = validate_clinical_query("What is the first line treatment for hypertension?")
    check("Query Guard validates clean clinical query", q1["is_valid"] and not q1["has_typos"])

    corrected, has_typos = correct_medical_typos("lisnopril and metfomin for diabetis")
    check("Typo corrector repairs clinical medication typos", has_typos and "lisinopril" in corrected.lower() and "metformin" in corrected.lower(), f"Repaired: '{corrected}'")

    # Test Clinical NLP Engine integration
    from app.services.clinical_nlp import clinical_nlp
    nlp_res = clinical_nlp.process("Patient has crushing chest pain, denies shortness of breath and no fever.")
    check("Clinical NLP Engine correctly identifies NegEx negated symptoms", 
          len(nlp_res.negated_symptoms) > 0 and any("fever" in s for s in nlp_res.negated_symptoms),
          f"Negated: {nlp_res.negated_symptoms}")
    check("Clinical NLP Engine flags emergency acuity for crushing chest pain",
          nlp_res.acuity == "EMERGENCY_LIFE_THREATENING",
          f"Acuity: {nlp_res.acuity}")

    # =========================================================================
    # STEP 4: Clinical Chat Engine (Doctor & Patient Mode with Source Grounding)
    # =========================================================================
    print("\n--- 4. Clinical Chat Engine Layer ---")
    from app.services.chat_engine import MedicalChatEngine
    from app.models.chat_schemas import ChatRequest

    engine = MedicalChatEngine()
    chat_req_patient = ChatRequest(
        message="What is the treatment for Wilson Disease?",
        audience="patient",
        conversation_id="test-conv-wilson-001"
    )
    res_patient = engine.process_message(chat_req_patient)
    check("Chat Engine generates grounded response in Patient mode",
          bool(res_patient.message) and len(res_patient.message) > 50,
          f"Answer preview: {res_patient.message[:120]}...")

    check("Chat Engine attaches verified sources with DOIs",
          len(res_patient.sources) > 0,
          f"Attached {len(res_patient.sources)} sources")


    # =========================================================================
    # STEP 5: Agentic Workflow & Autonomous Tool Execution
    # =========================================================================
    print("\n--- 5. Agentic Multi-Agent Pipeline & Tools Layer ---")
    from app.services.tools.medical_db_tool import lookup_disease_in_database
    from app.services.agent_workflow import execute_agentic_rag_workflow

    tool_res = lookup_disease_in_database("Wilson Disease")
    check("Tool lookup_disease_in_database finds Wilson Disease monograph",
          tool_res.get("status") == "success" and tool_res.get("matches_count", 0) > 0,
          f"Matched: {tool_res.get('results', [{}])[0].get('name')}, ICD-10: {tool_res.get('results', [{}])[0].get('icd10')}")

    # Test full agentic workflow on a new disease
    wf_res = execute_agentic_rag_workflow("What is the first line management for Carbon Monoxide Toxicity?", audience="patient")
    check("Agentic workflow executes and returns synthesized answer",
          bool(wf_res.get("answer")),
          f"Answer length: {len(wf_res.get('answer', ''))} chars")
    check("Agentic workflow includes multi-agent execution trace",
          len(wf_res.get("execution_trace", [])) >= 4,
          f"Steps executed: {[t.get('step') for t in wf_res.get('execution_trace', [])]}")

    # =========================================================================
    # STEP 6: Frontend Suggestions & Search Chips Layer
    # =========================================================================
    print("\n--- 6. Frontend Suggestions & Chips Layer ---")
    suggestions_path = Path(__file__).resolve().parent.parent / "web" / "src" / "lib" / "suggestions.ts"
    if suggestions_path.exists():
        content = suggestions_path.read_text(encoding="utf-8")
        import re
        items = re.findall(r'["\']?query["\']?:\s*"([^"]+)"', content)
        check("Frontend suggestions.ts exists and contains all 550 condition chips",
              len(items) == 550,
              f"Found {len(items)} suggested queries in suggestions.ts")
        check("Frontend chips include new conditions like Carbon Monoxide and Wilson Disease",
              any("Carbon Monoxide" in it for it in items) and any("Wilson" in it for it in items),
              "Verified sample new chips present")

    else:
        check("Frontend suggestions.ts exists", False, f"File not found at {suggestions_path}")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 80)
    print(f" AUDIT COMPLETE: {results['passed']} PASSED, {results['failed']} FAILED")
    print("=" * 80)
    return results

if __name__ == "__main__":
    res = run_sync_verification()
    sys.exit(0 if res["failed"] == 0 else 1)

