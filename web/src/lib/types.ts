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

export interface SearchResponse {
  query: string;
  user_mode: UserMode;
  is_emergency: boolean;
  triage_alert?: EmergencyTriageAlert;
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
}
