from model import Elevator

UP = 1
DOWN = -1
STOP = 0


class SortNextStairs(object):
    def __init__(self):
        self.next_stairs = None
        self.elevator = None
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []

    def run(self, next_stairs, elevator: Elevator) -> None:
        self.next_stairs = next_stairs
        self.elevator = elevator
        self.classify_next_stairs()
        self.sort_part_of_next_stairs()
        if self.elevator.direct is UP or self.direct_exception(UP):
            self.next_stairs.clear()
            self.next_stairs.extend(self.up_bigger + self.down_bigger + self.down_smaller + self.up_smaller)
        elif self.elevator.direct is DOWN or self.direct_exception(DOWN):
            self.next_stairs.clear()
            self.next_stairs.extend(self.down_smaller + self.up_smaller + self.up_bigger + self.down_bigger)

    def classify_next_stairs(self) -> None:
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

    def sort_part_of_next_stairs(self) -> None:
        self.sort_by_stair(self.up_bigger)
        self.sort_by_stair(self.up_smaller)
        self.sort_by_stair(self.down_bigger, True)
        self.sort_by_stair(self.down_smaller, True)

    def sort_by_stair(self, the_list: [], reverse=False) -> None:
        the_list.sort(key=lambda b: b.get_btn_info().stair, reverse=reverse)

    def direct_exception(self, direct) -> int:
        return self.elevator.direct_former is direct and self.elevator.direct is STOP
