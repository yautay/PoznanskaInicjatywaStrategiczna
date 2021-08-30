from sqlalchemy import Column, Integer, Date, ForeignKey, String, JSON
from sqlalchemy.orm import relationship

from db.base_class import Base


class BggDesigner(Base):
    id = Column(Integer, primary_key=True)
    designer_index = Column(Integer, index=True)
    designer_name = Column(String(250))

