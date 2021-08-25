import xml.etree.ElementTree as ET


class BaseParser(object):
    def __init__(self, xml_payload: str):
        self._xml_payload = xml_payload
        self._root = self._get_root()

    def _get_root(self) -> ET:
        return ET.fromstring(self._xml_payload)

    def get_root_elements(self, element: str) -> list[dict]:
        attributes = []
        for i in self._root.iter(element):
            attributes.append({"tag": i.tag, "attribute": i.attrib, "text": i.text})
        return attributes

    def get_root_attributes(self, element: str) -> list[dict]:
        attributes = []
        for i in self._root.iter(element):
            attributes.append(i.attrib)
        return attributes

    def get_root_elements_text(self, element: str) -> list:
        attributes = []
        for i in self._root.iter(element):
            attributes.append(i.text)
        return attributes

    @staticmethod
    def get_attributes(tree, element: str) -> list[dict]:
        attributes = []
        for i in tree:
            if i.tag == element:
                attributes.append(i.attrib)
        return attributes

    @staticmethod
    def get_text(tree, element: str) -> list:
        text = []
        for i in tree:
            if i.tag == element:
                text.append(i.text)
        return text

    @property
    def payload(self) -> str:
        return self._xml_payload

    @property
    def root(self):
        return self._root
