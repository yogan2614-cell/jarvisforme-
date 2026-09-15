"""Create JARVIS PostgreSQL tables."""

from database.connection import engine
from database.models import Base


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("JARVIS PostgreSQL tables are ready.")
