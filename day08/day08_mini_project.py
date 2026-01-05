"""
Day 08: Mini Project -- Simple Banking System (CLI)

Author: Drawts

Description:

"""

# Goal: simulate a small bank account system using only what I already know

balance = 1000
menu_options = ('1.', '2.', '3.', '4.', '5.')         

while True:
    print()
    print("** OPTIONS**")
    print("1. = deposit")
    print("2. = withdraw")
    print("3. = transfer")
    print("4. = check balance")
    print("5. = exit")

    print()
    user_input = input("Enter an option: ")
    if user_input in menu_options:
        break
    else:
        print()
        print("OPTION NOT AVAILABLE")


# Function for deposit 

def deposit_transaction(balance, deposit, amount):

    deposit_amount = int("Enter amount to deposit: ")
    user_option = user_input

    if user_option:
        return deposit_amount
    
    if amount <= 0:
        return "Invalid amount"
    
    if deposit  == "Deposit":
        return balance + amount
    


# Function for Withdraw

def withdraw_transaction(balance, user_input, balance_forward):

    if user_input == "2.":
        return input("Enter amount to withdraw: ")
    
    if balance_forward <= 0:
        return "Invalid amount"
    
    if user_input == "Withdraw":
        if balance_forward > balance:
            return "Insufficient funds"
    return balance - balance_forward



# Function for Transfer 

def transfer_transaction(balance, user_input, amount):

    if user_input == "3.":
        return input("Enter amount to transfer: ")
    if amount <= 0:
        return "Invalid amount"
    if user_input == "Transfer":
        if amount > balance:
            return "Insufficient funds"
    return balance - amount



# Function Check Balance

def chk_balance_transaction(balance):

    if user_input == "4.":
        return balance



# Function exit 

def exit():
    if user_input == "5.":
        return exit
