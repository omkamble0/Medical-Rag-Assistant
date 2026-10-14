"""
AegisMed Medical Knowledge Database Autonomous Tool
Exposes LangChain compatible tools for the Agentic RAG workflow:
- `query_medical_knowledge_database`: looks up disease profiles, solutions, and research papers
- `differential_symptom_checker`: runs multi-symptom differential diagnosis matching
"""

from typing import List, Dict, Any, Optional
from langchain_core.tools import tool
from app.services.medical_db import medical_db
from app.models.medical_db_schemas import SymptomCheckerRequest


def lookup_disease_in_database(query: str, specialty: Optional[str] = None) -> Dict[str, Any]:
    """
    Looks up conditions, clinical treatments, and research trials in the Medical Knowledge Database.
    """
    diseases = medical_db.get_diseases(query=query, specialty=specialty, limit=3)
    if not diseases:
        # Try hybrid vector search
        hybrid_hits = medical_db.search_hybrid(query=query, top_k=2)
        if hybrid_hits:
            return {
                "status": "success",
                "source": "Qdrant Hybrid Vector Store",
                "matches_count": len(hybrid_hits),
                "results": hybrid_hits
            }
        return {
            "status": "not_found",
            "message": f"No exact matches for '{query}' in the medical knowledge database."
        }

    results = []
    for d in diseases:
        first_line_rx = [s.name for s in d.solutions if s.line_of_therapy == "first_line"]
        results.append({
            "disease_id": d.id,
            "name": d.name,
            "icd10": d.icd10_code,
            "specialty": d.specialty,
            "overview": d.overview[:250],
            "hallmark_symptoms": [s.name for s in d.symptoms if s.frequency == "hallmark"][:4],
            "first_line_solutions": first_line_rx[:2],
            "landmark_paper": d.research_papers[0].title if d.research_papers else None,
            "evidence_level": d.research_papers[0].cebm_level if d.research_papers else None,
            "red_flags": d.red_flags[:2]
        })

    return {
        "status": "success",
        "matches_count": len(results),
        "results": results
    }


def run_differential_symptom_checker(symptoms: List[str]) -> Dict[str, Any]:
    """
    Executes symptom-to-disease differential diagnosis ranking.
    """
    req = SymptomCheckerRequest(symptoms=symptoms, top_k=3)
    response = medical_db.check_symptoms(req)
    return response.model_dump()


@tool("medical_knowledge_database_tool")
def medical_database_tool(query: str, specialty: str = "") -> str:
    """
    Autonomous clinical tool to search the AegisMed Medical Knowledge Database
    for verified disease monographs, ICD-10 codes, first-line treatments, and landmark RCTs.
    """
    res = lookup_disease_in_database(query=query, specialty=specialty or None)
    return str(res)


@tool("symptom_differential_checker_tool")
def symptom_checker_tool(symptoms_csv: str) -> str:
    """
    Autonomous clinical tool to match patient symptoms to candidate diseases with
    confidence scores, hallmark symptoms, first-line solutions, and red flag warnings.
    Input should be comma-separated symptoms (e.g. 'chest pain, shortness of breath').
    """
    symptoms = [s.strip() for s in symptoms_csv.split(",") if s.strip()]
    res = run_differential_symptom_checker(symptoms)
    return str(res)
