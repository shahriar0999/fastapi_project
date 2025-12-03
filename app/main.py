import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from .database import engine
from . import models, schemas, utils, config
from .routers import chats, users, auth, vote

app = FastAPI()

app.include_router(chats.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
