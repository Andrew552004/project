"""
This module provides services for managing cards in the application.
"""
from sqlalchemy.orm import Session

from app.models.card import Card
from app.repositories.card_repository import (create_card, delete_card,
                                              get_card, get_cards_by_board,
                                              move_card, update_card)


def create_new_card(db: Session, text: str, board_id: int):
    """
    Creates a new card in the database.

    Args:
        db (Session): Database session.
        text (str): Text content of the card.
        board_id (int): ID of the board to which the card belongs.

    Returns:
        Card: The newly created card object.
    """
    card = Card(text=text, board_id=board_id)
    return create_card(db, card)

def get_card_by_id(db: Session, card_id: int):
    """
    Retrieves a card by its ID from the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to retrieve.

    Returns:
        Card: The retrieved card object.
    """
    return get_card(db, card_id)

def get_cards_by_board_id(db: Session, board_id: int, skip: int = 0, limit: int = 10):
    """
    Retrieves cards belonging to a specific board.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board.
        skip (int): Number of records to skip (for pagination).
        limit (int): Maximum number of records to retrieve (for pagination).

    Returns:
        List[Card]: List of card objects.
    """
    return get_cards_by_board(db, board_id, skip, limit)

def update_existing_card(db: Session, card_id: int, text: str):
    """
    Updates an existing card in the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to update.
        text (str): New text content for the card.

    Returns:
        Card: The updated card object.
    """
    return update_card(db, card_id, text)

def delete_existing_card(db: Session, card_id: int):
    """
    Deletes an existing card from the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to delete.

    Returns:
        None
    """
    return delete_card(db, card_id)

def move_existing_card(db: Session, card_id: int, new_board_id: int):
    """
    Moves an existing card to a different board in the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to move.
        new_board_id (int): ID of the new board to which the card will be moved.

    Returns:
        Card: The moved card object.
    """
    return move_card(db, card_id, new_board_id)
