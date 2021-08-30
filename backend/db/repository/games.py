from typing import List

from sqlalchemy.orm import Session
from datetime import date

from client.client_bgg.model import Thing
from schemas.collections import CollectionCreate
from db.models.bgg_user_collection import BggUserCollection
from db.models.bgg_game import BggGame
from db.models.user import User
from client.bgg_client import BggClient


def synchronize_games(db: Session, indexes: List[int]) -> bool:
    games = BggClient(Thing).get_data()
    if games:
        return True