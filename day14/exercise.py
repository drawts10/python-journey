
# Layer 1 -- Logic(dumb, strict, silent)

def add(a, b):return Result(True, a + b)
def subtract(a, b):return Result(True, a - b)
def multiply(a, b):return Result(True, a * b)
def divide(a, b): 
    if b == 0: 
        return Result(False, error=DIVISION_BY_ZERO)
    return Result(True, a / b)
def power(a, b): return Result(True, a ** b)
def modulo(a, b): return Result(True, a % b)
        
ACTIONS = {
    1: ("Add", add),
    2: ("Subtract", subtract),
    3: ("Multiply", multiply),
    4: ("Divide", divide),
    5: ("Power", power),
    6: ("Modulo", modulo),
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
        return Result(False, error=INVALID_OPERATION)
    
    return ACTIONS[choice](a, b)

# Extra layer

class Result:
    def __init__(self, ok, value=None, error=None):
        self.ok = ok
        self.value = value
        self.error = error

DIVISION_BY_ZERO = "DIVISION_BY_ZERO"
INVALID_OPERATION = "INVALID_OPERATION"

# Layer 3 -- Control(error handling)
def main():

    while True:

        print("\n---CALCULATOR---")
        print("\nOperations Available")

        print("0. Exit")
        
        for key, (name, _) in ACTIONS.items():
            print(f"{key}. {name}")

        choice = get_valid_int("\nChoose operation: ")

        if choice == 0:
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

    """
    if result.ok:
        print(f"Total: {result.value}")
    else:
        if result.error == DIVISION_BY_ZERO:
            print("Division by zero not allowed")
        elif result.error == INVALID_OPERATION:
            print("Error: Invalid Operation")
        else:
            print("Error: Unknown error")
    
    """