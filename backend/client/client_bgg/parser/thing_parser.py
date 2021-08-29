from pprint import pprint

from client.client_bgg.parser.base_parser import Parser


class ThingParser(Parser):
    def __init__(self, xml_payload: str):
        self.thumbnails = self.get_root_elements_text("thumbnail")
        self.images = self.get_root_elements_text("image")
        self.names = self.get_root_attributes("name")
        self.description = self.get_root_elements_text("description")
        self.published = self.get_root_attributes("yearpublished")
        self.minplayers = self.get_root_attributes("minplayers")
        self.maxplayers = self.get_root_attributes("maxplayers")
        self.links = self.get_root_attributes("link")
        self.versions = self.parse_versions(self.make_versions())
        self.marketplacelistings = self.parse_marketplace(self.make_marketplace())

    @property
    def game(self):
        return {
            "name": self.get_name(),
            "thumbnails": self.get_thumbnails(),
            "images": self.get_images(),
            "description": self.get_description(),
            "published": self.get_published(),
            "min_players": self.get_min_players(),
            "max_players": self.get_max_players(),
            "boardgame_categories": self.get_boardgame_categories(),
            "boardgame_implementations": self.get_boardgame_implementations(),
            "boardgame_mechanics": self.get_boardgame_mechanics(),
            "boardgame_family": self.get_boardgame_family(),
            "boardgame_expansions": self.get_boardgame_expansions(),
            "boardgame_versions": self.versions,
            "designers": self.get_designers(),
            "artists": self.get_artists(),
            "publishers": self.get_boardgame_publishers(),
            "marketplace": self.get_marketplacelistings()
        }

    def get_boardgame_implementations(self) -> list or str:
        implementations = self.value_extractor(self.links, "boardgameimplementation")
        if len(implementations) > 0:
            return self.value_extractor(self.links, "boardgameimplementation")
        else:
            return "undefined"

    def get_thumbnails(self) -> list or str:
        if self.thumbnails:
            return self.thumbnails
        else:
            return "undefined"

    def get_images(self) -> list or str:
        if self.images:
            return self.images
        else:
            return "undefined"

    def get_name(self) -> str:
        try:
            if len(self.names) > 0:
                for d in self.names:
                    if d["type"] == "primary":
                        return d["value"]
                    else:
                        return "undefined"
            else:
                return "undefined"
        except:
            return "undefined"

    def get_description(self) -> list or str:
        if self.description:
            return self.description
        else:
            return "undefined"

    def get_published(self) -> list or str:
        if self.published:
            for d in self.published:
                if d["value"]:
                    return d["value"]
        else:
            return "undefined"

    def get_min_players(self) -> str:
        if self.minplayers:
            return self.minplayers[0]["value"]
        else:
            return "undefined"

    def get_max_players(self) -> str:
        if self.maxplayers:
            return self.maxplayers[0]["value"]
        else:
            return "undefined"

    def get_boardgame_categories(self) -> list or str:
        categories = self.value_extractor(self.links, "boardgamecategory")
        if categories:
            return categories
        else:
            return "undefined"

    def get_boardgame_mechanics(self) -> list or str:
        mechanics = self.value_extractor(self.links, "boardgamemechanic")
        if mechanics:
            return mechanics
        else:
            return "undefined"

    def get_boardgame_family(self) -> list or str:
        family = self.value_extractor(self.links, "boardgamefamily")
        if family:
            return family
        else:
            return "undefined"

    def get_boardgame_expansions(self) -> list or str:
        expansions = self.value_extractor(self.links, "boardgameexpansion")
        if expansions:
            return expansions
        else:
            return "undefined"

    def get_versions(self) -> dict or str:
        if self.versions:
            return self.versions
        else:
            return "undefined"

    def get_designers(self) -> list or str:
        designers = self.value_extractor(self.links, "boardgamedesigner")
        tmp_ids = []
        cleaned_list = []
        for designer in designers:
            designer_id = designer[0]
            designer_name = designer[1]
            if designer_id not in tmp_ids:
                tmp_ids.append(designer_id)
                cleaned_list.append([designer_id, designer_name])
        if designers:
            return cleaned_list
        else:
            return "undefined"

    def get_artists(self) -> list or str:
        artists = self.value_extractor(self.links, "boardgameartist")
        tmp_ids = []
        cleaned_list = []
        for artist in artists:
            artist_id = artist[0]
            artist_name = artist[1]
            if artist_id not in tmp_ids:
                tmp_ids.append(artist_id)
                cleaned_list.append([artist_id, artist_name])
        if artists:
            return cleaned_list
        else:
            return "undefined"

    def get_boardgame_publishers(self) -> list or str:
        publishers = self.value_extractor(self.links, "boardgamepublisher")
        if publishers:
            return publishers
        else:
            return "undefined"

    def get_marketplacelistings(self) -> list or str:
        return self.marketplacelistings

    @staticmethod
    def value_extractor(elements, key) -> list or None:
        data = []
        try:
            for element in elements:
                try:
                    if element["type"] == key:
                        data.append([element["id"], element["value"]])
                except:
                    pass
        except:
            return None
        return data

    def make_versions(self) -> list or None:
        root = self.root
        versions = []
        try:
            for tree in root:
                for leaf in tree:
                    if leaf.tag == "versions":
                        for version in leaf:
                            versions.append(version)
        except:
            return None
        return versions

    def parse_versions(self, versions_raw: list) -> dict or str:
        versions = {}
        for version in versions_raw:
            version_thumb = self.get_text(version, "thumbnail")
            version_image = self.get_text(version, "image")
            version_name = self.get_attributes(version, "name")[0]["value"]
            version_published = self.get_attributes(version, "yearpublished")[0]["value"]
            if version_published == "0":
                version_published = "undefined"
            version_boardgameversion = []
            version_boardgamepublisher = []
            version_boardgameartist = []
            version_language = []
            for link in version:
                try:
                    if link.tag == "link":
                        if link.attrib["type"] == "boardgameversion":
                            version_boardgameversion.append([link.attrib["id"], link.attrib["value"]])
                        elif link.attrib["type"] == "boardgamepublisher":
                            version_boardgamepublisher.append([link.attrib["id"], link.attrib["value"]])
                        elif link.attrib["type"] == "boardgameartist":
                            version_boardgameartist.append([link.attrib["id"], link.attrib["value"]])
                        elif link.attrib["type"] == "language":
                            version_language.append([link.attrib["id"], link.attrib["value"]])
                except:
                    pass
            if version_boardgameversion == "0":
                version_boardgameversion = "undefined"
            if version_boardgamepublisher == "0":
                version_boardgamepublisher = "undefined"
            if version_boardgameartist == "0":
                version_boardgameartist = "undefined"
            if version_language == "0":
                version_language = "undefined"
            versions[version_name] = {
                "thumbnail": version_thumb,
                "image": version_image,
                "published": version_published,
                "boardgameversion": version_boardgameversion,
                "boardgamepublisher": version_boardgamepublisher,
                "boardgameartist": version_boardgameartist,
                "language": version_language
            }
        if len(versions) > 0:
            return versions
        else:
            return "undefined"

    def make_marketplace(self) -> list or None:
        root = self.root
        marketplace = []
        try:
            for tree in root:
                for leaf in tree:
                    if leaf.tag == "marketplacelistings":
                        for listing in leaf:
                            marketplace.append(listing)
        except:
            return None
        return marketplace

    @staticmethod
    def parse_marketplace(marketplace_raw: list) -> list or str:
        listings = []
        try:
            for listing in marketplace_raw:
                item = {}
                for element in listing:
                    if element.tag == "listdate":
                        item["date"] = element.attrib["value"]
                    elif element.tag == "price":
                        item["price"] = element.attrib["value"] + " " + element.attrib["currency"]
                    elif element.tag == "condition":
                        item["condition"] = element.attrib["value"]
                    elif element.tag == "notes":
                        item["notes"] = element.attrib["value"]
                    elif element.tag == "link":
                        item["link"] = element.attrib["href"]
                listings.append(item)
            return listings
        except:
            return "undefined"
