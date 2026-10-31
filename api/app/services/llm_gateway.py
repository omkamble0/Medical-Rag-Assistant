"""
Multi-Provider LLM Gateway for Medical-RAG-Assistant
Supports OpenAI (gpt-4o / gpt-4o-mini), Groq, Google Gemini, Ollama (local private LLM),
and provides an intelligent Local Clinical Synthesis Engine with zero external dependencies.
"""

import os
import logging
from typing import Dict, Any, Optional, List
import httpx

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from pydantic import SecretStr

logger = logging.getLogger(__name__)


class MedicalLLMGateway:
    """
    Unified LLM Gateway with seamless multi-provider cascade:
    1. OpenAI (if OPENAI_API_KEY is configured)
    2. Groq (if GROQ_API_KEY is configured)
    3. Google Gemini (if GEMINI_API_KEY or GOOGLE_API_KEY is configured)
    4. Ollama (if running locally at localhost:11434)
    5. Local High-Fidelity Clinical Synthesis Engine (instant offline fallback)
    """
    _network_blocked: bool = False

    def __init__(self):
        pass

    @property
    def is_offline(self) -> bool:
        if MedicalLLMGateway._network_blocked:
            return True
        try:
            from app.config import settings
            return getattr(settings, "is_offline", False)
        except Exception:
            return os.getenv("OFFLINE_MODE") in ("1", "true")

    @property
    def openai_key(self) -> str:
        if self.is_offline:
            return ""
        k = os.getenv("OPENAI_API_KEY", "")
        if not k:
            try:
                from app.config import settings
                k = getattr(settings, "OPENAI_API_KEY", "")
            except Exception:
                pass
        return "" if k.startswith("placeholder") else k

    @property
    def groq_key(self) -> str:
        if self.is_offline:
            return ""
        k = os.getenv("GROQ_API_KEY", "")
        if not k:
            try:
                from app.config import settings
                k = getattr(settings, "GROQ_API_KEY", "")
            except Exception:
                pass
        return "" if k.startswith("placeholder") else k

    @property
    def gemini_key(self) -> str:
        if self.is_offline:
            return ""
        k = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
        if not k:
            try:
                from app.config import settings
                k = getattr(settings, "GEMINI_API_KEY", "")
            except Exception:
                pass
        return "" if k.startswith("placeholder") else k

    @property
    def ollama_url(self) -> str:
        u = os.getenv("OLLAMA_BASE_URL", "")
        if not u:
            try:
                from app.config import settings
                u = getattr(settings, "OLLAMA_BASE_URL", "http://localhost:11434")
            except Exception:
                pass
        return u or "http://localhost:11434"

    @property
    def ollama_timeout(self) -> float:
        try:
            from app.config import settings
            default_t = getattr(settings, "OLLAMA_TIMEOUT", 20.0)
        except Exception:
            default_t = 20.0
        return float(os.getenv("OLLAMA_TIMEOUT", str(default_t)))

    def get_active_provider_info(self) -> Dict[str, Any]:
        """Returns detected provider availability status."""
        if self.is_offline:
            return {
                "active_provider": "Local High-Fidelity Engine",
                "openai_available": False,
                "groq_available": False,
                "gemini_available": False,
                "ollama_available": False,
                "local_fallback_active": True
            }

        has_openai = bool(self.openai_key and len(self.openai_key) > 10)
        has_groq = bool(self.groq_key and len(self.groq_key) > 10)
        has_gemini = bool(self.gemini_key and len(self.gemini_key) > 10)

        # Quick check for Ollama only if cloud providers are not configured and Ollama not disabled
        has_ollama = False
        if not (has_openai or has_groq or has_gemini) and os.getenv("DISABLE_OLLAMA", "").lower() not in ("1", "true", "yes"):
            try:
                with httpx.Client(timeout=0.4) as client:
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
                    api_key=SecretStr(self.openai_key),
                    timeout=10.0
                )
                messages: List[Any] = []
                if system_prompt:
                    messages.append(SystemMessage(content=system_prompt))
                messages.append(HumanMessage(content=prompt))

                resp = llm.invoke(messages)
                return {
                    "content": str(resp.content),
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
                    api_key=SecretStr(self.groq_key),
                    base_url="https://api.groq.com/openai/v1",
                    timeout=10.0
                )
                messages: List[Any] = []
                if system_prompt:
                    messages.append(SystemMessage(content=system_prompt))
                messages.append(HumanMessage(content=prompt))

                resp = llm.invoke(messages)
                return {
                    "content": str(resp.content),
                    "provider": "Groq",
                    "model": model_name or "llama-3.3-70b-versatile",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"Groq call failed, cascading to next provider: {e}")

        # 3. Try Google Gemini (OpenAI-compatible endpoint with direct REST fallback)
        if provider_info["gemini_available"]:
            try:
                from langchain_openai import ChatOpenAI
                from langchain_core.messages import SystemMessage, HumanMessage

                llm = ChatOpenAI(
                    model=model_name or os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
                    temperature=temperature,
                    api_key=SecretStr(self.gemini_key),
                    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                    timeout=4.0
                )
                messages: List[Any] = []
                if system_prompt:
                    messages.append(SystemMessage(content=system_prompt))
                messages.append(HumanMessage(content=prompt))

                resp = llm.invoke(messages)
                return {
                    "content": str(resp.content),
                    "provider": "Google Gemini",
                    "model": model_name or os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
                    "status": "success"
                }
            except Exception as e:
                err_str = str(e).lower()
                if "10013" in err_str or "forbidden by its access permissions" in err_str or "connection error" in err_str:
                    MedicalLLMGateway._network_blocked = True
                logger.warning(f"Google Gemini call via OpenAI endpoint failed: {e}. Trying direct REST API...")
                if MedicalLLMGateway._network_blocked:
                    pass
                else:
                    try:
                        with httpx.Client(timeout=4.0) as client:
                            target_model = model_name or os.getenv("GEMINI_MODEL", "gemini-flash-latest")
                            url = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={self.gemini_key}"
                            combined_text = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
                            payload = {
                                "contents": [{"parts": [{"text": combined_text}]}],
                                "generationConfig": {"temperature": temperature}
                            }
                            res = client.post(url, json=payload)
                            if res.status_code == 200:
                                data = res.json()
                                candidate_text = data["candidates"][0]["content"]["parts"][0]["text"]
                                return {
                                    "content": candidate_text,
                                    "provider": "Google Gemini (REST)",
                                    "model": target_model,
                                    "status": "success"
                                }
                    except Exception as ex2:
                        logger.warning(f"Google Gemini REST fallback failed, cascading: {ex2}")

        # 4. Try Ollama (Local)
        if provider_info["ollama_available"]:
            try:
                with httpx.Client(timeout=self.ollama_timeout) as client:
                    model_to_use = model_name or os.getenv("OLLAMA_MODEL", "")
                    if not model_to_use:
                        try:
                            tags_res = client.get(f"{self.ollama_url}/api/tags")
                            if tags_res.status_code == 200:
                                models = tags_res.json().get("models", [])
                                if models:
                                    model_to_use = models[0].get("name", "llama3.2")
                        except Exception:
                            pass
                    model_to_use = model_to_use or "llama3.2"

                    payload = {
                        "model": model_to_use,
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
                            "model": model_to_use,
                            "status": "success"
                        }
            except Exception as e:
                logger.warning(f"Ollama call failed: {e}")

        # 5. Local High-Fidelity Clinical Synthesis Fallback
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
        Multi-turn chat completion across active provider cascade (OpenAI, Groq, Gemini, Ollama, local fallback).
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
                    api_key=SecretStr(self.openai_key),
                    timeout=12.0
                )
                lc_messages: List[Any] = []
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
                    "content": str(resp.content),
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
                    api_key=SecretStr(self.groq_key),
                    base_url="https://api.groq.com/openai/v1",
                    timeout=12.0
                )
                lc_messages: List[Any] = []
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
                    "content": str(resp.content),
                    "provider": "Groq",
                    "model": model_name or "llama-3.3-70b-versatile",
                    "status": "success"
                }
            except Exception as e:
                logger.warning(f"Groq chat call failed, cascading: {e}")

        # 3. Try Google Gemini (OpenAI-compatible endpoint with direct REST fallback)
        if provider_info["gemini_available"]:
            try:
                from langchain_openai import ChatOpenAI
                from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

                llm = ChatOpenAI(
                    model=model_name or os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
                    temperature=temperature,
                    api_key=SecretStr(self.gemini_key),
                    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                    timeout=4.0
                )
                lc_messages: List[Any] = []
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
                    "content": str(resp.content),
                    "provider": "Google Gemini",
                    "model": model_name or os.getenv("GEMINI_MODEL", "gemini-flash-latest"),
                    "status": "success"
                }
            except Exception as e:
                err_str = str(e).lower()
                if "10013" in err_str or "forbidden by its access permissions" in err_str or "connection error" in err_str:
                    MedicalLLMGateway._network_blocked = True
                logger.warning(f"Google Gemini chat call via OpenAI endpoint failed: {e}. Trying direct REST API...")
                if MedicalLLMGateway._network_blocked:
                    pass
                else:
                    try:
                        with httpx.Client(timeout=4.0) as client:
                            target_model = model_name or os.getenv("GEMINI_MODEL", "gemini-flash-latest")
                            url = f"https://generativelanguage.googleapis.com/v1beta/models/{target_model}:generateContent?key={self.gemini_key}"
                            # Convert messages to Gemini contents structure
                            gemini_contents = []
                            for m in messages:
                                role = "model" if m.get("role") == "assistant" else "user"
                                gemini_contents.append({
                                    "role": role,
                                    "parts": [{"text": m.get("content", "")}]
                                })
                            payload = {
                                "contents": gemini_contents,
                                "generationConfig": {"temperature": temperature}
                            }
                            res = client.post(url, json=payload)
                            if res.status_code == 200:
                                data = res.json()
                                candidate_text = data["candidates"][0]["content"]["parts"][0]["text"]
                                return {
                                    "content": candidate_text,
                                    "provider": "Google Gemini (REST)",
                                    "model": target_model,
                                    "status": "success"
                                }
                    except Exception as ex2:
                        logger.warning(f"Google Gemini chat REST fallback failed, cascading: {ex2}")

        # 4. Try Ollama (Local Chat API)
        if provider_info["ollama_available"]:
            try:
                with httpx.Client(timeout=self.ollama_timeout) as client:
                    model_to_use = model_name or os.getenv("OLLAMA_MODEL", "")
                    if not model_to_use:
                        try:
                            tags_res = client.get(f"{self.ollama_url}/api/tags")
                            if tags_res.status_code == 200:
                                models = tags_res.json().get("models", [])
                                if models:
                                    model_to_use = models[0].get("name", "llama3.2")
                        except Exception:
                            pass
                    model_to_use = model_to_use or "llama3.2"

                    payload = {
                        "model": model_to_use,
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
                            "model": model_to_use,
                            "status": "success"
                        }
            except Exception as e:
                logger.warning(f"Ollama chat call failed: {e}")

        # 5. Fallback to Local High-Fidelity Multi-Turn Synthesis Engine
        return {
            "content": None,
            "provider": "AegisMed Local Clinical Synthesis Engine",
            "model": "rule-grounded-ebm-v2",
            "status": "fallback"
        }


# Singleton instance
llm_gateway = MedicalLLMGateway()

