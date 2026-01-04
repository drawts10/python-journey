
"""
Day 08: Refactor Without Changing Behavior

Author: Drawts

Description: In this scenario I have to re write one def I used before, try to reduce nesting, improve naming and keep exact output. I did basically the same 
thing but with different names, I was able to check also that I need to practice a lot to get better because I was doing the same function with different names
and I got confuse cause I was leaving some conditions out of the code that were causing errors.

"""

# Part 4 or Exercise 4

# Original Code 

prices = [10, 25, 5, 40, 15]

def process_cart(prices):
    
    total = 0
    for p in prices:
        total = total + p
       
    if total > 80:
        total = total * 0.9
    return total
        
total = process_cart(prices)
print(f"Final price: ${total:.2f}")


# Code re written

price_tag = [10, 25, 5, 40, 15]

def market_value(price_tag):

    total_value = 0
    for p in price_tag:
        total_value += p

    if total_value >= 80:
        return total_value * 0.9
    return total_value
    
total_value = market_value(price_tag)
print(f"Final Value: ${total_value:.2f}")
