INIT_PLACE_Y = 550
INIT_PLACE_Y_SPACE = 100
UP = 1
DOWN = -1
UNASSIGNED = 1000
STOP = 0


class Process(object):
    def __init__(self):
        self.btns_in_elevator = None
        self.btns_on_stair_up = None
        self.btns_on_stair_down = None

        self.next_stairs = []
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []

        self.elevator_place_now = 0
        self.elevator_place_next = 0
        self.elevator_next_temp = 0
        self.elevator_place_y = INIT_PLACE_Y

        self.temp_for_terminating = 0

        self.elevator_direct = STOP
        self.elevator_direct_former = STOP

    def run(self):
        self.next_stairs = []
        self.set_next_stairs(self.btns_in_elevator)
        self.set_next_stairs(self.btns_on_stair_up)
        self.set_next_stairs(self.btns_on_stair_down)
        self.sort_next_stairs()

        self.set_elevator_place()

    def set_elevator_place(self):
        self.elevator_direct_former = self.elevator_direct
        if len(self.next_stairs) > 0:
            self.elevator_place_next = self.next_stairs[0].get_btn_info().stair
            self.elevator_direct = self.set_direct(self.elevator_place_next)
            self.temp_for_terminating = int(self.elevator_place_now)
            self.arrive_next_stair()
        elif len(self.next_stairs) == 0:
            self.set_temp_for_terminating()
            self.elevator_direct = self.set_direct(self.elevator_place_next)
        self.set_elevator_lbl_place()

    def set_elevator_lbl_place(self):
        self.elevator_place_y -= 2 * self.elevator_direct
        self.elevator_place_now = (INIT_PLACE_Y - self.elevator_place_y) / INIT_PLACE_Y_SPACE

    def arrive_next_stair(self):
        if self.elevator_direct == 0:
            btn = self.next_stairs[0]
            btn.update_btn()

    def set_temp_for_terminating(self):
        if self.elevator_direct > 0:
            self.elevator_place_next = self.temp_for_terminating + 1
        self.elevator_place_next = self.temp_for_terminating

    def set_next_stairs(self, btns):
        for btn in btns:
            info = btn.get_btn_info()
            if info.state:
                info.direct = self.set_direct(info.stair) if info.direct == UNASSIGNED else info.direct
                self.next_stairs.append(btn)

    def set_direct(self, stair):
        if stair - self.elevator_place_now > 0:
            return UP
        elif stair - self.elevator_place_now < 0:
            return DOWN
        else:
            return STOP

    def sort_next_stairs(self):
        self.classify_next_stairs()
        if self.elevator_direct is UP or self.direct_exception(UP):
            self.next_stairs = self.up_bigger + self.down_bigger + self.down_smaller + self.up_smaller
        elif self.elevator_direct is DOWN or self.direct_exception(DOWN):
            self.next_stairs = self.down_smaller + self.up_smaller + self.up_bigger + self.down_bigger

    def direct_exception(self, direct):
        return self.elevator_direct_former is direct and self.elevator_direct is STOP

    def classify_next_stairs(self):
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []
        for btn in self.next_stairs:
            info = btn.get_btn_info()
            if info.direct == UP:
                if info.stair >= self.elevator_place_now:
                    self.up_bigger.append(btn)
                else:
                    self.up_smaller.append(btn)
            if info.direct == DOWN:
                if info.stair > self.elevator_place_now:
                    self.down_bigger.insert(0, btn)
                else:
                    self.down_smaller.insert(0, btn)
