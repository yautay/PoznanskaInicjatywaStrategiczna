from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import SortType
from client.client_bgg.model.base_model import BaseModel
from client.client_bgg.data import data_client_bgg


class Guilds(BaseModel):
    def __init__(self,
                 _id: int,
                 members: int = 0,
                 sort: str = SortType.USERNAME,
                 page: int = 10):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "guild")

        self._id = Parameter("id", _id)
        self._members = Parameter("members", members)
        self._sort = Parameter("sort", sort)
        self._page = Parameter("page", page)
