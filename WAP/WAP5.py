"""
5. WAP to input marks in 5 subjects and then calculate total marks, percentage, division and result(pass/fail).
"""

# Input marks for 5 subjects
mark1= float(input("Enter marks for subject 1: "))
mark2= float(input("Enter marks for subject 2: "))
mark3= float(input("Enter marks for subject 3: "))
mark4= float(input("Enter marks for subject 4: "))
mark5= float(input("Enter marks for subject 5: "))

# Calculate total marks
total_marks = mark1 + mark2 + mark3 + mark4 + mark5

# Calculate percentage
percentage = (total_marks / 500) * 100

# Determine division
if percentage >= 60:
    division = "First"
elif percentage >= 50:
    division = "Second"
else:
    division = "Third"

# Determine result
if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

# Display the results
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Division: {division}")
print(f"Result: {result}")