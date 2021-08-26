from pprint import pprint

from ..conftests import *
from client.client_bgg.parser.collection_parser import CollectionParser
from client.bgg import BggClient
from tests.utils.bgg import TestWrapper as tw
from client.client_bgg.parser.thing_parser import ThingParser
import datetime
import json


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
        assert BggClient().get_data(instance)[0] == 200


def test_thing_parser():
    parser = ThingParser(BggClient().get_data(tw.get_thing(versions=1,
                                                           videos=1,
                                                           stats=1,
                                                           historical=1,
                                                           marketplace=1,
                                                           comments=1))[1])
    pprint(parser.game)
    assert len(parser.game) == 17


def test_collection_parser():
    parser = CollectionParser(BggClient().get_data(tw.get_collection())[1])
    for key in parser.items.keys():
        print(parser.items[key])
    assert len(parser.items) > 180
