from typing import List
from client.client_bgg.lib.parameter import Parameter
from client.client_bgg.data.types import CollectionType
from client.client_bgg.model.base import Base
from client.client_bgg.data import data_client_bgg


class Collection(Base):
    def __init__(self,
                 username: str,
                 version: int = 0,
                 subtype: str = CollectionType.BOARDGAME,
                 excludesubtype: str = None,
                 _id: List[int] = None,
                 stats: int = 0,
                 own: int = 1,
                 rated: int = None,
                 played: int = None,
                 comment: int = None,
                 trade: int = None,
                 want: int = None,
                 wishlist: int = None,
                 wishlistpriority: int = None,
                 preordered: int = None,
                 wanttoplay: int = None,
                 wanttobuy: int = None,
                 prevowned: int = None,
                 hasparts: int = None,
                 wantparts: int = None,
                 minrating: int = None,
                 rating: int = None,
                 minbggrating: int = None,
                 bggrating: int = None,
                 minplays: int = None,
                 maxplays: int = None,
                 showprivate: int = 0,
                 collid: int = None,
                 modifiedsince: int = None,
                 ):
        super().__init__(data_client_bgg.xmlapi2_root_path() + "collection")

        assert subtype in CollectionType.__dict__.values()

        self._username = Parameter("username", username)
        self._version = Parameter("version", version)
        self._subtype = Parameter("subtype", subtype)
        self._excludesubtype = Parameter("excludesubtype", excludesubtype)
        self._id = Parameter("_id", _id)
        self._stats = Parameter("stats", stats)
        self._own = Parameter("own", own)
        self._rated = Parameter("rated", rated)
        self._played = Parameter("played", played)
        self._comment = Parameter("comment", comment)
        self._trade = Parameter("trade", trade)
        self._want = Parameter("want", want)
        self._wishlist = Parameter("wishlist", wishlist)
        self._wishlistpriority = Parameter("wishlistpriority", wishlistpriority)
        self._preordered = Parameter("preordered", preordered)
        self._wanttoplay = Parameter("wanttoplay", wanttoplay)
        self._wanttobuy = Parameter("wanttobuy", wanttobuy)
        self._prevowned = Parameter("prevowned", prevowned)
        self._hasparts = Parameter("hasparts", hasparts)
        self._wantparts = Parameter("wantparts", wantparts)
        self._minrating = Parameter("minrating", minrating)
        self._rating = Parameter("rating", rating)
        self._minbggrating = Parameter("minbggrating", minbggrating)
        self._bggrating = Parameter("bggrating", bggrating)
        self._minplays = Parameter("minplays", minplays)
        self._maxplays = Parameter("maxplays", maxplays)
        self._showprivate = Parameter("showprivate", showprivate)
        self._collid = Parameter("collid", collid)
        self._modifiedsince = Parameter("modifiedsince", modifiedsince)




