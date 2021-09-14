import datetime
from typing import List
from client.client_bgg.models.thing_bgg_object import BggObject


class ThingVersion(object):
    def __init__(self,
                 bgg_index: int,
                 name: BggObject,
                 publisher: BggObject,
                 artist: BggObject,
                 thumbnail: str,
                 image: str,
                 description: str,
                 yearpublished: datetime.date
                 ):
        self._bgg_index = bgg_index
        self._name = name
        self._publisher = publisher
        self._artist = artist
        self._thumbnail = thumbnail
        self._image = image
        self._description = description
        self._yearpublished = yearpublished

    @property
    def bgg_index(self) -> int:
        return self._bgg_index

    @bgg_index.setter
    def bgg_index(self, value: int):
        self._bgg_index = value

    @property
    def name(self) -> BggObject:
        return self._name

    @name.setter
    def name(self, value: BggObject):
        self._name = value

    @property
    def publisher(self) -> BggObject:
        return self._publisher

    @publisher.setter
    def publisher(self, value: BggObject):
        self._publisher = value

    @property
    def artist(self) -> BggObject:
        return self._artist

    @artist.setter
    def artist(self, value: BggObject):
        self._artist = value

    @property
    def thumbnail(self) -> str:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str):
        self._thumbnail = value

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, value: str):
        self._image = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def yearpublished(self) -> datetime.date:
        return self._yearpublished

    @yearpublished.setter
    def yearpublished(self, value: datetime.date):
        self._yearpublished = value

    def to_string(self) -> dict:
        return {
            "bgg_index": self._bgg_index,
            "name": self._name.to_string(),
            "publisher": self._publisher.to_string(),
            "artist": self._artist.to_string(),
            "thumbnail": self._thumbnail,
            "image": self._image,
            "description": self._description,
            "yearpublished": self._yearpublished.strftime('%Y')
        }
