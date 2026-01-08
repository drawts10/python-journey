
# Exercise A -- Local Variable

def message():
    message = input("Say a phrase you like: ")
    return message

print(message())


# Exercise B -- Global vs Local

value_out = 100 

def show_value(): 
    value = 50
    return value * value_out

print(f"Total value is: {show_value()}")
print(value_out)


# Exercise C -- No Globals

def calculate_total():
    price = float(input("Enter price amount: "))
    tax = float(input("Enter tax amount: ")) / 100
    total_tax = price * tax
    return price + total_tax

print(f"Total: {calculate_total()}")


# Exercise D -- Bug Fix 

count = int(input("Enter a number to increase: "))

def increase(count):
    return count + 15

print(increase(count))

