from sqlalchemy.orm import Session
from typing import List

from schemas.articles import ArticleCreate
from db.models.article import Article


def create_new_article(article: ArticleCreate, db: Session, user_id: int):
    article = Article(**article.dict(), user_id=user_id)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def retrieve_article_by_id(_id: int, db: Session) -> Article:
    return db.query(Article).filter(Article.id == _id).first()


def retrieve_articles_by_user(user_id: int, db: Session) -> List[Article]:
    return db.query(Article).filter(Article.user_id == user_id).all()


def retrieve_articles(db: Session) -> List[Article]:
    return db.query(Article).all()


def update_article_by_id(article_id: int, article: ArticleCreate, db: Session, owner_id: int) -> bool:
    existing_article = db.query(Article).filter(Article.id == article_id)
    if not existing_article.first():
        return False
    article.dict().update(owner_id=owner_id)
    existing_article.update(article.dict())
    db.commit()
    return True


def delete_article_dy_id(article_id: int, db: Session) -> bool:
    existing_article = db.query(Article).filter(Article.id == article_id)
    if not existing_article.first():
        return False
    existing_article.delete(synchronize_session=False)
    db.commit()
    return True
