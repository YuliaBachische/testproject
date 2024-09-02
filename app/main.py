from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

from app.auth import get_current_user, authenticate_user
from app.models import LoginRequest
from app.routers import notes, users

app = FastAPI()

app.include_router(notes.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the notes API!"}


@app.post("/login")
def login(request: LoginRequest):
    user = authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful", "user": user}


@app.get("/protected-route")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {user['username']}!"}