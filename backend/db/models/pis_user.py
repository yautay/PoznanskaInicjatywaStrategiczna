import datetime

from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class PisUser(Base):
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String(60), nullable=False, index=True)
    bgg_user = Column(String(60))
    name = Column(String(50))
    surname = Column(String(60))
    birthdate = Column(Date)
    administrator = Column(Integer, default=False)
    superuser = Column(Integer, default=False)
    created = Column(Date, default=datetime.datetime.now())
    is_active = Column(Integer, default=True)
    articles = relationship("PisArticle", back_populates="user")
    collections = relationship("BggUserCollection", back_populates="user")
