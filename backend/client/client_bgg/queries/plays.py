import re

from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import PlaysType, SubType
from client.client_bgg.queries.base_model import BaseModel
from client.client_bgg.data import data_client_bgg

compiled = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


class Plays(BaseModel):
    def __init__(self,
                 username: str,
                 _id: int,
                 _type: str = PlaysType.THING,
                 mindate: str = None,
                 maxdate: str = None,
                 subtype: str = SubType.BOARDGAME,
                 page: int = 1):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "plays")

        assert subtype in SubType.__dict__.values()
        assert _type in PlaysType.__dict__.values()

        self._username = Parameter("username", username)
        self._id = Parameter("id", _id)
        self._type = Parameter("type", _type)
        self._mindate = Parameter("mindate", mindate)
        self._maxdate = Parameter("maxdate", maxdate)
        self._subtype = Parameter("subtype", subtype)
        self._page = Parameter("page", page)
