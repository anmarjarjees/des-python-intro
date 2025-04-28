# Introduction to Lists in Python

# A list is an ordered collection of items (elements).
# Lists are used to store multiple items in a single variable.
# Lists are very important in programming when we want to handle collections of data,
# like names, numbers, search results, or even API responses.

# Lists are mutable, meaning we can change their contents after creation.

# Step 1: Creating lists
fruits = ["apple", "banana", "cherry"]  # A list of strings
ages = [25, 30, 35]                     # A list of integers
prices = [19.99, 9.99, 5.99]            # A list of floats

# Step 2: Accessing elements by index
# Lists are zero-indexed, meaning the first element is at position 0.
print(f"The first fruit is: {fruits[0]}")  # apple
print(f"The second fruit is: {fruits[1]}")  # banana

# Step 3: Modifying elements
# We can update an element at a specific index.
fruits[1] = "blueberry"  # Change 'banana' to 'blueberry'
print(f"The updated fruit list is: {fruits}")

# Step 4: Adding elements
# We can add a new item to the end of the list using append().
fruits.append("mango")
print(f"Fruit list after adding mango: {fruits}")

# Step 5: Visualizing a list and index positions
# Indexes:    0        1         2        3
# Fruits:  "apple" "blueberry" "cherry" "mango"

# Lists are flexible and commonly used for handling groups of related data!

# Step 6: Removing elements
# Lists also allow removing items in different ways:

# 6.1 Removing a specific value
fruits.remove("blueberry")  # Removes the first occurrence of 'blueberry'
print(f"Fruit list after removing 'blueberry': {fruits}")

# 6.2 Removing an item by index
removed_item = fruits.pop(2)  # Removes item at index 2 ('mango') and returns it
print(f"Removed item: {removed_item}")
print(f"Fruit list after popping index 2: {fruits}")

# 6.3 Clearing the entire list
fruits.clear()  # Removes all elements from the list
print(f"Fruit list after clearing: {fruits}")

# Notes:
# - remove(value): removes the first match only. If value not found, it raises an error.
# - pop(index): removes and returns the item at the given position. If no index, removes the last item.
# - clear(): empties the list, making it an empty list [].

# For more about lists, refer to:
# - https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
