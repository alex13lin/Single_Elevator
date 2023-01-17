import time

from SortNextStairs import SortNextStairs
from threading import Thread
from model import Elevator
from TkBtnElevator import TkBtnElevator
from typing import List

# import time
# import math

INIT_PLACE_Y = 550
INIT_PLACE_Y_SPACE = 100
UP = 1
DOWN = -1
UNASSIGNED = 1000
STOP = 0


class Process(Thread):
    def __init__(self):
        super().__init__()
        self.__sort_next_stairs = SortNextStairs()
        self.__next_stairs: List[TkBtnElevator] = []
        self.__all_buttons: List[TkBtnElevator] = []
        self.__elevator = Elevator()
        self.__set_elevator()

    def __set_elevator(self) -> None:
        self.__elevator.place_y = INIT_PLACE_Y
        self.__elevator.direct = STOP
        self.__elevator.direct_former = STOP

    def process_run(self) -> None:
        self.__elevator.run_times += 1
        self.__next_stairs.clear()
        self.__set_next_stairs(self.__all_buttons)
        self.__sort_next_stairs.run(self.__next_stairs, self.__elevator)
        self.__set_elevator_place()

    def __set_elevator_place(self) -> None:
        self.__elevator.direct_former = self.__elevator.direct
        self.__elevator_running() if len(self.__next_stairs) > 0 else self.__elevator_terminating()
        self.__set_elevator_lbl_place()
        self.__arrive_next_stair()

    def __elevator_running(self) -> None:
        self.__elevator.place_next = self.__next_stairs[0].get_btn_info().stair
        self.__elevator.direct = self.__set_direct(self.__elevator.place_next)
        self.__elevator.next_temp = int(self.__elevator.place_now)

    def __elevator_terminating(self) -> None:
        self.__set_next_temp_for_terminating()
        self.__elevator.direct = self.__set_direct(self.__elevator.place_next)

    def __set_elevator_lbl_place(self) -> None:
        self.__elevator.place_y -= 2 * self.__elevator.direct
        self.__elevator.place_now = (INIT_PLACE_Y - self.__elevator.place_y) / INIT_PLACE_Y_SPACE

    def __arrive_next_stair(self) -> None:
        if self.__elevator.place_now == self.__elevator.place_next and len(self.__next_stairs) > 0:
            btn: TkBtnElevator = self.__next_stairs[0]
            btn.update_btn()
            time.sleep(0.1)

    def __set_next_temp_for_terminating(self) -> None:
        if self.__elevator.direct > 0:
            self.__elevator.place_next = self.__elevator.next_temp + 1
        elif self.__elevator.direct < 0:
            self.__elevator.place_next = self.__elevator.next_temp

    def __set_next_stairs(self, btns: List[TkBtnElevator]) -> None:
        for btn in btns:
            info = btn.get_btn_info()
            if info.state:
                info.direct = self.__set_direct(info.stair) if info.direct == UNASSIGNED else info.direct
                self.__next_stairs.append(btn)

    def __set_direct(self, stair) -> int:
        if stair - self.__elevator.place_now > 0:
            return UP
        elif stair - self.__elevator.place_now < 0:
            return DOWN
        else:
            return STOP

    def set_all_buttons(self, all_buttons) -> None:
        self.__all_buttons = all_buttons

    def get_elevator(self) -> Elevator:
        return self.__elevator
