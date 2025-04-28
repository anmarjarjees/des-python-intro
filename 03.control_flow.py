# Introduction to Control Flow in Python

# In programming, "control flow" means deciding which instructions to execute
# based on certain conditions.
# Control flow structures like "if", "else", and "elif" (else-if) help programs
# make decisions and behave differently in different situations.

# Example 1: Basic if/else statement

# Ask the user for their age
# input() function always returns a string type.
# We wrap it with int() to immediately convert the string into an integer.
# This is an example of calling one function inside another (nested function call).
# It is the same as:
# user_input = input("Enter your age: ")  # Get input as string
# age = int(user_input)                   # Then convert to integer
# But combining them makes the code shorter and cleaner.
age = int(input("Enter your age: "))  # Nested function call

# For more about nested function calls, you can refer to:
# - https://docs.python.org/3/reference/expressions.html#calls


# NOTE: Python's Strict Indentation Requirement:
# Indentation is mandatory in Python (it's not just for readability like in some other languages — it controls the program's logic).
# Incorrect indentation will cause errors or unexpected behaviors (code outside the if/else block when it shouldn't be).

# Tips to consider:
# - Typically, use 4 spaces for each indentation level (this is the standard in Python).
# - Be consistent: never mix tabs and spaces!

# Simple decision based on age
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# How it works:
# - if the condition (age >= 18) is True, the first block runs.
# - else, the second block runs.


# Example 2: Using if/elif/else for multiple conditions

# Let's create more detailed categories based on age
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Note:
# - 'elif' stands for "else if" and lets us check multiple conditions one after another.
# - Python checks conditions from top to bottom and runs the first True condition.


# Important: Python uses indentation (spaces) to define blocks of code.
# Code that belongs to an "if", "else", or "elif" must be indented under it.
# Incorrect indentation will cause errors or wrong behavior.

# Correct example:
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Incorrect example (will cause an IndentationError):
# if age >= 18:
# print("You are an adult.")  # Missing indentation!

# Another incorrect example (logic error, not syntax error):
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
print("You need to wait!")  # This line runs NO MATTER WHAT (not inside else block)

# For more about Python's indentation rules, refer to:
# - https://docs.python.org/3/reference/lexical_analysis.html#indentation

# For more about control flow statements, refer to:
# - https://docs.python.org/3/tutorial/controlflow.html#if-statements
