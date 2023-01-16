import logging


class Log(object):
    def __init__(self):
        self.status = True
        pass

    def log(self, message):
        self.status = False
        logging.debug(message)
        logging.warning(message)
