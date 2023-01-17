from abc import ABCMeta, abstractmethod
from model import BtnElevatorInfo, BtnElevatorStyle


class IBtnForElevator(object, metaclass=ABCMeta):

    @abstractmethod
    def create_buttons(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        pass

    @abstractmethod
    def get_all_buttons(self):
        pass
