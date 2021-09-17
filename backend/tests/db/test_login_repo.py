from ..conftests import *
from sqlalchemy.orm import Session
from db.repository.pis_login import get_user_by_login_or_email
from tests.utils.user import \
    create_user, \
    create_test_users, \
    assert_test_users, \
    create_random_user_data


def test_retrieve_user_by_email(db_session: Session):
    create_test_users(db=db_session)
    user = create_user(db=db_session)
    retrieved_user = get_user_by_login_or_email(user_login_or_email=user.email, db=db_session)
    assert_test_users(retrieved_user, user)


def test_retrieve_user_by_login(db_session: Session):
    create_test_users(db=db_session)
    user = create_user(db=db_session)
    retrieved_user = get_user_by_login_or_email(user_login_or_email=user.login, db=db_session)
    assert_test_users(retrieved_user, user)


def test_retrieve_user_by_login_or_email_multiple_emails(db_session: Session):
    create_test_users(db=db_session)
    user_data_1 = create_random_user_data()
    user_data_2 = create_random_user_data()
    user_data_2["email"] = user_data_1["email"]
    user = create_user(db=db_session, data=user_data_1)
    create_user(db=db_session, data=user_data_2)
    retrieved_user = get_user_by_login_or_email(user_login_or_email=user.login, db=db_session)
    assert_test_users(retrieved_user, user)
