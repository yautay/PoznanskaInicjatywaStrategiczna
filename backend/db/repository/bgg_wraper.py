from client.bgg_client import BggClient
from client.client_bgg.model import Collection, Thing
from db.repository.collections import ORMWrapperCollection
from db.repository.games import ORMWrapperGame


class BggWrapper(ORMWrapperCollection):
    def __init__(self, db, bgg_user: str):
        super().__init__(db)
        self.bgg_user = bgg_user

    def synchronize(self) -> bool:
        user_collection = BggClient(Collection(self.bgg_user)).get_data()
        if user_collection:
            user_games = BggClient(Thing(self.__extract_keys(user_collection))).get_data()
            if user_games:
                print(user_games)

        return True

    @staticmethod
    def __extract_keys(data: dict):
        keys = []
        for k in data.keys():
            keys.append(k)
        return keys