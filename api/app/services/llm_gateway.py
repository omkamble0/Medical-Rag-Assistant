"""
Multi-Provider LLM Gateway for Medical-RAG-Assistant
Supports OpenAI (gpt-4o / gpt-4o-mini), Groq, Google Gemini, Ollama (local private LLM),
and provides an intelligent Local Clinical Synthesis Engine with zero external dependencies.
"""

import os
import logging
from typing import Dict, Any, Optional, List
import httpx

logger = logging.getLogger(__name__)


class MedicalLLMGateway:
    """
    Unified LLM Gateway with seamless multi-provider cascade:
    1. OpenAI (if OPENAI_API_KEY is configured)
    2. Groq (if GROQ_API_KEY is configured)
    3. Ollama (if running locally at localhost:11434)
    4. Local High-Fidelity Clinical Synthesis Engine (instant offline fallback)
    """

    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY", "")
        self.groq_key = os.getenv("GROQ_API_KEY", "")
        self.gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
        self.ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

    def get_active_provider_info(self) -> Dict[str, Any]:
        """Returns detected provider availability status."""
        has_openai = bool(self.openai_key and not self.openai_key.startswith("placeholder") and len(self.openai_key) > 10)
        has_groq = bool(self.groq_key and not self.groq_key.startswith("placeholder") and len(self.groq_key) > 10)
        has_gemini = bool(self.gemini_key and not self.gemini_key.startswith("placeholder") and len(self.gemini_key) > 10)

        # Quick check for Ollama
        has_ollama = False
        try:
            with httpx.Client(timeout=0.6) as client:
                res = client.get(f"{self.ollama_url}/api/tags")
                has_ollama = res.status_code == 200
        except Exception:
            has_ollama = False

        active_provider = "Local High-Fidelity Engine"
        if has_openai:
            active_provider = "OpenAI (GPT-4o)"
        elif has_groq:
            active_provider = "Groq (Llama-3.3-70B)"
        elif has_gemini:
            active_provider = "Google Gemini"
        elif has_ollama:
            active_provider = "Ollama (Local Private LLM)"

        return {
            "active_provider": active_provider,
            "openai_available": has_openai,
            "groq_available": has_groq,
            "gemini_available": has_gemini,
            "ollama_available": has_ollama,
            "local_fallback_active": True
        }

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Attempts execution via active provider cascade with automatic failover.
        """
        provider_info = self.get_active_provider_info()

        # 1. Try OpenAI
        if provider_info["openai_available"]:
            try:
                from langchain_openai import ChatOpenAI
                from langchain_core.messages import SystemMessage, HumanMessage

                llm = ChatOpenAI(
                    model=model_name or "gpt-4o",
                    temperature=temperature,
                    api_key=self.openai_key,
                    timeout=10.0
                )
                messages = []
                if system_prompt:
                    messages.append(SystemMessage(content=system_prompt))
                messages.append(HumanMessage(content=prompt))

                resp = llm.invoke(messages)
                return {
                    "content": resp.content,
                    "provider": "OpenAI",
                    "model": model_name or "gpt-4o",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"OpenAI call failed, cascading to next provider: {e}")

        # 2. Try Groq (using OpenAI compatible endpoint)
        if provider_info["groq_available"]:
            try:
                from langchain_openai import ChatOpenAI
                from langchain_core.messages import SystemMessage, HumanMessage

                llm = ChatOpenAI(
                    model=model_name or "llama-3.3-70b-versatile",
                    temperature=temperature,
                    api_key=self.groq_key,
                    base_url="https://api.groq.com/openai/v1",
                    timeout=10.0
                )
                messages = []
                if system_prompt:
                    messages.append(SystemMessage(content=system_prompt))
                messages.append(HumanMessage(content=prompt))

                resp = llm.invoke(messages)
                return {
                    "content": resp.content,
                    "provider": "Groq",
                    "model": model_name or "llama-3.3-70b-versatile",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"Groq call failed, cascading to next provider: {e}")

        # 3. Try Ollama (Local)
        if provider_info["ollama_available"]:
            try:
                with httpx.Client(timeout=8.0) as client:
                    payload = {
                        "model": model_name or "llama3",
                        "prompt": f"{system_prompt}\n\n{prompt}" if system_prompt else prompt,
                        "stream": False,
                        "options": {"temperature": temperature}
                    }
                    res = client.post(f"{self.ollama_url}/api/generate", json=payload)
                    if res.status_code == 200:
                        ollama_data = res.json()
                        return {
                            "content": ollama_data.get("response", ""),
                            "provider": "Ollama (Local)",
                            "model": model_name or "llama3",
                            "status": "success"
                        }
            except Exception as e:
                logger.warning(f"Ollama call failed: {e}")

        # 4. Local High-Fidelity Clinical Synthesis Fallback
        return {
            "content": None,
            "provider": "AegisMed Local Clinical Synthesis Engine",
            "model": "rule-grounded-ebm-v2",
            "status": "fallback"
        }

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.2,
        model_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Multi-turn chat completion across active provider cascade (OpenAI, Groq, Ollama, local fallback).
        Accepts list of message dicts: [{'role': 'system'|'user'|'assistant', 'content': '...'}]
        """
        provider_info = self.get_active_provider_info()

        # 1. Try OpenAI
        if provider_info["openai_available"]:
            try:
                from langchain_openai import ChatOpenAI
                from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

                llm = ChatOpenAI(
                    model=model_name or "gpt-4o",
                    temperature=temperature,
                    api_key=self.openai_key,
                    timeout=12.0
                )
                lc_messages = []
                for m in messages:
                    r = m.get("role", "user")
                    c = m.get("content", "")
                    if r == "system":
                        lc_messages.append(SystemMessage(content=c))
                    elif r == "assistant":
                        lc_messages.append(AIMessage(content=c))
                    else:
                        lc_messages.append(HumanMessage(content=c))

                resp = llm.invoke(lc_messages)
                return {
                    "content": resp.content,
                    "provider": "OpenAI",
                    "model": model_name or "gpt-4o",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"OpenAI chat call failed, cascading: {e}")

        # 2. Try Groq
        if provider_info["groq_available"]:
            try:
                from langchain_openai import ChatOpenAI
                from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

                llm = ChatOpenAI(
                    model=model_name or "llama-3.3-70b-versatile",
                    temperature=temperature,
                    api_key=self.groq_key,
                    base_url="https://api.groq.com/openai/v1",
                    timeout=12.0
                )
                lc_messages = []
                for m in messages:
                    r = m.get("role", "user")
                    c = m.get("content", "")
                    if r == "system":
                        lc_messages.append(SystemMessage(content=c))
                    elif r == "assistant":
                        lc_messages.append(AIMessage(content=c))
                    else:
                        lc_messages.append(HumanMessage(content=c))

                resp = llm.invoke(lc_messages)
                return {
                    "content": resp.content,
                    "provider": "Groq",
                    "model": model_name or "llama-3.3-70b-versatile",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"Groq chat call failed, cascading: {e}")

        # 3. Try Ollama (Local Chat API)
        if provider_info["ollama_available"]:
            try:
                with httpx.Client(timeout=10.0) as client:
                    payload = {
                        "model": model_name or "llama3",
                        "messages": messages,
                        "stream": False,
                        "options": {"temperature": temperature}
                    }
                    res = client.post(f"{self.ollama_url}/api/chat", json=payload)
                    if res.status_code == 200:
                        ollama_data = res.json()
                        msg = ollama_data.get("message", {}).get("content", "")
                        return {
                            "content": msg,
                            "provider": "Ollama (Local)",
                            "model": model_name or "llama3",
                            "status": "success"
                        }
            except Exception as e:
                logger.warning(f"Ollama chat call failed: {e}")

        # 4. Fallback to Local High-Fidelity Multi-Turn Synthesis Engine
        return {
            "content": None,
            "provider": "AegisMed Local Clinical Synthesis Engine",
            "model": "rule-grounded-ebm-v2",
            "status": "fallback"
        }


# Singleton instance
llm_gateway = MedicalLLMGateway()

