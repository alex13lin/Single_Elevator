import tkinter as tk
HIGHEST_STAIR = 6
class TkLblElevator(object):
    def __init__(self):
        pass

    def set_stairs_label(self):
        for i in range(HIGHEST_STAIR):
            self.stairs_label = tk.Label(text=f"{i + 1}F", font=("Arial", 15), height=2,
                                         width=3)
            self.stairs_label.place(x=5, y=INIT_PLACE_Y - INIT_PLACE_Y_SPACE * i)