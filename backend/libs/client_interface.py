import logging
from typing import List
from sqlalchemy.orm import Session
from client.bgg_client import BggClient
from client.client_bgg.queries.collection import Collection as CollectionQuery
from client.client_bgg.models.collection import Collection as CollectionModel
from client.client_bgg.queries.thing import Thing as ThingQuery
from client.client_bgg.models.thing import Thing as ThingModel

logger = logging.getLogger("BggClientInterface")


class BggClientInterface(object):
    def __init__(self, db: Session, user_name: str):
        self.db = db
        self.user = user_name
        self.client = BggClient

    def synchronize(self) -> bool:
        collections = self.get_collections()
        indexes = self.get_games_indexes(collections)
        games = self.get_games(indexes)
        for g in games:
            logger.debug(g.to_string()["marketplace"])
        return True

    def get_games(self, indexes: List[int]) -> List[ThingModel]:
        return self.client(ThingQuery(indexes)).get_data()

    def get_collections(self) -> List[CollectionModel]:
        return self.client(CollectionQuery(self.user)).get_data()

    @staticmethod
    def get_games_indexes(collections: List[CollectionModel]) -> List[int]:
        indexes = []
        for item in collections:
            indexes.append(item.game_index)
        return indexes
