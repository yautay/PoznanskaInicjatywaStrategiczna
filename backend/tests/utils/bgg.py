from client.client_bgg.queries.collection import Collection
from client.client_bgg.queries.family import Family
from client.client_bgg.queries.forums import Forums
from client.client_bgg.queries.guilds import Guilds
from client.client_bgg.queries.thing import Thing
from client.client_bgg.queries.threads import Threads
from client.client_bgg.queries.user import User
from client.client_bgg.queries.forumlist import ForumList
from client.client_bgg.queries.plays import Plays
from client.client_bgg.queries.hot_items import HotItems
from client.client_bgg.queries.search import Search


class TestWrapper:
    @staticmethod
    def get_thing(**kwargs) -> Thing:
        return Thing(135840, **kwargs)

    @staticmethod
    def get_things(**kwargs) -> Thing:
        return Thing([10183, 9084], **kwargs)

    @staticmethod
    def get_user():
        return User("clown")

    @staticmethod
    def get_collection(**kwargs) -> Collection:
        return Collection("yautay", **kwargs)

    @staticmethod
    def get_guild():
        return Guilds(21)

    @staticmethod
    def get_family():
        return Family(1)

    @staticmethod
    def get_forumlist():
        return ForumList(10183)

    @staticmethod
    def get_forum():
        return Forums(23)

    @staticmethod
    def get_threads():
        return Threads(1453)

    @staticmethod
    def get_plays():
        return Plays("clown", 10183)

    @staticmethod
    def get_hot():
        return HotItems()

    @staticmethod
    def get_search():
        return Search("russia")
