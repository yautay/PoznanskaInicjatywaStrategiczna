from sqlalchemy.orm import Session
from db.repository.pis_users import retrieve_users_by_email, set_superuser
from tests.utils.randoms import random_lower_string
from tests.utils.user import create_random_user_data, create_random_user
from fastapi.testclient import TestClient


def user_authentication_headers(client: TestClient, email: str, password: str):
    data = {"username": email, "password": password}
    auth_token = client.post("/login/token", data=data).json()["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email_superuser(client: TestClient, email: str, db: Session):
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = random_lower_string(k=10)
    user = retrieve_users_by_email(user_email=email, db=db)
    if not user:
        new_user = create_random_user_data()
        new_user["email"] = email
        new_user["password"] = password
        user = create_random_user(db=db, data=new_user)
        set_superuser(user_id=user.id, db=db)
    return user_authentication_headers(client=client, email=email, password=password)


def authentication_token_from_email_common_user(client: TestClient, email: str, db: Session):
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    bgg_user = "test"
    password = random_lower_string(k=10)
    user = retrieve_users_by_email(user_email=email, db=db)
    if not user:
        new_user = create_random_user_data()
        new_user["email"] = email
        new_user["password"] = password
        new_user["bgg_user"] = bgg_user
        user = create_random_user(db=db, data=new_user)
    return user_authentication_headers(client=client, email=email, password=password)