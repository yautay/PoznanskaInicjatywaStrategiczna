from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean, JSON, String, DateTime
from sqlalchemy.orm import relationship
from db.base_class import Base


class BggUserCollection(Base):
    id = Column(Integer, primary_key=True, index=True)
    collection_updated = Column(DateTime)
    user_id = Column(Integer, ForeignKey("pisuser.id"))
    game_index = Column(Integer)
    collection_own = Column(Integer)
    collection_comment = Column(String)
    collection_numplays = Column(Integer)
    collection_fortrade = Column(Integer)
    collection_preordered = Column(Integer)
    collection_prevowned = Column(Integer)
    collection_want = Column(Integer)
    collection_wanttobuy = Column(Integer)
    collection_wanttoplay = Column(Integer)
    collection_wishlist = Column(Integer)
    collection_lastmodified = Column(DateTime)
    user = relationship("PisUser", back_populates="collections")

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "game_index": self.game_index,
            "collection_own": self.collection_own,
            "collection_updated": self.collection_updated.isoformat(),
            "collection_numplays": self.collection_numplays,
            "collection_fortrade": self.collection_fortrade,
            "collection_preordered": self.collection_preordered,
            "collection_prevowned": self.collection_prevowned,
            "collection_want": self.collection_want,
            "collection_wanttobuy": self.collection_wanttobuy,
            "collection_wanttoplay": self.collection_wanttoplay,
            "collection_wishlist": self.collection_wishlist,
            "collection_lastmodified": self.collection_lastmodified.isoformat(),
            "collection_comment": self.collection_comment
        }
