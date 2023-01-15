from abc import ABCMeta, abstractmethod
from typing import List
from NewPrint import NewPrint as NPrint

from IBtnForElevator import IBtnForElevator


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
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[IBtnForElevator] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: IBtnForElevator) -> None:
        NPrint(f"    ObserverPattern.py Subject: Attached an observer {observer.get_func_name()}.")
        self._observers.append(observer)

    def detach(self, observer: IBtnForElevator) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")

    def create_button(self, highest_stair):
        for observer in self._observers:
            observer.create_button(highest_stair)

    def print_all_buttons(self):
        for observer in self._observers:
            print(observer.get_all_buttons())
