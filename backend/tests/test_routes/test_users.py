import json


def test_create_user(client):
    data = {
        "login": "test_login",
        "password": "test_password",
        "email": "test@example.com",
        "name": "Janusz",
        "surname": "Użytkownik",
        "age": 14,
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
