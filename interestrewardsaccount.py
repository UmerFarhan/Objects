from parentbank import *

class InterestRewardsAccount(BankAccount):
    def __init__(self, name, balance, type):
        super().__init__(name, balance, type)
        self.bonus = 1.05

    def deposit(self, amount):
        self.balance = self.balance + (amount * self.bonus)

    def __str__(self):
        return f'\nYour account: {self.name}\n'\
            f'Has balance: ${self.balance:.2f}\n'\
                f'Account type: {self.type}\n'\
                    f'Deposit has bonus of: {self.bonus}'

