# Medical-Rag-Assistant 🩺

An evidence-based **Agentic Medical RAG Assistant** featuring real-time query validation (typo correction), vector evidence retrieval, audience-aware answer generation (Patient vs. Clinician modes), and Oxford CEBM grounding.

---## 🏗️ Architecture Pipeline (LangGraph & CRAG / Self-RAG)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USER QUERY ("Can I take Paxlovid with simvastatin?")     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. NODE 1: SAFETY & EMERGENCY TRIAGE INTERCEPTOR            │
│    - Tier-1 deterministic guardrail (MI, Stroke, Airway)    │
│    - Halts on red-flags with emergency dispatch advice      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. NODE 2: QUERY DECONSTRUCTION & MeSH MAPPING              │
│    - Deconstructs query into clinical entities & MeSH terms │
│    - Generates 3 multi-angle sub-queries for RAG            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. NODE 3: AUTONOMOUS CLINICAL TOOL EXECUTION               │
│    - Drug-Drug Interaction (DDI) Screener & Black Box sweep │
│    - Clinical Risk Calculators (2021 CKD-EPI eGFR, BMI,     │
│      CHA2DS2-VASc, Wells PE Criteria)                       │
│    - Live NCBI PubMed & Consensus Guideline Fetcher         │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. NODE 4: VECTOR RETRIEVAL & OXFORD CEBM RE-RANKING        │
│    - Multi-query vector retrieval with Reciprocal Rank      │
│      Fusion (RRF) & Oxford CEBM multipliers (Level 1 boost) │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. NODE 5: CORRECTIVE RAG (CRAG) RELEVANCE GRADER           │
│    - Evaluates retrieval relevance & missing clinical aspects│
│    - Triggers supplemental PubMed / web fallback if needed  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. NODE 6: MULTI-PROVIDER AUDIENCE-AWARE SYNTHESIS          │
│    - Hybrid Gateway: OpenAI (GPT-4o), Groq (Llama 3.3),     │
│      Gemini, Ollama (Local Private LLM), or Local Engine    │
│    - Patient Mode (Grade 6-8, plain English, analogies)     │
│    - Clinician Mode (Oxford CEBM, endpoints, DDI, organ cutoffs)
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 8. NODE 7: SELF-RAG GROUNDING & HALLUCINATION AUDIT         │
│    - Reflective audit cross-referencing citations [1], [2]  │
│    - Computes Grounding Score & Hallucination Risk %        │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
Medical-Rag-Assistant/
├── api/
│   ├── app/
│   │   ├── core/
│   │   │   ├── prompts.py            # PATIENT & CLINICIAN prompt routing
│   │   │   ├── guardrails.py         # Deterministic Tier-1 safety guardrails
│   │   │   ├── query_parser.py       # Clinical entity extraction
│   │   │   └── evaluator.py          # Grounding & confidence evaluation
│   │   ├── services/
│   │   │   ├── agent_workflow.py     # LangGraph 7-stage state graph workflow
│   │   │   ├── llm_gateway.py        # OpenAI / Groq / Gemini / Ollama / Local gateway
│   │   │   ├── medical_db.py         # 100+ Disease, Symptom & Solution Knowledge DB + Qdrant
│   │   │   ├── rag_engine.py         # Evidence-based clinical RAG engine
│   │   │   ├── query_guard.py        # Typo correction & validation gate
│   │   │   ├── vector_store.py       # Vector evidence retrieval
│   │   │   ├── crag/                 # Corrective & Self-Reflective RAG (CRAG & Self-RAG)
│   │   │   │   ├── query_rewriter.py # MeSH mapping & sub-query generation
│   │   │   │   ├── retrieval_grader.py# CRAG relevance evaluation & fallback
│   │   │   │   ├── reranker.py       # Oxford CEBM hierarchy re-ranker
│   │   │   │   └── hallucination_grader.py # Self-RAG hallucination & grounding auditor
│   │   │   └── tools/                # Autonomous Clinical Tools (LangChain @tool)
│   │   │       ├── clinical_calculator.py # 2021 CKD-EPI eGFR, BMI, CHA2DS2, Wells PE
│   │   │       ├── drug_interaction.py    # DDI screener & Black Box warnings
│   │   │       ├── medical_db_tool.py     # Disease & Symptom Differential Diagnostic Tool
│   │   │       ├── pubmed_tool.py         # Live NCBI PubMed & clinical trial repository
│   │   │       └── guideline_tool.py      # WHO, AHA, ADA, GINA, NICE guidelines
│   │   ├── routes/
│   │   │   ├── agentic_pipeline.py   # /api/v1/agentic endpoints & tool APIs
│   │   │   ├── medical_database.py   # /api/v1/database endpoints & symptom checker
│   │   │   ├── medical_query.py      # /api/v1/medical-query with agent trace
│   │   │   └── validate.py           # Typo validation endpoints
│   │   ├── models/
│   │   │   ├── enums.py              # UserMode, EvidenceLevel
│   │   │   ├── medical_db_schemas.py # Disease, Symptom, Solution & Paper schemas
│   │   │   └── schemas.py            # Pydantic request/response schemas
│   │   └── main.py                   # FastAPI application
│   ├── requirements.txt
│   └── .env.example
├── web/
│   ├── src/
│   │   ├── app/                      # Next.js App router
│   │   ├── components/               # MedicalDatabaseExplorer, ClinicalCalculatorWidget, etc.
│   │   ├── hooks/                    # useMedicalQuery, useQueryValidator
│   │   └── lib/                      # API client, types, suggestions
│   ├── package.json
│   └── tsconfig.json
├── tests/
│   ├── test_agentic_workflow.py      # LangGraph workflow, tools, CRAG & Self-RAG tests
│   ├── test_rag_engine.py            # RAG and Query Guard unit tests
│   └── test_prompts.py               # Prompt routing tests
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Node.js 18+
- Python 3.10+

### 2. Install Dependencies
```bash
npm run install:all
```

### 3. Run Development Stack
```bash
# Starts both FastAPI Backend (port 8000) and Next.js Frontend (port 3000)
npm run dev
```

- **Frontend UI**: [http://localhost:3000](http://localhost:3000)
- **FastAPI Interactive Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## 🛡️ Key GenAI & Clinical Features

- **Integrated Conversational Clinical Chatbot**:
  - Embedded directly into the central report flow with stateful multi-turn dialogue memory.
  - Contextual "Ask More Details / Suggested Follow-up Questions" quick chips tailored to patient vs. doctor registers.
  - Retains the exact active disease topic throughout conversational follow-up turns.
  - Interactive citation badges linking straight to the shared evidence sidebar.
- **Disease-First Audience-Aware Generation**:
  - **Patient Register**: Grade 6-8 reading level, everyday relatable analogy explaining what happens inside the body, practical lifestyle solutions, home monitoring metrics, and doctor consultation checklists.
  - **Clinician Register**: Deep cellular/molecular pathophysiology, GDMT protocols, titration intervals, organ clearance cutoffs, and landmark trial endpoint citations.
- **Non-Blocking Clinical Acuity Guardrails**: Deterministic red-flag symptom detection attaches a prominent clinical acuity advisory banner while maintaining continuous access to evidence.
- **Private Internal Medical Database**: Hidden internal database comprising 100 conditions, 500+ symptoms, and 200+ GDMT solutions indexed via hybrid search (BM25 + Qdrant vectors).
- **Autonomous Clinical Tools**:
  - `eGFR Calculator (CKD-EPI 2021)`: Race-free renal filtration formula + drug dosing cutoffs (Paxlovid/Metformin).
  - `BMI & GLP-1 Eligibility`: WHO obesity classification and guideline-directed incretin indications.
  - `CHA2DS2-VASc Score`: Non-valvular Atrial Fibrillation stroke risk & oral anticoagulation (DOAC) guidance.
  - `Wells Criteria for PE`: Pulmonary embolism clinical probability & CTPA/D-dimer pathway.
  - `Drug-Drug Interaction (DDI) Screener`: CYP3A4/CYP2D6 inhibition, QT prolongation, Black Box warnings.
  - `PubMed & Guideline Tools`: NCBI Entrez literature retrieval + WHO, AHA, ADA, GINA consensus guidelines.
- **Multi-Provider LLM Gateway**: Seamless support for OpenAI (GPT-4o), Groq (Llama 3.3), Google Gemini, Ollama (local private model), and an offline EBM clinical fallback engine.

