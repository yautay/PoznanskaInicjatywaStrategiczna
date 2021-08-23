from typing import List
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import FamilyType, ThingType
from client.client_bgg.model.base_model import BaseModel
from client.client_bgg.data import data_client_bgg


class ForumList(BaseModel):
    def __init__(self,
                 _id: List[int] or int,
                 _type: str = ThingType.BOARDGAME):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "forumlist")

        assert _type in ThingType.__dict__.values() or _type in FamilyType.__dict__.values()
        if _id is not list:
            _id = [_id]

        self._id = Parameter("id", _id)
        self._type = Parameter("type", _type)
