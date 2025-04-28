# Introduction to Loops in Python

# A loop allows us to repeat a block of code multiple times without writing it manually.
# Loops are used to automate repetitive tasks, like processing items in a list, counting, etc.
# In Python, we have only two types of loops: "for" and "while"

# Step 1: Using a 'for' loop
# A 'for' loop is used to iterate over a sequence (like a list, string, or range).

# Let's use a list to store some names.
names = ["Alex", "Martin", "Simpson"]

# Using a 'for' loop to print a greeting for each name
for name in names:
    print(f"Hello, {name}!")  # f-string used to insert the name dynamically

# Explanation:
# - The variable 'name' takes the value of each element in 'names' list one by one.
# - The loop automatically stops when it reaches the end of the list.

# Step 2: Using a 'while' loop
# A 'while' loop keeps running as long as a condition is True.

# Example: print numbers from 0 to 4
count = 0  # Initialize count at 0
while count < 5:
    print(count)
    count += 1  # Increase count by 1 in every iteration

# Explanation:
# - First, the condition (count < 5) is checked.
# - If the condition is True, the code inside the loop runs.
# - After each iteration, 'count' is incremented by 1.
# - When 'count' reaches 5, the condition becomes False, and the loop stops.

# Important points:
# - A 'for' loop is often used when you know **how many times** you want to repeat.
# - A 'while' loop is often used when you want to repeat **until a condition changes**.

# Example of common mistakes:
# - If you forget to increment inside a 'while' loop, you might create an infinite loop!
# - Always make sure your loop will eventually stop.

# For more about loops, refer to:
# - https://docs.python.org/3/tutorial/controlflow.html#for-statements
# - https://docs.python.org/3/tutorial/controlflow.html#while-statements

