# Variables and Data Types

# Variables
# In Python, variables are used to store and manage data.
# You can think of a variable as a named container for a value.

# Creating Variables
age = 25
name = "John"

# Variable Naming Rules
# - Must start with a letter or underscore (_).
# - Can only contain letters, numbers, and underscores.
# - Case-sensitive (age and Age are different).

# Printing Variables
print("Name:", name)
print("Age:", age)

# Data Types
# Variables can hold different types of data.

# Common Data Types
# 1. Integers (int): Whole numbers without decimal points.
my_integer = 42

# 2. Floats (float): Numbers with decimal points.
my_float = 3.14

# 3. Strings (str): Text or a sequence of characters.
my_string = "Hello, Python!"

# 4. Booleans (bool): Represents either True or False.
is_student = True

# Checking Data Types
print("Type of age:", type(age))
print("Type of name:", type(name))
print("Type of my_float:", type(my_float))
print("Type of is_student:", type(is_student))

# Type Conversion
# Converting a float to an integer
float_number = 5.6
integer_number = int(float_number)

# Converting an integer to a string
age_string = str(age)

# Operations with Variables
# Mathematical Operations
result = age + 5
print("Age in 5 years:", result)

# String Concatenation
greeting = "Hello, " + name + "!"
print(greeting)

# Summary
# - Variables store and manage data.
# - Common data types: int, float, str, bool.
# - Use type() to check the data type of a variable.
# - Convert between data types when needed.