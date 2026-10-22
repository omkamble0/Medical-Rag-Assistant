export type UserMode = 'professional' | 'patient';

export type EvidenceLevel =
  | 'Level 1 (Meta-Analysis / Systematic Review)'
  | 'Level 2 (Randomized Controlled Trial)'
  | 'Level 3 (Cohort / Case-Control Study)'
  | 'Level 4 (Case Series / Observational)'
  | 'Level 5 (Expert Opinion / Clinical Guideline)';

export type ConfidenceStatus = 'high' | 'moderate' | 'low';

export interface JargonItem {
  term: string;
  plain_english: string;
}

export type PSAType = 'Parameter' | 'Safety' | 'Action';

export interface DoctorQuestion {
  question: string;
  category: string;
  psa_type?: PSAType | string;
  rationale?: string;
}

export interface PatientDemographics {
  age_group?: string;
  pregnancy_status?: string;
  comorbidities?: string[];
}

export interface ClinicalEntities {
  primary_condition?: string;
  interventions?: string[];
  patient_demographics?: PatientDemographics;
  clinical_metrics?: Record<string, any>;
}

export interface ParsedQueryAnalysis {
  raw_query: string;
  entities: ClinicalEntities;
  missing_variables: string[];
  context_gaps: string[];
  requires_disambiguation: boolean;
  recommended_clarifications: string[];
}

export interface PatientSuggestion {
  lifestyle_recommendations: string[];
  questions_for_doctor: DoctorQuestion[];
  monitoring_metrics: string[];
}

export interface ClinicianSuggestion {
  trial_subgroup_analyses: string[];
  titration_protocols: string[];
  guideline_comparisons: string[];
  contraindications_interactions: string[];
}

export interface ElaborationOption {
  label: string;
  query: string;
  health_body: string;
  context: string;
}

export interface SourceDocument {
  id: string;
  citation_index: number;
  title: string;
  journal: string;
  year: number;
  doi_or_pmid?: string;
  evidence_level: EvidenceLevel;
  snippet: string;
  relevance_score: number;
  key_takeaway?: string;
}

export interface ConfidenceMetrics {
  overall_score: number;
  status: ConfidenceStatus;
  retrieval_relevance: number;
  grounding_ratio: number;
  evidence_freshness: number;
  explanation: string;
}

export interface EmergencyTriageAlert {
  is_emergency: boolean;
  urgency: string;
  matched_keywords: string[];
  headline: string;
  critical_guidance: string;
  red_flag_symptoms: string[];
  emergency_contacts: string[];
}

export interface MedicalTermDetail {
  term: string;
  standard: string;
  category: string;
  snomed_id: string;
}

export interface ValidationResult {
  original: string;
  corrected: string;
  is_valid: boolean;
  corrections_made: string[];
  confidence_score: number;
  medical_terms_found: string[];
  medical_terms_details?: MedicalTermDetail[];
  issues: string[];
}

export interface SearchResponse {
  query: string;
  user_mode: UserMode;
  is_emergency: boolean;
  triage_alert?: EmergencyTriageAlert;
  validation?: ValidationResult;
  query_analysis?: ParsedQueryAnalysis;
  context_gaps?: string[];
  clinical_thinking?: string;
  answer: string;
  citations: number[];
  sources: SourceDocument[];
  confidence: ConfidenceMetrics;
  accuracy_score?: number;
  elaboration_leadings?: ElaborationOption[];
  jargon_glossary?: JargonItem[];
  doctor_questions?: DoctorQuestion[];
  patient_suggestions?: PatientSuggestion;
  clinician_suggestions?: ClinicianSuggestion;
  reading_level?: string;
  latency_ms: number;
  execution_trace?: AgentExecutionTraceStep[];
  tool_results?: ToolResults;
  crag_grade?: CRAGGradeResult;
  grounding_audit?: SelfRAGGroundingResult;
}

export interface AgentExecutionTraceStep {
  step: string;
  icon: string;
  timestamp: string;
  summary: string;
  details: any;
}

export interface DrugInteractionAlert {
  severity: 'CONTRAINDICATED' | 'MAJOR' | 'MODERATE' | string;
  mechanism: string;
  clinical_risk: string;
  management: string;
}

export interface DrugInteractionResult {
  screened_medications: string[];
  interactions_found: number;
  ddi_alerts: DrugInteractionAlert[];
  black_box_and_safety_profiles: Array<{
    drug: string;
    black_box_warning: string;
    key_precautions: string;
    organ_thresholds: string;
  }>;
}

export interface ClinicalCalculatorResult {
  calculator: string;
  egfr?: number;
  bmi?: number;
  score?: number;
  unit?: string;
  stage?: string;
  category?: string;
  risk_level?: string;
  interpretation?: string;
  recommendation?: string;
  guideline_indications?: string;
  pharmacotherapy_alerts?: string[];
  clinical_action?: string;
}

export interface CRAGGradeResult {
  is_sufficient: boolean;
  relevance_score: number;
  grade_decision: 'PASSED_CORRECTIVE_FILTER' | 'TRIGGER_FALLBACK_SEARCH' | string;
  graded_documents_count: number;
  rationale: string;
  missing_aspects: string[];
}

export interface SelfRAGGroundingResult {
  is_grounded: boolean;
  grounding_score: number;
  hallucination_risk_pct: number;
  total_citations_found: number;
  verified_citations: Array<{
    citation_index: number;
    title: string;
    journal: string;
    year: number;
    evidence_level: string;
    status: string;
  }>;
  unsupported_claims: string[];
  audit_summary: string;
  corrections_applied?: string[];
}

export interface ToolResults {
  drug_interactions?: DrugInteractionResult;
  clinical_calculator?: ClinicalCalculatorResult;
  pubmed_literature?: Array<{
    pmid: string;
    title: string;
    journal: string;
    year: number;
    evidence_level: string;
    abstract: string;
  }>;
  consensus_guidelines?: Array<{
    organization: string;
    guideline_title: string;
    year: number;
    condition: string;
    recommendation: string;
    evidence_strength: string;
  }>;
}

export interface AgenticWorkflowResponse {
  status: string;
  query: string;
  audience: string;
  answer: string;
  sources: SourceDocument[];
  execution_trace: AgentExecutionTraceStep[];
  tool_results: ToolResults;
  crag_grade?: CRAGGradeResult;
  grounding_audit?: SelfRAGGroundingResult;
  triage_alert?: EmergencyTriageAlert;
  decomposition?: any;
  provider_info?: {
    active_provider: string;
    openai_available: boolean;
    groq_available: boolean;
    gemini_available: boolean;
    ollama_available: boolean;
  };
}

// ============================================================
// Medical Knowledge Database & Symptom Differential Interfaces
// ============================================================

export interface DiseaseSymptom {
  name: string;
  frequency: 'hallmark' | 'common' | 'occasional' | 'rare' | string;
  severity: 'mild' | 'moderate' | 'severe' | string;
  description?: string;
}

export interface SolutionItem {
  id: string;
  type: 'pharmacological' | 'lifestyle' | 'non_pharmacological' | 'procedural' | 'emergency' | string;
  line_of_therapy: 'first_line' | 'second_line' | 'adjunctive' | 'maintenance' | 'rescue' | string;
  name: string;
  description: string;
  dosage_or_protocol?: string;
  contraindications: string[];
  side_effects: string[];
  monitoring?: string;
}

export interface ResearchPaper {
  id: string;
  title: string;
  journal: string;
  year: number;
  doi_or_pmid?: string;
  cebm_level: string;
  study_design: string;
  sample_size?: string;
  key_findings: string;
  clinical_takeaway: string;
  url?: string;
}

export interface DoctorChecklist {
  parameter_question: string;
  safety_question: string;
  action_threshold_question: string;
}

export interface DiseaseRecord {
  id: string;
  name: string;
  alternative_names: string[];
  icd10_code: string;
  specialty: string;
  organ_system: string;
  severity: string;
  overview: string;
  patient_plain_language: string;
  symptoms: DiseaseSymptom[];
  red_flags: string[];
  solutions: SolutionItem[];
  research_papers: ResearchPaper[];
  doctor_checklist?: DoctorChecklist;
  keywords: string[];
}

export interface SymptomCheckerRequest {
  symptoms: string[];
  patient_age?: number;
  gender?: string;
  duration?: string;
  top_k?: number;
}

export interface MatchedDiseaseResult {
  disease_id: string;
  disease_name: string;
  icd10_code: string;
  specialty: string;
  match_score: number;
  matched_symptoms: string[];
  missing_typical_symptoms: string[];
  has_red_flags: boolean;
  triggered_red_flags: string[];
  first_line_solutions: SolutionItem[];
  top_research_papers: ResearchPaper[];
  patient_summary: string;
  recommended_action: string;
}

export interface SymptomCheckerResponse {
  query_symptoms: string[];
  emergency_alert?: string;
  top_matches: MatchedDiseaseResult[];
  total_conditions_evaluated: number;
  disclaimer: string;
}

export interface DatabaseStatsResponse {
  total_diseases: number;
  total_symptoms: number;
  total_solutions: number;
  total_research_papers: number;
  specialties_distribution: Record<string, number>;
  evidence_levels_distribution: Record<string, number>;
  vector_store_status: string;
  vector_collection_name: string;
  indexed_vectors_count: number;
}

// ============================================================
// Conversational Clinical Chat Engine Types
// ============================================================

export interface ChatMessage {
  role: "user" | "assistant" | "system";
  content: string;
  timestamp?: string;
  audience?: "patient" | "doctor";
  citations?: number[];
  triage_alert?: EmergencyTriageAlert | null;
}

export interface ChatRequest {
  message: string;
  conversation_id?: string;
  audience?: "patient" | "doctor";
  history?: ChatMessage[];
  active_condition?: string;
}

export interface ChatResponse {
  conversation_id: string;
  audience: "patient" | "doctor";
  message: string;
  history: ChatMessage[];
  active_condition?: string;
  triage_alert?: EmergencyTriageAlert | null;
  citations: number[];
  sources: SourceDocument[];
  suggested_followups: string[];
  confidence?: ConfidenceMetrics;
  latency_ms: number;
}

// ============================================================
// Medical Encyclopedia & Clinical Compendium (WikiMed) Types
// ============================================================

export interface WikiSection {
  id: string;
  title: string;
  icon: string;
  content: string;
  summary_bullet?: string | null;
  callout_alert?: string | null;
}

export interface EncyclopediaTopicSummary {
  id: string;
  name: string;
  icd10_code: string;
  specialty: string;
  organ_system: string;
  severity: string;
  cebm_level: string;
  short_summary: string;
  hallmark_symptoms: string[];
  has_emergency_red_flags: boolean;
}

export interface EncyclopediaArticle {
  id: string;
  title: string;
  alternative_names: string[];
  icd10_code: string;
  specialty: string;
  organ_system: string;
  severity_tier: string;
  cebm_level: string;
  mode: "patient" | "clinician";
  layperson_summary: string;
  clinical_summary: string;
  plain_analogy: string;
  grounding_score: number;
  sections: WikiSection[];
  source_authorities: string[];
  landmark_citations: Array<{
    citation_index: number;
    title: string;
    journal: string;
    year: number;
    cebm_level: string;
    doi_or_pmid?: string | null;
    takeaway: string;
  }>;
  related_topics: Array<{
    id: string;
    name: string;
    specialty: string;
    icd10: string;
  }>;
  jargon_glossary: Array<{
    term: string;
    plain_english: string;
  }>;
  emergency_red_flags: string[];
  doctor_checklist?: {
    parameter?: string;
    safety?: string;
    action?: string;
  } | null;
  last_reviewed: string;
}



