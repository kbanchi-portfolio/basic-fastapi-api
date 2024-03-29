from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

# ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

# async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
# )


DB_URL = "sqlite:///./sqlite.db"
engine = create_engine(DB_URL, echo=True)
session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=Session
)

Base = declarative_base()


# async def get_db():
#     async with async_session() as session:
#         yield session

def get_db():
    with session() as s:
        yield s