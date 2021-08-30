from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Article(Base):
    id = Column(Integer, primary_key=True, index=True)
    article_title = Column(String(250), nullable=False)
    article_content = Column(String(2000), nullable=False)
    article_picture = Column(String(250), nullable=False)
    article_is_active = Column(Integer, default=False, nullable=False)
    article_created_at = Column(Date, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
