from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, JSON, String
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggUserCollection(Base):
    id = Column(Integer, primary_key=True, index=True)
    collection_updated = Column(Date)
    user_id = Column(Integer, ForeignKey("user.id"))
    game_index = Column(Integer, ForeignKey("bgggame.game_index"))
    collection_comment = Column(String)
    collection_numplays = Column(Integer)
    collection_fortrade = Column(Integer)
    collection_preordered = Column(Integer)
    collection_prevowned = Column(Integer)
    collection_want = Column(Integer)
    collection_wanttobuy = Column(Integer)
    collection_wanttoplay = Column(Integer)
    collection_wishlist = Column(Integer)
    collection_lastmodified = Column(Integer)
