from typing import List
from client.client_bgg.parser.base_parser import Parser, ParserWrapper
from client.client_bgg.models.thing import Thing
from client.client_bgg.models.thing_version import ThingVersion
from client.client_bgg.models.thing_marketplace import ThingMarketplace
from client.client_bgg.models.thing_bgg_object import BggObject, BggObjects


class ThingParser(Parser, ParserWrapper):
    def parse_data(self, xml_data: str) -> List[Thing]:
        games = []
        root = self.get_root(xml_data)
        for item in root:
            games.append(self.parse_item(item))
        return games

    def parse_item(self, item) -> Thing:
        game_index = self.get_boardgame_index(item)
        name = self.get_boardgame_name(item)
        description = self.get_boardgame_description(item)
        published = self.get_boardgame_published(item)
        thumbnails = self.get_boardgame_thumbnails(item)
        images = self.get_boardgame_images(item)
        min_players = self.get_boardgame_min_players(item)
        max_players = self.get_boardgame_max_players(item)
        designers = self.get_boardgame_designers(item)
        artists = self.get_boardgame_artists(item)
        publishers = self.get_boardgame_publishers(item)
        boardgame_categories = self.get_boardgame_categories(item)
        boardgame_mechanics = self.get_boardgame_mechanics(item)
        boardgame_family = self.get_boardgame_families(item)
        boardgame_versions = self.get_boardgame_versions(item)
        boardgame_expansions = self.get_boardgame_expansions(item)
        marketplace = self.get_boardgame_market(item)
        boardgame_implementations = self.get_boardgame_implementations(item)

        return Thing(game_index=game_index,
                     name=name,
                     description=description,
                     published=published,
                     thumbnails=thumbnails,
                     images=images,
                     min_players=min_players,
                     max_players=max_players,
                     designers=designers,
                     artists=artists,
                     publishers=publishers,
                     boardgame_categories=boardgame_categories,
                     boardgame_mechanics=boardgame_mechanics,
                     boardgame_family=boardgame_family,
                     boardgame_versions=boardgame_versions,
                     boardgame_expansions=boardgame_expansions,
                     marketplace=marketplace,
                     boardgame_implementations=boardgame_implementations)

    @staticmethod
    def get_boardgame_index(item) -> int:
        return item.attrib["id"]

    @staticmethod
    def get_boardgame_name(item) -> str or None:
        for element in item:
            if element.tag == "name" and element.attrib["type"] == "primary":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_description(item) -> str or None:
        for element in item:
            if element.tag == "description":
                return element.text
        return None

    def get_boardgame_designers(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgamedesigner")

    def get_boardgame_artists(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgameartist")

    def get_boardgame_publishers(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgamepublisher")

    def get_boardgame_categories(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgamecategory")

    def get_boardgame_families(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgamefamily")

    def get_boardgame_expansions(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgameexpansion")

    def get_boardgame_implementations(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgameimplementation")

    def get_boardgame_mechanics(self, item) -> BggObjects:
        return self.link_extractor(item, "boardgamemechanic")

    @staticmethod
    def get_boardgame_min_players(item) -> str or None:
        for element in item:
            if element.tag == "minplayers":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_max_players(item) -> str or None:
        for element in item:
            if element.tag == "maxplayers":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_published(item) -> str or None:
        for element in item:
            if element.tag == "yearpublished":
                return element.attrib["value"]
        return None

    @staticmethod
    def get_boardgame_thumbnails(item) -> str or None:
        for element in item:
            if element.tag == "thumbnail":
                return element.text
        return None

    @staticmethod
    def get_boardgame_images(item) -> str or None:
        for element in item:
            if element.tag == "image":
                return element.text
        return None

    def get_boardgame_versions(self, item) -> BggObjects:
        objects = BggObjects()
        for element in item:
            if element.tag == "versions":
                for version in element:
                    index = version.attrib["id"]
                    name = self.link_extractor(version, "boardgameversion")
                    publisher = self.link_extractor(version, "boardgamepublisher")
                    artist = self.link_extractor(version, "boardgameartist")
                    description = None
                    yearpublished = None
                    thumbnail = None
                    image = None
                    for details in version:
                        if element.tag == "name":
                            description = details.attrib["value"]
                        elif element.tag == "yearpublished":
                            yearpublished = details.attrib["value"]
                        elif element.tag == "thumbnail":
                            thumbnail = details.text
                        elif element.tag == "image":
                            image = details.text
                    objects.add_bgg_object(ThingVersion(bgg_index=index,
                                                        name=name,
                                                        publisher=publisher,
                                                        artist=artist,
                                                        thumbnail=thumbnail,
                                                        image=image,
                                                        description=description,
                                                        yearpublished=yearpublished))
        return objects

    def get_boardgame_market(self, item) -> BggObjects:
        def parse_offer(single_offer) -> ThingMarketplace:
            condition = None
            price = None
            currency = None
            link = None
            notes = None
            listdate = None
            for element in offer:
                if element.tag == "condition":
                    condition = element.attrib["value"]
                elif element.tag == "price":
                    price = element.attrib["value"]
                    currency = element.attrib["currency"]
                elif element.tag == "link":
                    link = element.attrib["href"]
                elif element.tag == "notes":
                    notes = element.attrib["value"]
                elif element.tag == "listdate":
                    listdate = element.attrib["value"]
            return ThingMarketplace(listdate=listdate,
                                    price=price,
                                    currency=currency,
                                    condition=condition,
                                    notes=notes,
                                    link=link)
        objects = BggObjects()
        for element in item:
            if element.tag == "marketplacelistings":
                for offer in element:
                    objects.add_bgg_object(parse_offer(offer))
        return objects

    @staticmethod
    def link_extractor(item, attribute: str) -> BggObjects:
        objects = BggObjects()
        for element in item:
            if element.tag == "link" and element.attrib["type"] == attribute:
                objects.add_bgg_object(BggObject(bgg_index=element.attrib["id"], name=element.attrib["value"]))
        return objects
