import logging
from schema import Schema, Use, SchemaError
from sqlalchemy.orm import Session
from db.models.bgg_game import BggGame

logger = logging.getLogger('ORMWrapperBggGame')


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
                logger.critical(f"BggGame not UPDATED to db. \n instance: {existing.to_json()} \n data: {data}")
                logger.exception("msg")
                return False
        else:
            game = BggGame(**data)
            try:
                db.add(game)
                db.commit()
                return True
            except:
                logger.critical(f"BggGame not ADDED to db. \n instance: {game.to_json()} \n data: {data}")
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
