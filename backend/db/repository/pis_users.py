from sqlalchemy.orm import Session
from typing import List

from schemas.users import UserCreate
from db.models.pis_user import PisUser
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session) -> PisUser:
    user = PisUser(
        login=user.login,
        hashed_password=Hasher.get_password_hash(user.password),
        email=user.email,
        bgg_user=user.bgg_user,
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


def retrieve_users(db: Session) -> List[PisUser]:
    return db.query(PisUser).all()


def retrieve_users_by_id(user_id: int, db: Session) -> PisUser:
    return db.query(PisUser).filter(PisUser.id == user_id).first()


def retrieve_users_by_email(user_email: str, db: Session) -> List[PisUser]:
    return db.query(PisUser).filter(PisUser.email == user_email).all()


def retrieve_users_by_login(user_login: str, db: Session) -> List[PisUser]:
    return db.query(PisUser).filter(PisUser.login == user_login).all()


def set_superuser(user_id: int, db: Session) -> bool:
    return db.query(PisUser).filter(PisUser.id == user_id).update({PisUser.superuser: True})


def unset_superuser(user_id: int, db: Session) -> bool:
    return db.query(PisUser).filter(PisUser.id == user_id).update({PisUser.superuser: False})


def set_administrator(user_id: int, db: Session) -> bool:
    return db.query(PisUser).filter(PisUser.id == user_id).update({PisUser.administrator: True})


def unset_administrator(user_id: int, db: Session) -> bool:
    return db.query(PisUser).filter(PisUser.id == user_id).update({PisUser.administrator: False})


def set_active(user_id: int, db: Session) -> bool:
    return db.query(PisUser).filter(PisUser.id == user_id).update({PisUser.is_active: True})


def set_inactive(user_id: int, db: Session) -> bool:
    return db.query(PisUser).filter(PisUser.id == user_id).update({PisUser.is_active: False})
