from ..conftests import *
from db.repository.bgg_user_collection import ORMWrapperBggUserCollection
from tests.utils.bgg_user_collection import create_random_bgg_user_collection


def test_add_bgg_user_collection(db_session: Session):
    data = create_random_bgg_user_collection()
    assert ORMWrapperBggUserCollection(db_session).create(data)


def test_update_bgg_user_collection(db_session: Session):
    data = create_random_bgg_user_collection()
    ORMWrapperBggUserCollection(db_session).create(data)
    data.pop("collection_updated")
    data["collection_comment"] = "changed"
    assert ORMWrapperBggUserCollection(db_session).create(data)


def test_retrieve_bgg_user_collection(db_session: Session):
    data = create_random_bgg_user_collection()
    ORMWrapperBggUserCollection(db_session).create(data)
    assert ORMWrapperBggUserCollection(db_session).read(1)


def test_delete_bgg_user_collection(db_session: Session):
    data = create_random_bgg_user_collection()
    ORMWrapperBggUserCollection(db_session).create(data)
    assert ORMWrapperBggUserCollection(db_session).delete(1)
