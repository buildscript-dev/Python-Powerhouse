# -------------------------------------------
# Conditional Statements in Python
# -------------------------------------------

# If-Else Statement and Indentation
"""
Syntax:
if condition:
    block_of_code
else:
    other_block_of_code
"""

# Example: Check voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote.")
    # 'pass' can be used if you want to leave the block empty
    # pass
else:
    print("You cannot vote.")

# Ternary Operator (Single-line If-Else)
print("Vote") if age >= 18 else print("Not Vote")

# -------------------------------------------
# Elif Statement (Multiple Conditions)
# -------------------------------------------

# Example: Greeting by name
name = input("Enter your name: ")

if name == "Build":
    print("Welcome, Build.")
elif name == "Script":
    print("Welcome, BuildScript.")
else:
    print("Invalid Data.")

# -------------------------------------------
# Logical Operators in Conditions
# -------------------------------------------

# Example: Using 'and' operator
if 10 > 9 and 10 > 7:
    print("10 is the largest number in this comparison.")
