"""
Day 02: conditional logic and boolean expressions

Author: Drawts

Description: here I explore how Python evaluates truth through Booleans and comparisons to drive decision-making using conditional if/elif/else structures. 
It also details logical operators—and, or, and not—for combining multiple rules into precise, top-to-bottom program logic.

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