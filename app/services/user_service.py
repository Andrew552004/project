"""
This module provides functions for user registration, authentication, 
and token creation.
"""
from datetime import timedelta

from app.core.security import (create_access_token, get_password_hash,
                               verify_password)
from app.models.user import User
from app.repositories.user_repository import create_user, get_user_by_username
from sqlalchemy.orm import Session


def register_user(db: Session, username: str, password: str):
    """
    Registers a new user in the database.

    Args:
        db (Session): Database session.
        username (str): User's username.
        password (str): User's password.

    Returns:
        User: The newly created user object.
    Raises:
        ValueError: If the username is already registered.
    """
    user = get_user_by_username(db, username)
    if user:
        raise ValueError("Username already registered")
    hashed_password = get_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    return create_user(db, new_user)

def authenticate_user(db: Session, username: str, password: str):
    """
    Authenticates a user during login.

    Args:
        db (Session): Database session.
        username (str): User's username.
        password (str): User's password.

    Returns:
        User: The authenticated user if successful, None otherwise.
    """
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password):
        return None
    return user

def create_user_token(user: User):
    """
    Creates an access token for an authenticated user.

    Args:
        user (User): Authenticated user object.

    Returns:
        str: Access token.
    """
    access_token_expires = timedelta(minutes=30)
    return create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )