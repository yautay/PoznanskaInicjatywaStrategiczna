from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, AnyUrl


class CollectionBase(BaseModel):
    updated: Optional[date] = datetime.now().date()


class CollectionCreate(CollectionBase):
    pass


class CollectionShow(BaseModel):
    id: int
    user_id: int
    updated: date

    class Config:
        orm_mode = True
