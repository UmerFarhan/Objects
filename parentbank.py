class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, name, balance, type):
        self.name = name
        self.balance = balance
        self.type = type
    
    def __str__(self):
        return f'Account details: {self.name} ${self.balance:.2f} {self.type}'

    def deposit(self, amount):
        self.balance = self.balance + amount

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        self.viableTransaction(amount)
        self.balance = self.balance - amount
    

    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceException as error:
            return error

