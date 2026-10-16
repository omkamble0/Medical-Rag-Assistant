from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class DiseaseSymptom(BaseModel):
    name: str = Field(..., description="Name of the symptom")
    frequency: str = Field(default="common", description="common, occasional, hallmark, or rare")
    severity: str = Field(default="moderate", description="mild, moderate, or severe")
    description: Optional[str] = Field(default=None, description="Clinical description of symptom manifestation")

class SolutionItem(BaseModel):
    id: str = Field(..., description="Unique solution ID")
    type: str = Field(..., description="pharmacological, lifestyle, non_pharmacological, procedural, emergency")
    line_of_therapy: str = Field(default="first_line", description="first_line, second_line, adjunctive, maintenance, rescue")
    name: str = Field(..., description="Name of medication, procedure, or lifestyle therapy")
    description: str = Field(..., description="Mechanism, protocol, or guideline description")
    dosage_or_protocol: Optional[str] = Field(default=None, description="Clinical dosing or protocol target")
    contraindications: List[str] = Field(default_factory=list, description="Known contraindications")
    side_effects: List[str] = Field(default_factory=list, description="Common adverse effects")
    monitoring: Optional[str] = Field(default=None, description="Monitoring cadence and lab surveillance")

class ResearchPaper(BaseModel):
    id: str = Field(..., description="Unique paper identifier")
    title: str = Field(..., description="Full paper or trial title")
    journal: str = Field(..., description="Journal or publishing medical body")
    year: int = Field(..., description="Year of publication")
    doi_or_pmid: Optional[str] = Field(default=None, description="DOI or PubMed PMID")
    cebm_level: str = Field(..., description="Oxford CEBM Evidence Level (Level 1 to Level 5)")
    study_design: str = Field(default="Randomized Controlled Trial", description="Study design (e.g. Phase 3 RCT, Meta-Analysis, Guideline)")
    sample_size: Optional[str] = Field(default=None, description="Study cohort size (n)")
    key_findings: str = Field(..., description="Statistical endpoints, relative risk reduction, hazard ratios")
    clinical_takeaway: str = Field(..., description="Actionable conclusion for clinicians")
    url: Optional[str] = Field(default=None, description="Web citation link or PubMed URL")

class DoctorChecklist(BaseModel):
    parameter_question: str = Field(..., description="Quantitative metric question for doctor")
    safety_question: str = Field(..., description="Medication interaction or safety question")
    action_threshold_question: str = Field(..., description="Urgency / emergency action question")

class DiseaseRecord(BaseModel):
    id: str = Field(..., description="Unique condition code (e.g. DIS-CARD-001)")
    name: str = Field(..., description="Primary clinical condition name")
    alternative_names: List[str] = Field(default_factory=list, description="Synonyms, acronyms, or layman terms")
    icd10_code: str = Field(..., description="ICD-10-CM diagnostic classification code")
    specialty: str = Field(..., description="Medical specialty (Cardiology, Endocrinology, Pulmonology, etc.)")
    organ_system: str = Field(..., description="Target physiological system")
    severity: str = Field(default="Moderate", description="Typical severity spectrum (Mild, Moderate, Severe, Life-Threatening)")
    overview: str = Field(..., description="Comprehensive clinical monograph overview")
    patient_plain_language: str = Field(..., description="Everyday language explanation for patients")
    symptoms: List[DiseaseSymptom] = Field(default_factory=list, description="Associated symptoms")
    red_flags: List[str] = Field(default_factory=list, description="Emergency warning signs requiring immediate triage")
    solutions: List[SolutionItem] = Field(default_factory=list, description="Clinical solutions and treatment protocols")
    research_papers: List[ResearchPaper] = Field(default_factory=list, description="Peer-reviewed research evidence and trials")
    doctor_checklist: Optional[DoctorChecklist] = Field(default=None, description="Guidance questions for clinical visits")
    keywords: List[str] = Field(default_factory=list, description="Searchable indexing keywords")
    evidence_stack: Optional[Dict[str, Any]] = Field(default=None, description="3-Stack evidence layer (MedlinePlus, OpenFDA, PubMed/CEBM)")

class SymptomCheckerRequest(BaseModel):
    symptoms: List[str] = Field(..., min_length=1, description="List of patient symptoms (e.g. ['chest pain', 'shortness of breath'])")
    patient_age: Optional[int] = Field(default=None, description="Optional patient age")
    gender: Optional[str] = Field(default=None, description="Optional patient gender ('male', 'female', 'other')")
    duration: Optional[str] = Field(default=None, description="Optional symptom duration (e.g. '3 days', 'acute', 'chronic')")
    top_k: int = Field(default=5, ge=1, le=15, description="Number of differential candidate matches to return")

class MatchedDiseaseResult(BaseModel):
    disease_id: str
    disease_name: str
    icd10_code: str
    specialty: str
    match_score: float = Field(..., description="Calculated matching confidence (0 - 100%)")
    matched_symptoms: List[str] = Field(default_factory=list)
    missing_typical_symptoms: List[str] = Field(default_factory=list)
    has_red_flags: bool = False
    triggered_red_flags: List[str] = Field(default_factory=list)
    first_line_solutions: List[SolutionItem] = Field(default_factory=list)
    top_research_papers: List[ResearchPaper] = Field(default_factory=list)
    patient_summary: str
    recommended_action: str

class SymptomCheckerResponse(BaseModel):
    query_symptoms: List[str]
    emergency_alert: Optional[str] = None
    top_matches: List[MatchedDiseaseResult]
    total_conditions_evaluated: int
    disclaimer: str

class DatabaseStatsResponse(BaseModel):
    total_diseases: int
    total_symptoms: int
    total_solutions: int
    total_research_papers: int
    specialties_distribution: Dict[str, int]
    evidence_levels_distribution: Dict[str, int]
    vector_store_status: str
    vector_collection_name: str
    indexed_vectors_count: int
