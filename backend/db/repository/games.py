from typing import List

from sqlalchemy.orm import Session
from datetime import date
from schemas.collections import CollectionCreate
from db.models.bgg_user_collection import Collection
from db.models.bgg_game import Game
from db.models.user import User
from client.bgg_client import BggClient

def synchronize_games(db: Session, indexes: List[int]) -> bool:
    games = BggClient().get_thing_by_id(indexes,
                                        versions=1,
                                        videos=1,
                                        stats=1,
                                        historical=1,
                                        marketplace=1,
                                        comments=1)


    # return True