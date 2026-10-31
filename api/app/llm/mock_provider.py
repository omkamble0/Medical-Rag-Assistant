"""
Deterministic Mock LLM Provider for Testing and Benchmarking.
Allows tests to run without external network, API keys, or nondeterministic flakiness.
"""

from typing import List, Dict, Optional
from app.interfaces.llm_provider import LLMProviderInterface, LLMResponse


class MockClinicalLLMProvider(LLMProviderInterface):
    """Mock LLM provider returning realistic clinical syntheses."""

    def __init__(self, default_response: Optional[str] = None):
        self.default_response = default_response

    def get_provider_name(self) -> str:
        return "Deterministic Mock Provider"

    def is_available(self) -> bool:
        return True

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> LLMResponse:
        p_low = prompt.lower()
        evidence_sentences = []
        if "CLINICAL EVIDENCE:" in prompt:
            ev_section = prompt.split("CLINICAL EVIDENCE:")[1].split("USER INQUIRY:")[0]
            for line in ev_section.splitlines():
                line = line.strip()
                if len(line) > 30 and not line.startswith("[Evidence"):
                    # Extract a clean sentence from evidence
                    first_sent = line.split(". ")[0] + "." if ". " in line else line[:120] + "."
                    evidence_sentences.append(first_sent)

        if self.default_response:
            ans = self.default_response
        elif "patient" in (system_prompt or "").lower():
            ev_summary = " ".join(evidence_sentences[:2]) if evidence_sentences else (
                "Proven clinical guidelines recommend lifestyle adjustments and prescribed medication therapy."
            )
            ans = (
                f"### 1. Understanding the Condition: What It Is\n"
                f"{ev_summary}\n\n"
                f"### 2. Practical Solutions\n"
                f"- Adopt daily aerobic walking and healthy nutrition with lower sodium.\n"
                f"- Continue prescribed medications according to medical guidelines.\n\n"
                f"### 3. Questions to Ask Your Doctor\n"
                f"- What are my specific target numbers?\n"
                f"- What warning signs should I watch out for?"
            )
        else:
            ev_summary = "\n".join([f"- {s}" for s in evidence_sentences[:3]]) if evidence_sentences else (
                "- Guideline-directed medical therapy recommended."
            )
            ans = (
                f"### 1. Disease Overview\n"
                f"{ev_summary}\n\n"
                f"### 2. Guideline-Directed Medical Therapy\n"
                f"First-line pharmacotherapy recommendations with contraindication screening.\n\n"
                f"### 3. Landmark Clinical Research\n"
                f"Referencing Oxford CEBM Level 1 systematic reviews and randomized controlled trials."
            )

        return LLMResponse(
            content=ans,
            provider="MockClinicalLLMProvider",
            model="mock-gpt4-v1",
            prompt_tokens=len(prompt.split()),
            completion_tokens=len(ans.split()),
            latency_ms=5.0,
            status="success"
        )

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> LLMResponse:
        last_msg = messages[-1]["content"] if messages else ""
        sys_msg = next((m["content"] for m in messages if m.get("role") == "system"), None)
        return self.generate(prompt=last_msg, system_prompt=sys_msg, temperature=temperature, model_name=model_name)

