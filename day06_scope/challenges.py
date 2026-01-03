

# Challenge 1: The "Security Gate" (Logic & Conditionals)

user_age = 25
has_id = True

if user_age >= 18 and has_id:
    print("Access granted")
elif user_age <= 18 and has_id:
    print("Needs parental permission")
else: 
    print("Access denied")


# Challenge 2: The "Smart Counter" (Loops & Modulo)

for i in range(1, 20):
    if i % 3 == 0:
        print(f"Number {i} is a multiple of 3")
    elif i % 2 == 0:
        print(f"Number {i} is even")
    if i == 15:
        break


# Challenge 3: The "Tip Calculator" (Functions & Scope)

def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * tip_percent / 100
    return bill_amount + tip

total = calculate_tip(50, 15)
print(f"The total bill is ${total}")


