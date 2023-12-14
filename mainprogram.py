from savingsaccount import *
import sys
import csv
import random
import os

passwordManager = "accounts.csv"
accountNumbers = set()

def userCommands(username, accountNumber):
    def deposit(amount):
        username.deposit(amount)
        username.str()

    def withdraw(amount):
        username.withdraw(amount)

    def transfer(accountName, amount):
        username.transfer(amount, accountName)

    while True:
        userChoice = int(input('Please choose an action you would like to do (1-4):\n'))
        match userChoice:
            case 1:
                while True:
                    try:
                        amount = eval(input("Enter the amount you would like to deposit:\n"))
                    except ValueError:
                        print("Please keep input to numbers only")
                deposit(amount)
                break
            case 2:
                while True:
                    try:
                        amount = eval(input("Please enter the amount to withdraw:\n"))
                    except ValueError:
                        print("Please keep input to numbers only")
                withdraw(amount)
                break
            case 3:
                while True:
                    try:
                        accountName = input("Type the name of the account you want to transfer to:\n")
                        amount = eval(input("Please enter the amount to transfer:\n"))
                    except:
                        print("There was an error, please try again!")
                transfer(accountName, amount)
                break
            case 4:
                sys.exit()
            case _:
                print("That isn't an option on the list, please try again")
                continue





def menu():
    print("******* Welcome to Umer's Bank *******")
    print(("****** 1. Create Account *******"))
    print(("****** 2. Log In to your Account *******"))
    print(("****** 3. Batch Create Accounts *******"))
    print(("****** 4. Exit Program *******"))

def userMenu(username, accountNumber):
    print((f"****** Welcome {username}! *******"))
    print(("****** 1. Deposit Balance *******"))
    print(("****** 2. Withdraw Balance *******"))
    print(("****** 3. Transfer Balance *******"))
    print(("****** 4. Exit Program *******"))

def initialiseAccounts():
    try:
        with open(passwordManager, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accountNumber = row["Account Number"]
                username = row["Username"]
                password = row["Password"]
                pin = row["Pin"]
    except:
        with open(passwordManager, "w", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["Account Number", "Username", "Password", "Pin"])

initialiseAccounts()

def createAccountFile(accountNumber, username, password, pin):

    existingAccountNumbers = set()
    try:
        with open(passwordManager, "r") as file:
            reader = csv.DictReader(file)
            existingAccountNumbers = {row["Account Number"] for row in reader}
    except FileNotFoundError:
        pass

    if accountNumber in existingAccountNumbers:
        tryAgain = int(input((f"\nThe account number '{accountNumber}' already exists. Would you like to log into your existing account?\n1.Log In\n2.Try Again")))
        match tryAgain:
            case 1:
                managerLogin()
            case 2:
                anotherAccountNumber = input("Enter another account number:\n")
                anotherUsername = input("Enter your username:\n")
                anotherPassword = input("Enter your password:\n")
                anotherPin = input("Enter your pin number:\n")

                createAccountFile(anotherAccountNumber, anotherUsername, anotherPassword, anotherPin)
            case _:
                print("Sorry you've exausted too many attempts")
                sys.exit()
    
    with open(passwordManager, "a", newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([accountNumber, username, password, pin])

    print(f"Congratulations {username}, you have succesfully created an account, time to initialise your account.")

    while True:
        accountChoice = int(input("Choose which type of bank account you want to create\n1. Normal Account\
            \n2. Interest Rewards Account\n3. Savings Account"))

        match accountChoice:
            case 1:
                accountNumber = input("Please enter your account number:\n")
                initialDeposit = input("Enter initial deposit amount:\n")
                initialiseBankAccount(BankAccount, accountNumber, initialDeposit)
                break
            case 2:
                accountNumber = input("Please enter your account number:\n")
                initialDeposit = input("Enter initial deposit amount:\n")
                initialiseBankAccount(InterestRewardsAccount, accountNumber, initialDeposit)
                break
            case 3:
                accountNumber = input("Please enter your account number:\n")
                initialDeposit = input("Enter initial deposit amount:\n")
                initialiseBankAccount(SavingsAccount, accountNumber, initialDeposit)
                break
            case _:
                continue
    



counter = 2

def accountLogin():

    global counter
    print("\n*****Welcome to the login page*****\n")
    loginSuccess = False

    for i in range(counter):
        loginAccount = input("Please enter your account number:\n")
        loginUsername = input("Please enter your username:\n")
        loginPassword = input("Please enter your account password:\n")
        loginPin = input("Please enter your pin:\n")

        with open(passwordManager, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                accountNumber = row["Account Number"]
                username = row["Username"]
                password = row["Password"]
                pin = row["Pin"]

            if (loginAccount == accountNumber) and (loginUsername == username) and (loginPassword == password) and (loginPin == pin):
                os.system('cls')
                userMenu(loginUsername)
                userCommands(username, accountNumber)
                loginSuccess = True
                break
        if loginSuccess == False:
            print("\nThe account number, username, password, or pin were incorrect. Please try again!\n")
            print(f"You have {counter-i} attempts remaining!\n")
        else:
            break
    
    decision = input("You have run out of login attempts\n1. Create New Account\n2. Try one more time\n")
    match decision:
        case "1":
            print("Welcome to the account manager, we hope you have a good experience!\n")
            anotherAccountNumber = input("Enter another account number:\n")
            anotherUsername = input("Enter your username:\n")
            anotherPassword = input("Enter your password:\n")
            anotherPin = input("Enter your pin number:\n")
            createAccountFile(anotherAccountNumber, anotherUsername, anotherPassword, anotherPin)
        case "2":
            counter = 0
            accountLogin()
        case _:
            print("Attempts exhausted, exiting program")
            sys.exit()

def initialiseBankAccount(accountType, userAccountNumber, initialDeposit):
    global username
    with open(passwordManager) as file:
        reader = csv.DictReader(file)
        writer = csv.writer(file)
        for row in reader:
            accountNumber = row["Account Number"]
            username = row["Username"]
            password = row["Password"]
            pin = row["Pin"]

            if userAccountNumber == accountNumber:
                username = accountType(username, int(initialDeposit), accountType)
                userPin = input("Enter your pin number:\n")
                if userPin == pin:
                    print("Your account has been created successfully.")
                    csvFilename = username.name +  str(userAccountNumber) + ".csv"
                    with open(csvFilename, "w", newline="") as file:
                        csvwriter = csv.writer(file)
                        csvwriter.writerow(["Username", "Balance", "Account Type"])
                        csvwriter.writerow([username.name, int(username.balance), str(username.type)])



def batchAccountCreator():
    accounts = []
    user_choice = int(input("How many accounts do you want to make?\n"))

    for i in range(user_choice):
        accountNumber = input(f"Enter the account number for account #{i+1}:\n")
        accountName = input(f"Enter the account name for account #{i+1}:\n")
        accountPassword = input(f"Enter the password for account #{i+1}:\n")
        accountPin = input(f"Enter the pin for account #{i+1} to be:\n")
        createAccountFile(accountNumber, accountName, accountPassword, accountPin)
        
    for account in accounts:
        print(account.__str__())
            



def greeting():
    menu()
    user_choice = int(input("\nWhat would you like to do today?\n"))
    match user_choice:
        case 1:
            accountNumber = input("Choose an account number:\n")
            username = input("Enter the username you want:\n")
            password = input("Enter a security password:\n")
            pin = input("Choose your own pin!:\n")
            createAccountFile(accountNumber, username, password, pin)

        case 2:
            accountLogin()

        case 3:
            batchAccountCreator()

        case 4:
            sys.exit()

print("Welcome to Umer's bank!")
greeting()
"""
        case 4:
            accountNumber = input("Please enter your account number:\n")
            amount = int(input("Enter the amount you want to deposit:\n"))
            user_deposit(accountNumber, amount)

        case 5:
            username = input("Enter your username:\n")
            pin = int("Enter your pin number:\n")
            user_withdraw(username, pin)
       case 5:
        case 6:
        case _:"""

