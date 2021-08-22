from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Collection(Base):
    id = Column(Integer, primary_key=True, index=True)
    updated = Column(Date)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="collection")
