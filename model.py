class Elevator(object):
    direct: int
    direct_former: int
    place_now: float = 0.0
    place_next: int = 0
    next_temp: int = 0
    place_y: float
    run_times: int = 0


class BtnElevatorInfo(object):
    stair: int
    direct: str
    state: bool
    the_type: str
    position: str


class BtnElevatorStyle(object):
    height: int = 2
    width: int = 5
    fontsize: int = 12
    text: str = None
    x: int = 0
    y: int = 0
    y_space: int = 0
