"""
2. WAP to input two numbers, find their square root and then calculate their(square root) sum.
"""

import math

# Input two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the square root of both numbers
sqrt_number1 = math.sqrt(number1)
sqrt_number2 = math.sqrt(number2)

# Calculate the sum of the square roots
sqrt_sum = sqrt_number1 + sqrt_number2

# Output the result
print(f"The sum of the square roots of {number1} and {number2} is: {sqrt_sum}")