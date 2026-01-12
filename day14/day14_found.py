"""
Day 14: Error Model: Result vs Exceptions.

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
* For this part we're gonna add a "class Result" with a __init__() in order to add a data contract to the code, this is the part call #Extra layer.
"""

# Step 2 -- Define error types (not strings)
"""
* This is for define the commom errors that we might get while running the code.
"""

# Step 3 -- Update logic layer (strict, silent)
"""
* For this part we're modifying the logic or math part to better get along with the actions performed before in order to fully complete the changes of the model we're introducing to the code right now.
"""

