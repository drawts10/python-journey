
# Exercise A -- Simple Function

def say_hello():
    message = "Hello, World"
    return message

print(say_hello())


# Exercise B -- Function with Parameters

def square():

    number = int(input("Enter number: "))
    if number:
        return number * number

print(f"Result: {square()}")


# Exercise C -- Function with Logic

def is_adult():

    age = int(input("Enter your age: "))

    if age > 18:
        return "You are an adult"
    else:
        return "You are a minor"
    
print(is_adult())

# Exercise D -- Reuse

def multiply():

    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    return first_number * second_number

print(f"Result: {multiply()}")