"use client";

import React, { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { ChatMessage, ChatResponse, EmergencyTriageAlert } from "@/lib/types";
import { sendChatMessage, clearChatHistory } from "@/lib/api";
import {
  MessageSquare,
  X,
  Send,
  Trash2,
  Sparkles,
  HeartHandshake,
  Stethoscope,
  AlertTriangle,
  RotateCcw,
  CheckCircle2,
  ChevronDown,
  Info,
  ShieldCheck,
  Bot,
  User,
  Lightbulb
} from "lucide-react";

interface ChatDrawerProps {
  initialAudience?: "patient" | "doctor";
}

export function ChatDrawer({ initialAudience = "patient" }: ChatDrawerProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [audience, setAudience] = useState<"patient" | "doctor">(initialAudience);
  const [conversationId, setConversationId] = useState<string>("");
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [activeCondition, setActiveCondition] = useState<string | null>(null);
  const [suggestedFollowups, setSuggestedFollowups] = useState<string[]>([
    "What are the best lifestyle changes for high blood pressure?",
    "How does type 2 diabetes affect the body?",
    "What is the recommended inhaler approach for asthma?"
  ]);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Auto-scroll to bottom of messages
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (isOpen) {
      scrollToBottom();
      setTimeout(() => inputRef.current?.focus(), 150);
    }
  }, [messages, isOpen]);

  // Initial welcome message if empty
  useEffect(() => {
    if (messages.length === 0) {
      setMessages([
        {
          role: "assistant",
          content:
            audience === "patient"
              ? "### 1. Understanding How I Can Help You\n\nHello! I am **AegisMed**, your personal health assistant. I can explain any medical condition, medication, or symptom in simple everyday language using relatable analogies and practical solutions.\n\nWhat health question can I help you understand today?"
              : "### 1. Clinical Dialogue Initialized\n\nAegisMed multi-turn clinical chat engine initialized in **Clinician Register**. Grounded in peer-reviewed Oxford CEBM literature, GDMT titration regimens, and organ clearance cutoffs.\n\nPlease enter a clinical inquiry, guideline investigation, or pharmacotherapy query.",
          audience: audience,
          timestamp: new Date().toISOString()
        }
      ]);
    }
  }, [audience, messages.length]);

  const handleSend = async (messageText?: string) => {
    const textToSend = (messageText || inputMessage).trim();
    if (!textToSend || isLoading) return;

    setInputMessage("");
    setIsLoading(true);

    // Optimistically append user message
    const userMsg: ChatMessage = {
      role: "user",
      content: textToSend,
      audience: audience,
      timestamp: new Date().toISOString()
    };

    const newHistory = [...messages, userMsg];
    setMessages(newHistory);

    try {
      const response: ChatResponse = await sendChatMessage({
        message: textToSend,
        conversation_id: conversationId || undefined,
        audience: audience,
        history: newHistory
      });

      if (response.conversation_id && !conversationId) {
        setConversationId(response.conversation_id);
      }

      if (response.active_condition) {
        setActiveCondition(response.active_condition);
      }

      if (response.suggested_followups && response.suggested_followups.length > 0) {
        setSuggestedFollowups(response.suggested_followups);
      }

      const assistantMsg: ChatMessage = {
        role: "assistant",
        content: response.message,
        audience: response.audience,
        citations: response.citations,
        triage_alert: response.triage_alert,
        timestamp: new Date().toISOString()
      };

      setMessages((prev) => [...prev, assistantMsg]);
    } catch (error) {
      console.error("Chat error:", error);
      const errorMsg: ChatMessage = {
        role: "assistant",
        content:
          "⚠️ I had difficulty connecting to the clinical engine. Please ensure the backend is running and try your question again.",
        audience: audience,
        timestamp: new Date().toISOString()
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearHistory = async () => {
    if (conversationId) {
      try {
        await clearChatHistory(conversationId);
      } catch (e) {
        console.warn("Failed to clear remote session:", e);
      }
    }
    setConversationId("");
    setActiveCondition(null);
    setMessages([]);
  };

  const toggleAudience = () => {
    const nextAudience = audience === "patient" ? "doctor" : "patient";
    setAudience(nextAudience);
  };

  return (
    <>
      {/* Floating Trigger Button in Bottom Right */}
      {!isOpen && (
        <button
          type="button"
          onClick={() => setIsOpen(true)}
          className="fixed bottom-6 right-6 z-50 flex items-center gap-2.5 px-4 sm:px-5 py-3.5 rounded-full bg-gradient-to-r from-indigo-600 via-blue-600 to-teal-600 text-white font-semibold text-sm shadow-xl shadow-indigo-500/30 hover:shadow-indigo-500/50 hover:scale-105 active:scale-95 transition-all duration-300 border border-white/20 group cursor-pointer"
          title="Open AegisMed Clinical Chat Assistant"
        >
          <div className="relative">
            <Bot className="w-5 h-5 text-white animate-pulse" />
            <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-400 rounded-full ring-2 ring-indigo-700" />
          </div>
          <span className="tracking-wide">Ask Health Assistant</span>
        </button>
      )}

      {/* Floating Interactive Chat Drawer / Modal */}
      {isOpen && (
        <div className="fixed bottom-4 sm:bottom-6 right-4 sm:right-6 z-50 w-[calc(100vw-2rem)] sm:w-[460px] h-[640px] max-h-[calc(100vh-2rem)] bg-white rounded-3xl shadow-2xl border border-slate-200/90 flex flex-col overflow-hidden animate-fade-in backdrop-blur-xl">
          {/* Header Bar */}
          <div className="p-4 bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white flex items-center justify-between border-b border-indigo-500/20 shadow-sm shrink-0">
            <div className="flex items-center gap-2.5">
              <div className="p-2 bg-indigo-600/80 rounded-xl text-white shadow-xs">
                <Bot className="w-4 h-4" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h3 className="font-bold text-sm tracking-tight text-white">
                    AegisMed Assistant
                  </h3>
                  <span className="flex items-center gap-1 text-[10px] font-semibold bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded-full border border-emerald-500/30">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                    Live RAG
                  </span>
                </div>
                <p className="text-[11px] text-slate-400">
                  {audience === "patient" ? "Patient Mode (Plain English)" : "Doctor Mode (Postgraduate EBM)"}
                </p>
              </div>
            </div>

            <div className="flex items-center gap-1.5">
              {/* Audience Register Toggle */}
              <button
                type="button"
                onClick={toggleAudience}
                className={`flex items-center gap-1 px-2.5 py-1 rounded-lg text-xs font-semibold border transition-all ${
                  audience === "patient"
                    ? "bg-indigo-600/80 border-indigo-400/40 text-white hover:bg-indigo-500"
                    : "bg-teal-600/80 border-teal-400/40 text-white hover:bg-teal-500"
                }`}
                title={`Switch to ${audience === "patient" ? "Doctor" : "Patient"} perspective`}
              >
                {audience === "patient" ? (
                  <>
                    <HeartHandshake className="w-3.5 h-3.5" />
                    <span>Patient</span>
                  </>
                ) : (
                  <>
                    <Stethoscope className="w-3.5 h-3.5" />
                    <span>Doctor</span>
                  </>
                )}
              </button>

              {/* Clear History Button */}
              <button
                type="button"
                onClick={handleClearHistory}
                className="p-1.5 text-slate-400 hover:text-rose-400 rounded-lg hover:bg-white/10 transition-colors"
                title="Clear conversation history"
              >
                <Trash2 className="w-4 h-4" />
              </button>

              {/* Close Button */}
              <button
                type="button"
                onClick={() => setIsOpen(false)}
                className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors"
                title="Minimize chat"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Active Condition Banner if resolved */}
          {activeCondition && (
            <div className="px-4 py-2 bg-indigo-50/90 border-b border-indigo-100/80 flex items-center justify-between text-xs text-indigo-900 shrink-0">
              <span className="flex items-center gap-1.5 font-medium truncate">
                <Stethoscope className="w-3.5 h-3.5 text-indigo-600 shrink-0" />
                <span>Active Clinical Topic: <strong>{activeCondition}</strong></span>
              </span>
              <span className="text-[10px] text-indigo-500 font-semibold uppercase tracking-wider shrink-0">
                Grounding Active
              </span>
            </div>
          )}

          {/* Message List Area */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-slate-50/60">
            {messages.map((msg, index) => {
              const isUser = msg.role === "user";
              return (
                <div
                  key={index}
                  className={`flex gap-2.5 ${isUser ? "justify-end" : "justify-start"} animate-fade-in`}
                >
                  {!isUser && (
                    <div className="w-7 h-7 rounded-xl bg-gradient-to-tr from-indigo-600 to-blue-500 text-white flex items-center justify-center shrink-0 shadow-xs mt-0.5">
                      <Bot className="w-4 h-4" />
                    </div>
                  )}

                  <div
                    className={`max-w-[85%] rounded-2xl p-3.5 sm:p-4 text-sm leading-relaxed shadow-xs ${
                      isUser
                        ? "bg-gradient-to-r from-indigo-600 to-blue-600 text-white rounded-tr-none"
                        : "bg-white text-slate-800 border border-slate-200/80 rounded-tl-none"
                    }`}
                  >
                    {/* Non-blocking triage alert in message if present */}
                    {msg.triage_alert && (
                      <div className="mb-3 p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-rose-900 text-xs">
                        <div className="flex items-center gap-1.5 font-bold mb-1">
                          <AlertTriangle className="w-3.5 h-3.5 text-rose-600" />
                          <span>{msg.triage_alert.headline}</span>
                        </div>
                        <p className="text-[11px] leading-relaxed text-rose-800">
                          {msg.triage_alert.critical_guidance}
                        </p>
                      </div>
                    )}

                    {isUser ? (
                      <p className="whitespace-pre-wrap">{msg.content}</p>
                    ) : (
                      <div className="prose prose-sm max-w-none prose-slate prose-headings:font-bold prose-headings:text-slate-900 prose-headings:text-sm prose-p:my-1.5 prose-ul:my-1.5 prose-li:my-0.5">
                        <ReactMarkdown remarkPlugins={[remarkGfm]}>
                          {msg.content}
                        </ReactMarkdown>
                      </div>
                    )}

                    {msg.timestamp && (
                      <div
                        className={`text-[10px] mt-2 text-right ${
                          isUser ? "text-indigo-200" : "text-slate-400"
                        }`}
                      >
                        {new Date(msg.timestamp).toLocaleTimeString([], {
                          hour: "2-digit",
                          minute: "2-digit"
                        })}
                      </div>
                    )}
                  </div>

                  {isUser && (
                    <div className="w-7 h-7 rounded-xl bg-slate-700 text-white flex items-center justify-center shrink-0 shadow-xs mt-0.5">
                      <User className="w-4 h-4" />
                    </div>
                  )}
                </div>
              );
            })}

            {/* Loading indicator */}
            {isLoading && (
              <div className="flex gap-2.5 justify-start animate-fade-in">
                <div className="w-7 h-7 rounded-xl bg-gradient-to-tr from-indigo-600 to-blue-500 text-white flex items-center justify-center shrink-0 shadow-xs">
                  <Bot className="w-4 h-4" />
                </div>
                <div className="bg-white border border-slate-200 rounded-2xl rounded-tl-none p-3.5 shadow-xs flex items-center gap-2 text-slate-500 text-xs font-medium">
                  <div className="flex items-center gap-1">
                    <span className="w-2 h-2 rounded-full bg-indigo-600 animate-bounce" />
                    <span className="w-2 h-2 rounded-full bg-indigo-600 animate-bounce [animation-delay:0.2s]" />
                    <span className="w-2 h-2 rounded-full bg-indigo-600 animate-bounce [animation-delay:0.4s]" />
                  </div>
                  <span>Synthesizing evidence-based response...</span>
                </div>
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>

          {/* Suggested Follow-up Chips */}
          {suggestedFollowups.length > 0 && !isLoading && (
            <div className="px-3 pt-2 pb-1 bg-white border-t border-slate-100 flex items-center gap-1.5 overflow-x-auto no-scrollbar shrink-0">
              <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider pl-1 shrink-0">
                Suggested:
              </span>
              {suggestedFollowups.map((followup, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => handleSend(followup)}
                  className="px-2.5 py-1 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs rounded-full border border-indigo-200/80 transition-colors whitespace-nowrap shrink-0 cursor-pointer"
                >
                  {followup}
                </button>
              ))}
            </div>
          )}

          {/* Message Input Bar */}
          <div className="p-3 bg-white border-t border-slate-200/80 shrink-0">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSend();
              }}
              className="flex items-center gap-2"
            >
              <input
                ref={inputRef}
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder={
                  audience === "patient"
                    ? "Ask a follow-up or health question..."
                    : "Enter clinical query or follow-up protocol..."
                }
                disabled={isLoading}
                className="flex-1 px-4 py-2.5 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all bg-slate-50/50"
              />
              <button
                type="submit"
                disabled={!inputMessage.trim() || isLoading}
                className="p-2.5 rounded-xl bg-indigo-600 text-white hover:bg-indigo-500 disabled:opacity-40 disabled:cursor-not-allowed shadow-sm transition-all cursor-pointer"
                title="Send Message"
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
            <p className="text-[10px] text-slate-400 text-center mt-1.5">
              Evidence-grounded clinical navigator • Not a substitute for in-person diagnosis
            </p>
          </div>
        </div>
      )}
    </>
  );
}
