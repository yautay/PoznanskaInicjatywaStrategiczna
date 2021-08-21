from sqlalchemy.orm import Session
from typing import List

from schemas.users import UserCreate
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session) -> User:
    user = User(
        login=user.login,
        hashed_password=Hasher.get_password_hash(user.password),
        email=user.email,
        name=user.name,
        surname=user.surname,
        birthdate=user.birthdate,
        administrator=False,
        superuser=False,
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def retrieve_users(db: Session) -> List[User]:
    return db.query(User).all()


def retrieve_users_by_email(user_email: str, db: Session) -> List[User]:
    return db.query(User).filter(User.email == user_email).all()


def retrieve_users_by_login(user_login: str, db: Session) -> List[User]:
    return db.query(User).filter(User.login == user_login).all()


# TODO write Unit Tests + validation
def set_superuser(user_id: int, db: Session):
    db.query(User).filter(User.id == user_id).update({User.superuser: True})


# TODO write Unit Tests + validation
def set_administrator(user_id: int, db: Session):
    db.query(User).filter(User.id == user_id).update({User.administrator: True})


# TODO write Unit Tests + validation
def set_inactive(user_id: int, db: Session):
    db.query(User).filter(User.id == user_id).update({User.is_active: False})


# TODO write Unit Tests + validation
def set_active(user_id: int, db: Session):
    db.query(User).filter(User.id == user_id).update({User.is_active: True})
