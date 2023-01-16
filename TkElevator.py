import tkinter as tk
from model import BtnElevatorInfo, BtnElevatorStyle

IS_PRESSED = True
NOT_PRESSED = False


class BtnElevator(object):
    def __init__(self):
        self.btn = None
        self.btn_info = BtnElevatorInfo()
        self.btn_info.state = False

    def create_button(self, btn_info: BtnElevatorInfo, btn_style: BtnElevatorStyle):
        self.set_btn_info(btn_info)
        text = btn_info.stair + 1 if btn_style.text is None else btn_style.text
        self.btn = tk.Button(text=text, bg="gray", height=btn_style.height,
                             width=btn_style.width, font=('Arial', btn_style.fontsize))
        self.btn.place(x=btn_style.x, y=btn_style.y - btn_style.y_space * btn_info.stair)
        self.btn.config(command=self.update_btn)

    def update_btn(self):
        self.btn_info.state = not self.btn_info.state
        self.change_btn_color()

    def set_btn_info(self, btn_info: BtnElevatorInfo):
        self.btn_info.state = False
        self.btn_info.direct = btn_info.direct
        self.btn_info.stair = btn_info.stair + 1
        self.btn_info.the_type = btn_info.the_type

    def change_btn_color(self):
        if self.btn_info.state is IS_PRESSED:
            self.btn.config(bg='pink')
        elif self.btn_info.state is NOT_PRESSED:
            self.btn.config(bg='gray')
