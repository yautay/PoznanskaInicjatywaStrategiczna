from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.lib.types import DomainType
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class User(Base):
    def __init__(self, name: str, buddies: int = 0, guilds: int = 0, hot: int = 0,
                 top: int = 0, domain: str = DomainType.BOARDGAME, page: int = 1):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "user")

        self._name = Parameter("name", name)
        self._buddies = Parameter("buddies", buddies)
        self._guilds = Parameter("guilds", guilds)
        self._hot = Parameter("hot", hot)
        self._top = Parameter("top", top)
        self._domain = Parameter("domain", domain)
        self._page = Parameter("page", page)
