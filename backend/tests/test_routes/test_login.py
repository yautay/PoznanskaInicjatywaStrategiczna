from ..conftests import *
from tests.utils.user import create_random_user_data
import json


def test_login_user_by_email(client):
    data = create_random_user_data(to_string=True)
    client.post("/user/create", json.dumps(data))
    response = client.post("/login/token", {"username": data["email"], "password": data["password"]})
    assert response.status_code == 200
    assert response.json()["access_token"] is not None
    assert response.json()["token_type"] == "bearer"


def test_login_user_by_login(client):
    data = create_random_user_data(to_string=True)
    client.post("/user/create", json.dumps(data))
    response = client.post("/login/token", {"username": data["login"], "password": data["password"]})
    assert response.status_code == 200
    assert response.json()["access_token"] is not None
    assert response.json()["token_type"] == "bearer"


def test_login_incorrect_password(client):
    data = create_random_user_data(to_string=True)
    client.post("/user/create", json.dumps(data))
    response = client.post("/login/token", {"username": data["login"], "password": "false_password"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"


def test_login_incorrect_login(client):
    data = create_random_user_data(to_string=True)
    client.post("/user/create", json.dumps(data))
    response = client.post("/login/token", {"username": "false_login", "password": data["password"]})
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"


