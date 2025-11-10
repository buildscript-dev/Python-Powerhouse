# ---------------------------------------------------------
# Basic Python Notes - Comments, Variables, Strings & Input
# ---------------------------------------------------------

# ---------------------------
# Single Line Comment
# ---------------------------
# This program will print user's name
name = "Madara"
print(name)

# If we remove the comment symbol (#) from text lines,
# Python will throw a SyntaxError since plain text is invalid code.


# ---------------------------
# Multi-Line Comment
# ---------------------------
"""
Here, we can write multi-line comments.
They help describe code blocks without needing to
comment each line individually.
"""

'''
This program calculates user score:
Step 1: Take user input
Step 2: Add 10 bonus points
Step 3: Print final score
'''
score = int(input("Enter your score: "))
print(score + 10)


# ---------------------------
# Inline Comment
# ---------------------------
x = 10  # This is the number of apples


# ---------------------------
# Variables
# ---------------------------
# A variable is a container that stores data.

varName = "value"
print(varName)

# Reassigning value
score = 20
score = score + 5  # Now score = 25

# Multiple assignment
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# Example of referencing same object
lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
# Now lst1 is also [1, 2, 3, 4]
print(lst1)

# Uncommenting next line before assigning variable causes error
# print(age)
age = 18


# ---------------------------
# String Indexing & Slicing
# ---------------------------
# Every string has an index
# Example: “hello”
# Index positions:  0 1 2 3 4   or   -5 -4 -3 -2 -1
# Characters:       h e l l o         h e l l o

name = "buildscript is coder"
print(name[0:9:1])

age = 20
print("Name: "+name+"| Age: "+age)