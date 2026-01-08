
"""
Day 07: Control Flow + Thinkinf in Logic

Author: Drawts

Description: I was practicing the core building blocks of Python logic! I have successfully combined data structures (lists and tuples) with control flow 
(loops and conditionals) to process and categorize information.

"""


# Exercise A -- Age Classifier (function)

def classify_age():

    age = int(input("Enter your age: "))

    if age < 18: 
        return "minor"
    elif age >= 18 and age < 65: 
        return "adult"
    else: 
        return "senior"
        
print(classify_age())


# Exercise B -- Filter Numbers

numbers = [3, 10, 21, 4, 18, 7, 65, 16, 24, 80]

for n in numbers:
    if n > 10 and n % 4 == 0:
        print(n)


# Exercise C -- Loop + logic + output

people = [
    ("Mike", 26),
    ("Ana", 17),
    ("Luis", 65),
    ("Sofia", 30)
]

for name, age in people:
    if age < 18:
        print(name, "is a minor")
    elif age >= 18 and age < 65:
        print(name, "is an adult")
    else: 
        print(name, "is a senior")

