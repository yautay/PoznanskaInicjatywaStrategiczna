from logs import logger
from sqlalchemy import and_
from schema import Schema, Use, Or, SchemaError
from sqlalchemy.orm import Session
from db.models.bgg_attribute import BggAttribute

logger = logger.get_logger(__name__)


class ORMWrapperBggAttribute(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> int or bool:
        db = self.db

        def check_existing() -> BggAttribute or None:
            return db.query(BggAttribute)\
                .filter_by(**data).first()

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
                logger.exception("msg")
                return False

        if not check_schema():
            return False
        existing = check_existing()
        if existing:
            logger.warning("BggAttribute: {} already exists in bgg_attribute, updated with {}"
                           .format(existing.to_json(), data))
            try:
                existing.__init__(**data)
                db.commit()
                return existing.id
            except:
                logger.critical(f"BggAttributes not UPDATED to db. \n data: {data}")
                logger.exception("msg")
                return False
        else:
            try:
                attribute = BggAttribute(**data)
                db.add(attribute)
                db.commit()
                logger.debug(f"{attribute.to_json()} added to bgg_attribute")
                return attribute.id
            except:
                logger.critical(f"BggAttributes not ADDED to db. \n data: {data}")
                logger.exception("msg")
                return False

    def read(self, data: int) -> BggAttribute or None:
        db = self.db
        return db.query(BggAttribute).filter(BggAttribute.id == data).first()

    def delete(self, data: int) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
