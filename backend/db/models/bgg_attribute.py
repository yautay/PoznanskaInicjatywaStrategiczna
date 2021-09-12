from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from db.base_class import Base


class BggAttribute(Base):
    id = Column(Integer, primary_key=True)
    attribute_bgg_index = Column(Integer, index=True, nullable=True)
    attribute_bgg_value = Column(String(250), nullable=True)
    attribute_bgg_json = Column(JSON, nullable=True)
    bgggameattribute = relationship("BggGameAttribute", back_populates="bggattribute", uselist=False)

    def to_json(self):
        return {
            "id": self.id,
            "attribute_bgg_index": self.attribute_bgg_index,
            "attribute_bgg_value": self.attribute_bgg_value,
            "attribute_bgg_json": self.attribute_bgg_json
        }
