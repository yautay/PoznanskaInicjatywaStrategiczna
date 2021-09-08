from ..conftests import *
from db.repository.games import BggGameAttributes, BggGameAttributesTypes
from db.repository.games import ORMWrapperAttributes, ORMWrapperAttributeTypes


def test_crud_attributes(db_session: Session):
    db = ORMWrapperAttributes(db_session)
    add_test_attributes_types(db_session)
    test_attributes = {
        12345: {
            "type_index": 1,
            "bgg_index": 2342,
            "bgg_value": "test value"
        },
        1222345: {
            "type_index": 1,
            "bgg_index": 23432,
            "bgg_value": "test2 value"
        },
        1235: {
            "type_index": 2,
            "bgg_index": 23412,
            "bgg_value": "test3 value"
        }
    }
    assert db.write_attributes_to_db(data=test_attributes)
    attributes = db.get_attributes_by_game_index(game_index=1222345)
    assert len(attributes) == 1
    assert db.delete_attribute(attribute_id=attributes[0]["id"])
    attributes = db.get_attributes_by_game_index(game_index=1235)
    assert db.update_attribute(attribute_id=attributes[0]["id"],
                               attribute_bgg_index=111,
                               attribute_bgg_value="changed")
    assert len(db_session.query(BggGameAttributes).all()) == 2
    assert db.get_attribute_by_id(attribute_id=attributes[0]["id"])["attribute_bgg_value"] == "changed"


def test_add_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    ORMWrapperAttributes(db_session).add_attribute(game_index=22222,
                                                   attribute_type=2,
                                                   attribute_bgg_index=1,
                                                   attribute_bgg_value="Ed Haris")
    retrieved_attributes = db_session.query(BggGameAttributes)
    assert len(retrieved_attributes.all()) == 1
    assert retrieved_attributes.first().attribute_bgg_value == "Ed Haris"


def test_update_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    db = ORMWrapperAttributes(db_session)
    db.add_attribute(game_index=22222,
                     attribute_type=2,
                     attribute_bgg_index=1,
                     attribute_bgg_value="Ed Haris")
    db.update_attribute(attribute_id=1,
                        attribute_bgg_index=3,
                        attribute_bgg_value="changed")
    assert db.get_attribute_by_id(1)["attribute_bgg_value"] == "changed"


def test_delete_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    db = ORMWrapperAttributes(db_session)
    db.add_attribute(game_index=22222,
                     attribute_type=2,
                     attribute_bgg_index=1,
                     attribute_bgg_value="Ed Haris")
    db.delete_attribute(1)
    assert not db_session.query(BggGameAttributes).all()


def add_test_attributes_types(db):
    attribute_types = {
        1: "alfa",
        2: "beta",
        3: "gama"
    }
    ORMWrapperAttributeTypes(db).write_game_attributes_types_to_db(attribute_types)
