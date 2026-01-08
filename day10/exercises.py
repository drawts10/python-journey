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

def deposit(balance, amount):

    if amount <= 0:
        return balance, "Invalid amount"
    return balance + amount, "Deposit successful"


def withdraw(balance, amount):

    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient funds"
    return balance - amount, "Withdraw successful"


def transfer(balance, amount):

    if amount <= 0:
        return balance, "Invalid amount"
    if amount > balance:
        return balance, "Insufficient funds"
    return balance - amount, "Transfer successful"

ACTIONS = {
    "1": deposit,
    "2": withdraw,
    "3": transfer,
}

def main():
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

        amount = get_positive_int("Enter amount: ")
            
        action = ACTIONS[choice]
        balance, message = action(balance, amount)

        print(message)
        print("Current Balance: ", balance)

if __name__ == "__main__":
    main()