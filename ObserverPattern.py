from abc import ABCMeta, abstractmethod
from typing import List
from IBtnForElevator import IBtnForElevator
from TkBtnElevator import TkBtnElevator


class Subject(object, metaclass=ABCMeta):
    @abstractmethod
    def attach(self, observer: IBtnForElevator) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IBtnForElevator) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._state: int
        self._observers: List[IBtnForElevator] = []

    def attach(self, observer: IBtnForElevator) -> None:
        self._observers.append(observer)

    def detach(self, observer: IBtnForElevator) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        pass

    def create_buttons(self) -> None:
        for observer in self._observers:
            observer.create_buttons()

    def print_all_buttons(self) -> None:
        for observer in self._observers:
            print(observer.get_all_buttons())

    def get_all_buttons(self) -> List[TkBtnElevator]:
        all_buttons = []
        for observer in self._observers:
            all_buttons.extend(observer.get_all_buttons())
        return all_buttons
