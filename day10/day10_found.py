"""
DAY 10: PROGRAM STRUCTURE & CONTROL

Author: DRAWTS

DESCRIPTION BELOW:
-----------------------------------
This module represents a transition from linear scripting to structural 
development. By wrapping execution logic within a main() function and 
utilizing the 'if __name__ == "__main__":' entry point, the code becomes 
import-safe and modular. 

Key architectural changes include:
1. Separation of Definitions: Functions only define logic; they do not execute it.
2. Controlled Entry Point: The program only runs when executed directly.
3. State Isolation: Variables like 'balance' are encapsulated within main().

-----------------------------------

Day 10 Self-Check Success

Import-Safe: If you import bank_module in another file, the menu will not pop up.

Clear Entry Point: Any developer can look at the bottom of the file and see exactly where the engine starts (main()).

Encapsulation: The balance variable is no longer a global variable; it lives and dies inside the main() function.

"""