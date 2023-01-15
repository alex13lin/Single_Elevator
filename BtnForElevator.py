from IBtnForElevator import IBtnForElevator
from NewPrint import NewPrint as nPrint
import tkinter as tk


# 電梯按鈕abstract class
class BtnForElevatorSys(IBtnForElevator):
    def __init__(self, func_name):
        self.func_name = func_name
        self.all_buttons = []
        self.direct = 0

    def create_button(self, highest_stair, text=None, direct=None):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.create_button()")
        self.direct = direct
        for stair in range(highest_stair):
            self.all_buttons.append([stair + 1 if text is None else text, self.direct, stair + 1, True])

    def get_all_buttons(self):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.get_all_buttons()")
        return self.all_buttons

    def get_func_name(self):
        nPrint(f"    BtnForElevator.py Log: {self.func_name}.get_func_name()")
        return self.func_name


# 電梯內按鈕class
class BtnInElevator(BtnForElevatorSys):
    def __init__(self):
        super().__init__("BtnInElevator()")

    def create_button(self, highest_stair, text=None, direct="unknown"):
        super().create_button(highest_stair, text, direct)


# 樓層的向上按鈕
class BtnOnStairUp(BtnForElevatorSys):
    def __init__(self):
        super().__init__("BtnOnStairUp()")

    def create_button(self, highest_stair, text='▲', direct="up"):
        super().create_button(highest_stair, text, direct)
        self.all_buttons[-1][3] = False


# 樓層的向下按鈕
class BtnOnStairDown(BtnForElevatorSys):
    def __init__(self):
        super().__init__("BtnOnStairDown()")

    def create_button(self, highest_stair, text='▼', direct="down"):
        super().create_button(highest_stair, text, direct)
        self.all_buttons[0][3] = False
