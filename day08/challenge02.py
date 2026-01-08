"""
Day 08: Challenges to test knowledge from Part 02

Author: Drawts

Description: Challenges or exercises about Guard Clause which usually focuses on "failing fast" handling the negative or edge cases at the very top so the 
rest of the function can assume everything is okay.

"""

# 1 -- The "Password Validator" Challenge


def validate_password(): 
    while True:
        test_password = input("Enter your password: ")

        min_length = 12

        if len(test_password ) < min_length: # Check lengh
            print("Too short")
            continue
        if not any(char.isdigit() for char in test_password ): # Check for numbers
            print("Needs a number")
            continue
        if not any(c.isalpha() for c in test_password): # Check for letters
            print("Needs letters")
            continue
        if not any(char.isupper() for char in test_password): # Check for uppecase letters
            print("Uppercase character needed")
            continue
        if not any(char in "@#%&*-" for char in test_password):
            print("Any character required")
            continue

        print("Password strong")
        return test_password
        
def main():
    secure = validate_password()
    print(f"Your password has been updated with: {secure}")

if __name__ == "__main__":
    main()

# I added clear structure to the code as well as feature that I have learned ahead