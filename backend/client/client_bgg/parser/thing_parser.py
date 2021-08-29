from pprint import pprint

from client.client_bgg.parser.base_parser import Parser, ParserWrapper
from client.client_bgg.parser.item_keys import ThingItemKeys as key


class ThingParser(Parser, ParserWrapper):
    def parse_data(self, xml_data: str):
        items = []
        root = self.get_root(xml_data)
        for item in root:
            items.append({item.attrib["id"]: self.__parse_item(item)})

        pprint(items)

        raise Exception
        return items

    def __parse_item(self, item):
        thing = ThingModel()
        thing.data[key.NAME] = self.get_name(item)
        thing.data[key.DESCRIPTION] = self.get_description(item)
        thing.data[key.DESIGNERS] = self.get_designers(item)
        thing.data[key.ARTISTS] = self.get_artists(item)
        thing.data[key.PUBLISHERS] = self.get_publishers(item)
        thing.data[key.BOARDGAME_CATEGORIES] = self.get_boardgame_categories(item)
        thing.data[key.BOARDGAME_FAMILY] = self.get_boardgame_families(item)
        thing.data[key.BOARDGAME_EXPANSIONS] = self.get_boardgame_expansions(item)
        thing.data[key.BOARDGAME_IMPLEMENTATIONS] = self.get_boardgame_implementations(item)
        thing.data[key.BOARDGAME_MECHANICS] = self.get_boardgame_mechanics(item)
        # thing.data[key.BOARDGAME_VERSIONS] = self.get_boardgame_versions(item)
        return thing.data

    @staticmethod
    def get_name(item):
        for element in item:
            if element.tag == "name" and element.attrib["type"] == "primary":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_description(item):
        for element in item:
            if element.tag == "description":
                return element.text
        return None

    def get_designers(self, item):
        return self.link_extractor(item, "boardgameartist")

    def get_artists(self, item):
        return self.link_extractor(item, "boardgameartist")

    def get_publishers(self, item):
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

    def get_boardgame_versions(self, item):
        return self.link_extractor(item, "boardgameversion")

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




    # def get_boardgame_implementations(self) -> list or str:
    #     implementations = self.value_extractor(self.links, "boardgameimplementation")
    #     if len(implementations) > 0:
    #         return self.value_extractor(self.links, "boardgameimplementation")
    #     else:
    #         return "undefined"
    #
    # def get_thumbnails(self) -> list or str:
    #     if self.thumbnails:
    #         return self.thumbnails
    #     else:
    #         return "undefined"
    #
    # def get_images(self) -> list or str:
    #     if self.images:
    #         return self.images
    #     else:
    #         return "undefined"
    #
    #
    #
    # def get_min_players(self) -> str:
    #     if self.minplayers:
    #         return self.minplayers[0]["value"]
    #     else:
    #         return "undefined"
    #
    # def get_max_players(self) -> str:
    #     if self.maxplayers:
    #         return self.maxplayers[0]["value"]
    #     else:
    #         return "undefined"
    #
    #
    #
    # def get_marketplacelistings(self) -> list or str:
    #     return self.marketplacelistings
    #
    #
    # def make_versions(self) -> list or None:
    #     root = self.root
    #     versions = []
    #     try:
    #         for tree in root:
    #             for leaf in tree:
    #                 if leaf.tag == "versions":
    #                     for version in leaf:
    #                         versions.append(version)
    #     except:
    #         return None
    #     return versions
    #
    # def parse_versions(self, versions_raw: list) -> dict or str:
    #     versions = {}
    #     for version in versions_raw:
    #         version_thumb = self.get_text(version, "thumbnail")
    #         version_image = self.get_text(version, "image")
    #         version_name = self.get_attributes(version, "name")[0]["value"]
    #         version_published = self.get_attributes(version, "yearpublished")[0]["value"]
    #         if version_published == "0":
    #             version_published = "undefined"
    #         version_boardgameversion = []
    #         version_boardgamepublisher = []
    #         version_boardgameartist = []
    #         version_language = []
    #         for link in version:
    #             try:
    #                 if link.tag == "link":
    #                     if link.attrib["type"] == "boardgameversion":
    #                         version_boardgameversion.append([link.attrib["id"], link.attrib["value"]])
    #                     elif link.attrib["type"] == "boardgamepublisher":
    #                         version_boardgamepublisher.append([link.attrib["id"], link.attrib["value"]])
    #                     elif link.attrib["type"] == "boardgameartist":
    #                         version_boardgameartist.append([link.attrib["id"], link.attrib["value"]])
    #                     elif link.attrib["type"] == "language":
    #                         version_language.append([link.attrib["id"], link.attrib["value"]])
    #             except:
    #                 pass
    #         if version_boardgameversion == "0":
    #             version_boardgameversion = "undefined"
    #         if version_boardgamepublisher == "0":
    #             version_boardgamepublisher = "undefined"
    #         if version_boardgameartist == "0":
    #             version_boardgameartist = "undefined"
    #         if version_language == "0":
    #             version_language = "undefined"
    #         versions[version_name] = {
    #             "thumbnail": version_thumb,
    #             "image": version_image,
    #             "published": version_published,
    #             "boardgameversion": version_boardgameversion,
    #             "boardgamepublisher": version_boardgamepublisher,
    #             "boardgameartist": version_boardgameartist,
    #             "language": version_language
    #         }
    #     if len(versions) > 0:
    #         return versions
    #     else:
    #         return "undefined"
    #
    # def make_marketplace(self) -> list or None:
    #     root = self.root
    #     marketplace = []
    #     try:
    #         for tree in root:
    #             for leaf in tree:
    #                 if leaf.tag == "marketplacelistings":
    #                     for listing in leaf:
    #                         marketplace.append(listing)
    #     except:
    #         return None
    #     return marketplace
    #
    # @staticmethod
    # def parse_marketplace(marketplace_raw: list) -> list or str:
    #     listings = []
    #     try:
    #         for listing in marketplace_raw:
    #             item = {}
    #             for element in listing:
    #                 if element.tag == "listdate":
    #                     item["date"] = element.attrib["value"]
    #                 elif element.tag == "price":
    #                     item["price"] = element.attrib["value"] + " " + element.attrib["currency"]
    #                 elif element.tag == "condition":
    #                     item["condition"] = element.attrib["value"]
    #                 elif element.tag == "notes":
    #                     item["notes"] = element.attrib["value"]
    #                 elif element.tag == "link":
    #                     item["link"] = element.attrib["href"]
    #             listings.append(item)
    #         return listings
    #     except:
    #         return "undefined"
