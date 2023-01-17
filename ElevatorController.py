from SortNextStairs import SortNextStairs
from threading import Thread
from model import Elevator

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

        self.sort_next_stairs = SortNextStairs()
        self.btns_in_elevator = None
        self.btns_on_stair_up = None
        self.btns_on_stair_down = None

        self.next_stairs = []

        self.elevator = Elevator()

        self.elevator.place_now = 0
        self.elevator.place_next = 0
        self.elevator.next_temp = 0
        self.elevator.place_y = INIT_PLACE_Y

        self.temp_for_terminating = 0

        self.elevator.direct = STOP
        self.elevator.direct_former = STOP
        self.running = 1

    def process_run(self):
        self.running += 1
        print("\n", self.running)
        self.next_stairs = []
        self.set_next_stairs(self.btns_in_elevator)
        self.set_next_stairs(self.btns_on_stair_up)
        self.set_next_stairs(self.btns_on_stair_down)
        print("self.next_stairs", self.next_stairs)
        print("self.elevator.place_next:", self.elevator.place_next + 1)
        print("self.elevator.place_now:", self.elevator.place_now + 1)
        print("self.elevator.direct:", self.elevator.direct)
        print("self.elevator.direct_former:", self.elevator.direct_former)
        self.sort_next_stairs.run(self.next_stairs, self.elevator)
        self.set_elevator_place()

    def set_elevator_place(self):
        self.elevator.direct_former = self.elevator.direct
        if len(self.next_stairs) > 0:
            self.elevator.place_next = self.next_stairs[0].get_btn_info().stair
            self.elevator.direct = self.set_direct(self.elevator.place_next)
            self.temp_for_terminating = int(self.elevator.place_now)
            print("self.next_stairs", self.next_stairs)
            print("self.elevator.place_next:", self.elevator.place_next + 1)
            print("self.elevator.place_now:", self.elevator.place_now + 1)
            print("self.elevator.direct:", self.elevator.direct)
            print("self.elevator.direct_former:", self.elevator.direct_former)
        elif len(self.next_stairs) == 0:
            self.set_temp_for_terminating()
            self.elevator.direct = self.set_direct(self.elevator.place_next)
        self.set_elevator_lbl_place()
        self.arrive_next_stair()

    def set_elevator_lbl_place(self):
        self.elevator.place_y -= 2 * self.elevator.direct
        self.elevator.place_now = (INIT_PLACE_Y - self.elevator.place_y) / INIT_PLACE_Y_SPACE

    def arrive_next_stair(self):
        if self.elevator.place_now == self.elevator.place_next and len(self.next_stairs) > 0:
            print("arrive_next_stair")
            btn = self.next_stairs[0]
            btn.update_btn()

    def set_temp_for_terminating(self):
        if self.elevator.direct > 0:
            self.elevator.place_next = self.temp_for_terminating + 1
        elif self.elevator.direct < 0:
            self.elevator.place_next = self.temp_for_terminating

    def set_next_stairs(self, btns):
        for btn in btns:
            info = btn.get_btn_info()
            if info.state:
                info.direct = self.set_direct(info.stair) if info.direct == UNASSIGNED else info.direct
                self.next_stairs.append(btn)

    def set_direct(self, stair):
        if stair - self.elevator.place_now > 0:
            return UP
        elif stair - self.elevator.place_now < 0:
            return DOWN
        else:
            return STOP
