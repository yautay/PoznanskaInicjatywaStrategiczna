from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base


class BggAttributesJson(Base):
    id = Column(Integer, primary_key=True)
    attribute_bgg_json = Column(JSON)
    game_attribute = relationship("BggAttributes")
