from model import Elevator
from NextStairs import NextStairs

UP = 1
DOWN = -1
STOP = 0


class SortNextStairs(object):
    def __init__(self):
        self.__next_stairs = NextStairs()
        self.__elevator = None

    def run(self, next_stairs, elevator: Elevator) -> None:
        self.__next_stairs.the_all = next_stairs
        self.__elevator: Elevator = elevator
        self.__classify_next_stairs()
        self.__next_stairs.sort_all_parts()
        self.__set_next_stairs()

    def __classify_next_stairs(self) -> None:
        self.__next_stairs.clear_all_parts()
        for btn in self.__next_stairs.the_all:
            info = btn.get_btn_info()
            if info.direct == UP:
                if info.stair > self.__elevator.place_now:
                    self.__next_stairs.append_up_bigger(btn)
                else:
                    self.__next_stairs.append_up_smaller(btn)
            if info.direct == DOWN:
                if info.stair > self.__elevator.place_now:
                    self.__next_stairs.append_down_bigger(btn)
                else:
                    self.__next_stairs.append_down_smaller(btn)

    def __set_next_stairs(self) -> None:
        if self.__elevator.direct is UP or self.__direct_exception(UP):
            self.__next_stairs.extend_the_all(UP)
        elif self.__elevator.direct is DOWN or self.__direct_exception(DOWN):
            self.__next_stairs.extend_the_all(DOWN)

    def __direct_exception(self, direct) -> bool:
        return self.__elevator.direct_former is direct and self.__elevator.direct is STOP
