from BtnForElevator import BtnsInElevator, BtnsOnStairUp, BtnsOnStairDown
from ObserverPattern import ConcreteSubject
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.stairs_label = None
        self.title("Elevator")
        self.geometry('500x700+1000+20')
        self.resizable(False, False)

        self.btns_in_elevator = BtnsInElevator()
        self.btns_on_stair_up = BtnsOnStairUp()
        self.btns_on_stair_down = BtnsOnStairDown()
        self.elevator_subject = ConcreteSubject()
        self.attach_elevator_subject()
        self.run()

        self.mainloop()

    def attach_elevator_subject(self):
        self.elevator_subject.attach(self.btns_in_elevator)
        self.elevator_subject.attach(self.btns_on_stair_up)
        self.elevator_subject.attach(self.btns_on_stair_down)

    def run(self):
        self.elevator_subject.create_button()
        # self.elevator_subject.print_all_buttons()


if __name__ == '__main__':
    MainWindow()
