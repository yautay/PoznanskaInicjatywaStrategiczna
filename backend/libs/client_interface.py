from sqlalchemy.orm import Session
from client.bgg_client import BggClient
from client.client_bgg.queries.collection import Collection as CollectionQuerry
from client.client_bgg.models.collection import Collection as CollectionModel


class BggClientInterface(object):
    def __init__(self, db: Session, user_name: str):
        self.db = db
        self.user = user_name
        self.client = BggClient

    def synchronize(self) -> bool:
        print("SSSSSSSSSSSSSSSSSSSSSSSSs")
        collections = self.get_collections()
        print(collections)
        return True

    def get_collections(self) -> CollectionModel:
        return self.client(CollectionQuerry(self.user)).get_data()