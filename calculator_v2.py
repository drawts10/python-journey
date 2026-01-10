
# Layer 1 -- Logic(dumb, strict, silent)

def add(a, b):return a + b
def subtract(a, b):return a - b
def multiply(a, b):return a * b
def divide(a, b): 
    if b == 0: raise ValueError("Division by zero")
    return a / b

ACTIONS = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
}

# Layer -- Input (stupid but safe)

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid intenger")

# Layer 3 -- Control(the boss)
def main():

    while True:

        print("\n---CALCULATOR---")

        print("\nOperations Available")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    
        try: 
            choice = get_valid_int("\nChoose operation: ")

            if choice == 5:
                print("Operation Finished, Goodbye!")
                break

            if choice not in ACTIONS:
                print("Option not available. Please try again!")
                continue

            a_number = get_valid_int("Enter A number: ")
            b_number = get_valid_int("Enter B number: ")

        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue
        try:
            result = divide(a, b)
            print(result)
        except ValueError as e:
            print(e)

        operation = ACTIONS[choice]
        print(f"Total: {operation(a_number, b_number)}")

if __name__ == "__main__":
    main()
