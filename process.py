from threading import Thread
import time

INIT_PLACE_Y = 550
INIT_PLACE_Y_SPACE = 100
UP = 1
DOWN = -1
STOP = 0


def elevator_direct(differ):
    if differ > 0:
        return UP
    if differ < 0:
        return DOWN
    if differ == 0:
        return STOP


def classify_next_stairs(next_stairs, elevator_place_now):
    up_bigger, up_smaller, down_bigger, down_smaller = [], [], [], []
    for next_stair in next_stairs:
        if next_stair[0] == 1:
            if next_stair[1] >= elevator_place_now:
                up_bigger.append(next_stair)
            else:
                up_smaller.append(next_stair)
        if next_stair[0] == 0:
            if next_stair[1] > elevator_place_now:
                down_bigger.append(next_stair)
            else:
                down_smaller.append(next_stair)
    return up_bigger, up_smaller, down_bigger, down_smaller


class Process(Thread):
    def __init__(self):
        super().__init__()
        self.next_stairs = []
        self.status = True
        self.elevator_place_now = 1
        self.elevator_place_next = 0
        self.elevator_place_y = INIT_PLACE_Y
        self.elevator_name = "電梯"
        self.elevator_direct = UP

    def run(self):
        while self.status:
            if len(self.next_stairs) <= 0:
                time.sleep(0.5)
            if len(self.next_stairs) > 0:
                self.sort_next_stairs()
                self.set_elevator_place()
                self.arrive_next_stair()

    def set_elevator_place(self):
        self.elevator_place_next = self.next_stairs[0][1]
        elevator_differ = self.elevator_place_next - self.elevator_place_now
        self.elevator_direct = elevator_direct(elevator_differ)
        self.elevator_place_y -= 2 * self.elevator_direct
        self.elevator_place_now = (INIT_PLACE_Y - self.elevator_place_y) / INIT_PLACE_Y_SPACE + 1
        time.sleep(0.01)

    def arrive_next_stair(self):
        if self.elevator_place_now == self.elevator_place_next:
            self.next_stairs.pop(0)
            time.sleep(1)

    def append_next_stairs(self, direct, next_stair, btn):
        if direct == '?':
            if self.elevator_place_now - next_stair > 0:
                direct = 0
            else:
                direct = 1
        self.next_stairs.append([direct, next_stair, btn])

    def sort_next_stairs(self):
        up_bigger, up_smaller, down_bigger, down_smaller = classify_next_stairs(self.next_stairs,
                                                                                self.elevator_place_now)
        up_bigger.sort()
        up_smaller.sort()
        down_bigger.sort(reverse=True)
        down_smaller.sort(reverse=True)
        if self.elevator_direct is UP:
            self.next_stairs = up_bigger + down_bigger + down_smaller + up_smaller
        elif self.elevator_direct is DOWN:
            self.next_stairs = down_smaller + up_smaller + up_bigger + down_bigger

