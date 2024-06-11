"""This module implements two API endpoints using FastAPI to handle user registration and login.
"""

from app.dependencies import get_db
from app.services.user_service import (authenticate_user, create_user_token,
                                       register_user)
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Creating an APIRouter instance.
router = APIRouter()

# Defining Pydantic models to validate request and response data.
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Endpoint for user registration.
@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Calling register_user function to register the user.
        registered_user = register_user(db, user.username, user.password)
        token = create_user_token(registered_user)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint for user login.
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Authenticating the user.
    authenticated_user = authenticate_user(db, user.username, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_user_token(authenticated_user)
    return {"access_token": token, "token_type": "bearer"}
