from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggGame(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, index=True)
    game_name = Column(String(250))
    game_description = Column(String(10000))
    game_published = Column(Date)
    game_thumbnails = Column(String(2000))
    game_images = Column(String(2000))
    game_min_players = Column(Integer)
    game_max_players = Column(Integer)
    game_collection = relationship("BggUserCollection")
    game_attribute = relationship("BggGameAttributes")
