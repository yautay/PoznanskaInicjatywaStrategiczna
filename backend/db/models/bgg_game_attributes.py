from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from db.base_class import Base
import logging


class BggGameAttributes(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, ForeignKey("bgggame.game_index"))
    attribute_type_index = Column(Integer)
    bgg_attribute = Column(Integer, ForeignKey("bggattributes.id"))

    def to_json(self):
        return {
            "id": self.id,
            "game_index": self.game_index,
            "attribute_type_index": self.attribute_type_index,
            "bgg_attribute": self.bgg_attribute
        }
