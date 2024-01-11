# Day 9: Lists and List Methods

# Creating Lists
# Lists are ordered and mutable collections in Python.
# Elements can be of different data types.

# Example of creating a list
fruits = ["apple", "banana", "orange"]

# Accessing List Elements
# Elements in a list are accessed using index values.

# Example of accessing list elements
first_fruit = fruits[0]
print(first_fruit)  # Outputs: apple

# List Methods
# Lists have built-in methods for common operations.

# Adding Elements
# Append: Adds an element to the end of the list
fruits.append("grape")

# Insert: Adds an element at a specific index
fruits.insert(1, "kiwi")

# Removing Elements
# Remove: Removes the first occurrence of a specified value
fruits.remove("banana")

# Pop: Removes and returns an element at a specific index (default is the last element)
removed_fruit = fruits.pop(2)

# Other Methods
# Len: Returns the number of elements in the list
num_fruits = len(fruits)

# Count: Returns the number of occurrences of a specified value
num_apples = fruits.count("apple")

# Sort: Sorts the elements of the list
fruits.sort()

# Reverse: Reverses the order of the list
fruits.reverse()

# Summary
# Lists are ordered and mutable collections in Python.
# List elements are accessed using index values.
# Lists have various methods for adding, removing, and manipulating elements.