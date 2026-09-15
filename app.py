"""JARVISFORME Phase 1 desktop/terminal entry point."""

import os

from dotenv import load_dotenv

from core.router import route_command
from voice.elevenlabs import synthesize


load_dotenv()


def main() -> None:
    name = os.getenv("JARVIS_NAME", "JARVIS").strip() or "JARVIS"
    print(f"{name} online. Type 'exit' to stop.")

    while True:
        try:
            command = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{name}: Goodbye.")
            break

        if not command:
            continue
        if command.lower() in {"exit", "quit", "bye"}:
            print(f"{name}: Goodbye.")
            break

        answer = route_command(command)
        print(f"{name}: {answer}")

        # Voice is optional. If ElevenLabs credentials are absent, JARVIS
        # remains fully usable in text mode.
        audio_path = synthesize(answer)
        if audio_path:
            print(f"{name}: Voice saved to {audio_path}")


if __name__ == "__main__":
    main()
