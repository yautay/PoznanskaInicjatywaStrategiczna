class Base(object):

    def parameters(self):
        params = {}
        for k, v in self.__dict__.items():
            if k != "_url":
                params[v.name] = v.value
        return params
