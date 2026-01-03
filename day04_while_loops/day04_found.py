"""
Day 04: While Loops + Control Flow (Real Logic Starts) --- while loops, break, and continue control flow

Author: Drawts

Description: The while loop repeats logic as long as a condition is true, using break to exit immediately and continue to skip the current cycle. 
Use for loops for a known number of iterations and while loops when the end point depends on a specific event or logical change.

"""

# Core Concepts

# 1 - while Loop

count = 0 
while count < 5:
    print(count)
    count += 1 # Rule: If the condition never becomes false is gonna be infinite loop


# 2 - break

while True:
    user_input = input("Type 'exit' to quit: ")

    if user_input == "exit":
        break # break exits the loop inmediately


# 3 - continue

for i in range(5):
    if i == 2:
        continue # skips the iteration
    print(i) 


""" 4 - While vs For

for "when you know how many times"
while "when you know when it stop"

"""

# Take a knowledge quiz (Python Loop Control: While, Break and Continue) here: https://gemini.google.com/share/ae6a6e1a4486