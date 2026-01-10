
# Layer 1 -- Logic(dumb, strict, silent)

def add(a, b):return True, a + b, None
def subtract(a, b):return True, a - b, None
def multiply(a, b):return True, a * b, None
def divide(a, b): 
    if b == 0: 
        return False, None, "Division by zero not allowed"
    return True, a / b, None
        
ACTIONS = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
}

# Layer -- Input (safe, defensive)

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer")

# Engine function

def calculate(choice, a, b):
    if choice not in ACTIONS:
        return False, None, "Invalid operation"
    return ACTIONS[choice](a, b)

# Layer 3 -- Control(error handling)
def main():

    while True:

        print("\n---CALCULATOR---")

        print("\nOperations Available")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = get_valid_int("\nChoose operation: ")

        if choice == 5:
            print("Operation Finished, Goodbye!")
            break

        if choice not in ACTIONS:
            print("Invalid option")
            continue
        
        a_number = get_valid_int("Enter A number: ")
        b_number = get_valid_int("Enter B number: ")

        success, result, error = calculate(choice, a_number, b_number)

        if success:
            print(f"Total: {result}")
        else: 
            print(f"Error: {error}")
       
if __name__ == "__main__":
    main()