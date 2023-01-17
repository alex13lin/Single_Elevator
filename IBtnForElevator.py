from abc import ABCMeta, abstractmethod
from typing import List

from TkBtnElevator import TkBtnElevator
from model import BtnElevatorInfo, BtnElevatorStyle


class IBtnForElevator(object, metaclass=ABCMeta):

    @abstractmethod
    def create_buttons(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None) -> None:
        pass

    @abstractmethod
    def get_all_buttons(self) -> List[TkBtnElevator]:
        pass
