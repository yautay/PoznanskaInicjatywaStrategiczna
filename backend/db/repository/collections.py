from typing import List

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
                "collection_numplays": And(Use(int)),
                "collection_fortrade": And(Use(int)),
                "collection_preordered": And(Use(int)),
                "collection_prevowned": And(Use(int)),
                "collection_want": And(Use(int)),
                "collection_wanttobuy": And(Use(int)),
                "collection_wanttoplay": And(Use(int)),
                "collection_wishlist": And(Use(int)),
                "collection_lastmodified": And(Use(int)),
                "collection_comment": And(Use(str))
            })
            try:
                data_schema.validate(data_schema)
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

    def update_collection(self, existing_row, item_data: dict) -> bool:
        db = self.db

        def check_schema():
            data_schema = Schema({
                Optional("collection_numplays"): (Use(int)),
                Optional("collection_fortrade"): (Use(int)),
                Optional("collection_preordered"): (Use(int)),
                Optional("collection_prevowned"): (Use(int)),
                Optional("collection_want"): (Use(int)),
                Optional( "collection_wanttobuy"): (Use(int)),
                Optional( "collection_wanttoplay"): (Use(int)),
                Optional("collection_wishlist"): (Use(int)),
                Optional("collection_lastmodified"): (Use(int)),
                Optional("collection_comment"): (Use(str))
            })
            try:
                data_schema.validate(data_schema)
                return True
            except SchemaError:
                return False

        if not check_schema():
            return False

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
        existing_data.collection_lastmodified = datetime.strptime(item_data["status"]["lastmodified"],
                                                                  "%Y-%m-%d %H:%M:%S")
        if "comment" in item_data.keys():
            existing_data.collection_comment = item_data["comment"]
        else:
            existing_data.collection_comment = "undefined"
        try:
            db.commit()
            return True
        except:
            return False

    def delete_collection_by_id(self, collection_id: int) -> bool:
        db = self.db
        try:
            db.delete(db.query(BggUserCollection).filter(BggUserCollection.id == collection_id).first())
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
        return {
            "collection_id": instance.id,
            "game_index": instance.game_index,
            "collection_updated": instance.collection_updated,
            "collection_numplays": instance.collection_numplays,
            "collection_fortrade": instance.collection_fortrade,
            "collection_preordered": instance.collection_preordered,
            "collection_prevowned": instance.collection_prevowned,
            "collection_want": instance.collection_want,
            "collection_wanttobuy": instance.collection_wanttobuy,
            "collection_wanttoplay": instance.collection_wanttoplay,
            "collection_wishlist": instance.collection_wishlist,
            "collection_lastmodified": instance.collection_lastmodified,
            "collection_comment": instance.collection_comment
        }


class ORMWrapperCollection(ORMWrapperCollectionCRUD):
    def __init__(self, db):
        super().__init__(db)

    def write_collections_to_db(self, user_id: int, bgg_data: dict) -> bool:
        db = self.db
        for k, v in bgg_data.items():
            existing_collection_item = db.query(BggUserCollection).filter(BggUserCollection.game_index == k)
            if not existing_collection_item.first():
                status = self.add_collection(game_index=k, collection_data=v, user_id=user_id)
            else:
                status = self.update_collection(existing_row=existing_collection_item, item_data=v)
        return status
