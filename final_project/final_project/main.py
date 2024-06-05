"""
This module is the main entry point where web services are defined
to interact with all external users, including frontend clients

Authors: Andrés Vanegas, Sergio Sanabria
last update: 4/06/2024

"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from passlib.hash import bcrypt


app = FastAPI(
    title="Trello Backend Project",
    version="0.1",
    description="This is a web API for consuming services for project management based on virtual boards.",
)


# Model for the user
class User(BaseModel):
    username: str
    password: str

# Dummy data base
db_users = {}

# Function for register a new user
@app.post("/register")
async def register(user: User):
    # Verify the existence of one user
    if user.username in db_users:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    # Hash of password before of keep
    hashed_password = bcrypt.hash(user.password)
    
    # simulation for keep the user in DB
    db_users[user.username] = hashed_password
    
    return {"message": "User registered successfully"}

# Function for login
@app.post("/login")
async def login(user: User):
    # Verify the existence of user
    if user.username not in db_users:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    # Verify the correct password
    if not bcrypt.verify(user.password, db_users[user.username]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    
    return {"message": "Login successful"}

#------------------------------------------------------------------------
@app.post("/boards/")
def create_board(name: str):
    # Logic to create a new board
    return {"message": f"Board '{name}' created successfully"}

# End point to retive a board information
@app.get("/boards/{board_id}/")
def get_board(board_id: int):
    # Here put the logic
    return {"message": f"Getting information for board with ID: {board_id}"}

# End point to create a new card in a specific list of a board
@app.post("/boards/{board_id}/lists/{list_id}/cards/")
def create_card(board_id: int, list_id: int, name: str):
    # Here put the logic 
    return {"message": f"Card '{name}' created successfully in list {list_id} of board {board_id}"}

# End point to move a card to a different list within the same board
@app.put("/boards/{board_id}/cards/{card_id}/move/")
def move_card(board_id: int, card_id: int, new_list_id: int):
    # Here put the logic 
    return {"message": f"Card {card_id} moved to list {new_list_id} of board {board_id}"}

# End point to get all cards in a specific list of a board
@app.get("/boards/{board_id}/lists/{list_id}/cards/")
def get_cards_in_list(board_id: int, list_id: int):
    # Here put the logic 
    return {"message": f"Getting all cards in list {list_id} of board {board_id}"}

# End point to delete a card from a board
@app.delete("/boards/{board_id}/cards/{card_id}/")
def delete_card(board_id: int, card_id: int):
    # Here put the logic 
    return {"message": f"Card {card_id} deleted successfully from board {board_id}"}
