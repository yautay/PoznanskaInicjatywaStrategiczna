from sqlalchemy import Column, Integer, ForeignKey, String
from db.base_class import Base


class BggGameAttributes(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, ForeignKey("bgggame.game_index"), index=True)
    attribute_type_index = Column(Integer)
    attribute_bgg_index = Column(Integer, index=True)
    attribute_bgg_value = Column(String(250))
