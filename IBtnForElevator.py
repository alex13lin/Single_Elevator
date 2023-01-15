from abc import ABCMeta, abstractmethod


class IBtnForElevator(object, metaclass=ABCMeta):

    @abstractmethod
    def create_button(self, highest_stair, text=None, direct=None):
        pass

    @abstractmethod
    def get_all_buttons(self):
        pass

    @abstractmethod
    def get_func_name(self):
        pass
