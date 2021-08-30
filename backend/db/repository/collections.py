from pprint import pprint

from sqlalchemy.orm import Session
from datetime import date

from client.client_bgg.model import Collection
from schemas.collections import CollectionCreate
from db.models.bgg_user_collection import BggUserCollection
from db.models.user import User
from client.bgg_client import BggClient
from db.repository.games import synchronize_games


def synchronize_collection(data: CollectionCreate, db: Session, user_id: int) -> bool:
    if not data.bgg_user:
        data.bgg_user = db.query(User).filter(User.id == user_id).first().bgg_user
    collection = BggClient(Collection(data.bgg_user)).get_data()
    if collection:
        try:
            game_indexes = []
            db.query(BggUserCollection).filter(BggUserCollection.user_id == user_id).delete()
            db.commit()
            for key in collection.keys():
                tree = collection[key]
                game_indexes.append(key)
                collection_item = BggUserCollection(
                    collection_updated = date.today(),
                    user_id = user_id,
                    game_index = key,
                    collection_comment = tree["comment"],
                    collection_numplays = tree["numplays"],
                    collection_fortrade = tree["status"]["fortrade"],
                    collection_preordered = tree["status"]["preordered"],
                    collection_prevowned = tree["status"]["prevowned"],
                    collection_want = tree["status"]["want"],
                    collection_wanttobuy = tree["status"]["wanttobuy"],
                    collection_wanttoplay = tree["status"]["wanttoplay"],
                    collection_wishlist = tree["status"]["wishlist"],
                    collection_lastmodified = tree["status"]["lastmodified"]
                )
                db.add(collection_item)
                db.commit()
                db.refresh(collection_item)
        except:
            return False
        try:
            synchronize_games(db=db, indexes=game_indexes)
            return True
        except:
            return False
    return True
