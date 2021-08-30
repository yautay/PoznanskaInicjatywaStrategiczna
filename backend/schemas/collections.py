from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, AnyUrl


class CollectionBase(BaseModel):
    collection_updated: Optional[date] = datetime.now().date()
    bgg_user: Optional[str] = None


class CollectionCreate(CollectionBase):
    bgg_user: str


class CollectionShow(BaseModel):
    id: int
    bgg_user: str
    collection_updated: date

    class Config:
        orm_mode = True
