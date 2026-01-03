"""
Day 06: Scope + Function Rules

Author: Drawts

Description: Understand local and global scope. Know what lives inside a function and what doesn't. 
Avoid accidental global variable bugs. Write clear, predicatable functions. 

Scope defines the visibility and lifetime of variables, where local variables stay confined within functions while global variables are accessible script-wide.
For cleaner code, prioritize passing parameters and returning values over using the global keyword to maintain modular and predictable logic.

Summary of Rules
Local Scope: Variables created inside a function are "born" when the function starts and "die" when it ends.

Shadowing: If you use the same name for a local and global variable, the function will prioritize its own local version.

The global Keyword: This forces a function to link to the variable outside itself, though it is usually avoided because it makes code harder to track.

Pure Functions: The "Good" example shows a function that only depends on what you give it—this makes your code much easier to test.

"""

# Core Concepts

# 1 - Local Scope: variables created inside a function exits only there.

def test():
    x = 10
    print(x)

test()
# Print(x) X ERROR
# Rule: What happens inside the function stays inside the function.


# 2 - Global Scope: variables created outside functions are global.

x = 5

def show():
    print(x)

show()


# 3 - Local Overrides Global

x = 5 

def change():
    x = 10
    print(x)

change()
print(x)


# 4 - The Global Keyword (Use Sparingly)

x = 5

def change():
    global x
    x = 10

change()
print(x)


# 5 - Functions Should Return, Not Depend

# BAD:
total = 0 

def add(num): 
    global total
    total += num

# GOOD:
def add(total, num):
    return total + num

# Take a knowledge quiz (Python) here: https://gemini.google.com/share/b7c2019d1789