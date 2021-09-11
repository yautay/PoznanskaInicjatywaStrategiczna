from sqlalchemy import and_
from sqlalchemy.orm import Session
from schema import Schema, Use, SchemaError
from db.models.bgg_game_attributes import BggGameAttributes
import logging

logger = logging.getLogger('ORMWrapperBggGameAttributes')


class ORMWrapperBggGameAttributes(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> bool:
        db = self.db

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
        attribute = BggGameAttributes(**data)
        try:
            db.add(attribute)
            db.commit()
            return True
        except:
            logger.critical(f"BggGameAttributes not ADDED to db. instance: {attribute} data: {data}")
            return False

    def read(self, data: int) -> BggGameAttributes or None:
        db = self.db
        return db.query(BggGameAttributes).filter(BggGameAttributes.id == data).first()

    def delete(self, data: int or str) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
