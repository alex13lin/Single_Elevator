from abc import ABCMeta, abstractmethod


class BtnElevatorSetting(object):
    def __init__(self):
        self.height = 2
        self.width = 5
        self.fontsize = 12
        self.text = None
        self.x = 0
        self.y = 0
        self.y_space = 0


class IBtnForElevator(object, metaclass=ABCMeta):

    @abstractmethod
    def create_button(self, highest_stair, btn_style: BtnElevatorSetting = None, direct=None):
        pass

    @abstractmethod
    def get_all_buttons(self):
        pass

    @abstractmethod
    def get_func_name(self):
        pass
