"""
Demonstrates dictionary data type in Python.
"""
# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Original dictionary: {my_dict}")

# Accessing values by key
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict['age']}")

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"
print(f"Dictionary after adding email: {my_dict}")

# Updating an existing value
my_dict["age"] = 31
print(f"Dictionary after updating age: {my_dict}")

# Removing a key-value pair
del my_dict["city"]
print(f"Dictionary after removing city: {my_dict}")

# Looping through the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
print(f"Is 'name' in the dictionary? {'name' in my_dict}")
print(f"Is 'city' in the dictionary? {'city' in my_dict}")