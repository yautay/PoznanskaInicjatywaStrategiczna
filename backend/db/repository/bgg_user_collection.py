import datetime
from logs.logger import Logger
from schema import Schema, Or, Use, SchemaError
from sqlalchemy import and_
from sqlalchemy.orm import Session
from db.models.bgg_user_collection import BggUserCollection

logger = Logger().logger


class ORMWrapperBggUserCollection(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> bool:
        db = self.db

        def check_existing() -> BggUserCollection or None:
            return db.query(BggUserCollection)\
                .filter(and_(BggUserCollection.user_id == data["user_id"],
                             BggUserCollection.game_index == data["game_index"])).first()

        def check_schema():
            data_schema = Schema({
                "user_id": (Use(int)),
                "game_index": (Use(int)),
                "collection_own": Or(Use(int), None),
                "collection_comment": Or(Use(str), None),
                "collection_numplays": Or(Use(int), None),
                "collection_fortrade": Or(Use(int), None),
                "collection_preordered": Or(Use(int), None),
                "collection_prevowned": Or(Use(int), None),
                "collection_want": Or(Use(int), None),
                "collection_wanttobuy": Or(Use(int), None),
                "collection_wanttoplay": Or(Use(int), None),
                "collection_wishlist": Or(Use(int), None),
                "collection_lastmodified": Or(Use(str), None)})
            try:
                data_schema.validate(data)
                data["collection_updated"] = datetime.datetime.now()
                return True
            except SchemaError:
                logger.error(f'Schema validation error for {data}')
                logger.exception("msg")
                return False

        if not check_schema():
            return False

        existing = check_existing()
        if existing:
            existing.__init__(**data)
            try:
                db.commit()
                return True
            except:
                logger.critical(f"BggUserCollection not UPDATED to db. \n instance: {existing.to_json()} \n data: {data}")
                logger.exception("msg")
                return False
        else:
            collection = BggUserCollection(**data)
            try:
                db.add(collection)
                db.commit()
                return True
            except:
                logger.critical(f"BggUserCollection not ADDED to db. \n instance: {collection.to_json()} \n data: {data}")
                logger.exception("msg")
                return False

    def read(self, data: int) -> BggUserCollection or None:
        db = self.db
        return db.query(BggUserCollection).filter(BggUserCollection.id == data).first()

    def delete(self, data: int) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
