"""
This module sets up a PostgreSQL database engine using settings 
from the configuration. It also defines a function get_db() to obtain 
a SQLAlchemy database session. The session is created using the SessionLocal 
sessionmaker, and it is closed automatically after its use.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

# Constructing the database URL 
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOST}/{settings.POSTGRES_DB}"

# Creating the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# Creating a sessionmaker for creating new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """
    Function to get a database session.
    Returns:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()