from ..conftests import *
from sqlalchemy.orm import Session
from db.repository.users import \
    retrieve_users, \
    retrieve_users_by_email, \
    retrieve_users_by_login, \
    set_administrator, \
    unset_administrator, \
    set_superuser, \
    unset_superuser, \
    set_active, \
    set_inactive
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


def test_set_administrator(db_session: Session):
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    assert not retrieved_user[0].administrator
    assert set_administrator(user_id=user.id, db=db_session)
    assert retrieved_user[0].administrator


def test_set_superuser(db_session: Session):
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    assert not retrieved_user[0].superuser
    assert set_superuser(user_id=user.id, db=db_session)
    assert retrieved_user[0].superuser


def test_unset_administrator(db_session: Session):
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    assert not retrieved_user[0].administrator
    assert set_administrator(user_id=user.id, db=db_session)
    assert retrieved_user[0].administrator
    assert unset_administrator(user_id=user.id, db=db_session)
    assert not retrieved_user[0].administrator


def test_unset_superuser(db_session: Session):
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    assert not retrieved_user[0].superuser
    assert set_superuser(user_id=user.id, db=db_session)
    assert retrieved_user[0].superuser
    assert unset_superuser(user_id=user.id, db=db_session)
    assert not retrieved_user[0].administrator


def test_set_inactive(db_session: Session):
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    assert retrieved_user[0].is_active
    assert set_inactive(user_id=user.id, db=db_session)
    assert not retrieved_user[0].is_active


def test_set_active(db_session: Session):
    user = create_random_user(db=db_session)
    retrieved_user = retrieve_users_by_login(user_login=user.login, db=db_session)
    set_inactive(user_id=user.id, db=db_session)
    assert not retrieved_user[0].is_active
    assert set_active(user_id=user.id, db=db_session)
    assert retrieved_user[0].is_active
