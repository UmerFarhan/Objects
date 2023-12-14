from interestrewardsaccount import *


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, name, balance, type):
        super().__init__(name, balance, type)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
        except BalanceException as error:
            return error
        
    def __str__(self):
        return f'\nYour account: {self.name}\n'\
            f'Has balance: ${self.balance:.2f}\n'\
                f'Account type: {self.type}\n'\
                    f'Withdraw fee is: ${self.fee:.2f}\n'