from parentbank import *

class InterestRewardsAccount(BankAccount):
    def __init__(self, name, balance, type):
        super().__init__(self, name, balance, type)

    def deposit(self, amount):
        bonus = 1.05
        self.balance = self.balance + (amount * bonus)

