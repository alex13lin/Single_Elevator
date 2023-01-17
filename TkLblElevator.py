import tkinter as tk
import math

HIGHEST_STAIR = 6
INIT_PLACE_Y = 580
INIT_PLACE_Y_SPACE = 100


class TkLblElevator(object):
    def __init__(self):
        self.__stairs_lbl = None
        self.__elevator_place_lbl = None
        self.__set_elevator_place_lbl()

    def set_stairs_lbl(self) -> None:
        for stair in range(HIGHEST_STAIR):
            self.__stairs_lbl = tk.Label(text=f"{stair + 1}F", font=("Arial", 15), height=2, width=3)
            self.__stairs_lbl.place(x=5, y=INIT_PLACE_Y - INIT_PLACE_Y_SPACE * stair)

    def __set_elevator_place_lbl(self) -> None:
        self.__elevator_place_lbl = tk.Label(font=("Arial", 18), bg="gray", height=3, width=7)
        self.update_elevator_place_lbl()

    def update_elevator_place_lbl(self, place_now: float = 0, y: float = 0) -> None:
        self.__elevator_place_lbl.config(text=math.floor(place_now) + 1)
        self.__elevator_place_lbl.place(x=200, y=y + 5)
