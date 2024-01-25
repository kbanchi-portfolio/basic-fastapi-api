from typing import Optional

from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    description: Optional[str] = Field(None, example="This is Description")


class Todo(TodoBase):
    id: int
    
    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    pass

class TodoCreateResponse(TodoCreate):
    id: int
    
    class Config:
        orm_mode = True