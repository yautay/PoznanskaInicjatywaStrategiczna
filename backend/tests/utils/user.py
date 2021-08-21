from sqlalchemy.orm import Session
from typing import List

from db.models.user import User
from schemas.users import UserCreate
from db.repository.users import create_new_user
from tests.utils.randoms import random_lower_string, random_date


def create_test_users(db: Session, count=10) -> List[User]:
    users = []
    for user in range(count):
        user = create_random_user(db=db)
        _id = user.id
        login = user.login
        emial = user.email
        hashed_password = user.hashed_password
        users.append([_id, login, emial, hashed_password])
    return users


def assert_test_users(retrieved_users: List[User] or User, users: List[User] or User):
    if users is list:
        for user in range(len(retrieved_users)):
            assert retrieved_users[user].id == users[user][0]
            assert retrieved_users[user].login == users[user][1]
            assert retrieved_users[user].email == users[user][2]
            assert retrieved_users[user].hashed_password == users[user][3]
    elif users is User:
        if retrieved_users is list:
            assert retrieved_users[0].id == users.id
            assert retrieved_users[0].login == users.login
            assert retrieved_users[0].email == users.email
            assert retrieved_users[0].hashed_password == users.hashed_password
        elif retrieved_users is User:
            assert retrieved_users.id == users.id
            assert retrieved_users.login == users.login
            assert retrieved_users.email == users.email
            assert retrieved_users.hashed_password == users.hashed_password


def create_random_user(db: Session, data: dict = None) -> User:
    if not data:
        data = create_random_user_data()
    user_schema = UserCreate(
        login=data["login"],
        email=data["email"],
        password=data["password"],
        name=data["name"],
        surname=data["surname"],
        birthdate=data["birthdate"])
    user = create_new_user(user=user_schema, db=db)
    return user


def create_random_user_data() -> dict:
    return {
        "login": random_lower_string(7),
        "email": f"{random_lower_string(6)}@{random_lower_string(6)}.com",
        "password": random_lower_string(10),
        "name": random_lower_string(10),
        "surname": random_lower_string(15),
        "birthdate": random_date()}
