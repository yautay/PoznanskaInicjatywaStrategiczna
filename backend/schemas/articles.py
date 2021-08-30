from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, AnyUrl


class ArticleBase(BaseModel):
    article_title: Optional[str] = None
    article_content: Optional[str] = None
    article_picture: Optional[AnyUrl] = None
    article_created_at: Optional[date] = datetime.now().date()
    article_is_active: Optional[bool] = False


class ArticleCreate(ArticleBase):
    article_title: str
    article_content: str
    article_picture: AnyUrl


class ArticleShow(BaseModel):
    article_title: str
    article_created_at: date
    article_is_active: bool

    class Config:
        orm_mode = True
