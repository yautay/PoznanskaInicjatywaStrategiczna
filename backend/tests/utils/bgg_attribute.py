from tests.utils.randoms import random_index, random_lower_string, random_json


def create_random_bgg_attribute_attrib() -> dict:
    return {
        "attribute_bgg_index": random_index(),
        "attribute_bgg_value": random_lower_string(50),
        "attribute_bgg_json": None
        }


def create_random_bgg_attribute_json() -> dict:
    return {
        "attribute_bgg_index": None,
        "attribute_bgg_value": None,
        "attribute_bgg_json": random_json()
        }
