from client.client_bgg.model.parameter import Parameter
from client.client_bgg.model.thingtype import ThingType
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class Thing(Base):
    def __init__(self, _id: int, _type: tuple[str] = (ThingType.BOARDGAME,), versions: bool = 0,
                 videos: bool = 0, stats: bool = 0, historical: bool = 0, marketplace: bool = 0,
                 comments: bool = 0, page: int = 1, pagesize: int = 10):

        if not (10 <= pagesize <= 100):
            raise AttributeError

        self._url = data_client_bgg.xmlapi2_root_path() + "thing"
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

    @property
    def url(self):
        return self._url

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def versions(self):
        return self._versions

    @property
    def videos(self):
        return self._videos

    @property
    def stats(self):
        return self._stats

    @property
    def historical(self):
        return self._historical

    @property
    def marketplace(self):
        return self._marketplace

    @property
    def comments(self):
        return self._comments

    @property
    def page(self):
        return self._page

    @property
    def pagesize(self):
        return self._pagesize
