"""
Conversational Clinical Chat API Router for AegisMed.
Exposes endpoints for multi-turn dialogue, session history, and follow-up generation.
"""

from fastapi import APIRouter, HTTPException, status
from app.models.chat_schemas import ChatRequest, ChatResponse, ChatMessage
from app.services.chat_engine import chat_engine
from typing import List

router = APIRouter(prefix="/api/v1/chat", tags=["Conversational Clinical Chat Engine"])


@router.post("/message", response_model=ChatResponse, summary="Send a Message to the Clinical Chat Assistant")
async def send_chat_message_endpoint(payload: ChatRequest):
    """
    Primary multi-turn conversational chat endpoint:
    - Maintains conversational memory and resolves context across dialogue turns
    - Enforces non-blocking clinical acuity advisories for acute symptoms
    - Adapts response register to active audience (Patient Grade 6-8 vs Doctor Postgraduate)
    - Always explains the condition first before moving to practical solutions or GDMT
    - Generates 3 intelligent, context-aware follow-up suggestions
    """
    try:
        response = chat_engine.process_message(payload)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the chat message: {str(e)}"
        )


@router.get("/history/{conversation_id}", response_model=List[ChatMessage], summary="Retrieve Conversation History")
async def get_chat_history_endpoint(conversation_id: str):
    """Retrieves all message turns for a given conversation session."""
    return chat_engine.get_session_history(conversation_id)


@router.delete("/history/{conversation_id}", summary="Reset / Clear Conversation History")
async def clear_chat_history_endpoint(conversation_id: str):
    """Clears all turns and context for a given conversation session."""
    success = chat_engine.clear_session(conversation_id)
    return {"status": "cleared" if success else "not_found", "conversation_id": conversation_id}
