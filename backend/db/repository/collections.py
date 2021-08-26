from sqlalchemy.orm import Session
from typing import List

from schemas.collections import CollectionCreate
from db.models.collection import Collection
from client.bgg import BggClient
from db.models.user import User


def synchronize_collection(data: CollectionCreate, db: Session, user_id: int) -> bool:
    if not data.bgg_user:
        data.bgg_user = db.query(User).filter(User.id == user_id).first().bgg_user
    collection = BggClient().get_collection_by_user(data.bgg_user)

    return True
    # db.add(collection)
    # db.commit()
    # db.refresh(collection)
    # return collection
