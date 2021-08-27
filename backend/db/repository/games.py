from sqlalchemy.orm import Session
from datetime import date
from schemas.collections import CollectionCreate
from db.models.collection import Collection
from db.models.game import Game
from db.models.user import User
from client.bgg import BggClient


def synchronize_games(db: Session, indexes: list[int]) -> bool:
    games = BggClient().get_thing_by_id(indexes,
                                        versions=1,
                                        videos=1,
                                        stats=1,
                                        historical=1,
                                        marketplace=1,
                                        comments=1)


    # return True