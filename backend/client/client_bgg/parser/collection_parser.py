from pprint import pprint

from client.client_bgg.parser.base_parser import BaseParser


class CollectionParser(BaseParser):
    def __init__(self, xml_payload: str):
        super().__init__(xml_payload)

        self.items = self.get_items()

    def get_items(self):
        collection = self.root
        collection_data = {}
        for item in collection:
            collection_data[item.attrib["objectid"]] = {}
            for element in item:
                if element.tag == "name":
                    collection_data[item.attrib["objectid"]]["name"] = element.text
                elif element.tag == "status":
                    collection_data[item.attrib["objectid"]]["status"] = element.attrib
                elif element.tag == "numplays":
                    collection_data[item.attrib["objectid"]]["numplays"] = element.text
        return collection_data
