from ..conftests import *
from tests.utils.bgg_game_marketplace import create_random_bgg_game_marketplace
from db.repository.bgg_game_marketplace import ORMWrapperBggGameMarketplace


def test_add_bgg_game_marketplace(db_session: Session):
    data = create_random_bgg_game_marketplace()
    assert ORMWrapperBggGameMarketplace(db_session).create(data)


def test_retrieve_bgg_game_marketplace(db_session: Session):
    data = create_random_bgg_game_marketplace()
    ORMWrapperBggGameMarketplace(db_session).create(data)
    assert ORMWrapperBggGameMarketplace(db_session).read(1)


def test_delete_bgg_game_marketplace(db_session: Session):
    data = create_random_bgg_game_marketplace()
    ORMWrapperBggGameMarketplace(db_session).create(data)
    assert ORMWrapperBggGameMarketplace(db_session).delete(1)
