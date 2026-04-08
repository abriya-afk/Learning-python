"""
Addition, subtraction, multiplication, and division 
"""

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Addition
addition_result = number1 + number2
print(f"Addition: {number1} + {number2} = {addition_result}")

# Subtraction
subtraction_result = number1 - number2
print(f"Subtraction: {number1} - {number2} = {subtraction_result}")

# Multiplication
multiplication_result = number1 * number2
print(f"Multiplication: {number1} * {number2} = {multiplication_result}")

# Division
if number2 != 0:
    division_result = number1 / number2
    print(f"Division: {number1} / {number2} = {division_result}")
else:
    print("Division by zero is not allowed.")