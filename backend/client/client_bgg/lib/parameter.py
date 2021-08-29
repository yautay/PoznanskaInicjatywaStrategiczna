class Parameter(object):
    def __init__(self, name, value):
        self.__name: str = name
        if not isinstance(value, list):
            self.__value = value
        else:
            self.__value = self.__concatenate_bgg_parameter_list(value)

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @staticmethod
    def __concatenate_bgg_parameter_list(values_list) -> str:
        params_value = str(values_list[0])
        for index in range(len(values_list)):
            if index == 0:
                continue
            params_value += f", {str(values_list[index])}"
        return params_value
