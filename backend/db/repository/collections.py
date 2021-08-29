from sqlalchemy.orm import Session
from datetime import date
from schemas.collections import CollectionCreate
from db.models.collection import Collection
from db.models.user import User
from client.bgg_client import BggClient
from db.repository.games import synchronize_games


def synchronize_collection(data: CollectionCreate, db: Session, user_id: int) -> bool:
    if not data.bgg_user:
        data.bgg_user = db.query(User).filter(User.id == user_id).first().bgg_user
    collection_new = BggClient().get_collection_by_user(data.bgg_user)
    game_indexes = []
    db.query(Collection).filter(Collection.user_id == user_id).delete()
    db.commit()
    # try:
    for key in collection_new.items.keys():
        game_indexes.append(key)
        collection_item = Collection(
            updated=date.today(),
            user_id=user_id,
            game_index=key,
            want_to_play=collection_new.items[key]["status"]["wanttoplay"],
            data=collection_new.items[key]
        )
        db.add(collection_item)
        db.commit()
        db.refresh(collection_item)
    synchronize_games(db=db, indexes=game_indexes)
    #     return True
    # except:
    #     return False
