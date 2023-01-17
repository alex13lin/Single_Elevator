from IBtnForElevator import IBtnForElevator
from TkElevator import BtnElevator
from model import BtnElevatorInfo, BtnElevatorStyle
from log import Log

HIGHEST_STAIR = 6
UP = 1
DOWN = -1
UNASSIGNED = 0


# 電梯按鈕abstract class
class BtnsForElevatorSys(IBtnForElevator):
    def __init__(self):
        self.log = Log()
        self.func_name = BtnsForElevatorSys.__name__
        self.all_buttons = []

    def create_buttons(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        self.log.log()
        for stair in range(HIGHEST_STAIR):
            btn_info.stair = stair
            btn_elevator = BtnElevator()
            btn_elevator.create_button(btn_info, btn_style)
            self.all_buttons.append(btn_elevator)

    def get_all_buttons(self):
        return self.all_buttons


# 電梯內按鈕class
class BtnsInElevator(BtnsForElevatorSys):
    def __init__(self):
        super().__init__()

    def create_buttons(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        btn_info = BtnElevatorInfo() if btn_info is None else btn_info
        btn_info.the_type = "elevator"
        btn_info.direct = UNASSIGNED
        btn_style = BtnElevatorStyle() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 12
        btn_style.text = None
        btn_style.x = 400
        btn_style.y = 600
        btn_style.y_space = 60
        super().create_buttons(btn_info, btn_style)


# 樓層的向上按鈕
class BtnsOnStairUp(BtnsForElevatorSys):
    def __init__(self):
        super().__init__()

    def create_buttons(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        btn_info = BtnElevatorInfo() if btn_info is None else btn_info
        btn_info.the_type = "stair"
        btn_info.direct = 1
        btn_style = BtnElevatorStyle() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▲'
        btn_style.x = 50
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_buttons(btn_info, btn_style)


# 樓層的向下按鈕
class BtnsOnStairDown(BtnsForElevatorSys):
    def __init__(self):
        super().__init__()

    def create_buttons(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        btn_info = BtnElevatorInfo() if btn_info is None else btn_info
        btn_info.the_type = "stair"
        btn_info.direct = DOWN
        btn_style = BtnElevatorStyle() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▼'
        btn_style.x = 120
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_buttons(btn_info, btn_style)
