"""
Unified Production LLM Gateway for AegisMed.
Implements LLMProviderInterface with multi-provider failover cascade:
OpenAI -> Groq -> Gemini -> Ollama -> High-Fidelity Local Offline Clinical Engine.
"""

import time
import logging
from typing import List, Dict, Any, Optional
from app.interfaces.llm_provider import LLMProviderInterface, LLMResponse
from app.config import settings
from app.services.llm_gateway import llm_gateway
from app.core.metrics import metrics

logger = logging.getLogger(__name__)


class AegisMedLLMGateway(LLMProviderInterface):
    """
    Production-grade LLM Gateway implementing LLMProviderInterface:
    - Provides seamless failover across OpenAI, Groq, Gemini, and Ollama
    - Guaranteed zero-dependency fallback via rule-grounded clinical synthesizer
    - Tracks latency, token counts, and fallback events into metrics registry
    """

    def __init__(self, offline_mode: Optional[bool] = None):
        self.offline_mode = offline_mode if offline_mode is not None else (settings.OFFLINE_MODE or settings.IS_TESTING)

    def get_provider_name(self) -> str:
        if self.offline_mode:
            return "Local Clinical Synthesis Engine (Offline Mode)"
        return llm_gateway.get_active_provider_info().get("active_provider", "Local Clinical Synthesis Engine")

    def is_available(self) -> bool:
        return True

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> LLMResponse:
        start_time = time.time()

        if self.offline_mode:
            # Fast offline / deterministic test path
            from app.llm.mock_provider import MockClinicalLLMProvider
            mock = MockClinicalLLMProvider()
            res = mock.generate(prompt=prompt, system_prompt=system_prompt, temperature=temperature, model_name=model_name)
            metrics.record_fallback(provider="AegisMed Local Synthesizer", reason="offline_mode_active")
            return res

        try:
            res = llm_gateway.generate(
                prompt=prompt,
                system_prompt=system_prompt,
                temperature=temperature,
                model_name=model_name
            )
            duration = (time.time() - start_time) * 1000
            content = res.get("content")

            if not content:
                # LLM returned empty or failed -> use local fallback
                metrics.record_fallback(provider=res.get("provider", "unknown"), reason="empty_or_refusal")
                content = llm_gateway._synthesize_local_response(user_text=prompt, system_prompt=system_prompt)

            p_tokens = len(prompt.split())
            c_tokens = len(content.split()) if content else 0
            metrics.record_tokens(p_tokens, c_tokens)

            return LLMResponse(
                content=content,
                provider=res.get("provider", "AegisMed Local Engine"),
                model=res.get("model", "default"),
                prompt_tokens=p_tokens,
                completion_tokens=c_tokens,
                latency_ms=round(duration, 2),
                status="success" if res.get("status") == "success" else "fallback"
            )
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            logger.warning(f"LLM Gateway execution error: {e}. Cascading to local clinical synthesizer.")
            metrics.record_fallback(provider="AegisMed Local Synthesizer", reason="exception_cascade")
            fallback_content = llm_gateway._synthesize_local_response(user_text=prompt, system_prompt=system_prompt)
            return LLMResponse(
                content=fallback_content,
                provider="AegisMed Local Clinical Synthesizer",
                model="rule-grounded-ebm-v2",
                latency_ms=round(duration, 2),
                status="fallback",
                error=str(e)
            )

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> LLMResponse:
        start_time = time.time()

        if self.offline_mode:
            last_user_msg = next((m["content"] for m in reversed(messages) if m.get("role") == "user"), "")
            sys_msg = next((m["content"] for m in messages if m.get("role") == "system"), None)
            content = llm_gateway._synthesize_local_response(user_text=last_user_msg, system_prompt=sys_msg)
            duration = (time.time() - start_time) * 1000
            return LLMResponse(
                content=content,
                provider="AegisMed Local Clinical Synthesizer",
                model="rule-grounded-ebm-v2",
                latency_ms=round(duration, 2),
                status="success"
            )

        try:
            res = llm_gateway.chat(messages=messages, temperature=temperature, model_name=model_name)
            duration = (time.time() - start_time) * 1000
            content = res.get("content")

            if not content:
                last_user = next((m["content"] for m in reversed(messages) if m.get("role") == "user"), "")
                sys_msg = next((m["content"] for m in messages if m.get("role") == "system"), None)
                content = llm_gateway._synthesize_local_response(user_text=last_user, system_prompt=sys_msg)

            return LLMResponse(
                content=content,
                provider=res.get("provider", "AegisMed Local Engine"),
                model=res.get("model", "default"),
                latency_ms=round(duration, 2),
                status="success" if res.get("status") == "success" else "fallback"
            )
        except Exception as e:
            duration = (time.time() - start_time) * 1000
            last_user = next((m["content"] for m in reversed(messages) if m.get("role") == "user"), "")
            content = llm_gateway._synthesize_local_response(user_text=last_user)
            return LLMResponse(
                content=content,
                provider="AegisMed Local Clinical Synthesizer",
                model="rule-grounded-ebm-v2",
                latency_ms=round(duration, 2),
                status="fallback",
                error=str(e)
            )

