# Example of using functions in Python

# Functions are reusable blocks of code that perform a specific task.
# They allow us to organize code into smaller, more manageable pieces.
# Functions can be called multiple times with different inputs, which helps reduce code duplication.
# Functions in Python are defined using the 'def' keyword.

# Step 1: Define a simple function
# Let's define a function to greet the user by their name.

def greet_user(name):
    """This function greets the user by name."""
    return f"Hello, {name}!"  # Returns a greeting message

# Call the function with the argument 'Alex'
print(greet_user("Alex"))  # Hello, Alex!

# Explanation:
# - The 'greet_user' function takes 'name' as an input parameter and returns a greeting message.
# - The return value of the function is then printed out.

# NOTE: In Python:
# The triple-quoted text """This function greets the user by name.""" is called a docstring.
# It is not a normal comment (#), but a special string used for documentation.
# 
# "Docstrings":
# > are special string literals (written between triple quotes """ """ or ''' ''') 
# > are attached to functions, classes, or modules.
# > are meant to describe what the function/class/module does.
# > can even be accessed programmatically (using help() or .__doc__)!


# Step 2: Define a function to calculate the square of a number
def square_number(number):
    """This function returns the square of a number."""
    return number ** 2  # Squares the number (number * number)

# Call the function with the argument 4
print(square_number(4))  # 16

# Explanation:
# - The 'square_number' function takes one argument 'number' and returns its square.
# - The returned value (16) is printed out.

# Step 3: Using default parameters (optional, for advanced students)
# A function can also have default values for parameters. 
# This is useful when we want a default behavior.

def greet_user_with_default(name="Guest"):
    """Greets the user with a default value if no name is provided."""
    return f"Hello, {name}!"

# Call the function without providing a name (it will use the default)
print(greet_user_with_default())  # Hello, Guest!

# Explanation:
# - The parameter 'name' has a default value of "Guest". 
# If no argument is provided when calling the function,
# it will use this default value.

# Step 4: Returning multiple values
# Functions can return multiple values, which is useful when you need more than one result.

def get_name_and_square(number):
    """Returns both the number and its square."""
    return number, number ** 2

# Call the function with the argument 5
name_and_square = get_name_and_square(5)  # (5, 25)
print(f"Number and its square: {name_and_square}")

# Explanation:
# - The 'get_name_and_square' function returns a tuple with two values: the number and its square.


# Step 5: Define a function to calculate the average of two numbers

def calculate_average(num1, num2):
    """This function returns the average of two numbers."""
    return (num1 + num2) / 2  # Add the two numbers first, then divide by 2

# Call the function with arguments 10 and 20
average_result = calculate_average(10, 20)
print(f"The average of 10 and 20 is: {average_result}")  # 15.0

# Explanation:
# - The 'calculate_average' function takes two parameters: num1 and num2.
# - It first adds the two numbers (num1 + num2), then divides the result by 2 to get the average.
# - The result (15.0) is returned and printed.

# Important Note:
# - Python follows the "order of operations" rules, 
#   also called **PEMDAS** (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
#   or **BEDMAS** (Brackets, Exponents, Division/Multiplication, Addition/Subtraction).
# 
# - In our formula (num1 + num2) / 2:
#   - Parentheses are evaluated first (addition inside the parentheses),
#   - Then division happens.
# - Without the parentheses, Python would follow normal left-to-right precedence, which could cause mistakes in more complex formulas.


# For more about functions, refer to:
# - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
