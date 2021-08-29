from client.client_bgg.lib.interface_bgg import InterfaceBgg
from client.client_bgg.model.collection import Collection
from client.client_bgg.model.thing import Thing


class BggClient(InterfaceBgg):
    def __init__(self, bgg_object):
        super().__init__(bgg_object)
