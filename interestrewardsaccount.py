from parentbank import *

class InterestRewardsAccount(BankAccount):

    def deposit(self, amount):
        bonus = 1.05
        self.balance = self.balance + (amount * bonus)

    def __str__(self):
        return super().__str__() + f'Your account: {self.name}\n'\
            f'Has balance: ${self.balance:.2f}\n'\
                f'Account type: {self.type}\n'\
                    f'Deposit has bonus of: {bonus}'

