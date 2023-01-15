from IBtnForElevator import IBtnForElevator
from NewPrint import NewPrint as nPrint
from TkElevator import TkElevator
from model import ElevatorInfo, BtnElevatorDetail

HIGHEST_STAIR = 6


# 電梯按鈕abstract class
class BtnsForElevatorSys(IBtnForElevator):
    def __init__(self, func_name):
        self.func_name = func_name
        self.all_buttons = []

    def create_button(self, elevator_info: ElevatorInfo = None, btn_style: BtnElevatorDetail = None):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.create_button()")
        for stair in range(HIGHEST_STAIR):
            elevator_info.stair = stair
            btn = TkElevator(elevator_info, btn_style).create_button()
            self.all_buttons.append(btn)

    def get_all_buttons(self):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.get_all_buttons()")
        return self.all_buttons

    def get_func_name(self):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.get_func_name()")
        return self.func_name


# 電梯內按鈕class
class BtnsInElevator(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnsInElevator()")

    def create_button(self, elevator_info: ElevatorInfo = None, btn_style: BtnElevatorDetail = None):
        elevator_info = ElevatorInfo() if elevator_info is None else elevator_info
        elevator_info.direct = "unknown"
        btn_style = BtnElevatorDetail() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 12
        btn_style.text = None
        btn_style.x = 400
        btn_style.y = 600
        btn_style.y_space = 60
        super().create_button(elevator_info, btn_style)


# 樓層的向上按鈕
class BtnsOnStairUp(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnsOnStairUp()")

    def create_button(self, elevator_info: ElevatorInfo = None, btn_style: BtnElevatorDetail = None):
        elevator_info = ElevatorInfo() if elevator_info is None else elevator_info
        elevator_info.direct = "up"
        btn_style = BtnElevatorDetail() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▲'
        btn_style.x = 50
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_button(elevator_info, btn_style)


# 樓層的向下按鈕
class BtnsOnStairDown(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnsOnStairDown()")

    def create_button(self, elevator_info: ElevatorInfo = None, btn_style: BtnElevatorDetail = None):
        elevator_info = ElevatorInfo() if elevator_info is None else elevator_info
        elevator_info.direct = "down"
        btn_style = BtnElevatorDetail() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▼'
        btn_style.x = 120
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_button(elevator_info, btn_style)
