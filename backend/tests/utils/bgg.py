from client.client_bgg.model.collection import Collection
from client.client_bgg.model.family import Family
from client.client_bgg.model.forums import Forums
from client.client_bgg.model.guilds import Guilds
from client.client_bgg.model.thing import Thing
from client.client_bgg.model.threads import Threads
from client.client_bgg.model.user import User
from client.client_bgg.model.forumlist import ForumList


class TestWraper:
    @staticmethod
    def get_thing():
        return Thing(10183)

    @staticmethod
    def get_user():
        return User("clown")

    @staticmethod
    def get_collection():
        return Collection("clown")

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
