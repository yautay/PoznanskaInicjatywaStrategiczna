from typing import List

from sqlalchemy.orm import Session
from db.repository.bgg_user_collection import ORMWrapperBggUserCollection as ColWrp
from db.repository.bgg_game import ORMWrapperBggGame as GamWrp
from db.repository.bgg_game_attribute import ORMWrapperBggGameAttribute as GamAtrWrp
from db.repository.bgg_attribute import ORMWrapperBggAttribute as AtrWrp
from client.bgg_client import BggClient
from client.client_bgg.model.collection import Collection as ColMdl
from client.client_bgg.parser.item_keys import CollectionItemKeys as keyCol
from client.client_bgg.model.thing import Thing as ThgMdl

import logging

logger = logging.getLogger("WrapperRouteBgg")


class UserCollectionItem(object):
    def __init__(self, data: dict):
        self.data = data
        self.game_index: int = 0
        self.own: int = 0
        self.numplays: int = 0
        self.comment: str = ""
        self.prevowned: int = 0
        self.fortrade: int = 0
        self.want: int = 0
        self.wanttoplay: int = 0
        self.wanttobuy: int = 0
        self.wishlist: int = 0
        self.preordered: int = 0
        self.lastmodified: str = "None"
        self.parse_data()

    def parse_data(self):
        for k, v in self.data.items():
            self.game_index = k
            self.numplays = v[keyCol.NUMPLAYS]
            self.comment = v[keyCol.COMMENT]
            status = v[keyCol.STATUS]
            for item in status:
                self.own = item[keyCol.OWN]
                self.prevowned = item[keyCol.PREVOWNED]
                self.fortrade = item[keyCol.FORTRADE]
                self.want = item[keyCol.WANT]
                self.wanttoplay = item[keyCol.WANTTOPLAY]
                self.wanttobuy = item[keyCol.WANTTOBUY]
                self.wishlist = item[keyCol.WISHLIST]
                self.preordered = item[keyCol.PREORDERED]
                self.lastmodified = item[keyCol.LASTMODIFIED]


class UserCollection(object):
    def __init__(self, data: dict):
        self.data = data
        self.collections = self.parse_data()

    def parse_data(self) -> List[UserCollectionItem]:
        instances_list = []
        for game_index, game_data in self.data.items():
            item_data = {game_index: game_data}
            instances_list.append(UserCollectionItem(item_data))
        return instances_list

    @property
    def collections(self) -> List[UserCollectionItem]:
        return self.collections

    @collections.setter
    def collections(self, value: List[UserCollectionItem]):
        self._collections = value


class WrapperRouteBgg(object):
    def __init__(self, db: Session, bgg_user: str):
        self.db = db
        self.bgg_user = bgg_user

    def synchronize(self) -> bool:
        interface = BggClient(ColMdl(username=self.bgg_user))
        try:
            data_user_collection = interface.get_data()

        except:
            logger.critical("Collection data nor rcvd!")
            logger.exception("msg")
            return False
        collection = UserCollection(data_user_collection)
        return True


