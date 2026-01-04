"""
Day 08: Real World Logic System 

Author: Drawts

Description: I had to build a small logic for a Bank Transaction System which was giving a few erros, I made the code myself, However, I corrected it below 
in order to better undertand what I waas doing wrong.

"""

# Exercises 3 -- Bank Transaction System 

# Code before look for help

def process_transaction(balance, action, amount):

# Mistake 1 - I was overwriting "action" like action = "deposit", "withdraw", "transfer" and this isn't needed. (You should never overwrite input parameters)

    if amount <= 0:
        return "Invalid amount"
    
    if action == "deposit":
        return balance + amount
    
    if action == "withdraw" or action == "transfer": # Mistake 2 - I was missing the parameter action before the "transfer", when we use (and, or) we need to enter the variable or parameter before each string desiganted on the condition.
        if amount > balance: 
            return "Insufficient funds"
        return balance - amount
    
 # Mistake 3 - We should validate action and amount positivity before checking funds.

print(process_transaction(1000, "deposit", 500))
print(process_transaction(1000, "withdraw", 300))
print(process_transaction(1000, "withdraw", 1500))
print(process_transaction(1000, "deposit", -50))
print(process_transaction(1000, "transfer", 200))


