from typing import List
from typing import Tuple
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result

import models.todo as todo_model
import schemas.todo as todo_schema

def create_todo(db: Session, todo_create: todo_schema.TodoCreate) -> todo_model.Todo:
    todo = todo_model.Todo(**todo_create.dict())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todos(db: Session) -> List[Tuple[int, str]]:
    result: Result = db.execute(
        select(
            todo_model.Todo
        )
    )
    return result.all()



def get_todo(db: Session, todo_id: int) -> Optional[todo_model.Todo]:
    result: Result = db.execute(
        select(
            todo_model.Todo
        ).filter(todo_model.Todo.id == todo_id)
    )
    todo: Optional[Tuple[todo_model.Todo]] = result.first()
    return todo[0] if todo is not None else None


def update_task(db: Session, todo_create: todo_schema.TodoCreate, original: todo_model.Todo) -> todo_model.Todo:
    original.description = todo_create.description
    db.add(original)
    db.commit()
    db.refresh(original)
    return original

def delete_task(db: Session, original: todo_model.Todo) -> None:
    db.delete(original)
    db.commit()
