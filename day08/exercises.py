"""
Day 08: Rewriting exercises without looking back

Author: Drawts

Description: In this file we could rebuilt logic from memory; fixe past mistakes; structure functions early; thought in conditions, not syntax. We were able 
to get more options to make our code looks better.

"""

# Exercise 1 -- Transaction Processor

def process_transaction(balance, action, amount):

    if amount <= 0:
        return "Invalid amount"
    
    if action == "deposit":
        return balance + amount
    
    if action in ("withdraw", "transfer"): # Before it was if <<< action == "withdraw" or action == "transfer" >>>
        if amount > balance:
            return "Insufficient funds"
        return balance - amount

print(process_transaction(2000, "deposit", 800))
print(process_transaction(1500, "withdraw", 450))
print(process_transaction(2000, "withdraw", 2100))
print(process_transaction(1000, "deposit", -100))
print(process_transaction(900, "transfer", 300))


# Exercise 2 -- Discount Calculator

list_cart = [25, 39, 16, 45, 35]

def products_value(list_cart):

    cart_value = 0
    for p in list_cart:
        cart_value += p # We could replace this loop by <<< sum(list_cart)

    if cart_value >= 125:
        return cart_value * 0.9
    return cart_value

cart_value = products_value(list_cart)
print(f"Your cart value is: {cart_value:.2f}")


# Exercise 3 -- User Access Validator

def verify_user(age, got_id):

    if age < 18:
        return "Underage"
    if not got_id:
        return "ID Required"
    
    return "Access granted"

print(verify_user(25, True))