# Introduction to Input and Output in Python

# In Python, we can interact with the user using input and output.
# - The input() function allows us to ask the user for information.
# - The print() function lets us display messages or results to the user.

# Example 1: Basic Input and Output

# Ask the user to enter their name
name = input("Enter your name: ")  # input() returns a string by default

# Display a personalized greeting
print(f"Hello, {name}!")

# Note:
# - The 'f' before the string means we are using an "f-string" (formatted string literal).
# - Inside the f-string, anything inside curly braces {} will be replaced with its value.
# - Example: If name = "Alex", then f"Hello, {name}!" becomes "Hello, Alex!"

# More about f-strings:
# - https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals


# Example 2: Taking multiple inputs and displaying formatted output

# Ask for more information
age = input("Enter your age: ")
city = input("Where do you live (in which city)? ")

# Display a summary using multiple variables
print(f"{name} is {age} years old and lives in {city}.")

# Reminder:
# - All inputs taken using input() are of type string.
# - If you need to use numbers (like for calculations), you should convert input to int or float.

# Example: Converting input to an integer
birth_year = int(input("Enter your birth year: "))  # int() converts string to integer
current_year = 2025
age_calculated = current_year - birth_year

print(f"Based on your birth year, you are approximately {age_calculated} years old.")

# For more about input() and print(), refer to:
# - https://docs.python.org/3/library/functions.html#input
# - https://docs.python.org/3/library/functions.html#print
