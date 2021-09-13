from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.queries.base_model import BaseModel
from client.client_bgg.data import data_client_bgg


class Forums(BaseModel):
    def __init__(self,
                 _id: int,
                 page: int = 10):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "forum")

        self._id = Parameter("id", _id)
        self._page = Parameter("page", page)
