def get_positive_int(prompt):

    while True:

        user_input = input(prompt)

        try:

            number = int(user_input)

            if number >= 0:
                return number

            else:
                print("Enter a positive number.")

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
    4: divide
}

def main():

    while True:

        print()
        print("CALCULATOR")

        print("\nOperations Available")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = get_positive_int(("\nChoose operation: "))

        print()

        a_number = get_positive_int("Enter A number: ")
        b_number = get_positive_int("Enter B number: ")

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

        if choice not in ACTIONS: 
            print("Option not available. Please try again!")
            continue


if __name__ == "__main__":
    main()