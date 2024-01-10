# Day 8: Functions and Function Arguments

# Basic Function
# Functions are blocks of reusable code that perform a specific task.
# A basic function can be defined without any parameters.

def greet():
    print("Hello, welcome!")

# Calling the function
greet()  # Outputs: Hello, welcome!

# Function with Arguments
# Functions can take parameters (arguments) to make them more versatile.

def greet_user(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_user("Alice")  # Outputs: Hello, Alice!

# Multiple Arguments
# Functions can have multiple parameters, allowing flexibility in usage.

def add_numbers(x, y):
    result = x + y
    print(f"The sum is: {result}")

# Calling the function with multiple arguments
add_numbers(5, 3)  # Outputs: The sum is: 8

# Default Arguments
# You can set default values for function parameters.

def greet_person(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without providing an argument
greet_person()  # Outputs: Hello, Guest!

# Return Statement
# Functions can return values using the return statement.

def square(number):
    return number ** 2

# Calling the function and storing the result
result = square(4)
print(f"The square is: {result}")  # Outputs: The square is: 16

# Summary
# Functions are reusable blocks of code.
# Parameters make functions more flexible.
# Functions can have multiple parameters and default values.
# The return statement is used to send a value back from a function.