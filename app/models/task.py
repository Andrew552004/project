"""
This module defines the Task model for the application.
"""
# app/models.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Task(Base):
    """
    Represents a task in the system.

    Attributes:
        id (int): The primary key of the task.
        text (str): The text content of the task.
        status (str): The status of the task.
        card_id (int): The foreign key referencing the card associated with the task.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    status = Column(String)
    card_id = Column(Integer, ForeignKey("cards.id"))

    card = relationship("Card", back_populates="tasks")
