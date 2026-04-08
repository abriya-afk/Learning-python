"""
Selection Statements Example
"""
number = 10

#if statements
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#match case
match number:
    case 0:
        print("The number is zero.")
    case 1:
        print("The number is one.")
    case _:
        print("The number is something else.")  