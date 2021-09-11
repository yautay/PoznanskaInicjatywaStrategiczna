from ..conftests import *
import json
from db.repository.bgg_collections import *
from tests.utils.user import create_random_user
from db.repository.bgg_collections import ORMWrapperCollection


path_test_data = os.path.join(os.path.abspath(os.getcwd()), "tests", "utils", "test_data")


def test_add_collection_from_data(db_session: Session):
    db = ORMWrapperCollection(db_session)
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    assert db.write_user_collections_to_db(user_id=user.id, bgg_data=collection)
    assert len(db_session.query(BggUserCollection).all()) == 181


def test_update_collection_from_data(db_session: Session):
    db = ORMWrapperCollection(db_session)
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    db.write_user_collections_to_db(user_id=user.id, bgg_data=collection)
    collection["23685"]["numplays"] = 13
    db.update_collection(db_session.query(BggUserCollection).filter(BggUserCollection.id == 1).first(),
                         collection["23685"])
    test_plays = db.get_collection_by_id(1)
    assert test_plays["collection_numplays"] == 13


def test_delete_collection_from_data(db_session: Session):
    db = ORMWrapperCollection(db_session)
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    db.write_user_collections_to_db(user_id=user.id, bgg_data=collection)
    assert db.get_collection_by_id(1)
    assert db.delete_collection_by_id(1)
    assert not db.get_collection_by_id(1)


def test_delete_user_collections(db_session: Session):
    db = ORMWrapperCollection(db_session)
    user = create_random_user(db_session)
    collection_test_data = os.path.join(path_test_data, "collection.json")
    with open(collection_test_data, "r") as data:
        collection = json.loads(data.read())
    db.write_user_collections_to_db(user_id=user.id, bgg_data=collection)
    assert db.get_collections_by_user_id(user.id)
    db.delete_user_collections(user.id)
    assert not db.get_collections_by_user_id(user.id)