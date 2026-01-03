"""
Day 08: Boolean Logic

Author: Drawts

Description: It needs to be understood and not just use. what must be internalize:

and -- both must be true
or -- at least one must be true
not -- reverses the result

"""

# Exercise 1 -- Predict before running 

print(5 > 3 and 10 < 20) # True (Both conditions are correct)
print(5 > 3 and 10 > 20) # False (The second condition is wrong, in order to be true needs both to be right)
print(5 > 3 or 10 > 20) # True (First condiction is met)
print(not (5 > 3)) # False (Final result not right)
print(not (5 > 3 and 10 < 20)) # False 