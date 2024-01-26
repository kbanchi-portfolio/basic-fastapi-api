from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

import schemas.todo as todo_schema
import cruds.todo as todo_cruds
from db import get_db

router = APIRouter()

@router.get("/todos", response_model=List[todo_schema.Todo])
async def list(db: Session = Depends(get_db)):
    # return [todo_schema.Todo(id=1, description="Sample")]
    return todo_cruds.get_todos(db)


@router.post("/todos", response_model=todo_schema.TodoCreateResponse)
async def create(todo: todo_schema.TodoCreate, db: Session = Depends(get_db)):
    # return todo_schema.TodoCreateResponse(id=1, **todo.dict())
    return todo_cruds.create_todo(db, todo)


@router.put("/todos/{todo_id}", response_model=todo_schema.TodoCreateResponse)
async def update(todo_id: int, todo_body: todo_schema.TodoCreate, db: Session = Depends(get_db)):
    # todo_schema.TodoCreateResponse(id=todo_id, **todo.dict())
    todo = todo_cruds.get_todo(db, todo_id=todo_id)
    if todo is None:
        return HTTPException(status_code=404, detail="Todo not found.")
    return todo_cruds.update_task(db, todo_body, original=todo)


@router.delete("/todos/{todo_id}", response_model=None)
async def delete(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_cruds.get_todo(db, todo_id=todo_id)
    if todo is None:
        return HTTPException(status_code=404, detail="Todo not found.")
    return todo_cruds.delete_task(db, original=todo)
