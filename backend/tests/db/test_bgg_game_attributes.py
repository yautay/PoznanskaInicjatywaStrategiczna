from ..conftests import *
from db.repository.games import BggGameAttributes
from db.repository.games import ORMWrapperAttributes, ORMWrapperAttributeTypes

# game_index = Column(Integer, ForeignKey("bgggame.game_index"), index=True)
#     attribute_type_index = Column(Integer, ForeignKey("bgggameattributestypes.attribute_type_index"))
#     attribute_bgg_index = Column(Integer, index=True)
#     attribute_bgg_value = Co


def add_test_attributes_types(db):
    attribute_types = {
        1: "alfa",
        2: "beta",
        3: "gama"
    }
    ORMWrapperAttributeTypes().write_game_attribute_types_to_db(db, attribute_types)


def test_crud_attributes(db_session: Session):
    attributes = {
        "12345": {
            "type_index": "1",
            "bgg_index": "2342",
            "bgg_value": "test value"
        },
        "1222345": {
            "type_index": "1",
            "bgg_index": "23432",
            "bgg_value": "test2 value"
        },
        "1235": {
            "type_index": "2",
            "bgg_index": "23412",
            "bgg_value": "test3 value"
        }
    }
    ORMWrapperAttributeTypes().write_game_attribute_types_to_db(db_session, attribute_types)
    ORMWrapperAttributeTypes().CRUD.delete_attribute_type(db_session, "test3")
    ORMWrapperAttributeTypes().CRUD.update_attribute_type(db_session, 54321, "changed")
    get_test_attributes = db_session.query(BggGameAttributesTypes)
    assert len(get_test_attributes.all()) == 2
    assert get_test_attributes.all()[1].attribute_type_name == "changed"


def test_add_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    ORMWrapperAttributes().CRUD.add_attribute(db=db_session,
                                            game_index=22222,
                                            attribute_type=2,
                                            bgg_attribute_index=1,
                                            bgg_attribute_value="Ed Haris")
    get_test_attributes = db_session.query(BggGameAttributes)
    assert len(get_test_attributes.all()) == 1
    assert get_test_attributes.first().attribute_bgg_value == "Ed Haris"


def test_update_attribute(db_session: Session):
    add_test_attributes_types(db_session)
    ORMWrapperAttributes().CRUD.add_attribute(db=db_session,
                                            game_index=22222,
                                            attribute_type=2,
                                            bgg_attribute_index=1,
                                            bgg_attribute_value="Ed Haris")
    ORMWrapperAttributes().CRUD.update_attribute(db=db_session, index="1", name="testup")
    assert db_session.query(BggGameAttributes).first() == 0


# def test_delete_attribute_type(db_session: Session):
#     attribute_type = ORMWrapperAttributeTypes().CRUD.add_attribute_type(db_session, 12345, "test")
#     assert len(db_session.query(BggGameAttributesTypes)
#                .filter(BggGameAttributesTypes.attribute_type_index == 12345).all()) == 1
#     ORMWrapperAttributeTypes().CRUD.delete_attribute_type(db_session, 12345)
#     assert len(db_session.query(BggGameAttributesTypes)
#                .filter(BggGameAttributesTypes.attribute_type_index == 12345).all()) == 0
