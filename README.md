# Medical-Rag-Assistant 🩺

An evidence-based **Agentic Medical RAG Assistant** featuring real-time query validation (typo correction), vector evidence retrieval, audience-aware answer generation (Patient vs. Clinician modes), and Oxford CEBM grounding.

---

## 🏗️ Architecture Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USER QUERY ("headavhe symptoms")                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. QUERY GUARD & VALIDATION LAYER                           │
│    - Detects medical typos & normalizes terms               │
│    - Intercepts "headavhe" -> "headache" (100% confidence)  │
│    - Deterministic Tier-1 emergency triage guardrail        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. RETRIEVAL LAYER (Vector Evidence Base)                   │
│    - Fetches relevant consensus clinical guidelines (WHO,   │
│      AHA, ADA, GINA, ICHD-3, IDSA)                          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. AGENTIC LLM GENERATION & AUDIENCE ROUTING                │
│    - Patient Mode: 6th–8th grade reading level, empathy,    │
│      symptoms, home relief, red flag alerts, doctor queries │
│    - Doctor Mode: Precise clinical terminology, trial       │
│      endpoints, DDI screening, and Oxford CEBM evidence     │
│    - Cites grounded sources [1], [2]                        │
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
│   │   │   ├── rag_engine.py         # 4-stage clinical RAG engine
│   │   │   ├── query_guard.py        # Typo correction & validation gate
│   │   │   ├── query_validator.py    # Medical term lookup
│   │   │   ├── rag_agent.py          # Agentic RAG orchestrator
│   │   │   └── vector_store.py       # Vector evidence retrieval
│   │   ├── routes/
│   │   │   ├── medical_query.py      # /api/v1/medical-query & validation endpoints
│   │   │   └── validate.py           # Real-time query validation endpoints
│   │   ├── models/
│   │   │   ├── enums.py              # UserMode, EvidenceLevel
│   │   │   └── schemas.py            # Pydantic request/response schemas
│   │   └── main.py                   # FastAPI application
│   ├── requirements.txt
│   └── .env.example
├── web/
│   ├── src/
│   │   ├── app/                      # Next.js App router
│   │   ├── components/               # MedicalQueryPanel, ClinicianView, PatientView
│   │   ├── hooks/                    # useMedicalQuery, useQueryValidator
│   │   └── lib/                      # API client, types, suggestions
│   ├── package.json
│   └── tsconfig.json
├── tests/
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
cd api
pytest ../tests
```

---

## 🛡️ Key Features

- **Query Guard**: Catches typos like `headavhe` or `diabtes` and prompts user correction or auto-corrects before vector search.
- **Dual Perspective**: Toggle between plain-language patient summaries and rigorous clinician evidence.
- **Strict Evidence Grounding**: Answers cite peer-reviewed trial guidelines directly.
- **Safety Intercepts**: Deterministic red-flag emergency detection for acute presentations.
