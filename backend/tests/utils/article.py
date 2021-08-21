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
        title = article.title
        content = article.content
        _id = article.id
        picture = article.picture
        articles.append([_id, title, content, picture])
        return articles


def assert_test_articles(retrieved_articles: List[Article], articles: List[Article]):
    for index in range(len(retrieved_articles)):
        assert retrieved_articles[index].id == articles[index][0]
        assert retrieved_articles[index].title == articles[index][1]
        assert retrieved_articles[index].content == articles[index][2]
        assert retrieved_articles[index].picture == articles[index][3]


def create_random_article(db: Session, user_id=1) -> Article:
    data = create_random_article_data()
    article_schema = ArticleCreate(title=data["title"], content=data["content"], picture=data["picture"])
    article = create_new_article(article=article_schema, user_id=user_id, db=db)
    return article


def create_random_article_data() -> dict:
    return {
        "title": random_lower_string(10),
        "content": random_lower_string(150),
        "picture": f"https://www.{random_lower_string(4)}.{random_lower_string(3)}.com/test.jpg",
    }
