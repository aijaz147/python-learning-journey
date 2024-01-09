# If-Else Conditions

# Conditional Statements
# Conditional statements allow your program to make decisions based on certain conditions.

# If Statement
# Example: Checking if a number is positive
number = 5

if number > 0:
    print("The number is positive.")

# If-Else Statement
# Example: Checking if a number is positive or negative
number = -3

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# If-Elif-Else Statement
# Example: Checking if a number is positive, negative, or zero
number = 0

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Logical Operators
# Logical operators (and, or, not) help combine multiple conditions.
# Example: Checking if a number is between 10 and 20
number = 15

if number > 10 and number < 20:
    print("The number is between 10 and 20.")

# Nested If-Else
# You can nest conditional statements to handle more complex scenarios.
# Example: Checking if a number is positive, negative, or zero using nested if-else
number = 0

if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

# Summary
# - Conditional statements (if, if-else, if-elif-else) are used for decision-making.
# - Logical operators (and, or, not) help combine multiple conditions.
# - Nested if-else statements handle more complex scenarios.