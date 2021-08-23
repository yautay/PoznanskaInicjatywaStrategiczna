from typing import List
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import FamilyType, ThingType
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class ForumList(Base):
    def __init__(self,
                 _id: List[int],
                 _type: str = ThingType.BOARDGAME):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "forumlist")

        assert _type in ThingType.__dict__.values() or _type in FamilyType.__dict__.values()

        self._id = Parameter("id", _id)
        self._type = Parameter("type", _type)
