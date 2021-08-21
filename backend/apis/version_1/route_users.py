from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user


router = APIRouter()


@router.post("/create", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(user, db)
