# Challenge 4: The "Shopping Cart" 

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



"""
Issues before got it right:

The Accumulator (total = total + p)

The Indentation (if and return were inside the loop's fence)

The "p" iterator variable, intead of "for total in prices" or "for price in prices", I should've had "for p in prices"
"""