
# Layer 1 -- Logic(dumb, strict, silent)

def add(a, b):return True, a + b, None
def subtract(a, b):return True, a - b, None
def multiply(a, b):return True, a * b, None
def divide(a, b): 
    if b == 0: 
        return False, None, "Division by zero not allowed"
    return True, a / b, None
def power(a, b): return True, a ^ b, None
def modulo(a, b): return True, a % b, None
        
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
        return False, None, "Invalid operation"
    
    _, operation = ACTIONS[choice]
    return operation(a, b)

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