from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class Collection(Base):
    id = Column(Integer, primary_key=True, index=True)
    updated = Column(Date)
    user_id = Column(Integer, ForeignKey("user.id"))
    game_index = Column(Integer, ForeignKey("game.index"))
    want_to_play = Column(Integer)
    data = Column(JSON)
    user = relationship("User", back_populates="collection")
    game = relationship("Game", back_populates="collection")
