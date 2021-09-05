from sqlalchemy.orm import Session
from datetime import datetime

from db.models.bgg_user_collection import BggUserCollection


class ORMWrapperCollections:
    def write_collection_to_db(self, db: Session, user_id: int, bgg_data: dict) -> bool:
        for k, v in bgg_data.items():
            existing_collection_item = db.query(BggUserCollection).filter(BggUserCollection.game_index == k)
            if not existing_collection_item.first():
                status = self.CRUD.add_collection_row(db=db, game_index=k, game_data=v, user_id=user_id)
            else:
                status = self.CRUD.update_collection_row(db=db, existing_row=existing_collection_item, item_data=v)
        return status

    class CRUD:
        @staticmethod
        def add_collection_row(db: Session, game_index: int, game_data: dict, user_id: int) -> bool:
            def create_row():
                row = BggUserCollection()
                row.collection_updated = datetime.now()
                row.user_id = user_id
                row.game_index = game_index
                row.collection_numplays = game_data["numplays"]
                row.collection_fortrade = game_data["status"]["fortrade"]
                row.collection_preordered = game_data["status"]["preordered"]
                row.collection_prevowned = game_data["status"]["prevowned"]
                row.collection_want = game_data["status"]["want"]
                row.collection_wanttobuy = game_data["status"]["wanttobuy"]
                row.collection_wanttoplay = game_data["status"]["wanttoplay"]
                row.collection_wishlist = game_data["status"]["wishlist"]
                row.collection_lastmodified = datetime.strptime(game_data["status"]["lastmodified"],
                                                                "%Y-%m-%d %H:%M:%S")
                if "comment" in game_data.keys():
                    row.collection_comment = game_data["comment"]
                else:
                    row.collection_comment = "undefined"
                return row
            row = create_row()
            try:
                db.add(row)
                db.commit()
                return True
            except:
                return False

        @staticmethod
        def update_collection_row(db: Session, existing_row, item_data: dict) -> bool:
            existing_data = existing_row.first()
            existing_data.collection_updated = datetime.now()
            existing_data.collection_numplays = item_data["numplays"]
            existing_data.collection_fortrade = item_data["status"]["fortrade"]
            existing_data.collection_preordered = item_data["status"]["fortrade"]
            existing_data.collection_prevowned = item_data["status"]["fortrade"]
            existing_data.collection_want = item_data["status"]["fortrade"]
            existing_data.collection_wanttobuy = item_data["status"]["fortrade"]
            existing_data.collection_wanttoplay = item_data["status"]["fortrade"]
            existing_data.collection_wishlist = item_data["status"]["fortrade"]
            existing_data.collection_lastmodified = datetime.strptime(item_data["status"]["lastmodified"], "%Y-%m-%d %H:%M:%S")
            if "comment" in item_data.keys():
                existing_data.collection_comment = item_data["comment"]
            else:
                existing_data.collection_comment = "undefined"
            try:
                db.commit()
                return True
            except:
                return False

        @staticmethod
        def delete_collection_row(db: Session, existing_row) -> bool:
            try:
                db.delete(existing_row)
                db.commit()
                return True
            except:
                return False

# def synchronize_collection(data: CollectionCreate, db: Session, user_id: int) -> bool:
#     if not data.bgg_user:
#         data.bgg_user = db.query(User).filter(User.id == user_id).first().bgg_user
#     collection = BggClient(Collection(data.bgg_user)).get_data()
#     if collection:
#         try:
#             game_indexes = []
#             db.query(BggUserCollection).filter(BggUserCollection.user_id == user_id).delete()
#             db.commit()
#             for key in collection.keys():
#                 tree = collection[key]
#                 game_indexes.append(key)
#                 collection_item = BggUserCollection(
#                     collection_updated = date.today(),
#                     user_id = user_id,
#                     game_index = key,
#                     collection_comment = tree["comment"],
#                     collection_numplays = tree["numplays"],
#                     collection_fortrade = tree["status"]["fortrade"],
#                     collection_preordered = tree["status"]["preordered"],
#                     collection_prevowned = tree["status"]["prevowned"],
#                     collection_want = tree["status"]["want"],
#                     collection_wanttobuy = tree["status"]["wanttobuy"],
#                     collection_wanttoplay = tree["status"]["wanttoplay"],
#                     collection_wishlist = tree["status"]["wishlist"],
#                     collection_lastmodified = tree["status"]["lastmodified"]
#                 )
#                 db.add(collection_item)
#                 db.commit()
#                 db.refresh(collection_item)
#         except:
#             return False
#         try:
#             synchronize_games(db=db, indexes=game_indexes)
#             return True
#         except:
#             return False
#     return True

