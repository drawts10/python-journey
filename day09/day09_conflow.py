"""
Day 09: Control Flow, Dispatching, and Safer Programs

Author: Drawts

Description: Implementing Command Dispatch to replace messy if/else chains with clean dictionary mapping. Establishing Separation of 
Concerns by decoupling UI input from core mathematical logic. Building Robust Validation to ensure the program survives hostile user 
input without crashing.

Important action from this Day was:

While loop
try/except
validation
clean return

It could be done with "No input", "No print", Logic and clear return values
"""

# Concepts for Today
# 1. Command Dispatch (IMPORTANT)

# Instead of this:
choice = ""

if choice == "1":
    ...
elif choice == "2":
    ...
elif choice == "3":
    ...


# We use mapping:

deposit = ""
withdraw = ""
actions = {
    "1": deposit,
    "2": withdraw,
}

"""

2. Input Validation (No More Crashes)

User input is hostile.
Your program must survive bad input.

We will: 

validate numbers

avoid crashes

fail safely

////////////////



3. Separation of Concerns

Today we separate:

UI (input / print)

Logic (math, rules)

Control (menu loop)

This is huge.

"""