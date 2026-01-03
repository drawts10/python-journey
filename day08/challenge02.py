"""
Day 08: Challenges to test knowledge from Part 02

Author: Drawts

Description: Challenges or exercises about Guard Clause which usually focuses on "failing fast" handling the negative or edge cases at the very top so the 
rest of the function can assume everything is okay.

"""

# 1 -- The "Password Validator" Challenge


def validate_password(test_password = input("Enter your password: ")): 

    min_length = 8

    if len(test_password ) < min_length: # To check the size of the password
        return "Too short"
    if not any(char.isdigit() for char in test_password ): # Make sure password contains numbers
        return "Needs a number"
    if not any(c.isalpha() for c in test_password): # Make sure password contains letters
        return "Needs letters"
  
    return "Password strong"

result = validate_password(test_password = input("Enter your password: "))
print(result)