# 1. Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# 2. Generate and Print the Multiplication Table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")