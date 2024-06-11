"""
This module provides repository functions for card management in the application.
"""

from app.models.card import Card
from sqlalchemy.orm import Session


def get_card(db: Session, card_id: int):
    """
    Retrieves a card by ID from the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to retrieve.

    Returns:
        Card: The retrieved card object.
    """
    return db.query(Card).filter(Card.id == card_id).first()

def get_cards_by_board(db: Session, board_id: int, skip: int = 0, limit: int = 10):
    """
    Retrieves cards by board ID from the database.

    Args:
        db (Session): Database session.
        board_id (int): ID of the board to retrieve cards for.
        skip (int): Number of records to skip.
        limit (int): Maximum number of records to retrieve.

    Returns:
        List[Card]: A list of card objects.
    """
    return db.query(Card).filter(Card.board_id == board_id).offset(skip).limit(limit).all()

def create_card(db: Session, card: Card):
    """
    Creates a new card in the database.

    Args:
        db (Session): Database session.
        card (Card): Card object to create.

    Returns:
        Card: The created card object.
    """
    db.add(card)
    db.commit()
    db.refresh(card)
    return card

def update_card(db: Session, card_id: int, text: str):
    """
    Updates a card in the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to update.
        text (str): New text for the card.

    Returns:
        Card: The updated card object.
    """
    card = get_card(db, card_id)
    if card:
        card.text = text
        db.commit()
        db.refresh(card)
    return card

def delete_card(db: Session, card_id: int):
    """
    Deletes a card from the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to delete.

    Returns:
        Card: The deleted card object.
    """
    card = get_card(db, card_id)
    if card:
        db.delete(card)
        db.commit()
    return card

def move_card(db: Session, card_id: int, new_board_id: int):
    """
    Moves a card to a different board in the database.

    Args:
        db (Session): Database session.
        card_id (int): ID of the card to move.
        new_board_id (int): ID of the new board to move the card to.

    Returns:
        Card: The updated card object.
    """
    card = get_card(db, card_id)
    if card:
        card.board_id = new_board_id
        db.commit()
        db.refresh(card)
    return card
