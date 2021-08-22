import datetime

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String(60), nullable=False, index=True)
    bgg_user = Column(String(60), unique=True)
    name = Column(String(50))
    surname = Column(String(60))
    birthdate = Column(Date, index=True)
    administrator = Column(Boolean, default=False)
    superuser = Column(Boolean, default=False)
    created = Column(Date, default=datetime.datetime.now(), index=True)
    is_active = Column(Boolean, default=True)
    article = relationship("Article", back_populates="user")
    user_collection = relationship("UserCollection", back_populates="user")
