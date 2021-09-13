import re
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import HotType
from client.client_bgg.queries.base_model import BaseModel
from client.client_bgg.data import data_client_bgg

compiled = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


class HotItems(BaseModel):
    def __init__(self,
                 _type: str = HotType.BOARDGAME):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "hot")

        assert _type in HotType.__dict__.values()

        self._type = Parameter("type", _type)
