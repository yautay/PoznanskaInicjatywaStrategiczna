from sqlalchemy.orm import Session

from schemas.users import UserCreate
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    return User(
        login=user.login,
        hashed_password=Hasher.get_password_hash(user.password),
        email=user.email,
        name=user.name,
        surname=user.surname,
        age=user.age,
        administrator=False,
        superuser=False,
        is_active=True
    )
    