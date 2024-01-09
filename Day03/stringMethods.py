# String Methods

# Strings in Python come with a variety of built-in methods to perform operations.

# String Methods
message = "Hello, Python!"

# Changing Case
print("Original Message:", message)
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())

# Counting Occurrences
substring = "o"
print("Occurrences of 'o':", message.count(substring))

# Finding Substrings
search_term = "Python"
print("Index of 'Python':", message.find(search_term))

# Replacing Substrings
new_message = message.replace("Python", "World")
print("Replaced Message:", new_message)

# Checking Start and End
starts_with_hello = message.startswith("Hello")
ends_with_python = message.endswith("Python!")
print("Starts with 'Hello':", starts_with_hello)
print("Ends with 'Python!':", ends_with_python)

# Stripping Whitespace
whitespace_message = "    Python    "
stripped_message = whitespace_message.strip()
print("Original Message:", whitespace_message)
print("Stripped Message:", stripped_message)

# String Formatting
name = "Alice"
age = 25
formatted_message = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_message)

# f-String (Python 3.6+)
f_string_message = f"Hello, {name}! You are {age} years old."
print(f_string_message)

# Summary
# - String methods offer various operations on strings.
# - Methods like lower(), upper(), count(), find(), replace(), startswith(), endswith(), strip() are useful.
# - String formatting allows dynamic construction of strings.