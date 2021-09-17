from sqlalchemy import and_

from logs import logger
from sqlalchemy.orm import Session
from schema import Schema, Use, SchemaError
from db.models.bgg_game_attribute import BggGameAttribute

logger = logger.get_logger(__name__)


class ORMWrapperBggGameAttribute(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> int or bool:
        db = self.db

        def check_existing() -> BggGameAttribute or None:
            return db.query(BggGameAttribute)\
                .filter(and_(BggGameAttribute.game_index == data["game_index"]),
                        (BggGameAttribute.bgg_attribute == data["bgg_attribute"])).first()

        def check_schema():
            data_schema = Schema({
                "game_index": Use(int),
                "attribute_type_index": Use(int),
                "bgg_attribute": Use(int)})
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                logger.error(f'Schema validation error for {data}')
                return False

        if not check_schema():
            return False
        existing = check_existing()
        if existing:
            logger.warning("BggGameAttribute: {} already exists in bgg_attribute, updated with {}"
                           .format(existing.to_json(), data))
            try:
                existing.__init__(**data)
                db.commit()
                return existing.id
            except:
                logger.critical(f"BggGameAttributes not UPDATED to db. \n data: {data}")
                logger.exception("msg")
                return False
        attribute = BggGameAttribute(**data)
        try:
            db.add(attribute)
            db.commit()
            logger.debug(f"{attribute.to_json()} added to bgg_game_attribute")
            return attribute.id
        except:
            logger.critical(f"BggGameAttributes not ADDED to db. \n data: {attribute.to_json()}")
            return False

    def read(self, data: int) -> BggGameAttribute or None:
        db = self.db
        return db.query(BggGameAttribute).filter(BggGameAttribute.id == data).first()

    def delete(self, data: int) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
