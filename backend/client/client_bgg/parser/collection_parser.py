from pprint import pprint
from client.client_bgg.parser.base_parser import Parser, ParserWrapper
from client.client_bgg.parser.item_keys import CollectionItemKeys as key


class CollectionParser(Parser, ParserWrapper):
    def parse_data(self, xml_data: str):
        items = {}
        root = self.get_root(xml_data)
        for item in root:
            items[item.attrib["objectid"]] = self.parse_item(item)
        return items

    def parse_item(self, item):
        entity = CollectionModel()
        for element in item:
            if element.tag == key.NUMPLAYS:
                entity.data[key.NUMPLAYS] = element.text
            elif element.tag == key.COMMENT:
                entity.data[key.COMMENT] = element.text
            elif element.tag == key.STATUS:
                entity.data[key.STATUS] = self.parse_status(element.attrib.items())
        return entity.data

    @staticmethod
    def parse_status(element):
        status = {}
        for i in element:
            if i[0] == key.PREVOWNED:
                status[key.PREVOWNED] = i[1]
            elif i[0] == key.FORTRADE:
                status[key.FORTRADE] = i[1]
            elif i[0] == key.WANT:
                status[key.WANT] = i[1]
            elif i[0] == key.WANTTOPLAY:
                status[key.WANTTOPLAY] = i[1]
            elif i[0] == key.WANTTOBUY:
                status[key.WANTTOBUY] = i[1]
            elif i[0] == key.WISHLIST:
                status[key.WISHLIST] = i[1]
            elif i[0] == key.PREORDERED:
                status[key.PREORDERED] = i[1]
            elif i[0] == key.LASTMODIFIED:
                status[key.LASTMODIFIED] = i[1]
        return status


class CollectionModel(object):
    def __init__(self):
        self.__data = {
            key.NUMPLAYS: None,
            key.COMMENT: None,
            key.STATUS: {
                key.OWN: None,
                key.PREVOWNED: None,
                key.FORTRADE: None,
                key.WANT: None,
                key.WANTTOPLAY: None,
                key.WANTTOBUY: None,
                key.WISHLIST: None,
                key.PREORDERED: None,
                key.LASTMODIFIED: None,
            }
        }

    @property
    def data(self):
        return self.__data
