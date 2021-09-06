from ..conftests import *
from db.repository.games import ORMWrapperGame
from tests.utils.game import create_random_game_data, random_index


def test_crud_games(db_session: Session):
    pass


def test_add_game(db_session: Session):
    db = ORMWrapperGame(db_session)
    index = random_index(1)
    data = {index: create_random_game_data()}
    assert db.add_game(data)
    assert len(db.get_game_by_bgg_index(index)) == 9


def test_update_game(db_session: Session):
    db = ORMWrapperGame(db_session)
    index = random_index(1)
    data = {index: create_random_game_data()}
    data2 = {index: create_random_game_data()}
    db.add_game(data)
    assert db.update_game(data2)


def test_partial_update_game(db_session: Session):
    db = ORMWrapperGame(db_session)
    index = random_index(1)
    data = {index: create_random_game_data()}
    db.add_game(data)
    data[index] = {"game_description": "test changed"}
    assert db.update_game(data)
    assert db.get_game_by_bgg_index(index)["game_description"] == "test changed"

