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

    # def get_root_elements(self, element: str) -> list[dict] or None:
    #     attributes = []
    #     try:
    #         for i in self._root.iter(element):
    #             attributes.append({"tag": i.tag, "attribute": i.attrib, "text": i.text})
    #     except:
    #         return None
    #     return attributes
    #
    # def get_root_attributes(self, element: str) -> list[dict] or None:
    #     attributes = []
    #     try:
    #         for i in self._root.iter(element):
    # super().__init__(xml_payload)            attributes.append(i.attrib)
    #     except:
    #         return None
    #     return attributes
    #
    # def get_root_elements_text(self, element: str) -> list or None:
    #     """
    #
    #     @rtype: object
    #     """
    #     attributes = []
    #     try:
    #         for i in self._root.iter(element):
    #             attributes.append(i.text)
    #     except:
    #         return None
    #     return attributes
    #
    # @staticmethod
    # def get_attributes(tree, element: str) -> list[dict] or None:
    #     attributes = []
    #     try:
    #         for i in tree:
    #             if i.tag == element:
    #                 attributes.append(i.attrib)
    #     except:
    #         return None
    #     return attributes
    #
    # @staticmethod
    # def get_text(tree, element: str) -> list or None:
    #     text = []
    #     try:
    #         for i in tree:
    #             if i.tag == element:
    #                 text.append(i.text)
    #     except:
    #         return None
    #     return text
    #
    # @property
    # def root(self):
    #     return self._root
