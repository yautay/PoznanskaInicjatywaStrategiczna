from pprint import pprint
from client.client_bgg.parser.base_parser import Parser, ParserWrapper
from client.client_bgg.parser.item_keys import CollectionItemKeys as key


class CollectionParser(Parser, ParserWrapper):
    def parse_data(self, xml_data: str):
        items = []
        root = self.get_root(xml_data)
        for item in root:
            print(item.tag)
        return items

    def parse_item(self, item):
        collection = CollectionModel
        collection.data[key.NAME] = self.get_boardgame_name(item)
        collection.data[key.DESCRIPTION] = self.get_boardgame_description(item)
        return collection.data

    @staticmethod
    def get_boardgame_name(item):
        for element in item:
            if element.tag == "name" and element.attrib["type"] == "primary":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_description(item):
        for element in item:
            if element.tag == "description":
                return element.text
        return None


class CollectionModel(object):
    def __init__(self):
        self.__data = {
            key.NAME: None,
            key.DESCRIPTION: None,
            key.PUBLISHED: None,
            key.THUMBNAILS: None,
            key.IMAGES: None,
            key.MIN_PLAYERS: None,
            key.MAX_PLAYERS: None,
            key.DESIGNERS: None,
            key.ARTISTS: None,
            key.PUBLISHERS: None,
            key.BOARDGAME_IMPLEMENTATIONS: None,
            key.BOARDGAME_CATEGORIES: None,
            key.BOARDGAME_MECHANICS: None,
            key.BOARDGAME_FAMILY: None,
            key.BOARDGAME_VERSIONS: None,
            key.BOARDGAME_EXPANSIONS: None,
            key.MARKETPLACE: None
        }

    @property
    def data(self):
        return self.__data
