from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class Game(Base):
    id = Column(Integer, primary_key=True)
    index = Column(Integer, index=True)
    name = Column(String(200))
    published = Column(Date)
    thumbnails = Column(String(2000))
    pictures = Column(String(2000))
    data = Column(JSON)
    collection = relationship("Collection", back_populates="game")
