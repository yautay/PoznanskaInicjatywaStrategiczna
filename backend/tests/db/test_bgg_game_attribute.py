from ..conftests import *
from tests.utils.bgg_game_attribute import create_random_bgg_game_attribute
from db.repository.bgg_game_attribute import ORMWrapperBggGameAttribute
from db.repository.bgg_attribute import ORMWrapperBggAttribute


def test_add_bgg_game_attribute(db_session: Session):
    data = create_random_bgg_game_attribute()
    assert ORMWrapperBggGameAttribute(db_session).create(data)


def test_retrieve_bgg_game_attribute(db_session: Session):
    data = create_random_bgg_game_attribute()
    ORMWrapperBggGameAttribute(db_session).create(data)
    assert ORMWrapperBggGameAttribute(db_session).read(1)


def test_delete_bgg_game_attribute(db_session: Session):
    data = create_random_bgg_game_attribute()
    ORMWrapperBggGameAttribute(db_session).create(data)
    assert ORMWrapperBggGameAttribute(db_session).delete(1)
