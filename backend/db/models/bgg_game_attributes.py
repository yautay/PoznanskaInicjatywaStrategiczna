from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggGameAttributes(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, ForeignKey("bgggame.game_index"))
    attribute_type_index = Column(Integer, ForeignKey("bgggameattributestypes.attribute_type_index"))
    attribute_bgg_index = Column(Integer)
    attribute_bgg_value = Column(String(250))
