"""
Demonstrates indentation in Python.
"""


def classify_number(value: int) -> str:
    if value > 0:
        if value % 2 == 0:
            return "positive even"
        return "positive odd"
    elif value < 0:
        return "negative"
    return "zero"



for number in [4, 7, -3, 0]:
    print(f"{number}: {classify_number(number)}")
