
# Exercise A -- Simple Function

def say_hello():
    print("Hello, World")

say_hello()


# Exercise B -- Function with Parameters

def square(number):
    return number * number

print(square(4))


# Exercise C -- Function with Logic

def is_adult(age):
    if age > 18:
        return "adult"
    else:
        return "minor"
        
print(is_adult(20))


# Exercise D -- Reuse

def multiply(a, b):
    return a * b

print(multiply(2, 3))
print(multiply(5, 4))