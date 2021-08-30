from sqlalchemy.orm import Session
from typing import List

from db.models.article import Article
from schemas.articles import ArticleCreate
from db.repository.articles import create_new_article
from tests.utils.randoms import random_lower_string


def create_test_articles(db: Session, user_id=1, count=10) -> list:
    articles = []
    for instance in range(count):
        article = create_random_article(db=db, user_id=user_id)
        article_title = article.article_title
        article_content = article.article_content
        _id = article.id
        article_picture = article.article_picture
        articles.append([_id, article_title, article_content, article_picture])
        return articles


def assert_test_articles(retrieved_articles: List[Article], articles: List[Article]):
    for index in range(len(retrieved_articles)):
        assert retrieved_articles[index].id == articles[index][0]
        assert retrieved_articles[index].article_title == articles[index][1]
        assert retrieved_articles[index].article_content == articles[index][2]
        assert retrieved_articles[index].article_picture == articles[index][3]


def create_random_article(db: Session, user_id=1) -> Article:
    data = create_random_article_data()
    article_schema = ArticleCreate(article_title=data["article_title"], article_content=data["article_content"], article_picture=data["article_picture"])
    article = create_new_article(article=article_schema, user_id=user_id, db=db)
    return article


def create_random_article_data() -> dict:
    return {
        "article_title": random_lower_string(10),
        "article_content": random_lower_string(150),
        "article_picture": f"https://www.{random_lower_string(4)}.{random_lower_string(3)}.com/test.jpg",
    }
