import requests
from client.client_bgg.model.parameter import Parameter
from client.client_bgg.model.base import Base


class InterfaceBgg:

    @staticmethod
    def get_data(bgg_object: Base):
        try:
            data = requests.get(bgg_object.url, params=bgg_object.parameters())
            if data.status_code == 200:
                return data.text
            else:
                return None
        except:
            return None
