import json
import logging
from ..conftests import *

logger = logging.getLogger("TestsBgg")


def test_synchro_collection_by_user_normal(client, normal_user_token_headers):
    data = {"bgg_user": "testxx"}
    response = client.post("/bgg/collection", json.dumps(data), headers=normal_user_token_headers)
    logger.info(f"url: {response.url}, params: {response.json()}")
    assert response.status_code == 401


def test_synchro_collection_by_user_not_authorized(client, normal_user_token_headers):
    data = {"bgg_user": "not_test"}
    response = client.post("/bgg/collection", json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 401


def test_synchro_collection_process(client, super_user_token_headers):
    data = {"bgg_user": "test"}
    response = client.post("/bgg/collection", json.dumps(data), headers=super_user_token_headers)
    assert response.status_code == 200
