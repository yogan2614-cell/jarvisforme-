"""ElevenLabs text-to-speech adapter for JARVIS."""

import os
from pathlib import Path

import requests


API_URL = "https://api.elevenlabs.io/v1/text-to-speech"


def synthesize(text: str, output_path: str = "runtime/jarvis_reply.mp3") -> str | None:
    """Convert text to speech and save the returned MP3 locally.

    Returns the output path when successful, otherwise None. Audio playback is
    intentionally separate so JARVIS can run on machines without a media
    player installed.
    """
    api_key = os.getenv("ELEVENLABS_API_KEY", "").strip()
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "").strip()
    if not api_key or not voice_id:
        return None

    model_id = os.getenv("ELEVENLABS_MODEL", "eleven_multilingual_v2").strip()
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.post(
            f"{API_URL}/{voice_id}",
            headers={"xi-api-key": api_key, "Content-Type": "application/json"},
            params={"output_format": "mp3_44100_128"},
            json={"text": text, "model_id": model_id},
            timeout=60,
        )
        response.raise_for_status()
        target.write_bytes(response.content)
        return str(target)
    except requests.RequestException:
        return None
