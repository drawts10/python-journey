
# Exercise A -- Age Classification

age = int(input("Enter your age: "))

if age < 12:
    print("Your are a child")
elif age < 17: 
    print("You are a teenager")
elif age < 65: 
    print("You are an adult")
else: 
    print("You are a senior")


# Exercise B -- Number Check

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Exercise C -- Simple Access Rule

have_id = input("Do you have id? (yes/no): ").lower().strip()
age = int(input("Enter your age: "))

if have_id == "yes" and age >= 18:
    print("Access granted")
else: 
    print("Access denied")