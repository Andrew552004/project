"""
This module handles database setup by constructing the database URL, 
creating a PostgreSQL database engine, and defining a session factory. 
It also establishes a declarative base for defining models. The init_db() 
function initializes the database by creating tables based on defined models.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

# Constructing the database URL
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOST}/{settings.POSTGRES_DB}"

# Creating the database engine
engine = create_engine(DATABASE_URL)

# Creating a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating a declarative base for models
Base = declarative_base()

def init_db():
    """
    Initializes the database by creating all tables based on the defined models.
    """ 
    from app.models.board import Board
    from app.models.card import Card
    from app.models.task import Task
    from app.models.user import User

    # Creating all tables in the database
    Base.metadata.create_all(bind=engine)
