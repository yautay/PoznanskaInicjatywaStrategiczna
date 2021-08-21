from random import randrange
from datetime import timedelta, datetime
import random
import string


def random_lower_string(k: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k))


def random_date():
    d1 = datetime.strptime('1/1/1975', '%m/%d/%Y')
    d2 = datetime.strptime('1/1/2021', '%m/%d/%Y')
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return (d1 + timedelta(seconds=random_second)).strftime('%Y-%m-%d')
