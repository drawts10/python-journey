
# input layer

def get_valid_int(prompt):
    user_input = input(prompt)
    number = float(user_input)
    return number

# logic layer

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b): return a / b


# Dispatcher
ACTIONS = {1: add, 2: subtract, 3: multiply, 4:divide,}
choice = ACTIONS

# Error handling

def main():
    while True:
        print("---CALCULATOR---")

        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        print(f"{get_valid_int("Choose an Operation: ")}")

        try:
          if exit:
              break
          if b in 4 == 0:
              raise ValueError("Divide by zero not allowed")

        except ValueError:
            print(f"{get_valid_int} not a valid input. Please try again!")

operation = ACTIONS
print(f"Total: {get_valid_int}")

if __name__ == "__main__":
    main()