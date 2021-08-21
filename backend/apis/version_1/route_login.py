from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from core.config import settings
from core.hashing import Hasher
from core.security import create_access_token
from db.models.user import User
from db.session import get_db
from db.repository.login import get_user_by_login_or_email


router = APIRouter()


def authenticate_user(username: str, password: str, db: Session) -> User or None:
    user = get_user_by_login_or_email(user_login_or_email=username, db=db)
    if not user:
        return None
    if not Hasher.verify_password(password, user.hashed_password):
        return None
    return user


@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expire = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRES_MINUTES))
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expire)
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_login_or_email(user_login_or_email=username, db=db)
    if user is None:
        raise credentials_exception
    return user
