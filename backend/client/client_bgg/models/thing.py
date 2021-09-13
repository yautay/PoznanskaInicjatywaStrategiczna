from typing import List
from client.client_bgg.models.thing_sub import *


class Thing(object):
    def __init__(self,
                 game_index: int or None = None,
                 name: int or None = None,
                 description: int or None = None,
                 published: str or None = None,
                 thumbnails: int or None = None,
                 images: int or None = None,
                 min_players: int or None = None,
                 max_players: int or None = None,
                 designers: BggObjects or None = None,
                 artists: BggObjects or None = None,
                 publishers: BggObjects or None = None,
                 boardgame_categories: BggObjects or None = None,
                 boardgame_mechanics: BggObjects or None = None,
                 boardgame_family: BggObjects or None = None,
                 boardgame_versions: Versions or None = None,
                 boardgame_expansions: Expansions or None = None,
                 marketplace: Marketplace or None = None,
                 boardgame_implementations: Implementations or None = None):
        self._game_index = game_index
        self._name = name
        self._description = description
        self._published = published
        self._thumbnails = thumbnails
        self._images = images
        self._min_players = min_players
        self._max_players = max_players
        self._designers = designers
        self._artists = artists
        self._publishers = publishers
        self._boardgame_categories = boardgame_categories
        self._boardgame_mechanics = boardgame_mechanics
        self._boardgame_family = boardgame_family
        self._boardgame_versions = boardgame_versions
        self._boardgame_expansions = boardgame_expansions
        self._marketplace = marketplace
        self._boardgame_implementations = boardgame_implementations

    @property
    def game_index(self) -> int:
        return self._game_index

    @game_index.setter
    def game_index(self, value: int):
        self._game_index = value

    @property
    def name(self) -> int:
        return self._name

    @name.setter
    def name(self, value: int):
        self._name = value

    @property
    def description(self) -> int:
        return self._description

    @description.setter
    def description(self, value: int):
        self._description = value

    @property
    def published(self) -> str:
        return self._published

    @published.setter
    def published(self, value: str):
        self._published = value

    @property
    def thumbnails(self) -> int:
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, value: int):
        self._thumbnails = value

    @property
    def images(self) -> int:
        return self._images

    @images.setter
    def images(self, value: int):
        self._images = value

    @property
    def min_players(self) -> int:
        return self._min_players

    @min_players.setter
    def min_players(self, value: int):
        self._min_players = value

    @property
    def max_players(self) -> int:
        return self._max_players

    @max_players.setter
    def max_players(self, value: int):
        self._max_players = value

    @property
    def designers(self) -> BggObjects:
        return self._designers

    @designers.setter
    def designers(self, value: BggObjects):
        self._designers = value

    @property
    def artists(self) -> BggObjects:
        return self._artists

    @artists.setter
    def artists(self, value: BggObjects):
        self._artists = value

    @property
    def publishers(self) -> BggObjects:
        return self._publishers

    @publishers.setter
    def publishers(self, value: BggObjects):
        self._publishers = value

    @property
    def boardgame_categories(self) -> BggObjects:
        return self._boardgame_categories

    @boardgame_categories.setter
    def boardgame_categories(self, value: BggObjects):
        self._boardgame_categories = value

    @property
    def boardgame_mechanics(self) -> BggObjects:
        return self._boardgame_mechanics

    @boardgame_mechanics.setter
    def boardgame_mechanics(self, value: BggObjects):
        self._boardgame_mechanics = value

    @property
    def boardgame_family(self) -> BggObjects:
        return self._boardgame_family

    @boardgame_family.setter
    def boardgame_family(self, value: BggObjects):
        self._boardgame_family = value

    @property
    def boardgame_versions(self) -> Versions:
        return self._boardgame_versions

    @boardgame_versions.setter
    def boardgame_versions(self, value: Versions):
        self._boardgame_versions = value

    @property
    def boardgame_expansions(self) -> Expansions:
        return self._boardgame_expansions

    @boardgame_expansions.setter
    def boardgame_expansions(self, value: Expansions):
        self._boardgame_expansions = value

    @property
    def marketplace(self) -> Marketplace:
        return self._marketplace

    @marketplace.setter
    def marketplace(self, value: Marketplace):
        self._marketplace = value

    @property
    def boardgame_implementations(self) -> Implementations:
        return self._boardgame_implementations

    @boardgame_implementations.setter
    def boardgame_implementations(self, value: Implementations):
        self._boardgame_implementations = value

    def to_string(self) -> dict:
        return {
            "game_index": self._game_index,
            "name": self._name,
            "description": self._description,
            "published": self._published,
            "thumbnails": self._thumbnails,
            "images": self._images,
            "min_players": self._min_players,
            "max_players": self._max_players,
            "designers": self._designers.to_string(),
            "artists": self._artists.to_string(),
            "publishers": self._publishers.to_string(),
            "boardgame_categories": self._boardgame_categories.to_string(),
            "boardgame_mechanics": self._boardgame_mechanics.to_string(),
            "boardgame_family": self._boardgame_family.to_string(),
            "boardgame_versions": self._boardgame_versions,
            "boardgame_expansions": self._boardgame_expansions,
            "marketplace": self._marketplace,
            "boardgame_implementations": self._boardgame_implementations
        }
