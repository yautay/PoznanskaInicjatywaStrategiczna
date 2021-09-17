from sqlalchemy import Column, Integer, Date, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import relationship
from db.base_class import Base


class BggGameMarketplace(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, ForeignKey("bgggame.game_index"))
    offer_date = Column(DateTime)
    offer_price = Column(Float)
    offer_currency = Column(String(3))
    offer_condition = Column(String(20))
    offer_notes = Column(String(2000))
    offer_bgg_link = Column(String(300))
    bgggame = relationship("BggGame", back_populates="bgggamemarketplace")

    def to_json(self):
        return {
            "id": self.id,
            "game_index": self.game_index,
            "offer_date": self.offer_date,
            "offer_price": self.offer_price,
            "offer_currency": self.offer_currency,
            "offer_condition": self.offer_condition,
            "offer_notes": self.offer_notes,
            "offer_bgg_link": self.offer_bgg_link
        }
