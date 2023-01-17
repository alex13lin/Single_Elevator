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

    def refresh_window(self) -> None:
        self.process.process_run()
        self.set_lbl_elevator()
        self.after(10, self.refresh_window)

    def start(self) -> None:
        self.attach_elevator_subject()
        self.elevator_subject.create_buttons()
        self.process.set_all_buttons(self.elevator_subject.get_all_buttons())
        self.set_label()

    def attach_elevator_subject(self) -> None:
        self.elevator_subject.attach(self.btns_in_elevator)
        self.elevator_subject.attach(self.btns_on_stair_up)
        self.elevator_subject.attach(self.btns_on_stair_down)

    def run(self) -> None:
        pass

    def set_label(self) -> None:
        self.set_lbl_elevator()
        self.lbl_elevator.set_stairs_label()

    def set_lbl_elevator(self) -> None:
        place_now = self.process.get_elevator_place_now()
        place_y = self.process.get_elevator_place_y()
        self.lbl_elevator.set_elevator_place_label(place_now, place_y)


if __name__ == '__main__':
    MainWindow()
