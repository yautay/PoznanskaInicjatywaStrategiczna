from typing import List
from client.client_bgg.parser.base_parser import Parser, ParserWrapper
from client.client_bgg.models.collection import Collection
from client.client_bgg.parser.item_keys import CollectionItemKeys as key


class CollectionParser(Parser, ParserWrapper):
    def parse_data(self, xml_data: str) -> List[Collection]:
        usr_collection = []
        root = self.get_root(xml_data)
        for item in root:
            usr_collection.append(self.parse_item(item))
        return usr_collection

    @staticmethod
    def parse_item(item):
        en_game_index: int = item.attrib["objectid"]
        en_own = None
        en_numplays = None
        en_comment = None
        en_prevowned = None
        en_fortrade = None
        en_want = None
        en_wanttoplay = None
        en_wanttobuy = None
        en_wishlist = None
        en_preordered = None
        en_lastmodified = None

        for element in item:
            if element.tag == key.NUMPLAYS:
                en_numplays = element.text
            elif element.tag == key.COMMENT:
                en_comment = element.text
            elif element.tag == key.STATUS:
                en_own = element.attrib["own"]
                en_prevowned = element.attrib["prevowned"]
                en_fortrade = element.attrib["fortrade"]
                en_want = element.attrib["want"]
                en_wanttoplay = element.attrib["wanttoplay"]
                en_wanttobuy = element.attrib["wanttobuy"]
                en_wishlist = element.attrib["wishlist"]
                en_preordered = element.attrib["preordered"]
                en_lastmodified = element.attrib["lastmodified"]

        return Collection(game_index=en_game_index,
                          own=en_own,
                          numplays=en_numplays,
                          comment=en_comment,
                          fortrade=en_fortrade,
                          want=en_want,
                          wanttobuy=en_wanttobuy,
                          preordered=en_preordered,
                          prevowned=en_prevowned,
                          wishlist=en_wishlist,
                          wanttoplay=en_wanttoplay,
                          lastmodified=en_lastmodified)
