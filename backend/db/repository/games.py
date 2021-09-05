from sqlalchemy.orm import Session
from datetime import datetime

from db.models.bgg_game import BggGame
from db.models.bgg_game_attributes import BggGameAttributes
from db.models.bgg_game_attributes_types import BggGameAttributesTypes

# attribute_type_index = Column(Integer, primary_key=True)
#     attribute_type_name = Column(String(50))
#     attributes = relationship("BggGameAttributes")


class ORMWrapperAttributeTypes:
    def write_game_attribute_types_to_db(self, db: Session, data: dict) -> bool:
        for k, v in data.items():
            existing_attribute_type = db.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == k)
            if not existing_attribute_type.first():
                status = self.CRUD.add_attribute_type(db=db, index=k, name=v)
            else:
                status = self.CRUD.update_attribute_type(db=db, existing_row=existing_attribute_type, name=v)
        return status

    class CRUD:
        @staticmethod
        def add_attribute_type(db: Session, index: int, name: str) -> bool:
            def create_attribute_type_row():
                row = BggGameAttributesTypes()
                row.attribute_type_index = index
                row.attribute_type_name = name
                return row
            row = create_attribute_type_row()
            try:
                db.add(row)
                db.commit()
                return True
            except:
                return False

        @staticmethod
        def get_attribute_type(db: Session, attribute: int or str) -> dict:
            if issubclass(attribute, int):
                row = db.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == attribute).first()
            elif issubclass(attribute, str):
                row = db.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_name == attribute).first()
            return {"attribute_id": row.attribute_type_index,
                    "attribute_name": row.attribute_type_name}

        @staticmethod
        def update_attribute_type(db: Session, index: int, name: str) -> bool:
            existing_data = db.query(BggGameAttributesTypes).filter(
                BggGameAttributesTypes.attribute_type_index == index).first()
            if existing_data.name != name:
                existing_data.name = name
                try:
                    db.commit()
                    return True
                except:
                    return False
            return False

        @staticmethod
        def delete_attribute_type(db: Session, attribute: int or str) -> bool:
            if issubclass(attribute, int):
                row = db.query(BggGameAttributesTypes).filter(
                    BggGameAttributesTypes.attribute_type_index == attribute).first()
            elif issubclass(attribute, str):
                row = db.query(BggGameAttributesTypes).filter(
                    BggGameAttributesTypes.attribute_type_name == attribute).first()
            try:
                db.delete(row)
                db.commit()
                return True
            except:
                return False


class ORMWrapperAttributes:
    def write_game_attributes_to_db(self, db: Session, data: dict) -> bool:
        for k, v in data.items():
            existing_attribute_type = db.query(BggGameAttributesTypes).filter(
                BggGameAttributesTypes.attribute_type_index == k)
            if not existing_attribute_type.first():
                status = self.CRUD.add_attribute_type(db=db, index=k, name=v)
            else:
                status = self.CRUD.update_attribute_type(db=db, existing_row=existing_attribute_type, name=v)
        return status

    class CRUD:
        @staticmethod
        def add_attribute(db: Session, game_index: int,
                          attribute_type: int or str,
                          bgg_attribute_index: int,
                          bgg_attribute_value: str) -> bool:

            def get_type():
                if isinstance(attribute_type, int):
                    return db.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == attribute_type).first()
                else:
                    return db.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_name == attribute_type).first()

            def create_attribute_row():
                row = BggGameAttributes()
                row.game_index = game_index
                row.attribute_type_index = attribute_type
                row.attribute_bgg_index = bgg_attribute_index
                row.attribute_bgg_value = bgg_attribute_value
                return row

            row = create_attribute_row()
            try:
                db.add(row)
                db.commit()
                return True
            except:
                return False

        @staticmethod
        def get_attribute(db: Session, attribute: int or str) -> dict:
            if issubclass(attribute, int):
                row = db.query(BggGameAttributesTypes).filter(
                    BggGameAttributesTypes.attribute_type_index == attribute).first()
            elif issubclass(attribute, str):
                row = db.query(BggGameAttributesTypes).filter(
                    BggGameAttributesTypes.attribute_type_name == attribute).first()
            return {"attribute_id": row.attribute_type_index,
                    "attribute_name": row.attribute_type_name}

        @staticmethod
        def update_attribute(db: Session, index: int, name: str) -> bool:
            existing_data = db.query(BggGameAttributesTypes).filter(
                BggGameAttributesTypes.attribute_type_index == index).first()
            if existing_data.name != name:
                existing_data.name = name
                try:
                    db.commit()
                    return True
                except:
                    return False
            return False

        @staticmethod
        def delete_attribute(db: Session, attribute: int or str) -> bool:
            if issubclass(attribute, int):
                row = db.query(BggGameAttributesTypes).filter(
                    BggGameAttributesTypes.attribute_type_index == attribute).first()
            elif issubclass(attribute, str):
                row = db.query(BggGameAttributesTypes).filter(
                    BggGameAttributesTypes.attribute_type_name == attribute).first()
            try:
                db.delete(row)
                db.commit()
                return True
            except:
                return False
