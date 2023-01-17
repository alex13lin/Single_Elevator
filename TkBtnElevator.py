import tkinter as tk
from model import BtnElevatorInfo, BtnElevatorStyle
from log import Log


IS_PRESSED = True
NOT_PRESSED = False
UNASSIGNED = 1000


class TkBtnElevator(object):
    def __init__(self):
        self.btn = None
        self.btn_info = BtnElevatorInfo()
        self.btn_info.state = NOT_PRESSED
        self.log = Log()

    def create_button(self, btn_info: BtnElevatorInfo, btn_style: BtnElevatorStyle):
        self.log.log()
        self.set_btn_info(btn_info)
        text = btn_info.stair + 1 if btn_style.text is None else btn_style.text
        self.btn = tk.Button(text=text, bg="gray", height=btn_style.height,
                             width=btn_style.width, font=('Arial', btn_style.fontsize))
        self.btn.place(x=btn_style.x, y=btn_style.y - btn_style.y_space * btn_info.stair)
        self.btn.config(command=self.update_btn)
        self.disable_btn()

    def set_btn_info(self, btn_info: BtnElevatorInfo):
        self.log.log()
        self.btn_info.state = False
        self.btn_info.direct = btn_info.direct
        self.btn_info.stair = btn_info.stair
        self.btn_info.the_type = btn_info.the_type
        self.btn_info.position = btn_info.position

    def update_btn(self):
        self.log.log()
        self.btn_info.state = not self.btn_info.state
        self.btn_info.direct = UNASSIGNED if self.btn_info.the_type is "elevator" else self.btn_info.direct
        self.change_btn_color()

    def change_btn_color(self):
        self.log.log()
        if self.btn_info.state is IS_PRESSED:
            self.btn.config(bg='pink')
        elif self.btn_info.state is NOT_PRESSED:
            self.btn.config(bg='gray')

    def get_btn_info(self):
        return self.btn_info

    def disable_btn(self):
        if self.btn_info.the_type == "stair_up" and self.btn_info.position == "top":
            self.btn.config(state=tk.DISABLED)
        if self.btn_info.the_type == "stair_down" and self.btn_info.position == "bottom":
            self.btn.config(state=tk.DISABLED)

