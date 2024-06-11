"""
This module initializes a FastAPI application, sets up routers for 
various API endpoints (users, boards, cards, and tasks), initializes 
the database, creates tables based on defined models, and integrates the 
routers into the FastAPI application instance with specific prefixes and tags 
for organization.
Authors: Andrés Vanegas, Sergio Sanabria
"""

from fastapi import FastAPI

from app.api.board import router as BoardRouter
from app.api.card import router as CardRouter
from app.api.task import router as TaskRouter
from app.api.user import router as UserRouter

from app.database import engine, init_db

from app.models.board import Base as BoardBase
from app.models.card import Base as CardBase
from app.models.user import Base as UserBase

app = FastAPI()

init_db()

# Creating database tables
UserBase.metadata.create_all(bind=engine)
BoardBase.metadata.create_all(bind=engine)
CardBase.metadata.create_all(bind=engine)

# Add routers to the FastAPI instance
app.include_router(UserRouter, prefix="/api/users", tags=["users"])
app.include_router(BoardRouter, prefix="/api/boards", tags=["boards"])
app.include_router(CardRouter, prefix="/api/cards", tags=["cards"])
app.include_router(TaskRouter, prefix="/api/tasks", tags=["tasks"])
