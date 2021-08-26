import xml.etree.ElementTree as ET


class BaseParser(object):
    def __init__(self, xml_payload: str):
        self._xml_payload = xml_payload
        self._root = self._get_root()

    @property
    def payload(self):
        return self._xml_payload

    def _get_root(self) -> ET:
        try:
            return ET.fromstring(self._xml_payload)
        except:
            return None

    def get_root_elements(self, element: str) -> list[dict] or None:
        attributes = []
        try:
            for i in self._root.iter(element):
                attributes.append({"tag": i.tag, "attribute": i.attrib, "text": i.text})
        except:
            return None
        return attributes

    def get_root_attributes(self, element: str) -> list[dict] or None:
        attributes = []
        try:
            for i in self._root.iter(element):
                attributes.append(i.attrib)
        except:
            return None
        return attributes

    def get_root_elements_text(self, element: str) -> list or None:
        """

        @rtype: object
        """
        attributes = []
        try:
            for i in self._root.iter(element):
                attributes.append(i.text)
        except:
            return None
        return attributes

    @staticmethod
    def get_attributes(tree, element: str) -> list[dict] or None:
        attributes = []
        try:
            for i in tree:
                if i.tag == element:
                    attributes.append(i.attrib)
        except:
            return None
        return attributes

    @staticmethod
    def get_text(tree, element: str) -> list or None:
        text = []
        try:
            for i in tree:
                if i.tag == element:
                    text.append(i.text)
        except:
            return None
        return text

    @property
    def root(self):
        return self._root
