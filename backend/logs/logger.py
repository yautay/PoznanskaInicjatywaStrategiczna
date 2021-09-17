import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler


FORMATTER = logging.Formatter("%(asctime)s - %(name)s - line:%(lineno)d - %(levelname)s -> %(message)s")
LOG_FILE = cwd = os.path.join(os.path.abspath(os.getcwd()), "logs", "pis-common.log")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger
