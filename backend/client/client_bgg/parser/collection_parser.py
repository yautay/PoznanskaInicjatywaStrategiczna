from pprint import pprint

from client.client_bgg.parser.base_parser import Parser, ParserWrapper


class CollectionParser(Parser, ParserWrapper):
    def parse_data(self, xml_data):
        return xml_data

    # def get_data(self, xml_data: str):
    #     et_data = self.get_root(xml_data)
    #     data = {}
    #
    #     for item in collection:
    #         collection_data[item.attrib["objectid"]] = {}
    #         for element in item:
    #             if element.tag == "name":
    #                 collection_data[item.attrib["objectid"]]["name"] = element.text
    #             elif element.tag == "status":
    #                 collection_data[item.attrib["objectid"]]["status"] = element.attrib
    #             elif element.tag == "numplays":
    #                 collection_data[item.attrib["objectid"]]["numplays"] = element.text
    #     return collection_data
