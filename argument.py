
def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."  
    else:
        return "Invalid operation."
    
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

result = calculator(number1, number2, operation)

print(f"The result is: {result}")