from IBtnForElevator import IBtnForElevator
from TkElevator import BtnElevator
from model import BtnElevatorInfo, BtnElevatorStyle
from log import Log

HIGHEST_STAIR = 6
log = Log()


# 電梯按鈕abstract class
class BtnsForElevatorSys(IBtnForElevator):
    def __init__(self, a):
        log.log(self.__class__.__name__)
        self.func_name = BtnsForElevatorSys.__name__
        self.all_buttons = []

    def create_button(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        log.log(self.__class__.__name__)
        for stair in range(HIGHEST_STAIR):
            btn_info.stair = stair
            BtnElevator().create_button(btn_info, btn_style)

    def get_all_buttons(self):
        return self.all_buttons

    def get_func_name(self):
        return self.func_name


# 電梯內按鈕class
class BtnsInElevator(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnsInElevator()")

    def create_button(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        btn_info = BtnElevatorInfo() if btn_info is None else btn_info
        btn_info.the_type = "elevator"
        btn_info.direct = "unknown"
        btn_style = BtnElevatorStyle() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 12
        btn_style.text = None
        btn_style.x = 400
        btn_style.y = 600
        btn_style.y_space = 60
        super().create_button(btn_info, btn_style)


# 樓層的向上按鈕
class BtnsOnStairUp(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnsOnStairUp()")

    def create_button(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        btn_info = BtnElevatorInfo() if btn_info is None else btn_info
        btn_info.the_type = "stair"
        btn_info.direct = "up"
        btn_style = BtnElevatorStyle() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▲'
        btn_style.x = 50
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_button(btn_info, btn_style)


# 樓層的向下按鈕
class BtnsOnStairDown(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnsOnStairDown()")

    def create_button(self, btn_info: BtnElevatorInfo = None, btn_style: BtnElevatorStyle = None):
        btn_info = BtnElevatorInfo() if btn_info is None else btn_info
        btn_info.the_type = "stair"
        btn_info.direct = "down"
        btn_style = BtnElevatorStyle() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▼'
        btn_style.x = 120
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_button(btn_info, btn_style)
