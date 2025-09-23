# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()  # Move to next row
    row += 1