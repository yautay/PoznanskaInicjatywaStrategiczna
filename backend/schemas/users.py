from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    login: str
    password: str
    email: EmailStr
    name: str
    surname: str
    age: int
    administrator: bool
    superuser: bool
    is_active: bool


class ShowUser(BaseModel):
    login: str
    email: EmailStr

    class Config():
        orm_mode = True
