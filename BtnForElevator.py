from IBtnForElevator import IBtnForElevator
from NewPrint import NewPrint as nPrint
from model import ElevatorInfo, BtnElevatorDetail
import tkinter as tk


# 電梯按鈕abstract class
class BtnsForElevatorSys(IBtnForElevator):
    def __init__(self, func_name):
        self.func_name = func_name
        self.all_buttons = []
        self.direct = 0

    def create_button(self, highest_stair, btn_style: BtnElevatorDetail = None, direct=None):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.create_button()")
        self.direct = direct
        for stair in range(highest_stair):
            text = stair + 1 if btn_style.text is None else btn_style.text
            btn = tk.Button(text=text, bg="gray", height=btn_style.height, width=btn_style.width,
                            font=('Arial', btn_style.fontsize))
            btn.place(x=btn_style.x, y=btn_style.y - btn_style.y_space * stair)
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
        super().__init__("BtnInElevator()")

    def create_button(self, highest_stair, btn_style: BtnElevatorDetail = None, direct="unknown"):
        btn_style = BtnElevatorDetail() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 12
        btn_style.text = None
        btn_style.x = 400
        btn_style.y = 600
        btn_style.y_space = 60
        super().create_button(highest_stair, btn_style, direct)


# 樓層的向上按鈕
class BtnsOnStairUp(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnOnStairUp()")

    def create_button(self, highest_stair, btn_style: BtnElevatorDetail = None, direct="up"):
        btn_style = BtnElevatorDetail() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▲'
        btn_style.x = 50
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_button(highest_stair, btn_style, direct)


# 樓層的向下按鈕
class BtnsOnStairDown(BtnsForElevatorSys):
    def __init__(self):
        super().__init__("BtnOnStairDown()")

    def create_button(self, highest_stair, btn_style: BtnElevatorDetail = None, direct="down"):
        btn_style = BtnElevatorDetail() if btn_style is None else btn_style
        btn_style.height = 2
        btn_style.width = 5
        btn_style.fontsize = 15
        btn_style.text = '▼'
        btn_style.x = 120
        btn_style.y = 580
        btn_style.y_space = 100
        super().create_button(highest_stair, btn_style, direct)
