# MatchCase

# Define a function named process_data that takes a parameter 'data'
def process_data(data):
    # Use the match statement to perform pattern matching on the 'data' parameter
    match data:
        # Case 0: If 'data' is equal to 0
        case 0:
            print("Zero")
        
        # Case 1 or 2: If 'data' is equal to 1 or 2
        case 1 | 2:
            print("One or Two")
        
        # Case for integers greater than 2: If 'data' is an integer greater than 2
        case int(n) if n > 2:
            print(f"Greater than two: {n}")
        
        # Default case (wildcard): If 'data' doesn't match any previous case
        case _:
            print("Other")

# Example usage of the process_data function with different inputs
process_data(0)    # Output: Zero
process_data(1)    # Output: One or Two
process_data(3)    # Output: Greater than two: 3
process_data('abc') # Output: Other