"""Simple command router for the Phase 1 assistant."""

from core.brain import think


def route_command(command: str) -> str:
    """Route a user command to the appropriate subsystem."""
    normalized = command.strip().lower()

    if normalized in {"hello", "hi", "hey"}:
        return "Hello! How can I help you?"
    if normalized in {"status", "system status"}:
        return "All core JARVIS modules are ready."

    return think(command)
