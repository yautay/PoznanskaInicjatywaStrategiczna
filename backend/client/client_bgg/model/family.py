from typing import List
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import FamilyType
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class Family(Base):
    def __init__(self,
                 _id: List[int] or int,
                 _type: str = FamilyType.BOARDGAMEFAMILY):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "family")

        assert _type in FamilyType.__dict__.values()
        if _id is not list:
            _id = [_id]

        self._id = Parameter("id", _id)
        self._type = Parameter("type", _type)
