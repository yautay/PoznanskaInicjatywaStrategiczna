import requests
from client.client_bgg.model.parameter import Parameter


class InterfaceBgg(object):
    def __init__(self, url: str, params: dict):
        self._url = url
        self._params = params

    def get_data(self):
        return requests.get(self._url, params=self._params)
