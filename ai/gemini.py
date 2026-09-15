"""Gemini REST API adapter for JARVIS."""

import os

import requests


DEFAULT_MODEL = "gemini-3.6-flash"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def generate_text(prompt: str) -> str:
    """Generate a text response from Gemini.

    Returns a useful local message when the API key is not configured instead
    of crashing the assistant during setup.
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        return "Gemini is not configured yet. Add GEMINI_API_KEY to your .env file."

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    url = f"{BASE_URL}/{model}:generateContent"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "systemInstruction": {
            "parts": [{
                "text": (
                    "You are JARVISFORME, a helpful personal AI assistant. "
                    "Be concise, practical, polite, and honest."
                )
            }]
        },
    }

    try:
        response = requests.post(
            url,
            headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
            json=payload,
            timeout=45,
        )
        response.raise_for_status()
        data = response.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return "Gemini returned no response. Please try again."

        parts = candidates[0].get("content", {}).get("parts", [])
        text = "".join(part.get("text", "") for part in parts).strip()
        return text or "Gemini returned an empty response."
    except requests.RequestException as exc:
        return f"Gemini connection error: {exc}"
    except (TypeError, ValueError, KeyError) as exc:
        return f"Gemini response error: {exc}"
