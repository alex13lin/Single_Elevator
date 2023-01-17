import tkinter as tk
import math

HIGHEST_STAIR = 6
INIT_PLACE_Y = 580
INIT_PLACE_Y_SPACE = 100


class TkLblElevator(object):
    def __init__(self):
        self.stairs_label = None
        self.elevator_place_label = tk.Label(font=("Arial", 18), bg="gray", height=3, width=7)

    def set_stairs_label(self):
        for i in range(HIGHEST_STAIR):
            self.stairs_label = tk.Label(text=f"{i + 1}F", font=("Arial", 15), height=2,
                                         width=3)
            self.stairs_label.place(x=5, y=INIT_PLACE_Y - INIT_PLACE_Y_SPACE * i)

    def set_elevator_place_label(self, place_now, y):
        self.elevator_place_label.config(text=math.floor(place_now) + 1)
        self.elevator_place_label.place(x=200, y=y + 5)
