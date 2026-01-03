
# Exercise A -- Local Variable

def example():
    message = "Hello"
    return message

print(example())


# Exercise B -- Global vs Local

value = 100 

def show_value(): 
    value = 50
    return value

print(show_value())
print(value)


# Exercise C -- No Globals

def calculate_total(price, tax):
    return price + tax

print(calculate_total(100, 15))


# Exercise D -- Bug Fix 

count = 0

def increase(count):
    return count + 1 

count = increase(count)
print(count)

