from BtnForElevator import BtnsInElevator, BtnsOnStairUp, BtnsOnStairDown
from ObserverPattern import ConcreteSubject
from ElevatorController import Process
from TkLblElevator import TkLblElevator
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elevator")
        self.geometry('500x700+1000+20')
        self.resizable(False, False)
        self.process = Process()
        self.process.start()
        self.btns_in_elevator = BtnsInElevator()
        self.btns_on_stair_up = BtnsOnStairUp()
        self.btns_on_stair_down = BtnsOnStairDown()
        self.elevator_subject = ConcreteSubject()
        self.lbl_elevator = TkLblElevator()
        self.start()
        self.after(10, self.refresh_window)
        self.mainloop()

    def refresh_window(self):
        self.process.process_run()
        self.lbl_elevator.set_elevator_place_label(self.process.elevator_place_now, self.process.elevator_place_y)
        self.after(10, self.refresh_window)

    def attach_elevator_subject(self):
        self.elevator_subject.attach(self.btns_in_elevator)
        self.elevator_subject.attach(self.btns_on_stair_up)
        self.elevator_subject.attach(self.btns_on_stair_down)

    def start(self):
        self.attach_elevator_subject()
        self.elevator_subject.create_buttons()
        self.set_label()
        self.process.btns_in_elevator = self.btns_in_elevator.get_all_buttons()
        self.process.btns_on_stair_up = self.btns_on_stair_up.get_all_buttons()
        self.process.btns_on_stair_down = self.btns_on_stair_down.get_all_buttons()
        self.run()

    def run(self):
        pass

    def set_label(self):
        self.lbl_elevator.set_elevator_place_label(self.process.elevator_place_now, self.process.elevator_place_y)
        self.lbl_elevator.set_stairs_label()


if __name__ == '__main__':
    MainWindow()
