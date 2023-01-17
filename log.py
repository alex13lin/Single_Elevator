import logging
import inspect

DEBUG = False


class Log(object):
    def __init__(self):
        self.__logger = None

    def log(self):
        if not DEBUG:
            return
        self.__logger = logging.getLogger(inspect.stack()[1].frame.f_code.co_name)
        self.__logger.setLevel(logging.DEBUG)
        self.__add_handler(self.__logger.handlers)
        class_name = inspect.stack()[1].frame.f_locals["self"].__class__.__name__
        func_name = inspect.stack()[1].frame.f_code.co_name
        self.__logger.debug(f"{class_name}: {func_name}")

    def __add_handler(self, is_add):
        if is_add:
            return
        # file_handler = logging.FileHandler('test.log')
        handler = logging.StreamHandler()
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
