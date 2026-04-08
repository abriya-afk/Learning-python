"""
Demonstrates variables and constants by naming convention.
"""

PI = 3.14159
max_retries = 3


def calculate_circle_area(radius: float) -> float:
    area = PI * radius**2
    return area


def retry_demo() -> None:
    attempt = 0
    while attempt < max_retries:
        attempt += 1
        print(f"Attempt {attempt}")


print(f"Area of circle (r=2): {calculate_circle_area(2):.2f}")
retry_demo()
