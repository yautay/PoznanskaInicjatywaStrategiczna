from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, AnyUrl


class UserCollectionBase(BaseModel):
    updated: Optional[date] = datetime.now().date()


class UserCollectionCreate(UserCollectionBase):
    pass

class UserCollectionShow(BaseModel):
    id: int
    user_id: int
    updated: date

    class Config:
        orm_mode = True
