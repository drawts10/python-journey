"""
Day 12: Engine & Interface Contract

Author: Drawts

Description: For this day we're making the code callable, testable and reusable. Applying contracts, engine/interface boundaries, as well as the separatin of concerns.

***Key Strenght***

Engine rule: never trust callers. Validate inputs. Always return a valid response.
Controller rule: Never proceed with invalid state. Guard the flow early.

"""

# Day 12 Goal
"""
Turn the calculator into an engine with a clear contract

* One function controls all operations
* UI never touches logic directly
* I can test everything without "input()"
"""

# New Concept: Contract
"""
This means if you give me X, I guarantee Y.

My engine will guarantee:
(success, result, error)

Always with no exceptions.
"""

# Step 1 -- Normalize all logic outputs
"""
* This can be performed by adding (success, result, error) to math functions
"""

# Step 2 -- Create the engine function
"""
* This becomes the only gateway to logic, UI never calls add, divide, etc. directly anymore.
"""

# Step 3 -- Control layer uses contract
"""
* We don't need teh try/except for logic anymore.
"""

