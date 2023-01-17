from BtnForElevator import BtnsInElevator, BtnsOnStairUp, BtnsOnStairDown
from ObserverPattern import ConcreteSubject
from ElevatorController import Process
from TkLblElevator import TkLblElevator
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__set_window()
        self.__process = Process()
        self.__process.start()
        self.__elevator_subject = ConcreteSubject()
        self.__lbl_elevator = TkLblElevator()
        self.start()
        self.after(10, self.__refresh_window)
        self.mainloop()

    def __set_window(self) -> None:
        self.title("Elevator")
        self.geometry('500x700+1000+20')
        self.resizable(False, False)

    def __refresh_window(self) -> None:
        self.__process.process_run()
        self.__set_lbl_elevator()
        self.after(10, self.__refresh_window)

    def start(self) -> None:
        self.__attach_elevator_subject()
        self.__elevator_subject.create_buttons()
        self.__process.set_all_buttons(self.__elevator_subject.get_all_buttons())
        self.__set_all_lbl()

    def __attach_elevator_subject(self) -> None:
        self.__elevator_subject.attach(BtnsInElevator())
        self.__elevator_subject.attach(BtnsOnStairUp())
        self.__elevator_subject.attach(BtnsOnStairDown())

    def __set_all_lbl(self) -> None:
        self.__lbl_elevator.set_stairs_lbl()
        self.__set_lbl_elevator()

    def __set_lbl_elevator(self) -> None:
        self.__lbl_elevator.update_elevator_place_lbl(self.__process.get_elevator())


if __name__ == '__main__':
    MainWindow()
