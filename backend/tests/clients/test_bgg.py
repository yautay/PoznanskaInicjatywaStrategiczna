from pprint import pprint

from ..conftests import *
from client.bgg import BggClient
from tests.utils.bgg import TestWraper as tw
from client.client_bgg.parser.thing_parser import ThingParser
import datetime
import json


def test_bgg_xmlapi2_endpoints():
    bgg_client = BggClient()

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
    print(parser.name)
    print(parser.boardgame_implementations)
    print("CAT:")
    pprint(parser.boardgame_categories)
    print("FAMILY:")
    pprint(parser.boardgame_family)
    print("MECH:")
    pprint(parser.boardgame_mechanics)
    print("DESIG:")
    pprint(parser.designers)
    print("ARTIST:")
    pprint(parser.artists)
    print("PUBLISHERS:")
    pprint(parser.boardgame_publishers)
    pprint(parser.versions)

