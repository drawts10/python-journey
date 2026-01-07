
# Exercise 1 -- Safe Integer Input

def get_positive_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            positive = int(user_input)
        
            if positive > 0:
                return positive
            else:
                print("Error: Please enter a number greater than 0.")

        except ValueError:
            print((f"Error: '{user_input}' is not a valid integer. Please try again!"))
    
    
if __name__ == "__main__":
    print("Testing get_positive_int function...")
    age = get_positive_int("Enter your age: ")
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")


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