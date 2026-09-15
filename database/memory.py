"""Simple persistence helpers for JARVIS memory and conversations."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import Conversation, Memory


def save_memory(session: Session, key: str, value: str) -> Memory:
    """Create a durable memory entry."""
    memory = Memory(key=key.strip(), value=value.strip())
    session.add(memory)
    session.commit()
    session.refresh(memory)
    return memory


def get_memories(session: Session, key: str | None = None) -> list[Memory]:
    """Return stored memories, optionally filtered by key."""
    statement = select(Memory).order_by(Memory.created_at.desc())
    if key:
        statement = statement.where(Memory.key == key.strip())
    return list(session.scalars(statement))


def save_message(session: Session, role: str, content: str) -> Conversation:
    """Persist one conversation message."""
    message = Conversation(role=role.strip(), content=content.strip())
    session.add(message)
    session.commit()
    session.refresh(message)
    return message
