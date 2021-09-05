from sqlalchemy.orm import Session
from datetime import datetime

from db.models.bgg_game import BggGame
from db.models.bgg_game_attributes import BggGameAttributes
from db.models.bgg_game_attributes_types import BggGameAttributesTypes


class ORMWrapperAttributeTypes:
    def write_game_attribute_types_to_db(self, db: Session, data: dict) -> bool:
        for k, v in data.items():
            existing_attribute_type = db.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == k)
            if not existing_attribute_type.first():
                status = self.CRUD.add_attribute_type(db=db, attribute_type_index=k, attribute_type_name=v)
            else:
                status = self.CRUD.update_attribute_type(db=db,
                                                         attribute_type_index=existing_attribute_type,
                                                         attribute_type_name=v)
        return status

    class CRUD:
        @staticmethod
        def add_attribute_type(db: Session, attribute_type_index: int, attribute_type_name: str) -> bool:
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

        @staticmethod
        def get_attribute_type(db: Session, attribute_type_index: int or str) -> dict:
            if issubclass(attribute_type_index, int):
                row = db.query(BggGameAttributesTypes)\
                    .filter(BggGameAttributesTypes.attribute_type_index == attribute_type_index).first()
            elif issubclass(attribute_type_index, str):
                row = db.query(BggGameAttributesTypes)\
                    .filter(BggGameAttributesTypes.attribute_type_name == attribute_type_index).first()
            return {"attribute_id": row.attribute_type_index,
                    "attribute_name": row.attribute_type_name}

        @staticmethod
        def update_attribute_type(db: Session, attribute_type_index: int, attribute_type_name: str) -> bool:
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

        @staticmethod
        def delete_attribute_type(db: Session, attribute_id: int or str) -> bool:
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


class ORMWrapperAttributes:
    def write_attributes_to_db(self, db: Session, data: dict) -> bool:
        for k, v in data.items():
            existing_attribute = db.query(BggGameAttributes).filter(
                BggGameAttributes.id == k)
            if not existing_attribute.first():
                status = self.CRUD.add_attribute(db=db,
                                                 game_index=k,
                                                 attribute_type=v["type_index"],
                                                 attribute_bgg_index=v["bgg_index"],
                                                 attribute_bgg_value=v["bgg_value"])
            else:
                status = self.CRUD.update_attribute(db=db,
                                                    attribute_id=k,
                                                    attribute_bgg_index=v["bgg_index"],
                                                    attribute_bgg_value=v["bgg_value"])
        return status

    class CRUD:
        @staticmethod
        def add_attribute(db: Session,
                          game_index: int,
                          attribute_type: int or str,
                          attribute_bgg_index: int,
                          attribute_bgg_value: str) -> bool:

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

        @staticmethod
        def get_attribute_by_id(db: Session, attribute_id: int):
            try:
                # TODO zwracać JSON
                return db.query(BggGameAttributes).filter(BggGameAttributes.id == attribute_id).first()
            except:
                return None

        @staticmethod
        def get_attribute_by_game_index(db: Session, bgg_game_index: int):
            try:
                # TODO zwracać JSON
                return db.query(BggGameAttributes).filter(BggGameAttributes.game_index == bgg_game_index).all()
            except:
                return None

        @staticmethod
        def update_attribute(db: Session,
                             attribute_id: int,
                             attribute_bgg_index: int,
                             attribute_bgg_value: str) -> bool:
            existing_data = db.query(BggGameAttributes).filter(
                BggGameAttributes.id == attribute_id).first()
            if existing_data.attribute_bgg_index != attribute_bgg_index:
                existing_data.attribute_bgg_index = attribute_bgg_index
            if existing_data.attribute_bgg_value != attribute_bgg_value:
                existing_data.attribute_bgg_value = attribute_bgg_value
            try:
                db.commit()
                return True
            except:
                return False

        @staticmethod
        def delete_attribute(db: Session, attribute_id: int) -> bool:
            row = db.query(BggGameAttributes).filter(BggGameAttributes.id == attribute_id).first()
            try:
                db.delete(row)
                db.commit()
                return True
            except:
                return False
