from ..conftests import *
from db.repository.bgg_attribute import ORMWrapperBggAttribute
from tests.utils.bgg_attribute import create_random_bgg_attribute_attrib, create_random_bgg_attribute_json


def test_add_bgg_attribute_attr(db_session: Session):
    data = create_random_bgg_attribute_attrib()
    assert ORMWrapperBggAttribute(db_session).create(data)


def test_add_bgg_attribute_json(db_session: Session):
    data = create_random_bgg_attribute_json()
    assert ORMWrapperBggAttribute(db_session).create(data)


def test_update_bgg_attribute_attr(db_session: Session):
    data = create_random_bgg_attribute_attrib()
    assert ORMWrapperBggAttribute(db_session).create(data)
    data["attribute_bgg_value"] = "changed"
    assert ORMWrapperBggAttribute(db_session).create(data)


def test_retrieve_bgg_attribute(db_session: Session):
    data = create_random_bgg_attribute_attrib()
    ORMWrapperBggAttribute(db_session).create(data)
    assert ORMWrapperBggAttribute(db_session).read(1)


def test_delete_bgg_attribute(db_session: Session):
    data = create_random_bgg_attribute_attrib()
    ORMWrapperBggAttribute(db_session).create(data)
    assert ORMWrapperBggAttribute(db_session).delete(1)
