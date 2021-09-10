import datetime
from typing import List
from schema import Schema, And, Use, Optional, SchemaError
from sqlalchemy import JSON

from sqlalchemy.orm import Session

from db.models.bgg_game import BggGame
from db.models.bgg_game_attributes import BggGameAttributes
from db.models.bgg_game_attributes_types import BggGameAttributesTypes


class ORMWrapperGameCRUD(object):
    def __init__(self, db: Session):
        self.db = db

    def add_game(self, data: dict):
        db = self.db

        def check_schema():
            data_schema = Schema({
                Use(int): {
                    "game_name": And(Use(str)),
                    "game_description": And(Use(str)),
                    "game_published": And(Use(str)),
                    "game_thumbnails": And(Use(str)),
                    "game_images": And(Use(str)),
                    "game_min_players": And(Use(int)),
                    "game_max_players": And(Use(int)),
                }
            })
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                return False

        if not check_schema():
            return False

        def create_row():
            row = BggGame()
            for k, v in data.items():
                row.game_index = k
                row.game_description = v["game_description"]
                row.game_name = v["game_name"]
                row.game_published = datetime.date.fromisoformat(v["game_published"])
                row.game_thumbnails = v["game_thumbnails"]
                row.game_images = v["game_images"]
                row.game_min_players = v["game_min_players"]
                row.game_max_players = v["game_max_players"]
            return row

        try:
            db.add(create_row())
            db.commit()
            return True
        except:
            return False

    def update_game(self, data: dict):
        db = self.db

        def check_schema():
            data_schema = Schema({
                Use(int): {
                    Optional("game_name"): (Use(str)),
                    Optional("game_description"): (Use(str)),
                    Optional("game_published"): (Use(str)),
                    Optional("game_thumbnails"): (Use(str)),
                    Optional("game_images"): (Use(str)),
                    Optional("game_min_players"): (Use(int)),
                    Optional("game_max_players"): (Use(int)),
                }
            })
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                return False

        if not check_schema():
            return False

        def update_row():
            for k in data.keys():
                row = db.query(BggGame).filter(BggGame.game_index == k).first()
                for k2, v in data[k].items():
                    if "game_name" == k2:
                        row.game_name = v
                    elif "game_description" == k2:
                        row.game_description = v
                    elif "game_published" == k2:
                        row.game_published = datetime.date.fromisoformat(v)
                    elif "game_thumbnails" == k2:
                        row.game_thumbnails = v
                    elif "game_min_players" == k2:
                        row.game_min_players = v
                    elif "game_max_players" == k2:
                        row.game_max_players = v
                return row

        try:
            update_row()
            db.commit()
            return True
        except:
            return False

    def delete_game_by_bgg_index(self, game_index: int) -> bool:
        db = self.db
        try:
            db.delete(db.query(BggGame).filter(BggGame.game_index).first())
            db.commit()
            return True
        except:
            return False

    def delete_game_by_id(self, game_id: int) -> bool:
        db = self.db
        try:
           db.delete(db.query(BggGame).filter(BggGame.id).first())
           db.commit()
           return True
        except:
            return False

    def get_game_by_bgg_index(self, game_index: int) -> dict or None:
        db = self.db
        try:
            game = db.query(BggGame).filter(BggGame.game_index == game_index).first()
            return self.__instance_to_json(game)
        except:
            return None

    def get_game_by_id(self, game_id: int) -> dict or None:
        db = self.db
        try:
            game = db.query(BggGame).filter(BggGame.id == game_id).first()
            return self.__instance_to_json(game)
        except:
            return None

    @staticmethod
    def __instance_to_json(instance: BggGame):
        return {
            "game_id": instance.id,
            "game_index": instance.game_index,
            "game_name": instance.game_name,
            "game_description": instance.game_description,
            "game_published": instance.game_published,
            "game_thumbnails": instance.game_thumbnails,
            "game_images": instance.game_images,
            "game_min_players": instance.game_min_players,
            "game_max_players": instance.game_max_players
        }


class ORMWrapperGame(ORMWrapperGameCRUD):
    def __init__(self, db: Session):
        super().__init__(db)

    def write_games_to_db(self, data: dict) -> bool:
        def check_schema():
            data_schema = Schema({
                Use(int): {
                    "game_name": And(Use(str)),
                    "game_description": And(Use(str)),
                    "game_published": And(Use(str)),
                    "game_thumbnails": And(Use(str)),
                    "game_images": And(Use(str)),
                    "game_min_players": And(Use(str)),
                    "game_max_players": And(Use(str)),
                }})
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                return False
        if not check_schema():
            return False
        db = self.db
        for k, v in data.items():
            game = {k: v}
            existing_game = db.query(BggGame).filter(BggGame.game_index == k)
            if not existing_game.first():
                status = self.add_game(game)
            else:
                status = self.update_game(game)
        return status


class ORMWrapperAttributeTypesCRUD(object):
    def __init__(self, db: Session):
        self.db = db

    def add_attribute_type(self, attribute_type_index: int, attribute_type_name: str) -> bool:
        db = self.db

        def create_attribute_type_row():
            row = BggGameAttributesTypes()
            row.attribute_type_index = attribute_type_index
            row.attribute_type_name = attribute_type_name
            return row

        row = create_attribute_type_row()
        try:
            db.add(row)
            db.commit()
            return True
        except:
            return False

    def get_attribute_type(self, attribute_type_index: int or str) -> dict:
        db = self.db

        if issubclass(attribute_type_index, int):
            row = db.query(BggGameAttributesTypes) \
                .filter(BggGameAttributesTypes.attribute_type_index == attribute_type_index).first()
        elif issubclass(attribute_type_index, str):
            row = db.query(BggGameAttributesTypes) \
                .filter(BggGameAttributesTypes.attribute_type_name == attribute_type_index).first()
        return {"attribute_type_index": row.attribute_type_index,
                "attribute_type_name": row.attribute_type_name}

    def update_attribute_type(self, attribute_type_index: int, attribute_type_name: str) -> bool:
        db = self.db

        existing_data = db.query(BggGameAttributesTypes).filter(
            BggGameAttributesTypes.attribute_type_index == attribute_type_index).first()
        if existing_data.attribute_type_name != attribute_type_name:
            existing_data.attribute_type_name = attribute_type_name
            try:
                db.commit()
                return True
            except:
                return False
        return False

    def delete_attribute_type(self, attribute_id: int or str) -> bool:
        db = self.db
        if isinstance(attribute_id, int):
            row = db.query(BggGameAttributesTypes).filter(
                BggGameAttributesTypes.attribute_type_index == attribute_id).first()
        elif isinstance(attribute_id, str):
            row = db.query(BggGameAttributesTypes).filter(
                BggGameAttributesTypes.attribute_type_name == attribute_id).first()
        try:
            db.delete(row)
            db.commit()
            return True
        except:
            return False


class ORMWrapperAttributeTypes(ORMWrapperAttributeTypesCRUD):
    def __init__(self, db: Session):
        super().__init__(db)

    def write_game_attributes_types_to_db(self, data: dict) -> bool:
        def check_schema():
            data_schema = Schema({
                Use(int): And(Use(str))
                })
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                return False
        if not check_schema():
            return False
        db = self.db
        for k, v in data.items():
            existing_attribute_type = db.query(BggGameAttributesTypes)\
                .filter(BggGameAttributesTypes.attribute_type_index == k)
            if not existing_attribute_type.first():
                status = self.add_attribute_type(attribute_type_index=k, attribute_type_name=v)
            else:
                status = self.update_attribute_type(attribute_type_index=existing_attribute_type,
                                                    attribute_type_name=v)
        return status


class ORMWrapperAttributesCRUD(object):
    def __init__(self, db: Session):
        self.db = db

    def add_attribute(self,
                      game_index: int,
                      attribute_type: int or str,
                      attribute_bgg_index: int,
                      attribute_bgg_value: str,
                      attribute_bgg_json: JSON) -> bool:
        db = self.db

        def get_type():
            if isinstance(attribute_type, int):
                attr = db.query(BggGameAttributesTypes)\
                    .filter(BggGameAttributesTypes.attribute_type_index == attribute_type).first()
            else:
                attr = db.query(BggGameAttributesTypes)\
                    .filter(BggGameAttributesTypes.attribute_type_name == attribute_type).first()
            if attr:
                return attr
            else:
                return "undefined"

        def create_attribute_row():
            row = BggGameAttributes()
            row.game_index = game_index
            row.attribute_type_index = get_type().attribute_type_index
            row.attribute_bgg_index = attribute_bgg_index
            row.attribute_bgg_value = attribute_bgg_value
            row.attribute_bgg_json = attribute_bgg_json
            return row

        row = create_attribute_row()
        try:
            db.add(row)
            db.commit()
            return True
        except:
            return False

    def get_attribute_by_id(self, attribute_id: int) -> dict or None:
        db = self.db
        try:
            instance = db.query(BggGameAttributes).filter(BggGameAttributes.id == attribute_id).first()
            return self.__instance_to_json(instance)
        except:
            return None

    def get_attributes_by_game_index(self, game_index: int) -> List[dict] or None:
        db = self.db
        try:
            data = []
            instances = db.query(BggGameAttributes).filter(BggGameAttributes.game_index == game_index).all()
            for instance in instances:
                data.append(self.__instance_to_json(instance))
            return data
        except:
            return None

    def update_attribute(self,
                         attribute_id: int,
                         attribute_bgg_index: int,
                         attribute_bgg_value: str,
                         attribute_bgg_json: JSON) -> bool:
        db = self.db
        existing_data = db.query(BggGameAttributes).filter(
            BggGameAttributes.id == attribute_id).first()
        if existing_data:
            if existing_data.attribute_bgg_index != attribute_bgg_index:
                existing_data.attribute_bgg_index = attribute_bgg_index
            if existing_data.attribute_bgg_value != attribute_bgg_value:
                existing_data.attribute_bgg_value = attribute_bgg_value
            try:
                db.commit()
                return True
            except:
                return False
        else:
            return False

    def delete_attribute(self, attribute_id: int) -> bool:
        db = self.db
        row = db.query(BggGameAttributes).filter(BggGameAttributes.id == attribute_id).first()
        try:
            db.delete(row)
            db.commit()
            return True
        except:
            return False

    @staticmethod
    def __instance_to_json(instance: BggGameAttributes) -> dict:
        return {
            "id": instance.id,
            "game_index": instance.game_index,
            "attribute_type_index": instance.attribute_type_index,
            "attribute_bgg_index": instance.attribute_bgg_index,
            "attribute_bgg_value": instance.attribute_bgg_value,
            "attribute_bgg_json": instance.attribute_bgg_json
        }


class ORMWrapperAttributes(ORMWrapperAttributesCRUD):
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def write_attributes_to_db(self, data: dict) -> bool:
        def check_schema():
            data_schema = Schema({
                Use(int): {
                    "type_index": And(Use(str)),
                    "bgg_index": And(Use(str)),
                    "bgg_value": And(Use(str)),
                    "attribute_bgg_json": And(Use(str))
                }})
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                return False
        if not check_schema():
            return False
        for k, v in data.items():
            existing_attribute = self.db.query(BggGameAttributes).filter(
                BggGameAttributes.id == k)
            if not existing_attribute.first():
                status = self.add_attribute(game_index=k,
                                            attribute_type=v["type_index"],
                                            attribute_bgg_index=v["bgg_index"],
                                            attribute_bgg_value=v["bgg_value"],
                                            attribute_bgg_json=v["bgg_json"])
            else:
                #TODO dodać validację czy nie nadpisujemy różnych atrybutów
                status = self.update_attribute(attribute_id=k,
                                               attribute_bgg_index=v["bgg_index"],
                                               attribute_bgg_value=v["bgg_value"],
                                               attribute_bgg_json=v["bgg_json"])
        return status
