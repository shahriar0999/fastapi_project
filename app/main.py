import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session

from fastapi_project.app import models
from fastapi_project.app.database import engine
from fastapi_project.app.routers import chats, users, auth, vote
from fastapi_project.app.config import settings

app = FastAPI()


@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=engine)

app.include_router(chats.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World!"}


# if __name__ == "__main__":
#    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
