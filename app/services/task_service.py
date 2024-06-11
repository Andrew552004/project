"""
This module provides services for managing tasks in the application.
"""

from sqlalchemy.orm import Session

from app.repositories.task_repository import (create_task, delete_task,
                                              get_task_by_id, move_task,
                                              update_task)


def create_task_service(db: Session, text: str, status: str, card_id: int):
    """
    Creates a new task in the database.

    Args:
        db (Session): Database session.
        text (str): Task text.
        status (str): Task status.
        card_id (int): ID of the card to which the task belongs.

    Returns:
        Task: The newly created task object.
    """
    return create_task(db, text, status, card_id)

def get_task_by_id_service(db: Session, task_id: int):
    """
    Retrieves a task by its ID from the database.

    Args:
        db (Session): Database session.
        task_id (int): ID of the task to retrieve.

    Returns:
        Task: The retrieved task object.
    """
    return get_task_by_id(db, task_id)

def update_task_service(db: Session, text: str, status: str, task_id: int):
    """
    Updates a task in the database.

    Args:
        db (Session): Database session.
        text (str): New task text.
        status (str): New task status.
        task_id (int): ID of the task to update.

    Returns:
        Task: The updated task object.
    """
    return update_task(db, text=text, status=status, task_id=task_id)

def delete_task_service(db: Session, task_id: int):
    """
    Deletes a task from the database.

    Args:
        db (Session): Database session.
        task_id (int): ID of the task to delete.

    Returns:
        None
    """
    return delete_task(db, task_id)

def move_task_service(db: Session, task_id: int, new_card_id: int):
    """
    Moves a task to a different card in the database.

    Args:
        db (Session): Database session.
        task_id (int): ID of the task to move.
        new_card_id (int): ID of the new card to which the task will be moved.

    Returns:
        Task: The moved task object.
    """
    return move_task(db, task_id, new_card_id)
