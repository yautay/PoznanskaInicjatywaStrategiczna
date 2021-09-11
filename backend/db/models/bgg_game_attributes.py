from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from db.base_class import Base


class BggGameAttributes(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, ForeignKey("bgggame.game_index"))
    attribute_type_index = Column(Integer)
    attribute = Column(Integer, ForeignKey("bggattributes.id"))
