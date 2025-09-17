# Drawing Patterns with Nested Loops
# This program draws a square pattern using asterisks.


# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate input (must be a positive integer)
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops

row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1