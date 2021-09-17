from logs import logger
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from client.bgg_client import BggClient
from client.client_bgg.queries.collection import Collection as CollectionQuery
from client.client_bgg.models.collection import Collection as CollectionModel
from client.client_bgg.queries.thing import Thing as ThingQuery
from client.client_bgg.models.thing import Thing as ThingModel
from client.client_bgg.models.thing_bgg_object import BggObject
from client.client_bgg.models.thing_marketplace import ThingMarketplace
from db.repository.bgg_game import ORMWrapperBggGame
from db.repository.bgg_attribute import ORMWrapperBggAttribute
from db.repository.bgg_user_collection import ORMWrapperBggUserCollection
from db.repository.bgg_game_attribute import ORMWrapperBggGameAttribute
from db.repository.bgg_game_marketplace import ORMWrapperBggGameMarketplace
from db.repository.pis_users import PisUser
from db.models.bgg_game import BggGame
from db.models.bgg_game_attribute import BggGameAttribute
from db.models.bgg_user_collection import BggUserCollection
from db.models.bgg_attribute import BggAttribute

logger = logger.get_logger(__name__)


class BggClientInterface(object):
    def __init__(self, db: Session, user_name: str):
        self.db = db
        self.user = user_name
        self.client = BggClient

    def synchronize(self) -> bool:
        collections = self.get_collections()
        if self.add_collections_to_db(collections):
            indexes = self.get_games_indexes(collections)
            games = self.get_games(indexes)
            self.add_game_to_db(games)
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

    def add_collections_to_db(self, collections: List[CollectionModel]) -> bool:
        user_id: PisUser = self.db.query(PisUser).filter(PisUser.bgg_user == self.user).first()
        if user_id:
            success = True
            for collection in collections:
                data = {
                    "user_id": user_id.id,
                    "game_index": collection.game_index,
                    "collection_own": collection.own,
                    "collection_comment": collection.comment,
                    "collection_numplays": collection.numplays,
                    "collection_fortrade": collection.fortrade,
                    "collection_preordered": collection.preordered,
                    "collection_prevowned": collection.prevowned,
                    "collection_want": collection.want,
                    "collection_wanttobuy": collection.wanttobuy,
                    "collection_wanttoplay": collection.wanttoplay,
                    "collection_wishlist": collection.wishlist,
                    "collection_lastmodified": collection.lastmodified
                }
                part_of_success = ORMWrapperBggUserCollection(self.db).create(data)
                if not part_of_success:
                    success = False
            return success
        else:
            logger.critical(f"User {self.user} does not exists in DB, collections not added")
            return False

    def add_game_to_db(self, _game: List[ThingModel]):
        def add(_game: ThingModel):
            self.__add_game(_game)
            self.__add_marketplace(_game)
            self.__add_attributes(_game)
            return _game.game_index
        new_games = []
        for each in _game:
            new_games.append(add(each))
        logger.info(f"added {len(new_games)} games -> {new_games}")

    def __add_game(self, game_obj: ThingModel) -> bool:
        try:
            game_published = datetime.strptime(game_obj.published, "%Y")
        except:
            game_published = datetime.strptime("1945", "%Y")
        game_data = {
            "game_index": game_obj.game_index,
            "game_name": game_obj.name,
            "game_description": game_obj.description,
            "game_published": game_published,
            "game_thumbnails": game_obj.thumbnails,
            "game_images": game_obj.images,
            "game_min_players": game_obj.min_players,
            "game_max_players": game_obj.max_players
        }
        control = ORMWrapperBggGame(db=self.db).create(data=game_data)
        return control

    def __add_marketplace(self, game_obj: ThingModel or object) -> bool:
        def __add_offer(input_data: ThingMarketplace, game_index: int) -> bool:
            marketplace_data = {
                "game_index": game_index,
                "offer_date": input_data.listdate,
                "offer_price": input_data.price,
                "offer_currency": input_data.currency,
                "offer_condition": input_data.condition,
                "offer_notes": input_data.notes,
                "offer_bgg_link": input_data.link}
            return ORMWrapperBggGameMarketplace(db=self.db).create(data=marketplace_data)

        marketplace_obj = game_obj.marketplace.bgg_objects
        success = True
        for offer in marketplace_obj:
            control = __add_offer(offer, game_obj.game_index)
            if not control:
                success = False
        return success

    def __add_attributes(self, game: ThingModel) -> bool:
        def __add_attribute(input_data: BggObject) -> bool:
            prepeg = {
                "attribute_bgg_index": input_data.bgg_index,
                "attribute_bgg_value": input_data.name,
                "attribute_bgg_json": None}
            return ORMWrapperBggAttribute(db=self.db).create(data=prepeg)

        def __add_game_attribute(_game: ThingModel, att_type: int, att_index: int) -> bool:
            prepeg = {
                "game_index": _game.game_index,
                "attribute_type_index": att_type,
                "bgg_attribute": att_index}
            return ORMWrapperBggGameAttribute(db=self.db).create(data=prepeg)

        error = False
        _objects = [game.designers.bgg_objects,
                    game.artists.bgg_objects,
                    game.publishers.bgg_objects,
                    game.boardgame_implementations.bgg_objects,
                    game.boardgame_categories.bgg_objects,
                    game.boardgame_mechanics.bgg_objects,
                    game.boardgame_family.bgg_objects,
                    game.boardgame_versions,
                    game.boardgame_expansions.bgg_objects]
        for x in range(len(_objects)):
            if x != 7:  # skip boardgame_versions
                for _sub in _objects[x]:
                    att_id = __add_attribute(_sub)
                    control2 = __add_game_attribute(game, x + 1, att_id)
                    if not att_id:
                        error = True
        return error
