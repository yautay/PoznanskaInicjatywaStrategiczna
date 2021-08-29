from pprint import pprint


class BaseModel(object):
    def __init__(self, url):
        self._url = url

    def parameters(self):
        params = {}
        for k, v in self.__dict__.items():
            print(k)
            print(k, v)
            if k != "_url":
                if v:
                    params[v.name] = v.value
        return params

    @property
    def url(self):
        return self._url
