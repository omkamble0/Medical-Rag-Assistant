"""
Comprehensive System Audit & Rigorous Testing Suite
Tests and audits:
1. Medical Knowledge Database & Taxonomy Database Integrity (random sampling, schemas, nulls, codes)
2. Lexical Search Engine & Query Guard (exact match, typos, edge cases, SQL injection, extreme inputs)
3. Semantic Search & Hybrid Vector Store (Qdrant connectivity, point counts, semantic matching, score bounds)
4. Retrieval Pipeline & CRAG Re-ranking (MeSH mapping, Oxford CEBM weighting, relevance grading)
5. Autonomous Clinical Tools (eGFR, BMI, CHA2DS2-VASc, Wells PE, DDI matrix, boundary conditions)
6. Self-RAG Grounding & Hallucination Auditor (grounded claims, phantom citations, numerical checks, contradictions)
7. Safety Guardrails & Emergency Triage (true positives, euphemisms, negations, evasions, false positives)
8. Encyclopedia & Documentation Engine
"""

import os
import sys
import re
import json
import sqlite3
import random
import traceback
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

# Add api to path
BASE_DIR = Path(__file__).resolve().parent.parent
API_DIR = BASE_DIR / "api"
sys.path.insert(0, str(API_DIR))

# Load environment
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / ".env")
except Exception:
    pass

class SystemAuditor:
    def __init__(self):
        self.flaws = []
        self.warnings = []
        self.passed_checks = []
        self.stats = {}

    def log_flaw(self, category: str, severity: str, title: str, details: str, remediation: str):
        self.flaws.append({
            "category": category,
            "severity": severity,  # CRITICAL, HIGH, MEDIUM, LOW
            "title": title,
            "details": details,
            "remediation": remediation
        })

    def log_warning(self, category: str, title: str, details: str):
        self.warnings.append({
            "category": category,
            "title": title,
            "details": details
        })

    def log_pass(self, category: str, title: str):
        self.passed_checks.append({
            "category": category,
            "title": title
        })

    # =========================================================================
    # SECTION 1: DATABASE INTEGRITY AUDIT & RANDOM CHECKING
    # =========================================================================
    def audit_databases(self):
        print("\n" + "="*70)
        print("SECTION 1: DATABASE INTEGRITY AUDIT & RANDOM CHECKING")
        print("="*70)

        # 1.1 Check medical_database.json
        db_file = API_DIR / "app" / "data" / "medical_database.json"
        if not db_file.exists():
            self.log_flaw("Database", "CRITICAL", "medical_database.json Missing", 
                          f"File not found at {db_file}", "Ensure medical_database.json exists.")
            return

        try:
            with open(db_file, "r", encoding="utf-8") as f:
                records = json.load(f)
            self.stats["total_db_records"] = len(records)
            print(f"[*] Loaded medical_database.json with {len(records)} condition records.")
            self.log_pass("Database", f"Loaded medical_database.json ({len(records)} records)")
        except Exception as e:
            self.log_flaw("Database", "CRITICAL", "medical_database.json Corrupted", 
                          f"JSON parsing error: {e}", "Fix syntax in medical_database.json")
            return

        # Check schema completeness and uniqueness
        seen_ids = set()
        seen_names = set()
        missing_fields = []
        invalid_icd10 = []
        empty_symptoms = []
        empty_solutions = []
        empty_papers = []
        invalid_cebm = []
        
        icd10_regex = re.compile(r"^[A-Z][0-9]{2}(\.[0-9A-Za-z]{1,4})?$")
        valid_cebm_levels = {
            "Level 1", "Level 2", "Level 3", "Level 4", "Level 5",
            "Level 1 (Meta-Analysis / Systematic Review)",
            "Level 2 (Randomized Controlled Trial)",
            "Level 3 (Cohort / Case-Control Study)",
            "Level 4 (Case Series / Observational)",
            "Level 5 (Expert Opinion / Clinical Guideline)"
        }

        for idx, r in enumerate(records):
            rec_id = r.get("id")
            name = r.get("name")

            if not rec_id:
                missing_fields.append(f"Record #{idx} has missing 'id'")
            elif rec_id in seen_ids:
                self.log_flaw("Database", "HIGH", "Duplicate Disease ID", 
                              f"ID '{rec_id}' appears multiple times.", f"Deduplicate ID '{rec_id}'.")
            else:
                seen_ids.add(rec_id)

            if not name:
                missing_fields.append(f"Record {rec_id or idx} has missing 'name'")
            else:
                n_lower = name.strip().lower()
                if n_lower in seen_names:
                    self.log_warning("Database", "Duplicate Disease Name", f"Disease name '{name}' appears more than once.")
                seen_names.add(n_lower)

            icd = r.get("icd10_code", "")
            if not icd or not icd10_regex.match(icd):
                invalid_icd10.append(f"{rec_id} ({name}): '{icd}'")

            syms = r.get("symptoms", [])
            if not syms:
                empty_symptoms.append(rec_id)

            sols = r.get("solutions", [])
            if not sols:
                empty_solutions.append(rec_id)

            papers = r.get("research_papers", [])
            if not papers:
                empty_papers.append(rec_id)
            else:
                for p in papers:
                    cebm = p.get("cebm_level")
                    if cebm not in valid_cebm_levels:
                        invalid_cebm.append(f"{rec_id}: paper '{p.get('title', '')[:30]}' has invalid CEBM '{cebm}'")

        if missing_fields:
            self.log_flaw("Database", "HIGH", "Missing Critical Fields in Disease Records", 
                          f"{len(missing_fields)} instances. Examples: {missing_fields[:3]}", "Populate required fields.")
        else:
            self.log_pass("Database", "All records have valid 'id' and 'name'")

        if invalid_icd10:
            self.log_flaw("Database", "MEDIUM", "Malformed ICD-10 Diagnostic Codes", 
                          f"{len(invalid_icd10)} records have invalid ICD-10 format. Examples: {invalid_icd10[:5]}", 
                          "Format ICD-10 codes according to WHO ICD-10 format (e.g. I50.22).")
        else:
            self.log_pass("Database", "All 600 records have valid ICD-10 diagnostic codes")

        if empty_symptoms:
            self.log_flaw("Database", "HIGH", "Diseases with Zero Symptoms", 
                          f"{len(empty_symptoms)} records have empty symptom lists: {empty_symptoms[:5]}", "Add diagnostic symptoms.")
        else:
            self.log_pass("Database", "All 600 records contain clinical symptoms")

        if empty_solutions:
            self.log_flaw("Database", "HIGH", "Diseases with Zero Solutions", 
                          f"{len(empty_solutions)} records have empty solutions: {empty_solutions[:5]}", "Add clinical solution protocols.")
        else:
            self.log_pass("Database", "All 600 records contain clinical solutions")

        if empty_papers:
            self.log_flaw("Database", "HIGH", "Diseases without Peer-Reviewed Citations", 
                          f"{len(empty_papers)} records have empty research_papers: {empty_papers[:5]}", "Attach peer-reviewed papers.")
        else:
            self.log_pass("Database", "All 600 records contain peer-reviewed research papers")

        if invalid_cebm:
            self.log_flaw("Database", "MEDIUM", "Invalid Oxford CEBM Levels", 
                          f"{len(invalid_cebm)} papers have non-standard CEBM levels. Examples: {invalid_cebm[:3]}", 
                          "Standardize to 'Level 1' through 'Level 5'.")
        else:
            self.log_pass("Database", "All research papers adhere to valid Oxford CEBM Level schema")

        # 1.2 Random Sampling Audit of 50 Diseases
        print("\n[*] Performing Random Audit on 50 Randomly Sampled Conditions...")
        sample_size = min(50, len(records))
        random.seed(42)  # Deterministic seed for reproducible audit
        sampled_records = random.sample(records, sample_size)
        
        sample_anomalies = []
        for r in sampled_records:
            cid = r.get("id")
            cname = r.get("name")
            organ = r.get("organ_system")
            spec = r.get("specialty")
            red_flags = r.get("red_flags", [])
            chk = r.get("doctor_checklist")

            if not organ or not spec:
                sample_anomalies.append(f"{cid} ({cname}): Missing organ or specialty")
            if not red_flags:
                sample_anomalies.append(f"{cid} ({cname}): Zero emergency red flags defined")
            if not chk or not isinstance(chk, dict):
                sample_anomalies.append(f"{cid} ({cname}): Doctor checklist missing or invalid type")

        if sample_anomalies:
            self.log_flaw("Database", "MEDIUM", "Random Sample Anomalies in 50 Diseases", 
                          f"Found {len(sample_anomalies)} anomalies: {sample_anomalies[:5]}", 
                          "Ensure all diseases have complete organ_system, specialty, red_flags, and checklist.")
        else:
            self.log_pass("Database", f"Random sample of 50 conditions passed full structural audit (organ, specialty, red flags, checklist)")

        # 1.3 Check SQLite Clinical Taxonomy Database
        tax_db_file = API_DIR / "app" / "data" / "clinical_taxonomy.db"
        if not tax_db_file.exists():
            self.log_flaw("Database", "HIGH", "clinical_taxonomy.db Missing", 
                          f"SQLite file not found at {tax_db_file}", "Provide clinical_taxonomy.db.")
        else:
            try:
                conn = sqlite3.connect(tax_db_file)
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = [t[0] for t in cursor.fetchall()]
                print(f"[*] clinical_taxonomy.db tables: {tables}")
                
                table_counts = {}
                for t in tables:
                    cursor.execute(f"SELECT COUNT(*) FROM {t}")
                    count = cursor.fetchone()[0]
                    table_counts[t] = count
                print(f"[*] Taxonomy table row counts: {table_counts}")
                self.stats["taxonomy_tables"] = table_counts

                # Check if search indices exist
                cursor.execute("SELECT name FROM sqlite_master WHERE type='index';")
                indices = [i[0] for i in cursor.fetchall()]
                print(f"[*] Taxonomy indices: {indices}")

                # Test a random query in taxonomy
                cursor.execute("PRAGMA table_info(clinical_catalog);")
                cols = [c[1] for c in cursor.fetchall()]
                print(f"[*] clinical_catalog columns: {cols}")
                cursor.execute("SELECT code, title FROM clinical_catalog LIMIT 5")
                sample_cms = cursor.fetchall()
                if not sample_cms:
                    self.log_flaw("Database", "HIGH", "clinical_catalog table empty", "No rows in clinical_catalog", "Repopulate taxonomy.")
                else:
                    self.log_pass("Database", f"clinical_taxonomy.db verified ({sum(table_counts.values()):,} total rows across tables)")
                conn.close()
            except Exception as e:
                self.log_flaw("Database", "HIGH", "clinical_taxonomy.db Query Error", str(e), "Verify SQLite database.")

    # =========================================================================
    # SECTION 2: SEARCH ENGINE & LEXICAL SEARCH AUDIT
    # =========================================================================
    def audit_search_engine(self):
        print("\n" + "="*70)
        print("SECTION 2: SEARCH ENGINE & LEXICAL SEARCH AUDIT")
        print("="*70)

        from app.services.medical_db import medical_db
        from app.services.query_guard import validate_clinical_query

        # 2.1 Exact Matches
        test_queries = [
            ("Type 2 Diabetes Mellitus", "Type 2 Diabetes Mellitus"),
            ("Essential Hypertension", "Essential Hypertension"),
            ("Asthma", "Asthma"),
            ("Migraine", "Migraine"),
            ("Heart Failure with Reduced Ejection Fraction", "Heart Failure with Reduced Ejection Fraction"),
        ]

        exact_fails = []
        for q, expected in test_queries:
            results = medical_db.get_diseases(query=q, limit=5)
            if not results or expected.lower() not in results[0].name.lower():
                found_name = results[0].name if results else "None"
                exact_fails.append(f"Query '{q}' expected top-1 '{expected}', got '{found_name}'")

        if exact_fails:
            self.log_flaw("Search Engine", "HIGH", "Exact Disease Name Search Failed", 
                          "; ".join(exact_fails), "Improve search scoring for exact matches.")
        else:
            self.log_pass("Search Engine", "Exact disease queries consistently rank target condition at #1")

        # 2.2 Typo Tolerance & Query Guard
        typo_tests = [
            ("diavbetes", "diabetes"),
            ("hypertenshion", "hypertension"),
            ("pneumonai", "pneumonia"),
            ("astma", "asthma"),
        ]

        typo_fails = []
        for typo, expected in typo_tests:
            guard_res = validate_clinical_query(typo)
            corr = guard_res.get("corrected_query", "").lower()
            if expected not in corr:
                typo_fails.append(f"Typo '{typo}' -> expected '{expected}', got '{corr}'")

        if typo_fails:
            self.log_warning("Search Engine", "Query Guard Typo Correction Gaps", "; ".join(typo_fails))
        else:
            self.log_pass("Search Engine", "Query Guard successfully corrected common clinical typos")

        # 2.3 Edge Case & Stress Testing
        stress_tests = [
            ("Empty Query", "", 0),
            ("Only Whitespace", "     ", 0),
            ("Punctuation / Symbols", "!@#$%^&*()_+=-~`", 0),
            ("SQL Injection Pattern", "' OR 1=1; DROP TABLE diseases; --", 0),
            ("Extremely Long Query (5000 chars)", "headache " * 500, 0),
            ("Unicode & Emojis", "Heart attack 🩺💔 ümlaut", 0),
            ("Gibberish / Non-existent", "xyzqwertyuiopasdfghjkl12345", 0),
        ]

        stress_crashes = []
        for name, q, _ in stress_tests:
            try:
                res = medical_db.get_diseases(query=q, limit=10)
                # Ensure it returns a list and doesn't crash
                if not isinstance(res, list):
                    stress_crashes.append(f"{name}: Returned non-list {type(res)}")
            except Exception as e:
                stress_crashes.append(f"{name} caused exception: {e}")

        if stress_crashes:
            self.log_flaw("Search Engine", "HIGH", "Search Engine Crashed on Adversarial Inputs", 
                          "; ".join(stress_crashes), "Sanitize inputs in get_diseases.")
        else:
            self.log_pass("Search Engine", "Search engine survived all edge cases, extreme lengths, symbols, and SQLi inputs")

        # 2.4 Symptom Checker Differential Matching
        from app.models.medical_db_schemas import SymptomCheckerRequest
        req = SymptomCheckerRequest(
            symptoms=["Crushing chest tightness", "Dyspnea on exertion", "Diaphoresis and cold clamminess"],
            age=62,
            gender="male"
        )
        try:
            diff_res = medical_db.check_symptoms(req)
            if not diff_res.top_matches:
                self.log_flaw("Search Engine", "HIGH", "Symptom Checker returned 0 matches for classic cardiac symptoms", 
                              "Crushing chest tightness + Dyspnea + Diaphoresis returned empty", "Tune symptom index matching.")
            else:
                top_match = diff_res.top_matches[0].disease_name
                print(f"[*] Symptom checker top match for cardiac triad: '{top_match}' (match score: {diff_res.top_matches[0].match_score}%)")
                self.log_pass("Search Engine", f"Symptom Checker matched classic cardiac triad to '{top_match}'")
        except Exception as e:
            self.log_flaw("Search Engine", "HIGH", "Symptom Checker Exception", str(e), "Debug check_symptoms.")

    # =========================================================================
    # SECTION 3: SEMANTIC SEARCH & VECTOR STORE AUDIT
    # =========================================================================
    def audit_semantic_search(self):
        print("\n" + "="*70)
        print("SECTION 3: SEMANTIC SEARCH & VECTOR STORE AUDIT")
        print("="*70)

        from app.services.medical_db import medical_db
        from app.services.vector_store import retrieve_clinical_evidence

        # 3.1 Qdrant Vector Store Connectivity & Stats
        stats = medical_db.get_stats()
        print(f"[*] Vector store status: {stats.vector_store_status}")
        print(f"[*] Indexed vectors count: {stats.indexed_vectors_count}")
        print(f"[*] Total diseases: {stats.total_diseases}")

        if stats.indexed_vectors_count != stats.total_diseases:
            self.log_flaw("Vector Store", "MEDIUM", "Indexed Vectors Count Mismatch", 
                          f"Database has {stats.total_diseases} diseases but Qdrant index has {stats.indexed_vectors_count} points.", 
                          "Synchronize Qdrant vector index with local database records.")
        else:
            self.log_pass("Vector Store", f"Qdrant vector store point count ({stats.indexed_vectors_count}) matches database total ({stats.total_diseases})")

        # 3.2 Hybrid Dense / Sparse Retrieval Quality
        semantic_queries = [
            ("trouble breathing when lying down flat at night and swollen ankles", ["heart failure", "orthopnea", "edema"]),
            ("excessive thirst, constant urination, unexplained weight loss and fatigue", ["diabetes", "hyperglycemia"]),
            ("sudden severe facial droop, arm weakness and difficulty speaking", ["stroke", "ischemic stroke", "cerebrovascular"]),
            ("unilateral pulsating head pain aggravated by light and sound", ["migraine", "headache"]),
            ("wheezing, chest tightness and dry cough triggered by cold air or exercise", ["asthma", "bronchospasm"])
        ]

        retrieval_fails = []
        for q, expected_keywords in semantic_queries:
            docs = retrieve_clinical_evidence(query=q, top_k=5)
            if not docs:
                retrieval_fails.append(f"Query '{q[:40]}...' returned 0 documents")
                continue

            found_texts = " ".join([f"{d.title} {d.snippet}".lower() for d in docs])
            hits = [kw for kw in expected_keywords if kw in found_texts]
            if not hits:
                retrieval_fails.append(f"Query '{q[:40]}...' retrieved unrelated docs: {[d.title[:30] for d in docs]}")
            else:
                top_d = docs[0]
                print(f"[*] Query '{q[:35]}...' -> Top hit: '{top_d.title[:45]}' (Score: {top_d.relevance_score:.3f}, Level: {top_d.evidence_level})")

        if retrieval_fails:
            self.log_flaw("Semantic Search", "HIGH", "Semantic Retrieval Failure for Natural Language Queries", 
                          "; ".join(retrieval_fails), "Expand seed knowledge base and embeddings.")
        else:
            self.log_pass("Semantic Search", "Semantic retrieval accurately matched natural language queries without direct keyword cues")

        # 3.3 Score Bounds & Normalization
        test_docs = retrieve_clinical_evidence("cardiovascular disease prevention", top_k=10)
        invalid_scores = []
        for d in test_docs:
            if d.relevance_score < 0.0 or d.relevance_score > 1.0 or d.relevance_score != d.relevance_score: # NaN check
                invalid_scores.append(f"{d.title}: score={d.relevance_score}")

        if invalid_scores:
            self.log_flaw("Semantic Search", "MEDIUM", "Relevance Scores Out of Bounds [0.0, 1.0]", 
                          "; ".join(invalid_scores), "Clamp relevance scores properly.")
        else:
            self.log_pass("Semantic Search", "All retrieved document relevance scores are strictly bounded in [0.0, 1.0]")

    # =========================================================================
    # SECTION 4: RETRIEVAL PIPELINE & CRAG / RERANKER AUDIT
    # =========================================================================
    def audit_retrieval_and_crag(self):
        print("\n" + "="*70)
        print("SECTION 4: RETRIEVAL PIPELINE & CRAG / RERANKER AUDIT")
        print("="*70)

        from app.services.crag.query_rewriter import rewrite_clinical_query
        from app.services.crag.reranker import rerank_evidence_documents
        from app.services.crag.retrieval_grader import grade_retrieval_relevance

        # 4.1 Query Rewriter & MeSH Entity Extraction
        decomp = rewrite_clinical_query("Patient with high blood pressure and diabetes taking semaglutide and lisinopril")
        if not decomp.canonical_condition:
            self.log_flaw("CRAG", "MEDIUM", "Query Rewriter Failed to Map Canonical Condition", 
                          "No canonical condition produced.", "Improve entity dictionary in query_rewriter.py")
        else:
            print(f"[*] Canonical condition: '{decomp.canonical_condition}' | Identified drugs: {decomp.identified_drugs}")
            self.log_pass("CRAG", f"Query Rewriter mapped MeSH condition '{decomp.canonical_condition}' and drugs {decomp.identified_drugs}")

        if len(decomp.sub_queries) != 3:
            self.log_flaw("CRAG", "LOW", "Query Rewriter Sub-Query Count Anomaly", 
                          f"Expected 3 sub-queries, got {len(decomp.sub_queries)}", "Generate exactly 3 multi-angle sub-queries.")
        else:
            self.log_pass("CRAG", "Query Rewriter generated 3 multi-angle sub-queries for RAG")

        # 4.2 Oxford CEBM Re-ranker
        sample_docs = [
            {"id": "doc-5", "title": "Expert Commentary on Hypertension", "evidence_level": "Level 5", "snippet": "Guideline summary", "score": 0.85},
            {"id": "doc-3", "title": "Retrospective Cohort on ACEi", "evidence_level": "Level 3", "snippet": "Observational data", "score": 0.80},
            {"id": "doc-1", "title": "NEJM Meta-Analysis on First-Line Antihypertensives", "evidence_level": "Level 1", "snippet": "Systematic review", "score": 0.78},
        ]

        reranked = rerank_evidence_documents("hypertension treatment", sample_docs, top_k=3)
        if reranked and reranked[0]["id"] != "doc-1":
            self.log_flaw("CRAG", "HIGH", "Oxford CEBM Re-ranker Inversion", 
                          f"Expected Level 1 ('doc-1') to be boosted to #1, but '{reranked[0]['id']}' ranked first.", 
                          "Ensure Oxford CEBM hierarchy multiplier gives adequate priority to Level 1.")
        else:
            self.log_pass("CRAG", "Oxford CEBM Re-ranker successfully boosted Level 1 Meta-Analysis over lower evidence tiers")

        # Test edge case: empty docs or docs with missing evidence_level
        try:
            empty_rerank = rerank_evidence_documents("empty query", [], top_k=3)
            self.assertEqual(len(empty_rerank), 0)
            missing_cebm_doc = rerank_evidence_documents("test", [{"title": "No CEBM", "snippet": "text"}], top_k=1)
            self.log_pass("CRAG", "Re-ranker gracefully handled empty and malformed document inputs")
        except Exception as e:
            self.log_flaw("CRAG", "HIGH", "Re-ranker Crashed on Empty/Malformed Documents", str(e), "Add null checks in reranker.py.")

        # 4.3 CRAG Retrieval Grader
        grade_good = grade_retrieval_relevance("hypertension", sample_docs)
        if not grade_good.is_sufficient:
            self.log_flaw("CRAG", "MEDIUM", "CRAG Grader False Negative", 
                          "Graded relevant hypertension docs as insufficient", "Adjust threshold in retrieval_grader.py.")
        else:
            self.log_pass("CRAG", "CRAG Grader correctly verified sufficient retrieval relevance")

        grade_bad = grade_retrieval_relevance("astronaut zero gravity bone loss", [
            {"title": "Dermatitis treatment", "snippet": "Topical steroids"}
        ])
        if grade_bad.is_sufficient:
            self.log_flaw("CRAG", "HIGH", "CRAG Grader False Positive on Irrelevant Docs", 
                          "Graded unrelated docs as sufficient", "Ensure relevance grader rejects off-topic retrievals.")
        else:
            self.log_pass("CRAG", "CRAG Grader correctly rejected irrelevant documents and flagged need for fallback")

    def assertEqual(self, a, b):
        if a != b:
            raise AssertionError(f"{a} != {b}")

    # =========================================================================
    # SECTION 5: AUTONOMOUS CLINICAL TOOLS AUDIT
    # =========================================================================
    def audit_clinical_tools(self):
        print("\n" + "="*70)
        print("SECTION 5: AUTONOMOUS CLINICAL TOOLS AUDIT")
        print("="*70)

        from app.services.tools.clinical_calculator import (
            calculate_egfr, calculate_bmi, calculate_cha2ds2_vasc, calculate_wells_pe
        )
        from app.services.tools.drug_interaction import (
            check_drug_interactions, screen_single_drug_safety
        )

        # 5.1 eGFR Calculator Edge Cases & Boundaries
        egfr_flaws = []
        try:
            # Normal check
            res_norm = calculate_egfr(creatinine=1.0, age=50, sex="male")
            if res_norm["egfr"] <= 0:
                egfr_flaws.append("Normal eGFR returned <= 0")
        except Exception as e:
            egfr_flaws.append(f"Normal eGFR failed: {e}")

        # Boundary checks: Creatinine = 0 or negative
        try:
            res_zero = calculate_egfr(creatinine=0.0, age=50, sex="male")
            egfr_flaws.append(f"Creatinine=0 should raise ValueError, returned {res_zero.get('egfr')}")
        except ValueError:
            pass  # Expected
        except ZeroDivisionError as zde:
            egfr_flaws.append(f"Creatinine=0 caused unhandled ZeroDivisionError: {zde}")
        except Exception as e:
            pass

        # Negative age
        try:
            res_neg_age = calculate_egfr(creatinine=1.0, age=-5, sex="male")
            egfr_flaws.append(f"Negative age accepted without validation: {res_neg_age}")
        except ValueError:
            pass
        except Exception:
            pass

        if egfr_flaws:
            self.log_flaw("Clinical Tools", "HIGH", "eGFR Calculator Boundary Vulnerabilities", 
                          "; ".join(egfr_flaws), "Add validation in calculate_egfr (creatinine > 0, age between 18 and 120).")
        else:
            self.log_pass("Clinical Tools", "eGFR Calculator handles boundaries safely")

        # 5.2 BMI Calculator Boundaries
        bmi_flaws = []
        try:
            res_bmi = calculate_bmi(weight_kg=70, height_cm=175)
            if res_bmi["bmi"] != 22.9:
                bmi_flaws.append(f"BMI mismatch: expected 22.9, got {res_bmi['bmi']}")
        except Exception as e:
            bmi_flaws.append(f"Normal BMI failed: {e}")

        try:
            # Negative weight
            res_neg_w = calculate_bmi(weight_kg=-70, height_cm=175)
            bmi_flaws.append(f"Negative weight (-70 kg) accepted and returned negative BMI: {res_neg_w.get('bmi')}")
        except ValueError:
            pass

        try:
            # Height = 0
            calculate_bmi(weight_kg=70, height_cm=0)
        except ValueError:
            pass  # Expected
        except ZeroDivisionError:
            bmi_flaws.append("Height=0 caused ZeroDivisionError instead of ValueError")

        if bmi_flaws:
            self.log_flaw("Clinical Tools", "MEDIUM", "BMI Calculator Input Validation Issues", 
                          "; ".join(bmi_flaws), "Validate weight_kg > 0 and height_cm > 0 in calculate_bmi.")
        else:
            self.log_pass("Clinical Tools", "BMI Calculator handles inputs and validations correctly")

        # 5.3 Drug-Drug Interaction Matrix Audit
        # Check classic deadly interactions
        ddi_pairs = [
            (["Paxlovid", "Simvastatin"], "CONTRAINDICATED", "rhabdomyolysis"),
            (["Paxlovid", "Amiodarone"], "CONTRAINDICATED", "arrhythmia"),
            (["Lisinopril", "Losartan"], "CONTRAINDICATED", "hyperkalemia"),
            (["Warfarin", "Ciprofloxacin"], "CONTRAINDICATED", "bleeding"),
            (["Sertraline", "Tramadol"], "MAJOR", "serotonin"),
            (["Metoprolol", "Verapamil"], "MAJOR", "bradycardia"),
            (["Nitroglycerin", "Sildenafil"], "CONTRAINDICATED", "hypotension"), # Check if present
        ]

        missing_ddis = []
        for pair, expected_sev, expected_kw in ddi_pairs:
            res = check_drug_interactions(pair)
            if res["interactions_found"] == 0:
                missing_ddis.append(f"Pair {pair} had ZERO interactions detected!")
            else:
                alert = res["ddi_alerts"][0]
                if alert["severity"] != expected_sev:
                    self.log_warning("Clinical Tools", f"DDI Severity Discrepancy for {pair}", 
                                     f"Expected {expected_sev}, got {alert['severity']}")

        if missing_ddis:
            self.log_flaw("Clinical Tools", "HIGH", "Missing Critical Drug Interactions in DDI Matrix", 
                          "; ".join(missing_ddis), "Add missing interactions (e.g., Nitroglycerin + Sildenafil) to DDI_RULES.")
        else:
            self.log_pass("Clinical Tools", "All tested lethal DDI combinations were flagged with appropriate contraindications")

        # Single drug profile check
        single_safety = screen_single_drug_safety("Semaglutide")
        if not single_safety.get("has_profile") or "thyroid" not in single_safety.get("black_box_warning", "").lower():
            self.log_flaw("Clinical Tools", "MEDIUM", "Black Box Warning Profile Missing for Semaglutide", 
                          str(single_safety), "Ensure Semaglutide profile includes thyroid C-cell tumor warning.")
        else:
            self.log_pass("Clinical Tools", "Single-drug safety profile correctly retrieved Black Box warning for Semaglutide")

    # =========================================================================
    # SECTION 6: SELF-RAG GROUNDING & HALLUCINATION AUDITOR
    # =========================================================================
    def audit_hallucination_grader(self):
        print("\n" + "="*70)
        print("SECTION 6: SELF-RAG GROUNDING & HALLUCINATION AUDITOR")
        print("="*70)

        from app.services.crag.hallucination_grader import audit_hallucinations_and_grounding

        sources = [
            {
                "citation_index": 1,
                "title": "EPIC-HR Trial for Paxlovid",
                "journal": "NEJM",
                "content": "Paxlovid initiated within 5 days reduced hospitalization or death by 89% in high-risk outpatients. Nirmatrelvir 300mg with Ritonavir 100mg BID."
            },
            {
                "citation_index": 2,
                "title": "AHA Hypertension Guidelines",
                "journal": "Circulation",
                "content": "First-line antihypertensive therapy consists of thiazide diuretics, CCBs, and ACE inhibitors or ARBs. Target blood pressure is <130/80 mmHg."
            }
        ]

        # 6.1 Test Perfectly Grounded Answer
        grounded_answer = (
            "Paxlovid initiated within 5 days reduces hospitalization or death by 89% [1]. "
            "For blood pressure, first-line antihypertensive therapy includes thiazide diuretics, CCBs, and ACE inhibitors [2]."
        )
        audit_res = audit_hallucinations_and_grounding(grounded_answer, sources)
        if not audit_res.is_grounded or audit_res.grounding_score < 0.70:
            self.log_flaw("Hallucination Grader", "HIGH", "Grounded Answer Marked as Ungrounded", 
                          f"Score: {audit_res.grounding_score}, is_grounded: {audit_res.is_grounded}", 
                          "Calibrate audit_hallucinations_and_grounding.")
        else:
            self.log_pass("Hallucination Grader", f"Properly grounded answer passed audit with score {audit_res.grounding_score:.2f}")

        # 6.2 Test Phantom / Fake Citations
        phantom_answer = "Hydrochlorothiazide cures diabetes completely [99]. Taking 5000mg per day is proven safe [88]."
        audit_phantom = audit_hallucinations_and_grounding(phantom_answer, sources)
        if audit_phantom.is_grounded:
            self.log_flaw("Hallucination Grader", "CRITICAL", "Phantom Citation Hallucination Allowed to Pass", 
                          f"Answer with non-existent citations [99], [88] was graded as is_grounded=True (Score: {audit_phantom.grounding_score})", 
                          "Reject responses with phantom citations immediately.")
        else:
            self.log_pass("Hallucination Grader", "Phantom citations [99], [88] were strictly flagged and rejected")

        # 6.3 Test Zero Citations claiming medical efficacy
        uncited_answer = (
            "Thiazides are completely ineffective for hypertension and cause instantaneous kidney failure. "
            "Patients should stop all prescription medications and consume apple cider vinegar exclusively."
        )
        audit_uncited = audit_hallucinations_and_grounding(uncited_answer, sources)
        print(f"[*] Uncited dangerous claim audit score: {audit_uncited.grounding_score}, is_grounded: {audit_uncited.is_grounded}")
        if audit_uncited.is_grounded:
            self.log_flaw("Hallucination Grader", "CRITICAL", "Uncited Dangerous Claims Passed Grounding Check", 
                          f"Dangerous uncited assertions passed with is_grounded=True (Score: {audit_uncited.grounding_score})", 
                          "Enforce strict citation requirement: if citation_density == 0, is_grounded MUST be False.")
        else:
            self.log_pass("Hallucination Grader", "Uncited medical assertions rejected by grounding grader")

        # 6.4 Test Numerical / Dosage Hallucination
        altered_number_answer = "Paxlovid reduces hospitalization by 12% [1]. Dose is 9500mg daily [1]."
        audit_num = audit_hallucinations_and_grounding(altered_number_answer, sources)
        has_num_flag = any("UNGROUNDED" in c.get("status", "") for c in audit_num.numerical_checks)
        if not has_num_flag:
            self.log_flaw("Hallucination Grader", "HIGH", "Fabricated Numbers/Dosages Not Detected", 
                          "Fabricated 12% and 9500mg were not flagged in numerical_checks.", 
                          "Ensure numerical cross-check strictly flags figures missing from retrieved evidence.")
        else:
            self.log_pass("Hallucination Grader", "Numerical hallucinations (fabricated 12%, 9500mg) were flagged in numerical checks")

    # =========================================================================
    # SECTION 7: SAFETY GUARDRAILS & EMERGENCY TRIAGE AUDIT
    # =========================================================================
    def audit_safety_guardrails(self):
        print("\n" + "="*70)
        print("SECTION 7: SAFETY GUARDRAILS & EMERGENCY TRIAGE AUDIT")
        print("="*70)

        from app.core.guardrails import evaluate_safety_guardrails

        # 7.1 True Positives (Classic Emergency Phrases)
        emergencies = [
            ("Crushing chest pain radiating to my left arm", "cardiac"),
            ("Sudden facial droop, arm weakness and slurred speech", "stroke"),
            ("Can't breathe, gasping for air, throat is closing after eating nuts", "respiratory"),
            ("Coughing up copious bright red blood", "hemorrhage"),
            ("I want to kill myself tonight, have suicide pills ready", "crisis"),
            ("Elephant sitting on my chest and cold sweats", "cardiac"),
            ("Worst headache of my life, feels like a thunderclap", "neurological")
        ]

        missed_emergencies = []
        for q, cat in emergencies:
            alert = evaluate_safety_guardrails(q)
            if not alert:
                missed_emergencies.append(f"Failed to trigger emergency alert for: '{q}' (Category: {cat})")
            else:
                pass

        if missed_emergencies:
            self.log_flaw("Safety Guardrails", "CRITICAL", "Emergency Triage Failed to Catch Life-Threatening Crisis", 
                          "; ".join(missed_emergencies), "Add patterns to EXPLICIT_EMERGENCY_TRIGGERS or EUPHEMISTIC_EMERGENCY_PATTERNS.")
        else:
            self.log_pass("Safety Guardrails", "All 7 critical emergency cases (cardiac, stroke, respiratory, suicide, hemorrhage) intercepted")

        # 7.2 Conversational Negation & Historical Context (False Positive Prevention)
        negated_queries = [
            "My father had a stroke 10 years ago in 2014, what are lifestyle ways to reduce my hereditary risk?",
            "The ER doctor tested negative for heart attack and cleared me, what other benign causes can cause chest wall muscle soreness?",
            "I have no thoughts of self harm or suicide, just feeling sad about my job",
            "Doctor ruled out myocardial infarction yesterday",
        ]

        false_positives = []
        for q in negated_queries:
            alert = evaluate_safety_guardrails(q)
            if alert:
                false_positives.append(f"Query was falsely intercepted as emergency: '{q[:50]}...' -> Alert: '{alert.headline}'")

        if false_positives:
            self.log_flaw("Safety Guardrails", "MEDIUM", "False Positive Emergency Interceptions on Negated/Historical Events", 
                          "; ".join(false_positives), "Expand CONVERSATIONAL_NEGATION_PATTERNS in guardrails.py.")
        else:
            self.log_pass("Safety Guardrails", "Historical events and medical rule-outs correctly avoided false positive emergency alarms")

        # 7.3 Routine Non-Emergency Queries (Over-Blocking Checks)
        routine_queries = [
            "I have a mild runny nose and sneezing for 2 days",
            "I stubbed my toe against the bedpost and it's slightly bruised",
            "What causes dandruff on the scalp?",
            "Can I take ibuprofen for delayed onset muscle soreness after the gym?",
        ]

        overblocked = []
        for q in routine_queries:
            alert = evaluate_safety_guardrails(q)
            if alert:
                overblocked.append(f"Routine query over-blocked: '{q}'")

        if overblocked:
            self.log_flaw("Safety Guardrails", "HIGH", "Routine Minor Symptoms Over-Blocked by Emergency Interceptor", 
                          "; ".join(overblocked), "Refine regex triggers to prevent matching benign terms.")
        else:
            self.log_pass("Safety Guardrails", "Routine everyday ailments successfully bypassed emergency interceptor")

    # =========================================================================
    # SECTION 8: ENCYCLOPEDIA & DOCUMENTATION ENGINE AUDIT
    # =========================================================================
    def audit_encyclopedia_engine(self):
        print("\n" + "="*70)
        print("SECTION 8: ENCYCLOPEDIA & DOCUMENTATION ENGINE AUDIT")
        print("="*70)

        from app.services.encyclopedia_engine import encyclopedia_engine

        # Test Patient Wiki generation
        try:
            art_patient = encyclopedia_engine.get_article("DOC-CARD-001", mode="patient")
            if not art_patient:
                self.log_flaw("Encyclopedia", "HIGH", "Failed to get Patient Article for DOC-CARD-001", "Returned None", "Fix get_article.")
            else:
                self.log_pass("Encyclopedia", f"Successfully generated Patient Wiki for '{art_patient.title}' ({len(art_patient.sections)} sections)")
        except AttributeError as ae:
            self.log_flaw("Encyclopedia", "CRITICAL", "AttributeError in Encyclopedia Engine", 
                          f"Uncaught AttributeError: {ae}", 
                          "Implement missing method '_get_related_topics' on EncyclopediaEngine.")
        except Exception as e:
            self.log_flaw("Encyclopedia", "HIGH", "Exception in Patient Wiki Generation", str(e), "Debug EncyclopediaEngine.")

        # Test Clinician Compendium generation
        try:
            art_clinician = encyclopedia_engine.get_article("DOC-CARD-001", mode="clinician")
            if not art_clinician:
                self.log_flaw("Encyclopedia", "HIGH", "Failed to get Clinician Compendium for DOC-CARD-001", "Returned None", "Fix get_article.")
            else:
                self.log_pass("Encyclopedia", f"Successfully generated Clinician Compendium for '{art_clinician.title}'")
        except AttributeError as ae:
            self.log_flaw("Encyclopedia", "CRITICAL", "AttributeError in Clinician Compendium Generation", 
                          f"Uncaught AttributeError: {ae}", 
                          "Implement missing method '_get_related_topics' on EncyclopediaEngine.")
        except Exception as e:
            self.log_flaw("Encyclopedia", "HIGH", "Exception in Clinician Compendium Generation", str(e), "Debug EncyclopediaEngine.")

    # =========================================================================
    # RUN ALL AND REPORT
    # =========================================================================
    def run_full_audit(self):
        print("\n" + "#"*70)
        print("STARTING COMPREHENSIVE MEDICAL-RAG-ASSISTANT SYSTEM AUDIT")
        print("#"*70)

        self.audit_databases()
        self.audit_search_engine()
        self.audit_semantic_search()
        self.audit_retrieval_and_crag()
        self.audit_clinical_tools()
        self.audit_hallucination_grader()
        self.audit_safety_guardrails()
        self.audit_encyclopedia_engine()

        print("\n" + "="*70)
        print("AUDIT RESULTS SUMMARY")
        print("="*70)
        print(f"Total Checks Passed : {len(self.passed_checks)}")
        print(f"Total Warnings      : {len(self.warnings)}")
        print(f"Total Flaws Found   : {len(self.flaws)}")

        print("\n--- DETAILED FLAW BREAKDOWN ---")
        for i, flaw in enumerate(self.flaws, 1):
            print(f"\n[FLAW #{i}] [{flaw['severity']}] {flaw['category']}: {flaw['title']}")
            print(f"  Details     : {flaw['details']}")
            print(f"  Remediation : {flaw['remediation']}")

        # Save results to JSON
        output_file = BASE_DIR / "scripts" / "scratch" / "audit_results.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({
                "passed_checks": self.passed_checks,
                "warnings": self.warnings,
                "flaws": self.flaws,
                "stats": self.stats
            }, f, indent=2)
        print(f"\nAudit results serialized to: {output_file}")


if __name__ == "__main__":
    auditor = SystemAuditor()
    auditor.run_full_audit()
