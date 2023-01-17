INIT_PLACE_Y = 550
INIT_PLACE_Y_SPACE = 100
UP = 1
DOWN = -1
UNASSIGNED = 1000
STOP = 0


class Process(object):
    def __init__(self):
        self.btns_in_elevator_info = None
        self.btns_on_stair_up_info = None
        self.btns_on_stair_down_info = None

        self.next_stairs = []
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []

        self.elevator_place_now = 0
        self.elevator_place_next = 0
        self.elevator_next_temp = 0
        self.elevator_place_y = INIT_PLACE_Y

        self.temp_for_terminating = 0

        self.elevator_direct = STOP

    def run(self):
        print("self.elevator_place_now:", self.elevator_place_now + 1)
        self.next_stairs = []
        self.set_next_stairs(self.btns_in_elevator_info)
        self.set_next_stairs(self.btns_on_stair_up_info)
        self.set_next_stairs(self.btns_on_stair_down_info)
        self.sort_next_stairs()
        self.set_elevator_place()

        # print(self.btns_in_elevator_info)
        # print(self.btns_on_stair_up_info)
        # print(self.btns_on_stair_down_info)
        # print(self.next_stairs)

    def set_elevator_place(self):
        if len(self.next_stairs) > 0:
            info = self.next_stairs[0]
            self.elevator_place_next = info.stair
            self.elevator_direct = self.set_direct(self.elevator_place_next)
            self.temp_for_terminating = int(self.elevator_place_now)
            if self.elevator_direct == 0:
                self.arrive_next_stair()
        elif len(self.next_stairs) == 0:
            self.elevator_place_next = self.set_temp_for_terminating(self.temp_for_terminating)
            self.elevator_direct = self.set_direct(self.elevator_place_next)
        self.elevator_place_y -= 2 * self.elevator_direct
        self.elevator_place_now = (INIT_PLACE_Y - self.elevator_place_y) / INIT_PLACE_Y_SPACE

    def arrive_next_stair(self):
        info = self.next_stairs[0]
        info.state = False
        info.direct = UNASSIGNED if info.the_type is "elevator" else info.direct

    def set_temp_for_terminating(self, temp_for_terminating):
        if self.elevator_direct > 0:
            return temp_for_terminating + 1
        return temp_for_terminating

    def set_next_stairs(self, infos):
        for info in infos:
            if info.state:
                info.direct = self.set_direct(info.stair) if info.direct == UNASSIGNED else info.direct
                self.next_stairs.append(info)

    def set_direct(self, stair):
        if stair - self.elevator_place_now > 0:
            return UP
        elif stair - self.elevator_place_now < 0:
            return DOWN
        else:
            return STOP

    def sort_next_stairs(self):
        self.classify_next_stairs()
        if self.elevator_direct is UP or STOP:
            self.next_stairs = self.up_bigger + self.down_bigger + self.down_smaller + self.up_smaller
        elif self.elevator_direct is DOWN:
            self.next_stairs = self.down_smaller + self.up_smaller + self.up_bigger + self.down_bigger

    def classify_next_stairs(self):
        self.up_bigger, self.up_smaller, self.down_bigger, self.down_smaller = [], [], [], []
        for info in self.next_stairs:
            if info.direct == UP:
                if info.stair >= self.elevator_place_now:
                    self.up_bigger.append(info)
                else:
                    self.up_smaller.append(info)
            if info.direct == DOWN:
                if info.stair > self.elevator_place_now:
                    self.down_bigger.insert(0, info)
                else:
                    self.down_smaller.insert(0, info)