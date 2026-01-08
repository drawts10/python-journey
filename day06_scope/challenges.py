

# Challenge 1: The "Security Gate" (Logic & Conditionals)

user_age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower().strip()

if user_age >= 18 and has_id == "yes":
    print("Access granted")
elif user_age <= 18 and has_id == "yes":
    print("Needs parental permission")
else: 
    print("Access denied")


# Challenge 2: The "Smart Counter" (Loops & Modulo)

for i in range(1, 5):
    if i % 3 == 0:
        print(f"Number {i} is a multiple of 3")
    elif i % 2 == 0:
        print(f"Number {i} is even")
    if i == 5:
        break


# Challenge 3: The "Tip Calculator" (Functions & Scope)

def calculate_tip():

    bill_amount = float(input("What is the bill amount?: "))
    tip_percent = float(input("What tip percent was charged?: "))
    tip = bill_amount * tip_percent / 100
    
    return bill_amount + tip

print(f"The total bill is ${calculate_tip()}")


