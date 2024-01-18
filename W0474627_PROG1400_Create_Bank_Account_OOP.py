"""
Name: Johnjie Alzate
ID No.: W0474627
Program: IT Generalist
Course: PROG1400
"""
# Create function: create a bank account by crreating a dictionary
def create_account(owner, balance=0):
    return{"owner": owner, "balance": balance}

# Create function: deposit
def deposit(account, amount):
    account["balance"] += amount
    print(f"Deposited ${amount}. New balance: ${account['balance']}")

# Create a function: withdrawal
def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrew ${amount}. New balance: ${account['balance']}")
    else:
        print(f"Insufficient funds")

# Creatre a funciton: display balance
def display_balance (account):
    print(f"Account owner: {account['owner']}, Balance: S{account['balance']}")

# main
account1 = create_account("Davis")
print(account1)
print(f"Account: {account1}")

# Display the balance
display_balance(account1)

# Deposit an amount
deposit(account1, 1000)

# Withdraw an amount
withdraw(account1, 500)

print(type(account1))