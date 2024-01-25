from typing import List

from fastapi import APIRouter

import schemas.todo as todo_schema

router = APIRouter()

@router.get("/todos", response_model=List[todo_schema.Todo])
async def list():
    return [todo_schema.Todo(id=1, description="Sample")]

@router.post("/todos", response_model=todo_schema.TodoCreateResponse)
async def create(todo: todo_schema.TodoCreate):
    return todo_schema.TodoCreateResponse(id=1, **todo.dict())

@router.put("/todos/{todo_id}", response_model=todo_schema.TodoCreateResponse)
async def update(todo_id: int, todo: todo_schema.TodoCreate):
    todo_schema.TodoCreateResponse(id=todo_id, **todo.dict())

@router.delete("/todos/{todo_id}", response_model=None)
async def delete():
    return