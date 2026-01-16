"""
Database initialization utilities.

Provides functions for creating database schema.

Usage:
    from app.db.init import init_db
    init_db()
"""

from app.db.database import get_engine, Base


def init_db() -> None:
    """
    Create all database tables defined in models.

    Uses SQLAlchemy's create_all which is safe to run multiple times -
    it only creates tables that don't exist.
    """
    # Import models to ensure they're registered with Base
    from app.db import models  # noqa: F401

    Base.metadata.create_all(bind=get_engine())
    print("Tables created")
