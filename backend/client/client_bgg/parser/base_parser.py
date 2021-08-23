import xml.etree.ElementTree as ET


class BaseParser(object):
    def __init__(self, xml_payload: str):
        self._xml_payload = xml_payload
        self._root = self._get_root()

    def _get_root(self) -> ET:
        return ET.fromstring(self._xml_payload)

    def get_elements(self, element: str) -> list[dict]:
        attributes = []
        for i in self._root.iter(element):
            attributes.append({"tag": i.tag, "attribute": i.attrib, "text": i.text})
        return attributes

    def get_elements_attributes(self, element: str) -> dict:
        attributes = []
        for i in self._root.iter(element):
            attributes.append(i.attrib)
        return attributes

    def get_elements_text(self, element: str) -> list:
        attributes = []
        for i in self._root.iter(element):
            attributes.append(i.text)
        return attributes

    @property
    def payload(self) -> str:
        return self._xml_payload
