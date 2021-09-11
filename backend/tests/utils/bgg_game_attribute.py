import random
from tests.utils.randoms import random_index


def create_random_bgg_game_attribute() -> dict:
    return {
        "game_index": random_index(),
        "attribute_type_index": random.randint(1, 9),
        "bgg_attribute": random.randint(230, 9000)}
