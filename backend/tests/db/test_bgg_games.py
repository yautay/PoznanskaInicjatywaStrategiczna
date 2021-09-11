from ..conftests import *
from db.repository.bgg_games import ORMWrapperBggGame
from tests.utils.bgg_game import create_random_bgg_game


def test_add_bgg_game(db_session: Session):
    data = create_random_bgg_game()
    assert ORMWrapperBggGame(db_session).create(data)


def test_update_bgg_game(db_session: Session):
    data = create_random_bgg_game()
    assert ORMWrapperBggGame(db_session).create(data)
    data["attribute_bgg_value"] = "changed"
    assert ORMWrapperBggGame(db_session).create(data)


def test_retrieve_bgg_game(db_session: Session):
    data = create_random_bgg_game()
    ORMWrapperBggGame(db_session).create(data)
    assert ORMWrapperBggGame(db_session).read(1)


def test_delete_bgg_game(db_session: Session):
    data = create_random_bgg_game()
    ORMWrapperBggGame(db_session).create(data)
    assert ORMWrapperBggGame(db_session).delete(1)
