import datetime
from typing import List
from client.client_bgg.models.thing_bgg_object import BggObject


class ThingMarketplace(object):
    def __init__(self,
                 listdate: str,
                 price: str,
                 currency: str,
                 condition: str,
                 notes: str,
                 link: str,
                 ):
        self._listdate = listdate
        self._price = price
        self._currency = currency
        self._condition = condition
        self._notes = notes
        self._link = link

    @property
    def bgg_index(self) -> int:
        return self._bgg_index

    @bgg_index.setter
    def bgg_index(self, value: int):
        self._bgg_index = value

    @property
    def listdate(self) -> str:
        return self._listdate

    @listdate.setter
    def listdate(self, value: str):
        self._listdate = value

    @property
    def price(self) -> str:
        return self._price

    @price.setter
    def price(self, value: str):
        self._price = value

    @property
    def currency(self) -> str:
        return self._currency

    @currency.setter
    def currency(self, value: str):
        self._currency = value

    @property
    def condition(self) -> str:
        return self._condition

    @condition.setter
    def condition(self, value: str):
        self._condition = value

    @property
    def notes(self) -> str:
        return self._notes

    @notes.setter
    def notes(self, value: str):
        self._notes = value

    @property
    def link(self) -> str:
        return self._link

    @link.setter
    def link(self, value: str):
        self._link = value

    def to_string(self) -> dict:
        return {
            "listdate": self._listdate,
            "price": self._price,
            "currency": self._currency,
            "condition": self._condition,
            "notes": self._notes,
            "link": self._link,
        }
