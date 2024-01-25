from fastapi import FastAPI

from routers import todo

api = FastAPI()
api.include_router(todo.router)

@api.get("/healthcheck")
async def healthcheck():
    return {"healthcheck": "ok"}