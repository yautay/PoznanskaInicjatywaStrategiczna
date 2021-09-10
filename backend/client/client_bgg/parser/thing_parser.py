from client.client_bgg.parser.base_parser import Parser, ParserWrapper
from client.client_bgg.parser.item_keys import ThingItemKeys as key


class ThingParser(Parser, ParserWrapper):
    def parse_data(self, xml_data: str) -> dict:
        items = {}
        root = self.get_root(xml_data)
        for item in root:
            items[item.attrib["id"]] = self.parse_item(item)
        return items

    def parse_item(self, item) -> dict:
        thing = ThingModel()
        thing.data[key.NAME] = self.get_boardgame_name(item)
        thing.data[key.DESCRIPTION] = self.get_boardgame_description(item)
        thing.data[key.DESIGNERS] = self.get_boardgame_designers(item)
        thing.data[key.ARTISTS] = self.get_boardgame_artists(item)
        thing.data[key.PUBLISHERS] = self.get_boardgame_publishers(item)
        thing.data[key.BOARDGAME_CATEGORIES] = self.get_boardgame_categories(item)
        thing.data[key.BOARDGAME_FAMILY] = self.get_boardgame_families(item)
        thing.data[key.BOARDGAME_EXPANSIONS] = self.get_boardgame_expansions(item)
        thing.data[key.BOARDGAME_IMPLEMENTATIONS] = self.get_boardgame_implementations(item)
        thing.data[key.BOARDGAME_MECHANICS] = self.get_boardgame_mechanics(item)
        thing.data[key.MIN_PLAYERS] = self.get_boardgame_min_players(item)
        thing.data[key.MAX_PLAYERS] = self.get_boardgame_max_players(item)
        thing.data[key.PUBLISHED] = self.get_boardgame_published(item)
        thing.data[key.THUMBNAILS] = self.get_boardgame_thumbnails(item)
        thing.data[key.IMAGES] = self.get_boardgame_images(item)
        thing.data[key.BOARDGAME_VERSIONS] = self.get_boardgame_versions(item)
        thing.data[key.MARKETPLACE] = self.get_boardgame_market(item)
        return thing.data

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

    def get_boardgame_designers(self, item):
        return self.link_extractor(item, "boardgameartist")

    def get_boardgame_artists(self, item):
        return self.link_extractor(item, "boardgameartist")

    def get_boardgame_publishers(self, item):
        return self.link_extractor(item, "boardgamepublisher")

    def get_boardgame_categories(self, item):
        return self.link_extractor(item, "boardgamecategory")

    def get_boardgame_families(self, item):
        return self.link_extractor(item, "boardgamefamily")

    def get_boardgame_expansions(self, item):
        return self.link_extractor(item, "boardgameexpansion")

    def get_boardgame_implementations(self, item):
        return self.link_extractor(item, "boardgameimplementation")

    def get_boardgame_mechanics(self, item):
        return self.link_extractor(item, "boardgamemechanic")

    @staticmethod
    def get_boardgame_min_players(item):
        for element in item:
            if element.tag == "minplayers":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_max_players(item):
        for element in item:
            if element.tag == "maxplayers":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_published(item):
        for element in item:
            if element.tag == "yearpublished":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_thumbnails(item):
        for element in item:
            if element.tag == "thumbnail":
                return element.text
        return None

    @staticmethod
    def get_boardgame_images(item):
        for element in item:
            if element.tag == "image":
                return element.text
        return None

    def get_boardgame_versions(self, item):
        vesions = {}
        for element in item:
            if element.tag == "versions":
                for version in element:
                    vesions[version.attrib["id"]] = self.parse_version(version)
        return vesions

    def parse_version(self, version):
        data = {"name": self.link_extractor(version, "boardgameversion"),
                "publisher": self.link_extractor(version, "boardgamepublisher"),
                "artist": self.link_extractor(version, "boardgameartist")}
        for element in version:
            if element.tag == "name":
                data["description"] = element.attrib["value"]
            elif element.tag == "yearpublished":
                data["yearpublished"] = element.attrib["value"]
            elif element.tag == "thumbnail":
                data["thumbnail"] = element.text
            elif element.tag == "image":
                data["image"] = element.text
        return data

    def get_boardgame_market(self, item):
        market = []
        for element in item:
            if element.tag == "marketplacelistings":
                for offer in element:
                    market.append(self.parse_offer(offer))
        return market

    @staticmethod
    def parse_offer(offer):
        data = {}
        for element in offer:
            if element.tag == "condition":
                data["condition"] = element.attrib["value"]
            elif element.tag == "price":
                data["price"] = [element.attrib["value"], element.attrib["currency"]]
            elif element.tag == "link":
                data["link"] = element.attrib["href"]
            elif element.tag == "notes":
                data["notes"] = element.attrib["value"]
            elif element.tag == "listdate":
                data["listdate"] = element.attrib["value"]
        return data

    @staticmethod
    def link_extractor(item, attribute: str):
        data = []
        for element in item:
            if element.tag == "link" and element.attrib["type"] == attribute:
                data.append([element.attrib["id"], element.attrib["value"]])
        if data:
            return ParserWrapper.remove_duplicates_from_list(data)
        else:
            return None


class ThingModel(object):
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
