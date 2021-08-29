import abc
from client.client_bgg.parser import *
import xml.etree.ElementTree as ET


class Parser(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_data') and
                callable(subclass.get_data) or
                NotImplemented)

    @abc.abstractmethod
    def parse_data(self, xml_data):
        """Return parsed data"""
        raise NotImplementedError


class ParserWrapper:
    @staticmethod
    def get_root(xml_data: str) -> ET:
        try:
            return ET.fromstring(xml_data)
        except:
            return None

    @staticmethod
    def remove_duplicates_from_list(element: list[list]):
        tmp_ids = []
        cleaned_list = []
        for x in element:
            x_id = x[0]
            x_val = x[1]
            if x_id not in tmp_ids:
                tmp_ids.append(x_id)
                cleaned_list.append([x_id, x_val])
        return cleaned_list
