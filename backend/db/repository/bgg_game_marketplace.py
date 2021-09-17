import datetime

from logs import logger
from sqlalchemy.orm import Session
from schema import Schema, Use, SchemaError
from db.models.bgg_game_marketplace import BggGameMarketplace

logger = logger.get_logger(__name__)


class ORMWrapperBggGameMarketplace(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> bool:
        db = self.db

        def check_existing() -> BggGameMarketplace or None:
            return db.query(BggGameMarketplace)\
                .filter_by(**data).first()

        def check_schema():
            data_schema = Schema({
                "game_index": Use(int),
                "offer_date": Use(str),
                "offer_price": Use(float),
                "offer_currency": Use(str),
                "offer_condition": Use(str),
                "offer_notes": Use(str),
                "offer_bgg_link": Use(str)})
            try:
                data_schema.validate(data)
                if not isinstance(data["offer_date"], datetime.datetime):
                    data["offer_date"] = datetime.datetime.strptime(data["offer_date"], "%a, %d %b %Y %H:%M:%S %z")
                return True
            except SchemaError:
                logger.error(f'Schema validation error for {data}')
                return False

        if not check_schema():
            return False
        existing = check_existing()
        if existing:
            logger.warning("Offer: {} already exists in bgg_game_marketplace -> {}"
                           .format(existing.to_json(), data))
        try:
            marketplace = BggGameMarketplace(**data)
            db.add(marketplace)
            db.commit()
            logger.debug(f"{marketplace.to_json()} added to bgg_marketplace")
            return True
        except:
            logger.critical(f"BggGameMarketplace not ADDED to db. \n data: {data}")
            return False

    def read(self, data: int) -> BggGameMarketplace or None:
        db = self.db
        return db.query(BggGameMarketplace).filter(BggGameMarketplace.id == data).first()

    def delete(self, data: int) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
