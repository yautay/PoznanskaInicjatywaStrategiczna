from random import randrange
from datetime import timedelta, datetime
import random
import string


def random_lower_string(k: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k))


def random_date(to_string=False) -> datetime or str:
    d1 = datetime.strptime('1/1/1975', '%m/%d/%Y')
    d2 = datetime.strptime('1/1/2021', '%m/%d/%Y')
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    if to_string:
        return (d1 + timedelta(seconds=random_second)).strftime('%Y-%m-%d')
    else:
        return d1 + timedelta(seconds=random_second)


def random_index() -> int:
    return random.randint(10000, 99999)


def random_json() -> dict:
    return {
        random_lower_string(5): random_lower_string(12),
        random_lower_string(2): random_lower_string(10),
        random_index(): random_lower_string(21)
    }
