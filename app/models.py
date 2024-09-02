from pydantic import BaseModel


class Note(BaseModel):
    title: str
    content: str
    user_id: int


class User(BaseModel):
    id: int
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class NoteCreate(BaseModel):
    title: str
    content: str