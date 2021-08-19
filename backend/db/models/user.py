from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String(60), nullable=False, unique=True, index=True)
    name = Column(String(50))
    surname = Column(String(60))
    age = Column(Integer)
    administrator = Column(Boolean, default=False)
    superuser = Column(Boolean, default=False)
    created = Column(Date, index=True)
    is_active = Column(Boolean, default=True)
    article = relationship("Article", back_populates="user")
