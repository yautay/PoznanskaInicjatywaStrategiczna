import logging
import os.path

logs_file = "logs_common"
cwd = os.path.abspath(os.getcwd())
print(cwd)


class Logger(object):
    def __init__(self, file: str = logs_file, suffix: str = "", logger_name: str = ""):
        self.__log = os.path.join(cwd, "logs",  file + suffix + ".log")
        print(self.__log)
        self.__logger = logging.getLogger(logger_name)
        self.__logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.__log)
        fh.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.__logger.addHandler(fh)
        self.__logger.addHandler(sh)

    @property
    def logger(self):
        return self.__logger

    @logger.setter
    def logger(self, value):
        self.__logger = value
