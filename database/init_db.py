"""Initialize JARVIS database tables."""

from database.connection import engine
from database.models import Base


def init_db() -> None:
    """Create all tables that do not already exist."""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("JARVIS database initialized.")
