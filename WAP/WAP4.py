"""
4. WAP to input 3 different numbers and print the middle number.
"""

# Input three different numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the middle number
if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    middle_number = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    middle_number = num2
else:
    middle_number = num3

print(f"The middle number is: {middle_number}")