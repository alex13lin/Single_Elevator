import tkinter as tk
from model import ElevatorInfo, BtnElevatorDetail
from NewPrint import NewPrint as nPrint


class TkElevator(object):
    def __init__(self, elevator_info: ElevatorInfo, btn_style: BtnElevatorDetail):
        self.elevator_info = elevator_info
        self.btn_style = btn_style
        self.stair = self.elevator_info.stair

    def create_button(self):
        text = self.stair + 1 if self.btn_style.text is None else self.btn_style.text
        btn = tk.Button(text=text, bg="gray", height=self.btn_style.height,
                        width=self.btn_style.width, font=('Arial', self.btn_style.fontsize))
        btn.place(x=self.btn_style.x, y=self.btn_style.y - self.btn_style.y_space * self.stair)
        btn.config(command=self.print_detail)

    def print_detail(self):
        nPrint([self.stair + 1])
