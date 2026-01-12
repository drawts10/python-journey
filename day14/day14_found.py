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