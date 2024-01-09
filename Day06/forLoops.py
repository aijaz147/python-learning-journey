# For Loops

# For Loop Basics
# For loops are used to iterate over a sequence (e.g., a list, tuple, string, or range).
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Range Function
# range() generates a sequence of numbers.
for num in range(1, 4):
    print(num)

# Nested Loops
# You can nest loops to iterate over multiple sequences.
for i in range(1, 4):
    for j in ["a", "b", "c"]:
        print(i, j)

# Looping with Index
# enumerate() provides both the index and the value during iteration.
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Loop Control Statements
# break exits the loop prematurely, while continue skips the rest of the code and goes to the next iteration.
for num in range(1, 6):
    if num == 3:
        continue  # Skip iteration when num is 3
    print(num)
    if num == 4:
        break  # Exit the loop when num is 4

# Summary
# - for loops iterate over sequences. 
# - range() generates sequences of numbers.
# - Nested loops iterate over multiple sequences.
# - enumerate() provides index and value during iteration.
# - break exits the loop prematurely, and continue skips the rest of the code in the current iteration.
