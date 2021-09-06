import random
from tests.utils.randoms import random_index, random_lower_string, random_date


def create_random_game_data() -> dict:
    return {
        "game_name": random_lower_string(15),
        "game_description": random_lower_string(500),
        "game_published": random_date(),
        "game_thumbnails": f"https://{random_lower_string(6)}.{random_lower_string(2)}.com/test.jpeg",
        "game_images": f"https://{random_lower_string(6)}.{random_lower_string(2)}.com/test.jpeg",
        "game_min_players": random.randint(1, 3),
        "game_max_players": random.randint(2, 7)
        }
