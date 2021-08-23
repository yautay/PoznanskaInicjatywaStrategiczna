from client.client_bgg.parser.base_parser import BaseParser


class ThingParser(BaseParser):
    def __init__(self, xml_payload: str):
        super().__init__(xml_payload)

        self.__thumbnails = self.get_elements_text("thumbnail")
        self.__images = self.get_elements_text("image")
        self.__names = self.get_elements_attributes("name")
        self.__description = self.get_elements_text("description")
        self.__published = self.get_elements_attributes("yearpublished")


    @property
    def thumbnails(self) -> list:
        return self.__thumbnails

    @property
    def images(self) -> list:
        return self.__images

    @property
    def names(self) -> dict:
        return self.__names

    @property
    def name(self) -> list or None:
        for d in self.__names:
            if d["type"] == "primary":
                return d["value"]
        return None

    @property
    def description(self) -> list:
        return self.__description

    @property
    def published(self) -> list or None:
        for d in self.__published:
            if d["value"]:
                return d["value"]
        return None


