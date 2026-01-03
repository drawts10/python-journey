"""
Day 08: Challenges to test knowledge from Part 01

Author: Drawts

Description: Challenges or exercises about (not, and & or)

"""

# 1 -- The "Priority" Challenge
print(True or False and not True) # True (All conditions are met, it started by "not True" which is False, then "False and False" is True, finally True or True) is True because only one needs to be True, either way it was supposed to be True.

# 2 -- The "Range" Challenge
for i in range(10, 20):
    if i % 3 == 0:
        print(True)

# 3 -- The "Membership" Challenge

fruits = ["Banana", "Cherry", "Orange"]

for f in fruits:
    if "Apple" not in fruits:
        print(True)