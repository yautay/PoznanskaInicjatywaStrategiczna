from typing import List


class BggObject(object):
    def __init__(self,
                 bgg_index: int,
                 name: str):
        self._bgg_index = bgg_index
        self._name = name

    @property
    def bgg_index(self) -> int:
        return self._bgg_index

    @bgg_index.setter
    def bgg_index(self, value: int):
        self._bgg_index = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def to_string(self) -> dict:
        return {
            "bgg_index": self._bgg_index,
            "name": self._name
        }


class BggObjects(object):
    def __init__(self, objects: List[BggObject]):
        self._objects = objects

    @property
    def bgg_objects(self):
        return self._bgg_objects

    @bgg_objects.setter
    def bgg_objects(self, value: List[BggObject]):
        self._objects = value

    def add_bgg_object(self, _object: BggObject):
        self._objects.append(_object)

    def to_string(self) -> List[dict]:
        objects = []
        for v in self._objects:
            objects.append(v.to_string())
        return objects