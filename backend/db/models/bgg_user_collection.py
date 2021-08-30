from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, JSON, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggUserCollection(Base):
    id = Column(Integer, primary_key=True, index=True)
    updated = Column(Date)
    user_id = Column(Integer, ForeignKey("user.id"))
    game_index = Column(Integer, ForeignKey("bgg_game.index"))
    comment = Column(String)
    numplays = Column(Integer)
    fortrade = Column(Integer)
    preordered = Column(Integer)
    prevowned = Column(Integer)
    want = Column(Integer)
    wanttobuy = Column(Integer)
    wanttoplay = Column(Integer)
    wishlist = Column(Integer)
    lastmodified = Column(Integer)
    user = relationship("User", back_populates="collection")
    game = relationship("Game", back_populates="collection")
