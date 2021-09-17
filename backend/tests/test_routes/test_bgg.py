import json
from logs import logger
from ..conftests import *
from tests.utils.user import create_user, create_random_user_data
from db.repository.bgg_game import ORMWrapperBggGame
from db.repository.bgg_attribute import ORMWrapperBggAttribute
from db.repository.bgg_game_attribute import ORMWrapperBggGameAttribute
from db.repository.pis_users import PisUser

logger = logger.get_logger(__name__)


def test_synchro_collection_by_user_normal(client, normal_user_token_headers):
    data = {"bgg_user": "testxy"}
    response = client.post("/bgg/collection", json.dumps(data), headers=normal_user_token_headers)
    logger.info(f"url: {response.url}, params: {response.json()}")
    assert response.status_code == 401


def test_synchro_collection_by_user_not_authorized(client, normal_user_token_headers):
    data = {"bgg_user": "not_test"}
    response = client.post("/bgg/collection", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 401


def test_synchro_collection_process(client, super_user_token_headers, db_session: Session):
    test_user_data = create_random_user_data()
    test_user_data["bgg_user"] = "yautay"
    create_user(db_session, test_user_data)
    data = {"bgg_user": "yautay"}
    response = client.post("/bgg/collection", json.dumps(data), headers=super_user_token_headers)
    assert response.status_code == 200
