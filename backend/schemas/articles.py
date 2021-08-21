from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, AnyUrl


class ArticleBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    picture: Optional[AnyUrl] = None
    created_at: Optional[date] = datetime.now().date()
    is_active: Optional[bool] = False


class ArticleCreate(ArticleBase):
    title: str
    content: str
    picture: AnyUrl


class ArticleShow(BaseModel):
    title: str
    created_at: date
    is_active: bool

    class Config:
        orm_mode = True
