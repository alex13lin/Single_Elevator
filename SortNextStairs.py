from model import Elevator

UP = 1
DOWN = -1
STOP = 0


class SortNextStairs(object):
    def __init__(self):
        self.next_stairs = None
        self.elevator = None
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []

    def run(self, next_stairs, elevator: Elevator):
        self.next_stairs = next_stairs
        self.elevator = elevator
        self.classify_next_stairs()
        self.sort_part_of_next_stairs()
        if self.elevator.direct is UP or self.direct_exception(UP):
            self.next_stairs = self.up_bigger + self.down_bigger + self.down_smaller + self.up_smaller
        elif self.elevator.direct is DOWN or self.direct_exception(DOWN):
            self.next_stairs = self.down_smaller + self.up_smaller + self.up_bigger + self.down_bigger
        print(f"self.down_smaller: {self.down_smaller}, self.up_smaller: {self.up_smaller}")
        print(f"self.down_bigger: {self.down_bigger}, self.up_bigger: {self.up_bigger}")

    def classify_next_stairs(self):
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []
        for btn in self.next_stairs:
            info = btn.get_btn_info()
            if info.direct == UP:
                if info.stair > self.elevator.place_now:
                    self.up_bigger.append(btn)
                else:
                    self.up_smaller.append(btn)
            if info.direct == DOWN:
                if info.stair > self.elevator.place_now:
                    self.down_bigger.append(btn)
                else:
                    self.down_smaller.append(btn)

    def sort_part_of_next_stairs(self):
        self.up_bigger.sort(key=lambda b: b.get_btn_info().stair)
        self.up_smaller.sort(key=lambda b: b.get_btn_info().stair)
        self.down_bigger.sort(key=lambda b: b.get_btn_info().stair, reverse=True)
        self.down_smaller.sort(key=lambda b: b.get_btn_info().stair, reverse=True)

    def direct_exception(self, direct):
        return self.elevator.direct_former is direct and self.elevator.direct is STOP
