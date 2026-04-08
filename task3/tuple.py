"""
Demonstrates tuple data type in Python.
"""

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"Original tuple: {my_tuple}")

#updating a tuple (tuples are immutable, so we create a new one)
my_list = list(my_tuple)
my_list.append(6)
my_tuple = tuple(my_list)
print(f"Tuple after appending 6: {my_tuple}")

# indexing the tuple
first_element = my_tuple[0]
print(f"First element of the tuple: {first_element}")

# Slicing the tuple
sliced_tuple = my_tuple[1:4]
print(f"Sliced tuple (index 1 to 3): {sliced_tuple}")

# Joining two tuples
another_tuple = (6, 7, 8)
joinedtuple = my_tuple + another_tuple
print(f"Joined tuple: {joinedtuple}")

# Tuple unpacking
a, b, c, d, e = my_tuple
print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}")

# Looping through the tuple
for item in my_tuple:
    print(item)
