"""
Day 05: Functions, parameters, and return values

Author: Drawts

Description: functions are reusable code blocks designed to perform specific tasks, helping to eliminate repetition and organize logic inot modular units. By 
utilizing parameters for input and the "return" statement for output, funcitons allow for flexible and efficient data processing across your program.

"""

# Core Concepts

# 1 - Defining a Function

def greet(): # Calling it greet()
    print("Hello")


# 2 - Parameters

name = "Mike"

def greet(name):
    print(f"Hello, {name}")


# 3 - Return Values

def add(a, b):
    return a + b # Rule: return sends data back and ends the function

result = add(3, 5)
print(result)


# 4 - Why Functions 

# BAD: 
print("Welcome")
print("Welcome")
print("Welcome")

# GOOD: 
def welcome():
    print("Welcome")


# Take a knowledge quiz (Python Functions: Definition, Parameters, and Returns) here: https://gemini.google.com/share/052ca5b2f6a9