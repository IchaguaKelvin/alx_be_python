# 1. Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# 2. Draw the Pattern
row = 0
while row < size:
    for column in range(size):
        print("*", end="")
    print()
    row += 1