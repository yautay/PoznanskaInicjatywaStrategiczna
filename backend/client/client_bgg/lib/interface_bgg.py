import time
import requests
from client.client_bgg.model import *
from client.client_bgg.parser import *


class InterfaceBgg:
    def __init__(self, bgg_object):
        self.__bgg_object = bgg_object
        self.__client = self.Response(self.__bgg_object)
        self.__parser = self.__get_parser()

    def get_response(self) -> bool:
        self.__client.send_request()
        if self.__client.html_code == 200:
            return True
        elif self.__client.html_code == 202:
            retry = 1
            while retry < 100:
                time.sleep(5)
                retry += 1
                self.__client.send_request()
                if self.__client.html_code == 200:
                    return True
                else:
                    pass
            return False
        else:
            return False

    def __get_parser(self):
        if isinstance(self.__bgg_object, Thing):
            return ThingParser()
        elif isinstance(self.__bgg_object, Collection):
            return CollectionParser()

    def __parse_data(self):
        return self.__parser.parse_data(self.__client.data)

    def get_data(self) -> dict or None:
        if self.get_response():
            return self.__parse_data()
        return None


    class Response(object):
        def __init__(self, bgg_object):
            self.__response = None
            self.__bgg = bgg_object

        def send_request(self):
            self.__response = requests.get(self.__bgg.url, self.__bgg.parameters())

        @property
        def html_code(self):
            return self.__response.status_code

        @property
        def data(self):
            return self.__response.text
