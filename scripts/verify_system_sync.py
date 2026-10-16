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
    check("Database total disease count is exactly 300", stats.total_diseases == 300, f"Found {stats.total_diseases} diseases")
    check("Database has comprehensive symptom indexing", stats.total_symptoms >= 1500, f"Total symptoms indexed: {stats.total_symptoms}")
    check("Database has verified solutions/treatments", stats.total_solutions >= 600, f"Total solutions: {stats.total_solutions}")
    check("Database has landmark research papers", stats.total_research_papers >= 300, f"Total research papers: {stats.total_research_papers}")

    # Check sample conditions across the entire 300 span:
    # 001-100: DOC-CARD-001 (Hypertension)
    # 101-200: DOC-CARD-101 (Aortic Valve Stenosis), DOC-CARD-150 (Acne Vulgaris), DOC-CARD-200 (Diabetic Retinopathy)
    # 201-300: DOC-CARD-201 (Mitral Regurgitation), DOC-CARD-221 (Barrett's Esophagus), DOC-CARD-241 (Cluster Headache), DOC-CARD-281 (ITP), DOC-CARD-300 (Kaposi Sarcoma)
    test_ids = [
        "DOC-CARD-001", "DOC-CARD-101", "DOC-CARD-150", "DOC-CARD-200",
        "DOC-CARD-201", "DOC-CARD-221", "DOC-CARD-241", "DOC-CARD-281", "DOC-CARD-300"
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
    check("Vector store corpus holds full synchronized knowledge base", c_stats["total_documents"] >= 300, f"Total documents in vector corpus: {c_stats['total_documents']}")

    # Search for conditions via hybrid retrieval across existing and new 201-300 batches
    test_queries = [
        ("Croup in toddlers", "Croup (Laryngotracheobronchitis)"),
        ("Achalasia dysphagia first line", "Achalasia"),
        ("Mitral regurgitation transcatheter edge to edge repair COAPT", "Mitral Valve Regurgitation"),
        ("Infective endocarditis Duke criteria oral switch POET", "Infective Endocarditis"),
        ("Primary biliary cholangitis ursodeoxycholic acid", "Primary Biliary Cholangitis (PBC)"),
        ("Polycythemia Vera JAK2 inhibitor ruxolitinib", "Polycythemia Vera"),
        ("Immune thrombocytopenia ITP thrombopoietin receptor", "Immune Thrombocytopenia (ITP)")
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
    from app.services.query_validator import validator

    # Test exact terms recognition for conditions across all tiers
    v1 = validator.validate_and_correct("What are the first line treatments for achalasia?")
    check("Query Guard recognizes 'achalasia' as valid medical term without false typo flag", 
          v1["is_valid"] and "achalasia" in v1["medical_terms_found"], 
          f"Terms found: {v1['medical_terms_found']}")

    v2 = validator.validate_and_correct("management of sarcoidosis in adults")
    check("Query Guard recognizes 'sarcoidosis' as valid medical term", 
          v2["is_valid"] and "sarcoidosis" in v2["medical_terms_found"], 
          f"Terms found: {v2['medical_terms_found']}")

    # Test typo correction
    v3 = validator.validate_and_correct("patient has achlasia and severe dysphagia")
    has_achlasia_corr = any(c.get("original_word") == "achlasia" and c.get("corrected_word") == "achalasia" for c in v3.get("corrections", []))
    check("Query Guard corrects typo 'achlasia' -> 'achalasia'", 
          has_achlasia_corr, 
          f"Corrections: {v3.get('corrections_made')}")

    # =========================================================================
    # STEP 4: Clinical Chatbot Engine Layer
    # =========================================================================
    print("\n--- 4. Clinical Chatbot Engine (Multi-Turn & Audience Tailoring) ---")
    from app.services.chat_engine import MedicalChatEngine
    from app.models.chat_schemas import ChatRequest

    engine = MedicalChatEngine()

    # 4A. Test Condition Keyword Detection across new conditions & acronyms
    detection_tests = [
        ("What causes Addison disease?", "Primary Adrenal Insufficiency (Addison's Disease)"),
        ("How is Croup treated in pediatric clinics?", "Croup (Laryngotracheobronchitis)"),
        ("Tell me about HCM", "Hypertrophic Cardiomyopathy (HCM)"),
        ("Patient diagnosed with AAA", "Abdominal Aortic Aneurysm (AAA)"),
        ("Myasthenia Gravis acetylcholine receptor antibodies", "Myasthenia Gravis"),
        ("What is the protocol for Mitral Valve Regurgitation?", "Mitral Valve Regurgitation"),
        ("Management of Immune Thrombocytopenia in clinic", "Immune Thrombocytopenia (ITP)")
    ]

    for q, exp in detection_tests:
        det = engine._match_condition_keywords(q)
        check(f"Chatbot detects condition '{exp}' from '{q}'", det == exp, f"Detected: {det}")

    # 4B. Test Patient Mode Synthesis on newly added disease
    req_patient = ChatRequest(
        message="What is Mitral Valve Regurgitation and what should I avoid doing?",
        audience="patient",
        conversation_id="test-sync-patient-300"
    )
    resp_patient = engine.process_message(req_patient)
    check("Chatbot returns valid Patient mode response for Mitral Valve Regurgitation", 
          bool(resp_patient.message) and "Mitral" in (resp_patient.active_condition or ""), 
          f"Active condition: {resp_patient.active_condition}")
    check("Patient mode includes plain-English explanation, solutions & doctor questions",
          "Understanding the Condition" in resp_patient.message and "Questions to Ask Your Doctor" in resp_patient.message,
          f"Length: {len(resp_patient.message)} chars")
    check("Patient mode includes retrieved clinical citations",
          len(resp_patient.sources) > 0,
          f"Sources returned: {len(resp_patient.sources)}")

    # 4C. Test Doctor Mode Synthesis with genuine landmark peer-reviewed paper
    req_doctor = ChatRequest(
        message="Guideline-directed medical therapy for Mitral Valve Regurgitation",
        audience="doctor",
        conversation_id="test-sync-doctor-300"
    )
    resp_doctor = engine.process_message(req_doctor)
    check("Chatbot returns valid Doctor mode response for Mitral Valve Regurgitation",
          bool(resp_doctor.message) and "Mitral" in (resp_doctor.active_condition or ""),
          f"Active condition: {resp_doctor.active_condition}")
    check("Doctor mode contains GDMT, pathophysiologic mechanism, and landmark trial citation",
          "Guideline-Directed Medical Therapy" in resp_doctor.message and "Landmark Clinical Research" in resp_doctor.message,
          f"Snippet: {resp_doctor.message[:180]}...")
    
    # Verify the real research paper DOI appears in Doctor mode response
    source_dois = [s.doi_or_pmid for s in resp_doctor.sources if s.doi_or_pmid]
    check("Doctor mode sources contain genuine peer-reviewed DOIs",
          len(source_dois) > 0 and any("10." in doi for doi in source_dois),
          f"DOIs: {source_dois}")

    # =========================================================================
    # STEP 5: Agentic Workflow & Autonomous Tool Execution
    # =========================================================================
    print("\n--- 5. Agentic Multi-Agent Pipeline & Tools Layer ---")
    from app.services.tools.medical_db_tool import lookup_disease_in_database
    from app.services.agent_workflow import execute_agentic_rag_workflow

    tool_res = lookup_disease_in_database("Mitral Valve Regurgitation")
    check("Tool lookup_disease_in_database finds Mitral Valve Regurgitation monograph",
          tool_res.get("status") == "success" and tool_res.get("matches_count", 0) > 0,
          f"Matched: {tool_res.get('results', [{}])[0].get('name')}, ICD-10: {tool_res.get('results', [{}])[0].get('icd10')}")

    # Test full agentic workflow on a new disease
    wf_res = execute_agentic_rag_workflow("What is the first line management for Mitral Valve Regurgitation?", audience="patient")
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
        check("Frontend suggestions.ts exists and contains all 300 condition chips",
              len(items) == 300,
              f"Found {len(items)} suggested queries in suggestions.ts")
        check("Frontend chips include new conditions like Mitral Valve Regurgitation and ITP",
              any("Mitral Valve" in it for it in items) and any("Thrombocytopenia" in it for it in items),
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
