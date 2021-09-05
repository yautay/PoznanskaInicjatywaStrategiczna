from ..conftests import *
from db.repository.games import BggGameAttributesTypes
from db.repository.games import ORMWrapperAttributeTypes


path_test_data = os.path.join(os.path.abspath(os.getcwd()), "tests", "utils", "test_data")


def test_crud_attribute_types(db_session: Session):
    attribute_types = {
        12345: "test",
        54321: "test2",
        98764: "test3"
    }
    ORMWrapperAttributeTypes().write_game_attribute_types_to_db(db_session, attribute_types)
    ORMWrapperAttributeTypes().CRUD.delete_attribute_type(db_session, "test3")
    ORMWrapperAttributeTypes().CRUD.update_attribute_type(db_session, 54321, "changed")
    get_test_attributes = db_session.query(BggGameAttributesTypes)
    assert len(get_test_attributes.all()) == 2
    assert get_test_attributes.all()[1].attribute_type_name == "changed"


def test_add_attribute_types(db_session: Session):
    attribute_types = {
        12345: "test",
        54321: "test2",
        98764: "test3"
    }
    ORMWrapperAttributeTypes().write_game_attribute_types_to_db(db_session, attribute_types)
    get_test_attributes = db_session.query(BggGameAttributesTypes)
    assert len(get_test_attributes.all()) == 3
    assert get_test_attributes.all()[1].attribute_type_name == "test2"


def test_add_attribute_type(db_session: Session):
    attribute_type = ORMWrapperAttributeTypes().CRUD.add_attribute_type(db_session, 12345, "test")
    get_test_attribute = db_session.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == 12345)
    assert get_test_attribute.first().attribute_type_name == "test"


def test_update_attribute_type(db_session: Session):
    attribute_type = ORMWrapperAttributeTypes().CRUD.add_attribute_type(db_session, 12345, "test")
    assert db_session.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == 12345)\
        .first().attribute_type_name == "test"
    ORMWrapperAttributeTypes().CRUD.update_attribute_type(db_session, 12345, "test2")
    assert db_session.query(BggGameAttributesTypes).filter(BggGameAttributesTypes.attribute_type_index == 12345) \
               .first().attribute_type_name == "test2"


def test_delete_attribute_type(db_session: Session):
    attribute_type = ORMWrapperAttributeTypes().CRUD.add_attribute_type(db_session, 12345, "test")
    assert len(db_session.query(BggGameAttributesTypes)
               .filter(BggGameAttributesTypes.attribute_type_index == 12345).all()) == 1
    ORMWrapperAttributeTypes().CRUD.delete_attribute_type(db_session, 12345)
    assert len(db_session.query(BggGameAttributesTypes)
               .filter(BggGameAttributesTypes.attribute_type_index == 12345).all()) == 0
