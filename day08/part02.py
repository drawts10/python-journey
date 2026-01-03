"""
Day 08: Guard Clauses 

Author: Drawts

Description: 

"""

# BAD Style (Beginners Way)

def withdraw(balance, amount):
    if amount > 0:
        if amount <= balance:
            return balance - amount
        else:
            return "Not enough balance"
    else:
        return "Invalid amount"

# GOOD Style (Professional Way)

def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    if amount > balance:
        return "Not enough balance"
    return balance - amount


# Exercise 2 -- Rewrite with guard clauses 

def check_access(age, has_id):
    if age >= 18:
        if has_id:
            return "Access granted"
        else:
            return "ID required"
    else:
        return "Underage"
    

# Clean Version (My version)

def check_access(age, has_id):
    if age < 18:
        return "Underage"
    if not has_id:
        return "ID required"
    
    return "Access granted" # If we get here, they passed both checks!