"""
This module defines the Card model for the application.
"""

from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Card(Base):
    """
    Represents a card in the system.

    Attributes:
        id (int): The primary key of the card.
        text (str): The text content of the card.
        board_id (int): The foreign key referencing the board associated with the card.
    """
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    board_id = Column(Integer, ForeignKey('boards.id'))

    board = relationship("Board", back_populates="cards")
    tasks = relationship("Task", back_populates="card", cascade="all, delete")

    def task_ids(self):
        return [task.id for task in self.tasks]
