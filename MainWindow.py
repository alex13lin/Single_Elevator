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
        self.__process = Process()
        self.__process.start()
        self.__btns_in_elevator = BtnsInElevator()
        self.__btns_on_stair_up = BtnsOnStairUp()
        self.__btns_on_stair_down = BtnsOnStairDown()
        self.__elevator_subject = ConcreteSubject()
        self.__lbl_elevator = TkLblElevator()
        self.start()
        self.after(10, self.__refresh_window)
        self.mainloop()

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
        self.__elevator_subject.attach(self.__btns_in_elevator)
        self.__elevator_subject.attach(self.__btns_on_stair_up)
        self.__elevator_subject.attach(self.__btns_on_stair_down)

    def run(self) -> None:
        pass

    def __set_all_lbl(self) -> None:
        self.__set_lbl_elevator()
        self.__lbl_elevator.set_stairs_lbl()

    def __set_lbl_elevator(self) -> None:
        place_now = self.__process.get_elevator_place_now()
        place_y = self.__process.get_elevator_place_y()
        self.__lbl_elevator.set_elevator_place_lbl(place_now, place_y)


if __name__ == '__main__':
    MainWindow()
