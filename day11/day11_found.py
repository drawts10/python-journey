"""
Day 11: Separation of Concerns & Function Contracts

Author: Drawts

Description: Here I'm gonna show relevant information of things I'm not gonna do no more, in order to improve performance on writing working scripts, there are some rules I need to implement for me to get to levelup my programming skills with python:

"""

# Rule 1 -- NO FUNCTION TRUST THE CALLER
"""
The functions of my calculator assume valid input, That's not good.

From now on:

* Every logic function validates its own inputs
* UI does NOT handle business rules
"""

# Rule 2 -- UI DOES NOT MAKE DECISIONS
"""
main() should:

* Display menus
* Read input
* Call functions
* Handle errors

(NOTHING ELSE)
"""

# Rule 3 -- ONE FUNCTION, ONE RESPONSABILITY
"""
If a function:

* Prints 
* Calculates
* Validates

It's already wrong
"""

## TODAY'S TASK IS: BUILD CALCULATOR V2

# REQUIREMENTS: 

# 1 -- LOGIC LAYER
"""
* add(a, b)
* subtract(a, b)
* multiply(a, b)
* divide(a, b)
"""


# 2 -- INPUT LAYER
"""
* One function for reading intengers
* No math inside it
"""


# 3 -- DISPATCHER
"""
* Dictionary maps options to functions
* No "if choice == 1" chains
"""


# 4 -- ERROR HANDLING
"""
* try / except only in main()
* Logic functions raise errors, never print
"""


# 5 -- EXIT IS CLEAN
"""
* Exit is handled explicity
* No magic numbers scattered
"""