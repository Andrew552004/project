"""
This module provides repository functions for user management in the application.
"""
from app.models.user import User
from sqlalchemy.orm import Session


def get_user_by_username(db: Session, username: str):
    """
    Retrieves a user by username from the database.

    Args:
        db (Session): Database session.
        username (str): Username of the user to retrieve.

    Returns:
        User: The retrieved user object.
    """
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: User):
    """
    Creates a new user in the database.

    Args:
        db (Session): Database session.
        user (User): User object to create.

    Returns:
        User: The created user object.
    """
    db.add(user)
    db.commit()
    db.refresh(user)
    return user