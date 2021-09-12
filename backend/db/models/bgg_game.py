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
    bgggameattributes = relationship("BggGameAttribute", back_populates="bgggame", uselist=False)

    def to_json(self):
        return {
            "id": self.id,
            "game_index": self.game_index,
            "game_name": self.game_name,
            "game_description": self.game_description,
            "game_published": self.game_published,
            "game_thumbnails": self.game_thumbnails,
            "game_images": self.game_images,
            "game_min_players": self.game_min_players,
            "game_max_players": self.game_max_players,
        }