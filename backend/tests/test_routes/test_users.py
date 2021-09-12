from ..conftests import *
from tests.utils.user import create_random_user_data
import json


def test_create_user(client):
    data = create_random_user_data(to_string=True)
    response = client.post("/user/create", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == data["email"]
    assert response.json()["is_active"] is True


def test_create_user_validate_fields(client):
    data = create_random_user_data(to_string=True)
    data.pop("birthdate", None)
    response = client.post("/user/create", json.dumps(data))
    assert response.status_code == 422


def test_create_user_validate_email(client):
    data = create_random_user_data(to_string=True)
    data["email"] = "janusz@nie%$.pl"
    response = client.post("/user/create", json.dumps(data))
    assert response.status_code == 422
