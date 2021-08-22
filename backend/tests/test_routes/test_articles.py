from ..conftests import *
from tests.utils.article import create_random_article_data
import datetime
import json


def test_create_article(client, super_user_token_headers):
    data = create_random_article_data()
    response = __create_article_from_data(client, data, headers=super_user_token_headers)
    assert response.status_code == 200
    assert response.json()["title"] == data["title"]
    assert response.json()["created_at"] == str(datetime.date.today())
    assert response.json()["is_active"] is False


def test_create_active_article(client, super_user_token_headers):
    data = create_random_article_data()
    data["is_active"] = True
    response = __create_article_from_data(client, data, headers=super_user_token_headers)
    assert response.status_code == 200
    assert response.json()["title"] == data["title"]
    assert response.json()["created_at"] == str(datetime.date.today())
    assert response.json()["is_active"] is True


def test_create_article_with_date(client, super_user_token_headers):
    data = create_random_article_data()
    data["created_at"] = "2019-08-18"
    response = __create_article_from_data(client, data, headers=super_user_token_headers)
    assert response.status_code == 200
    assert response.json()["title"] == data["title"]
    assert response.json()["created_at"] == "2019-08-18"
    assert response.json()["is_active"] is False


def test_retrieve_article_by_id(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    response = client.get("/article/?article_id=1")
    assert response.status_code == 200
    assert response.json()["title"] == data["title"]


def test_retrieve_article_by_id_not_exist(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    response = client.get("/article/?article_id=2")
    assert response.status_code == 404


def test_retrieve_article_by_user(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    response = client.get("/article/?user_id=1")
    assert response.status_code == 200
    assert response.json()[0]["title"] == data["title"]


def test_retrieve_articles(client, super_user_token_headers):
    articles = __create_test_articles(client, super_user_token_headers)
    response = client.get("/article/")
    assert response.status_code == 200
    __assert_test_articles(response.json(), articles)


def test_update_article_by_id(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    updated_data = create_random_article_data()
    response = client.put("/article/update/1", json.dumps(updated_data), headers=super_user_token_headers)
    assert response.status_code == 200


def test_update_article_by_id_fail(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    updated_data = create_random_article_data()
    response = client.put("/article/update/8", json.dumps(updated_data), headers=super_user_token_headers)
    assert response.status_code == 404


def test_delete_article_by_id(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    response = client.delete("/article/delete/1", headers=super_user_token_headers)
    assert response.status_code == 200


def test_delete_article_by_id_fail(client, super_user_token_headers):
    data = create_random_article_data()
    __create_article_from_data(client, data, headers=super_user_token_headers)
    response = client.delete("/article/delete/9", headers=super_user_token_headers)
    assert response.status_code == 404


def __create_test_articles(client, super_user_token_headers, count=10):
    articles = []
    for article in range(count):
        data = create_random_article_data()
        articles.append(data)
        __create_article_from_data(client, data, headers=super_user_token_headers)
        return articles


def __assert_test_articles(retrieved_articles, articles):
    for index in range(len(retrieved_articles)):
        assert retrieved_articles[index]["title"] == articles[index]["title"]
        assert retrieved_articles[index]["content"] == articles[index]["content"]
        assert retrieved_articles[index]["picture"] == articles[index]["picture"]


def __create_article_from_data(client, data, headers=None):
    return client.post("/article/create", json.dumps(data), headers=headers)
