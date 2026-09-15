"""Repository helpers for JARVIS persistence."""

from sqlalchemy import select

from database.connection import SessionLocal
from database.models import Conversation, Memory


def save_conversation(role: str, content: str) -> None:
    """Persist one user or assistant message when PostgreSQL is configured."""
    session = SessionLocal()
    try:
        session.add(Conversation(role=role, content=content))
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()


def remember(key: str, value: str) -> None:
    """Create or update a durable memory."""
    session = SessionLocal()
    try:
        memory = session.scalar(select(Memory).where(Memory.key == key))
        if memory is None:
            memory = Memory(key=key, value=value)
            session.add(memory)
        else:
            memory.value = value
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()


def recall(key: str) -> str | None:
    """Return a remembered value, if present."""
    session = SessionLocal()
    try:
        memory = session.scalar(select(Memory).where(Memory.key == key))
        return memory.value if memory else None
    finally:
        session.close()
