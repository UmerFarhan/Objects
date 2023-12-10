from interestrewardsaccount import *

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, name, balance, type, fee):
        super().__init__(self, name, balance, type)
        self.fee = fee

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
        except BalanceException as error:
            return error