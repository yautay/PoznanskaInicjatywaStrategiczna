from sqlalchemy.orm import Session
from db.repository.pis_users import \
    retrieve_users_by_email, \
    retrieve_users_by_login
from db.models.pis_user import PisUser


def get_user_by_login_or_email(user_login_or_email: str, db: Session) -> PisUser or None:
    user_by_email = retrieve_users_by_email(user_email=user_login_or_email, db=db)
    if len(user_by_email) == 1:
        return user_by_email[0]
    else:
        user_by_login = retrieve_users_by_login(user_login=user_login_or_email, db=db)
        if len(user_by_login) == 1:
            return user_by_login[0]
        else:
            return None
