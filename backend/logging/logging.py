import logging
import mylib


def main(func):
    def logger():
    	logging.basicConfig(filename='myapp.log', level=logging.INFO)
   	logging.info('Started')
    	func()
    	logging.info('Finished')
    return logger
