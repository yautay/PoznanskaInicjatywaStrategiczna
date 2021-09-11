import random
from tests.utils.randoms import random_index, random_lower_string


def create_random_bgg_game() -> dict:
    return {
        "game_index": random_index(),
        "game_name": random_lower_string(12),
        "game_description": random_lower_string(143),
        "game_published": random.randint(1920, 2020),
        "game_thumbnails": f"https://{random_lower_string(5)}.com.pl/{random_lower_string(3)}.jpg",
        "game_images": f"https://{random_lower_string(5)}.com.pl/{random_lower_string(3)}.jpg",
        "game_min_players": random.randint(1, 3),
        "game_max_players": random.randint(4, 7)
    }
