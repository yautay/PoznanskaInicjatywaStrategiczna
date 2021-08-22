from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    bgg_user: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birthdate: Optional[date] = None


class UserCreate(UserBase):
    login: str
    password: str
    email: EmailStr
    name: str
    surname: str
    birthdate: date


class ShowUser(BaseModel):
    login: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
