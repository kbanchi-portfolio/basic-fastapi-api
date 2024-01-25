from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    description = Column(String(1024))