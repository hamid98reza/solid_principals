import settings
from abc import ABC, abstractmethod

class Member(ABC):

    def __init__(self, name, family, id):
        self.name = name
        self.family = family
        self.id = id

    # @abstractmethod
    # def introduce_yourself(self):
    #     print(f"I am {self.name} {self.family} with id --> {self.id}")
    #     return f"I am {self.name} {self.family} with id --> {self.id}"


    # def save_member(self):
    #     with open(settings.DATA_FILE, "a") as file:
    #         file.write(self.introduce_yourself())

    #     file.close()
    #     print("saved successfully ! ")