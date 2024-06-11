"""
This module defines API endpoints related to card management using FastAPI and Pydantic.
"""

from typing import List

from app.dependencies import get_db
from app.services.card_service import (create_new_card, delete_existing_card,
                                       get_card_by_id, get_cards_by_board_id,
                                       move_existing_card,
                                       update_existing_card)
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

router = APIRouter()

class CardCreate(BaseModel):
    #Pydantic BaseModel for creating a new card.
    text: str
    board_id: int

class CardUpdate(BaseModel):
    #Pydantic BaseModel for updating an existing card.
    text: str

class CardResponse(BaseModel):
    #Pydantic BaseModel for the response data of a card.
    id: int
    text: str
    board_id: int

@router.post("/", response_model=CardResponse)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    #Endpoint to create a new card.
    return create_new_card(db, card.text, card.board_id)

@router.get("/{card_id}", response_model=CardResponse)
def read_card(card_id: int, db: Session = Depends(get_db)):
    #Endpoint to read details of a specific card.
    db_card = get_card_by_id(db, card_id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card

@router.get("/by_board/{board_id}", response_model=List[CardResponse])
def read_cards_by_board(board_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    #Endpoint to read cards associated with a board.
    return get_cards_by_board_id(db, board_id, skip, limit)

@router.patch("/{card_id}", response_model=CardResponse)
def update_card(card_id: int, card: CardUpdate, db: Session = Depends(get_db)):
    #Endpoint to update an existing card.
    db_card = get_card_by_id(db, card_id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return update_existing_card(db, card_id, card.text)

@router.delete("/{card_id}", response_model=CardResponse)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    #Endpoint to delete an existing card.
    db_card = get_card_by_id(db, card_id)
    if db_card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return delete_existing_card(db, card_id)
