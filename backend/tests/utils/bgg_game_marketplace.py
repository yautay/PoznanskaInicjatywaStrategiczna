import random
from tests.utils.randoms import random_index, random_date, random_lower_string


def create_random_bgg_game_marketplace() -> dict:
    return {
        "game_index": random_index(),
        "offer_date": random_date(),
        "offer_price": random.uniform(10, 150),
        "offer_currency": random_lower_string(3).upper(),
        "offer_condition": random_lower_string(12),
        "offer_notes": random_lower_string(231),
        "offer_bgg_link": f"https://{random_lower_string(5)}.com.pl/{random_lower_string(3)}"
    }
