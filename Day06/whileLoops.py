# While Loops

# While Loop Basics
# while loops continue executing as long as a certain condition is true.
count = 0

while count < 5:
    print(count)
    count += 1

# Infinite Loops and Break
# Be cautious of creating infinite loops. Use break to exit the loop based on a condition.
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Continue Statement
# continue skips the rest of the code in the current iteration and moves to the next iteration.
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # Skip iteration when count is 3
    print(count)

# Else Clause with While Loop
# The else clause is executed when the while condition becomes false.
count = 0

while count < 3:
    print(count)
    count += 1
else:
    print("Loop finished")

# Summary
# - while loops continue while a condition is true.
# - Be cautious of creating infinite loops; use break to exit.
# - continue skips the rest of the code in the current iteration.
# - The else clause is executed when the while condition becomes false.
