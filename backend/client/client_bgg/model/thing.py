from typing import List
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import ThingType
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class Thing(Base):
    def __init__(self,
                 _id: int,
                 _type: List[str] = ThingType.BOARDGAME,
                 versions: int = 0,
                 videos: int = 0,
                 stats: int = 0,
                 historical: int = 0,
                 marketplace: int = 0,
                 comments: int = 0,
                 page: int = 1,
                 pagesize: int = 10):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "thing")

        assert (10 <= pagesize <= 100)
        assert _type in ThingType.__dict__.values()

        self._id = Parameter("id", _id)
        self._type = Parameter("type", _type)
        self._versions = Parameter("versions", versions)
        self._videos = Parameter("videos", videos)
        self._stats = Parameter("stats", stats)
        self._historical = Parameter("historical", historical)
        self._marketplace = Parameter("marketplace", marketplace)
        self._comments = Parameter("comments", comments)
        self._page = Parameter("page", page)
        self._pagesize = Parameter("pagesize", pagesize)
        self._from = Parameter("from", None)
        self._to = Parameter("to", None)
