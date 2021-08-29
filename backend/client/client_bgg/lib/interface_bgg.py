import time

import requests
from client.client_bgg.model import *
from client.client_bgg.parser import *


class InterfaceBgg:
    def __init__(self, bgg_object):
        assert isinstance(bgg_object, BaseModel)
        self.__bgg_object = bgg_object
        self.__client = self.Response(self.__bgg_object)
        self.parser = self.__get_parser(self.__bgg_object)

    def get_response(self) -> bool:
        self.__client.send_request(self.__bgg_object)
        if self.__client.html_code == 200:
            return True
        elif self.__client.html_code == 202:
            retry = 1
            while retry < 100:
                time.sleep(5)
                retry += 1
                self.__client.send_request(self.__bgg_object)
                if self.__client.html_code == 200:
                    return True
                else:
                    pass
            return False
        else:
            return False

    def get_data(self) -> dict or None:
        if self.get_response():
            return self.__parse_data(self.__client.data, self.parser)

    @staticmethod
    def __get_parser(bgg_object):
        if isinstance(bgg_object, Thing):
            return ThingParser
        elif isinstance(bgg_object, Collection):
            return CollectionParser

    @staticmethod
    def __parse_data(data, parser):
        return parser.get_data(data)

    class Response(object):
        def __init__(self, bgg_object):
            self.__response = None
            bgg = bgg_object

        def send_request(self, bgg):
            self.__response = requests.get(bgg.url, bgg.parameters())

        @property
        def html_code(self):
            return self.__response.status_code

        @property
        def data(self):
            return self.__response.text
