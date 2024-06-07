from typing import Optional, List
from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

class UserCreate(BaseModel):
    fullname: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    fullname: str
    email: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class BoardCreate(BaseModel):
    name: str
    public: bool

class BoardResponse(BaseModel):
    id: int
    name: str
    public: bool
    owner_id: int

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    board_id: int
    owner_id: int

    class Config:
        orm_mode = True

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class Pagination(BaseModel):
    total: int
    page: int
    size: int
    items: List[PostResponse]
