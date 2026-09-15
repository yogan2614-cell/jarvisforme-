"""High-level AI brain used by the command router."""

from ai.gemini import generate_text


def think(prompt: str) -> str:
    """Generate a JARVIS response for a user prompt."""
    return generate_text(prompt)
