"""
Day 02: conditional logic and boolean expressions

Author: Drawts

Description: here I explore how Python evaluates truth through Booleans and comparisons to drive decision-making using conditional if/elif/else structures. 
It also details logical operators—and, or, and not—for combining multiple rules into precise, top-to-bottom program logic.

Key Takeaways
Sequential Logic: Python evaluates conditions from top to bottom; the first True block runs, and the rest are skipped.

The "Fallback": The else statement acts as a catch-all for when no previous conditions are met.

Logical Operators: Use and when both sides must be true, and or when only one side needs to be true.

"""

# Core Concepts

"""   1- Boolean Logic (this is critical) 
True
False

# Comparisons:

age > 18
age == 18
age != 18
age <= 65
"""


# 2 - if / elif / else
age = 26

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")


""" Rules:

Python reads top to bottom

First True wins
elif is optional
else is fallback, not magic """


""" 3 - Logical Operators
and (both require to be true) comes second
or (one require to be true) comes last
not (requires to follow the logical operator) comes first

Example:  """ 

age >= 18 and age < 65

# Take a knowledge quiz "Python Logic and COnditionals" here: https://gemini.google.com/share/b0111aa35d76