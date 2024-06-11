"""
This module is the main entry point where web services are defined
to interact with all external users, including frontend clients
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.task_service import (create_task_service,
                                       delete_task_service,
                                       get_task_by_id_service,
                                       move_task_service, update_task_service)

router = APIRouter()

# Pydantic model to validate request data for creating a task.
class TaskCreate(BaseModel):
    text: str
    status: str
    card_id: int

# Pydantic model to validate request data for updating a task.
class TaskUpdate(BaseModel):
    text: str
    status: str

# Pydantic model to define the response data format for tasks.
class TaskResponse(BaseModel):
    id: int
    text: str
    status: str

# Endpoint to create a new task.
@router.post("/", response_model=TaskResponse)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task.text, task.status, task.card_id)

# Endpoint to update an existing task.
@router.patch("/{task_id}", response_model=TaskResponse)
def update(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    # Retrieve the task from the database.
    db_task = get_task_by_id_service(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return update_task_service(db, text=task.text, status=task.status, task_id=task_id)

# Endpoint to delete a task.
@router.delete("/{task_id}", response_model=TaskResponse)
def delete(task_id: int, db: Session = Depends(get_db)):
    # Retrieve the task from the database.
    db_task = get_task_by_id_service(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return delete_task_service(db, task_id)

# Endpoint to move a task to a different card.
@router.patch("/move/{task_id}/{new_task_id}", response_model=TaskResponse)
def move(task_id: int, new_task_id: int, db: Session = Depends(get_db)):
    # Retrieve the task from the database.
    db_task = get_task_by_id_service(db, task_id)
    if db_task is None:
        # Raise an HTTPException if the task is not found.
        raise HTTPException(status_code=404, detail="task not found")
    # Call the service function to move the task to a different card in the database.
    return move_task_service(db, task_id, new_task_id)
