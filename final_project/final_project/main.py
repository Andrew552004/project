"""
This module is the main entry point where web services are defined
to interact with all external users, including frontend clients

Authors: Andrés Vanegas, Sergio Sanabria
last update of this project: 7/06/2024"""

import os
from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
from dotenv import load_dotenv

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
class Register(BaseModel):
    username: str
    password: SecretStr

@app.post("/register")
async def register_user(register: Register):
    return {"message": "User registered successfully"}

# Function for login
class Login(BaseModel):
    username: str
    password: SecretStr

@app.post("/login")
def login(user_info: Login) -> bool:
    """This service lets authenticate an user using username and password."""
    # TODO make authentication
    return False

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
    return {"message": f"Card {card_id} deleted successfully from board {board_id}"}