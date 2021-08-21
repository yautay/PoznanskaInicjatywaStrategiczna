from ..conftests import *
from sqlalchemy.orm import Session
from db.repository.users import \
    retrieve_users, \
    retrieve_users_by_email, \
    retrieve_users_by_login
from tests.utils.user import \
    create_test_users, \
    create_random_user, \
    assert_test_users


def test_create_user(db_session: Session):
    users = create_test_users(db=db_session)
    retrieved_users = retrieve_users(db=db_session)
    assert_test_users(retrieved_users, users)


def test_retrieve_user_by_email(db_session: Session):
    create_test_users(db=db_session)
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_email(user_email=user.email, db=db_session)
    assert_test_users(retrieved_user, user)
    assert len(retrieved_user) == 1


def test_retrieve_user_by_login(db_session: Session):
    create_test_users(db=db_session)
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    assert_test_users(retrieved_user, user)
    assert len(retrieved_user) == 1
