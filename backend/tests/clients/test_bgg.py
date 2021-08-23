from ..conftests import *
from client.bgg import BggClient
from tests.utils.bgg import TestWraper as tw
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
