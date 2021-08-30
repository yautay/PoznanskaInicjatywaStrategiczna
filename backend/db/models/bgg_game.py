from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggGame(Base):
    id = Column(Integer, primary_key=True)
    index = Column(Integer, index=True)
    name = Column(String(250))
    description = Column(String(10000))
    published = Column(Date)
    thumbnails = Column(String(2000))
    images = Column(String(2000))
    min_players = Column(Integer)
    max_players = Column(Integer)
    collection = relationship("BggUserCollection", back_populates="game_index")
    attributes = relationship("BggGameAttributes", back_populates="game_index")
