"""
Demonstrates list manipulation in Python.
"""

# Creating a list
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Adding an element to the list
my_list.append(6)
print(f"List after appending 6: {my_list}")

# Removing an element from the list
my_list.remove(3)
print(f"List after removing 3: {my_list}")

# Slicing the list
sliced_list = my_list[1:4]
print(f"Sliced list (index 1 to 3): {sliced_list}")

# List comprehension to create a new list
squared_list = [x**2 for x in my_list]
print(f"Squared list: {squared_list}")

#indexing the list
first_element = my_list[0]
print(f"First element of the list: {first_element}")

# Looping through the list
for item in my_list:
    print(item)

#copying the list
copied_list = my_list.copy()
print(f"Copied list: {copied_list}")

#List sorting
my_list.sort()
print(f"Sorted list: {my_list}")

#joining two lists
another_list = [7, 8, 9]
joined_list = my_list + another_list
print(f"Joined list: {joined_list}")