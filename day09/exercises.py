
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

    if amount <= 0:
        return balance, "Invalid amount"
    return balance + amount, "Deposit successful"


def withdraw(balance, amount):

    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient funds"
    return balance - amount, "withdraw successful"


def transfer(balance, amount):

    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient funds"
    return balance - amount, "Transfer successful"

# Exercise 3 -- Action Dispatcher

ACTIONS = {
    "1": deposit,
    "2": withdraw,
    "3": transfer,
}

balance = 45000

while True:

    print("\nOptions Available: ")

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check balance")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "4":
        print(f"Current Balance: {balance}")
        continue

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ACTIONS:
        print("Invalid option")
        continue

    user_input = input("Enter amount: ")

    try:

        amount = int(user_input)
        
        action = ACTIONS[choice]
        balance, message = action(balance, amount)

        print(message)
        print("Current Balance: ", balance)

    except ValueError:
        print(f"Error: {user_input} is not a valid number")