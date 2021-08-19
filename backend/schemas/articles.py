from typing import Optional
from pydantic import BaseModel, AnyUrl


class UserCreate(BaseModel):
    title: str
    content: str
    picture: AnyUrl
    is_active: bool
