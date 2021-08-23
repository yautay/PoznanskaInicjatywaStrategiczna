from typing import List
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import SearchTypes
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class Search(Base):
    def __init__(self,
                 query: str,
                 _type: str = SearchTypes.ALLBOARDGAME,
                 exact: int = 1):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "search")

        assert _type in SearchTypes.__dict__.values()

        self._query = Parameter("query", query)
        self._type = Parameter("type", _type)
        self._exact = Parameter("exact", exact)
