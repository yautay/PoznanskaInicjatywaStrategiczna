from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggGameAttributesTypes(Base):
    # id = Column(Integer)
    attribute_type_index = Column(Integer, primary_key=True)
    attribute_type_name = Column(String(50))
    attributes = relationship("BggGameAttributes")
