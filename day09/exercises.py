
# Exercise 1 -- Safe Integer Input

def get_positive_int(prompt):

    user_input = input(prompt)
    positive = int(user_input)

    if positive > 0: 
        return positive
    else: 
        print(f"{user_input} is an invalid intenger")
    

age = get_positive_int("Enter your age: ")
print(f"Your {age} is valid")


# Exercise 2 -- Logic Only Bank Functions

def deposit(balance, amount):
    balance = 1000
    amount = int("Enter amount to deposit: ")

    if amount <= 0:
        return balance, "Invalid amount"
    return balance + amount, "Deposit suscessful"


def withdraw(balance, amount):
    balance = 1000
    amount = int("Enter amount to withdraw: ")

    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient funds"
    return balance - amount, "Withdrawl successful"


def transfer(balance, amount):
    balance = 1000
    amount = int("Enter amount to transfer: ")

    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient funds"
    return balance - amount, "Transfer successful"

# Exercise 3 -- Action Dispatcher

ACTIONS = {
    "1": deposit,
    "2": withdraw,
    "3": transfer
}

user_input = input(f"Choose an option: {ACTIONS}")