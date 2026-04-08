"""
Demonstrates set data type in Python.
"""
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(f"Original set: {my_set}")

# Adding an element to the set
my_set.add(6)
print(f"Set after adding 6: {my_set}")

# Removing an element from the set
my_set.remove(3)
print(f"Set after removing 3: {my_set}")

# Set operations
another_set = {4, 5, 6, 7, 8}
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)
print(f"Union of sets: {union_set}")
print(f"Intersection of sets: {intersection_set}") 

# Looping through the set
for item in my_set:
    print(item)

#accessing set elements 
print(f"Is 4 in the set? {4 in my_set}")

#frozenset (immutable set)
frozen_set = frozenset([1, 2, 3])
print(f"Frozen set: {frozen_set}")