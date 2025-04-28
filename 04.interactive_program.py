# Building an Interactive Python Program

# In this example, we combine input, output, and control flow to create
# a small interactive program.
# Interactive programs take input from users and respond with personalized messages.

# Step 1: Take user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer

# Step 2: Greet the user
print(f"Hello, {name}!")

# Step 3: Use if/else to make decisions based on the age
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Step 4 (Optional Enhancement): Ask for another piece of information
fav_color = input("What is your favour colour? ")

# Step 5: Display a final personalized message
# We use .capitalize() to make sure the color name starts with a capital letter.

# Built-in Functions VS Methods:
# - input() and int() are built-in functions you call by their name.
# - capitalize() is a method tied to a string, 
# so you need to call it on a string object like fav_color.capitalize().

# For more about string methods, refer to:
# - https://docs.python.org/3/library/stdtypes.html#string-methods

# Important Note To Recall:
# - .capitalize() is a *method* that belongs to string objects.
# - Methods are different from functions like input() and int().
# - Methods must be called using the dot (.) notation after an object (like fav_color.capitalize()).
print(f"Nice to meet you, {name}! {fav_color.capitalize()} is a great color!")

# Note:
# - .capitalize() makes sure the color name starts with a capital letter.
# - Programs grow by combining simple input, decision-making, and output.

# For more about input/output and control flow, refer to:
# - https://docs.python.org/3/tutorial/inputoutput.html
# - https://docs.python.org/3/tutorial/controlflow.html#if-statements
