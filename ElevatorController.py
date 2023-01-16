UP = 1
DOWN = -1
UNASSIGNED = 0
STOP = 0


class Process(object):
    def __init__(self):
        self.btns_in_elevator_info = None
        self.btns_on_stair_up_info = None
        self.btns_on_stair_down_info = None

        self.next_stairs = []

        self.elevator_place_now = 4
        self.elevator_place_next = 1

    def run(self):
        # print(self.elevator_place_now)
        self.next_stairs = []
        self.set_next_stairs(self.btns_in_elevator_info)
        self.set_next_stairs(self.btns_on_stair_up_info)
        self.set_next_stairs(self.btns_on_stair_down_info)
        self.sort_next_stairs()

        # print(self.btns_in_elevator_info)
        # print(self.btns_on_stair_up_info)
        # print(self.btns_on_stair_down_info)
        # print(self.next_stairs)

    def set_next_stairs(self, infos):
        for info in infos:
            if info.state:
                info.direct = self.set_direct(info) if info.direct == UNASSIGNED else info.direct
                self.next_stairs.append(info)

    def set_direct(self, info):
        return UP if info.stair - self.elevator_place_now > 0 else DOWN

    def sort_next_stairs(self):
        pass

    def classify_next_stairs(self):


