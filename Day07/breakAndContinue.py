# Break and Continue Statements

# Break Statement
# The break statement is used to exit a loop prematurely based on a certain condition.
for num in range(1, 6):
    if num == 3:
        break  # Exit the loop when num is 3
    print(num) 

# Continue Statement
# The continue statement skips the rest of the code in the current iteration and moves to the next iteration.
for num in range(1, 6):
    if num == 3:
        continue  # Skip iteration when num is 3
    print(num)

# Example: Using break and continue in a while loop
count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # Skip iteration when count is 3
    print(count)
    if count == 4:
        break  # Exit the loop when count is 4
