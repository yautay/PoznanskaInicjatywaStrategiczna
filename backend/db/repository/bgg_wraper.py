from pprint import pprint

from client.bgg_client import BggClient
from client.client_bgg.model import Collection, Thing
from db.repository.collections import ORMWrapperCollection
from db.repository.games import ORMWrapperGame, ORMWrapperAttributes

from db.models.data.data_bgg_game_attributes_types import DataBggGameAttributesTypes as key


class BggWrapper(ORMWrapperCollection, ORMWrapperGame, ORMWrapperAttributes):
    def __init__(self, db, bgg_user: str):
        super().__init__(db)
        self.bgg_user = bgg_user

    def synchronize(self) -> bool:
        user_collection = BggClient(Collection(self.bgg_user)).get_data()
        if user_collection:
            user_games = BggClient(Thing(self.__extract_keys(user_collection), versions=1, marketplace=1)).get_data()
            if user_games:
                games_db_dict = self.__prepare_games_data(user_games)
                games_attributes_db_dict = self.__prepare_games_attributes_data(user_games)
                self.__add_attributes_to_db(games_attributes_db_dict)
            else:
                return False
        else:
            return False
        return True

    def __add_attributes_to_db(self, games_attributes_db_dict: dict) -> bool:
        db = ORMWrapperAttributes(self.db)
        for game_index, v in games_attributes_db_dict.items():

            for attr_type, v2 in v.items():
                if attr_type in [1, 2, 3, 5, 6, 7]:
                    #TODO TERA
                print("K", game_index, "K2", k2,"V2", v2)
                db.write_attributes_to_db(games_attributes_db_dict)
                print(v2)

    # "type_index": And(Use(str)),
    # "bgg_index": And(Use(str)),
    # "bgg_value": And(Use(str))
    # "bgg_json": Or({object: object}, None)
    # 1[['71', 'Rodger B. MacGowan'], ['11856', 'Mark Mahaffey']]


    @staticmethod
    def __prepare_games_data(bgg_data: dict) -> dict:
        model = {}
        for k, v in bgg_data.items():
            model[k] = {
                "game_name": v["name"],
                "game_description": v["description"],
                "game_published": v["published"],
                "game_thumbnails": v["thumbnails"],
                "game_images": v["images"],
                "game_min_players": v["min_players"],
                "game_max_players": v["max_players"],
            }
        return model

    @staticmethod
    def __prepare_games_attributes_data(bgg_data: dict) -> dict:
        model = {}
        for k, v in bgg_data.items():
            model[k] = {}
            for kv, vv in v.items():
                if kv == key.DESIGNERS:
                    model[k][1] = vv
                elif kv == key.ARTISTS:
                    model[k][2] = vv
                elif kv == key.PUBLISHERS:
                    model[k][3] = vv
                elif kv == key.BOARDGAME_IMPLEMENTATIONS:
                    model[k][4] = vv
                elif kv == key.BOARDGAME_CATEGORIES:
                    model[k][5] = vv
                elif kv == key.BOARDGAME_MECHANICS:
                    model[k][6] = vv
                elif kv == key.BOARDGAME_FAMILY:
                    model[k][7] = vv
                elif kv == key.BOARDGAME_VERSIONS:
                    model[k][8] = vv
                elif kv == key.BOARDGAME_EXPANSIONS:
                    model[k][9] = vv
                elif kv == key.MARKETPLACE:
                    model[k][10] = vv
        return model

    @staticmethod
    def __extract_keys(data: dict) -> list:
        keys = []
        for k in data.keys():
            keys.append(k)
        return keys