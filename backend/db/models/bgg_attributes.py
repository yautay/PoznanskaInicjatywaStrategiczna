from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggAttributes(Base):
    id = Column(Integer, primary_key=True)
    attribute_bgg_index = Column(Integer, index=True, nullable=True)
    attribute_bgg_value = Column(String(250), nullable=True)
    attribute_bgg_json = Column(JSON, nullable=True)
    bgg_game_attributes = relationship("BggGameAttributes")

