from BtnForElevator import BtnsInElevator, BtnsOnStairUp, BtnsOnStairDown
from ObserverPattern import ConcreteSubject
from ElevatorController import Process
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.stairs_label = None
        self.title("Elevator")
        self.geometry('500x700+1000+20')
        self.resizable(False, False)

        self.process = Process()
        self.btns_in_elevator = BtnsInElevator()
        self.btns_on_stair_up = BtnsOnStairUp()
        self.btns_on_stair_down = BtnsOnStairDown()
        self.elevator_subject = ConcreteSubject()

        self.start()

        a = 1
        if a == 0:
            return

        self.after(10, self.refresh_window)

        self.mainloop()

    def refresh_window(self):
        self.run()
        self.after(10, self.refresh_window)

    def attach_elevator_subject(self):
        self.elevator_subject.attach(self.btns_in_elevator)
        self.elevator_subject.attach(self.btns_on_stair_up)
        self.elevator_subject.attach(self.btns_on_stair_down)

    def start(self):
        self.attach_elevator_subject()
        self.elevator_subject.create_buttons()
        self.run()

    def run(self):
        # print(self.btns_in_elevator.get_all_buttons()[0].get_btn_info().state)
        self.process.btns_in_elevator = self.btns_in_elevator.get_all_buttons()
        self.process.btns_on_stair_up = self.btns_on_stair_up.get_all_buttons()
        self.process.btns_on_stair_down = self.btns_on_stair_down.get_all_buttons()
        self.process.run()

    def set_label(self):
        self.elevator_place_label = tk.Label(font=("Arial", 18), bg="gray", height=3, width=7)
        self.set_elevator_place_label()
        self.set_stairs_label()



    def set_elevator_place_label(self):
        self.elevator_place_label.config(text=math.floor(self.process.elevator_place_now))
        self.elevator_place_label.place(x=200, y=self.process.elevator_place_y)


if __name__ == '__main__':
    MainWindow()
