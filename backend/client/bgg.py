from pprint import pprint

from client.client_bgg.lib.interface_bgg import InterfaceBgg
from client.client_bgg.parser.collection_parser import CollectionParser
from client.client_bgg.parser.thing_parser import ThingParser
from client.client_bgg.model.collection import Collection
from client.client_bgg.model.thing import Thing


class BggClient(InterfaceBgg):
    def __init__(self):
        pass

    def get_collection_by_user(self, user_name: str, **kwargs) -> dict or None:
        bgg_data = self.get_data(Collection(user_name, **kwargs))
        if bgg_data[0] == 200:
            return CollectionParser(bgg_data[1])
        else:
            return None

    def get_thing_by_id(self, _id: int or list[int], **kwargs) -> dict or None:
        bgg_data = self.get_data(Thing(_id, **kwargs))
        print(bgg_data)
        if bgg_data[0] == 200:
            # TODO To jest do dupy ;/
            if isinstance(_id, int):
                return ThingParser(bgg_data[1])
            else:
                return ThingParser(bgg_data[1], group_call=True)
        else:
            return None
