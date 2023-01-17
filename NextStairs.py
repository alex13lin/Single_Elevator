from TkBtnElevator import TkBtnElevator
from typing import List

UP = 1
DOWN = -1
STOP = 0


class NextStairs(object):
    def __init__(self):
        self.the_all: List[TkBtnElevator] = []
        self.__up_bigger: List[TkBtnElevator] = []
        self.__up_smaller: List[TkBtnElevator] = []
        self.__down_bigger: List[TkBtnElevator] = []
        self.__down_smaller: List[TkBtnElevator] = []

    def extend_the_all(self, direct: int) -> None:
        self.the_all.clear()
        if direct is UP:
            self.the_all.extend(self.__up_bigger + self.__down_bigger)
            self.the_all.extend(self.__down_smaller + self.__up_smaller)
        elif direct is DOWN:
            self.the_all.extend(self.__down_smaller + self.__up_smaller)
            self.the_all.extend(self.__up_bigger + self.__down_bigger)

    def sort_all_parts(self) -> None:
        self.__sort_by_stair(self.__up_bigger)
        self.__sort_by_stair(self.__up_smaller)
        self.__sort_by_stair(self.__down_bigger, True)
        self.__sort_by_stair(self.__down_smaller, True)

    @staticmethod
    def __sort_by_stair(the_list: [], reverse: bool = False) -> None:
        the_list.sort(key=lambda b: b.get_btn_info().stair, reverse=reverse)

    def clear_all_parts(self) -> None:
        self.__up_bigger.clear()
        self.__down_bigger.clear()
        self.__down_smaller.clear()
        self.__up_smaller.clear()

    def append_up_bigger(self, btn: TkBtnElevator) -> None:
        self.__up_bigger.append(btn)

    def append_up_smaller(self, btn: TkBtnElevator) -> None:
        self.__up_smaller.append(btn)

    def append_down_bigger(self, btn: TkBtnElevator) -> None:
        self.__down_bigger.append(btn)

    def append_down_smaller(self, btn: TkBtnElevator) -> None:
        self.__down_smaller.append(btn)
