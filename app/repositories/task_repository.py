"""
This module provides repository functions for task management in the application.
"""
from sqlalchemy.orm import Session

from app.models.task import Task


def create_task(db: Session, text: str, status: str, card_id: int):
    """
    Creates a new task in the database.

    Args:
        db (Session): Database session.
        text (str): Text of the task.
        status (str): Status of the task.
        card_id (int): ID of the card associated with the task.

    Returns:
        Task: The created task object.
    """
    task = Task(text=text, status=status, card_id=card_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int):
    """
    Retrieves a task by ID from the database.

    Args:
        db (Session): Database session.
        task_id (int): ID of the task to retrieve.

    Returns:
        Task: The retrieved task object.
    """
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, text: str, status: str, task_id: int):
    """
    Updates a task in the database.

    Args:
        db (Session): Database session.
        text (str): New text for the task.
        status (str): New status for the task.
        task_id (int): ID of the task to update.

    Returns:
        Task: The updated task object.
    """
    task = get_task_by_id(db, task_id)
    if task:
        task.text = text
        task.status = status
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    """
    Deletes a task from the database.

    Args:
        db (Session): Database session.
        task_id (int): ID of the task to delete.

    Returns:
        Task: The deleted task object.
    """
    task = get_task_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task

def move_task(db: Session, task_id: int, new_card_id: int):
    """
    Moves a task to a different card in the database.

    Args:
        db (Session): Database session.
        task_id (int): ID of the task to move.
        new_card_id (int): ID of the new card to move the task to.

    Returns:
        Task: The updated task object.
    """
    task = get_task_by_id(db, task_id)
    if task:
        task.card_id = new_card_id
        db.commit()
        db.refresh(task)
    return task
