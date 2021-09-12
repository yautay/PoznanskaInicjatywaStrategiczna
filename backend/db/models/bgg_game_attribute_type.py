from sqlalchemy import Column, Integer, String
from db.base_class import Base


class BggGameAttributeType(Base):
    attribute_type_index = Column(Integer, primary_key=True)
    attribute_type_name = Column(String(50), unique=True)
