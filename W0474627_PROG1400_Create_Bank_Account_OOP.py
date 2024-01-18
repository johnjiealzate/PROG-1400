"""
Name: Johnjie Alzate
ID No.: W0474627
Program: IT Generalist
Course: PROG1400
"""

# Class definition
class BankAccount:
    # Constructor (initialization method: __init__method)
    # Initialize the attributes of the class (variables of the the class BankAccount)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Define the method for  deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    # Define the method for withdraw
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print(f"Insufficient funds")

    # Define the method for display balance
    def display_balance (self):
        print(f"Account owner: {self.owner}, Balance: S{self.balance}")

account1 = BankAccount ("Johnjie")

# Display the balance
account1.display_balance()

# Deposit an amount
account1.deposit(1000)

# Withdraw an amount
account1.withdraw(200)