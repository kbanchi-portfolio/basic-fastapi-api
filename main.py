from fastapi import FastAPI

api = FastAPI()

@api.get("/healthcheck")
async def healthcheck():
    return {"healthcheck": "ok"}