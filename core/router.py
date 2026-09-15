"""Command router for the JARVIS assistant."""

import os

from core.brain import think


def _save_message(role: str, content: str) -> None:
    """Persist a message when PostgreSQL is configured."""
    if not os.getenv("DATABASE_URL", "").strip():
        return

    try:
        from database.repository import save_conversation

        save_conversation(role, content)
    except Exception:
        # Database failures must not stop the assistant from answering.
        pass


def route_command(command: str) -> str:
    """Route a user command and persist the conversation when possible."""
    normalized = command.strip().lower()
    _save_message("user", command)

    if normalized in {"hello", "hi", "hey"}:
        answer = "Hello! How can I help you?"
    elif normalized in {"status", "system status"}:
        answer = "All core JARVIS modules are ready."
    else:
        answer = think(command)

    _save_message("assistant", answer)
    return answer
