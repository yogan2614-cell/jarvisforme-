"""AI brain abstraction.

The first version stays dependency-light and safely falls back when no AI
provider is configured. Provider integrations can be added without changing
the router or application entry point.
"""

import os


def think(prompt: str) -> str:
    """Return a response for a prompt.

    A provider can be enabled later by implementing the configured backend.
    For now this gives a deterministic local response instead of failing.
    """
    if os.getenv("GEMINI_API_KEY"):
        return "Gemini integration is configured but the provider adapter is not enabled yet."
    return f"I received: {prompt}"
