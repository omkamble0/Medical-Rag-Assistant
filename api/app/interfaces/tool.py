"""
Clinical Tool Interface Specification for AegisMed.
Defines contracts for validated medical calculators, drug interaction screeners,
guideline checkers, and literature search tools.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class ToolParameter(BaseModel):
    name: str
    type: str
    description: str
    required: bool = True
    default: Optional[Any] = None


class ToolExecutionResult(BaseModel):
    tool_name: str
    success: bool
    data: Dict[str, Any]
    clinical_alerts: List[str] = Field(default_factory=list)
    confidence: float = 1.0
    error: Optional[str] = None


class ClinicalToolInterface(ABC):
    """Abstract interface for clinical computation & decision support tools."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier of the tool."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Clinical purpose and evidence basis for the tool."""
        pass

    @property
    @abstractmethod
    def parameters(self) -> List[ToolParameter]:
        """Typed input schema."""
        pass

    @abstractmethod
    def execute(self, **kwargs) -> ToolExecutionResult:
        """Executes the clinical tool with provided arguments."""
        pass


class ToolRegistryInterface(ABC):
    """Registry managing available clinical tools."""

    @abstractmethod
    def register(self, tool: ClinicalToolInterface) -> None:
        pass

    @abstractmethod
    def get(self, name: str) -> Optional[ClinicalToolInterface]:
        pass

    @abstractmethod
    def list_tools(self) -> List[Dict[str, Any]]:
        pass

