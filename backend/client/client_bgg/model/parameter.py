class Parameter(object):
    def __init__(self, name, *args):
        self.__name: str = name
        if len(args) == 1:
            self.__value: object = args[0]
        else:
            self.__value: object = args

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
