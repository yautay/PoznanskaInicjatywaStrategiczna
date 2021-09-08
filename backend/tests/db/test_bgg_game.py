from ..conftests import *
from db.repository.games import ORMWrapperGame
from tests.utils.game import create_random_game_data, random_index
from db.models.bgg_game import BggGame


def test_add_game_from_data(db_session: Session):
    game = {random_index(1): create_random_game_data()}
    db = ORMWrapperGame(db_session)
    assert db.write_games_to_db(game)


def test_add_games_from_data(db_session: Session):
    games = {
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
        random_index(1): create_random_game_data(),
    }
    db = ORMWrapperGame(db_session)
    assert db.write_games_to_db(games)
    assert len(db_session.query(BggGame).all()) == len(games)


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


def test_delete_game_by_index(db_session: Session):
    db = ORMWrapperGame(db_session)
    index = random_index(1)
    data = {index: create_random_game_data()}
    db.add_game(data)
    db.delete_game_by_bgg_index(game_index=index)
    assert not db.get_game_by_bgg_index(game_index=index)


def test_delete_game_by_id(db_session: Session):
    db = ORMWrapperGame(db_session)
    index = random_index(1)
    data = {index: create_random_game_data()}
    db.add_game(data)
    _id = db.get_game_by_bgg_index(game_index=index)["game_id"]
    db.delete_game_by_id(game_id=_id)
    assert not db.get_game_by_id(game_id=_id)
