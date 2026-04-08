"""
Demonstrates binary data type in Python.
"""
# Creating a bytes object
my_bytes = b"Hello, World!"
print(f"Original bytes: {my_bytes}")

# Creating a bytearray object
my_bytearray = bytearray([65, 66, 67])
print(f"Original bytearray: {my_bytearray}")

# Accessing elements in bytes and bytearray
print(f"First element in bytes: {my_bytes[0]}")
print(f"First element in bytearray: {my_bytearray[0]}")

# Modifying elements in bytearray (bytes is immutable)
my_bytearray[0] = 68
print(f"Bytearray after modification: {my_bytearray}")