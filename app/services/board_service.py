"""
This module provides services for managing boards in the application.
"""
from sqlalchemy.orm import Session

from app.models.board import Board
from app.repositories.board_repository import (create_board, delete_board,
                                               get_board, get_boards,
                                               update_board)


def create_new_board(db: Session, title: str):
    """
    Creates a new board in the database.

    Args:
        db (Session): Database session.
        title (str): Title of the new board.

    Returns:
        Board: The newly created board object.
    """
    board = Board(title=title)
    return create_board(db, board)

def get_board_by_id(db: Session, board_id: int):
    """
    Retrieves a board by its ID from the database.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to retrieve.

    Returns:
        Board: The retrieved board object.
    """
    return get_board(db, board_id)

def get_all_boards(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieves all boards from the database with optional pagination.

    Args:
        db (Session): Database session.
        skip (int): Number of records to skip (for pagination).
        limit (int): Maximum number of records to retrieve (for pagination).

    Returns:
        List[Board]: List of board objects.
    """
    return db.query(Board).offset(skip).limit(limit).all()

def update_existing_board(db: Session, board_id: int, title: str):
    """
    Updates an existing board in the database.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to update.
        title (str): New title for the board.

    Returns:
        Board: The updated board object.
    """
    return update_board(db, board_id, title)

def delete_existing_board(db: Session, board_id: int):
    """
    Deletes an existing board from the database.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to delete.

    Returns:
        None
    """
    return delete_board(db, board_id)
