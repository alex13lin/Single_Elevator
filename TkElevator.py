import tkinter as tk
from model import ElevatorInfo, BtnElevatorDetail


class TkElevator(object):
    def __init__(self, elevator_info: ElevatorInfo, btn_style: BtnElevatorDetail):
        self.elevator_info = elevator_info
        self.btn_style = btn_style

    def create_button(self):
        btn = tk.Button(text=text, bg="gray", height=self.btn_style.height, width=self.btn_style.width,
                        font=('Arial', self.btn_style.fontsize))
        btn.place(x=self.btn_style.x, y=self.btn_style.y - self.btn_style.y_space * stair)