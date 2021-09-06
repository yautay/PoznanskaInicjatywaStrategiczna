from typing import List
from schema import Schema, And, Use, Optional, SchemaError

from sqlalchemy.orm import Session
from datetime import datetime

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
                    "game_published": And(Use(datetime)),
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


    def update_game(self):
        pass

    def delete_game(self):
        pass

    def get_game_by_bgg_index(self):
        pass

class ORMWrapperGame(ORMWrapperGameCRUD):
    def __init__(self, db: Session):
        super().__init__(db)



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

    def write_game_attribute_types_to_db(self, data: dict) -> bool:
        def check_schema():
            data_schema = Schema({
                Use(int): And(Use(str))
                })
            try:
                data_schema.validate(data)
                return True
            except SchemaError:
                return False
        if check_schema():
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
        else:
            return False


class ORMWrapperAttributesCRUD(object):
    def __init__(self, db: Session):
        self.db = db

    def add_attribute(self,
                      game_index: int,
                      attribute_type: int or str,
                      attribute_bgg_index: int,
                      attribute_bgg_value: str) -> bool:
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
                         attribute_bgg_value: str) -> bool:
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
    def __instance_to_json(instance):
        return {
            "id": instance.id,
            "game_index": instance.game_index,
            "attribute_type_index": instance.attribute_type_index,
            "attribute_bgg_index": instance.attribute_bgg_index,
            "attribute_bgg_value": instance.attribute_bgg_value
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
                    "bgg_value": And(Use(str))
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
                                            attribute_bgg_value=v["bgg_value"])
            else:
                status = self.update_attribute(attribute_id=k,
                                               attribute_bgg_index=v["bgg_index"],
                                               attribute_bgg_value=v["bgg_value"])
        return status
