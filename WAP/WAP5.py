"""
5. WAP to input marks in 5 subjects and then calculate total marks, percentage, division and result(pass/fail).
"""

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate total marks
total_marks = sum(marks)  

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