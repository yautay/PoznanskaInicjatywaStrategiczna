import time

import requests
from client.client_bgg.model.base import Base


class InterfaceBgg:

    def get_data(self, bgg_object: Base):
        data = requests.get(bgg_object.url, params=bgg_object.parameters())
        if data.status_code == 200:
            return [data.status_code, data.text]
        elif data.status_code == 202:
            time.sleep(5)
            return self.get_data(bgg_object=bgg_object)
        else:
            raise Exception
