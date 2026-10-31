"""
Dependency Injection Container and FastAPI Providers for AegisMed.
Enables pluggable, testable, and replaceable service dependencies across API routes.
"""

from typing import Optional
from fastapi import Depends

from app.interfaces.retriever import RetrieverInterface
from app.interfaces.llm_provider import LLMProviderInterface
from app.interfaces.guardrail import SafetyGuardrailInterface
from app.retrieval.hybrid_retriever import HybridClinicalRetriever
from app.llm.gateway import AegisMedLLMGateway
from app.domain.services.safety_service import ClinicalSafetyService
from app.domain.services.triage_service import ClinicalTriageService
from app.domain.services.escalation_service import ClinicalEscalationService
from app.domain.services.knowledge_service import MedicalKnowledgeService
from app.domain.services.clinical_orchestrator import ClinicalOrchestrator


class DIContainer:
    """Singleton Dependency Injection registry with test overrides."""

    def __init__(self, settings: Optional[Any] = None):
        self.settings = settings
        self._retriever: Optional[RetrieverInterface] = None
        self._llm: Optional[LLMProviderInterface] = None
        self._safety: Optional[SafetyGuardrailInterface] = None
        self._triage: Optional[ClinicalTriageService] = None
        self._escalation: Optional[ClinicalEscalationService] = None
        self._knowledge: Optional[MedicalKnowledgeService] = None
        self._orchestrator: Optional[ClinicalOrchestrator] = None

    def get_retriever(self) -> RetrieverInterface:
        if self._retriever is None:
            self._retriever = HybridClinicalRetriever()
        return self._retriever

    def set_retriever(self, retriever: RetrieverInterface):
        self._retriever = retriever
        self._orchestrator = None  # Invalidate orchestrator cache

    def get_llm(self) -> LLMProviderInterface:
        if self._llm is None:
            self._llm = AegisMedLLMGateway()
        return self._llm

    def set_llm(self, llm: LLMProviderInterface):
        self._llm = llm
        self._orchestrator = None

    def get_safety(self) -> SafetyGuardrailInterface:
        if self._safety is None:
            self._safety = ClinicalSafetyService()
        return self._safety

    def set_safety(self, safety: SafetyGuardrailInterface):
        self._safety = safety
        self._orchestrator = None

    def get_triage(self) -> ClinicalTriageService:
        if self._triage is None:
            self._triage = ClinicalTriageService()
        return self._triage

    def get_escalation(self) -> ClinicalEscalationService:
        if self._escalation is None:
            self._escalation = ClinicalEscalationService()
        return self._escalation

    def get_knowledge(self) -> MedicalKnowledgeService:
        if self._knowledge is None:
            self._knowledge = MedicalKnowledgeService()
        return self._knowledge

    # Convenience alias methods for domain nomenclature
    get_llm_gateway = get_llm
    get_safety_service = get_safety
    get_triage_service = get_triage
    get_escalation_service = get_escalation
    get_knowledge_service = get_knowledge

    def get_orchestrator(self) -> ClinicalOrchestrator:
        if self._orchestrator is None:
            self._orchestrator = ClinicalOrchestrator(
                retriever=self.get_retriever(),
                llm_provider=self.get_llm(),
                safety_service=self.get_safety(),
                triage_service=self.get_triage(),
                escalation_service=self.get_escalation()
            )
        return self._orchestrator

    def reset(self):
        """Resets all singletons to defaults (useful in test teardown)."""
        self._retriever = None
        self._llm = None
        self._safety = None
        self._triage = None
        self._escalation = None
        self._knowledge = None
        self._orchestrator = None


container = DIContainer()


# FastAPI Dependency Providers
def get_retriever_dep() -> RetrieverInterface:
    return container.get_retriever()


def get_llm_dep() -> LLMProviderInterface:
    return container.get_llm()


def get_safety_dep() -> SafetyGuardrailInterface:
    return container.get_safety()


def get_triage_dep() -> ClinicalTriageService:
    return container.get_triage()


def get_escalation_dep() -> ClinicalEscalationService:
    return container.get_escalation()


def get_knowledge_dep() -> MedicalKnowledgeService:
    return container.get_knowledge()


def get_orchestrator_dep() -> ClinicalOrchestrator:
    return container.get_orchestrator()

