import datetime
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

    def parse_item(self, item):
        en_game_index: int
        en_own: int
        en_numplays: int
        en_comment: str
        en_prevowned: int
        en_fortrade: int
        en_want: int
        en_wanttoplay: int
        en_wanttobuy: int
        en_wishlist: int
        en_preordered: int
        en_lastmodified: datetime.date

        def parse_status(element):
            status = {}
            for i in element:
                if i[0] == key.OWN:
                    self.en_own = i[1]
                if i[0] == key.PREVOWNED:
                    self.en_prevowned = i[1]
                elif i[0] == key.FORTRADE:
                    self.en_fortrade = i[1]
                elif i[0] == key.WANT:
                    self.en_want = i[1]
                elif i[0] == key.WANTTOPLAY:
                    self.en_wanttoplay = i[1]
                elif i[0] == key.WANTTOBUY:
                    self.en_wanttobuy = i[1]
                elif i[0] == key.WISHLIST:
                    self.en_wishlist = i[1]
                elif i[0] == key.PREORDERED:
                    self.en_preordered = i[1]
                elif i[0] == key.LASTMODIFIED:
                    self.en_lastmodified = datetime.date.fromisoformat(i[1])

        for element in item:
            if element.tag == key.NUMPLAYS:
                en_numplays = element.text
            elif element.tag == key.COMMENT:
                en_comment = element.text
            elif element.tag == key.STATUS:
                parse_status(element.attrib.items())

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
