from fastapi import FastAPI

from events import lifespan
from api.routers import login_router

app = FastAPI(lifespan=lifespan, title="FG Tracking App")
app.include_router(login_router, tags=["Login"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
