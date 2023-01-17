class Elevator(object):
    direct: int
    direct_former: int
    place_now: float
    place_next: int
    next_temp: int
    place_y: float


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
