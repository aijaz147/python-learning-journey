# String Slicing

# String slicing is the process of extracting a portion (substring) from a string.

# String to Slice
original_message = "Python is fun!"

# Basic Slicing
first_three_chars = original_message[0:3]
print("First three characters:", first_three_chars)

# Omitting the Start or End
substring_without_start = original_message[:6]
substring_without_end = original_message[7:]
print("Substring without start:", substring_without_start)
print("Substring without end:", substring_without_end)

# Negative Indexing
last_three_chars = original_message[-3:]
print("Last three characters:", last_three_chars)

# Stride (Step) in Slicing
every_second_char = original_message[::2]
print("Every second character:", every_second_char)

# Reverse a String
reversed_string = original_message[::-1]
print("Reversed string:", reversed_string)

# Slicing and Replacing
replaced_message = original_message[:6] + "is awesome!"
print("Replaced message:", replaced_message)

# Summary
# - String slicing allows extracting substrings from a string.
# - Basic slicing involves specifying start and end indices.
# - Omitting start or end implies the beginning or end of the string.
# - Negative indexing counts from the end of the string.
# - Stride (step) allows skipping characters during slicing.
# - Slicing can be used to reverse a string or replace parts of it.