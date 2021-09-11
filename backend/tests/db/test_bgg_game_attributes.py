from ..conftests import *
from tests.utils.bgg_game_attribute import create_random_bgg_game_attribute
from db.repository.bgg_game_attributes import ORMWrapperBggGameAttributes


def test_add_bgg_game_attribute(db_session: Session):
    data = create_random_bgg_game_attribute()
    assert ORMWrapperBggGameAttributes(db_session).create(data)


def test_retrieve_bgg_game_attribute(db_session: Session):
    data = create_random_bgg_game_attribute()
    ORMWrapperBggGameAttributes(db_session).create(data)
    assert ORMWrapperBggGameAttributes(db_session).read(1)


def test_delete_bgg_game_attribute(db_session: Session):
    data = create_random_bgg_game_attribute()
    ORMWrapperBggGameAttributes(db_session).create(data)
    assert ORMWrapperBggGameAttributes(db_session).delete(1)
