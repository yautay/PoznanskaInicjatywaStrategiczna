from ..conftests import *
from sqlalchemy.orm import Session
from db.repository.pis_article import\
    create_new_article,\
    retrieve_article_by_id,\
    retrieve_articles,\
    retrieve_articles_by_user
from schemas.articles import ArticleCreate
from tests.utils.user import create_user
from tests.utils.article import \
    create_test_articles, \
    assert_test_articles


def test_retrieve_articles(db_session: Session):
    user = create_user(db=db_session)
    articles = create_test_articles(db=db_session)
    retrieved_articles = retrieve_articles(db=db_session)
    assert_test_articles(retrieved_articles, articles)


def test_retrieve_article_by_id(db_session: Session):
    article_title = "test_title"
    article_content = "content of article"
    article_picture = "https://www.wp.pl/test.jpg"
    user = create_user(db=db_session)
    article_schema = ArticleCreate(article_title=article_title, article_content=article_content, article_picture=article_picture)
    article = create_new_article(article=article_schema, db=db_session, user_id=user.id)
    retrieved_article = retrieve_article_by_id(_id=article.id, db=db_session)
    assert retrieved_article.id == article.id
    assert retrieved_article.article_title == article_title


def test_retrieve_articles_by_user(db_session: Session):
    user_1 = create_user(db=db_session)
    user_2 = create_user(db=db_session)
    articles_user_1 = create_test_articles(db=db_session, user_id=1)
    articles_user_2 = create_test_articles(db=db_session, user_id=2)
    retrieved_articles_user_1 = retrieve_articles_by_user(db=db_session, user_id=1)
    retrieved_articles_user_2 = retrieve_articles_by_user(db=db_session, user_id=2)
    assert_test_articles(retrieved_articles_user_1, articles_user_1)
    assert_test_articles(retrieved_articles_user_2, articles_user_2)
