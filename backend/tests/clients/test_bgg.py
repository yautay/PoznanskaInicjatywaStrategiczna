from pprint import pprint

from ..conftests import *
from client.bgg_client import BggClient
from tests.utils.bgg import TestWrapper as tw


def test_bgg_xmlapi2_endpoints():
    for instance in [tw.get_user(),
                     tw.get_thing(),
                     tw.get_collection(),
                     tw.get_forumlist(),
                     tw.get_family(),
                     tw.get_guild(),
                     tw.get_forum(),
                     tw.get_threads(),
                     tw.get_plays(),
                     tw.get_hot(),
                     tw.get_search()]:
        assert BggClient(instance).get_response()


def test_thing_parser():
    thing = tw.get_thing(versions=1,
                         videos=1,
                         stats=1,
                         historical=1,
                         marketplace=1,
                         comments=1)
    client = BggClient(thing)
    for element in client.get_data():
        assert element


def test_things_parser():
    things = tw.get_things(versions=1,
                           videos=1,
                           stats=1,
                           historical=1,
                           marketplace=1,
                           comments=1)
    client = BggClient(things)
    for element in client.get_data():
        assert element


def test_collection_parser():
    collection = tw.get_collection()
    client = BggClient(collection)
    for element in client.get_data():
        assert element
