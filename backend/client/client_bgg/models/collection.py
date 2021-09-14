import datetime


class Collection(object):
    def __init__(self,
                 game_index: int,
                 own: int,
                 numplays: int,
                 comment: str,
                 prevowned: int,
                 fortrade: int,
                 want: int,
                 wanttoplay: int,
                 wanttobuy: int,
                 wishlist: int,
                 preordered: int,
                 lastmodified: datetime.date):

        self._game_index = game_index
        self._own = own
        self._numplays = numplays
        self._comment = comment
        self._prevowned = prevowned
        self._fortrade = fortrade
        self._want = want
        self._wanttoplay = wanttoplay
        self._wanttobuy = wanttobuy
        self._wishlist = wishlist
        self._preordered = preordered
        self._lastmodified = lastmodified

    @property
    def game_index(self) -> int:
        return self._game_index

    @game_index.setter
    def game_index(self, value: int):
        self._game_index = value

    @property
    def own(self) -> int:
        return self._own

    @own.setter
    def own(self, value: int):
        self._own = value

    @property
    def numplays(self) -> int:
        return self._numplays

    @numplays.setter
    def numplays(self, value: int):
        self._numplays = value

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, value: str):
        self._comment = value

    @property
    def prevowned(self) -> int:
        return self._prevowned

    @prevowned.setter
    def prevowned(self, value: int):
        self._prevowned = value

    @property
    def fortrade(self) -> int:
        return self._fortrade

    @fortrade.setter
    def fortrade(self, value: int):
        self._fortrade = value

    @property
    def want(self) -> int:
        return self._want

    @want.setter
    def want(self, value: int):
        self._want = value

    @property
    def wanttoplay(self) -> int:
        return self._wanttoplay

    @wanttoplay.setter
    def wanttoplay(self, value: int):
        self._wanttoplay = value

    @property
    def wanttobuy(self) -> int:
        return self._wanttobuy

    @wanttobuy.setter
    def wanttobuy(self, value: int):
        self._wanttobuy = value

    @property
    def wishlist(self) -> int:
        return self._wishlist

    @wishlist.setter
    def wishlist(self, value: int):
        self._wishlist = value

    @property
    def preordered(self) -> int:
        return self._preordered

    @preordered.setter
    def preordered(self, value: int):
        self._preordered = value

    @property
    def lastmodified(self) -> datetime.date:
        return self._lastmodified

    @lastmodified.setter
    def lastmodified(self, value: datetime.date):
        self._lastmodified = value

    def to_string(self):
        return {
            "game_index": self._game_index,
            "own": self._own,
            "numplays": self._numplays,
            "comment": self._comment,
            "prevowned": self._prevowned,
            "fortrade": self._fortrade,
            "want": self._want,
            "wanttoplay": self._wanttoplay,
            "wanttobuy": self._wanttobuy,
            "wishlist": self._wishlist,
            "preordered": self._preordered,
            "lastmodified": self._lastmodified.isoformat()
        }
