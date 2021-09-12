from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class BggGameAttribute(Base):
    id = Column(Integer, primary_key=True)
    game_index = Column(Integer, ForeignKey("bgggame.game_index"))
    bgg_attribute = Column(Integer, ForeignKey("bggattribute.id"))
    attribute_type_index = Column(Integer)
    bgggame = relationship("BggGame", back_populates="bgggameattributes")
    bggattribute = relationship("BggAttribute", back_populates="bgggameattribute", uselist=False)

    def to_json(self):
        return {
            "id": self.id,
            "game_index": self.game_index,
            "attribute_type_index": self.attribute_type_index,
            "bgg_attribute": self.bgg_attribute
        }
