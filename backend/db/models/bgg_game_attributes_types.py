from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggGameAttributesTypes(Base):
    id = Column(Integer, primary_key=True)
    attribute_type_index = Column(Integer, index=True)
    attribute_type_name = Column(String(50))
    attribute = relationship("BggGameAttributes", back_populates="attribute_type_index")
