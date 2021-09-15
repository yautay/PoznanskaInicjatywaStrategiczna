import logging
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from client.bgg_client import BggClient
from client.client_bgg.queries.collection import Collection as CollectionQuery
from client.client_bgg.models.collection import Collection as CollectionModel
from client.client_bgg.queries.thing import Thing as ThingQuery
from client.client_bgg.models.thing import Thing as ThingModel
from client.client_bgg.models.thing_bgg_object import BggObject
from db.repository.bgg_game import ORMWrapperBggGame
from db.repository.bgg_attribute import ORMWrapperBggAttribute
from db.repository.bgg_user_collection import ORMWrapperBggUserCollection
from db.repository.bgg_game_attribute import ORMWrapperBggGameAttribute
from db.models.bgg_game import BggGame
from db.models.bgg_game_attribute import BggGameAttribute
from db.models.bgg_user_collection import BggUserCollection
from db.models.bgg_attribute import BggAttribute


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
        self.add_game_to_db(self, game=games[1])
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

    @staticmethod
    def add_game_to_db(self, game: ThingModel):
        self.__add_game(game)
        self.__add_marketplace(game)
        self.__add_attributes(game)

    def __add_game(self, game_obj: ThingModel) -> bool:
        game_data = {
            "game_index": game_obj.game_index,
            "game_name": game_obj.name,
            "game_description": game_obj.description,
            "game_published": datetime.strptime(game_obj.published, "%Y"),
            "game_thumbnails": game_obj.thumbnails,
            "game_images": game_obj.images,
            "game_min_players": game_obj.min_players,
            "game_max_players": game_obj.max_players
        }
        control = ORMWrapperBggGame(db=self.db).create(data=game_data)
        logger.debug("Game {} added to db: {}".format(game_data, control))
        return control

    def __add_marketplace(self, game_obj: ThingModel) -> bool:
        marketplace_data = {
            # TODO TERATU
            "game_index": game_obj.game_index,
            "game_name": game_obj.name,
            "game_description": game_obj.description,
            "game_published": datetime.strptime(game_obj.published, "%Y"),
            "game_thumbnails": game_obj.thumbnails,
            "game_images": game_obj.images,
            "game_min_players": game_obj.min_players,
            "game_max_players": game_obj.max_players
        }
        control = ORMWrapperBggGame(db=self.db).create(data=game_data)
        logger.debug("Game {} added to db: {}".format(game_data, control))
        return control

    def __add_attributes(self, game: ThingModel) -> bool:
        error = False
        for designer in game.designers.bgg_objects:
            control = self.__add_attribute(designer)
            if not control:
                error = True
            logger.debug("Designer {} added to db: {}".format(designer.to_string(), control))
        for artist in game.artists.bgg_objects:
            control = self.__add_attribute(artist)
            if not control:
                error = True
            logger.debug("Artist {} added to db: {}".format(artist.to_string(), control))
        for publisher in game.publishers.bgg_objects:
            control = self.__add_attribute(publisher)
            logger.debug("Publisher {} added to db: {}".format(publisher.to_string(), control))
        for family in game.boardgame_family.bgg_objects:
            control = self.__add_attribute(family)
            if not control:
                error = True
            logger.debug("Family {} added to db: {}".format(family.to_string(), control))
        for mechanic in game.boardgame_mechanics.bgg_objects:
            control = self.__add_attribute(mechanic)
            if not control:
                error = True
            logger.debug("Mechanic {} added to db: {}".format(mechanic.to_string(), control))
        for category in game.boardgame_categories.bgg_objects:
            control = self.__add_attribute(category)
            if not control:
                error = True
            logger.debug("Category {} added to db: {}".format(category.to_string(), control))
        for implementation in game.boardgame_implementations.bgg_objects:
            control = self.__add_attribute(implementation)
            if not control:
                error = True
            logger.debug("Implementation {} added to db: {}".format(implementation.to_string(), control))
        for expansion in game.boardgame_expansions.bgg_objects:
            control = self.__add_attribute(expansion)
            if not control:
                error = True
            logger.debug("Expansion {} added to db: {}".format(expansion.to_string(), control))
        return error

    def __add_attribute(self, attribute: BggObject) -> bool:
        designer_data = {
            "attribute_bgg_index": attribute.bgg_index,
            "attribute_bgg_value": attribute.name,
            "attribute_bgg_json": None}
        return ORMWrapperBggAttribute(db=self.db).create(data=designer_data)
