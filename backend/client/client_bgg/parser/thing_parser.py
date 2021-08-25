from pprint import pprint

from client.client_bgg.parser.base_parser import BaseParser


class ThingParser(BaseParser):
    def __init__(self, xml_payload: str):
        super().__init__(xml_payload)

        self.__thumbnails = self.get_root_elements_text("thumbnail")
        self.__images = self.get_root_elements_text("image")
        self.__names = self.get_root_attributes("name")
        self.__description = self.get_root_elements_text("description")
        self.__published = self.get_root_attributes("yearpublished")
        self.__minplayers = self.get_root_attributes("minplayers")
        self.__maxplayers = self.get_root_attributes("maxplayers")
        self.__links = self.get_root_attributes("link")
        self.__versions = self.__get_versions()
        self.__parse_versions()

    @property
    def boardgame_implementations(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgameimplementation")

    @property
    def thumbnails(self) -> list:
        return self.__thumbnails

    @property
    def images(self) -> list:
        return self.__images

    @property
    def name(self) -> list or None:
        for d in self.__names:
            if d["type"] == "primary":
                return d["value"]
        return None

    @property
    def description(self) -> list:
        return self.__description

    @property
    def published(self) -> list or None:
        for d in self.__published:
            if d["value"]:
                return d["value"]
        return None

    @property
    def min_players(self) -> str:
        return self.__minplayers[0]["value"]

    @property
    def max_players(self) -> str:
        return self.__maxplayers[0]["value"]

    @property
    def designers(self) ->  list[list[str]]:
        return self.__value_extractor(self.__links, "boardgamedesigner")

    @property
    def artists(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgameartist")

    @property
    def boardgame_categories(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgamecategory")

    @property
    def boardgame_mechanics(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgamemechanic")

    @property
    def boardgame_family(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgamefamily")

    @property
    def boardgame_expansions(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgameexpansion")


    @property
    def boardgame_publishers(self) -> list[list[str]]:
        return self.__value_extractor(self.__links, "boardgamepublisher")

    @property
    def versions(self):
        return self.__versions

    @staticmethod
    def __value_extractor(elements, key):
        data = []
        for element in elements:
            try:
                if element["type"] == key:
                    data.append([element["id"], element["value"]])
            except:
                pass
        return data

    def __get_versions(self) -> list:
        root = self.root
        versions = []
        for tree in root:
            for leaf in tree:
                if leaf.tag == "versions":
                    for version in leaf:
                        versions.append(version)
        return versions

    def __parse_versions(self):
        versions = {}
        for version in self.__versions:
            version_thumb = self.get_text(version, "thumbnail")
            version_image = self.get_text(version, "image")
            version_name = self.get_attributes(version, "name")[0]["value"]
            version_published = self.get_attributes(version, "yearpublished")[0]["value"]
            version_boardgameversion = []
            version_boardgamepublisher = []
            version_boardgameartist = []
            version_language = []
            for link in version:
                if link.tag == "link":
                    if link.attrib["type"] == "boardgameversion":
                        version_boardgameversion.append([link.attrib["id"], link.attrib["value"]])
                    elif link.attrib["type"] == "boardgamepublisher":
                        version_boardgamepublisher.append([link.attrib["id"], link.attrib["value"]])
                    elif link.attrib["type"] == "boardgameartist":
                        version_boardgameartist.append([link.attrib["id"], link.attrib["value"]])
                    elif link.attrib["type"] == "language":
                        version_language.append([link.attrib["id"], link.attrib["value"]])
            if version_published == "0":
                version_published = "undefined"
            versions[version_name] = {
                "thumbnail": version_thumb,
                "image": version_image,
                "published": version_published,
                "boardgameversion": version_boardgameversion,
                "boardgamepublisher": version_boardgamepublisher,
                "boardgameartist": version_boardgameartist,
                "language": version_language
            }
        self.__versions = versions
