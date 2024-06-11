"""
This module defines the Board model for the application.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Board(Base):
    """
    Represents a board in the system.

    Attributes:
        id (int): The primary key of the board.
        title (str): The title of the board.
    """
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    cards = relationship("Card", back_populates="board", cascade="all, delete-orphan")
