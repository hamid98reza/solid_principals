from src.member import Member
from src.buyer import Buyer

class Manager(Member, Buyer):
    def __init__(self, name, family, id):
        super().__init__(name, family, id)



    def pay(self):
        return "600$"