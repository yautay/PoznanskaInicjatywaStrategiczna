import random
from tests.utils.randoms import random_index, random_lower_string, random_date


def create_random_bgg_user_collection() -> dict:
    return {
        "user_id": random_index(),
        "game_index": random_index(),
        "collection_own": random.randint(0, 1),
        "collection_comment": random_lower_string(12),
        "collection_numplays": random.randint(4, 12),
        "collection_fortrade": random.randint(0, 1),
        "collection_preordered": random.randint(0, 1),
        "collection_prevowned": random.randint(0, 1),
        "collection_want": random.randint(0, 1),
        "collection_wanttobuy": random.randint(0, 1),
        "collection_wanttoplay": random.randint(0, 1),
        "collection_wishlist": random.randint(0, 1),
        "collection_lastmodified": random_date()
    }
