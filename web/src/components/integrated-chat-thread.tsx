"use client";

import React, { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { ChatMessage, ChatResponse, SearchResponse, UserMode } from "@/lib/types";
import { sendChatMessage } from "@/lib/api";
import {
  MessageSquare,
  Send,
  Sparkles,
  Bot,
  User,
  AlertTriangle,
  RefreshCw,
  HelpCircle,
  Stethoscope,
  HeartHandshake,
  ChevronRight,
  ShieldCheck,
  PlusCircle,
  Lightbulb
} from "lucide-react";

interface IntegratedChatThreadProps {
  initialTopic: string;
  mode: UserMode;
  response: SearchResponse;
  activeCitation: number | null;
  onSelectCitation: (index: number) => void;
}

export function IntegratedChatThread({
  initialTopic,
  mode,
  response,
  activeCitation,
  onSelectCitation
}: IntegratedChatThreadProps) {
  const [conversationId, setConversationId] = useState<string>("");
  const [followupTurns, setFollowupTurns] = useState<ChatMessage[]>([]);
  const [inputVal, setInputVal] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  // Audience string mapping
  const audience = mode === "professional" ? "doctor" : "patient";

  // Dynamic initial follow-up chips based on topic and register
  const defaultFollowups = React.useMemo(() => {
    return audience === "patient"
      ? [
          `Can you explain what happens inside the body in even simpler terms?`,
          `What are the most common side effects of treatments for this?`,
          `What specific questions should I ask my doctor about this?`,
          `What daily foods or lifestyle habits help the most?`
        ]
      : [
          `What are the guideline-directed titration intervals and target doses?`,
          `What are the specific eGFR and hepatic clearance cutoffs?`,
          `What did landmark Phase 3 trials establish for composite endpoints?`,
          `What are the critical drug-drug interactions and contraindications?`
        ];
  }, [audience]);

  const [quickChips, setQuickChips] = useState<string[]>(defaultFollowups);

  // Reset or update when primary topic/mode changes
  useEffect(() => {
    setFollowupTurns([]);
    setConversationId("");
    setQuickChips(defaultFollowups);
  }, [initialTopic, mode, defaultFollowups]);

  // Helper to inject interactive citation badges into text nodes
  const renderInlineCitations = (content: string) => {
    const parts = content.split(/(\[\d+(?:,\s*\d+)*\])/g);
    return parts.map((part, index) => {
      const match = part.match(/^\[(\d+(?:,\s*\d+)*)\]$/);
      if (match) {
        const citationIndices = match[1].split(",").map((s) => parseInt(s.trim(), 10));
        return (
          <span key={index} className="inline-flex gap-1 mx-1 align-baseline">
            {citationIndices.map((citIdx) => (
              <button
                key={citIdx}
                type="button"
                onClick={() => onSelectCitation(citIdx)}
                className={`px-2 py-0.5 rounded-full text-xs font-semibold transition-all ${
                  activeCitation === citIdx
                    ? "bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-300"
                    : "bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200"
                }`}
                title={`View Verified Reference [${citIdx}]`}
              >
                [{citIdx}]
              </button>
            ))}
          </span>
        );
      }
      return <span key={index}>{part}</span>;
    });
  };

  const handleSend = async (messageText?: string) => {
    const queryText = (messageText || inputVal).trim();
    if (!queryText || isLoading) return;

    setInputVal("");
    setIsLoading(true);

    const userMessage: ChatMessage = {
      role: "user",
      content: queryText,
      audience: audience,
      timestamp: new Date().toISOString()
    };

    // Prepend initial synthesis context if this is the first follow-up turn
    const historyPayload: ChatMessage[] = [];
    if (followupTurns.length === 0 && response.answer) {
      historyPayload.push({
        role: "user",
        content: initialTopic,
        audience: audience
      });
      historyPayload.push({
        role: "assistant",
        content: response.answer,
        audience: audience
      });
    }
    historyPayload.push(...followupTurns, userMessage);

    setFollowupTurns((prev) => [...prev, userMessage]);

    try {
      const res: ChatResponse = await sendChatMessage({
        message: queryText,
        conversation_id: conversationId || undefined,
        audience: audience,
        history: historyPayload,
        active_condition: initialTopic || response.query || undefined
      });

      if (res.conversation_id && !conversationId) {
        setConversationId(res.conversation_id);
      }

      if (res.suggested_followups && res.suggested_followups.length > 0) {
        setQuickChips(res.suggested_followups);
      }

      const assistantMsg: ChatMessage = {
        role: "assistant",
        content: res.message,
        audience: res.audience,
        citations: res.citations,
        triage_alert: res.triage_alert,
        timestamp: new Date().toISOString()
      };

      setFollowupTurns((prev) => [...prev, assistantMsg]);
    } catch (err) {
      console.error("Integrated follow-up chat error:", err);
      setFollowupTurns((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "⚠️ I had trouble connecting with the follow-up clinical engine. Please try asking your question again.",
          audience: audience,
          timestamp: new Date().toISOString()
        }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="mt-8 border border-slate-200/90 rounded-3xl bg-white shadow-sm overflow-hidden animate-fade-in transition-all">
      {/* Header Banner */}
      <div className="p-5 sm:p-6 bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-2xl bg-indigo-600/90 text-white shadow-sm">
            <MessageSquare className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base sm:text-lg font-bold tracking-tight text-white">
                Conversational Follow-up & Deep Dive
              </h3>
              <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 flex items-center gap-1">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                Context-Aware Assistant
              </span>
            </div>
            <p className="text-xs text-slate-300 mt-0.5">
              Ask follow-up questions, request deeper details, check interactions, or clarify next steps.
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 shrink-0">
          <span className="text-xs px-3 py-1 rounded-xl bg-white/10 text-slate-200 font-medium border border-white/10 flex items-center gap-1.5">
            {audience === "patient" ? (
              <>
                <HeartHandshake className="w-3.5 h-3.5 text-indigo-400" />
                <span>Patient Register</span>
              </>
            ) : (
              <>
                <Stethoscope className="w-3.5 h-3.5 text-teal-400" />
                <span>Doctor Register</span>
              </>
            )}
          </span>
        </div>
      </div>

      {/* Quick Suggestion Chips */}
      <div className="p-4 sm:p-5 bg-indigo-50/50 border-b border-indigo-100/70">
        <div className="flex items-center gap-1.5 mb-2.5 text-xs font-bold text-slate-500 uppercase tracking-wider">
          <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
          <span>Ask More Details / Suggested Follow-up Questions:</span>
        </div>
        <div className="flex flex-wrap gap-2">
          {quickChips.map((chip, idx) => (
            <button
              key={idx}
              type="button"
              disabled={isLoading}
              onClick={() => handleSend(chip)}
              className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-white hover:bg-indigo-50/80 active:bg-indigo-100 border border-slate-200 hover:border-indigo-300 text-xs sm:text-[13px] text-slate-700 hover:text-indigo-900 font-medium transition-all shadow-2xs hover:shadow-xs group cursor-pointer disabled:opacity-50 text-left"
            >
              <Lightbulb className="w-3.5 h-3.5 text-amber-500 group-hover:scale-110 transition-transform shrink-0" />
              <span>{chip}</span>
              <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-indigo-600 transition-colors shrink-0" />
            </button>
          ))}
        </div>
      </div>

      {/* Render Follow-up Message Turns if any */}
      {followupTurns.length > 0 && (
        <div className="p-5 sm:p-6 space-y-5 bg-slate-50/50 border-b border-slate-200/80">
          {followupTurns.map((turn, i) => {
            const isUser = turn.role === "user";
            return (
              <div
                key={i}
                className={`flex gap-3 ${isUser ? "justify-end" : "justify-start"} animate-fade-in`}
              >
                {!isUser && (
                  <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-indigo-600 to-blue-500 text-white flex items-center justify-center shrink-0 shadow-xs mt-1">
                    <Bot className="w-4 h-4" />
                  </div>
                )}

                <div
                  className={`max-w-[90%] sm:max-w-[80%] rounded-2xl p-4 sm:p-5 text-sm sm:text-base leading-relaxed shadow-xs ${
                    isUser
                      ? "bg-gradient-to-r from-indigo-600 to-blue-600 text-white rounded-tr-none font-medium"
                      : "bg-white text-slate-800 border border-slate-200/90 rounded-tl-none"
                  }`}
                >
                  {/* Non-blocking triage advisory if present */}
                  {turn.triage_alert && (
                    <div className="mb-3.5 p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-900 text-xs sm:text-sm">
                      <div className="flex items-center gap-2 font-bold mb-1">
                        <AlertTriangle className="w-4 h-4 text-rose-600" />
                        <span>{turn.triage_alert.headline}</span>
                      </div>
                      <p className="text-xs text-rose-800 leading-relaxed">
                        {turn.triage_alert.critical_guidance}
                      </p>
                    </div>
                  )}

                  {isUser ? (
                    <p className="whitespace-pre-wrap">{turn.content}</p>
                  ) : (
                    <div className="prose prose-sm sm:prose-base max-w-none prose-slate prose-headings:font-bold prose-headings:text-slate-900 prose-headings:text-base prose-p:my-2 prose-ul:my-2 prose-li:my-0.5">
                      <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        components={{
                          p: ({ children }) => {
                            if (typeof children === "string") {
                              return <p className="mb-3 leading-relaxed">{renderInlineCitations(children)}</p>;
                            }
                            return <div className="mb-3 leading-relaxed">{children}</div>;
                          }
                        }}
                      >
                        {turn.content}
                      </ReactMarkdown>
                    </div>
                  )}

                  {turn.timestamp && (
                    <div
                      className={`text-[10px] mt-2.5 text-right ${
                        isUser ? "text-indigo-200" : "text-slate-400"
                      }`}
                    >
                      {new Date(turn.timestamp).toLocaleTimeString([], {
                        hour: "2-digit",
                        minute: "2-digit"
                      })}
                    </div>
                  )}
                </div>

                {isUser && (
                  <div className="w-8 h-8 rounded-xl bg-slate-700 text-white flex items-center justify-center shrink-0 shadow-xs mt-1">
                    <User className="w-4 h-4" />
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* Loading Indicator */}
      {isLoading && (
        <div className="p-4 sm:p-5 bg-slate-50 flex items-center gap-3 border-b border-slate-200 text-slate-600 text-sm animate-fade-in">
          <div className="w-7 h-7 rounded-xl bg-indigo-600 text-white flex items-center justify-center shrink-0">
            <RefreshCw className="w-4 h-4 animate-spin" />
          </div>
          <div className="flex items-center gap-2 font-medium">
            <span>Consulting clinical evidence and generating follow-up response...</span>
            <span className="flex gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: "0ms" }} />
              <span className="w-1.5 h-1.5 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: "150ms" }} />
              <span className="w-1.5 h-1.5 rounded-full bg-indigo-600 animate-bounce" style={{ animationDelay: "300ms" }} />
            </span>
          </div>
        </div>
      )}

      {/* Follow-up Question Input Bar */}
      <div className="p-4 sm:p-5 bg-white">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend();
          }}
          className="flex items-center gap-2.5"
        >
          <input
            type="text"
            value={inputVal}
            onChange={(e) => setInputVal(e.target.value)}
            disabled={isLoading}
            placeholder={
              audience === "patient"
                ? "Ask a follow-up, request simpler words, or ask about another symptom..."
                : "Ask for deeper clinical details, drug titration protocols, or trial subgroups..."
            }
            className="flex-1 px-4 py-3 bg-slate-50 border border-slate-200 rounded-2xl text-sm sm:text-base focus:outline-none focus:ring-3 focus:ring-indigo-100 focus:border-indigo-600 transition-all text-slate-800 placeholder:text-slate-400"
          />
          <button
            type="submit"
            disabled={!inputVal.trim() || isLoading}
            className="px-5 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-700 active:scale-95 disabled:opacity-40 disabled:cursor-not-allowed text-white font-semibold text-sm transition-all shadow-xs flex items-center gap-2 shrink-0 cursor-pointer"
          >
            <Send className="w-4 h-4" />
            <span className="hidden sm:inline">Ask Follow-up</span>
          </button>
        </form>

        <p className="text-[11px] text-slate-400 mt-2 text-center">
          💡 The assistant retains full context of <strong>{initialTopic}</strong> for all follow-up inquiries.
        </p>
      </div>
    </div>
  );
}
