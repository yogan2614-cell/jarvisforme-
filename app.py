"""JARVISFORME Phase 1 entry point."""

from core.router import route_command


def main() -> None:
    print("JARVISFORME online. Type 'exit' to stop.")
    while True:
        try:
            command = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nJARVIS: Goodbye.")
            break

        if not command:
            continue
        if command.lower() in {"exit", "quit", "bye"}:
            print("JARVIS: Goodbye.")
            break

        print(f"JARVIS: {route_command(command)}")


if __name__ == "__main__":
    main()
