import logging
from schema import Schema, Use, Or, SchemaError
from sqlalchemy.orm import Session
from db.models.bgg_attribute import BggAttribute

logger = logging.getLogger('ORMWrapperBggAttributes')


class ORMWrapperBggAttribute(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> bool:
        db = self.db

        def check_existing() -> BggAttribute or None:
            return db.query(BggAttribute).filter(BggAttribute.attribute_bgg_index == data["attribute_bgg_index"]).first()

        def check_schema():
            data_schema = Schema({
                "attribute_bgg_index": Or(Use(int), None),
                "attribute_bgg_value": Or(Use(str), None),
                "attribute_bgg_json": Or(Use(str), None)})
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
            existing.__init__(**data)
            try:
                db.commit()
                return True
            except:
                logger.critical(f"BggAttributes not UPDATED to db. \n instance: {existing.to_json()} \n data: {data}")
                return False
        else:
            attribute = BggAttribute(**data)
            try:
                db.add(attribute)
                db.commit()
                return True
            except:
                logger.critical(f"BggAttributes not ADDED to db. \n instance: {attribute.to_json()} \n data: {data}")
                return False

    def read(self, data: int) -> BggAttribute or None:
        db = self.db
        return db.query(BggAttribute).filter(BggAttribute.id == data).first()

    def delete(self, data: int or str) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
