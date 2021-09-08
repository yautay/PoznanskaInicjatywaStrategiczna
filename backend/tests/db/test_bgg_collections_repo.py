from ..conftests import *
import json
from db.repository.collections import *
from tests.utils.user import create_random_user
from db.repository.collections import ORMWrapperCollection


path_test_data = os.path.join(os.path.abspath(os.getcwd()), "tests", "utils", "test_data")


def test_add_collection_from_data(db_session: Session):
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    assert ORMWrapperCollections().write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    assert len(db_session.query(BggUserCollection).all()) == 181


def test_update_collection_from_data(db_session: Session):
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    ORMWrapperCollections().write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    collection["23685"]["numplays"] = 13
    ORMWrapperCollections().write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    test_plays = db_session.query(BggUserCollection).filter(BggUserCollection.game_index == "23685")\
        .first().collection_numplays
    assert test_plays == 13


def test_delete_collection_from_data(db_session: Session):
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    ORMWrapperCollections().write_collection_to_db(db=db_session, user_id=user.id, bgg_data=collection)
    row = db_session.query(BggUserCollection).filter(BggUserCollection.game_index == "23685").first()
    ORMWrapperCollections().CRUD.delete_collection_row(db=db_session, existing_row=row)
    assert len(db_session.query(BggUserCollection).all()) == 180
