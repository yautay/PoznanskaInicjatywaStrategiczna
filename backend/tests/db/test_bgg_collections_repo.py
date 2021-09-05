from ..conftests import *
import json
from db.repository.collections import *
from tests.utils.user import create_random_user
from db.repository.collections import write_collection_to_db


path_test_data = os.path.join(os.path.abspath(os.getcwd()), "tests", "utils", "test_data")


def test_add_collection_from_data(db_session: Session):
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    assert write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    assert db_session.query(BggUserCollection).all().len() == 12


def test_update_collection_from_data(db_session: Session):
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    collection["23685"]["numplays"] = 13
    write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    test_plays = db_session.query(BggUserCollection).filter(BggUserCollection.game_index == "23685").first().collection_numplays
    assert 13 == test_plays