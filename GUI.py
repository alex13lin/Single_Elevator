import tkinter as tk
import threading
from process import Process
import math

UPSTAIRS = 1
DOWNSTAIRS = 0
THE_HIGHEST_STAIR = 6
INIT_PLACE_Y = 580
INIT_PLACE_Y_SPACE = 600 / THE_HIGHEST_STAIR


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.stairs_label = None
        self.title("Elevator")
        self.geometry('500x700+1000+20')
        self.resizable(False, False)
        # Process的執行緒
        self.process = Process()
        self.process.start()

        self.btn_stairs = [[], []]
        self.btn_elevator = []
        self.set_btn_stairs()
        self.set_btn_elevator()
        self.elevator_place_label = None
        self.set_label()

        self.after(10, self.refresh_window)

        self.mainloop()

    def refresh_window(self):
        self.set_elevator_place_label()
        self.set_btn_stairs_status()
        self.set_btn_elevator_status()
        self.after(10, self.refresh_window)

    def set_label(self):
        self.elevator_place_label = tk.Label(font=("Arial", 18), bg="gray", height=3, width=7)
        self.set_elevator_place_label()
        self.set_stairs_label()

    def set_btn_elevator(self):
        for n in range(THE_HIGHEST_STAIR):
            self.btn_elevator.append(None)
            self.btn_elevator[n] = tk.Button(text=n + 1, bg="gray", height=2, width=5,
                                             font=("Arial", 12),
                                             command=lambda s=n + 1: self.btn_next_stairs_click(None, s))
            self.btn_elevator[n].place(x=400, y=600 - 60 * n)

    def set_btn_elevator_status(self):
        for i in range(THE_HIGHEST_STAIR):
            self.btn_elevator[i].config(state=tk.NORMAL)
        for i, j, k in self.process.next_stairs:
            if k == "elevator":
                self.btn_elevator[j - 1].config(state=tk.DISABLED)

    def btn_next_stairs_click(self, direct, stair):
        if direct is not None:
            self.process.append_next_stairs(direct, stair, "stairs")
        else:
            self.process.append_next_stairs('?', stair, "elevator")

    def set_btn_stairs(self):
        for n in range(THE_HIGHEST_STAIR):
            self.btn_stairs[UPSTAIRS].append(None)
            self.btn_stairs[UPSTAIRS][n] = tk.Button(text='▲', bg="gray", height=2, width=5,
                                                     font=15,
                                                     command=lambda s=n + 1: self.btn_next_stairs_click(UPSTAIRS, s))
            self.btn_stairs[UPSTAIRS][n].place(x=50, y=INIT_PLACE_Y - INIT_PLACE_Y_SPACE * n)

            self.btn_stairs[DOWNSTAIRS].append(None)
            self.btn_stairs[DOWNSTAIRS][n] = tk.Button(text='▼', bg="gray", height=2, width=5,
                                                       font=15,
                                                       command=lambda s=n + 1: self.btn_next_stairs_click(DOWNSTAIRS,
                                                                                                          s))
            self.btn_stairs[DOWNSTAIRS][n].place(x=120, y=INIT_PLACE_Y - INIT_PLACE_Y_SPACE * n)

    def set_btn_stairs_status(self):
        for i in range(2):
            for j in range(THE_HIGHEST_STAIR):
                self.btn_stairs[i][j].config(state=tk.NORMAL)
        self.disabled_btn()
        for i, j, k in self.process.next_stairs:
            if k == "stairs":
                self.btn_stairs[i][j - 1].config(state=tk.DISABLED)

    def disabled_btn(self):
        self.btn_stairs[UPSTAIRS][-1].config(text="N/A", bg="gray", state=tk.DISABLED)
        self.btn_stairs[DOWNSTAIRS][0].config(text="N/A", bg="gray", state=tk.DISABLED)

    def set_stairs_label(self):
        for i in range(THE_HIGHEST_STAIR):
            self.stairs_label = tk.Label(text=f"{i + 1}F", font=("Arial", 15), height=2,
                                         width=3)
            self.stairs_label.place(x=5, y=INIT_PLACE_Y - INIT_PLACE_Y_SPACE * i)

    def set_elevator_place_label(self):
        self.elevator_place_label.config(text=math.floor(self.process.elevator_place_now))
        self.elevator_place_label.place(x=200, y=self.process.elevator_place_y)


if __name__ == '__main__':
    Window = MainWindow()
    Window.process.status = False
