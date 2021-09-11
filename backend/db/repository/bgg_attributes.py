import datetime
from typing import List
from schema import Schema, And, Use, Optional, SchemaError, Or
from sqlalchemy import JSON, and_, not_, or_

from sqlalchemy.orm import Session

from db.models.bgg_game import BggGame
from db.models.bgg_attributes import BggAttributes
from db.models.bgg_game_attributes import BggGameAttributes
from db.models.bgg_game_attributes_types import BggGameAttributesTypes


class ORMWrapperAttributesCRUD(object):
    def __init__(self, db: Session):
        self.db = db

    def add_attribute(self,
                      game_index: int,
                      attribute_type: int,
                      attribute_bgg_index: int or None,
                      attribute_bgg_value: str or None,
                      attribute_bgg_json: dict or None = None) -> bool:
        db = self.db

        def create_bgg_attribute() -> BggAttributes:
            row = BggAttributes()
            row.attribute_bgg_index = attribute_bgg_index
            row.attribute_bgg_value = attribute_bgg_value
            row.attribute_bgg_json = attribute_bgg_json
            return row

        def create_game_attribute_row(attribute_id: int) -> BggGameAttributes:
            row = BggGameAttributes()
            row.game_index = game_index
            row.attribute_type_index = attribute_type
            row.attribute = attribute_id
            return row

        bgg_attribute = create_bgg_attribute()
        try:
            db.add(bgg_attribute)
            db.commit()
        except:
            return False

        game_attribute = create_game_attribute_row(bgg_attribute.id)
        try:
            db.add(game_attribute)
            db.commit()
            return True
        except:
            return False

    def update_attribute(self,
                         attribute_id: int,
                         attribute_bgg_index: int,
                         attribute_bgg_value: str,
                         attribute_bgg_json: dict or None = None) -> bool:
        changed = False
        db = self.db
        try:
            existing_bgg_attribute: BggAttributes = db.query(BggAttributes) \
                .filter(BggAttributes.id == attribute_id).first()

            if existing_bgg_attribute.attribute_bgg_index != attribute_bgg_index:
                existing_bgg_attribute.attribute_bgg_index = attribute_bgg_index
                changed = True
            if existing_bgg_attribute.attribute_bgg_value != attribute_bgg_value:
                existing_bgg_attribute.attribute_bgg_value = attribute_bgg_value
                changed = True
            if attribute_bgg_json:
                if existing_bgg_attribute.attribute_bgg_json != attribute_bgg_json:
                    existing_bgg_attribute.attribute_bgg_json = attribute_bgg_json
                    changed = True
            if changed:
                db.commit()
                return True
            else:
                return False
        except:
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

    def get_attribute_by_id(self, attribute_id: int) -> dict or None:
        db = self.db
        try:
            instance = db.query(BggGameAttributes).filter(BggGameAttributes.id == attribute_id).first()
            return self.__instance_to_json(instance, db)
        except:
            return None

    def get_attributes_by_game_index(self, game_index: int) -> List[dict] or None:
        db = self.db
        data = []
        try:
            instances = db.query(BggGameAttributes).filter(BggGameAttributes.game_index == game_index).all()
            for instance in instances:
                data.append(self.__instance_to_json(instance, db))
            return data
        except:
            return None

    @staticmethod
    def __instance_to_json(instance: BggGameAttributes, db: Session) -> dict:
        bgg_attribute: BggAttributes = db.query(BggAttributes).filter(BggAttributes.id == instance.attribute).first()
        return {
            "id": instance.id,
            "game_index": instance.game_index,
            "attribute_type_index": instance.attribute_type_index,
            "attribute_bgg_index": bgg_attribute.attribute_bgg_index,
            "attribute_bgg_value": bgg_attribute.attribute_bgg_value,
            "attribute_bgg_json": bgg_attribute.attribute_bgg_json
        }


class ORMWrapperAttributes(ORMWrapperAttributesCRUD):
    def __init__(self, db: Session):
        super().__init__(db)
        self.db = db

    def write_attributes_to_db(self, data: list) -> bool:
        def check_schema(dict_data):
            data_schema = Schema({
                Use(int): {
                    "type_index": And(Use(str)),
                    "bgg_index": And(Use(str)),
                    "bgg_value": And(Use(str)),
                    "bgg_json": Or({object: object}, None)
                }})
            try:
                data_schema.validate(dict_data)
                return True
            except SchemaError:
                return False
        for index in data:
            if not check_schema(index):
                return False
            for game_index, v in index.items():
                instance = self.add_attribute(game_index=game_index,
                                              attribute_type=v["type_index"],
                                              attribute_bgg_index=v["bgg_index"],
                                              attribute_bgg_value=v["bgg_value"],
                                              attribute_bgg_json=v["bgg_json"])
                if not instance:
                    return False
        return True

    def delete_attributes_by_game_index(self, game_index: list) -> bool:
        db = self.db

        def delete_game_attribs(game_i: int) -> bool:
            try:
                attributes: List[BggAttributes] = db.query(BggGameAttributes)\
                    .filter(BggGameAttributes.game_index == game_i).all()
                for attribute in attributes:
                    db.delete(attribute)
                db.commit()
                return True
            except:
                return False
        for game in game_index:
            x = delete_game_attribs(game)
            if not x:
                return False
        return True
