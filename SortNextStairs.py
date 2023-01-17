from model import Elevator

UP = 1
DOWN = -1
STOP = 0


class SortNextStairs(object):
    def __init__(self):
        self.__next_stairs = None
        self.__elevator = None
        self.__up_bigger, self.__up_smaller, self.__down_bigger, self.__down_smaller = [], [], [], []

    def run(self, next_stairs, elevator: Elevator) -> None:
        self.__next_stairs = next_stairs
        self.__elevator = elevator
        self.__classify_next_stairs()
        self.__sort_part_of_next_stairs()
        if self.__elevator.direct is UP or self.__direct_exception(UP):
            self.__next_stairs.clear()
            self.__next_stairs.extend(self.__up_bigger + self.__down_bigger + self.__down_smaller + self.__up_smaller)
        elif self.__elevator.direct is DOWN or self.__direct_exception(DOWN):
            self.__next_stairs.clear()
            self.__next_stairs.extend(self.__down_smaller + self.__up_smaller + self.__up_bigger + self.__down_bigger)

    def __classify_next_stairs(self) -> None:
        self.__up_bigger, self.__up_smaller, self.__down_bigger, self.__down_smaller = [], [], [], []
        for btn in self.__next_stairs:
            info = btn.get_btn_info()
            if info.direct == UP:
                if info.stair > self.__elevator.place_now:
                    self.__up_bigger.append(btn)
                else:
                    self.__up_smaller.append(btn)
            if info.direct == DOWN:
                if info.stair > self.__elevator.place_now:
                    self.__down_bigger.append(btn)
                else:
                    self.__down_smaller.append(btn)

    def __sort_part_of_next_stairs(self) -> None:
        self.__sort_by_stair(self.__up_bigger)
        self.__sort_by_stair(self.__up_smaller)
        self.__sort_by_stair(self.__down_bigger, True)
        self.__sort_by_stair(self.__down_smaller, True)

    def __sort_by_stair(self, the_list: [], reverse=False) -> None:
        the_list.sort(key=lambda b: b.get_btn_info().stair, reverse=reverse)

    def __direct_exception(self, direct) -> int:
        return self.__elevator.direct_former is direct and self.__elevator.direct is STOP
