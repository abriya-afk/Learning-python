"""
Create the following menu driven program:
   1.Area of Circle
   2.Vowel/Consonant
   3.Odd/Even
"""

# Function to calculate the area of a circle
PI = 3.14
def area_of_circle(radius):
    return (PI * radius * radius)

# Function to check if a character is a vowel or consonant
def vowel_or_consonant(char):
    match char.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "Vowel"
        case _:
            return "Consonant"

# Function to check if a number is odd or even
def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
radius = int(input("Enter the radius of the circle: "))
letter = input("Enter a character: ")
number = int(input("Enter a number: "))

print(f"Area of the circle with radius {radius} is: {area_of_circle(radius)}")
print(f"The character '{letter}' is a {vowel_or_consonant(letter)}.")
print(f"The number {number} is {odd_or_even(number)}.")