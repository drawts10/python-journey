def get_valid_int(prompt):

    while True:

        user_input = input(prompt)

        try:

            number = float(user_input)
            return number

        except ValueError:
            print(f"Error: {user_input} is an invalid input. Please try again!")

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


def multiply(a, b):

    return a * b


def divide(a, b):

    return a / b

ACTIONS = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
}

def main():

    while True:

        print("\n---CALCULATOR---")

        print("\nOperations Available")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = get_valid_int(("\nChoose operation: "))

        if choice == 5:
            print("Operation Finished, Goodbye!")
            break

        if choice not in ACTIONS: 
            print("Option not available. Please try again!")
            continue

        a_number = get_valid_int("Enter A number: ")
        b_number = get_valid_int("Enter B number: ")

        if choice == 4 and b_number == 0:
            print("Cannot divide by zero")
            continue
        
        operation = ACTIONS[choice]
        print(f"Total: {operation(a_number, b_number)}")

if __name__ == "__main__":
    main()


    """

    This is my if statement before using using the ACTIONS dictionary to get output and have better structure.

        if choice == 1:
            print(f"Total: {add(a_number, b_number)}")
            continue

        if choice == 2:
            print(f"Total: {subtract(a_number, b_number)}")
            continue

        if choice == 3:
            print(f"Total: {multiply(a_number, b_number)}")
            continue

        if choice == 4:
            print(f"Total: {divide(a_number, b_number)}")
            continue
    """