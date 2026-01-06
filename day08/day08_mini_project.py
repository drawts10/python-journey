"""
Day 08: Mini Project -- Simple Banking System (CLI)

Author: Drawts

Description: On Day 08, I developed a procedural banking simulation that proved challenging due to the complexity of integrating multiple logic layers. While 
I initially struggled with small syntax errors and "merging" separate components, the final outcome exceeded my expectations and taught me that struggle is 
essential to the learning process. I built a system capable of checking balances, depositing, transferring, withdrawing, and exiting by defining dedicated 
functions for each operation. By utilizing a global starting balance of $1000, I mastered state management and realized that while I can handle variables and 
conditions individually, the real challenge lies in the "hand-off" between functions. I learned that print statements can coexist with logic inside conditional 
blocks and that consistent return values are vital for program stability. Finally, implementing a while True loop provided the persistent control flow necessary
to handle a continuous user interface effectively.

"""

# Goal: simulate a small bank account system using only what I already know

balance = 1000

# Function for deposit 

def deposit_transaction(balance):

    deposit_amount = int(input("Enter amount to deposit: "))

    if deposit_amount <= 0:
        print(f"Invalid amount. Current balance: {balance}")
        return balance
    else: 
        return balance + deposit_amount


# Function for Withdraw

def withdraw_transaction(balance):
    
    withdraw_amount = int(input("Enter amount to withdraw: "))

    if withdraw_amount <= 0 or withdraw_amount > balance:
        print(f"Transaction failed!. Current balance: {balance}")
        return balance
    else:
        return balance - withdraw_amount


# Function for Transfer 

def transfer_transaction(balance):

    transfer_amount = int(input("Enter amount to transfer: "))

    if transfer_amount <= 0 or transfer_amount > balance:
        print(f"Transaction failed!. Current balance: {balance}") 
        return balance
    else:
        return balance - transfer_amount
    

# Function Check Balance

def chk_balance_transaction(balance):

    print("Current Balance: ", balance)
    return balance
        

# Function exit 

def exit_program():
    print("Transaction finished. Goodbye!")

       
def get_menu_options():
    global balance
    menu_options = ("1.", "2.", "3.", "4.", "5.")  
    running = True

    while running:
        
        print()
        print("** OPTIONS**")
        print("1. = deposit")
        print("2. = withdraw")
        print("3. = transfer")
        print("4. = check balance")
        print("5. = exit")

        print()
        choice = input("Enter an option: ")

        if choice == "1.":
            balance = deposit_transaction(balance)
            print(f"Deposit successful. New Balance: {balance}")
        elif choice == "2.":
            balance = withdraw_transaction(balance) 
            print(f"Withdraw successful. New balance: {balance}")
        elif choice == "3.":
            balance = transfer_transaction(balance)
            print(f"Transfer successful. New Balance: {balance}")
        elif choice == "4.":
            balance = chk_balance_transaction(balance)
        elif choice == "5.":
            exit_program()
            running = False
        else:
            print()
            print("OPTION NOT AVAILABLE")


get_menu_options()