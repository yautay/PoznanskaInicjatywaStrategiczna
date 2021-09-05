from ..conftests import *
from db.repository.games import BggGameAttributes, BggGameAttributesTypes
from db.repository.games import ORMWrapperAttributes, ORMWrapperAttributeTypes


def test_crud_attributes(db_session: Session):
    add_test_attributes_types(db_session)
    attributes = {
        "12345": {
            "type_index": 1,
            "bgg_index": 2342,
            "bgg_value": "test value"
        },
        "1222345": {
            "type_index": 1,
            "bgg_index": 23432,
            "bgg_value": "test2 value"
        },
        "1235": {
            "type_index": 2,
            "bgg_index": 23412,
            "bgg_value": "test3 value"
        }
    }
    assert ORMWrapperAttributes().write_attributes_to_db(db=db_session, data=attributes)
    # TODO przerobić
    att = db_session.query(BggGameAttributes).all()
    for a in att:
        print(a.id)
    assert ORMWrapperAttributes().CRUD.delete_attribute(db=db_session,
                                                        attribute_id=1222345)
    print(db_session.query(BggGameAttributes).all())
    assert ORMWrapperAttributes().CRUD.update_attribute(db=db_session,
                                                        attribute_id=1235,
                                                        attribute_bgg_index=111,
                                                        attribute_bgg_value="changed")
    assert len(db_session.query(BggGameAttributes).all()) == 2
    assert db_session.query(BggGameAttributes).filter(BggGameAttributes.id == 1235)\
        .first().attribute_bgg_value == "changed"


def test_add_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    ORMWrapperAttributes().CRUD.add_attribute(db=db_session,
                                              game_index=22222,
                                              attribute_type=2,
                                              attribute_bgg_index=1,
                                              attribute_bgg_value="Ed Haris")
    get_test_attributes = db_session.query(BggGameAttributes)
    assert len(get_test_attributes.all()) == 1
    assert get_test_attributes.first().attribute_bgg_value == "Ed Haris"


def test_update_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    ORMWrapperAttributes().CRUD.add_attribute(db=db_session,
                                              game_index=22222,
                                              attribute_type=2,
                                              attribute_bgg_index=1,
                                              attribute_bgg_value="Ed Haris")
    ORMWrapperAttributes().CRUD.update_attribute(db=db_session,
                                                 attribute_id=1,
                                                 attribute_bgg_index=3,
                                                 attribute_bgg_value="changed")
    assert db_session.query(BggGameAttributes).first().attribute_bgg_value == "changed"


def test_delete_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    ORMWrapperAttributes().CRUD.add_attribute(db=db_session,
                                              game_index=22222,
                                              attribute_type=2,
                                              attribute_bgg_index=1,
                                              attribute_bgg_value="Ed Haris")
    ORMWrapperAttributes().CRUD.delete_attribute(db=db_session, attribute_id=1)
    assert not db_session.query(BggGameAttributes).all()


def add_test_attributes_types(db):
    attribute_types = {
        1: "alfa",
        2: "beta",
        3: "gama"
    }
    ORMWrapperAttributeTypes().write_game_attribute_types_to_db(db, attribute_types)