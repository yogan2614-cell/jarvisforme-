"""PostgreSQL connection and session management."""

import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()

# Keep the assistant usable before PostgreSQL is configured locally.
engine = create_engine(DATABASE_URL, pool_pre_ping=True) if DATABASE_URL else None
SessionLocal = (
    sessionmaker(bind=engine, autoflush=False, autocommit=False)
    if engine is not None
    else None
)


def get_session() -> Generator[Session, None, None]:
    """Yield a database session and close it safely."""
    if SessionLocal is None:
        raise RuntimeError("DATABASE_URL is not configured.")

    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
