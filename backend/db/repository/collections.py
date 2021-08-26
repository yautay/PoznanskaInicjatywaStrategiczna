from sqlalchemy.orm import Session
from typing import List
from datetime import date
from sqlalchemy import delete
from schemas.collections import CollectionCreate
from db.models.collection import Collection
from client.bgg import BggClient
from db.models.user import User


def synchronize_collection(data: CollectionCreate, db: Session, user_id: int) -> bool:
    if not data.bgg_user:
        data.bgg_user = db.query(User).filter(User.id == user_id).first().bgg_user
    collection = BggClient().get_collection_by_user(data.bgg_user)
    delete_collection(db=db, user_id=user_id)
    try:
        for key in collection.items.keys():
            collection_item = Collection(
                updated=date.today(),
                user_id=user_id,
                game_index=key,
                want_to_play=bool(collection.items[key]["status"]["wanttoplay"]),
                data=collection.items[key]
            )
            db.add(collection_item)
            db.commit()
            db.refresh(collection_item)
        return True
    except:
        return False


def delete_collection(db: Session, user_id: int) -> bool:
    delete = (delete("collection").where(collection.user_id == user_id))
    entries = db.query(Collection).filter(User.id == user_id).first()
    entries.delete(synchronize_session=False)
    db.commit()
    return True