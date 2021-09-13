from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.queries.base_model import BaseModel
from client.client_bgg.data import data_client_bgg
import re

patterns = ["^[0-9]{4}-[0-9]{2}-[0-9]{2}$", "^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?$"]
compiled = [re.compile(patterns[0]), re.compile(patterns[1])]


class Threads(BaseModel):
    def __init__(self,
                 _id: int,
                 minarticleid: int = None,
                 minarticledate: str = None,
                 count: int = None):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "thread")

        if minarticledate:
            assert compiled[0].search(minarticledate) or compiled[1].search(minarticledate)

        self._id = Parameter("id", _id)
        self._minarticleid = Parameter("minarticleid", minarticleid)
        self._minarticledate = Parameter("minarticledate", minarticledate)
        self._count = Parameter("count", count)
        self._username = Parameter("username", None)
