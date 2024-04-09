from abc import ABC, abstractmethod


class Buyer(ABC):
    def __init__(self, amnt):
        pass

    @abstractmethod
    def pay(self):
        pass