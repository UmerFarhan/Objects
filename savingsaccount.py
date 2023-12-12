from interestrewardsaccount import *


class SavingsAccount(InterestRewardsAccount):

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + fee)
            self.balance = self.balance - (amount + fee)
        except BalanceException as error:
            return error
        
        def __str__(self):
            return super().__str__() + f'Your account: {self.name}\n'\
                f'Has balance: ${self.balance:.2f}\n'\
                    f'Account type: {self.type}\n'\
                        f'Withdraw fee is: ${fee:.2f}\n'