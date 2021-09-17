from logs import logger
from schema import Schema, Use, SchemaError
from sqlalchemy.orm import Session
from db.models.bgg_game import BggGame

logger = logger.get_logger(__name__)


class ORMWrapperBggGame(object):
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> bool:
        db = self.db

        def check_existing() -> BggGame or None:
            return db.query(BggGame).filter(BggGame.game_index == data["game_index"]).first()

        def check_schema():
            data_schema = Schema({
                "game_index": Use(int),
                "game_name": Use(str),
                "game_description": Use(str),
                "game_published": Use(str),
                "game_thumbnails": Use(str),
                "game_images": Use(str),
                "game_min_players": Use(int),
                "game_max_players": Use(int)})
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                logger.error(f"Schema validation error for {data}")
                logger.exception("msg")
                return False

        if not check_schema():
            return False
        existing = check_existing()
        if existing:
            logger.warning(f"Game exists in bgg_game: {existing.to_json()} updating with: {data}")
            try:
                existing.__init__(**data)
                db.commit()
                return True
            except:
                logger.critical(f"BggGame not UPDATED to db. \n data: {data}")
                logger.exception("msg")
                return False
        else:
            try:
                game = BggGame(**data)
                db.add(game)
                db.commit()
                return True
            except:
                logger.critical(f"BggGame not ADDED to db. \n data: {data}")
                logger.exception("msg")
                return False

    def read(self, data: int) -> BggGame or None:
        db = self.db
        return db.query(BggGame).filter(BggGame.id == data).first()

    def delete(self, data: int) -> bool:
        db = self.db
        try:
            instance = self.read(data)
            db.delete(instance)
            db.commit()
            return True
        except:
            return False
