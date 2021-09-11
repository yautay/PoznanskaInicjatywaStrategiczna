from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.models.pis_user import User
from db.session import get_db
from schemas.articles import \
    ArticleCreate, \
    ArticleShow
from db.repository.pis_articles import \
    create_new_article, \
    retrieve_article_by_id, \
    retrieve_articles_by_user, \
    retrieve_articles, \
    update_article_by_id, \
    delete_article_dy_id
from apis.version_1.route_login import get_current_user_from_token


router = APIRouter()


@router.post("/create", response_model=ArticleShow)
def create_article(article: ArticleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    if current_user.superuser or current_user.administrator:
        return create_new_article(article=article, db=db, user_id=current_user.id)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")


@router.get("/")
async def retrieve_article(article_id: int = None, user_id: int = None, db: Session = Depends(get_db)):
    if article_id:
        article = retrieve_article_by_id(_id=article_id, db=db)
        if not article:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {article_id} does not exist")
        return article
    elif user_id:
        articles = retrieve_articles_by_user(user_id=user_id, db=db)
        if not articles:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Articles with user_id {user_id} does not exist")
        return articles
    else:
        return retrieve_articles(db=db)


@router.put("/update/{_id}")
def update_article(_id: int, article: ArticleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    article_stored = retrieve_article_by_id(_id=_id, db=db)
    if article_stored:
        if article_stored.user_id == current_user.id or current_user.superuser:
            if update_article_by_id(article_id=_id, article=article, db=db, owner_id=current_user.id):
                return {"detail": "Successfully updated"}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {_id} does not exist")


@router.delete("/delete/{_id}")
def delete_article(_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    article = retrieve_article_by_id(_id=_id, db=db)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with id {_id} does not exist")
    elif article.user_id == current_user.id or current_user.superuser:
        delete_article_dy_id(article_id=_id, db=db)
        return {"detail": "Successfully deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
