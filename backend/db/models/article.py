from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Article(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=False, unique=True)
    content = Column(String(2000), nullable=False)
    picture = Column(String(60), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    created_at = Column(Date, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="article")
