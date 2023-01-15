from abc import ABCMeta, abstractmethod


class BtnStyle(object):
    def __init__(self):
        self.height = 2
        self.weight = 5
        self.fontsize = 12
        self.text = None


class IBtnForElevator(object, metaclass=ABCMeta):

    @abstractmethod
    def create_button(self, highest_stair, btn_style: BtnStyle = None, direct=None):
        pass

    @abstractmethod
    def get_all_buttons(self):
        pass

    @abstractmethod
    def get_func_name(self):
        pass
