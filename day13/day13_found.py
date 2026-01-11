"""
Day 13: Decoupling Control From Features (Open/Closed Principle)

Author: Drawts

Description: This is about removing menus entirely and making the system, extensible without touching control flow.

"""

# Day 13 Goal
"""
*  Add new operations without touching main() logic.

-- Open/Closed Principle: --
* Open for extension
* Closed for modification

(If we have to edit main(), we failed already).
"""

# Step 1 -- Stop Hardcoding the Menu
"""
* Here is where we remove the prints for each operation and generate the menu right from the data.
"""

# Step 2 -- Add Metadata
"""
* In this step we add data or strings by the name of each operation on the Menu, that way the system knows the Name and Bevahior.
"""

# Step 3 -- Dynamic Menu Rendering
"""
* After remove prints of operations, now we work on adding a loop so that we can call all operations from the Menu without printing out one by one.
"""

# Step 4 -- Update the Engine (Minimal change)
"""
* One changes in Menu are done, and new loop added, we need to formalize the changes by modifying a little bit the engine which is the calculate(), adding the key of the operations, basically following the loop, which added first.
"""

# Step 5 -- Control Becomes Truly Generic
"""
* Here we are updating the exit condition from 5 to 0, in order to not touch the main() again, and once we need to add any other operation, we just need to work on the math logic and Menu directly, and no more changes will be needed.
"""

# Task Assignement
"""
* After we test that the calculator works perfectly fine, we have added a power() and modulo() to prove that we cab add it without touching the main(). 
"""