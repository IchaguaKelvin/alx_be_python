def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, or divide.

    Handles division by zero by returning a specific message.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Requirement: include handling for division by zero
            return "Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Invalid operation"