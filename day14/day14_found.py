"""
Day 14: Error Model: Result vs Exceptions.

Author: Drawts

Error Handling Philosophy: Result Objects vs. Exceptions

This module explores the two primary ways to handle failures:

1. Model A (Result Objects): 
   - Returns a tuple like (success, result, error). 
   - Inspired by C/Go/Rust. 
   - Pros: Explicit, predictable, no 'hidden' jumps. 
   - Cons: Verbose, easy to accidentally ignore errors.

2. Model B (Exceptions): 
   - Uses 'raise' and 'try/except' blocks. 
   - The Pythonic standard for most apps.
   - Pros: Clean code, errors can't be ignored, carries rich metadata. 
   - Cons: Can hide control flow, potentially dangerous if misused.

Key Takeaway: Neither is 'better,' but consistency is king. Use Result 
objects for safety-critical/embedded logic and Exceptions for large-scale 
application flow.


| Context              | Correct Model    |
| -------------------- | ---------------- |
| Beginner learning    | Result           |
| CLI tools            | Either           |
| APIs                 | Exceptions       |
| Libraries            | Exceptions       |
| Embedded / safety    | Result           |
| Large systems        | Exceptions       |
| Financial / critical | Result or hybrid |

"""

# Step 1 -- Define a Result type (logic-level only)
"""
* For this part we're gonna add a "class Result" with a __init__() in order to define a unifrom return shape unforced across layers "add a data contract to the code", this is the part call #Extra layer.
"""

# Step 2 -- Define error types (not strings)
"""
* This is for define the commom errors that we might get while running the code.
"""

# Step 3 -- Update logic layer (strict, silent)
"""
* For this part we're modifying and replacing the responsibility of the logic or math part to better get along with the actions performed before (logic must obey the contract) in order to fully complete the changes of the model we're introducing to the code right now.
"""

# Step 4 -- Engine stays dumb but safe
"""
* Aplying the new error types defined for the calculate() and updating the return part.
"""

# Step 5 -- Control layter interprets meaning 
"""
* Here we remove the tuple-unpacking logic to execute the calculate() on the main() and updating with the new option used which is Result and its exceptions. We replaced it with object based interpretation.
"""


# Few questions
"""
* What broke today?

I broke the exceptions and returns from the logic code which is success, result and error. By breaking that, I had to update the calculate and main(). Had to create a class along with a __init__() for the new exception and result I was supposed to use for this day.

* What rule did I learn?

For we to use the Result Objects, we always have to follow the instructions from the class result, applying the rules on the logic of your code, as well update the outputs or main() of your code to do what the class ask it to do. (Basically if a contract changes, every produces and consumer must obey it).

* What would past-me have done wrong here?

I violated the contract from the class result by not adding the name of the class which was result at the beginning of each return on the math logic of the code. It was fixed by just adding Result after each return, and put the success along with the parameters in a parentheses, for example: return Result(True, a + b)
"""