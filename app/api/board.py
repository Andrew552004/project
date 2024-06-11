"""
This module defines API endpoints related to board management using FastAPI and Pydantic.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.board_service import (create_new_board,
                                        delete_existing_board, get_all_boards,
                                        get_board_by_id, update_existing_board)

router = APIRouter()

class BoardCreate(BaseModel):
    #Pydantic BaseModel for creating a new board.
    title: str
class BoardUpdate(BaseModel):
    #Pydantic BaseModel for updating an existing board.
    title: str

class TaskResponse(BaseModel):
    """Pydantic BaseModel for the response data of a task."""
    id: int
    text: str
    status: str

class CardResponse(BaseModel):
    #Pydantic BaseModel for the response data of a card.
    id: int
    text: str
    tasks: List[TaskResponse] = []

class BoardResponse(BaseModel):
    #Pydantic BaseModel for the response data of a board.
    id: int
    title: str
    cards: List[CardResponse] = []

@router.post("/", response_model=BoardResponse)
def create_board(board: BoardCreate, db: Session = Depends(get_db)):
    #Endpoint to create a new board.
    return create_new_board(db, board.title)

@router.get("/{board_id}", response_model=BoardResponse)
def read_board(board_id: int, db: Session = Depends(get_db)):
    #Endpoint to read details of a specific board.
    db_board = get_board_by_id(db, board_id)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board

@router.get("/", response_model=List[BoardResponse])
def read_boards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    #Endpoint to read all boards.
    return get_all_boards(db, skip, limit)

@router.patch("/{board_id}", response_model=BoardResponse)
def update_board(board_id: int, board: BoardUpdate, db: Session = Depends(get_db)):
    #Endpoint to update an existing board.
    db_board = get_board_by_id(db, board_id)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return update_existing_board(db, board_id, board.title)

@router.delete("/{board_id}", response_model=BoardResponse)
def delete_board(board_id: int, db: Session = Depends(get_db)):
    #Endpoint to delete an existing board.
    db_board = get_board_by_id(db, board_id)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return delete_existing_board(db, board_id)