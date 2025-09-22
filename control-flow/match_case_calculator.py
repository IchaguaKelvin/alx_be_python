# 1. Prompt User for Input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")
except ValueError:
    print("Invalid number entered.")
else:
    # 2. Perform the Calculation Using Match Case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}")
        case '-':
            result = num1 - num2
            print(f"The result is {result}")
        case '*':
            result = num1 * num2
            print(f"The result is {result}")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation.")