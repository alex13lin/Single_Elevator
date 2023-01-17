import tkinter as tk
from model import BtnElevatorInfo, BtnElevatorStyle
from log import Log

IS_PRESSED = True
NOT_PRESSED = False
UNASSIGNED = 1000


class TkBtnElevator(object):
    def __init__(self):
        self.btn = None
        self.__btn_info = BtnElevatorInfo()
        self.__btn_info.state = NOT_PRESSED
        self.__log = Log()

    def run(self, btn_info: BtnElevatorInfo, btn_style: BtnElevatorStyle) -> None:
        self.__log.log()
        self.__set_btn_info(btn_info)
        self.__create_button(btn_style)
        self.__disable_btn()

    def __create_button(self, style: BtnElevatorStyle) -> None:
        self.btn = tk.Button(text=self.__set_btn_txt(style), bg="gray", height=style.height,
                             width=style.width, font=('Arial', style.fontsize))
        self.btn.place(x=style.x, y=style.y - style.y_space * self.__btn_info.stair)
        self.btn.config(command=self.update_btn)

    def __set_btn_txt(self, style: BtnElevatorStyle) -> int:
        return self.__btn_info.stair + 1 if style.text is None else style.text

    def __set_btn_info(self, btn_info: BtnElevatorInfo) -> None:
        self.__log.log()
        self.__btn_info.state = False
        self.__btn_info.direct = btn_info.direct
        self.__btn_info.stair = btn_info.stair
        self.__btn_info.the_type = btn_info.the_type
        self.__btn_info.position = btn_info.position

    def update_btn(self) -> None:
        self.__log.log()
        self.__btn_info.state = not self.__btn_info.state
        self.__btn_info.direct = UNASSIGNED if self.__btn_info.the_type is "elevator" else self.__btn_info.direct
        self.__change_btn_color()

    def __change_btn_color(self) -> None:
        self.__log.log()
        if self.__btn_info.state is IS_PRESSED:
            self.btn.config(bg='pink')
        elif self.__btn_info.state is NOT_PRESSED:
            self.btn.config(bg='gray')

    def get_btn_info(self) -> BtnElevatorInfo:
        return self.__btn_info

    def __disable_btn(self) -> None:
        if self.__btn_info.the_type == "stair_up" and self.__btn_info.position == "top":
            self.btn.config(state=tk.DISABLED)
        if self.__btn_info.the_type == "stair_down" and self.__btn_info.position == "bottom":
            self.btn.config(state=tk.DISABLED)
