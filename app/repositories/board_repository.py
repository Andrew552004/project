"""
This module provides repository functions for board management in the application.
"""

from sqlalchemy.orm import Session, joinedload

from app.models.board import Board


def get_board(db: Session, board_id: int):
    """
    Retrieves a board by ID from the database with its associated cards and tasks.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to retrieve.

    Returns:
        Board: The retrieved board object.
    """
    return (
        db.query(Board)
        .filter(Board.id == board_id)
        .options(joinedload(Board.cards).joinedload(Card.tasks))
        .first()
    )

def get_boards(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieves multiple boards from the database with their associated cards and tasks.

    Args:
        db (Session): Database session.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.

    Returns:
        List[Board]: A list of board objects.
    """
    return (
        db.query(Board)
        .offset(skip)
        .limit(limit)
        .options(joinedload(Board.cards).joinedload(Card.tasks))
        .all()
    )

def create_board(db: Session, board: Board):
    """
    Creates a new board in the database.

    Args:
        db (Session): Database session.
        board (Board): Board object to create.

    Returns:
        Board: The created board object.
    """
    db.add(board)
    db.commit()
    db.refresh(board)
    return board

def update_board(db: Session, board_id: int, title: str):
    """
    Updates a board in the database.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to update.
        title (str): New title for the board.

    Returns:
        Board: The updated board object.
    """
    board = get_board(db, board_id)
    if board:
        board.title = title
        db.commit()
        db.refresh(board)
    return board

def delete_board(db: Session, board_id: int):
    """
    Deletes a board from the database.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to delete.

    Returns:
        Board: The deleted board object.
    """
    board = get_board(db, board_id)
    if board:
        db.delete(board)
        db.commit()
    return board
