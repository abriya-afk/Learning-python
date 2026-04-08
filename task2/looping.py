"""
for and while loops
"""
# For loop example
print("For loop example:") 
for i in range(5):
    print(f"Iteration {i}")

# While loop example
print("\nWhile loop example:")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

#else clause for loops
print("\nFor loop with else clause:")
for i in range(5):
    print(f"Iteration {i}")
else:
    print("Loop completed without break.")

print("\nWhile loop with else clause:")
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop completed without break.")
