from typing import List
from client.client_bgg.parser.item_keys import CollectionItemKeys as key

from schema import Schema, And, Use, Optional, SchemaError
from sqlalchemy.orm import Session
from datetime import datetime

from db.models.bgg_user_collection import BggUserCollection


class ORMWrapperCollectionCRUD(object):
    def __init__(self, db):
        self.db = db

    def add_collection(self, game_index: int, collection_data: dict, user_id: int) -> bool:
        db = self.db

        def check_schema():
            data_schema = Schema({
                Optional(key.COMMENT): (Use(str)),
                key.NUMPLAYS: And(Use(int)),
                key.STATUS: {
                     key.FORTRADE: And(Use(int)),
                     key.LASTMODIFIED: And(Use(str)),
                     key.PREORDERED: And(Use(int)),
                     key.PREVOWNED: And(Use(int)),
                     key.WANT: And(Use(int)),
                     key.WANTTOBUY: And(Use(int)),
                     key.WANTTOPLAY: And(Use(int)),
                     key.WISHLIST: And(Use(int))
                }
            })
            try:
                data_schema.validate(collection_data)
                return True
            except SchemaError:
                return False

        if not check_schema():
            return False

        def create_row():
            row = BggUserCollection()
            row.collection_updated = datetime.now()
            row.user_id = user_id
            row.game_index = game_index
            row.collection_numplays = collection_data["numplays"]
            row.collection_fortrade = collection_data["status"]["fortrade"]
            row.collection_preordered = collection_data["status"]["preordered"]
            row.collection_prevowned = collection_data["status"]["prevowned"]
            row.collection_want = collection_data["status"]["want"]
            row.collection_wanttobuy = collection_data["status"]["wanttobuy"]
            row.collection_wanttoplay = collection_data["status"]["wanttoplay"]
            row.collection_wishlist = collection_data["status"]["wishlist"]
            row.collection_lastmodified = datetime.strptime(collection_data["status"]["lastmodified"],
                                                            "%Y-%m-%d %H:%M:%S")
            if "comment" in collection_data.keys():
                row.collection_comment = collection_data["comment"]
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

    def update_collection(self, existing_row: BggUserCollection, item_data: dict) -> bool:
        db = self.db

        def check_schema():
            data_schema = Schema({
                Optional(key.COMMENT): (Use(str)),
                Optional(key.NUMPLAYS): (Use(int)),
                Optional(key.STATUS): {
                    Optional(key.FORTRADE): (Use(int)),
                    Optional(key.LASTMODIFIED): (Use(str)),
                    Optional(key.PREORDERED): (Use(int)),
                    Optional(key.PREVOWNED): (Use(int)),
                    Optional(key.WANT): (Use(int)),
                    Optional(key.WANTTOBUY): (Use(int)),
                    Optional(key.WANTTOPLAY): (Use(int)),
                    Optional(key.WISHLIST): (Use(int))
                }
            })
            try:
                data_schema.validate(item_data)
                return True
            except SchemaError:
                return False

        if not check_schema():
            return False

        existing_data = existing_row
        for k, v in item_data.items():
            if k == key.COMMENT:
                existing_row.collection_comment = v
            elif k == key.NUMPLAYS:
                existing_row.collection_numplays = v
            elif k == key.STATUS:
                for kn, vn in v.items():
                    if kn == key.PREVOWNED:
                        existing_row.collection_prevowned = vn
                    elif kn == key.PREORDERED:
                        existing_row.collection_preordered = vn
                    elif kn == key.WANT:
                        existing_row.collection_want = vn
                    elif kn == key.WANTTOBUY:
                        existing_row.collection_wanttobuy = vn
                    elif kn == key.WANTTOPLAY:
                        existing_row.collection_wanttoplay = vn
                    elif kn == key.WISHLIST:
                        existing_row.collection_wishlist = vn
                    elif kn == key.NUMPLAYS:
                        existing_row.collection_numplays = vn
                    elif kn == key.LASTMODIFIED:
                        existing_row.collection_lastmodified = datetime.fromisoformat(vn)
            existing_row.collection_updated = datetime.now()
        try:
            db.commit()
            return True
        except:
            return False

    def delete_collection_by_id(self, collection_id: int or List[int]) -> bool:
        db = self.db
        try:
            if isinstance(collection_id, int):
                db.delete(db.query(BggUserCollection).filter(BggUserCollection.id == collection_id).first())
            else:
                for _id in collection_id:
                    db.delete(db.query(BggUserCollection).filter(BggUserCollection.id == _id).first())
            db.commit()
            return True
        except:
            return False

    def get_collection_by_id(self, collection_id: int) -> dict or None:
        db = self.db
        return self.__instance_to_json(db.query(BggUserCollection)
                                       .filter(BggUserCollection.id == collection_id).first())

    def get_collections_by_user_id(self, user_id: int) -> List[dict] or None:
        db = self.db
        try:
            instances = db.query(BggUserCollection).filter(BggUserCollection.user_id == user_id).all()
            data = []
            for instance in instances:
                data.append(self.__instance_to_json(instance))
            return data
        except:
            return None

    @staticmethod
    def __instance_to_json(instance: BggUserCollection):
        if instance is None:
            return None
        else:
            return {
                "collection_id": instance.id,
                "game_index": instance.game_index,
                "collection_updated": instance.collection_updated.isoformat(),
                "collection_numplays": instance.collection_numplays,
                "collection_fortrade": instance.collection_fortrade,
                "collection_preordered": instance.collection_preordered,
                "collection_prevowned": instance.collection_prevowned,
                "collection_want": instance.collection_want,
                "collection_wanttobuy": instance.collection_wanttobuy,
                "collection_wanttoplay": instance.collection_wanttoplay,
                "collection_wishlist": instance.collection_wishlist,
                "collection_lastmodified": instance.collection_lastmodified.isoformat(),
                "collection_comment": instance.collection_comment
            }


class ORMWrapperCollection(ORMWrapperCollectionCRUD):
    def __init__(self, db):
        super().__init__(db)

    def write_user_collections_to_db(self, user_id: int, bgg_data: dict) -> bool:
        db = self.db
        for k, v in bgg_data.items():
            existing_collection_item = db.query(BggUserCollection).filter(BggUserCollection.game_index == k)
            if not existing_collection_item.first():
                status = self.add_collection(game_index=k, collection_data=v, user_id=user_id)
            else:
                status = self.update_collection(existing_row=existing_collection_item, item_data=v)
        return status

    def delete_user_collections(self, user_id: int) -> bool:
        db = self.db
        collections = self.get_collections_by_user_id(user_id)
        collections_ids = []
        for col in collections:
            collections_ids.append(col["collection_id"])
        return self.delete_collection_by_id(collections_ids)
